"""Backtest a P123 screen and print summary statistics.

Purpose: run a historical backtest of a screen and show the port-vs-benchmark
summary stats table. With --rolling, run a rolling backtest instead.

Endpoint(s): POST /screen/backtest, and POST /screen/rolling-backtest with --rolling.
Wrapper method(s): Client.screen_backtest(params, to_pandas=True);
                   Client.screen_rolling_backtest(params, to_pandas=True).

API quota note: responses carry cost and quotaRemaining. The to_pandas=True form
of screen_backtest returns a dict of DataFrames (stats / results / chart) and does
not preserve the raw cost block, so cost is read from a non-pandas probe is avoided
here; rely on quotaRemaining shown by other scripts. (See api.md -> Quotas & Costs.)

Mode: READ-ONLY. Changes no account state.

Usage:
    python 03_screen_backtest.py --universe Prussell3000 --start 2015-01-01 \
        --rule "MktCap > 500" --rule "Close(0) > 5"

    python 03_screen_backtest.py --screen-id 12345 --start 2015-01-01 --rolling
"""

import argparse
import sys

import p123api

from p123_helpers import make_client


def build_screen(args):
    """Return the 'screen' value: a saved id or an inline long-only ScreenParams."""
    if args.screen_id is not None:
        return args.screen_id
    rules = [{"formula": formula} for formula in args.rule]
    screen = {
        "type": "Stock",
        "method": "long",
        "universe": args.universe,
        "rules": rules,
    }
    if args.max_holdings is not None:
        screen["maxNumHoldings"] = args.max_holdings
    return screen


def main():
    parser = argparse.ArgumentParser(description="Backtest a P123 screen (read-only).")
    parser.add_argument("--screen-id", type=int, default=None,
                        help="Backtest a saved screen by id.")
    parser.add_argument("--universe", default="Prussell3000",
                        help="Universe for an inline screen (default: Prussell3000).")
    parser.add_argument("--rule", action="append", default=None,
                        help="A screen rule formula; repeatable. Long-only rules carry no 'type'.")
    parser.add_argument("--max-holdings", type=int, default=None,
                        help="Override maximum number of holdings (0 = all).")
    parser.add_argument("--start", required=True, help="Backtest start date (yyyy-mm-dd).")
    parser.add_argument("--end", default=None, help="Backtest end date (yyyy-mm-dd).")
    parser.add_argument("--rolling", action="store_true",
                        help="Use the rolling backtest endpoint instead of the standard one.")
    args = parser.parse_args()

    if args.screen_id is None and not args.rule:
        args.rule = ["MktCap > 500", "Close(0) > 5"]

    params = {"screen": build_screen(args), "startDt": args.start}
    if args.end:
        params["endDt"] = args.end

    try:
        with make_client() as client:
            if args.rolling:
                frame = client.screen_rolling_backtest(params, to_pandas=True)
                print("Rolling backtest results:")
                print(frame.to_string(index=False))
            else:
                result = client.screen_backtest(params, to_pandas=True)
                # to_pandas=True returns {'stats': df, 'results': df, 'chart': df}.
                print("Summary statistics (screen vs benchmark):")
                print(result["stats"].to_string(index=False))
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

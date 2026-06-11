"""Run a P123 screen by inline definition or by saved screen id.

Purpose: demonstrate screen_run with the post-PR-#6 payload shape. For a
long-only screen the per-rule 'type' field must be omitted (the API rejects it
with "Rule type parameter should not be present"); per-rule 'type' is only valid
for long/short and hedged screens (see api.md -> Known Pitfalls).

Endpoint(s): POST /screen/run.
Wrapper method(s): Client.screen_run(params, to_pandas=True).

API quota note: the response carries cost and quotaRemaining; this script prints
them via print_quota when available (kept on the DataFrame's attrs['raw_obj']).

Mode: READ-ONLY. Changes no account state.

Usage:
    # Inline screen on a universe with a couple of long-only rules:
    python 02_screen_run.py --universe SP500 --rule "MktCap > 1000" --rule "ROE%TTM > 10"

    # Run a saved screen by id:
    python 02_screen_run.py --screen-id 12345

    # Save results to CSV:
    python 02_screen_run.py --universe SP500 --csv out.csv
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota, save_csv


def build_params(args):
    """Build the screen_run params dict.

    Uses the ScreenRunParams schema: top-level 'screen' is either a saved screen
    id (int) or an inline ScreenParams object. The inline form here uses
    method='long', so rule objects contain only 'formula' (no per-rule 'type').
    """
    if args.screen_id is not None:
        # Run an existing saved screen by id.
        params = {"screen": args.screen_id}
    else:
        rules = [{"formula": formula} for formula in args.rule]
        screen = {
            "type": "Stock",
            "method": "long",
            "universe": args.universe,
            "rules": rules,
        }
        if args.max_holdings is not None:
            screen["maxNumHoldings"] = args.max_holdings
        params = {"screen": screen}

    if args.as_of_dt:
        params["asOfDt"] = args.as_of_dt
    return params


def main():
    parser = argparse.ArgumentParser(description="Run a P123 screen (read-only).")
    parser.add_argument("--screen-id", type=int, default=None,
                        help="Run a saved screen by id instead of an inline definition.")
    parser.add_argument("--universe", default="SP500",
                        help="Universe name for an inline screen (default: SP500).")
    parser.add_argument("--rule", action="append", default=None,
                        help="A screen rule formula; repeatable. Long-only rules carry no 'type'.")
    parser.add_argument("--max-holdings", type=int, default=None,
                        help="Override maximum number of holdings (0 = all).")
    parser.add_argument("--as-of-dt", default=None,
                        help="As-of date (yyyy-mm-dd); defaults to today server-side.")
    parser.add_argument("--csv", default=None, help="Save the results to this CSV path.")
    args = parser.parse_args()

    # Provide a sensible default rule set for the inline path.
    if args.screen_id is None and not args.rule:
        args.rule = ["MktCap > 1000"]

    params = build_params(args)

    try:
        with make_client() as client:
            frame = client.screen_run(params, to_pandas=True)
            print_quota(frame)
            print(frame.to_string(index=False))
            if args.csv:
                save_csv(frame, args.csv)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

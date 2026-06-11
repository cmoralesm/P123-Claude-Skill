"""Download end-of-day price history for one security.

Purpose: fetch OHLCV bars for a ticker or P123 UID over a date range. Defaults to
IBM, which the spec lists among the free-trial tickers (IBM, MSFT, INTC) usable
without a data license.

Endpoint(s): GET /data/prices/{identifier}.
Wrapper method(s): Client.data_prices(identifier, start, end, to_pandas=True).

API quota note: the response carries cost and quotaRemaining; this script prints
them via print_quota (kept on the DataFrame's attrs['raw_obj'] where available;
the bars themselves are returned under 'prices'). (See api.md -> Quotas & Costs.)

Mode: READ-ONLY. Changes no account state.

Usage:
    python 07_price_history.py
    python 07_price_history.py --identifier MSFT --start 2024-01-01 --end 2024-12-31 \
        --csv msft.csv
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, save_csv


def main():
    parser = argparse.ArgumentParser(description="Download EOD price history (read-only).")
    parser.add_argument("--identifier", default="IBM",
                        help="Ticker or P123 UID (default: IBM, a free-trial ticker).")
    parser.add_argument("--start", default="2020-01-01", help="Start date (yyyy-mm-dd).")
    parser.add_argument("--end", default=None,
                        help="End date (yyyy-mm-dd); omit for through-today.")
    parser.add_argument("--csv", default=None, help="Save the price bars to this CSV path.")
    args = parser.parse_args()

    try:
        with make_client() as client:
            # 'end' is optional in the wrapper; None means through today.
            frame = client.data_prices(args.identifier, args.start, args.end, to_pandas=True)
            print(frame.head(20).to_string(index=False))
            print("Rows returned: {}".format(len(frame)))
            if args.csv:
                save_csv(frame, args.csv)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

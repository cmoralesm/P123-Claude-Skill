"""Download end-of-day price history for one security.

Purpose: fetch OHLCV bars for a ticker or P123 UID over a date range. Defaults to
IBM, one of the three tickers (IBM, MSFT, INTC) named by the spec's licence waiver.
That waiver is written on POST /data; GET /data/prices/{identifier} carries no
licence clause either way, so do not assume it is usable without a data license.

Endpoint(s): GET /data/prices/{identifier}.
Wrapper method(s): Client.data_prices(identifier, start, end, to_pandas=True).

API quota note: the response carries cost and quotaRemaining, but data_prices'
to_pandas path returns a bare DataFrame of the 'prices' array and keeps no
attrs['raw_obj'], so this script does not print them. Read them from client.cost /
client.quotaRemaining (p123api 3.1.0+). (See api.md -> Quotas & Costs.)

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
                        help="Ticker or P123 UID (default: IBM, one of the three tickers "
                             "named by the spec's POST /data licence waiver).")
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

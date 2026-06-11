"""Bulk-download point-in-time factor data for a universe.

Purpose: evaluate one or more formulas across a universe as of a date and write
the result to a DataFrame / CSV.

Endpoint(s): POST /data/universe.
Wrapper method(s): Client.data_universe(params, to_pandas=True).

Response format options (from the OpenAPI spec): /data/universe can respond as
application/json, text/csv, or application/parquet. The p123api wrapper requests
JSON and converts to a DataFrame when to_pandas=True; to obtain CSV or Parquet
directly you would call the REST endpoint yourself with the appropriate Accept
header. (See api.md -> Endpoints by Tag -> Data.)

API quota note: the response carries cost and quotaRemaining; this script prints
them via print_quota (kept on the DataFrame's attrs['raw_obj']). The free trial
covers IBM, MSFT, INTC with 5 years of history without a data license.

Mode: READ-ONLY. Changes no account state.

Usage:
    python 06_data_universe_download.py --universe SP500 --as-of-dt 2025-03-08 \
        --formula "PEExclXorTTM" --formula "ROE%TTM" --csv universe.csv
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota, save_csv


def main():
    parser = argparse.ArgumentParser(description="Bulk universe factor download (read-only).")
    parser.add_argument("--universe", default="SP500", help="Universe name (default: SP500).")
    parser.add_argument("--formula", action="append", default=None,
                        help="A P123 formula to evaluate; repeatable.")
    parser.add_argument("--as-of-dt", default=None, help="As-of date (yyyy-mm-dd).")
    parser.add_argument("--csv", default=None, help="Save the data to this CSV path.")
    args = parser.parse_args()

    if not args.formula:
        args.formula = ["PEExclXorTTM", "ROE%TTM"]

    params = {
        "universe": args.universe,
        "formulas": args.formula,
        "includeNames": True,
    }
    if args.as_of_dt:
        params["asOfDt"] = args.as_of_dt

    try:
        with make_client() as client:
            frame = client.data_universe(params, to_pandas=True)
            print_quota(frame)
            print(frame.head(20).to_string(index=False))
            if args.csv:
                save_csv(frame, args.csv)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

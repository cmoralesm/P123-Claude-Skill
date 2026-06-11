"""Download ranking-system ranks as of a date and save them to CSV.

Purpose: fetch ranks for a universe as of a single date and write a DataFrame to
CSV. Demonstrates the 'nodeDetails' parameter (composite | factor) -- NOT the
deprecated 'includeNodeDetails' (see api.md -> Known Pitfalls).

Endpoint(s): POST /rank/ranks.
Wrapper method(s): Client.rank_ranks(params, to_pandas=True).

API quota note: the response carries cost and quotaRemaining; this script prints
them via print_quota (kept on the DataFrame's attrs['raw_obj']).
(See api.md -> Quotas & Costs.)

Mode: READ-ONLY. Changes no account state.

Usage:
    python 05_rank_ranks_to_csv.py --ranking "My Ranking System" --as-of-dt 2025-03-08 \
        --universe SP500 --csv ranks.csv

    python 05_rank_ranks_to_csv.py --ranking 12345 --as-of-dt 2025-03-08 \
        --node-details composite
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota, save_csv


def main():
    parser = argparse.ArgumentParser(description="Download ranking-system ranks (read-only).")
    parser.add_argument("--ranking", required=True,
                        help="Ranking system name or numeric id.")
    parser.add_argument("--as-of-dt", required=True, help="As-of date (yyyy-mm-dd).")
    parser.add_argument("--universe", default="SP500", help="Universe name (default: SP500).")
    parser.add_argument("--node-details", choices=["composite", "factor"], default=None,
                        help="Include node-level detail columns (composite or factor).")
    parser.add_argument("--csv", default=None, help="Save the ranks to this CSV path.")
    args = parser.parse_args()

    ranking = args.ranking
    try:
        ranking = int(ranking)
    except ValueError:
        pass

    params = {
        "rankingSystem": ranking,
        "asOfDt": args.as_of_dt,
        "universe": args.universe,
        "includeNames": True,
    }
    # Use the current 'nodeDetails' enum, not the deprecated 'includeNodeDetails'.
    if args.node_details:
        params["nodeDetails"] = args.node_details

    try:
        with make_client() as client:
            frame = client.rank_ranks(params, to_pandas=True)
            print_quota(frame)
            print(frame.head(20).to_string(index=False))
            if args.csv:
                save_csv(frame, args.csv)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

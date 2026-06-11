"""Bucket performance test for a saved ranking system.

Purpose: run rank_perf for a ranking system id (or name) and print the per-bucket
annualized returns alongside the benchmark.

Endpoint(s): POST /rank/performance.
Wrapper method(s): Client.rank_perf(params).

API quota note: the response carries cost and quotaRemaining; this script prints
them via print_quota. (See api.md -> Quotas & Costs.)

Mode: READ-ONLY. Changes no account state.

Usage:
    python 04_rank_performance.py --ranking "My Ranking System" --start 2010-01-01
    python 04_rank_performance.py --ranking 12345 --start 2010-01-01 --buckets 10 \
        --universe Prussell3000
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota


def main():
    parser = argparse.ArgumentParser(description="Ranking-system bucket performance (read-only).")
    parser.add_argument("--ranking", required=True,
                        help="Ranking system name or numeric id.")
    parser.add_argument("--start", required=True, help="Start date (yyyy-mm-dd).")
    parser.add_argument("--end", default=None, help="End date (yyyy-mm-dd).")
    parser.add_argument("--universe", default=None, help="Universe name (optional).")
    parser.add_argument("--buckets", type=int, default=None,
                        help="Number of rank buckets (2-200, default 20).")
    parser.add_argument("--benchmark", default=None, help="Benchmark ticker (default SPY).")
    args = parser.parse_args()

    # rankingSystem accepts a name or an id; pass the int when it parses as one.
    ranking = args.ranking
    try:
        ranking = int(ranking)
    except ValueError:
        pass

    params = {"rankingSystem": ranking, "startDt": args.start}
    if args.end:
        params["endDt"] = args.end
    if args.universe:
        params["universe"] = args.universe
    if args.buckets is not None:
        params["numBuckets"] = args.buckets
    if args.benchmark:
        params["benchmark"] = args.benchmark

    try:
        with make_client() as client:
            result = client.rank_perf(params)
            print_quota(result)
            benchmark_ann = result.get("benchmarkAnnRet")
            buckets = result.get("bucketAnnRet")
            if buckets is not None:
                print("Benchmark annualized return: {}".format(benchmark_ann))
                print("Bucket annualized returns (low rank -> high rank):")
                for idx, value in enumerate(buckets, 1):
                    print("  bucket {}: {}".format(idx, value))
            else:
                # outputType 'perf' returns series instead of annualized buckets.
                print(result)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

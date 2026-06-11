"""Get strategy rebalance recommendations, and (only with --execute) commit them.

Purpose: the flagship safety example. By default this is a DRY RUN: it fetches
rebalance recommendations and prints the proposed transactions WITHOUT changing
anything. Committing the orders requires the explicit --execute flag AND a typed
confirmation.

Endpoint(s):
  POST /strategy/{id}/rebalance         (read-only, recommendations)
  POST /strategy/{id}/rebalance/commit  (MUTATING, only with --execute)
Wrapper method(s):
  Client.strategy_rebalance(strategy_id, params)         -> recommendations
  Client.strategy_rebalance_commit(strategy_id, params)  -> commits orders

API quota note: both responses carry cost and quotaRemaining; this script prints
them via print_quota. (See api.md -> Quotas & Costs.)

Mode: MUTATING (gated). The default path is read-only. The commit path runs only
behind --execute and a typed "COMMIT" confirmation. Build Ground Rule 5: mutating
operations are never executed automatically.

The rebalance response returns 'op' and 'ranks' that must be forwarded to the
commit endpoint UNALTERED (required for Live Strategy rebalances); this script
echoes them back as-is.

Usage:
    # Dry run (safe; prints recommendations only):
    python 09_strategy_rebalance_dryrun.py --strategy-id 12345

    # Commit the recommended transactions (asks for typed confirmation):
    python 09_strategy_rebalance_dryrun.py --strategy-id 12345 --execute
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota


def print_recommendations(recs):
    """Print the rebalance recommendation list in a readable form."""
    if not recs:
        print("No rebalance recommendations returned.")
        return
    print("Proposed transactions ({}):".format(len(recs)))
    for rec in recs:
        print("  {action:<5} {ticker:<12} shares={shares} price={price}".format(
            action=rec.get("action", "?"),
            ticker=rec.get("ticker", "?"),
            shares=rec.get("shares"),
            price=rec.get("price"),
        ))


def build_commit_trans(recs):
    """Map rebalance recommendations to RebalanceTran objects for commit.

    RebalanceTran requires p123Uid, action, price, shares (comm/slip/note optional).
    """
    trans = []
    for rec in recs:
        tran = {
            "p123Uid": rec["p123Uid"],
            "action": rec["action"],
            "price": rec["price"],
            "shares": rec["shares"],
        }
        for src, dst in (("comm", "comm"), ("slip", "slip"), ("note", "note")):
            if rec.get(src) is not None:
                tran[dst] = rec[src]
        trans.append(tran)
    return trans


def main():
    parser = argparse.ArgumentParser(
        description="Strategy rebalance: dry run by default; commit only with --execute.")
    parser.add_argument("--strategy-id", type=int, required=True,
                        help="ID of the strategy/book to rebalance.")
    parser.add_argument("--execute", action="store_true",
                        help="Commit the recommended transactions (MUTATING). "
                             "Without this flag the script only prints recommendations.")
    args = parser.parse_args()

    try:
        with make_client() as client:
            # Step 1 (always): fetch recommendations. This does not change state.
            result = client.strategy_rebalance(args.strategy_id, {})
            print_quota(result)
            recs = result.get("recs", [])
            print_recommendations(recs)

            if not args.execute:
                print("\nDRY RUN: no transactions were committed. "
                      "Re-run with --execute to commit.")
                return

            if not recs:
                print("\nNothing to commit.")
                return

            # Step 2 (only with --execute): require an explicit typed confirmation.
            print("\n--execute supplied. This will COMMIT the transactions above "
                  "to strategy {} and CHANGE ACCOUNT STATE.".format(args.strategy_id))
            confirm = input('Type COMMIT to proceed (anything else aborts): ').strip()
            if confirm != "COMMIT":
                print("Aborted. No transactions were committed.")
                return

            commit_params = {"trans": build_commit_trans(recs)}
            # Forward op and ranks unaltered when present (required for Live Strategy).
            if "op" in result:
                commit_params["op"] = result["op"]
            if "ranks" in result:
                commit_params["ranks"] = result["ranks"]

            commit_result = client.strategy_rebalance_commit(args.strategy_id, commit_params)
            print_quota(commit_result)
            print("Committed {} transaction(s).".format(len(commit_params["trans"])))
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

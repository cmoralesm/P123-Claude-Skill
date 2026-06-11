"""Retrieve AI Factor predictions for a trained predictor.

Purpose: fetch model predictions for every stock in a predictor's universe, with
optional company names and the transformed feature matrix, and write to CSV.

Endpoint(s): POST /aiFactor/predict/{id}.
Wrapper method(s): Client.aifactor_predict(predictor_id, params={}, to_pandas=True).

API quota note: the OpenAPI spec example shows cost: 1, but the live-tested AI
Factor reference reports a fixed 20 credits per call regardless of params or
universe size. This discrepancy is documented in api.md -> AI Factor and is being
confirmed live by the orchestrator. Always read quotaRemaining from the response.

Historical predictions: pass --as-of-dt, which MUST be a Saturday (the server
rejects any other day with "asOfDt must be a Saturday if specified"). Current
calls return priceDt/updateDt; historical calls return dt only.

Mode: READ-ONLY. Changes no account state. (Training and configuration are UI-only;
the API has no mutating AI Factor operations.)

Usage:
    python 08_aifactor_predict.py --predictor-id 123456
    python 08_aifactor_predict.py --predictor-id 123456 --names --features --csv preds.csv
    python 08_aifactor_predict.py --predictor-id 123456 --as-of-dt 2026-03-14
"""

import argparse
import sys

import p123api

from p123_helpers import make_client, print_quota, save_csv


def main():
    parser = argparse.ArgumentParser(description="AI Factor predictions (read-only).")
    parser.add_argument("--predictor-id", type=int, required=True,
                        help="Numeric id of the trained predictor (from the P123 UI).")
    parser.add_argument("--as-of-dt", default=None,
                        help="Historical date (yyyy-mm-dd); MUST be a Saturday.")
    parser.add_argument("--names", action="store_true",
                        help="Include company names (includeNames).")
    parser.add_argument("--features", action="store_true",
                        help="Include feature names and transformed values (includeFeatures).")
    parser.add_argument("--precision", type=int, default=None,
                        help="Decimal precision for predictions (2-6).")
    parser.add_argument("--csv", default=None, help="Save predictions to this CSV path.")
    args = parser.parse_args()

    params = {}
    if args.as_of_dt:
        params["asOfDt"] = args.as_of_dt
    if args.names:
        params["includeNames"] = True
    if args.features:
        params["includeFeatures"] = True
    if args.precision is not None:
        params["precision"] = args.precision

    try:
        with make_client() as client:
            frame = client.aifactor_predict(args.predictor_id, params, to_pandas=True)
            print_quota(frame)
            # Predictions can be null for ~3-4% of the universe; surface that.
            if "prediction" in frame.columns:
                null_count = int(frame["prediction"].isna().sum())
                print("Rows: {} ({} with null prediction)".format(len(frame), null_count))
            print(frame.head(20).to_string(index=False))
            if args.csv:
                save_csv(frame, args.csv)
    except p123api.ClientException as exc:
        print("API error: {}".format(exc), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

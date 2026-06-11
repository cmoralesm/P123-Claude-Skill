# Portfolio123 API Example Scripts

Nine runnable Python examples covering the core Portfolio123 API workflows with the
official `p123api` wrapper. They are teaching examples first, utilities second:
short, heavily commented, and safe by default. For the full endpoint and parameter
reference see [`../references/api.md`](../references/api.md).

## The scripts

| # | File | Wrapper call(s) | Mode | What it does |
|---|---|---|---|---|
| 0 | `p123_helpers.py` | — | library | Loads credentials from env, builds the client, prints `cost`/`quotaRemaining`, saves CSV. |
| 1 | `01_auth_check.py` | `auth()`, `get_api_id()`, `get_token()` | read-only | Verifies credentials and confirms a token was obtained. |
| 2 | `02_screen_run.py` | `screen_run(..., to_pandas=True)` | read-only | Runs a screen by inline definition or `--screen-id`; uses the post-PR-#6 payload (no per-rule `type` for long-only). |
| 3 | `03_screen_backtest.py` | `screen_backtest`, `screen_rolling_backtest` (`--rolling`) | read-only | Backtests a screen and prints summary stats. |
| 4 | `04_rank_performance.py` | `rank_perf` | read-only | Bucket performance for a saved ranking system. |
| 5 | `05_rank_ranks_to_csv.py` | `rank_ranks(..., to_pandas=True)` | read-only | Ranks as of a date to a DataFrame/CSV; uses `nodeDetails` (not the deprecated `includeNodeDetails`). |
| 6 | `06_data_universe_download.py` | `data_universe(..., to_pandas=True)` | read-only | Bulk factor download; documents the JSON/CSV/Parquet response options. |
| 7 | `07_price_history.py` | `data_prices` | read-only | EOD prices; defaults to IBM (works on the free trial). |
| 8 | `08_aifactor_predict.py` | `aifactor_predict(..., to_pandas=True)` | read-only | AI Factor predictions for a predictor id; notes the cost discrepancy and Saturday `asOfDt` rule. |
| 9 | `09_strategy_rebalance_dryrun.py` | `strategy_rebalance`; `strategy_rebalance_commit` (only with `--execute`) | mutating (gated) | Dry-run prints rebalance recommendations; `--execute` asks for typed confirmation before committing. |

Every script prints `--help` text. Read-only scripts that produce tabular output
accept `--csv <path>` to save the result.

## Setup

1. Install the wrapper (and its dependencies, pandas + requests):

   ```bash
   pip install p123api
   ```

2. Export your API credentials as environment variables. API keys are created in
   P123 under Account Settings -> API; a paying subscription is required.

   ```bash
   export P123_API_ID=your_api_id
   export P123_API_KEY=your_api_key
   ```

   On Windows PowerShell:

   ```powershell
   $env:P123_API_ID = "your_api_id"
   $env:P123_API_KEY = "your_api_key"
   ```

   Credentials are read only from these variables. They are never hardcoded and
   never printed.

3. Run a script from this directory, for example:

   ```bash
   python 01_auth_check.py
   python 07_price_history.py --identifier IBM --start 2024-01-01
   ```

## Quotas and costs

Most API responses include two fields from the `SharedResult` schema:

- `cost` — credits the call consumed.
- `quotaRemaining` — credits left in your current billing period.

The scripts print these via `print_quota` when present. Do not assume a fixed
price: real cost depends on the data volume returned. The quota is shared across
all operations (data, screening, backtesting, AI Factor), and the API allows only
one in-flight request per key. The AI Factor per-call cost is unsettled between
sources (spec example shows `1`; the live-tested reference reports `20`) — see
[`../references/api.md`](../references/api.md) (AI Factor). The free trial covers
IBM, MSFT, and INTC with 5 years of history on `data` and `data/universe` without a
data license.

## Safety model

- **Read-only scripts (1-8)** never change account state. They retrieve data,
  ranks, prices, backtests, or predictions.
- **The mutating script (9)** is gated. By default it is a dry run that prints
  rebalance recommendations only. Committing orders requires both the `--execute`
  flag and a typed `COMMIT` confirmation. This follows the build rule that mutating
  operations are never executed automatically.
- All calls are wrapped in `try/except p123api.ClientException`, so API errors
  print a clear message and exit non-zero rather than raising a traceback.

<!-- name-whitelist:
quotaRemaining SharedResult nodeDetails includeNodeDetails asOfDt COMMIT
-->
# Portfolio123 API Example Scripts

Nine runnable Python examples covering the core Portfolio123 API workflows with the
official `p123api` wrapper. They are teaching examples first, utilities second:
short, heavily commented, and safe by default. For the full endpoint and parameter
reference see [`../references/api.md`](../references/api.md).

**Wrapper version.** All nine were audited against `p123api` **3.1.0** (Python 3.10+).
None of them calls one of the nine methods that return typed objects instead of dicts
in 3.x, and no kwarg they pass was renamed, so the call sites are unchanged from the
2.x-era version. What 3.x changes here is the install line below and where the
cost and quota figures are read from. On a 2.x pin they still run; see
[`../references/api.md`](../references/api.md) -> Migrating from p123api 2.x.

## The scripts

| # | File | Wrapper call(s) | Mode | What it does |
|---|---|---|---|---|
| 0 | `p123_helpers.py` | - | library | Loads credentials from env, builds the client, prints `cost`/`quotaRemaining`, saves CSV. |
| 1 | `01_auth_check.py` | `auth()`, `get_api_id()`, `get_token()` | read-only | Verifies credentials and confirms a token was obtained. |
| 2 | `02_screen_run.py` | `screen_run(..., to_pandas=True)` | read-only | Runs a screen by inline definition or `--screen-id`; uses the post-PR-#6 payload (no per-rule `type` for long-only). |
| 3 | `03_screen_backtest.py` | `screen_backtest`, `screen_rolling_backtest` (`--rolling`) | read-only | Backtests a screen and prints summary stats. |
| 4 | `04_rank_performance.py` | `rank_perf` | read-only | Bucket performance for a saved ranking system. |
| 5 | `05_rank_ranks_to_csv.py` | `rank_ranks(..., to_pandas=True)` | read-only | Ranks as of a date to a DataFrame/CSV; uses `nodeDetails` (not the deprecated `includeNodeDetails`). |
| 6 | `06_data_universe_download.py` | `data_universe(..., to_pandas=True)` | read-only | Bulk factor download; documents the JSON/CSV/Parquet response options. |
| 7 | `07_price_history.py` | `data_prices` | read-only | EOD prices; defaults to IBM, one of the three tickers the spec's `data` waiver names. |
| 8 | `08_aifactor_predict.py` | `aifactor_predict(..., to_pandas=True)` | read-only | AI Factor predictions for a predictor id; notes the cost discrepancy and Saturday `asOfDt` rule. |
| 9 | `09_strategy_rebalance_dryrun.py` | `strategy_rebalance`; `strategy_rebalance_commit` (only with `--execute`) | mutating (gated) | Dry-run prints rebalance recommendations; `--execute` asks for typed confirmation before committing. |

Every script prints `--help` text. Read-only scripts that produce tabular output
accept `--csv <path>` to save the result.

## Setup

1. Install the wrapper. These scripts target **`p123api` 3.1.0**, which requires
   **Python 3.10+**. Install it *with the `pandas` extra* - since p123api 3.0 pandas
   is optional and the wrapper imports it lazily, so without the extra every
   `to_pandas=True` script below fails at call time, not at import:

   ```bash
   pip install "p123api[pandas]"
   ```

   Runtime dependencies are `requests` and `typing_extensions`; `pandas` comes only
   from the extra. On `p123api` 2.x, `pip install p123api` pulled pandas in
   automatically - that change is the one install-level break in the 2.x to 3.x
   upgrade. The failure it causes is `ModuleNotFoundError: No module named 'pandas'`
   raised from inside the wrapper, which the scripts' `except
   p123api.ClientException` does not catch.

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

- `cost` - credits the call consumed.
- `quotaRemaining` - credits left in your current billing period.

The scripts print these via `print_quota`, which looks in the dict response first,
then at `frame.attrs['raw_obj']`, then at `client.cost` / `client.quotaRemaining` -
instance attributes added in `p123api` 3.1.0 and set after every successful request.
The third source is the only one that works for `screen_run`, `screen_backtest`,
`aifactor_predict`, `data_prices` and `data_universe` with `--as-of-dt`, none of
which keeps a usable raw object after the DataFrame conversion. Do not assume a fixed
price: real cost depends on the data volume returned. The quota is shared across
all operations (data, screening, backtesting, AI Factor), and the API allows only
one in-flight request per key. The AI Factor per-call cost is unsettled between
sources (spec example shows `1`; the live-tested reference reports `20`) - see
[`../references/api.md`](../references/api.md) (AI Factor). The spec's licence waiver
covers `data` only - IBM, MSFT, and INTC with 5 years of history without a data
license. `data/universe` carries no such clause and needs a data license.

## Safety model

- **Read-only scripts (1-8)** never change account state. They retrieve data,
  ranks, prices, backtests, or predictions.
- **The mutating script (9)** is gated. By default it is a dry run that prints
  rebalance recommendations only. Committing orders requires both the `--execute`
  flag and a typed `COMMIT` confirmation. This follows the build rule that mutating
  operations are never executed automatically.
- All calls are wrapped in `try/except p123api.ClientException`, so API errors
  print a clear message and exit non-zero rather than raising a traceback.

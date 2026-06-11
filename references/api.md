<!-- name-whitelist:
api_id api_key apiId apiKey to_pandas predictor_id strategy_id factor_id series_id rank_id
get_api_id get_token set_timeout set_max_request_retries rank_touch auth close
screen_run screen_backtest screen_rolling_backtest data data_universe data_prices
rank_ranks rank_perf rank_update universe_update strategy strategy_holdings
strategy_rebalance strategy_rebalance_commit strategy_transactions strategy_transaction_import
strategy_transaction_delete strategy_rerun strategy_trading_system strategy_trading_system_update
book_rerun book_trading_system_update aifactor_predict stock_factor_create_update
stock_factor_upload stock_factor_download stock_factor_delete stock_factor_info
data_series_create_update data_series_upload data_series_delete ClientException Client
startDt endDt asOfDt asOfDts pitMethod rankingSystem rankingMethod numBuckets rebalFreq
maxNAs minPrice minLiquidity maxReturn transType outputType benchmark slippage
maxNumHoldings lowerIsBetter includeNames includeNaCnt includeFinalStmt includeNodeDetails
nodeDetails additionalData currency precision frequency holdingPeriod transPrice maxPosPct
longWeight shortWeight rankTolerance carryCost riskStatsPeriod ignoreErrors region
quotaRemaining p123Uids p123Uid tickers gvkeys ciks figis figi startingUniverse
includeFeatures updateExisting makeRebalDtCurr content_type column_separator existing_data
date_format decimal_separator ignore_errors ignore_duplicates contains_header_row
columnSeparator existingData dateFormat decimalSeparator onError onDuplicates headerRow
minRebalTran saveTrans posWeight numPos reconFreq sizingMethod useMargin buyRules sellRules
dataSeriesId factorId processedTransactions tranId transId orderUid settleDt limitPrice
mktUid avgShareCost daysHeld benchmarkId rankingSystemId reconPeriod rebalPeriod rebalMode
SPTSX SPTSX60 EU600 EU200L EU200M EU200S TRADEUSA TRADEEUR TRADENOAM TRADENOAT NanoCap
ALLFUNDCAN PRIMARYCAN ALLSTOCKSCAN ALLFUNDEUR PRIMARYEUR PRIMARYNOAM PRIMARYNOAT PRIMARYUSA
ALLFUNDCDRCAD CanadaTrust priceDt updateDt rawData includeRawData ApiRankingSystem
RebalOp Recon ReconRebal Rebal DataParams DataUniverseParams ScreenRunParams ScreenParams
ScreenRuleParams RankRanksParams RankPerfParams RebalanceParams RebalanceCommitParams
PredictParams SharedResult AuthParams AccessToken StrategyTran RebalanceTran UniverseParams
DYNAMIC STATIC STATIC_OLD pip py
ENDPOINT Authorization PredictResult Canada Europe Complete Prelim ApiUniverse Stock ETF
PricesResult DataSeriesParams RankParams SPY RankPerfRetResult bucketAnnRet RankPerfDetailedResult
naCnt finalStmt ScreenByIdParams ScreenBacktestParams Monthly Weekly Daily
ScreenRollingBacktestParams ScreenBacktest StockFactorParams dailyPerf StrategyPortHolding
StrategyTradingSystemParams BookTradingSystemParams itemUid relativeWeight SimRerunParams
BookSimRerunParams RebalanceOutput BUY COVER SELL SHORT None KeyError
-->
# API — Portfolio123 REST API & p123api Python Wrapper

This file documents the Portfolio123 REST API and the official `p123api` Python wrapper.
"API" is not one of the 13 categories of the P123 Factor Reference; for the formula language and
factor/function names used inside API requests, see the category files
([technical.md](technical.md), [ratios-statistics.md](ratios-statistics.md),
[financials.md](financials.md), and the ranking XML rules in
[ranking-system-xml.md](ranking-system-xml.md)).

Sources: OpenAPI 3.1.0 spec `api-docs.yml` (28 paths / 33 operations / 9 tags / 102 schemas),
verified content-identical to `https://api.portfolio123.com/docs/api-docs.yml`; the official
`p123api` wrapper (version 2.3.0 at build time; install `p123api>=2.2.0`), all 38 public client
methods; plus curated content re-verified against both. Extracted 2026-06-09.

## Contents

- [Authentication](#authentication)
- [Quotas & Costs](#quotas--costs)
- [Endpoints by Tag](#endpoints-by-tag)
  - [Authenticate](#authenticate)
  - [AI Factor (tag)](#ai-factor-tag)
  - [Data](#data)
  - [Data Series](#data-series)
  - [Rank](#rank)
  - [Screen](#screen)
  - [Stock Factor](#stock-factor)
  - [Strategy](#strategy)
  - [Universe](#universe)
- [Wrapper Method Map](#wrapper-method-map)
- [AI Factor](#ai-factor)
- [Known Pitfalls](#known-pitfalls)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Authentication

Base URL: `https://api.portfolio123.com`. The OpenAPI spec has **no `servers` block** — the base
URL is established only in the wrapper source (`ENDPOINT`), so a raw spec reader will not find it.

Auth is `POST /auth` with a JSON body `{apiId, apiKey}`. On success the response is the access
token as `text/plain`; the token lifetime in seconds is returned in the **`X-Expires-In`** response
header (not in the body). Authenticated requests pass the token in a `token` header. Note: the
`token` parameter is stored under `components/schemas` (as `AccessToken`), not under
`components/parameters` — a spec quirk.

**apiId int-vs-string inconsistency.** The spec types `AuthParams.apiId` as `integer`
(`format: int32`), but the wrapper requires both `api_id` and `api_key` to be **non-empty strings**
and raises `ClientException` otherwise. Always pass strings to the wrapper. This is a genuine
spec/client disagreement; the wrapper is the production truth.

**Auto re-authentication.** You normally never call `auth()` yourself. Every request first checks
whether the `Authorization` header is set and re-authenticates on a `401`/`403`, so an expired
token is refreshed transparently. The wrapper retries failed requests up to 5 times by default
(settable 1–10 via `set_max_request_retries`) and uses a 300-second timeout (settable via
`set_timeout`).

Documented `/auth` error codes:

| Code | Meaning (wrapper message) |
|---|---|
| 400 | Missing or invalid request body / invalid key |
| 401 | Invalid API id/key combination or API key inactive |
| 402 | Paying subscription required |
| 406 | User account inactive |
| 503 | Under maintenance |

```python
import p123api

# Context manager is the officially documented pattern.
with p123api.Client(api_id='your api id', api_key='your api key') as client:
    try:
        print(client.get_api_id())   # echoes the configured apiId
        print(client.get_token())    # None until the first request authenticates
    except p123api.ClientException as e:
        print(e)
```

## Quotas & Costs

Every data-returning response includes a `SharedResult` block with two fields:

- `cost` — credits the call consumed.
- `quotaRemaining` — credits left in the current billing period.

Always read these from responses rather than assuming a fixed price; the spec examples show
`cost: 1` for several operations but real cost depends on data volume (e.g., points returned).

**Free trial without a data license.** The spec states that `POST /data` and `POST /data/universe`
can be tried without a license using **IBM, MSFT, and INTC with 5 years of history**. The example
scripts default to these tickers where applicable.

**One request at a time per API key.** The API enforces a single concurrent request per key; a
second simultaneous request fails. The quota is shared across all operations (data, screening,
backtesting, AI Factor), so budget heavy backtesting against AI Factor needs.

## Endpoints by Tag

All 33 operations across the 9 tags. Method + path come from `api-docs.yml`; the wrapper method is
from the `p123api` client. "Key params" lists request fields from the spec request schema (and, for
GET endpoints, query/path parameters).

### Authenticate

**`POST /auth`** — Authenticate. Wrapper: `auth()`.
Body `AuthParams`: `apiId` (spec int32; wrapper string), `apiKey` (string). Returns the token as
`text/plain` plus the `X-Expires-In` header. Errors 400/401/402/406/503 (see Authentication).

### AI Factor (tag)

**`POST /aiFactor/predict/{id}`** — AI Factor Predict. Wrapper: `aifactor_predict(predictor_id, params={}, to_pandas=False)`.
Path `id` = predictor ID (int32). Body `PredictParams` (all optional): `precision` (2–6),
`universe`, `asOfDt` (date), `includeNames`, `includeFeatures`, `figi`
(`Share Class` | `Country Composite`). Response `PredictResult`: `p123Uids`, `tickers`,
`predictions`, optional `names`/`features`/`data`/`figi`, plus `cost`/`quotaRemaining`. See the
[AI Factor](#ai-factor) section for the cost discrepancy and the Saturday-`asOfDt` constraint.

### Data

**`POST /data`** — Get Data. Wrapper: `data(params, to_pandas=False)`.
Body `DataParams`: required `formulas` (array, 100 max) and `startDt` (date). Choose one identifier
set: `tickers`, `p123Uids`, `gvkeys`, `ciks`, or `figis` (each 100 max). Optional: `endDt`,
`frequency` (default `Every Week`), `region` (`United States` default, `Canada`, `North America`,
`Europe`, `North Atlantic`), `pitMethod` (`Complete` default | `Prelim`), `precision` (2–8),
`currency`, `benchmark`, `includeNames`, `ignoreErrors` (default true). Free trial: IBM, MSFT,
INTC, 5Y. Response keyed by `p123Uids`.

**`POST /data/universe`** — Get Universe Data. Wrapper: `data_universe(params, to_pandas=False)`.
Body `DataUniverseParams`: required `formulas` and `universe` (name or id; `ApiUniverse` for a
temporary one). Optional: `type` (`Stock` default | `ETF`), `asOfDt` or `asOfDts`, `figi`,
`precision` (nullable for max precision), `currency`, `benchmark`, `pitMethod`, `includeNames`.
**Response content types:** `application/json`, `text/csv`, or `application/parquet` — the wrapper
returns JSON (or a DataFrame with `to_pandas=True`). Free trial: IBM, MSFT, INTC, 5Y.

**`GET /data/prices/{identifier}`** — Download Security Prices. Wrapper: `data_prices(identifier, start, end, to_pandas=False)`.
Path `identifier` = UID or ticker (no country defaults to `:USA`; numeric is a UID; `955:HKG` style
for explicit country). Query `start` (required, date) and `end` (optional, defaults to today).
Response `PricesResult`: `security` (`p123Uid`, `ticker`) and `prices` (OHLCV bars), plus
`cost`/`quotaRemaining`. Errors include 404 (UID/ticker not found) and 429 (rate limit).

### Data Series

**`POST /dataSeries`** — Data Series Create/Update. Wrapper: `data_series_create_update(params)`.
Body `DataSeriesParams`: required `name`; optional `id` (omit to create), `description`. Returns
`dataSeriesId`.

**`POST /dataSeries/upload/{id}`** — Upload Data Series. Wrapper: `data_series_upload(series_id, data, ...)`.
Path `id`. Request body is `text/csv`. Query options (set by wrapper kwargs): `headerRow`,
`existingData` (`overwrite`/`skip`/`delete`), `dateFormat` (default `yyyy-mm-dd`),
`decimalSeparator` (`.`/`,`), `onError` (`stop`/`continue`), `onDuplicates` (`stop`/`continue`).
Mutating.

**`DELETE /dataSeries/{id}`** — Data Series Deletion. Wrapper: `data_series_delete(series_id)`.
Path `id`. Mutating.

### Rank

**`POST /rank`** — Rank Update. Wrapper: `rank_update(params)`.
Body `RankParams`: required `nodes` (ranking-system XML string) and `type` (`Stock` | `ETF`);
optional `id` (omit to update the `ApiRankingSystem`), `rankingMethod`, `currency`. Mutating.
For the XML schema, see [ranking-system-xml.md](ranking-system-xml.md).

**`POST /rank/performance`** — Rank Performance. Wrapper: `rank_perf(params)`.
Body `RankPerfParams`: required `rankingSystem` (name or id) and `startDt`. Optional: `endDt`,
`universe`, `numBuckets` (2–200, default 20), `rebalFreq` (default `Every 4 Weeks`), `slippage`,
`benchmark` (default `SPY`), `minPrice` (default 3), `minLiquidity`, `maxReturn`, `maxNAs`,
`transType` (`long` default | `short`), `outputType` (`ann` default | `perf`), `pitMethod`,
`precision`, `rankingMethod`. Response is `RankPerfRetResult` (`bucketAnnRet`) or
`RankPerfDetailedResult` (series), depending on `outputType`.

**`POST /rank/ranks`** — Ranks. Wrapper: `rank_ranks(params, to_pandas=False)`.
Body `RankRanksParams`: required `rankingSystem` and `asOfDt`. Optional: `universe`, `tickers`,
`includeNames`, `includeNaCnt`, `includeFinalStmt`, `nodeDetails` (`composite` | `factor`),
`additionalData` (100 max), `currency`, `figi`, `pitMethod`, `precision`, `rankingMethod`.
**Use `nodeDetails`, not the deprecated `includeNodeDetails`** (see Known Pitfalls). Response:
`p123Uids`, `tickers`, `ranks`, optional `nodes`/`naCnt`/`finalStmt`/`additionalData`.

**`POST /rank/{id}/touch`** — Rank Touch. Wrapper: `rank_touch(rank_id)`.
Path `id` = ranking system ID. Invalidates cached ranks. Returns no body.

### Screen

**`POST /screen/run`** — Screen Run. Wrapper: `screen_run(params, to_pandas=False)`.
Body `ScreenRunParams`: required `screen`, which is one of: a screen ID (int), a
`ScreenByIdParams` object (`id`, optional `maxNumHoldings`), or an inline `ScreenParams`. Inline
`ScreenParams`: required `type` (`Stock` | `ETF`); optional `rules` (array of `ScreenRuleParams`),
`method` (`long` default | `short` | `long/short` | `hedged`), `maxNumHoldings`, `benchmark`,
`universe`, `ranking`, `currency`. Each rule: required `formula`; optional per-rule `type`
(`common` | `long` | `short` | `hedge`) **only for `long/short` or `hedged` methods**. Top-level
optional: `asOfDt`, `endDt`, `pitMethod`, `precision`. See Known Pitfalls for the per-rule `type`
fix.

**`POST /screen/backtest`** — Screen Backtest. Wrapper: `screen_backtest(params, to_pandas=False)`.
Body `ScreenBacktestParams`: required `screen` and `startDt`. Optional: `endDt`, `transPrice`
(1 Next Open default, 4 Next Close, 3 Next Avg Hi/Low), `maxPosPct`, `slippage` (default 0.25),
`longWeight`/`shortWeight` (default 100), `rankTolerance`, `carryCost` (default 1.5), `rebalFreq`
(default `Every 4 Weeks`), `riskStatsPeriod` (`Monthly` default | `Weekly` | `Daily`), `pitMethod`,
`precision`.

**`POST /screen/rolling-backtest`** — Screen Rolling Backtest. Wrapper: `screen_rolling_backtest(params, to_pandas=False)`.
Body `ScreenRollingBacktestParams`: the `ScreenBacktest` shared fields plus `frequency`
(`Every Week` default | `Every 4 Weeks`) and `holdingPeriod` (days, 1–730, default 182).

### Stock Factor

**`GET /stockFactor`** — Stock Factor Info. Wrapper: `stock_factor_info(factor_id=None, name=None)`.
Query `id` or `name`. Returns `factorId`, `name`, `description`.

**`POST /stockFactor`** — Stock Factor Create/Update. Wrapper: `stock_factor_create_update(params)`.
Body `StockFactorParams`: required `name`; optional `id` (omit to create), `description`. Returns
`factorId`. Mutating.

**`GET /stockFactor/{id}`** — Stock Factor Download. Wrapper: `stock_factor_download(factor_id)`.
Path `id`. Returns `dates`, `tickers`, `values`, `p123Uids`.

**`DELETE /stockFactor/{id}`** — Stock Factor Deletion. Wrapper: `stock_factor_delete(factor_id)`.
Path `id`. Mutating.

**`POST /stockFactor/upload/{id}`** — Upload Stock Factor Data. Wrapper: `stock_factor_upload(factor_id, data, ...)`.
Path `id`. Body `text/csv`. Query options (wrapper kwargs): `columnSeparator`
(`comma`/`semicolon`/`tab`), `existingData`, `dateFormat`, `decimalSeparator`, `onError`,
`onDuplicates`. Mutating.

### Strategy

**`GET /strategy/{id}`** — Strategy Details. Wrapper: `strategy(strategy_id)`.
Path `id` = strategy/book ID. Returns `summary`, `stats`, `dailyPerf` (plus `cost`/`quotaRemaining`).

**`GET /strategy/{id}/holdings`** — Historical Holdings. Wrapper: `strategy_holdings(strategy_id, date=None, to_pandas=False)`.
Path `id`; query `date` (defaults to today). Returns `holdings` (array of `StrategyPortHolding`).

**`GET /strategy/{id}/trading-system`** — Strategy Trading System. Wrapper: `strategy_trading_system(strategy_id)`.
Path `id`. Returns the live/simulated strategy or book trading system definition.

**`POST /strategy/{id}/trading-system`** — Live Strategy Trading System Update. Wrapper: `strategy_trading_system_update(strategy_id, params)`.
Path `id`. Body `StrategyTradingSystemParams` (`useMargin`, `universe`, `rankingSystem`,
`rankingMethod`, `buyRules`, `sellRules`, `rebalance`). Mutating.

**`POST /strategy/{id}/book-trading-system`** — Live Book Trading System Update. Wrapper: `book_trading_system_update(strategy_id, params)`.
Path `id`. Body `BookTradingSystemParams` (`assets`: `itemUid`, `type`, `relativeWeight`). Mutating.

**`POST /strategy/{id}/rerun`** — Simulation Rerun. Wrapper: `strategy_rerun(strategy_id, params)`.
Path `id`. Body `SimRerunParams`: trading-system fields plus required `startDt`/`endDt` and
optional `saveTrans`. Mutating when `saveTrans` is set.

**`POST /strategy/{id}/book-rerun`** — Book Simulation Rerun. Wrapper: `book_rerun(strategy_id, params)`.
Path `id`. Body `BookSimRerunParams`: `assets`, required `startDt`/`endDt`.

**`GET /strategy/{id}/transactions`** — Get Strategy Transactions. Wrapper: `strategy_transactions(strategy_id, start, end, to_pandas=False)`.
Path `id`; query `start` and `end` (both required dates). Returns `trans` (array of `StrategyTran`).

**`POST /strategy/{id}/transactions`** — Strategy Transaction Import. Wrapper: `strategy_transaction_import(strategy_id, data, content_type='text/csv', update_existing=False, make_rebal_dt_curr=False)`.
Path `id`. Body `text/csv` or `text/tsv`. Columns in order: date, ticker, type, shares, price,
commission, notes. Type is one of BUY, SELL, COVER, SHORT, DIV, SPLIT, CASH. Query
`updateExisting`, `makeRebalDtCurr`. Mutating.

**`DELETE /strategy/{id}/transactions`** — Strategy Transaction Delete. Wrapper: `strategy_transaction_delete(strategy_id, params)`.
Path `id`. Body is a JSON array of transaction IDs (integers). Mutating.

**`POST /strategy/{id}/rebalance`** — Rebalance. Wrapper: `strategy_rebalance(strategy_id, params)`.
Path `id`. Body `RebalanceParams` (all optional): `pitMethod`, `op` (`Rebal` | `Recon` |
`ReconRebal`, for Dynamic Weight Live Strategies; otherwise auto-assigned), `reject` (P123 UIDs to
suppress), `figi`, `minRebalTran` (Live Book only). Returns `RebalanceOutput`: `recs`, plus `op`
and `ranks` to be forwarded **unaltered** to the commit endpoint. Read-only (recommendations only).

**`POST /strategy/{id}/rebalance/commit`** — Rebalance Commit. Wrapper: `strategy_rebalance_commit(strategy_id, params)`.
Path `id`. Body `RebalanceCommitParams`: required `trans` (array of `RebalanceTran`: `p123Uid`,
`action` `BUY`/`COVER`/`SELL`/`SHORT`, `price`, `shares`, optional `comm`/`slip`/`note`); optional
`op` and `ranks` (echo what `rebalance` returned; `ranks` required for Live Strategy). **Mutating —
this commits orders to the strategy.**

### Universe

**`POST /universe`** — Universe Update. Wrapper: `universe_update(params)`.
Body `UniverseParams`: required `type` (`Stock` | `ETF`) and `rules` (array of formula strings);
optional `startingUniverse`, `currency`. Updates the `ApiUniverse` (or a named one). Then reference
`'universe': 'ApiUniverse'` in other calls. Mutating.

## Wrapper Method Map

All 38 public methods on the `p123api.Client` (GitHub master, generated programmatically at build
time — `public_method_count: 38`). The "to_pandas" column marks the 10 methods that accept
`to_pandas=True` and can return a DataFrame.

| Wrapper method | Operation (method + path) | to_pandas |
|---|---|---|
| `auth()` | `POST /auth` | — |
| `aifactor_predict(predictor_id, params, to_pandas)` | `POST /aiFactor/predict/{id}` | yes |
| `data(params, to_pandas)` | `POST /data` | yes |
| `data_universe(params, to_pandas)` | `POST /data/universe` | yes |
| `data_prices(identifier, start, end, to_pandas)` | `GET /data/prices/{identifier}` | yes |
| `data_series_create_update(params)` | `POST /dataSeries` | — |
| `data_series_upload(series_id, data, ...)` | `POST /dataSeries/upload/{id}` | — |
| `data_series_delete(series_id)` | `DELETE /dataSeries/{id}` | — |
| `rank_update(params)` | `POST /rank` | — |
| `rank_perf(params)` | `POST /rank/performance` | — |
| `rank_ranks(params, to_pandas)` | `POST /rank/ranks` | yes |
| `rank_touch(rank_id)` | `POST /rank/{id}/touch` | — |
| `screen_run(params, to_pandas)` | `POST /screen/run` | yes |
| `screen_backtest(params, to_pandas)` | `POST /screen/backtest` | yes |
| `screen_rolling_backtest(params, to_pandas)` | `POST /screen/rolling-backtest` | yes |
| `stock_factor_info(factor_id, name)` | `GET /stockFactor` | — |
| `stock_factor_create_update(params)` | `POST /stockFactor` | — |
| `stock_factor_download(factor_id)` | `GET /stockFactor/{id}` | — |
| `stock_factor_delete(factor_id)` | `DELETE /stockFactor/{id}` | — |
| `stock_factor_upload(factor_id, data, ...)` | `POST /stockFactor/upload/{id}` | — |
| `strategy(strategy_id)` | `GET /strategy/{id}` | — |
| `strategy_holdings(strategy_id, date, to_pandas)` | `GET /strategy/{id}/holdings` | yes |
| `strategy_trading_system(strategy_id)` | `GET /strategy/{id}/trading-system` | — |
| `strategy_trading_system_update(strategy_id, params)` | `POST /strategy/{id}/trading-system` | — |
| `book_trading_system_update(strategy_id, params)` | `POST /strategy/{id}/book-trading-system` | — |
| `strategy_rerun(strategy_id, params)` | `POST /strategy/{id}/rerun` | — |
| `book_rerun(strategy_id, params)` | `POST /strategy/{id}/book-rerun` | — |
| `strategy_transactions(strategy_id, start, end, to_pandas)` | `GET /strategy/{id}/transactions` | yes |
| `strategy_transaction_import(strategy_id, data, ...)` | `POST /strategy/{id}/transactions` | — |
| `strategy_transaction_delete(strategy_id, params)` | `DELETE /strategy/{id}/transactions` | — |
| `strategy_rebalance(strategy_id, params)` | `POST /strategy/{id}/rebalance` | — |
| `strategy_rebalance_commit(strategy_id, params)` | `POST /strategy/{id}/rebalance/commit` | — |
| `universe_update(params)` | `POST /universe` | — |
| `get_api_id()` | helper (returns configured `apiId`) | — |
| `get_token()` | helper (returns current Bearer token, or `None`) | — |
| `set_timeout(timeout)` | helper (request timeout in seconds; default 300) | — |
| `set_max_request_retries(retries)` | helper (1–10; default 5) | — |
| `close()` | helper (closes the HTTP session; called by the context manager) | — |

33 REST operations map to the first 33 rows; the remaining 5 (`get_api_id`, `get_token`,
`set_timeout`, `set_max_request_retries`, `close`) are local client helpers with no endpoint. The
context-manager dunders `__enter__`/`__exit__` are not counted as public methods.

## AI Factor

P123's AI Factor system trains machine-learning models (typically LightGBM) on user-defined feature
sets to predict future stock returns. The API exposes a **single prediction endpoint**; training,
feature configuration, predictor management, and metrics (IC, Sharpe, feature importance) are
UI-only. There is no API endpoint to list AI Factors or their predictor IDs — record them from the
web UI.

```python
# Current predictions as a DataFrame.
df = client.aifactor_predict(123456, {}, to_pandas=True)

# With names + transformed feature matrix.
df = client.aifactor_predict(123456, {
    'includeNames': True,
    'includeFeatures': True,
    'precision': 4,
}, to_pandas=True)

# Historical predictions: asOfDt must be a Saturday.
df = client.aifactor_predict(123456, {'asOfDt': '2026-03-14'}, to_pandas=True)
```

Accepted `params` (verified against the wrapper and the live-tested curated reference): `asOfDt`
(Saturday only — see below), `includeNames`, `includeFeatures`, `figi`
(`Country Composite` | `Share Class`), `pitMethod`, `precision` (2–6). Parameters rejected by this
endpoint (accepted elsewhere): `tickers`, `currency`, `region`, `type`, `rankingMethod`,
`includeRawData`.

**Cost discrepancy — unresolved at build time (2026-06-09).** The OpenAPI spec example shows
`cost: 1` for `/aiFactor/predict/{id}`. The curated, live-tested AI Factor reference (March 2026)
reports a **fixed 20 credits per call** regardless of params or universe size, and shows
`"cost": 20` in its recorded responses. These two sources disagree, and the discrepancy could not
be resolved live during the build: a prediction call requires an AI-factor predictor id from your
own account, and the API exposes no operation to enumerate predictors. Treat the spec example as
illustrative, budget for **20 credits per call** (the only live-observed value), and confirm
against the `cost` and `quotaRemaining` fields of your first response.

**Saturday `asOfDt` constraint.** Historical predictions require `asOfDt` to fall on a **Saturday**;
any other day raises `"asOfDt must be a Saturday if specified"`. This differs from `data_universe`,
which accepts arbitrary dates. Current (no-`asOfDt`) calls return `priceDt` + `updateDt`; historical
calls return `dt` only — accessing `priceDt` on a historical response raises `KeyError`.

**Nulls.** Roughly 3–4% of the universe can have null predictions; drop them before sorting or
uploading (`df.dropna(subset=['prediction'])`). Predictions are unitless model scores, not return
percentages — convert to percentiles with `FRank` in formulas. In the formula language, reference a
trained model with `AIFactor(...)` and the walk-forward out-of-sample model with
`AIFactorValidation(...)` (use the latter for backtests to avoid look-ahead bias).

## Known Pitfalls

These are verified spec/wrapper/PR discrepancies. Where the spec and wrapper disagree on a
parameter name, **the wrapper wins** (it is closer to production).

- **Per-rule `type` on long-only screens (issue #5 / PR #6).** For a `method: 'long'` screen, the
  rule objects must **not** carry a per-rule `type` field; the API rejects it with
  `"Rule type parameter should not be present"`. The per-rule `type` (`common`/`long`/`short`/
  `hedge`) is valid only when the screen `method` is `long/short` or `hedged`. The spec's
  `ScreenRuleParams.type` description confirms this ("only applicable if screen method is long/short
  or hedged"). Example script `02_screen_run.py` sends rules with no per-rule `type`.

- **`file=` renamed to `data=`.** P123's prose docs describe the upload body parameter as `file`,
  but the wrapper methods (`data_series_upload`, `stock_factor_upload`,
  `strategy_transaction_import`) take the payload as **`data=`** (a string or a file-like object).
  Use `data=`.

- **Deprecated `includeNodeDetails` → `nodeDetails`.** In `RankRanksParams`, `includeNodeDetails`
  (boolean) is marked `deprecated: true`. Use the `nodeDetails` enum (`composite` | `factor`)
  instead. Script `05_rank_ranks_to_csv.py` uses `nodeDetails`.

- **No `servers` block.** The spec omits the base URL; it is only `https://api.portfolio123.com` in
  the wrapper. A reader generating a client from the spec alone must supply the base URL.

- **`apiId` int vs string.** Spec types `apiId` as `integer`; the wrapper rejects non-string
  credentials. Pass strings.

- **`token` parameter location.** The auth-token header parameter lives under
  `components/schemas` (`AccessToken`), not `components/parameters` — tooling that only scans
  `parameters` will miss it.

- **`data_prices` end date.** `end` is optional in the wrapper (`Optional[str]`) and defaults to
  today server-side; pass `None` to mean "through today".

- **`screen` type casing.** The spec enum for screen/universe `type` is `Stock` / `ETF`
  (capitalized), but the official README example sends `'type': 'stock'` (lowercase) and it works.
  The server accepts the lowercase form; the examples here follow the spec casing where practical
  but either is accepted.

### Regional universe IDs (PR #6 — reported, not in extraction artifacts)

PR #6 adds regional universe IDs for non-US markets. **None of these appear in the P123 extraction
dictionary** (`dictionary-by-code.json`); only `SP500`, `NASDAQ100`, `ALLSTOCKS`, `ALLFUND`,
`Prussell1000/2000/3000`, `SP400/600/1500`, `DJIA`, and the cap tiers (`LargeCap`…`MicroCap`) are
verified there. List the following as **PR-#6-reported only**, to be confirmed against a live
universe call before relying on them: Canada — `ALLFUNDCAN`, `PRIMARYCAN`, `ALLSTOCKSCAN`, `SPTSX`,
`SPTSX60`; Europe — `ALLFUNDEUR`, `PRIMARYEUR`, `EU600`, `EU200L`, `EU200M`, `EU200S`;
multi-region — `PRIMARYNOAM`, `PRIMARYNOAT`, `TRADEEUR`, `TRADENOAM`, `TRADENOAT`; plus
`PRIMARYUSA`, `TRADEUSA`, and `NanoCap`.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `includeNodeDetails` | `nodeDetails` | `includeNodeDetails` is deprecated in `RankRanksParams`; use the `nodeDetails` enum (`composite`/`factor`). |
| `file=` (upload kwarg) | `data=` | The wrapper's upload/import methods take the payload as `data=`, not `file=`. |
| per-rule `'type'` on a long-only screen | omit the rule `type` | For `method: 'long'`, rules must not include a per-rule `type`; it is only valid for `long/short`/`hedged` (issue #5 / PR #6). |

## See Also

- [ranking-system-xml.md](ranking-system-xml.md) — the XML schema for the `nodes` field of
  `rank_update`; read before generating any ranking XML.
- [technical.md](technical.md), [ratios-statistics.md](ratios-statistics.md),
  [financials.md](financials.md), [fundamentals.md](fundamentals.md),
  [estimates.md](estimates.md) — factor and function names used inside `formulas`, `rules`, and
  `additionalData`.
- [misc.md](misc.md) — universe IDs, constants, and operators.
- `../scripts/README.md` — runnable examples for every core workflow in this file.

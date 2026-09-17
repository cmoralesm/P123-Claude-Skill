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
data_series_info header_row on_error on_duplicates update_existing make_rebal_dt_curr
DataSeriesResult StockFactorResult TypeError
minRebalTran saveTrans posWeight numPos reconFreq sizingMethod useMargin buyRules sellRules
dataSeriesId factorId processedTransactions tranId transId orderUid settleDt limitPrice
mktUid avgShareCost daysHeld benchmarkId rankingSystemId reconPeriod rebalPeriod rebalMode
SPTSX SPTSX60 EU600 EU200L EU200M EU200S TRADEUSA TRADEEUR TRADENOAM TRADENOAT NanoCap
ALLFUNDCAN PRIMARYCAN ALLSTOCKSCAN ALLFUNDEUR PRIMARYEUR PRIMARYNOAM PRIMARYNOAT PRIMARYUSA
ALLFUNDCDRCAD CanadaTrust TSX TSXV PTCCY RY GS priceDt updateDt rawData includeRawData
ApiRankingSystem
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
Currency USD CAD EUR GBP CHF NOK PLN SEK TRY PTF SIM BOOK BOOKSIM DM PRC
DataSeriesInfoResult RankGetResult RankCreateParams StrategyInfoResult StrategyCopyParams
BookCopyParams StrategyCopyResult DataUniversePreproc StockFactorInfoResult
IdResult RankInfoResult RankingMethod IntEnum PERCENTILE_NA_NEGATIVE ClientItemNotFoundException
AttributeError ModuleNotFoundError operationId naFill trimPct outlierLimit mlTrainingEnd
excludedFormulas groupUid resolveGroupUid strategyId maxDays fhistRange grossExposure
-->
# API - Portfolio123 REST API & p123api Python Wrapper

This file documents the Portfolio123 REST API and the official `p123api` Python wrapper.
"API" is not one of the 13 categories of the P123 Factor Reference; for the formula language and
factor/function names used inside API requests, see the category files
([technical.md](technical.md), [ratios-statistics.md](ratios-statistics.md),
[financials.md](financials.md), and the ranking XML rules in
[ranking-system-xml.md](ranking-system-xml.md)).

Sources: OpenAPI 3.1.0 spec `api-docs.yml` (**32 paths / 39 operations / 9 tags / 111 schemas**),
captured from `https://api.portfolio123.com/docs/api-docs.yml` on 2026-09-03; the official
`p123api` wrapper **version 3.1.0**, all 44 public client methods; plus curated content re-verified
against both. Spec first extracted 2026-06-09; wrapper facts re-derived 2026-09-17 from the
installed 3.1.0 source.

**The surface grew on 2026-08-28.** P123 added six operations - `GET /dataSeries`, `GET /rank`,
`POST /rank/create`, `GET /strategy`, `POST /strategy/{id}/copy` and `POST /strategy/{id}/copy-book`
- and revised several schemas. Nothing was removed. v4.0.0 of this file documented the older
28-path / 33-operation spec and said, correctly for that capture, that some of these lookups did
not exist; every such passage is corrected in place below, and
[Spec Changes (2026-08-28)](#spec-changes-2026-08-28) lists the whole diff. Read any undated claim
that a P123 endpoint "does not exist" as a statement about one spec capture, not a permanent fact.

**This file documents `p123api` 3.1.0.** Install it as `pip install "p123api[pandas]>=3.1.0"` -
pandas became an optional extra in the 3.x line and every `to_pandas=True` example here needs it.
3.1.0 requires **Python 3.10+**. Every signature, default and return type below was read from the
installed 3.1.0 `client.py` and `types.py`, and every query string by capturing the parameter list
the wrapper builds; none of it is copied from prose. 3.1.0 is a **breaking** release against the
2.x line this file used to document: six methods added, nine methods now return **typed objects
instead of dicts**, pandas demoted to an extra, and one upload default flipped. It is also the
first release in which each of the 39 operations has exactly one wrapper method behind it, so
nothing in the [Wrapper Method Map](#wrapper-method-map) is endpoint-less any more; on 2.3.0 - what
v4.0.0 documented - the six newest methods are absent entirely and calling one raises
`AttributeError`. Read [Return types](#return-types) before indexing any result, and
[Migrating from p123api 2.x](#migrating-from-p123api-2x) before moving an existing pin. Anything
not in the map is unverified here - check [Known Pitfalls](#known-pitfalls) first.

## Contents

- [Authentication](#authentication)
- [Quotas & Costs](#quotas--costs)
- [Spec Changes (2026-08-28)](#spec-changes-2026-08-28)
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
- [Migrating from p123api 2.x](#migrating-from-p123api-2x)
- [AI Factor](#ai-factor)
- [Upload Workflow](#upload-workflow)
- [Known Pitfalls](#known-pitfalls)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Authentication

Base URL: `https://api.portfolio123.com`. The OpenAPI spec has **no `servers` block** - the base
URL is established only in the wrapper source (`ENDPOINT`), so a raw spec reader will not find it.

Auth is `POST /auth` with a JSON body `{apiId, apiKey}`. On success the response is the access
token as `text/plain`; the token lifetime in seconds is returned in the **`X-Expires-In`** response
header (not in the body). Authenticated requests pass the token in a `token` header, declared once
as `AccessToken` under `components/parameters` and referenced by every non-`/auth` operation. Until
2026-08-28 it sat under `components/schemas` instead - the quirk v4.0.0 flagged, because tooling
that scans only `components/parameters` misses it there. That quirk now applies only to spec copies
captured before 2026-08-28.

**apiId int-vs-string - resolved in 3.x.** The spec types `AuthParams.apiId` as `integer`
(`format: int32`). 2.x rejected anything but a non-empty `str`; 3.1.0 accepts `str | int` and
calls `str()` on it, so the disagreement is gone. The non-empty check went with it: 3.1.0 builds a
`Client` from `api_id=''`, `api_key=''` without complaint and only fails later at `/auth`.
`api_key` must still be a `str`. Validate your credentials before constructing the client.

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

- `cost` - credits the call consumed.
- `quotaRemaining` - credits left in the current billing period.

Always read these from responses rather than assuming a fixed price; the spec examples show
`cost: 1` for several operations but real cost depends on data volume (e.g., points returned).

`p123api` 3.1.0 also mirrors both onto the client - `client.cost` and `client.quotaRemaining`, set
after every successful request other than `auth()`. That is the only way to read them for calls
whose result drops the block: the nine methods in [Return types](#return-types), and the
`to_pandas=True` paths that keep no **usable** `raw_obj` on the frame (`screen_run`,
`screen_backtest`, `screen_rolling_backtest`, `strategy_holdings`, `strategy_transactions`,
`data_prices`, `aifactor_predict`, and `data_universe` when `asOfDt` is set). `data`, `rank_ranks`
and `data_universe` without `asOfDt` do keep a usable `raw_obj`.

The two failure modes differ. `screen_run` and its siblings attach no `attrs['raw_obj']` at all.
`data_universe` with `asOfDt` does attach one, but it is an **alias** of the response dict rather
than a copy, and the wrapper deletes `dt`, `cost`, `quotaRemaining` and `data` out of that same
object while building the frame - so `df.attrs['raw_obj']` exists and the two quota fields are
gone from it. `data` and `rank_ranks` copy the dict (`dict(ret)`) before deleting anything, which
is why theirs survive.

**Free trial without a data license.** The spec grants this on `POST /data` only: it can be tried
without a license using **IBM, MSFT, and INTC with 5 years of history**. `POST /data/universe`
carries no such clause in either the 2026-06 or the 2026-09 capture - its description says only
that a data license is needed to take full advantage. (v4.0.0 extended the waiver to
`/data/universe`; that was wrong against the spec it was built on too.)
`GET /data/prices/{identifier}` carries no licence clause either way. The example scripts default
to these tickers where applicable, which is a convention, not a guarantee that the operation is
usable without a licence.

**One request at a time per API key.** The API enforces a single concurrent request per key; a
second simultaneous request fails. The quota is shared across all operations (data, screening,
backtesting, AI Factor), so budget heavy backtesting against AI Factor needs.

## Spec Changes (2026-08-28)

P123 revised the REST surface on **2026-08-28**, from 28 paths / 33 operations to **32 paths /
39 operations**. Nothing was removed and nothing moved: every operation v4.0.0 documented still
answers at the same method and path, the tag list is the same 9 tags, and the schema count went
102 to 111.

| New operation | Tag | What it gives you |
|---|---|---|
| `GET /dataSeries` | Data Series | Look a data series up by id or name; ends the write-only era of this tag. |
| `GET /rank` | Rank | Read a ranking system by id or name, XML `nodes` included. |
| `POST /rank/create` | Rank | Create a **new** ranking system instead of overwriting one. |
| `GET /strategy` | Strategy | Resolve a strategy or book name to the id every other Strategy call needs. |
| `POST /strategy/{id}/copy` | Strategy | Save a copy of a strategy as `PTF` (live) or `SIM`. |
| `POST /strategy/{id}/copy-book` | Strategy | Save a copy of a book as `BOOK` (live) or `BOOKSIM`. |

Same revision, no new path:

- **`preproc` on `POST /data/universe`** - an optional machine-learning preprocessing block
  (`DataUniversePreproc`) that scales the returned matrix server-side. See [Data](#data).
- **`Currency` extended from 5 values to 9**: `USD`, `CAD`, `EUR`, `GBP`, `CHF` plus `NOK`, `PLN`,
  `SEK` and `TRY`. The `USD` default moved off the enum onto each field that references it, so the
  effective default is unchanged.
- **`StockFactorParams` dropped `description`** and gained `maxDays` and `fhistRange`;
  `StockFactorInfoResult` stopped returning `description` too. See [Stock Factor](#stock-factor).
- **`BookTradingSystemParams` gained `grossExposure`** (double, 0.1–3).
- **`AccessToken` moved** from `components/schemas` to `components/parameters`, where a header
  parameter belongs. See [Authentication](#authentication).
- **Descriptions filled in.** Both upload operations, `POST /rank` and `POST /universe` gained
  substantive prose - the `na`/`nan`/`null` clearing rule, the stock-factor identifier rules, and
  the `ApiRankingSystem` / `ApiUniverse` concurrency warnings. All of it is folded into the
  sections below; none of it changes a parameter name, an enum or a default.
- **Every `operationId` was renamed**, from leading-underscore placeholders (`_update_1`,
  `_details`) to proper camelCase names. Nothing changed on the wire; only client code generated
  off the old ids breaks.

**What this invalidates.** v4.0.0 said - correctly for the spec it was built on - that the Data
Series tag had no read operation at all, and used that absence to explain a reported
`405 Method Not Allowed`. The lookup exists now, so the absence explains nothing going forward; the
observation is kept in [Known Pitfalls](#known-pitfalls) as history, because it was real against
the older surface. The `AccessToken` quirk is corrected the same way. Everything else v4.0.0
documented about the 33 older operations survives this diff unchanged.

## Endpoints by Tag

All 39 operations across the 9 tags, as captured 2026-09-03. Method + path come from `api-docs.yml`;
the wrapper method is from the `p123api` client. "Key params" lists request fields from the spec
request schema (and, for GET endpoints, query/path parameters). Operations added in the 2026-08-28
revision are marked **(new 2026-08-28)**.

### Authenticate

**`POST /auth`** - Authenticate. Wrapper: `auth()`.
Body `AuthParams`: `apiId` (spec int32; wrapper accepts `str` or `int`), `apiKey` (string, and
still `str`-only). Returns the token as
`text/plain` plus the `X-Expires-In` header. Errors 400/401/402/406/503 (see Authentication).

### AI Factor (tag)

**`POST /aiFactor/predict/{id}`** - AI Factor Predict. Wrapper: `aifactor_predict(predictor_id, params={}, to_pandas=False)`.
Path `id` = predictor ID (int32). Body `PredictParams` (all optional): `precision` (2–6),
`universe`, `asOfDt` (date), `includeNames`, `includeFeatures`, `figi`
(`Share Class` | `Country Composite`). Response `PredictResult`: `p123Uids`, `tickers`,
`predictions`, optional `names`/`features`/`data`/`figi`, plus `cost`/`quotaRemaining`. See the
[AI Factor](#ai-factor) section for the cost discrepancy and the Saturday-`asOfDt` constraint.

### Data

**`POST /data`** - Get Data. Wrapper: `data(params, to_pandas=False)`.
Body `DataParams`: required `formulas` (array, 100 max) and `startDt` (date). Choose one identifier
set: `tickers`, `p123Uids`, `gvkeys`, `ciks`, or `figis` (each 100 max). Optional: `endDt`,
`frequency` (default `Every Week`), `region` (`United States` default, `Canada`, `North America`,
`Europe`, `North Atlantic`), `pitMethod` (`Complete` default | `Prelim`), `precision` (2–8),
`currency` (`USD` default, plus `CAD`, `EUR`, `GBP`, `CHF`, `NOK`, `PLN`, `SEK` and `TRY`),
`benchmark`, `includeNames`, `ignoreErrors` (default true). Free trial: IBM, MSFT, INTC, 5Y.
Response keyed by `p123Uids`. That nine-value `Currency` enum - widened from five on 2026-08-28 -
is shared: the same values apply wherever `currency` appears below.

**`POST /data/universe`** - Get Universe Data. Wrapper: `data_universe(params, to_pandas=False)`.
Body `DataUniverseParams`: required `formulas` and `universe` (name or id; `ApiUniverse` for a
temporary one). Optional: `type` (`Stock` default | `ETF`), `asOfDt` or `asOfDts`, `figi`,
`precision` (nullable for max precision), `currency` (default `USD`), `benchmark`, `pitMethod`,
`includeNames`, and `preproc` **(new 2026-08-28)**.
**Response content types:** `application/json`, `text/csv`, or `application/parquet` - the wrapper
returns JSON (or a DataFrame with `to_pandas=True`). **No free trial here** - the licence waiver in
the spec covers `POST /data` only.

`preproc` (`DataUniversePreproc`) applies P123's machine-learning preprocessing server-side, so the
matrix arrives already scaled; do not scale it again downstream. It changes the numbers, never which
rows come back. Only `scaling` is required:

| Field | Values | Default | Meaning (spec wording) |
|---|---|---|---|
| `scaling` | `normal` \| `rank` \| `minmax` | - | **Required.** Scaling applied to each feature column. |
| `scope` | `dataset` \| `date` | `date` | Scale within each observation date, or pooled across the whole dataset. |
| `naFill` | bool | `false` | "Set NAs to the middle values". |
| `trimPct` | number | `0` | Trim percentage; the spec gives no description. |
| `outliers` | bool | `false` | "Clip outliers". |
| `outlierLimit` | number | `0` | Outlier limit; the spec says only "Used for normal scaling". |
| `mlTrainingEnd` | date | - | "End date for the scaling when scope = dataset". |
| `excludedFormulas` | string array | - | Formulas excluded from the preprocessing; annotated "Data license required for non technical factors". |

`scope: 'date'` (the default) scales each observation date on its own and is the point-in-time safe
choice. `scope: 'dataset'` pools across dates, so pair it with `mlTrainingEnd` to keep statistics
from after the training window out of the scaled features of your test period.

**`GET /data/prices/{identifier}`** - Download Security Prices. Wrapper: `data_prices(identifier, start, end, to_pandas=False)`.
Path `identifier` = UID or ticker (no country defaults to `:USA`; numeric is a UID; `955:HKG` style
for explicit country). Query `start` (required, date) and `end` (optional, defaults to today).
Response `PricesResult`: `security` (`p123Uid`, `ticker`) and `prices` (OHLCV bars), plus
`cost`/`quotaRemaining`. Errors include 404 (UID/ticker not found) and 429 (rate limit).

### Data Series

Four operations. The tag was write-only until **2026-08-28**, when P123 added `GET /dataSeries`;
that is why v4.0.0 and everything older says a series cannot be looked up by name, and why
`data_series_info` was seen returning a 405. It can be looked up now - see
[Known Pitfalls](#known-pitfalls) for the history.

**`GET /dataSeries`** - Data Series Info **(new 2026-08-28)**. Wrapper:
`data_series_info(*, id=None, name=None)`.
Query `id` (int32) or `name`; both are optional in the spec, so pass exactly one. The wrapper sends
`id` when it is given and `name` otherwise, and both args are **keyword-only** with the id kwarg
spelled `id`, not `series_id` - see [Keyword-only lookups](#keyword-only-lookups). Returns
`DataSeriesInfoResult` = `SharedResult` (`cost`, `quotaRemaining`) plus `dataSeriesId` and `name` -
**no `description`**, even though `POST /dataSeries` accepts one. Errors 402/403/404, and a miss
raises `ClientItemNotFoundException`. Read-only.

**`POST /dataSeries`** - Data Series Create/Update. Wrapper: `data_series_create_update(params)`.
Body `DataSeriesParams`: required `name`; optional `id` (omit to create, supply it to update),
`description`. Returns `DataSeriesResult` = `SharedResult` (`cost`, `quotaRemaining`) plus
`dataSeriesId` - **persist that id**. `GET /dataSeries` can recover it from the name since
2026-08-28, but that is a billable round trip, the id is what upload and delete take, and a name is
only a valid handle until somebody renames the series. Errors 400/402/403/404/409. Mutating.

**`POST /dataSeries/upload/{id}`** - Upload Data Series. Wrapper:
`data_series_upload(series_id, data, existing_data='overwrite', date_format='yyyy-mm-dd',
decimal_separator='.', ignore_errors=False, ignore_duplicates=False, contains_header_row=True)`.
Path `id`; request body is `text/csv` passed as `data=` (a string, or a file-like opened in
**binary** mode). Dates go in the first column and values in the second; a header row is skipped
only when `headerRow` is set, and the names in it are never processed. A value of `na`, `nan` or
`null` (any case) **clears** the stored value for that date instead of writing one. Returns
`SharedResult`. Mutating.

The wrapper takes **snake_case Python kwargs** and builds the camelCase **HTTP query parameters**
itself. The two vocabularies are never interchangeable - a camelCase name used as a kwarg raises
`TypeError`. In 3.1.0 every option below has a real default and is appended on **every** call, so
the server defaults in the last column apply only to a hand-rolled HTTP request. Pass `None`
explicitly to suppress one and fall back to the server default - `requests` drops `None`
parameters. In 2.x these kwargs defaulted to `None` and were omitted from the URL.

| Wrapper kwarg (Python) | Query param (HTTP) | Value | Wrapper default (3.1.0) | Server default |
|---|---|---|---|---|
| `existing_data` | `existingData` | `'overwrite'` \| `'skip'` \| `'delete'` | `'overwrite'` | `overwrite` |
| `date_format` | `dateFormat` | `dd`/`mm`/`yyyy`, any separator | `'yyyy-mm-dd'` | `yyyy-mm-dd` |
| `decimal_separator` | `decimalSeparator` | `'.'` \| `','` | `'.'` | `.` |
| `ignore_errors` | `onError` | bool → `continue` if true, else `stop` | `False` | `stop` |
| `ignore_duplicates` | `onDuplicates` | bool → `continue` if true, else `stop` | `False` | `stop` |
| `contains_header_row` | `headerRow` | bool | `True` | `false` |

**The header default is the one that changes results.** `contains_header_row` defaults to `True`
in 3.1.0 against a server default of `false`, and the spec defines `headerRow=true` as "the first
line of the uploaded data will be skipped". A headerless CSV that uploaded correctly through 2.x
therefore loses its first data row through 3.1.0 unless you pass `contains_header_row=False`.

There is **no `column_separator` kwarg here** (that one belongs to `stock_factor_upload`), and no
`header_row`, `on_error` or `on_duplicates` kwarg on any method. Worked example:
[Upload Workflow](#upload-workflow).

**`DELETE /dataSeries/{id}`** - Data Series Deletion. Wrapper: `data_series_delete(series_id)`.
Path `id`. Mutating.

### Rank

**`GET /rank`** - Rank Info **(new 2026-08-28)**. Wrapper: `rank_get(*, id=None, name=None)`.
Query `id` (int32) or `name`; pass exactly one. Returns `RankGetResult`: `name`, `id`, `nodes` (the
whole ranking system as one XML string), `type` (`Stock` | `ETF`), `rankingMethod`, `currency`,
`groupUid` (group ID) and `resolveGroupUid` (group context ID). `RankGetResult` is **not**
`SharedResult`-wrapped, so the body carries no `cost`/`quotaRemaining`. Errors 402/403/404/406.
Read-only. This is what makes a safe edit cycle possible: read `nodes`, change it, write it back
with `POST /rank`. See [Known Pitfalls](#known-pitfalls) - the wrapper's result type spells this
field `xml`, not `nodes`.

**`POST /rank`** - Rank Update. Wrapper: `rank_update(params)`.
Body `RankParams`: required `nodes` (ranking-system XML string) and `type` (`Stock` | `ETF`);
optional `id` (omit to update the `ApiRankingSystem`), `rankingMethod` (`2` Percentile NAs Negative,
the default | `4` Percentile NAs Neutral | `1` Normal Distribution, experimental), `currency`
(default `USD`). Mutating - it **overwrites** the target system in place; to add one instead, use
`POST /rank/create`. The spec warns that `ApiRankingSystem` is a real custom ranking system in the
account, so updating it while another request is still using it yields unexpected results.
For the XML schema, see [ranking-system-xml.md](ranking-system-xml.md).

**`POST /rank/create`** - Rank Creation **(new 2026-08-28)**. Wrapper:
`rank_create(name, nodes, *, rankingMethod, type, currency)`.
Body `RankCreateParams`: required `name` and `nodes` (the XML); optional `rankingMethod` (default
`2`), `type` (`Stock` | `ETF`) and `currency` (default `USD`). Errors 400/402/403/406/409.
Mutating - it creates a ranking system and consumes a slot on the account. **The 200 body's shape
is disputed:** the spec types it as a bare int32, the wrapper decodes an object and reads `id` off
it (see [Known Pitfalls](#known-pitfalls)). Print your first live response before writing code
against either.

**`POST /rank/performance`** - Rank Performance. Wrapper: `rank_perf(params)`.
Body `RankPerfParams`: required `rankingSystem` (name or id) and `startDt`. Optional: `endDt`,
`universe`, `numBuckets` (2–200, default 20), `rebalFreq` (default `Every 4 Weeks`), `slippage`,
`benchmark` (default `SPY`), `minPrice` (default 3), `minLiquidity`, `maxReturn`, `maxNAs`,
`transType` (`long` default | `short`), `outputType` (`ann` default | `perf`), `pitMethod`,
`precision`, `rankingMethod`. Response is `RankPerfRetResult` (`bucketAnnRet`) or
`RankPerfDetailedResult` (series), depending on `outputType`.

**`POST /rank/ranks`** - Ranks. Wrapper: `rank_ranks(params, to_pandas=False)`.
Body `RankRanksParams`: required `rankingSystem` and `asOfDt`. Optional: `universe`, `tickers`,
`includeNames`, `includeNaCnt`, `includeFinalStmt`, `nodeDetails` (`composite` | `factor`),
`additionalData` (100 max), `currency`, `figi`, `pitMethod`, `precision`, `rankingMethod`.
**Use `nodeDetails`, not the deprecated `includeNodeDetails`** (see Known Pitfalls). Response:
`p123Uids`, `tickers`, `ranks`, optional `nodes`/`naCnt`/`finalStmt`/`additionalData`.

**`POST /rank/{id}/touch`** - Rank Touch. Wrapper: `rank_touch(rank_id)`.
Path `id` = ranking system ID. Invalidates cached ranks. Returns no body.

### Screen

**`POST /screen/run`** - Screen Run. Wrapper: `screen_run(params, to_pandas=False)`.
Body `ScreenRunParams`: required `screen`, which is one of: a screen ID (int), a
`ScreenByIdParams` object (`id`, optional `maxNumHoldings`), or an inline `ScreenParams`. Inline
`ScreenParams`: required `type` (`Stock` | `ETF`); optional `rules` (array of `ScreenRuleParams`),
`method` (`long` default | `short` | `long/short` | `hedged`), `maxNumHoldings`, `benchmark`,
`universe`, `ranking`, `currency`. Each rule: required `formula`; optional per-rule `type`
(`common` | `long` | `short` | `hedge`) **only for `long/short` or `hedged` methods**. Top-level
optional: `asOfDt`, `endDt`, `pitMethod`, `precision`. See Known Pitfalls for the per-rule `type`
fix.

**`POST /screen/backtest`** - Screen Backtest. Wrapper: `screen_backtest(params, to_pandas=False)`.
Body `ScreenBacktestParams`: required `screen` and `startDt`. Optional: `endDt`, `transPrice`
(1 Next Open default, 4 Next Close, 3 Next Avg Hi/Low), `maxPosPct`, `slippage` (default 0.25),
`longWeight`/`shortWeight` (default 100), `rankTolerance`, `carryCost` (default 1.5), `rebalFreq`
(default `Every 4 Weeks`), `riskStatsPeriod` (`Monthly` default | `Weekly` | `Daily`), `pitMethod`,
`precision`.

**`POST /screen/rolling-backtest`** - Screen Rolling Backtest. Wrapper: `screen_rolling_backtest(params, to_pandas=False)`.
Body `ScreenRollingBacktestParams`: the `ScreenBacktest` shared fields plus `frequency`
(`Every Week` default | `Every 4 Weeks`) and `holdingPeriod` (days, 1–730, default 182).

### Stock Factor

**`GET /stockFactor`** - Stock Factor Info. Wrapper:
`stock_factor_info(*, id=None, factor_id=None, name=None)`.
Query `id` or `name`. Returns `StockFactorInfoResult` = `SharedResult` plus `factorId` and `name`.
**`description` left this response on 2026-08-28** - v4.0.0 listed it; the live spec does not. All
three wrapper args are **keyword-only** - `stock_factor_info(123)` raises `TypeError`. Pass exactly
one: the wrapper resolves `id`, then `factor_id`, then `name`, and sends the first it reaches as
the `id` or `name` query parameter. `factor_id` is the 2.x spelling, kept as a `@deprecated`
overload; prefer `id`. The sibling lookups are `data_series_info`, `rank_get` and `strategy_info` -
see [Keyword-only lookups](#keyword-only-lookups). Since 2026-08-28 the Data Series tag has the
matching `GET /dataSeries`, so this is no longer the API's only lookup by name.

**`POST /stockFactor`** - Stock Factor Create/Update. Wrapper: `stock_factor_create_update(params)`.
Body `StockFactorParams`: required `name` (the spec now marks it "required for creating a new stock
factor"); optional `id` (omit to create), `maxDays` and `fhistRange`. Returns `StockFactorResult` =
`SharedResult` plus `factorId`. Mutating. **`description` was removed from this body on
2026-08-28**; the two new fields took its place:

| Field | Default on create | Meaning |
|---|---|---|
| `maxDays` | 30 | How long an uploaded value stays valid. Older than `maxDays` from an observation date and it reads NA. |
| `fhistRange` | 0 | Extra weeks of data loaded either side of the observation date, so `FHist()` can reach it. Leave at 0 unless the factor is read through `FHist()` - the extra weeks are loaded on every evaluation. |

**`GET /stockFactor/{id}`** - Stock Factor Download. Wrapper: `stock_factor_download(factor_id)`.
Path `id`. Returns `dates`, `tickers`, `values`, `p123Uids`.

**`DELETE /stockFactor/{id}`** - Stock Factor Deletion. Wrapper: `stock_factor_delete(factor_id)`.
Path `id`. Mutating.

**`POST /stockFactor/upload/{id}`** - Upload Stock Factor Data. Wrapper:
`stock_factor_upload(factor_id, data, column_separator=',', existing_data='overwrite',
date_format='yyyy-mm-dd', decimal_separator='.', ignore_errors=False, ignore_duplicates=False)`.
Path `id`; body `text/csv` passed as `data=` (a string, or a file-like opened in **binary** mode).
The content **must** carry a header row here, and only the first three columns are processed:
`date`, an identifier and `value`. The identifier column may be `id` (a P123 stock ID), `ticker`,
`gvkey`, `cik` or `figi`; some identifier types resolve to several stocks (the spec's worked
example is one FIGI resolving to both `UMC:USA` and `UMCB:DEU`), and resolution is performed **at
upload time** - if coverage or an identifier relationship changes later, the stored data still
reflects the original resolution. `na`, `nan` or `null` (any case) in the value column clears the
stored value for that date. Returns `SharedResult`. Mutating. Same snake_case-kwarg to
camelCase-query translation as `data_series_upload`, with one option added and one removed, and
every option sent on every call:

| Wrapper kwarg (Python) | Query param (HTTP) | Value | Wrapper default (3.1.0) | Server default |
|---|---|---|---|---|
| `column_separator` | `columnSeparator` | `','` \| `';'` \| tab | `','` | `comma` |
| `existing_data` | `existingData` | `'overwrite'` \| `'skip'` \| `'delete'` | `'overwrite'` | `overwrite` |
| `date_format` | `dateFormat` | `dd`/`mm`/`yyyy`, any separator | `'yyyy-mm-dd'` | `yyyy-mm-dd` |
| `decimal_separator` | `decimalSeparator` | `'.'` \| `','` | `'.'` | `.` |
| `ignore_errors` | `onError` | bool → `continue` if true, else `stop` | `False` | `stop` |
| `ignore_duplicates` | `onDuplicates` | bool → `continue` if true, else `stop` | `False` | `stop` |

**`column_separator` changed vocabulary in 3.x.** 2.x took the API's own words
(`'comma'`/`'semicolon'`/`'tab'`), which is what still goes on the wire. 3.1.0 is annotated with
the literal characters and translates comma, semicolon and tab to those words before building the
URL. Any other string is forwarded verbatim, so the 2.x words still work at runtime - but the
characters are now the documented spelling.

**Deliberate asymmetry.** `stock_factor_upload` has `column_separator` and **no**
`contains_header_row`; `data_series_upload` has `contains_header_row` and **no**
`column_separator`. Neither method takes both, and copying a kwarg list from one to the other
raises `TypeError`. The spec agrees exactly - `columnSeparator` is a query parameter only on
`/stockFactor/upload/{id}`, `headerRow` only on `/dataSeries/upload/{id}` - so this is the API's
shape, not a wrapper omission. Both objects can be re-found by name since 2026-08-28 -
`stock_factor_info(name=...)` here, `data_series_info(name=...)` on the Data Series side; before
that date only the stock factor could.

### Strategy

**`GET /strategy`** - Strategy/Book Info **(new 2026-08-28)**. Wrapper:
`strategy_info(*, id=None, name=None)`.
Query `id` (int32) or `name`; pass exactly one, keyword-only. Returns `StrategyInfoResult` =
`SharedResult` plus `strategyId` and `name`. Errors 402/403/404. Read-only. It resolves a name to
the id every other Strategy operation carries in its path, and books resolve here too - hence the
spec's title "Strategy/Book Info". It returns **no** performance; use `GET /strategy/{id}` for that.

**`GET /strategy/{id}`** - Strategy/Book Details. Wrapper: `strategy(strategy_id)`.
Path `id` = strategy/book ID. Returns `summary`, `stats`, `dailyPerf` (plus `cost`/`quotaRemaining`).

**`GET /strategy/{id}/holdings`** - Historical Holdings. Wrapper: `strategy_holdings(strategy_id, date=None, to_pandas=False)`.
Path `id`; query `date` (defaults to today). Returns `holdings` (array of `StrategyPortHolding`).

**`GET /strategy/{id}/trading-system`** - Strategy Trading System. Wrapper: `strategy_trading_system(strategy_id)`.
Path `id`. Returns the live/simulated strategy or book trading system definition.

**`POST /strategy/{id}/trading-system`** - Live Strategy Trading System Update. Wrapper: `strategy_trading_system_update(strategy_id, params)`.
Path `id`. Body `StrategyTradingSystemParams` (`useMargin`, `universe`, `rankingSystem`,
`rankingMethod`, `buyRules`, `sellRules`, `rebalance`). Mutating.

**`POST /strategy/{id}/book-trading-system`** - Live Book Trading System Update. Wrapper: `book_trading_system_update(strategy_id, params)`.
Path `id`. Body `BookTradingSystemParams`: required `assets` (each with `itemUid`, `type` - `PTF`
live strategy, `DM` designer model, `PRC` stock or ETF - and `relativeWeight`); optional
`grossExposure` (0.1–3), added 2026-08-28. Mutating.

**`POST /strategy/{id}/rerun`** - Simulation Rerun. Wrapper: `strategy_rerun(strategy_id, params)`.
Path `id`. Body `SimRerunParams`: trading-system fields plus required `startDt`/`endDt` and
optional `saveTrans`. Mutating when `saveTrans` is set.

**`POST /strategy/{id}/book-rerun`** - Book Simulation Rerun. Wrapper: `book_rerun(strategy_id, params)`.
Path `id`. Body `BookSimRerunParams`: `assets`, required `startDt`/`endDt`.

**`POST /strategy/{id}/copy`** - Copy Strategy **(new 2026-08-28)**. Wrapper:
`strategy_copy(id, name, type=None)`.
Path `id` = the strategy to copy. Body `StrategyCopyParams`: required `name`, which must be unique
across every live and simulated strategy **and** book in the account; optional `type` - `PTF` (live)
or `SIM` (simulated). Omit `type` and a strategy of the source's own type is created, but the spec
recommends stating it. Returns `StrategyCopyResult` = `SharedResult` plus `id` (the new strategy).
Errors 402/403/404 (404 = invalid strategy ID). **Mutating - it creates an object in the account.**
The wrapper's docstring adds that copied live strategies are set to manual rebalance; the spec does
not say so.

**`POST /strategy/{id}/copy-book`** - Copy Book **(new 2026-08-28)**. Wrapper:
`book_copy(id, name, type=None)`.
Path `id` = the book to copy. Body `BookCopyParams`: required `name` (same account-wide uniqueness
rule); optional `type` - `BOOK` (live) or `BOOKSIM` (simulated), defaulting to the source's type.
Returns `StrategyCopyResult`. Errors 402/403/404 (404 = invalid book ID; its 200 has no description
in the spec). **Mutating.** Note the shape: books get their own copy path but share the strategy
result schema, and there is no Book tag at all - books are addressed through Strategy throughout.

**`GET /strategy/{id}/transactions`** - Get Strategy Transactions. Wrapper: `strategy_transactions(strategy_id, start, end, to_pandas=False)`.
Path `id`; query `start` and `end` (both required dates). Returns `trans` (array of `StrategyTran`).

**`POST /strategy/{id}/transactions`** - Strategy Transaction Import. Wrapper: `strategy_transaction_import(strategy_id, data, content_type='text/csv', update_existing=False, make_rebal_dt_curr=False)`.
Path `id`. Body `text/csv` or `text/tsv` passed as `data=`; select the format with
`content_type='text/tsv'`. Columns in order: date, ticker, type, shares, price, commission, notes.
Type is one of BUY, SELL, COVER, SHORT, DIV, SPLIT, CASH. Kwarg → query mapping:
`update_existing` → `updateExisting`, `make_rebal_dt_curr` → `makeRebalDtCurr`; both are bools
defaulting to `False`, and each is sent as `1` **only when true** (false is omitted, not sent as
`0`, so `False` is indistinguishable from leaving it out). `content_type` is not a query parameter
- it sets the `Content-Type` request header, and this is the only body-posting method that sends
one. This method accepts **none** of the CSV-parsing options: `existing_data`, `date_format`,
`decimal_separator`, `ignore_errors`, `ignore_duplicates`, `contains_header_row` and
`column_separator` all raise `TypeError` here. Mutating.

**`DELETE /strategy/{id}/transactions`** - Strategy Transaction Delete. Wrapper: `strategy_transaction_delete(strategy_id, params)`.
Path `id`. Body is a JSON array of transaction IDs (integers). Mutating.

**`POST /strategy/{id}/rebalance`** - Rebalance. Wrapper: `strategy_rebalance(strategy_id, params)`.
Path `id`. Body `RebalanceParams` (all optional): `pitMethod`, `op` (`Rebal` | `Recon` |
`ReconRebal`, for Dynamic Weight Live Strategies; otherwise auto-assigned), `reject` (P123 UIDs to
suppress), `figi`, `minRebalTran` (Live Book only). Returns `RebalanceOutput`: `recs`, plus `op`
and `ranks` to be forwarded **unaltered** to the commit endpoint. Read-only (recommendations only).

**`POST /strategy/{id}/rebalance/commit`** - Rebalance Commit. Wrapper: `strategy_rebalance_commit(strategy_id, params)`.
Path `id`. Body `RebalanceCommitParams`: required `trans` (array of `RebalanceTran`: `p123Uid`,
`action` `BUY`/`COVER`/`SELL`/`SHORT`, `price`, `shares`, optional `comm`/`slip`/`note`); optional
`op` and `ranks` (echo what `rebalance` returned; `ranks` required for Live Strategy). **Mutating -
this commits orders to the strategy.**

### Universe

**`POST /universe`** - Universe Update. Wrapper: `universe_update(params)`.
Body `UniverseParams`: required `type` (`Stock` | `ETF`) and `rules` (array of formula strings);
optional `startingUniverse`, `currency` (default `USD`; the enum widened to nine values on
2026-08-28 - see [Spec Changes (2026-08-28)](#spec-changes-2026-08-28)). Creates or updates the
`ApiUniverse` (or a named one). Then reference `'universe': 'ApiUniverse'` in other calls. Mutating
- and the spec warns that `ApiUniverse` is a real custom universe in the account, so updating it
while another request is still using it yields unexpected results.

## Wrapper Method Map

All 44 public methods on the `p123api.Client` of **3.1.0**, enumerated programmatically from the
installed source (53 `def` statements, 9 of them `@overload` stubs for four names). The
"to_pandas" column marks the 10 methods that accept `to_pandas=True` and can return a DataFrame;
that set is unchanged from 2.3.0.

| Wrapper method | Operation (method + path) | to_pandas |
|---|---|---|
| `auth()` | `POST /auth` | - |
| `aifactor_predict(predictor_id, params, to_pandas)` | `POST /aiFactor/predict/{id}` | yes |
| `data(params, to_pandas)` | `POST /data` | yes |
| `data_universe(params, to_pandas)` | `POST /data/universe` | yes |
| `data_prices(identifier, start, end, to_pandas)` | `GET /data/prices/{identifier}` | yes |
| `data_series_info(*, id, name)` | `GET /dataSeries` | - |
| `data_series_create_update(params)` | `POST /dataSeries` | - |
| `data_series_upload(series_id, data, existing_data, date_format, decimal_separator, ignore_errors, ignore_duplicates, contains_header_row)` | `POST /dataSeries/upload/{id}` | - |
| `data_series_delete(series_id)` | `DELETE /dataSeries/{id}` | - |
| `rank_get(*, id, name)` | `GET /rank` | - |
| `rank_update(params)` | `POST /rank` | - |
| `rank_create(name, nodes, *, rankingMethod, type, currency)` | `POST /rank/create` | - |
| `rank_perf(params)` | `POST /rank/performance` | - |
| `rank_ranks(params, to_pandas)` | `POST /rank/ranks` | yes |
| `rank_touch(rank_id)` | `POST /rank/{id}/touch` | - |
| `screen_run(params, to_pandas)` | `POST /screen/run` | yes |
| `screen_backtest(params, to_pandas)` | `POST /screen/backtest` | yes |
| `screen_rolling_backtest(params, to_pandas)` | `POST /screen/rolling-backtest` | yes |
| `stock_factor_info(*, id, factor_id, name)` | `GET /stockFactor` | - |
| `stock_factor_create_update(params)` | `POST /stockFactor` | - |
| `stock_factor_download(factor_id)` | `GET /stockFactor/{id}` | - |
| `stock_factor_delete(factor_id)` | `DELETE /stockFactor/{id}` | - |
| `stock_factor_upload(factor_id, data, column_separator, existing_data, date_format, decimal_separator, ignore_errors, ignore_duplicates)` | `POST /stockFactor/upload/{id}` | - |
| `strategy_info(*, id, name)` | `GET /strategy` | - |
| `strategy(strategy_id)` | `GET /strategy/{id}` | - |
| `strategy_holdings(strategy_id, date, to_pandas)` | `GET /strategy/{id}/holdings` | yes |
| `strategy_trading_system(strategy_id)` | `GET /strategy/{id}/trading-system` | - |
| `strategy_trading_system_update(strategy_id, params)` | `POST /strategy/{id}/trading-system` | - |
| `book_trading_system_update(strategy_id, params)` | `POST /strategy/{id}/book-trading-system` | - |
| `strategy_rerun(strategy_id, params)` | `POST /strategy/{id}/rerun` | - |
| `book_rerun(strategy_id, params)` | `POST /strategy/{id}/book-rerun` | - |
| `strategy_copy(id, name, type)` | `POST /strategy/{id}/copy` | - |
| `book_copy(id, name, type)` | `POST /strategy/{id}/copy-book` | - |
| `strategy_transactions(strategy_id, start, end, to_pandas)` | `GET /strategy/{id}/transactions` | yes |
| `strategy_transaction_import(strategy_id, data, content_type, update_existing, make_rebal_dt_curr)` | `POST /strategy/{id}/transactions` | - |
| `strategy_transaction_delete(strategy_id, params)` | `DELETE /strategy/{id}/transactions` | - |
| `strategy_rebalance(strategy_id, params)` | `POST /strategy/{id}/rebalance` | - |
| `strategy_rebalance_commit(strategy_id, params)` | `POST /strategy/{id}/rebalance/commit` | - |
| `universe_update(params)` | `POST /universe` | - |
| `get_api_id()` | helper (returns configured `apiId`) | - |
| `get_token()` | helper (returns current Bearer token, or `None`) | - |
| `set_timeout(timeout)` | helper (request timeout in seconds; default 300) | - |
| `set_max_request_retries(retries)` | helper (1–10; default 5) | - |
| `close()` | helper (closes the HTTP session; called by the context manager) | - |

39 REST operations map to the first 39 rows; the remaining 5 (`get_api_id`, `get_token`,
`set_timeout`, `set_max_request_retries`, `close`) are local client helpers with no endpoint. On
3.1.0 the correspondence is exact in both directions - no operation without a method, and no REST
method without an operation. The context-manager dunders `__enter__`/`__exit__` are not counted as
public methods.

Rows list argument **names**, not defaults - and in 3.1.0 optional no longer means absent: the two
uploads default to concrete values and send **every** query parameter on every call, where 2.x
defaulted them to `None` and omitted them. `strategy_transaction_import` still defaults its two
flags to `False`. Kwargs are snake_case - none of the camelCase query parameters in this file is
ever a kwarg - with one exception: `rank_create` takes `rankingMethod` in camelCase, because it is
a JSON body field rather than a query parameter. The four rows written `(*, id, ...)` are
**keyword-only**. This map is generated from 3.1.0; the six methods behind the 2026-08-28
operations (`data_series_info`, `rank_get`, `rank_create`, `strategy_info`, `strategy_copy`,
`book_copy`) exist on no 2.x release.

### Return types

3.1.0 is the first release that does not return a plain `dict` everywhere. Nine methods pass a
`result_type` to the request helper and return a small typed object from `p123api.types`. Every
other method still returns the parsed JSON body, and `to_pandas=True` is untouched.

| Method | Returns | Attributes on the object |
|---|---|---|
| `rank_create(...)` | `IdResult` | `id` |
| `strategy_copy(...)` | `IdResult` | `id` |
| `book_copy(...)` | `IdResult` | `id` |
| `rank_get(...)` | `RankInfoResult` | `name`, `id`, `xml`, `currency`, `rankingMethod`, `type`, `groupUid`, `resolveGroupUid` |
| `data_series_create_update(...)` | `DataSeriesResult` | `dataSeriesId` |
| `data_series_info(...)` | `DataSeriesInfoResult` | `dataSeriesId`, `name` |
| `stock_factor_create_update(...)` | `StockFactorResult` | `factorId` |
| `stock_factor_info(...)` | `StockFactorInfoResult` | `factorId`, `name` |
| `strategy_info(...)` | `StrategyInfoResult` | `strategyId`, `name` |

These objects are **attribute-only**. Their class decorator installs `__init__` and `__repr__` and
nothing else, so they are not subscriptable, not iterable, and have no `.get()`:

```python
created = client.data_series_create_update({'name': 'My Diffusion Index'})
created.dataSeriesId          # 12345 - the 3.x spelling
created['dataSeriesId']       # TypeError: 'DataSeriesResult' object is not subscriptable
created.get('dataSeriesId')   # AttributeError: no attribute 'get'
dict(created)                 # TypeError: 'DataSeriesResult' object is not iterable
vars(created)                 # {'dataSeriesId': 12345} - the supported dict view
```

Three consequences to plan for:

- **Only the listed attributes survive.** The generated constructor runs `self.<field> =
  d.get('<field>')` for its declared fields and discards the rest of the body, *including* `cost`
  and `quotaRemaining`. A field the server omits arrives as `None` rather than raising.
- **Read quota from the client instead.** 3.1.0 sets `client.cost` and `client.quotaRemaining`
  after every successful request other than `auth()`, before any DataFrame conversion or typed
  object is built. Both are `None` before the first call and whenever the body is not a JSON
  object.
- **`rankingMethod` comes back as an enum**, not a plain int: `RankingMethod`, an `IntEnum`, so it
  compares, serialises **and prints** as `2`, `4` or `1` - from Python 3.11 on `IntEnum.__str__`
  is `int.__str__`, so `print(m)` and `f'{m}'` both give the number. Only the repr shows the
  member name - `<RankingMethod.PERCENTILE_NA_NEGATIVE: 2>` - including inside a
  `RankInfoResult(...)` repr, which interpolates the member with `!r`.

The package root re-exports `IdResult`, `DataSeriesResult`, `DataSeriesInfoResult`,
`StockFactorResult`, `StockFactorInfoResult`, `StrategyInfoResult`, `Currency`, `Client`,
`ClientException` and `ClientItemNotFoundException`. `RankInfoResult` and `RankingMethod` are
**not** re-exported - import them from `p123api.types`, or pass the bare int to `rank_create`.

### Keyword-only lookups

The four lookup methods are keyword-only, and their id kwarg is `id` - not the `<thing>_id` name
their neighbours use. Calling one positionally raises
`TypeError: Client.data_series_info() takes 1 positional argument but 2 were given`.

| Method | Accepted kwargs | Id kwarg | Neighbour spelling the same value differently |
|---|---|---|---|
| `rank_get` | `id`, `name` | `id` | `rank_touch(rank_id)` |
| `stock_factor_info` | `id`, `factor_id` (deprecated), `name` | `id` | `stock_factor_upload(factor_id, ...)` |
| `data_series_info` | `id`, `name` | `id` | `data_series_upload(series_id, ...)` |
| `strategy_info` | `id`, `name` | `id` | `strategy(strategy_id)` |

`data_series_info` has no `series_id` kwarg, `strategy_info` has no `strategy_id` kwarg and
`rank_get` has no `rank_id` kwarg - those spellings raise
`TypeError: ... got an unexpected keyword argument`. `stock_factor_info` is the only one that
still accepts its old name: `factor_id` survives as a `@deprecated` overload mapped onto the same
`id` query parameter, so it runs.

Two implementation details that bite:

- **No argument is validated.** `data_series_info()`, `strategy_info()` and `rank_get()` with no
  arguments are legal Python; `requests` drops `None` parameters, so the wrapper issues a bare
  GET with no query string and lets the server decide. Always pass exactly one of `id` / `name`.
- **`id` wins over `name`.** `data_series_info` and `strategy_info` send `id` whenever it is not
  `None` and ignore `name` entirely. `rank_get` is the exception - it puts both on the query
  string and lets the server arbitrate.

## Migrating from p123api 2.x

For readers pinned to `p123api` 2.x. Every row is derived by diffing the installed 2.3.0 and 3.1.0
sources and the two distributions' metadata; nothing here comes from release notes.

| Area | 2.3.0 | 3.1.0 | Breaks code? |
|---|---|---|---|
| Python floor | `>=3.6` | `>=3.10` (PEP 604 unions, `match`) | yes, below 3.10 |
| pandas | hard dependency, imported at module load | optional extra, imported lazily inside each `to_pandas` branch | **yes**, for any `to_pandas=True` |
| Other deps | `requests` | `requests`, `typing_extensions` | no |
| Public methods | 38 | 44 - adds `rank_get`, `rank_create`, `strategy_info`, `strategy_copy`, `book_copy`, `data_series_info` | no, nothing removed or renamed |
| Return values | every method returns `dict` | nine methods return typed objects | **yes**, rewrite `res['key']` as `res.key` |
| `cost` / `quotaRemaining` | response body only | also `client.cost` / `client.quotaRemaining`; typed results drop them | no |
| `stock_factor_info` | `factor_id=` | `id=`, with `factor_id=` kept as a `@deprecated` overload | no |
| Upload query params | omitted while the kwarg is `None` | concrete defaults, always sent | no, same effective values |
| `contains_header_row` | `None`, so the server default `false` applied | `True`, always sent | **yes**, silently skips row 1 of a headerless CSV |
| `column_separator` | `'comma'` / `'semicolon'` / `'tab'` | the characters, translated to those words; the old words still pass through | no |
| Upload `data=` file-likes | `IO[str]`, re-sent already consumed on a retry | `IO[bytes]`, rewound or buffered before each retry | yes, open uploads in binary mode |
| 404 responses | `ClientException` with the server's message | `ClientItemNotFoundException`, a **subclass**, with the fixed text `Item not found` | no, but the server's explanation is gone |
| Credentials | `api_id` and `api_key` must be non-empty `str` | `api_id` may be `str` or `int`; emptiness is no longer checked | no, but a blank env var now fails at `/auth` |
| `ClientException(...)` | `(message, *, resp, exception)` | `(message, *, resp)`; `get_cause()` returns `__cause__` | only if you construct or chain it yourself |

The minimum upgrade for working 2.x code: move to Python 3.10+, install `p123api[pandas]` rather
than `p123api`, and change dict indexing to attribute access on the nine methods listed under
[Return types](#return-types). Nothing else in the 38 inherited methods changed shape.

## AI Factor

P123's AI Factor system trains machine-learning models (typically LightGBM) on user-defined feature
sets to predict future stock returns. The API exposes a **single prediction endpoint**; training,
feature configuration, predictor management, and metrics (IC, Sharpe, feature importance) are
UI-only. As of the 2026-09-03 capture the AI Factor tag still has exactly one operation: there is
no API endpoint to list AI Factors or their predictor IDs, so record them from the web UI. Date that
absence rather than treating it as permanent - the Data Series tag gained its lookup the same way.

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

Accepted `params` - the whole of `PredictParams`, all optional, identical in the 2026-06 and
2026-09 captures: `precision` (2–6), `universe` (scopes the prediction set), `asOfDt` (Saturday
only - see below), `includeNames`, `includeFeatures`, `figi`
(`Country Composite` | `Share Class`). The live-tested curated reference additionally reports
`pitMethod` as accepted here; **neither spec capture declares it on `PredictParams`**, so treat it
as unverified rather than as part of the documented body. Parameters rejected by this endpoint
(accepted elsewhere): `tickers`, `currency`, `region`, `type`, `rankingMethod`, `includeRawData`.

**Cost discrepancy - unresolved at build time (2026-06-09).** The OpenAPI spec example shows
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
calls return `dt` only - accessing `priceDt` on a historical response raises `KeyError`.

**Nulls.** Roughly 3–4% of the universe can have null predictions; drop them before sorting or
uploading (`df.dropna(subset=['prediction'])`). Predictions are unitless model scores, not return
percentages - convert to percentiles with `FRank` in formulas. In the formula language, reference a
trained model with `AIFactor(...)` and the walk-forward out-of-sample model with
`AIFactorValidation(...)` (use the latter for backtests to avoid look-ahead bias).

## Upload Workflow

Create the series, keep the id it returns, then push CSV text. Everything after `data=` is a
**snake_case Python kwarg**; the camelCase names are what the wrapper writes onto the URL.

```python
import p123api

CSV = """date,value
2026-01-02,101.4
2026-01-09,102.1
2026-01-16,99.8
"""

with p123api.Client(api_id='your api id', api_key='your api key') as client:
    try:
        # 1. Create. Omit 'id' to create; include it to update an existing series.
        created = client.data_series_create_update({
            'name': 'My Diffusion Index',
            'description': 'Weekly diffusion index, uploaded via API.',
        })
        # DataSeriesResult, NOT a dict: created['dataSeriesId'] raises TypeError in 3.x.
        series_id = created.dataSeriesId
        print('dataSeriesId =', series_id)
        print('cost =', client.cost)  # typed results carry no cost/quotaRemaining

        # 2. Upload. snake_case only. ignore_* are INVERTED booleans.
        result = client.data_series_upload(
            series_id,
            data=CSV,                     # not file=
            contains_header_row=True,     # not headerRow=; 3.1.0 default, server default false
            existing_data='overwrite',    # not existingData=
            date_format='yyyy-mm-dd',     # not dateFormat=
            decimal_separator='.',        # not decimalSeparator=
            ignore_errors=False,          # sends onError=stop
            ignore_duplicates=False,      # sends onDuplicates=stop
        )
        print(result)                     # cost / quotaRemaining
    except p123api.ClientException as e:
        print(e)
```

The URL the wrapper builds from that call, in wrapper parameter order:

```text
POST /dataSeries/upload/<id>?existingData=overwrite&dateFormat=yyyy-mm-dd&decimalSeparator=.&onError=stop&onDuplicates=stop&headerRow=True
```

That URL is what 3.1.0 sends for the call above - and also for a bare
`client.data_series_upload(series_id, data=CSV)` with no options at all, because **3.1.0 appends
all six parameters unconditionally** where 2.x appended only the ones you set. Note
`headerRow=True`: `contains_header_row` is the one option the wrapper forwards as a raw Python
bool, so the literal `True`/`False` goes on the wire rather than `1`/`0` - and its wrapper default
is `True` while the server's own `headerRow` default is `false`, so a headerless CSV loses its
first data row unless you pass `contains_header_row=False`. To take a server default instead, pass
`None` for that one option; `requests` drops `None` parameters. To override the spelling, pass the
string yourself - `contains_header_row='true'` is appended verbatim.

If `data` is a file-like rather than a string it must be opened in **binary** mode (`'rb'`). 3.1.0
seeks it back or buffers it before each retry; 2.x re-sent an already-consumed handle, so a
retried upload could post an empty body.

`stock_factor_upload(factor_id, data, ...)` is the same shape with `column_separator=` in place of
`contains_header_row=`.

**Recovering a lost id.** Persisting `dataSeriesId` is still the cheaper habit, but 3.x finally
gives you a fallback: `client.data_series_info(name='My Diffusion Index').dataSeriesId`, backed by
`GET /dataSeries`. A miss raises `ClientItemNotFoundException`, a `ClientException` subclass, with
the message `Item not found`.

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
  and `strategy_transaction_import`'s docstring still says `:param file:` (the other two were
  rewritten to Google-style docstrings in 3.x and now document the argument as `data`), but the
  wrapper methods
  (`data_series_upload`, `stock_factor_upload`, `strategy_transaction_import`) take the payload as
  **`data=`** (a string or a file-like object). Use `data=`.

- **Upload options are snake_case in Python, camelCase only on the wire.** The spec's query
  parameters (`headerRow`, `existingData`, `dateFormat`, `decimalSeparator`, `onError`,
  `onDuplicates`, `columnSeparator`) are **not** wrapper kwargs. Passing one raises, e.g.
  `TypeError: Client.data_series_upload() got an unexpected keyword argument 'headerRow'`. The
  kwargs are `existing_data`, `date_format`, `decimal_separator`, `ignore_errors`,
  `ignore_duplicates`, `contains_header_row` (data series) plus `column_separator` (stock factor).
  Three traps inside the trap: (a) the header kwarg is `contains_header_row`, **not** `header_row`;
  (b) `ignore_errors`/`ignore_duplicates` are **inverted booleans** - `ignore_errors=True` is what
  sends `onError=continue`, and there is no `on_error`/`on_duplicates` kwarg at all; (c) the two
  upload methods are **asymmetric** (`contains_header_row` is data-series only,
  `column_separator` is stock-factor only) and `strategy_transaction_import` shares none of these
  options. Re-derived for **3.1.0** by capturing the query list the wrapper actually builds, not by
  reading docstrings: every kwarg name and the inverted-boolean rule survived the 2.x-to-3.x
  rewrite unchanged. What did change is that 3.1.0 sends all of them on every call instead of
  omitting the ones left at `None`, that `contains_header_row` now defaults to `True`, and that
  `column_separator` takes `','`/`';'`/tab rather than `'comma'`/`'semicolon'`/`'tab'`. Full
  mappings: [Data Series](#data-series), [Stock Factor](#stock-factor); worked example:
  [Upload Workflow](#upload-workflow).

- **`data_series_info` and the 405 - closed upstream on 2026-08-28. This reverses v4.0.0.** The
  lookup exists now: `GET /dataSeries` takes `id` or `name` and returns `dataSeriesId` + `name`,
  and `p123api` 3.1.0 points `data_series_info` at it; a miss raises
  `ClientItemNotFoundException`. The history still matters, because the failure was real. Until
  the August revision the tag had exactly three operations - `POST /dataSeries`,
  `POST /dataSeries/upload/{id}` and `DELETE /dataSeries/{id}` - and no read of any kind, so
  `/dataSeries` was registered for POST and nothing else; a GET against a path routed for another
  method is precisely what `405 Method Not Allowed` is for, which is consistent with the
  **reported 405 on a live licensed account** from 2.4.x's `data_series_info`. Three things
  survive the fix. (a) It was never an account-permission problem, so a 405 here is still not a
  reason to chase API privileges or different credentials. (b) The fix needs the endpoint **and** a
  wrapper that calls it - installs pinned to the 2.4.x line can still meet the 405, and the
  wrapper raises it as `ClientException` without retrying (only 401/403 trigger re-auth). (c)
  Persist the `dataSeriesId` returned by `data_series_create_update` anyway: the lookup spends a
  request, the id is what upload and delete take, and a name is a valid handle only until someone
  renames the series.

- **`pip install p123api` no longer installs pandas.** In 3.x pandas is an optional extra; in 2.x
  it was a hard requirement imported at module load. 3.1.0 imports it lazily *inside* each
  `if to_pandas:` branch, so a bare install fails at call time with
  `ModuleNotFoundError: No module named 'pandas'` - pointing at your `screen_run` call, not at
  your install, and **not caught** by `except p123api.ClientException`. Install
  `p123api[pandas]`.

- **Deprecated `includeNodeDetails` → `nodeDetails`.** In `RankRanksParams`, `includeNodeDetails`
  (boolean) is marked `deprecated: true`. Use the `nodeDetails` enum (`composite` | `factor`)
  instead. Script `05_rank_ranks_to_csv.py` uses `nodeDetails`.

- **No `servers` block.** The spec omits the base URL; it is only `https://api.portfolio123.com` in
  the wrapper. A reader generating a client from the spec alone must supply the base URL.

- **`apiId` int vs string - resolved in 3.x, with a new edge.** The spec types `apiId` as
  `integer`; 2.x rejected anything but a non-empty `str`. 3.1.0 accepts `str` or `int` and
  stringifies it, so the disagreement is gone - but the non-empty check went with it. A `Client`
  built from `api_id=''`, `api_key=''` constructs happily and fails later at `/auth`. Validate
  your environment variables before building the client.

- **Typed results are not dicts.** Nine methods return attribute-only objects in 3.1.0; indexing
  one raises `TypeError: 'DataSeriesResult' object is not subscriptable`, and `.get()` raises
  `AttributeError`. They also discard `cost` and `quotaRemaining`, so read those from
  `client.cost` / `client.quotaRemaining`. Full list: [Return types](#return-types).

- **Spec and wrapper disagree on two 2026-08-28 response shapes.** This section's rule - the
  wrapper wins - settles *request* parameter names, not response shapes, and neither of these can
  be settled offline. (a) `rank_get(...).xml` may be empty: the wrapper's `RankInfoResult` declares
  the ranking XML as `xml`, the live spec's `RankGetResult` calls that property `nodes`, and the
  constructor copies only declared names - so if the server follows the spec, the XML arrives but
  the attribute is `None`. Read `getattr(result, 'xml', None)` and treat a `None` as suspect rather
  than as a ranking system with no nodes. (b) `rank_create` may raise `AttributeError` instead of
  returning: the spec types the 200 body of `POST /rank/create` as a bare `integer`, but the
  wrapper wraps it with `IdResult`, whose constructor calls `.get('id')` on the body - which fails
  on a bare integer, **after** the ranking system has already been created server-side. Verify each
  with one live call before scripting against it; if `rank_create` raises, recover the new id with
  `rank_get(name=...)`. `strategy_copy` and `book_copy` are unaffected - their `StrategyCopyResult`
  really does carry `id`.

- **`token` parameter location - fixed 2026-08-28.** The auth-token header parameter used to live
  under `components/schemas` (`AccessToken`) instead of `components/parameters`, so tooling that
  scans only `parameters` missed it. The live spec declares it under `components/parameters` and
  every authenticated operation references it there. Expect the old placement only in spec copies
  captured before the August revision.

- **`data_prices` end date.** `end` is typed `Optional[str]` but has **no default value** in the
  wrapper signature, so it must be supplied; pass `None` explicitly to mean "through today" (the
  server defaults to today). Omitting the argument raises
  `TypeError: ... missing 1 required positional argument: 'end'`.

- **`screen` type casing.** The spec enum for screen/universe `type` is `Stock` / `ETF`
  (capitalized), but the official README example sends `'type': 'stock'` (lowercase) and it works.
  The server accepts the lowercase form; the examples here follow the spec casing where practical
  but either is accepted.

### Regional universe IDs (verified live 2026-09-17)

These IDs work as the `universe` parameter but do **not** appear in the P123 extraction dictionary
(`dictionary-by-code.json`), which only carries `SP500`, `NASDAQ100`, `ALLSTOCKS`, `ALLFUND`,
`Prussell1000/2000/3000`, `SP400/600/1500`, `DJIA`, the exchange sets and the cap tiers
(`LargeCap`…`MicroCap`). They were reported in issue #5 / PR #6 and each one was confirmed against
the live API on 2026-09-17 with a one-row `screen_run`.

| Region | Verified IDs |
|---|---|
| Canada | `ALLFUNDCAN`, `PRIMARYCAN`, `ALLSTOCKSCAN`, `SPTSX`, `SPTSX60`, `TSX`, `TSXV`, `CanadaTrust`, `ALLFUNDCDRCAD` |
| Europe | `ALLFUNDEUR`, `PRIMARYEUR`, `EU600`, `EU200L`, `EU200M`, `EU200S`, `TRADEEUR` |
| Multi-region | `PRIMARYNOAM`, `PRIMARYNOAT`, `TRADENOAM`, `TRADENOAT` |
| United States | `PRIMARYUSA`, `TRADEUSA`, `NanoCap` |

A universe named CDR was reported alongside these and does **not** exist: the server answers
`Universe <CDR> not found`. The Canadian-dollar CDR universe is `ALLFUNDCDRCAD`.

**Reading the two error messages.** An unknown ID returns `Universe <X> not found`; a real ID your
subscription does not cover returns `Universe <X> is not in your subscribed regions`. Both are HTTP
400 and neither costs credits, so probing an ID is free - the second message is what proves an ID
exists without a regional data licence.

**`ALLFUND` is US-listed, not global.** Its dictionary label, "All Fundamentals", reads as if it
spanned every market. It does not: it holds securities listed in the US, which includes foreign
companies through their US lines and ADRs. A live band screen on `MktCap` between 280,000 and
287,000 returns `PTCCY` (PetroChina ADR), `RY` and `GS` from `ALLFUND`, but `RY:CAN` and `GS` from
`PRIMARYNOAM`. Note the consequence for cross-region work: the same company carries a **different
`p123Uid`** per listing - Royal Bank of Canada is `7652` as `RY` in `ALLFUND` and `47778` as
`RY:CAN` in the Canadian and North American universes. Joining on `p123Uid` across universes of
different regions will silently miss those pairs.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `includeNodeDetails` | `nodeDetails` | `includeNodeDetails` is deprecated in `RankRanksParams`; use the `nodeDetails` enum (`composite`/`factor`). |
| `file=` (upload kwarg) | `data=` | The wrapper's upload/import methods take the payload as `data=`, not `file=`. |
| per-rule `'type'` on a long-only screen | omit the rule `type` | For `method: 'long'`, rules must not include a per-rule `type`; it is only valid for `long/short`/`hedged` (issue #5 / PR #6). |
| `headerRow=`, `existingData=`, `dateFormat=`, `decimalSeparator=`, `onError=`, `onDuplicates=`, `columnSeparator=` as Python kwargs | `contains_header_row=`, `existing_data=`, `date_format=`, `decimal_separator=`, `ignore_errors=`, `ignore_duplicates=`, `column_separator=` | camelCase names are HTTP query parameters the wrapper builds itself; used as kwargs they raise `TypeError: ... got an unexpected keyword argument`. |
| `header_row=True` | `contains_header_row=True` | The kwarg is `contains_header_row`; `header_row` does not exist on any method. |
| `on_error='continue'` / `on_duplicates='continue'` | `ignore_errors=True` / `ignore_duplicates=True` | No `on_error`/`on_duplicates` kwarg exists. The wrapper derives `onError`/`onDuplicates` = `continue`/`stop` from those **inverted** booleans. |
| `column_separator=` on `data_series_upload`, or `contains_header_row=` on `stock_factor_upload` | use the option the method actually has | `column_separator` exists only on `stock_factor_upload`, `contains_header_row` only on `data_series_upload` - the spec's query parameters split the same way. |
| assuming `data_series_info` still 405s, or that no data-series lookup exists | `data_series_info(id=123)` / `data_series_info(name='...')` on `p123api` 3.1.0 | `GET /dataSeries` was added 2026-08-28 and 3.1.0 wires the method to it. The 405 was real before that date and still reaches older installs. Persist the `dataSeriesId` from creation anyway - the lookup spends quota. |
| `created['dataSeriesId']`, `info.get('factorId')` | `created.dataSeriesId`, `info.factorId` | The nine methods in [Return types](#return-types) return typed objects in 3.1.0; they are not subscriptable and have no `.get()`. |
| `data_series_info(series_id=123)`, `strategy_info(strategy_id=123)`, `rank_get(rank_id=1)` | `data_series_info(id=123)`, `strategy_info(id=123)`, `rank_get(id=1)` | The lookup methods are keyword-only and name the identifier `id`; any other spelling raises `TypeError`. |
| `stock_factor_info(factor_id=123)` | `stock_factor_info(id=123)` | `factor_id` still runs but is a `@deprecated` overload in 3.1.0. |
| `POST /rank` with no `id` to "create" a ranking system | `POST /rank/create` | `POST /rank` without an `id` overwrites the single `ApiRankingSystem` in place. `/rank/create` makes a new named system and returns its id. |
| `StockFactorParams.description`, or reading a description back from `GET /stockFactor` | `maxDays` / `fhistRange` | `description` left both the stock-factor request and result schemas on 2026-08-28. Data series keep theirs. |
| `GET /strategy` to fetch performance | `GET /strategy/{id}` | `GET /strategy` is the name-to-id lookup and returns only `strategyId` and `name`. |
| `pip install p123api` for a script that uses `to_pandas=True` | `pip install "p123api[pandas]"` | Since 3.0 pandas is an optional extra and the import is lazy, so the failure surfaces at call time as `ModuleNotFoundError`, which `except ClientException` will not catch. |
| `from p123api import RankingMethod` | `from p123api.types import RankingMethod` | The package root re-exports the result types and `Currency`, but not `RankingMethod` or `RankInfoResult`. |
| relying on the wrapper's header default for a headerless CSV | pass `contains_header_row=False` | 3.1.0 defaults it to `True` while the server default is `false`, so the first data row is skipped silently. |

## See Also

- [ranking-system-xml.md](ranking-system-xml.md) - the XML schema for the `nodes` field of
  `rank_update`; read before generating any ranking XML.
- [technical.md](technical.md), [ratios-statistics.md](ratios-statistics.md),
  [financials.md](financials.md), [fundamentals.md](fundamentals.md),
  [estimates.md](estimates.md) - factor and function names used inside `formulas`, `rules`, and
  `additionalData`.
- [misc.md](misc.md) - universe IDs, constants, and operators.
- `../scripts/README.md` - runnable examples for every core workflow in this file.

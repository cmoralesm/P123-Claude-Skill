---
name: portfolio123
description: >-
  Comprehensive, extraction-verified reference for Portfolio123 (P123), the systematic equity
  research platform: factor investing, stock screening, ranking systems, backtesting, and the
  REST API with the p123api Python wrapper. Use this skill whenever the user mentions
  Portfolio123, P123, p123api, P123 screens or screen rules, ranking system XML, simulated
  strategies, buy/sell rules, or any P123 formula syntax such as Close(0), FRank, FHist, MktCap,
  PEExclXorTTM, ROE%TTM, SetVar, or Eval. Also use it when the user wants to write or debug P123
  formulas, build or fix ranking systems, construct screens or universes, replicate academic
  factor strategies (value, momentum, quality, low volatility) on P123, or pull P123 data
  programmatically (screen_run, screen_backtest, rank_ranks, data_universe, AI Factor
  predictions). Covers all 4,463 factors and 465 functions of the official Factor Reference in
  13 category files, plus the full REST API (33 operations) and 9 runnable example scripts.
license: MIT
---

<!-- name-whitelist: NAHandling P123_API_ID P123_API_KEY quotaRemaining asOfDt
includeNodeDetails nodeDetails apiId Q PQ PYQ PTM A PY screen_run screen_backtest
rank_ranks data_universe aifactor_predict to_pandas api_id api_key ClientException -->
# Portfolio123 (P123)

Portfolio123 is a web platform for systematic equity research: screening, multi-factor ranking
systems, strategy simulation/backtesting, and a REST API. Its formula language (not Python) is
used in screen rules, ranking-system nodes, buy/sell rules, and API data pulls.

Everything in this skill was extracted from the official P123 Factor Reference on 2026-06-09
(4,463 factors and 465 functions across 13 categories, plus 473 constants/series-IDs/operators)
and from the official OpenAPI spec and `p123api` wrapper source. **Never invent a factor or
function name** - if a name is not in these reference files, assume it does not exist and look
up the correct one.

## Which reference file to read

Read only what the task needs:

| Task | Read |
|---|---|
| REST API or `p123api` Python calls (auth, screen_run, backtests, rank_ranks, data_universe, uploads, AI Factor) | [references/api.md](references/api.md) |
| Valuation ratios (PE, EV/EBITDA, price-to-X), margins, growth rates, quality scores (Piotroski), financial-strength and per-share ratios | [references/ratios-statistics.md](references/ratios-statistics.md) |
| Financial-statement line items (income statement, balance sheet, cash flow) and their factor variants; Compustat/FactSet vendor mapping | [references/financials.md](references/financials.md) |
| Company metadata, prices/dividends/splits as fundamentals, share stats, insider/institutional ownership, short interest, actuals | [references/fundamentals.md](references/fundamentals.md) |
| Analyst estimates: consensus EPS/sales (CurFY/NextFY/CurQ families), revisions, surprises, recommendations, long-term growth | [references/estimates.md](references/estimates.md) |
| Price/volume indicators: SMA/EMA, RSI, MACD, ADX/DMI, Bollinger, returns (Ret%Chg), 52-week stats, volatility, beta | [references/technical.md](references/technical.md) |
| Cross-sectional and time-series tools: FRank, FHist, FHistAvg, Aggregate, FMedian/FSum/FCount, Loop functions, linear regression, conditionals | [references/advanced-functions.md](references/advanced-functions.md) |
| Simulated-strategy context: buy/sell rule factors (Rank, RankPos, portfolio state), rule patterns, rebalance idioms | [references/strategy.md](references/strategy.md) |
| Universe-wide aggregates: UnivAvg, UnivCnt, UnivMedian, UnivSum, ... | [references/universe-operations.md](references/universe-operations.md) |
| Universe definition filters: UnivExclude, UnivSubset, UnivRBICS | [references/universe-filters.md](references/universe-filters.md) |
| Benchmark series access: BenchClose | [references/benchmark-functions.md](references/benchmark-functions.md) |
| Sector/industry classification (RBICS): Sector, IndCode, SubIndustry, sector/industry composites | [references/industry-sector.md](references/industry-sector.md) |
| ETF taxonomy vocabularies (ETF contexts): asset class, country, region, sector sets | [references/taxonomy.md](references/taxonomy.md) |
| Math/set/date utilities, InList, GetSeries, macro series IDs (##CPI, FRED mappings), country and universe ID constants, operators | [references/misc.md](references/misc.md) |
| **Generating or editing ranking-system XML** (mandatory read, see below) | [references/ranking-system-xml.md](references/ranking-system-xml.md) |
| Running the bundled example scripts (setup, env vars, safety model) | [scripts/README.md](scripts/README.md) |

## Formula language essentials

```p123
// Variables: set once, reuse; @var:expr also displays the value in screen reports
SetVar(@cheap, PEExclXorTTM < 15)

// Conditional: Eval(condition, value_if_true, value_if_false)
Eval(PEExclXorTTM = NA, Pr2SalesTTM < 2, PEExclXorTTM < 20)

// NA handling: IsNA(expr1, expr2) is a REPLACEMENT function (returns expr2 when
// expr1 is NA). It is NOT a one-argument boolean test - test NA with "= NA".
IsNA(DivPSTTM, 0)           // dividend per share, 0 when missing
LastSellPrice = NA          // boolean: never sold before

// Cross-sectional percentile rank (0-100). Defaults: scope #All, sort #DESC, NAs #InclNA
FRank("PEExclXorTTM", #All, #ASC) > 80   // #ASC: low PE ranks high

// Point-in-time history: value of a formula N weeks ago / averaged samples
FHist("ROE%TTM", 52)
FHistAvg("ROE%TTM", 4, 13)

// Technical: bars are trading days; constants #Year, #Month, #Week are bar counts
Close(0) > SMA(200, 0)
RSI(14) < 30
Ret%Chg(252, 21)            // total return over 252 bars, ending 21 bars ago

// Scope aggregates and counterparts
Aggregate("Pr2SalesTTM", #Industry)      // methods: #Avg (default), #CapAvg
FMedian("Pr2SalesTTM", #Industry)        // median; also FSum, FCount
UnivCnt("PEExclXorTTM < 10")             // universe-wide count

// Macro/index series in price functions via series IDs
Close(0, ##CPI)
Close(0, GetSeries("$SP500"))
```

**Line-item pattern (Financials).** Every statement line item is one function plus prebuilt
factor variants: `Sales(offset, type[, NAHandling])` with `type` = `QTR`/`ANN`/`TTM` and
`NAHandling` = `FALLBACK` (default), `KEEPNA`, `ZERONA`; prebuilt variants append period
suffixes to the same base - `SalesQ`, `SalesPQ`, `SalesPYQ`, `SalesTTM`, `SalesPTM`, `SalesA`,
`SalesPY`, growth `SalesGr%TTM`/`SalesGr%A`, per-share `SalesPSQ`, averages `Sales5YAvg`,
regressions `SalesRegGr%TTM`. The same suffix system drives most of the 4,463 factors - see
[references/financials.md](references/financials.md).

**Screens vs rankings.** Screen rules are boolean tests evaluated per stock. Ranking systems
combine weighted factor nodes into a 0–100 rank; in a ranking node, "lower is better" controls
direction (e.g. PE), while in `FRank` the equivalent is the `#ASC` sort argument.

## Critical: do not hallucinate names

The single most common failure mode is inventing plausible-looking factor names. Top
cross-category traps (every "correct" name verified against the extraction dictionary;
per-category tables live in each reference file's Common Mistakes section):

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `IsNA(x)` as boolean | `x = NA` | `IsNA(expr1, expr2)` is two-argument replacement |
| `Eval(IsNA(x), a, b)` | `Eval(x = NA, a, b)` | same trap inside Eval |
| `PiotroskiF` | `PiotFScore` | Piotroski F-Score |
| `EstEPSCY` / `EstEPSCQ` | `CurFYEPSMean` / `CurQEPSMean` | legacy Est... estimate family does not exist |
| `Revenue` | `Sales` | revenue line item |
| `NetIncome` | `NetIncBXor` | net income before extraordinaries |
| `TotalAssets` | `AstTot` | total assets |
| `FreeCashFlow` | `FCF` | free cash flow |
| `MarketCap` | `MktCap` | market capitalization |
| `EnterpriseVal` | `EV` | enterprise value (per-share: `EVPS`) |
| `GrossMargin` | `GMgn%` | gross margin (e.g. `GMgn%TTM`) |
| `CurrentRatio` | `CurRatio` | current ratio |
| `DivYield%TTM` | `Yield` | dividend yield takes no period suffix |
| `EarnYield%TTM` | `EarnYield` | yields are current-price figures, no suffix |
| `PEG` | `PEGLT` / `PEGST` | PEG ratio variants |
| `AltmanZ` | `AltmanZOrig` | also `AltmanZPriv`, `AltmanZNonManu` |
| `LatestRank` | `Rank` | current rank in buy/sell rules |
| `SectorCount` | `SecCount` | sector position count |
| `UnivCount` | `UnivCnt` | universe count |
| `BenchmarkClose` | `BenchClose` | benchmark close |
| `Average` / `Power` / `Ln` | `Avg` / `Pow` / `LN` | math function spellings |
| `PlusDI` / `MinusDI` | `DMIPlus` / `DMIMinus` | directional indicators |
| `IndustryCode` | `IndCode` | classification factor |

When unsure about any name, grep the relevant reference file before writing it.

## Ranking-system XML: always read the reference first

**ALWAYS read [references/ranking-system-xml.md](references/ranking-system-xml.md) before
generating or editing any ranking-system XML.** The correct schema is NOT guessable, and
earlier versions of this skill shipped a broken one. That file contains the validated schema,
RankType direction guidance, a worked Penman & Pope example, and a known-formula-errors table.

## API quick start

Credentials come from P123 Account Settings → API (paying subscription required). The bundled
scripts read them from the `P123_API_ID` / `P123_API_KEY` environment variables.

```python
import p123api

with p123api.Client(api_id='your api id', api_key='your api key') as client:
    try:
        # Screen by definition. Long-only screens: rules are plain formulas -
        # do NOT add a per-rule 'type' (it is rejected for method 'long').
        df = client.screen_run({
            'screen': {
                'type': 'stock',
                'universe': 'SP500',
                'method': 'long',
                'maxNumHoldings': 25,
                'ranking': {'formula': 'PEExclXorTTM', 'lowerIsBetter': True},
                'rules': [
                    {'formula': 'MktCap > 1000'},
                    {'formula': 'ROE%TTM > 10'},
                ],
            },
            'asOfDt': '2026-01-05',
        }, to_pandas=True)

        # Bulk factor download for research/ML
        df2 = client.data_universe({
            'universe': 'SP500',
            'asOfDts': ['2026-01-05'],
            'formulas': ['PEExclXorTTM', 'ROE%TTM', 'MktCap', 'Ret%Chg(252, 21)'],
            'includeNames': True,
            'precision': 4,
        }, to_pandas=True)
    except p123api.ClientException as e:
        print(e)
```

Responses carry `cost` and `quotaRemaining` - track them; see api.md → Quotas & Costs.
For endpoint-by-endpoint docs, the 38-method wrapper map, AI Factor usage (historical `asOfDt`
must be a Saturday), and known pitfalls (deprecated `includeNodeDetails` → `nodeDetails`,
upload payloads via `data=`, the per-rule `type` bug), read
[references/api.md](references/api.md).

## Runnable examples

`scripts/` contains 9 CLI examples built on `p123_helpers.py` (install: `pip install p123api`).
All are read-only except `09_strategy_rebalance_dryrun.py`, which only mutates with an explicit
`--execute` flag plus typed confirmation. Start with `01_auth_check.py`, then
`02_screen_run.py`, `07_price_history.py` (works on the free trial: IBM/MSFT/INTC, 5y history).
Full table and safety model: [scripts/README.md](scripts/README.md).

## Verified factor starting points by style

| Style | Verified factors/functions |
|---|---|
| Value | `PEExclXorTTM`, `Pr2BookQ`, `Pr2SalesTTM`, `Pr2FrCashFlTTM`, `EV2EBITDATTM`, `EarnYield`, `FCFYield` |
| Momentum | `Ret%Chg(252, 21)`, `Pr52W%Chg`, `Pr52WRel%Chg`, `RSI(14)` |
| Quality | `ROE%TTM`, `ROA%TTM`, `GMgn%TTM`, `OpMgn%TTM`, `PiotFScore` |
| Low volatility | `PctDev(52, 5)`, `BetaFunc(52, 104)` |
| Size / liquidity | `MktCap`, `AvgDailyTot(63)` |
| Growth | `SalesGr%TTM`, `EBITDAGr%TTM`, `CurFYEPSMean` vs `NextFYEPSMean` trends |

## Working rules for this skill

1. Verify every factor/function name in the reference files before using it; never extrapolate
   from one name family to another (suffix rules differ by family).
2. Read ranking-system-xml.md before any ranking XML work - no exceptions.
3. For API parameter names, api.md reflects the wrapper source where the spec disagrees
   (e.g. pass `api_id`/`api_key` as strings even though the spec types `apiId` as integer).
4. Period suffixes: `Q`, `PQ`, `PYQ`, `TTM`, `PTM`, `A`, `PY` are the core family; growth and
   statistical suffixes (`Gr%...`, `RSD%...`, `RegEst...`, `...3YAvg`) exist only where a
   category file lists them.
5. Mutating API operations (rebalance commits, uploads, deletes) require explicit user intent;
   default to dry runs (see scripts/README.md safety model).

---

Developed and maintained by [Quant Solvings](https://quantsolvings.com), a quantitative research practice in factor investing for equities.

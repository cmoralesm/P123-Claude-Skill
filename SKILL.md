---
name: portfolio123
description: >
  Comprehensive skill for Portfolio123 (P123) — a systematic/quantitative equity research platform
  used for factor investing, screening, ranking, backtesting, and portfolio management. Use this
  skill whenever the user mentions Portfolio123, P123, p123api, factor investing formulas, stock
  screening rules, ranking systems, DataMiner, P123 backtesting, P123 universe definitions, or any
  P123 syntax like Close(0), MktCap, PEExclXorTTM, SetVar, FRank, FHist, NodeRank, Eval(),
  screen rules, rank nodes, or P123 API calls. Also trigger when the user asks about writing P123
  formulas, building ranking systems, constructing screens, retrieving data via the P123 API, or
  replicating academic factor strategies (value, momentum, quality, low-volatility, BAB, etc.) on
  the P123 platform. This skill covers the full P123 formula language (464+ functions, 4456+ factors),
  the p123api Python wrapper, and best practices for systematic equity research.
---

# Portfolio123 Skill

## Overview

Portfolio123 (P123) is a web-based platform for systematic/quantitative equity research. It provides:

- **Screening**: Filter stocks using fundamental, technical, and estimate-based rules
- **Ranking Systems**: Multi-factor ranking with composite nodes and weighted factors
- **Backtesting**: Historical performance testing of screens and strategies
- **DataMiner API**: Programmatic access via REST API and `p123api` Python wrapper
- **Point-in-Time Data**: All data is evaluated as it was known at each historical date (survivorship-bias-free)

## When to Read Which Reference File

This skill has 8 reference files. Read only what's needed for the task:

| Task | Read This File |
|------|---------------|
| Writing P123 formulas (any kind) | `references/formula-quick-reference.md` |
| Using financial statement data (balance sheet, income, cash flow) | `references/fundamental-data.md` |
| Using factors and functions (determine which reference file to use with this index) | `references/factors-and-functions/index.md` |
| Building or editing a ranking system XML | `references/ranking-system-xml.md` |
| Python API calls (p123api wrapper) | `references/api-reference.md` |
| AI Factor predictions (ML models) | `references/ai-factor-reference.md` |

For ranking system XML tasks, ALWAYS read `ranking-system-xml.md` first — it contains
the verified schema, correct tag names, known formula errors, and a working example.
For most other tasks, start with `formula-quick-reference.md` + the relevant domain file.

IMPORTANT: When using factor and function names, always verify the factor name and syntax in the reference documents. Your training doesn't include enough samples of P123 syntax for you to do a good job by yourself.

Remember that not all factors and variables can be used in all parts of P123. Some things only work in a screen or universe while others will work everywhere. Some factors are ETF system specific.

## Key Concepts

### Formula Language Basics

P123 uses its own formula language (not Python) for screens, rankings, and data retrieval:

```
// Variables
SetVar(@myPE, PEExclXorTTM)
@myPE < 20

// Conditional logic
Eval(IsNA(PEExclXorTTM), Pr2SalesTTM < 2, PEExclXorTTM < 20)

// Cross-sectional ranking (#ASC = lower is better)
FRank("PEExclXorTTM", #All, #ASC) > 80

// Historical point-in-time value (52 weeks ago)
FHist("ROE%TTM", 52)

// Historical average (4 samples, 13 weeks apart)
FHistAvg("ROE%TTM", 4, 13)

// Technical with price series
Close(0) > SMA(200, 0)
RSI(14) < 30
```

### Fundamental Data Pattern

Every financial line item follows a consistent pattern:

- **Function**: `ItemName(offset, periodType[, NAHandling])`
  - offset: 0=most recent, 1=previous, etc.
  - periodType: `QTR`, `ANN`, `TTM`
  - NAHandling: `FALLBACK` (default), `KEEPNA`, `ZERONA`

- **Pre-built Factors** (no parentheses needed):
  - Period: `ItemNameQ`, `ItemNameA`, `ItemNameTTM`, `ItemNamePQ`, `ItemNamePY`
  - Growth: `ItemNameGr%TTM`, `ItemNameGr%A`, `ItemNameGr%PYQ`, `ItemNameGr%PQ`
  - Per Share: `ItemNamePSA`, `ItemNamePSQ`
  - Ratios: `ItemName%AssetsA`, `ItemName%SalesQ`
  - Regression: `ItemNameRegGr%ANN`, `ItemNameRSD%TTM`
  - Average: `ItemName3YAvg`, `ItemName5YAvg`

### Critical Function Name Differences

P123 uses its own naming conventions that differ from common financial terminology:

| Common Name | P123 Function Name |
|-------------|-------------------|
| High price | `Hi()` (not `High()`) |
| Volume | `Vol()` (not `Volume()`) |
| Cost of Goods Sold | `CostG()` (not `COGS()`) |
| Gross Profit | `GrossProfit()` (not `GrProfit()`) |
| SG&A | `SGandA()` (not `SGA()`) |
| Pre-tax Income | `IncBTax()` (not `PreTaxInc()`) |
| Income Tax | `IncTaxExp()` (not `IncomeTax()`) |
| Operating Cash Flow | `OperCashFl()` (not `OpCashFl()`) |
| Long-term Debt | `DbtLT()` (not `LTDebt()`) |
| Total Debt | `DbtTot()` (not `TotDebt()`) |
| Shares Outstanding | `Shares()` (not `ShOut()`) |
| Shares Diluted | `SharesFD()` (not `ShOutDil()`) |
| EPS (basic) | `EPSExclXor()` (not `EPS()`) |
| Dividends per Share | `DivPS()` (not `DPS()`) |
| FFO (REITs) | `FundsFromOp()` (not `FFO()`) |
| Stock Compensation | `StkOptExp()` (not `StockComp()`) |
| Preferred Dividends | `PfdDiv()` (not `PrefDiv()`) |
| Deferred Tax + IC | `TxDfdIC()` (not `DefTaxInvCr()`) |
| DMI+ | `DMIPlus()` (not `PlusDI()`) |
| DMI− | `DMIMinus()` (not `MinusDI()`) |
| Gross Margin | `GMgn%TTM` (not `GrMgn%TTM`) |
| Net Profit Margin | `NPMgn%TTM` (not `NetMgn%TTM`) |
| Debt/Equity | `DbtTot2EqQ` (not `DebtToEqQ`) |

### Ranking System Structure (XML)

Ranking systems use XML in the text editor. The correct schema uses `<Composite>`,
`<StockFactor>`, and `<StockFormula>` tags. **Always read `references/ranking-system-xml.md`
before writing any ranking system XML** — it contains the verified schema, correct
pre-built factor names, and known errors to avoid.

Minimal correct example:

```xml
<RankingSystem RankType="Higher">
  <Composite Name="Value" Weight="50" RankType="Higher">
    <StockFactor Weight="50" RankType="Lower" Scope="Industry">
      <Factor>PEExclXorTTM</Factor>
    </StockFactor>
    <StockFormula Weight="50" RankType="Higher" Name="EBITDA to EV" Description="" Scope="Universe">
      <Formula>OpIncBDeprTTM/EV</Formula>
    </StockFormula>
  </Composite>
  <Composite Name="Quality" Weight="50" RankType="Higher">
    <StockFactor Weight="100" RankType="Higher" Scope="Industry">
      <Factor>ROI%TTM</Factor>
    </StockFactor>
  </Composite>
</RankingSystem>
```

### Common Factor Investing Strategies on P123

**Value**: PEExclXorTTM, Pr2BookQ, Pr2SalesTTM, Pr2FrCashFlTTM, EV2EBITDATTM
**Momentum**: Ret%Chg(252, 21), Pr52W%Chg, Pr52WRel%Chg, RSI(14)
**Quality**: ROE%TTM, ROA%TTM, GMgn%TTM, OpMgn%TTM, PiotFScore
**Low Volatility**: PctDev(52, 5), BetaFunc(52, 104), StdDev(252)
**Size**: MktCap, Close(0)
**Growth**: SalesGr%TTM, EBITDAGr%TTM, ConsEstMean(#EPS, #NY) / ConsEstMean(#EPS, #CY) - 1

## Quick Start Examples

### Screen Rule: Cheap, Profitable, Momentum

```
// Universe filter
MktCap > 500
AvgDailyTot(63) > 500

// Value
PEExclXorTTM < 20

// Quality
ROE%TTM > 15

// Momentum (12-1 month)
Ret%Chg(252, 21) > 0
```

### API: Run a Screen

```python
import p123api

client = p123api.Client(api_id='YOUR_ID', api_key='YOUR_KEY')
result = client.screen_run({
    'screen': {
        'type': 'stock',
        'universe': 'SP500',
        'maxNumHoldings': 25,
        'method': 'long',
        'ranking': {'formula': 'PEExclXorTTM', 'lowerIsBetter': True},
        'rules': [
            {'formula': 'MktCap > 1000', 'type': 'long'},
            {'formula': 'ROE%TTM > 10', 'type': 'long'}
        ]
    },
    'asOfDt': '2025-01-01'
}, True)  # True = Pandas DataFrame
```

### API: Retrieve Factor Data for ML

```python
result = client.data_universe({
    'universe': 'SP500',
    'asOfDts': ['2025-03-08'],
    'formulas': ['PEExclXorTTM', 'ROE%TTM', 'MktCap', 'Ret%Chg(252)'],
    'names': ['PE', 'ROE', 'MktCap', 'Mom12M'],
    'precision': 4,
    'includeNames': True
}, to_pandas=True)
```

## Important Notes

- All P123 formulas are **point-in-time** — they evaluate using only data available on the as-of date
- `NA` handling is critical: use `FALLBACK` (fills from prior period), `KEEPNA`, or `ZERONA`
- Screen rules are **AND** conditions (all must be true); use `OR` keyword for disjunction
- In ranking systems, `RankType="Lower"` means lower values get higher ranks (e.g., PE ratio). See `ranking-system-xml.md`
- The API uses credits: `data` = 1 per 100K points, `screen_run` = 2, `screen_backtest` = 5
- Weekend dates should be used for `asOfDts` in `data_universe()` calls
- Bars = trading days (~251/year, ~21/month, ~5/week); use `#Year`, `#Month`, `#Week` constants
- FRank sort params are `#ASC` / `#DESC` (uppercase); NA params are `#InclNA`, `#ExclNA`, `#NANeutral`
- Aggregate only supports `#Avg` and `#CapAvg` as methods; use `FMedian()`, `FSum()`, `FCount()` for other stats
- `FHist()` returns a single point-in-time value; `FHistAvg()` returns the average of multiple samples

## Resources

- API Swagger: https://api.portfolio123.com/docs/index.html
- Help Center: https://portfolio123.customerly.help/en
- Community Forum: https://community.portfolio123.com/
- p123api PyPI: https://pypi.org/project/p123api/
- DataMiner Examples (Google Colab): https://drive.google.com/drive/u/0/folders/1F3geOi2IYIbdb9obDj8U_o2aDTjw6Fpr

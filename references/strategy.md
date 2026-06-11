# Strategy - Portfolio123 Reference

Strategy factors and functions are evaluated inside a Portfolio123 Strategy (simulation or
live portfolio) when buy and sell rules run. They expose portfolio-level state (cash, total
value, age), per-position state (gain, age, weight, distance from high), and diversification
counts and weights (sector, industry, market-cap group, ETF taxonomy). For general formula
operators, ranking and cross-sectional functions, see [Advanced Functions](advanced-functions.md);
for price and volume functions usable in rules, see [Technical](technical.md). For the buy/sell
rule syntax and worked rule patterns, see the [Buy/Sell Rule Patterns](#buysell-rule-patterns)
section below.

Coverage line: 4 functions / 51 factors - extracted from the official Factor Reference on
2026-06-09. Official subcategories: General; Diversification; Position.

## Contents

- [General](#general)
- [Diversification](#diversification)
- [Position](#position)
- [Buy/Sell Rule Patterns](#buysell-rule-patterns)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

---

## General

Portfolio-level state available in buy and sell rules.

### Factors

| Factor | Description | Period |
|---|---|---|
| `PortCash` | Amount of cash in the portfolio or simulation. | |
| `CashPct` | Cash in the portfolio/simulation as a percentage of total market value. | |
| `PortBars` | Number of bars (trading days) since portfolio/simulation inception. | |
| `SimWeeks` | Number of weeks since inception. | |
| `TotMktVal` | Total value of the portfolio/simulation, including cash. | |

The official descriptions note common idioms verbatim: `PortBars` is used to ensure enough
history before averaging portfolio equity (for example `PortBars<20 or Close(0,#Equity) >
SMA(20,0,#Equity)`), and `SimWeeks` supports periodic rebalancing (for example a weekly
simulation can buy every 13 weeks with `Mod(SimWeeks,13)=0`).

---

## Diversification

Counts and weights of current holdings grouped by country, industry, sector, market-cap band,
and (for ETF strategies) ETF taxonomy. For a buy rule the count or weight is evaluated as if
the stock is purchased; for a sell rule it is evaluated before the sell.

### Functions

#### `MaxCorrel(period_bars, pct_bars)`

Maximum correlation coefficient of the stock being evaluated versus the existing holdings.

| Parameter | Description |
|---|---|
| `period_bars` | Number of bars used in the correlation series. |
| `pct_bars` | Bars used to compute the percent price change (1 for daily, 5 for weekly, etc.). |

To avoid buying stocks correlated above 0.5 on the 1-day price-change series over the past
50 bars, use `MaxCorrel(50, 1) < 0.5` as a buy rule.

### Factors - Country and Industry

| Factor | Description | Period |
|---|---|---|
| `CountryCount` | Number of positions in the country of domicile. | |
| `IndCount` | Number of positions in the industry. | |
| `IndWeight` | Weight of the industry as a percentage of total market value. | |
| `SubIndCount` | Number of positions in the sub-industry. | |
| `SubIndWeight` | Weight of the sub-industry as a percentage of total market value. | |

### Factors - Sector

| Factor | Description | Period |
|---|---|---|
| `SecCount` | Number of positions in the sector. | |
| `SecWeight` | Weight of the sector as a percentage of total market value. | |
| `SubSecCount` | Number of positions in the sub-sector. | |
| `SubSecWeight` | Weight of the sub-sector as a percentage of total market value. | |

### Factors - Market-Cap Concentration

P123 defines the cap bands as MicroCap (0–250M), SmallCap (250M–1B), MidCap (1B–5B), and
LargeCap (greater than 5B). The grouped `CapCount`/`CapWeight` return the count/weight for the
band of the stock in context; the band-specific factors return a fixed band.

| Factor | Description | Period |
|---|---|---|
| `CapCount` | Number of positions in the market-cap group of the stock in context. | |
| `CapWeight` | Weight of the market-cap group of the stock in context, as a percentage of total market value. | |
| `MicroCount` | Number of positions in the MicroCap group. | |
| `MicroWeight` | Weight of the MicroCap group as a percentage of total market value. | |
| `SmallCount` | Number of positions in the SmallCap group. | |
| `SmallWeight` | Weight of the SmallCap group as a percentage of total market value. | |
| `MidCount` | Number of positions in the MidCap group. | |
| `MidWeight` | Weight of the MidCap group as a percentage of total market value. | |
| `LargeCount` | Number of positions in the LargeCap group. | |
| `LargeWeight` | Weight of the LargeCap group as a percentage of total market value. | |

### Factors - ETF Taxonomy

For ETF strategies. Each `*Count`/`*Weight` pair returns the number of positions / weight in
the ETF category named by the factor.

| Factor | Description | Period |
|---|---|---|
| `ETFClassCount` | Number of positions in the ETF asset-class category. | |
| `ETFClassWeight` | Weight of the ETF asset-class category as a percentage of total market value. | |
| `ETFCountryCount` | Number of positions in the ETF country category. | |
| `ETFCountryWeight` | Weight of the ETF country category as a percentage of total market value. | |
| `ETFFamilyCount` | Number of positions in the ETF family category. | |
| `ETFFamilyWeight` | Weight of the ETF family category as a percentage of total market value. | |
| `ETFMethodCount` | Number of positions in the ETF method category. | |
| `ETFMethodWeight` | Weight of the ETF method category as a percentage of total market value. | |
| `ETFRegionCount` | Number of positions in the ETF region category. | |
| `ETFRegionWeight` | Weight of the ETF region category as a percentage of total market value. | |
| `ETFSecCount` | Number of positions in the ETF sector category. | |
| `ETFSecWeight` | Weight of the ETF sector category as a percentage of total market value. | |
| `ETFSizeCount` | Number of positions in the ETF size category. | |
| `ETFSizeWeight` | Weight of the ETF size category as a percentage of total market value. | |
| `ETFStyleCount` | Number of positions in the ETF style category. | |
| `ETFStyleWeight` | Weight of the ETF style category as a percentage of total market value. | |

---

## Position

Per-position state. Available in sell rules (and in buy rules where a previously held position
is referenced, such as `LastSellPrice`).

### Functions

#### `PctAvgDailyTot(bars [, offset])`

Percentage that the trade represents compared to the liquidity for the stock. The trade amount
is shares times last close; liquidity is the average of price times volume over `bars`.

| Parameter | Description |
|---|---|
| `bars` | Number of bars used to average daily dollar volume. |
| `offset` | Offset in bars (optional). |

To avoid buying a stock if the trade would exceed 5% of the 20-day liquidity, use the buy
restriction `PctAvgDailyTot(20) < 5`.

#### `LastSellDaysLT(days)`

Returns TRUE (1) if the stock was sold within the last `days` calendar days, otherwise FALSE.

#### `HoldingsCnt("MyListName")`

Count of stocks in the named list that are current holdings.

### Factors

| Factor | Description | Period |
|---|---|---|
| `NoBars` | Trading days since the position was first opened (excludes weekends and holidays). | |
| `NoDays` | Calendar days since the position was first opened. | |
| `GainPct` | Return of the position as a percentage (dividends not included). | |
| `Gain` | Dollar return of the position. | |
| `PctFromHi` | Percentage from the highest close since the position started; always 0 or negative. | |
| `Weight` | Weight of the position as a percentage of total portfolio market value. | |
| `BuyAmount` | Amount used to buy the stock, before commissions or slippage. | |
| `BenchPct` | Benchmark return since the position was opened. | |
| `BenchPctFromPosHi` | Benchmark percentage return from the highest close of the position. | |
| `LastSellPrice` | Price the stock was last sold at, or NA. | |
| `PosCnt` | Number of positions in the portfolio during a rebalance. | |

Common idioms from the official descriptions: a 20% trailing stop is `PctFromHi <= -20`; a
relative stop that does not fire when the market is also dropping is
`PctFromHi <= -20 And BenchPctFromPosHi > -20`; a time-and-relative exit is
`GainPct < BenchPct & NoDays > 30`; and `LastSellPrice` is tested for re-entry with
`Eval(LastSellPrice=NA,TRUE,Close(0) > LastSellPrice)`.

---

## Buy/Sell Rule Patterns

A Strategy uses buy rules to decide which stocks/ETFs may be bought and sell rules to decide
when to exit. The rule syntax and the patterns below come from community PR #4; every factor
and function name in them has been re-verified against the official dictionary. (PR #4 also
corrected the NA-test idiom - see [Common Mistakes](#common-mistakes) and the
[IsNA verdict in Advanced Functions](advanced-functions.md#na-handling-isna-arity).)

### Buy rules

Buy rules tell a Strategy which stocks/ETFs can be bought. All buy rules must be true to buy
(they are AND'ed). If no buy rules are specified, the strategy keeps buying the next
highest-ranked stock until all cash is used.

```p123
[Buy1] Close(0) > SMA_W(43)
[Buy2] RankPos < 5
```

### Sell rules

Sell rules tell the Strategy when to sell a position. Any single sell rule that is true
triggers a sell (they are OR'ed). Strategies often, but not always, sell on `RankPos` or
`Rank`. A rule prefixed with `[OFF]` is disabled.

```p123
[Sell1] RankPos > 80
[Sell2] Rank < 60
[OFF] [Sell3]
[Sell4] FRank("LoopAvg(`Spread(CTR)`,20)",#All,#ASC) <= 5
[Sell5] LoopMin("AvgDailyTot(5,CTR)",10,0,5) <= 50000
[Sell6] FRank("FCount(`SMA(50) > SMA(200)`, #Industry) / FCount(`1`, #Industry)") <= 25
[Sell7] SecCount >= 5 and IndCount >= 2
```

Notes on the verified patterns:

- `Close(0) > SMA_W(43)` requires price above the 43-week simple moving average.
- `RankPos` and `Rank` come from the Strategy's selected ranking system; see
  [Advanced Functions - Ranking](advanced-functions.md#ranking).
- The `[Sell4]` rule ranks on average bid-ask spread; `[Sell5]` checks minimum daily dollar
  volume; `[Sell6]` ranks on the fraction of the industry in an uptrend.
- `SecCount` and `IndCount` are diversification counts (see [Diversification](#diversification)).

PR #4 wrote some names in lowercase (for example the moving-average and rank functions); this
reference normalizes them to the canonical dictionary casing (`SMA`, `FRank`) throughout -
always use the casing exactly as listed in the reference files.

---

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `SectorCount` | `SecCount` | The sector position count is `SecCount`. The spelled-out form is not a valid name. |
| `Eval(IsNA(LastSellPrice), ...)` | `Eval(LastSellPrice=NA, ...)` | `IsNA` takes two arguments; test for NA with `expression = NA`. See [Advanced Functions](advanced-functions.md#na-handling-isna-arity). |

---

## See Also

- [Advanced Functions](advanced-functions.md) - ranking, FRank/FCount, loop functions, NA handling.
- [Technical](technical.md) - price, volume, and moving-average functions usable in rules.
- [Ranking System XML](ranking-system-xml.md) - building the ranking system a Strategy sells on.

# Advanced Functions - Portfolio123 Reference

Advanced functions add cross-sectional ranking, historical and loop-based time series,
regression, ranking-system access, AI-factor predictions, and screen/watchlist/account holdings
logic to the P123 formula language. For the conditional and NA-handling operators (`Eval`,
`IsNA`, `IsNeg`) and set statistics (`StdDev`, `RelStdDev`) see [Misc](misc.md); those are their
official home category. The single- vs. two-argument `IsNA` defect is adjudicated here because
loop and ranking formulas are where it most often bites - see
[NA handling (IsNA arity)](#na-handling-isna-arity). For price and volume functions see
[Technical](technical.md); for buy/sell rule state see [Strategy](strategy.md).

Coverage line: 60 functions / 11 factors - extracted from the official Factor Reference on
2026-06-09. Official subcategories: AI Factor; Ranking; FHist Functions; Loop Functions; Loop
Regression; Relative vs. History; Relative vs. Group; Group Summary Statistics; Screener Only;
Watchlists, Holdings, & Opinions.

## Contents

- [NA handling (IsNA arity)](#na-handling-isna-arity)
- [Scope values](#scope-values)
- [AI Factor](#ai-factor)
- [Ranking](#ranking)
- [FHist Functions](#fhist-functions)
- [Loop Functions](#loop-functions)
- [Loop Regression](#loop-regression)
- [Relative vs. History](#relative-vs-history)
- [Relative vs. Group](#relative-vs-group)
- [Group Summary Statistics](#group-summary-statistics)
- [Screener Only](#screener-only)
- [Watchlists, Holdings, & Opinions](#watchlists-holdings--opinions)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

---

## NA handling (IsNA arity)

`IsNA` is a **two-argument** function. The official signature is `IsNA(expr1, expr2)`: it
returns `expr1` when `expr1` is not NA, otherwise it returns `expr2`. There is **no**
single-argument `IsNA(x)` boolean form. To test whether a value is NA, compare it to the `NA`
constant: `expression = NA`.

This resolves a known defect carried by earlier community skill versions, which used
`IsNA(x)` as if it returned a boolean (for example `Eval(IsNA(PEExclXorTTM), ..., ...)`). That
usage does not work. The corrected idioms are:

```p123
// Test for NA (the correct boolean form)
Eval(PEExclXorTTM = NA, Pr2SalesTTM, PEExclXorTTM)
// Replace NA with a fallback value (the correct use of IsNA)
IsNA(PEExclXorTTM, Pr2SalesTTM)
// Replace NA with a literal
IsNA(PEExclXorTTM, 999)
```

The related replacement functions share the same two-argument shape (all in
[Misc](misc.md)): `IsNeg(expr1, expr2)`, `IsNegOrNA(expr1, expr2)`, `IsZero(expr1, expr2)`.

Evidence: the dictionary signature for `IsNA` is `expr1, expr2`, and the official Misc/Math
detail page states "IsNA(expr1, expr2) can be used to replace NAs" and "NA values can be
handled using `expression = NA`." The strategy factor description for `LastSellPrice`
independently uses the same idiom: `Eval(LastSellPrice=NA,TRUE,Close(0) > LastSellPrice)`.

All examples in this file and in the sibling reference files use the two-argument `IsNA` and
the `= NA` test.

---

## Scope values

<!-- name-whitelist: #Mean #Median #Sum #Count #Min #Max -->
The group functions (`FRank`, `ZScore`, `Aggregate`, `FOrder`, `FCount`, `FSum`, `FMedian`)
take a scope argument. The 16 official scope constants (descriptions verbatim from the
Factor Reference):

| Scope | Description |
|---|---|
| `#All` | Operate within selected universe (the default). |
| `#Sector` | Operate within Sectors in selected universe. |
| `#Industry` | Operate within Industries in selected universe. |
| `#SubIndustry` | Operate within Sub-Industries in selected universe. |
| `#SubSector` | Operate within Sub-Sectors in selected universe. |
| `#SP500` | Operate within the SP500 stocks. |
| `#Previous` | Operate on the results from previous rule. Available only in the Screener and Custom Universes (official footnote). |
| `#GroupVar` | Operates on groups based on value of variable `@Group`. Not available in Ranking Systems (official footnote). |
| `#Family` | Operate within each ETF Family. |
| `#AssetClass` | Operate within each ETF Class. |
| `#Region` | Operate within each ETF Region. |
| `#Country` | Operate within each ETF Country. |
| `#Method` | Operate within each ETF Method. |
| `#Style` | Operate within each ETF Style. |
| `#Size` | Operate within each ETF Size. |
| `#ETFSector` | Operate within each ETF Sector. |

---

## AI Factor

### Functions

#### `AIFactor("AI Factor Name", "Predictor Name")`

Returns the inferences (predictions) of your trained Predictor. Intended for rebalancing; it
can also be used in backtests with some restrictions.

**Example**
```p123
FRank(`AIFactor("My AI Factor", "lightgbm II predictor")`, #All, #DESC) > 90
```

#### `AIFactorValidation("AI Factor Name", "Model Name" [, "dup_id"])`

Returns the saved inference (prediction) from your model's validation run.

**Example**
```p123
FRank(`AIFactorValidation("My AI Factor", "lightgbm II")`, #All, #DESC) > 90
```

---

## Ranking

### Functions

#### `Rating("RankName")`

Rank (0–100) from the named ranking system. Accepts one of your systems or a P123 pre-built
system. A maximum of 3 `Rating`/`RatingPos` calls may be used per request.

#### `RatingPos("RankName")`

Rank position from the named ranking system (1 = best).

#### `NodeRank("name")`

Rank of a named node within the current ranking system.

#### `GetRank("ticker")`

Rank of the specified ticker.

#### `GetRankPos("ticker")`

Rank position of the specified ticker.

#### `RankPrev(weeksAgo)`

Historical weekly rank based on the selected ranking system (updated every Saturday). The
weeks-ago argument ranges 0–261.

#### `RankPosPrev(weeksAgo)`

Historical weekly rank position. The weeks-ago argument ranges 0–261.

**Example**
```p123
// Rank improved week over week
RankPrev(0) > RankPrev(1)
// Use a node from the current ranking system
NodeRank("Value") > 80
```

### Factors

| Factor | Description | Period |
|---|---|---|
| `Rank` | Latest stock rank, updated daily Tuesday–Saturday. | |
| `RankPos` | Position within the ranked array (1 = highest ranked). | |
| `RankBars` | Number of bars (trading days) since the last rank data. | |

---

## FHist Functions

`FHist` reads a formula's value as it was a number of weeks in the past; the aggregate variants
sample the formula multiple times and summarize. Split/dividend-sensitive values are adjusted to
the as-of (observation) date.

### Functions

#### `FHist("formula", weeksAgo)`

Value of the formula a number of weeks in the past (negative values look into the future).

#### `FHistAvg("formula", samples [, weeks_increment=1, NA_pct=20])`

Average of the formula sampled `samples` times, spaced `weeks_increment` weeks apart.

#### `FHistMax("formula", samples [, weeks_increment=1, NA_pct=20])`

Maximum of the sampled historical values.

#### `FHistMin("formula", samples [, weeks_increment=1, NA_pct=20])`

Minimum of the sampled historical values.

#### `FHistMed("formula", samples [, weeks_increment=1, NA_pct=20])`

Median of the sampled historical values.

#### `FHistSum("formula", samples [, weeks_increment=1, NA_pct=20])`

Sum of the sampled historical values.

#### `FHistStdDev("formula", samples [, weeks_increment=1, NA_pct=20])`

Standard deviation of the sampled historical values.

#### `FHistRelStdDev("formula", samples [, weeks_increment=1, NA_pct=20])`

Relative standard deviation of the sampled historical values.

**Example**
```p123
// Price-to-sales below its 3-year average (39 samples, 4 weeks apart)
Pr2SalesTTM < FHistAvg("Pr2SalesTTM", 39, 4)
```

---

## Loop Functions

Loop functions evaluate a formula multiple times using a `CTR` counter variable that increments
each iteration. Optional parameters control the iteration: start (default 0), increment
(default 1), an NA-skipping flag, and a break-on-NA flag, as shown in each signature.

### Functions

#### `LoopAvg("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Average of the iterated values.

#### `LoopMax("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Maximum of the iterated values.

#### `LoopMin("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Minimum of the iterated values.

#### `LoopMedian("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Median of the iterated values.

#### `LoopSum("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Sum of the iterated values.

#### `LoopProd("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Product of the iterated values.

#### `LoopStdDev("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Standard deviation of the iterated values.

#### `LoopRelStdDev("formula(CTR)", iterations [, start=0, increment=1, noNAs=FALSE, break=FALSE])`

Relative standard deviation of the iterated values.

#### `LoopStreak("formula(CTR)", iterations [, start=0, increment=1, streak=#Positive, recent=TRUE])`

Streak count of the iterated values; by default the most recent streak of positive values.

**Example**
```p123
// Recreate SMA(5)
LoopAvg("Close(CTR)", 5)
// Count up-days over the past 10 bars
LoopSum("Close(CTR) > Close(CTR + 1)", 10)
// Quarters of rising after-tax income, 8 of the last 10
LoopSum("IncAftTax(CTR, QTR) > IncAftTax(CTR + 1, QTR)", 10) >= 8
// Closed higher than the previous day for more than 10 days in a row
LoopStreak("Close(CTR)", 21, 0, 1, #Increasing, TRUE) > 10
```

---

## Loop Regression

These run a regression over loop-iterated values and return TRUE on success. Place the
regression statistics (`Slope`, `R2`, `SurpriseY`, etc.) immediately after the call.

### Functions

#### `LinReg("Formula(CTR)", iterations [, start, increment])`

Time-series regression over the iterated values.

#### `LinRegXY("X-Formula(CTR)", "Y-Formula(CTR)", iterations [, start, increment])`

Bivariate (XY) regression over the iterated value pairs.

**Example**
```p123
// 10-year sales regression: positive slope, good fit, latest above trend
LinReg("Sales(CTR, ANN)", 10) = TRUE
R2 > 0.8 and Slope > 0 and SurpriseY(0) > 0
// Rank on the slope of the past 60 prices when the regression succeeds
Eval(LinReg("Close(CTR)", 60), Slope, NA)
```

Regression statistics available after a successful regression: `Slope`, `SlopeConf%`,
`SlopePVal`, `SlopeSE`, `SlopeTStat`, `R`, `R2`, `Intercept`, `InterceptSE`, `SE`, `Samples`,
`EstimateY(offset)`, `EstimateXY(X)`, `SurpriseY(offset)`, and `RegGr%([period])`. (These stats
and `LinRegVals` / `LinRegXYVals` are documented in [Misc](misc.md).)

---

## Relative vs. History

Compare the most recent value of a formula to its own historical (or loop-iterated) values.

### Functions

#### `FHistRank("formula", samples [, weeks_increment=1, sort=#DESC, sort_style=#Top, NA_value=NA, NA_pct=20])`

Percentile rank (0–100) of the most recent value versus previous point-in-time values.

#### `FHistRel("formula", samples [, weeks_increment=1, NA_value=NA, NA_pct=20])`

Relative position (0–1) of the most recent value between the historical minimum and maximum.

#### `FHistZScore("formula", samples [, weeks_increment=1, clip=3.5, NA_value=NA, NA_pct=20])`

Z-score of the most recent value versus previous point-in-time values.

#### `LoopRank("formula(CTR)", iterations [, start=0, increment=1, sort=#DESC, sort_style=#Top, NA_value=NA, NA_pct=20])`

Percentile rank of the most recent loop value versus the other iterated values.

#### `LoopRel("formula(CTR)", iterations [, start=0, increment=1, NA_value=NA, NA_pct=20])`

Relative position (0–1) of the most recent loop value between the iterated minimum and maximum.

#### `LoopZScore("formula(CTR)", iterations [, start=0, increment=1, clip=3.5, NA_value=NA, NA_pct=20])`

Z-score of the most recent loop value versus the other iterated values.

**Example**
```p123
// Gross margin in the top decile vs. the last 20 reported values
LoopRank("GMgn%(CTR, TTM)", 20) >= 90
```

---

## Relative vs. Group

Cross-sectional ranking and scoring across a scope (see [Scope values](#scope-values)).

### Functions

#### `FRank("formula" [, scope=#All, sort=#DESC, incl_na=#InclNA, sort_style=#Top])`

Ranks stocks on a formula and returns the percentile (0–100). `sort` is `#DESC` (higher value
ranks higher) or `#ASC` (lower value ranks higher, e.g. for valuation). `incl_na` is `#InclNA`,
`#ExclNA`, or `#NANeutral`. `sort_style` is `#Top` or `#Neutral`.

#### `FOrder("formula" [, scope=#All, sort=#DESC, distinct=FALSE, incl_na=#InclNA])`

Sorts stocks on a formula and returns the position in the array (1, 2, 3, ...).

#### `ZScore("formula" [, scope=#All, outlier_pct=7.5, na_value=0, max_zscore=3.5])`

Number of standard deviations from the cross-sectional mean, clipped to `±max_zscore`.

**Example**
```p123
// Cheapest quintile (low PE is good, so #ASC)
FRank("PEExclXorTTM", #All, #ASC) > 80
// Sector-relative quality
FRank("ROE%TTM", #Sector, #DESC) > 70
// Complex expression with backticks
FRank(`Close(0)/Close(252)`, #All, #DESC) > 90
```

---

## Group Summary Statistics

Group statistics across a scope. `FRank`, `FOrder`, and `ZScore` are covered under
[Relative vs. Group](#relative-vs-group).

### Functions

#### `Aggregate("formula", scope [, method, outlier_pct, outlier_handl, excl_zero, excl_adrs, median_fallback])`

Average (`method = #Avg`, default) or cap-weighted average (`method = #CapAvg`) of the formula
in each scope. `outlier_handl` is `#Exclude` (default) or `#Winsor`. P123 does not support
`#Mean`, `#Median`, `#Sum`, `#Count`, `#Min`, or `#Max` as `Aggregate` methods - use `FMedian`,
`FSum`, `FCount`, or `ZScore` for those.

#### `FCount("formula" [, scope])`

Count of stocks in the scope where the formula is true (non-zero).

#### `FMedian("formula" [, scope, excl_zero])`

Median value of the formula in the scope.

#### `FSum("formula" [, scope])`

Sum of the formula values in the scope.

**Example**
```p123
// Cheaper than the industry average PE
PEExclXorTTM < Aggregate("PEExclXorTTM", #Industry, #Avg)
// How many sector peers have PE below 20
FCount("PEExclXorTTM < 20", #Sector)
// Larger than the industry median market cap
MktCap > FMedian("MktCap", #Industry)
```

---

## Screener Only

These functions work only in the screener.

### Functions

#### `Screen("ScreenName", top)`

Runs the named screen; if `top > 0`, returns only the top `top` stocks. Enables screens of
screens.

#### `ShowCorrel(period, samples)`

Produces a correlation matrix in the screen report.

#### `ShowVar(@myvar, expression)`

Sets the variable `@myvar` to `expression`, returns TRUE, and displays `@myvar` in the screen
report. (`SetVar` itself lives in [Misc](misc.md).)

### Factors

| Factor | Description | Period |
|---|---|---|
| `SecCount` | Running count of stocks in the sector (must be the last rule). | |
| `SubSecCount` | Running count of stocks in the sub-sector (must be the last rule). | |
| `IndCount` | Running count of stocks in the industry (must be the last rule). | |
| `SubIndCount` | Running count of stocks in the sub-industry (must be the last rule). | |

---

## Watchlists, Holdings, & Opinions

Membership and timing of a stock in your watchlists, account, and portfolio positions, plus
recorded opinions. For the `id` parameters use either the name in quotes or the numeric ID.

### Functions - Watchlists

#### `WatchlistCurrent("Name")`

Returns TRUE if the stock is currently in your watchlist.

#### `Watchlist(id1 [, .., id10])`

Returns TRUE if the stock was in the watchlist on the date in question.

#### `WatchlistOpen(id1 [, .., id10])`

Calendar days since the stock was first added, otherwise NA.

#### `WatchlistOpenBar(id1 [, .., id10])`

Bars since the stock was first added, otherwise NA.

#### `WatchlistClose(id1 [, .., id10])`

Calendar days since the stock was last removed; -1 if currently in the watchlist; NA if not
added within the past 6 months.

#### `WatchlistCloseBar(id1 [, .., id10])`

Bars since the stock was last removed; -1 if currently in the watchlist; NA otherwise.

### Functions - Account Holdings

#### `Account(id1 [, .., id10])`

Returns TRUE if the stock is an open position in the account.

#### `AccountOpen(id1 [, .., id10])`

Calendar days since the position was first opened, otherwise NA.

#### `AccountOpenBar(id1 [, .., id10])`

Bars since the position was first opened, otherwise NA.

#### `AccountClose(id1 [, .., id10])`

Calendar days since the position was last closed; -1 if currently held; NA if not held within
the past 6 months.

#### `AccountCloseBar(id1 [, .., id10])`

Bars since the position was last closed; -1 if currently held; NA otherwise.

### Functions - Portfolio Holdings

#### `Portfolio(id1 [, .., id10])`

Returns TRUE if the stock is an open position in the portfolio.

#### `PortfolioOpen(id1 [, .., id10])`

Calendar days since the position was first opened, otherwise NA.

#### `PortfolioOpenBar(id1 [, .., id10])`

Bars since the position was first opened, otherwise NA.

#### `PortfolioClose(id1 [, .., id10])`

Calendar days since the position was last closed; -1 if currently held; NA otherwise.

#### `PortfolioCloseBar(id1 [, .., id10])`

Bars since the position was last closed; -1 if currently held; NA otherwise.

### Factors - Recent Opinion

| Factor | Description | Period |
|---|---|---|
| `Opinion` | Your most recent opinion for the stock, or NA. | |
| `Opinion%Chg` | Total return percent since your most recent opinion. | |
| `OpinionBars` | Bars since your most recent opinion. | |
| `OpinionDays` | Calendar days since your most recent opinion. | |

---

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `IsNA(PEExclXorTTM)` | `PEExclXorTTM = NA` | `IsNA` takes two arguments; test for NA with `expression = NA`. |
| `Eval(IsNA(x), a, b)` | `Eval(x = NA, a, b)` | Single-argument `IsNA` as a boolean does not work. |
| `LatestRank` | `Rank` | The latest daily rank factor is `Rank`. |
| `OtherRank("name")` | `Rating("name")` | Cross-system rank is `Rating` / `RatingPos`. |
| `SectorCount` | `SecCount` | The sector running count is `SecCount`. |
| `RegEst(0)` | `EstimateY(0)` | The regression Y-estimate function is `EstimateY`. |

---

## See Also

- [Misc](misc.md) - `SetVar`, `Eval`, `IsNA`, set statistics, and regression-value functions.
- [Technical](technical.md) - price, volume, and moving-average functions.
- [Strategy](strategy.md) - buy/sell rule state and ranking-based exits.
- [Ranking System XML](ranking-system-xml.md) - building ranking systems that `Rating`/`Rank` read.

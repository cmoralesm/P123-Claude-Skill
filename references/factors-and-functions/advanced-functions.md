# Advanced Functions

Advanced functions that provide things like summary statistics, ranks, and other specific analytics.

## AI Factor

Functions that return AI model predictions

### Predictions

Returns the inferences (predictions) of your trained Predictor. Mainly for use to rebalance but it can also be used in backtests with some restrictions.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `AIFactor()` | "AI Factor Name", "Predictor Name" |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AIFactor |


### Validation Predictions

Returns the saved inference (prediction) of your model's validation

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `AIFactorValidation()` | "AI Factor Name", "Model Name"[, "dup_id"] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AIFactorValidation |


## Ranking

Functions that return the rank from a ranking system.

### Other Rank

Returns the rank position for the named Ranking System. You can specify one of your systems or one of our pre-built ranking systems. Example:

RatingPos("Momentum Value")<10

NOTE: A maximum of 3 Rating/RatingPos functions can be used for a request.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RatingPos()` | "RankName" |  |  |
| `Rating()` | "RankName" |  |  |


### Previous Rank

Historical weekly rank position based on the selected ranking system. Weekly ranks are updated every Saturday.

weeksAgo: number of weeks from 0-261.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RankPosPrev()` | weeksAgo |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RankPosPrev |
| `RankPrev()` | weeksAgo |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RankPrev |


### Latest Rank

Latest stock rank updated daily Tuesday-Saturday. Usage examples:

Portfolios and Sims: to sell a position when rank drops below 60, enter the following SELL rule:

Rank < 60

Screener: to screen for stocks with a Rank above 90 select the Ranking System to use and enter the following rule:

Rank > 90

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Rank` |  |  |  |
| `RankPos` |  |  |  |
| `GetRank()` | "ticker" |  |  |
| `GetRankPos()` | "ticker" |  |  |


### Rank Bars

Returns the number of bars of the last rank data. NOTE: A "bar" is a trading day. Therefore there are 5 bars in a week with no holidays.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RankBars` |  |  |  |


### Node Rank

Returns the node rank within a ranking system. Please see the Full Description for details and examples.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NodeRank()` | "name" |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NodeRank |


## FHist Functions

Functions that calculate Point In Time values (PIT) by changing the observation date. An example use case for these functions is to find stocks that are cheap relative to their previous valuations.

### Historical Average

Returns the average of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistAvg()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistAvg |


### Historical Max

Returns the maximum value of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistMax()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistMax |


### Historical Median

Returns the median of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistMed()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistMed |


### Historical Min

Returns the minimum value of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistMin()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistMin |


### Historical Relative Standard Deviation

Returns the RSD of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistRelStdDev()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistRelStdDev |


### Historical Standard Deviation

Returns the SD of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistStdDev()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistStdDev |


### Historical Sum

Returns the sum of 'formula' sampled multiple times in the past. Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistSum()` | "formula", samples [, weeks_increment=1, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistSum |


### Point In Time Value

Returns the value of 'formula' calculated in the past (or future when using negative values). Split/dividend sensitive values adjusted to the as-of date (observation date).

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHist()` | "formula", weeksAgo |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHist |


## Loop Functions

Functions that operate on historical values using a loop formula which must contain the CTR iterator. Example use cases for these functions include counting how many quarters have positive cashflow, and finding companies that have increased their dividend every year.

### Loop Average

Evaluates the "formula" parameter a number of times and return the average. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopAvg()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopAvg |


### Loop Max

Evaluates the "formula" parameter a number of times and return the maximum value. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopMax()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopMax |


### Loop Median

Evaluates the "formula" parameter a number of times and returns the median value. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopMedian()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopMedian |


### Loop Min

Evaluates the "formula" parameter a number of times and returns the minimum value. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopMin()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopMin |


### Loop Product

Evaluates the "formula" parameter a number of times and returns the product of the values. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopProd()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopProd |


### Loop Rel Standard Deviation

Evaluates the "formula" parameter a number of times and returns the relative standard deviation. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopRelStdDev()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopRelStdDev |


### Loop Standard Deviation

Evaluates the "formula" parameter a number of times and returns the standard deviation. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopStdDev()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopStdDev |


### Loop Streak

Evaluates the "formula" parameter a number of times and returns the streak count.  By default it returns the most recent streak of positive values. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopStreak()` | "formula(CTR)", iterations[, start=0, increment=1, streak=#Positive, recent=TRUE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopStreak |


### Loop Sum

Evaluates the "formula" parameter a number of times and returns the sum of the values. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopSum()` | "formula(CTR)", iterations[, start=0, increment=1, noNAs=FALSE, break=FALSE] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopSum |


## Loop Regression

Functions that calculate regressions on historical values using a loop formula which must contain the CTR iterator. Use cases for these functions include finding stocks with upward, well defined trends for sales.

### Linear Regression using Loop

Executes the "formula" parameter a number of times and operates a regression on the set of values. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LinReg()` | "Formula(CTR)", iterations[, start, increment] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LinReg |


### Linear XY Regression using Loop

Executes the "formula" parameter a number of times and operates a bivariate regression on the set of values. A special CTR variable must be used inside "formula".

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LinRegXY()` | "X-Formula(CTR)", "Y-Formula(CTR)", iterations[, start, increment] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LinRegXY |


## Relative vs. History

Functions that compare and normalize values longitudinally against historical values for the same stock.

### FHist Rank

Returns the percentile rank from 0 to 100 of most recent value vs. previous PIT values.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistRank()` | "formula", samples[, weeks_increment=1, sort=#DESC, sort_style=#Top, NA_value=NA, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistRank |


### FHist Relative

Returns the relative value from 0 to 1 of most recent value vs. previous minimum and maximum PIT values.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistRel()` | "formula", samples [, weeks_increment=1, NA_value=NA, NA_Pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistRel |


### FHist ZScore

Returns the zscore of most recent value vs. previous PIT values.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FHistZScore()` | "formula", samples, weeks_increment=1, clip=3.5, NA_value=NA, NA_pct=20 |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FHistZScore |


### Loop Rank

Returns the rank of most recent value of the Loop formula vs. previous values calculated by iterating the CTR variable.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopRank()` | “formula(CTR)”, iterations[, start=0, incr=1, sort=#DESC, sort_style=#Top, NA_value=NA, NA_Pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopRank |


### Loop Relative

Returns the relative value from 0 to 1 of most recent value of the Loop formula vs. previous minimum and maximum values calculated by iterating the CTR variable.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopRel()` | "formula(CTR)", iterations[, start=0, increment=0, NA_value=NA, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopRel |


### Loop ZScore

Returns the zscore of most recent value of the Loop formula vs. previous values calculated by iterating the CTR variable.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LoopZScore()` | "formula(CTR)", iterations[, start=0, increment=1, clip=3.5, NA_value=NA, NA_pct=20] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LoopZScore |


## Relative vs. Group

Functions that compare and normalize values cross-sectionally vs. other stocks in a group. Use cases for these functions include screening for stocks that are in the top 10% for a metric in their sector.

### Order in a Group

Sorts stocks based on formula and returns the position in the array.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FOrder()` | "formula" [, scope=#All, sort=#DESC, distinct=FALSE, incl_na=#InclNA] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FOrder |


### Rank in a Group

Ranks stocks based on a formula and returns the percentile.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FRank()` | "formula"[, scope=#All, sort=#DESC, incl_na=#InclNA, sort_style=#Top] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FRank |


### ZScore in a Group

Calculates how many standard deviations the value from the formula is from the mean

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ZScore()` | "formula"[, scope=#All, outlier_pct=7.5, na_value=0, max_zscore=3.5] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ZScore |


## Group Summary Statistics

Functions that calculate cross-sectional summary statistics for a group. An example use case for these functions is to find companies that are cheap relative to their industry or sub-sector.

### Group Average

Returns the average or cap-weighted average for each scope

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Aggregate()` | "formula", scope [, method, outlier_pct, outlier_handl, excl_zero, excl_adrs, median_fallback] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Aggregate |


### Group Count

Counts the number of stocks in each scope where formula is true (non 0)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FCount()` | "formula" [, scope] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FCount |


### Group Median

Returns the median value of the formula in each scope

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FMedian()` | "formula" [, scope, excl_zero] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FMedian |


### Group Sum

Returns the sum value of the formula in each scope

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FSum()` | "formula" [, scope] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FSum |


## Screener Only

Misc functions that only work in the screener.

### Screen Holdings

Runs the screen specified in the first parameter. If top>0 then only the specified top stocks are returned. With this you can create screen-of-screens.

Screen("Graham",7) Or Screen("Lynch",7)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Screen()` | "ScreenName", top |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Screen |


### Sector Count

Running count of stocks in the sector. This rule must be the last rule in the screen.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SecCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SecCount |
| `SubSecCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSecCount |


### Industry Count

Running count of stocks in the industry. This rule must be the last rule in the screen.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IndCount` |  |  |  |
| `SubIndCount` |  |  |  |


### Show Correlation Matrix in report

This function produces a correlation matrix in the screen report

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ShowCorrel()` | period , samples |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ShowCorrel |


### Show/Set Variable function

Sets the variable @myvar to expression, returns TRUE, and displays @myvar in the screen report.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ShowVar()` | @myvar, expression |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ShowVar |


## Watchlists, Holdings, & Opinions

Functions that access holdings in watchlists, portfolios, or accounts as well as functions that access stock opinions.

### Recent Opinion

Returns your most recent opinion for the stock or NA

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Opinion` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Opinion |
| `Opinion%Chg` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Opinion%Chg |
| `OpinionBars` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OpinionBars |
| `OpinionDays` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OpinionDays |


### Watchlist Holdings

Returns TRUE if the stock is currently in your watchlist.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `WatchlistCurrent()` | "Name" |  |  |
| `Watchlist()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Watchlist |
| `WatchlistClose()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WatchlistClose |
| `WatchlistCloseBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WatchlistCloseBar |
| `WatchlistOpen()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WatchlistOpen |
| `WatchlistOpenBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=WatchlistOpenBar |


### Account Holdings

Return TRUE if stock being analyzed is an open position. For the id parameters use either the name in quotes, or the numerical id.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Account()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Account |
| `AccountClose()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AccountClose |
| `AccountCloseBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AccountCloseBar |
| `AccountOpen()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AccountOpen |
| `AccountOpenBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AccountOpenBar |


### Portfolio Holdings

Return TRUE if stock being analyzed is an open position. For the id parameters use either the name in quotes, or the numerical id.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Portfolio()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Portfolio |
| `PortfolioClose()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PortfolioClose |
| `PortfolioCloseBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PortfolioCloseBar |
| `PortfolioOpen()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PortfolioOpen |
| `PortfolioOpenBar()` | id1[, .., id10] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PortfolioOpenBar |


# Technical — Portfolio123 Reference

Technical functions and factors operate on price and volume bar data (trading days by default).
This file covers price (OHLCV), returns and performance, volume and liquidity, moving averages,
accumulation/distribution, trend and directional movement, chart patterns, oscillators, and
volatility. For cross-sectional ranking and loop/regression machinery (`FRank`, `LoopAvg`,
`LinReg`, and friends) see [Advanced Functions](advanced-functions.md); for portfolio and
position state used in buy/sell rules (`PctFromHi`, `GainPct`, `NoBars`) see
[Strategy](strategy.md). Date and set utilities such as `BarsSince`, `StdDev`, and `GetSeries`
live in [Misc](misc.md).

Coverage line: 95 functions / 55 factors — extracted from the official Factor Reference on
2026-06-09. Official subcategories: Performance; Price; Volume; Moving Average; Accumulation;
Trending; Pattern; Oscillators; Volatility.

## Contents

- [Common parameters](#common-parameters)
- [Performance](#performance)
- [Price](#price)
- [Volume](#volume)
- [Moving Average](#moving-average)
- [Accumulation](#accumulation)
- [Trending](#trending)
- [Pattern](#pattern)
- [Oscillators](#oscillators)
- [Volatility](#volatility)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

---

## Common parameters

Most technical functions share these optional parameters:

- **offset** — bars ago to start the calculation (0 = from the latest bar).
- **series** — the price series to use. By default a function reads the time series of the
  instrument in context. You can pass `#Bench` (benchmark), `#Industry` or `#Sector` (index
  prices), `#Equity` (portfolio value, strategies only), a numeric P123 stock ID, or a series
  obtained with `GetSeries("ticker")`.

Many functions also have `_D` (calendar-day) and `_W` (weekly) variants that take the period in
days or weeks instead of trading-day bars. Negative bar arguments peek into the future and are
for labeling/backtesting only.

---

## Performance

### Functions

#### `FXPerf(bars [, offset])`

Ratio used to normalize a stock's performance to the currency of your system.

#### `Ret%Chg(bars [, offset, series])`

Total return (includes dividends) over the period specified.
*Period: Series Dependent*

#### `Ret%Chg_D(days [, offset, series])`

Total return (includes dividends) over the period in calendar days.
*Period: Weekday*

#### `Rel%Chg(bars [, series])`

Total return relative to the benchmark or another series.
*Period: Series Dependent*

#### `Rel%Chg_D(days [, series])`

Total return relative to the benchmark or another series, in calendar days.
*Period: Weekday*

#### `Future%Chg(bars [, series])`

Future total return. For labeling and backtesting only.
*Period: Series Dependent*

#### `Future%Chg_D(days [, series])`

Future total return, in calendar days.
*Period: Weekday*

#### `FutureRel%Chg(bars [, series])`

Future total return relative to the benchmark or another series.
*Period: Series Dependent*

#### `FutureRel%Chg_D(days [, series])`

Future relative return, in calendar days.
*Period: Weekday*

#### `SMAPct(bars [, series])`

Percent distance from the simple moving average (dividends included).
*Period: Series Dependent*

#### `SMAPct_W(weeks [, series])`

Percent distance from the SMA using the weekly series (dividends included).
*Period: Weekly*

#### `HighPct(bars [, series])`

Percent from the high in the period (dividends included).
*Period: Series Dependent*

#### `HighPct_W(weeks [, series])`

Percent from the high in the period using the weekly series.
*Period: Weekly*

#### `LowPct(bars [, series])`

Percent from the low in the period (dividends included).
*Period: Series Dependent*

#### `LowPct_W(weeks [, series])`

Percent from the low in the period using the weekly series.
*Period: Weekly*

**Example**
```p123
// 12-1 month momentum (skip the most recent month)
Ret%Chg(252, 21)
// Beat the benchmark over the past year
Rel%Chg(252) > 0
// Drawn down more than 20% from the 1-year high
HighPct(252) < -20
```

### Factors

#### Performance / Percent From Hi/Lo

| Factor | Description | Period |
|---|---|---|
| `Pct3MH` | Percent from the 3-month high (weekly series, dividends included). | 3 Months |
| `Pct3ML` | Percent from the 3-month low (weekly series, dividends included). | 3 Months |
| `Pct4WH` | Percent from the 4-week high (weekly series, dividends included). | 4 Weeks |
| `Pct4WL` | Percent from the 4-week low (weekly series, dividends included). | 4 Weeks |
| `Pct52WH` | Percent from the 52-week high (weekly series, dividends included). | 52 Weeks |
| `Pct52WL` | Percent from the 52-week low (weekly series, dividends included). | 52 Weeks |

#### Performance / Return Incl Div (Total Return)

Total return including dividends.

| Factor | Description | Period |
|---|---|---|
| `Ret1W%Chg` | Total return over 1 week. | 1 Week |
| `Ret4W%Chg` | Total return over 4 weeks. | 4 Weeks |
| `Ret3M%Chg` | Total return over 3 months. | 3 Months |
| `Ret6M%Chg` | Total return over 6 months. | 6 Months |
| `Ret1Y%Chg` | Total return over 1 year. | 1 Year |
| `Ret2Y%Chg` | Total return over 2 years. | 2 Years |

#### Performance / Return Excl Div

Price change excluding dividends; relative variants are versus the regional benchmark.

| Factor | Description | Period |
|---|---|---|
| `Pr4W%Chg` | Price percent change over 4 weeks (dividends not included). | 4 Weeks |
| `Pr4WRel%Chg` | Price percent change over 4 weeks relative to the regional benchmark. | 4 Weeks |
| `Pr13W%Chg` | Price percent change over 13 weeks (dividends not included). | 13 Weeks |
| `Pr13WRel%Chg` | Price percent change over 13 weeks relative to the regional benchmark. | 13 Weeks |
| `Pr26W%Chg` | Price percent change over 26 weeks (dividends not included). | 26 Weeks |
| `Pr26WRel%Chg` | Price percent change over 26 weeks relative to the regional benchmark. | 26 Weeks |
| `Pr52W%Chg` | Price percent change over 52 weeks (dividends not included). | 52 Weeks |
| `Pr52WRel%Chg` | Price percent change over 52 weeks relative to the regional benchmark. | 52 Weeks |

---

## Price

### Functions

#### `Close(bars [, series])`

Historical close price `bars` (trading days) ago. Use negative values to peek into the future.
*Period: Series Dependent*

#### `Close_D(days [, series])`

Historical daily close price `days` ago, including holidays (filled with the previous close).
*Period: Weekday*

#### `Close_W(weeks [, series])`

Historical weekly close price (0 for the most recent week).
*Period: Weekly*

#### `Open(bars [, series])`

Historical open price `bars` ago.
*Period: Series Dependent*

#### `Open_D(days [, series])`

Historical open price `days` ago, including holidays.
*Period: Weekday*

#### `Open_W(weeks [, series])`

Historical weekly open price.
*Period: Weekly*

#### `Hi(bars [, series])`

Historical high price `bars` ago.
*Period: Series Dependent*

#### `Hi_D(days [, series])`

Historical high price `days` ago, including holidays.
*Period: Weekday*

#### `Hi_W(weeks [, series])`

Historical weekly high price.
*Period: Weekly*

#### `Low(bars [, series])`

Historical low price `bars` ago.
*Period: Series Dependent*

#### `Low_D(days [, series])`

Historical low price `days` ago, including holidays.
*Period: Weekday*

#### `Low_W(weeks [, series])`

Historical weekly low price.
*Period: Weekly*

#### `BenchClose(barsAgo)`

Historical close price of the benchmark.

#### `BenchOpen(barsAgo)`

Historical open price of the benchmark.

#### `BenchHi(barsAgo)`

Historical high price of the benchmark.

#### `BenchLow(barsAgo)`

Historical low price of the benchmark.

#### `Spread(barsAgo)`

Closing spread (ask minus bid) for the bar. Data is from ICE Data.

#### `Spread_D(daysAgo)`

Closing spread for the day including holidays (holidays filled with the previous day's spread).

#### `HighVal(period [, offset, series])`

Highest value of the series within the lookback period (close prices by default).

#### `LowVal(period [, offset, series])`

Lowest value of the series within the lookback period.

#### `HighValBar(period [, offset, series])`

Bar at which the highest value of the series occurred within the lookback period.

#### `LowValBar(period [, offset, series])`

Bar at which the lowest value of the series occurred within the lookback period.

#### `CloseAdj(barsAgo)`

Historical close adjusted for splits even when evaluated in the past (Series Tool only). Not
to be used with point-in-time ratios.

#### `CloseExDiv(barsAgo)`

Historical close unadjusted by dividends; reverses out future splits when evaluated in the past.

**Example**
```p123
// Price above the 200-day moving average
Close(0) > SMA(200, 0)
// Close within 5% of the 1-year high
Close(0) / HighVal(252) > 0.95
```

### Factors

#### Price / Price

| Factor | Description | Period |
|---|---|---|
| `Price` | Price unadjusted for future splits; same as `Close(0)`. | Previous Close |
| `PricePY` | Price one year ago, adjusted for splits and dividends. | 1 Year Ago |

#### Price / Price Highest/Lowest

| Factor | Description | Period |
|---|---|---|
| `PriceH` | 12-month high price, adjusted for splits and dividends. | 52 Weeks |
| `PriceL` | 12-month low price, adjusted for splits and dividends. | 52 Weeks |

---

## Volume

### Functions

#### `Vol(bars [, series])`

Historical volume for a day in the past.
*Period: Series Dependent*

#### `Vol_D(days [, series])`

Historical volume `days` ago, including holidays.
*Period: Weekday*

#### `Vol_W(weeks [, series])`

Historical weekly volume.
*Period: Weekly*

#### `AvgVol(noBars [, offset, series])`

Daily average volume over the past number of bars.
*Period: Daily Avg*

#### `MedianVol(noBars [, offset, series])`

Median volume over the past number of bars.
*Period: Daily Median*

#### `AvgDailyTot(noBars [, offset])`

Average daily dollar volume (price times volume) over the past number of bars.

#### `MedianDailyTot(noBars [, offset])`

Median daily dollar volume over the past number of bars.

#### `MinLiquidity(noBars [, offset])`

Lowest daily dollar volume over the past number of bars.

### Factors

#### Volume / Average Volume

| Factor | Description | Period |
|---|---|---|
| `AvgVol5` | Daily average volume over the past 5 bars; equivalent to `AvgVol(5)`. | Daily Avg 1 Wk |
| `AvgVol10` | Daily average volume over the past 10 bars; equivalent to `AvgVol(10)`. | Daily Avg 2 Wk |
| `AvgVol1M` | Daily average volume over the past 21 bars. | Daily Avg 1 Mo |
| `AvgVol3M` | Daily average volume over the past 62 bars. | Daily Avg 3 Mo |
| `AvgVol6M` | Average volume over the past 125 bars. | Daily Avg 6 Mo |
| `Vol10DAvg` | Daily average volume in millions; equivalent to `AvgVol(10)/1000000`. | Daily Avg 2 Wk |
| `Vol3MAvg` | Monthly average total volume in millions. | Monthly Average |

#### Volume / Liquidity

| Factor | Description | Period |
|---|---|---|
| `VolD%ShsOut` | Daily 10-day average volume as a percent of shares outstanding. | Daily Avg 2 Wk |
| `VolM%ShsOut` | Monthly average total volume (past 3 months) as a percent of shares outstanding. | Monthly Avg 3 Mo |

---

## Moving Average

<!-- name-whitelist: #SMA #EMA #VMA #WMA -->
The `CrossOver` / `CrossUnder` `type` argument accepts the moving-average constants `#SMA`,
`#EMA`, `#VMA`, and `#WMA`. These are documented argument values rather than standalone
factor codes.

### Functions

#### `SMA(bars [, offset, series])`

Simple moving average of a time series; period is in bars.
*Period: Series Dependent*

#### `SMA_D(days [, offset, series])`

Simple moving average with the period in calendar days.
*Period: Weekday*

#### `SMA_W(weeks [, offset, series])`

Simple moving average of the weekly time series.
*Period: Weekly*

#### `EMA(bars [, offset, series])`

Exponential moving average of a time series; period is in bars.
*Period: Series Dependent*

#### `EMA_D(days [, offset, series])`

Exponential moving average with the period in calendar days.
*Period: Weekday*

#### `EMA_W(weeks [, offset, series])`

Exponential moving average of the weekly time series.
*Period: Weekly*

#### `WMA(bars [, offset, series])`

Weighted moving average of a time series; period is in bars.
*Period: Series Dependent*

#### `WMA_D(days [, offset, series])`

Weighted moving average with the period in calendar days.
*Period: Weekday*

#### `VMA(bars [, offset])`

Volume-weighted moving average of a time series; period is in bars.
*Period: Series Dependent*

#### `MACD(offset [, series])`

Moving Average Convergence/Divergence: the difference between a 26-bar and a 12-bar EMA.

#### `MACDD(short, long [, period, offset, series])`

Difference of the MACD with its EMA (the signal line) when `period > 1`; otherwise returns the
MACD itself. P123 has no separate signal-line or histogram function (see
[Common Mistakes](#common-mistakes)).

**Example**
```p123
MACDD(12,26,9) > 0 and MACDD(12,26,9,5) < 0
```

#### `CrossOver(type, bars, period1, period2)`

Returns TRUE when the moving average of `period1` crossed above the moving average of `period2`
within the last `bars` bars. `type` is one of `#SMA`, `#EMA`, `#VMA`, `#WMA`.

#### `CrossUnder(type, bars, period1, period2)`

Returns TRUE when the moving average of `period1` crossed below the moving average of `period2`
within the last `bars` bars.

**Example**
```p123
// Golden cross within the last 10 bars
CrossOver(#SMA,10,50,200)=TRUE
// 50/200 simple-MA golden cross, current state
SMA(50, 0) > SMA(200, 0)
```

---

## Accumulation

### Functions

#### `ChaikinAD(period [, offset])`

Chaikin Accumulation/Distribution: a measure of money flowing into and out of a stock.

#### `ChaikinMFP(period, lookback [, offset])`

Percentage of days in the previous lookback window during which the Chaikin A/D was positive.

#### `ChaikinTrend(bars [, offset, increment, series])`

Chaikin Trend: a double-smoothed exponential average.

#### `OBV(offset)`

On-Balance Volume: running total of volume (added on up closes, subtracted on down closes) over
the past 100 bars.

#### `OBVSlopeN(offset, bars)`

Normalized rate of change (regression slope) of OBV.

#### `UpDownRatio(bars, offset)`

Up/down volume ratio, calculated as up volume divided by total up-plus-down volume.

---

## Trending

### Functions

#### `ADX(period, offset [, series])`

Average Directional Movement Index (Welles Wilder); measures trend strength, not direction.

#### `DMIPlus(period, offset [, series])`

DMI+ component of Wilder's Directional Movement System (positive directional movement).

#### `DMIMinus(period, offset [, series])`

DMI- component of Wilder's Directional Movement System (negative directional movement).

#### `DMICrossOver(period, bars [, series])`

Returns TRUE if DMI+ crossed above DMI- within the previous bars.

#### `DMICrossUnder(period, bars [, series])`

Returns TRUE if DMI- crossed above DMI+ within the previous bars.

#### `BBUpper(period [, deviations, offset, series])`

Upper Bollinger Band value (typical period 20, default 2 deviations).

#### `BBLower(period [, deviations, offset, series])`

Lower Bollinger Band value (typical period 20, default 2 deviations).

#### `PrcRegEst(bars [, series])`

Ending value of a regression line of the prices (dividends included).
*Period: Series Dependent*

#### `PrcRegEst_W(bars [, series])`

Ending value of a regression line of the weekly prices (dividends included).
*Period: Weekly*

#### `ROC(bars [, offset, series])`

Rate of Change.

**Example**
```p123
// Strong uptrend
ADX(14, 0) > 25 AND DMIPlus(14, 0) > DMIMinus(14, 0)
// Price below the lower Bollinger Band
Close(0) < BBLower(20, 2)
// Price above the Parabolic SAR
Close(0) > SAR
```

### Factors

#### Trending / Parabolic SAR

| Factor | Description | Period |
|---|---|---|
| `SAR` | Parabolic SAR (stop-and-reversal) value, acceleration factor 0.02, maximum 0.2. | |

#### Trending / Price Regression End Value

| Factor | Description | Period |
|---|---|---|
| `PrcRegEst10` | Ending value of a 10-bar price regression line (dividends included). | 10 Bars |
| `PrcRegEst20` | Ending value of a 20-bar price regression line. | 20 Bars |
| `PrcRegEst50` | Ending value of a 50-bar price regression line. | 50 Bars |
| `PrcRegEst10W` | Ending value of a 10-week price regression line. | 10 Weeks |
| `PrcRegEst20W` | Ending value of a 20-week price regression line. | 20 Weeks |
| `PrcRegEst50W` | Ending value of a 50-week price regression line. | 50 Weeks |

---

## Pattern

### Functions

#### `GapUp(GapPct, VolPct, bars, offset)`

Returns TRUE when a gap-up pattern occurred in the period specified by `bars`, starting at
`offset`, subject to the price-gap and volume thresholds.

#### `GapDown(GapPct, VolPct, bars, offset)`

Returns TRUE when a gap-down pattern occurred in the period specified by `bars`.

---

## Oscillators

### Functions

#### `RSI(period [, offset, series])`

Welles Wilder's Relative Strength Index; period in bars (typically 14).
*Period: Series Dependent*

#### `RSI_D(days [, offset, series])`

RSI with the period in calendar days.
*Period: Weekday*

#### `RSI_W(weeks [, offset, series])`

RSI with the period in weeks.
*Period: Week*

#### `StochK(period [, smoothK, offset, series])`

Stochastic %K value.

#### `StochD(period, smoothK, smoothD [, offset, series])`

Stochastic %D value.

#### `CCI(bars [, offset, series])`

Commodity Channel Index.

#### `Momentum(bars [, offset, absolute])`

Amount a security's closing price has changed over a span. With `absolute = FALSE` (default) it
is `100*Close(0)/Close(bars)`; with `absolute = TRUE` it is `Close(0)-Close(bars)`. This is the
momentum oscillator (see [Common Mistakes](#common-mistakes) for the wrong spelling).

#### `ULTOSC(offset)`

Ultimate Oscillator (Larry Williams): weighted sum of three oscillators of different periods
(see [Common Mistakes](#common-mistakes)).

#### `FlipFlop(series, on_value, off_value [, initial_state])`

Returns TRUE or FALSE depending on the last threshold that was exceeded.

**Example**
```p123
// RSI oversold
RSI(14) < 30
// Slow stochastic crossover
StochK(14, 3) > StochD(14, 3, 3)
```

---

## Volatility

### Functions

#### `ATR(bars [, offset, series])`

Average True Range (Welles Wilder) over the period.

#### `ATRN(bars [, offset, series])`

ATR as a percentage of the closing price; comparable across price magnitudes.

#### `PctDev(samples, bars [, offset, min_samples, annualize])`

Standard deviation of the percentage moves of the closing prices. For example, the SD of 50
weekly percentage moves is `PctDev(50,5)`.

#### `PctAvg(samples, bars [, offset, min_samples, annualize])`

Average of the percentage moves over the selected period.

#### `BetaFunc(period, samples [, min_samples, offset, series])`

Stock's beta with the country's main benchmark.

#### `Correl(period, samples, series [, series2])`

Correlation coefficient between the specified series.

#### `Sharpe(range [, bars, offset])`

A Sharpe-like ratio (not adjusted for the risk-free return).

#### `Sortino(range [, bars, offset])`

A Sortino-like ratio (not adjusted for the risk-free return). `range` is the total bars used,
`bars` the bars per return (default 5), `offset` the offset in bars.

**Example**
```p123
// Custom beta: 52-week window, 104 weekly samples
BetaFunc(52, 104)
// Annualized 12-month volatility from weekly moves
PctDev(52, 5)
```

### Factors

#### Volatility / Beta

| Factor | Description | Period |
|---|---|---|
| `Beta1Y` | Beta using up to 1 year of weekly returns against the country's main benchmark. | 1 Year |
| `Beta3Y` | Beta using up to 3 years of weekly returns (minimum 70 weekly returns). | 3 Years |
| `Beta5Y` | Beta using up to 5 years of weekly returns (minimum 100 weekly returns). | 5 Years |

#### Volatility / Sharpe Ratio

| Factor | Description | Period |
|---|---|---|
| `Sharpe1Y` | 1-year Sharpe-like ratio (weekly returns, not risk-free adjusted). | 1 Year |
| `Sharpe2Y` | 2-year Sharpe-like ratio (weekly returns, not risk-free adjusted). | 2 Years |

#### Volatility / Sortino Ratio

| Factor | Description | Period |
|---|---|---|
| `Sortino1Y` | 1-year Sortino-like ratio (weekly returns, not risk-free adjusted). | 1 Year |
| `Sortino2Y` | 2-year Sortino-like ratio (weekly returns, not risk-free adjusted). | 2 Years |

#### Volatility / Standard Deviation (Volatility)

Annualized standard deviation of total return.

| Factor | Description | Period |
|---|---|---|
| `TRSD30D` | Annualized SD of daily total return over the last 30 days. | 30 Days |
| `TRSD60D` | Annualized SD of daily total return over the last 60 days. | 60 Days |
| `TRSD90D` | Annualized SD of daily total return over the last 90 days. | 90 Days |
| `TRSD1YD` | Annualized SD of daily total return over the last year. | 1 Year |
| `TRSD3YD` | Annualized SD of daily total return over the last 3 years. | 3 Years |
| `TRSD3YM` | Annualized SD of monthly total return over the last 3 years. | 3 Years |
| `TRSD5YD` | Annualized SD of daily total return over the last 5 years. | 5 Years |
| `TRSD5YM` | Annualized SD of monthly total return over the last 5 years. | 5 Years |

---

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `MACDSig(...)` | `MACDD(12,26,9)` | No separate signal-line function; `MACDD` with `period > 1` returns the difference with the signal line. |
| `MACDHist(...)` | `MACDD(12,26,9)` | No separate histogram function. |
| `MOM(...)` | `Momentum(...)` | The momentum oscillator is `Momentum`. |
| `WilliamsR(...)` | `ULTOSC(...)` | P123 ships the Ultimate Oscillator, not Williams %R. |
| `PlusDI(...)` | `DMIPlus(...)` | P123 uses `DMIPlus` / `DMIMinus` for the directional indicators. |
| `MinusDI(...)` | `DMIMinus(...)` | P123 uses `DMIPlus` / `DMIMinus` for the directional indicators. |
| `HiValue(...)` | `HighVal(...)` | The highest-value function is `HighVal`. |
| `LoValue(...)` | `LowVal(...)` | The lowest-value function is `LowVal`. |
| `HiBar(...)` | `HighValBar(...)` | The bar-of-high function is `HighValBar`. |
| `LoBar(...)` | `LowValBar(...)` | The bar-of-low function is `LowValBar`. |

---

## See Also

- [Advanced Functions](advanced-functions.md) — `FRank`, `ZScore`, loop and regression functions.
- [Strategy](strategy.md) — position and portfolio state for buy/sell rules.
- [Misc](misc.md) — set statistics (`StdDev`, `RelStdDev`), date utilities, and `GetSeries`.
- [Ranking System XML](ranking-system-xml.md) — using technical formulas inside ranking nodes.

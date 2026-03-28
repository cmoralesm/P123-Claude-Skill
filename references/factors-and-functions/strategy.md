# Strategy

Functions that relate to the strategy holdings and strategy itself

## General

Functions that reference the portfolio as a whole.

### Available cash

Returns the amount of cash in the port/sim

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PortCash` |  |  |  |


### Cash percentage

Returns the % of the cash in the port/sim vs. the total market value

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CashPct` |  |  |  |


### Days (bars) since inception

Returns the number of bars since the inception of the portfolio/sim. Use this when calculating averages of the portfolio equity to make sure there are enough bars. For ex., this buy rules prevents buying if the portfolio value is below its 20bar average:

PortBars<20 or Close(0,#Equity) > SMA(20,0,#Equity)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PortBars` |  |  |  |


### Total value of portfolio

Returns the total value of the port/sim (incl. cash)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `TotMktVal` |  |  |  |


### Weeks since inception

Returns the number of weeks since inception.

Usage example: In a weekly sim add the following Buy rule to only buy every 13 weeks

Mod(SimWeeks,13)=0

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SimWeeks` |  |  |  |


## Diversification

Functions that ensure diversification across industries or sectors.

### Country Weight

Number of positions in the country of domicile (could be misleading for companies domiciled in tax havens). For a buy rule, the count is checked assuming the stock is purchased. For a sell rule the count is checked before the sell.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CountryCount` |  |  |  |


### ETF Taxonomy Weight

Number of positions in the ETF category.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ETFClassCount` |  |  |  |
| `ETFClassWeight` |  |  |  |
| `ETFCountryCount` |  |  |  |
| `ETFCountryWeight` |  |  |  |
| `ETFFamilyCount` |  |  |  |
| `ETFFamilyWeight` |  |  |  |
| `ETFMethodCount` |  |  |  |
| `ETFMethodWeight` |  |  |  |
| `ETFRegionCount` |  |  |  |
| `ETFRegionWeight` |  |  |  |
| `ETFSecCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ETFSecCount |
| `ETFSecWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ETFSecWeight |
| `ETFSizeCount` |  |  |  |
| `ETFSizeWeight` |  |  |  |
| `ETFStyleCount` |  |  |  |
| `ETFStyleWeight` |  |  |  |


### Industry Weight

Number of positions in the industry. For a buy rule, the weight is checked assuming the stock is purchased. For a sell rule the weight is checked before the sell.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IndCount` |  |  |  |
| `IndWeight` |  |  |  |
| `SubIndCount` |  |  |  |
| `SubIndWeight` |  |  |  |


### Market Cap Concentration

Number of positions in the MarketCap group. You can use this function to control MarketCap concentrations.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CapCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapCount |
| `CapWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapWeight |
| `LargeCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LargeCount |
| `LargeWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=LargeWeight |
| `MicroCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MicroCount |
| `MicroWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MicroWeight |
| `MidCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MidCount |
| `MidWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MidWeight |
| `SmallCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SmallCount |
| `SmallWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SmallWeight |


### Maximum Position Correlation

Calculates the maximum correlation coefficient of the stock being evaluated vs. the current holdings. You can use this to avoid buying or holding highly correlated stocks.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `MaxCorrel()` | period_bars, pct_bars |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=MaxCorrel |


### Sector Weight

Number of positions in the sector. For a buy rule, the weight is checked assuming the stock is purchased. For a sell rule the weight is checked before the sell.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SecCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SecCount |
| `SecWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SecWeight |
| `SubSecCount` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSecCount |
| `SubSecWeight` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSecWeight |


## Position

Functions that reference individual positions within a portfolio.

### Benchmark Return

Benchmark return since the position was opened.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `BenchPct` |  |  |  |


### Benchmark Return From Hi

Benchmark percentage return from highest close of the position. Use this to prevent a stop-loss in case the market is also dropping. For example to enter a stoploss only if the market outperformed the position, enter:

PctFromHi <= -20 And BenchPctFromPosHi > -20

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `BenchPctFromPosHi` |  |  |  |


### Buy amount for new position

Amount which will be used to buy a stock before any commissions or slippage. You can use this to set up a liquidity filter, for ex.:

BuyAmount/Price < 0.05*AvgVol(20)

With this rule a stock will not be bought if the number of shares being considered is greater than 5% of the 20 day average volume.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `BuyAmount` |  |  |  |


### Days (bars) since position was started

Number of bars since the position has been first opened. This is the number of tradings days which excludes weekends and holidays.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NoBars` |  |  |  |


### Days (calendar) since position was started

Number of days since the position has been first opened. This is the actual number of days, not bars. Ex: sell rule to exit position if the return is less than the benchmark after 1 month:

GainPct < BenchPct & NoDays > 30

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NoDays` |  |  |  |


### Dollar Return of Position

Return of an existing position in dollars

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Gain` |  |  |  |


### Percent from high

Percentage from highest close since position started. Always 0 or negative.

Ex: To set a 20% stoploss enter

PctFromHi <= -20

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PctFromHi` |  |  |  |


### Percent return of Position

Return of an existing position in % (dividends are not included). Ex: to sell a position if it gained 50% enter:

GainPct>50

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `GainPct` |  |  |  |


### Previous sell price for new position

Price the stock was last sold at, or NA. Example: To check that the current price is either above the last sell price, or that the stock was never bought, enter:

Eval(LastSellPrice=NA,TRUE,Close(0) > LastSellPrice)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LastSellPrice` |  |  |  |


### Recently sold

LastSellDaysLT(days): Returns TRUE or 1 if the stock was sold within the last no. of days, otherwise it returns FALSE or 0 (LT stands for Less Than).

Ex: to avoid buying a stock that was sold within the last 30 days, enter the following Buy rule:

LastSellDaysLT(30)=FALSE

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `LastSellDaysLT()` | days |  |  |


### Running count of holdings

Returns a count of stocks in the list that are current holdings

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `HoldingsCnt()` | "MyListName" |  |  |
| `PosCnt` |  |  |  |


### Trade amount as % of liquidity

Returns the % of the liquidity for the trade. See Full Description for examples

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PctAvgDailyTot()` | bars[, offset] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PctAvgDailyTot |


### Weight of a position as % of total market value

Weight of an existing position in % of total portfolio market value. See the Eval() function for an interesting use of Weight.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Weight` |  |  |  |


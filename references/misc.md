# Misc — Portfolio123 Reference

<!-- name-whitelist: RTWEXBGS -->

The Misc category collects everything that does not belong to a single data
domain: time-series and macroeconomic series IDs (usable in series-aware
functions such as `Close(0, ##CPI)`), the math / set / regression / utility
functions, and the constant vocabularies (numerical constants, country IDs,
universe IDs, parameter enumerations) and operators used throughout the formula
language.

Coverage: 43 functions / 20 factors (official totals) — extracted from the
official Factor Reference on 2026-06-09. In addition, 473 entries are
documented here that the official factor totals do not count: time-series and
macro series IDs, numerical and enumeration constants, country and universe IDs,
and operators. They are additional vocabulary, not counted as functions or
factors.

## Contents

- [Time Series IDs](#time-series-ids)
- [Macro Series IDs (Adjusted)](#macro-series-ids-adjusted)
- [Macro Series IDs (Unadjusted)](#macro-series-ids-unadjusted)
- [Group](#group)
- [Math](#math)
- [Regression](#regression)
- [Regression Stats](#regression-stats)
- [Set](#set)
- [Utility](#utility)
- [Constants](#constants)
- [Operators](#operators)
- [Common Mistakes](#common-mistakes)
- [FRED Mapping Note](#fred-mapping-note)
- [See Also](#see-also)

## Series IDs (overview)

Series IDs are used in functions that take a `series` parameter — for example
`Close(0, ##CPI)` returns the latest CPI value, and
`%(Close(0, ##CPI), Close(12, ##CPI))` computes the year-over-year change (CPI is
monthly, so an offset of 12 is one year). The `$`-prefixed IDs are index tickers,
the `#`-prefixed IDs are blended or computed series, and the `##`-prefixed IDs are
macroeconomic series. For macro series, the official "Corresponding FRED id" is
shown in a dedicated column where the source provides one.

## Time Series IDs

### S&P 500 IDs

| ID | Description | Period |
|---|---|---|
| `#SPRPBlend` | SP500 Risk Premium (weekly) | Weekly |
| `#SPYieldBlend` | SP500 Yield (weekly) based on the time weighted analysts estimates of CurrY and NextY | Weekly |
| `#SPEPSCNY` | SP500 EPS Blend Y (weekly)  based on the time weighted analysts estimates of CurrY and NextY | Weekly |
| `#SPEPSQ` | SP500 EPS Blend Q (weekly) | Weekly |
| `#SPEPSTTM` | SP500 EPS Trailing 12 months (weekly) | Weekly |

### Index Tickers - Major

| ID | Description | Period |
|---|---|---|
| `$MID` | S&P 400 Mid |  |
| `$RUA` | Russell3000 |  |
| `$RUI` | Russell1000 |  |
| `$RUT` | Russell2000 |  |
| `$SML` | S&P 600 Small |  |
| `$SP500` | S&P 500 |  |
| `$SP500EQ` | S&P 500 EQUAL WEIGHT |  |
| `$SPALL` | S&P 1500 Super Composite |  |

### Index Tickers - Specialty

| ID | Description | Period |
|---|---|---|
| `$DJIA` | Dow Jones |  |
| `$MIDPG` | S&P 400 Pure Growth |  |
| `$MIDPV` | S&P 400 Pure Value |  |
| `$NASDAQ` | Nasdaq |  |
| `$NASDAQ100` | Nasdaq 100 |  |
| `$SMLPG` | S&P 600 Pure Growth |  |
| `$SMLPV` | S&P 600 Pure Value |  |
| `$SP500PG` | S&P 500 Pure Growth |  |
| `$SP500PV` | S&P 500 Pure Value |  |
| `$SPALLCND` | SP1500 Consumer Discretion |  |
| `$SPALLCNS` | SP1500 Consumer Staples |  |
| `$SPALLENG` | SP1500 Energy |  |
| `$SPALLEUT` | SP1500 Elec Utilities |  |
| `$SPALLFIN` | SP1500 Financials |  |
| `$SPALLGLD` | SP1500 Gold |  |
| `$SPALLHEA` | SP1500 Health Care |  |
| `$SPALLHEQ` | SP1500 Hlth Care Eq&Srvc |  |
| `$SPALLIND` | SP1500 Industrials |  |
| `$SPALLINT` | SP1500 Information Tech |  |
| `$SPALLMAT` | SP1500 Materials |  |
| `$SPALLPBL` | SP1500 Pharma Biotech Life |  |
| `$SPALLPG` | S&P 1500 Pure Growth |  |
| `$SPALLPV` | S&P 1500 Pure Value |  |
| `$SPALLTCM` | SP1500 Telecom Services |  |
| `$SPALLUTL` | SP1500 Utilities |  |
| `$VIX` | CBOE Volatility Index |  |

### Misc IDs

| ID | Description | Period |
|---|---|---|
| `#Bench` | Current benchmark closing prices (daily) |  |
| `#Equity` | The Portfolio/Sim total value (daily) |  |
| `#TNX` | 10Y Treasury Note coupon payment on $1000 bond (updated daily).  To get the yield divide by 10. Ex. $25 payment on a $1000 bond represents 2.5% yield. |  |

### Price IDs

| ID | Description | Period |
|---|---|---|
| `#Close` | Stock closing prices (daily) |  |
| `#High` | Stock high prices (daily) |  |
| `#Low` | Stock low prices (daily) |  |
| `#Open` | Stock opening prices (daily) |  |

## Macro Series IDs (Adjusted)

### Macro - Other Economic Activity

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##DBTGDP` | Debt as Percent of GDP (quarterly) | GFDEGDQ188S | Quarterly |
| `##DOMINV` | Gross Private Domestic Investment (quarterly) | GPDI | Quarterly |
| `##PCE` | Personal Consumption Expenditures (monthly) | PCE | Monthly |
| `##RPCE` | Real Personal Consumption Expenditures (monthly) | PCEC96 | Monthly |
| `##SAVING` | Personal Saving Rate (monthly) | PSAVERT | Monthly |
| `##SURPLUS` | Federal Surplus or Deficit [-] (annual) | FYFSD | Annual |
| `##USSLIND` | Leading Index for the United States (monthly) | USALOLITONOSTSAM | Monthly |

### Macro - Delinquency Rate

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##DELINQCC` | Delinquency Rate On Credit Card Loans, All Commercial Banks (quarterly) | DRCCLACBS | Quarterly |
| `##DELINQMORT` | Delinquency Rate On Single-Family Residential Mortgages (quarterly) | DRSFRMACBS | Quarterly |

### Macro - GDP/GNP

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##GNP` | Gross National Product (quarterly) | GNP | Quarterly |
| `##RGDP` | Real Gross Domestic Product (quarterly) | GDPC1 | Quarterly |

### Macro - Income

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##HDEBTSERV` | Household Debt Service Payments as a Percent of Disposable Personal Income (quarterly) | TDSP | Quarterly |
| `##RDISPINC` | Real Disposable Personal Income (monthly) | DSPIC96 | Monthly |
| `##RINCPERCAP` | Real Disposable Personal Income: Per capita (monthly) | A229RX0 | Monthly |
| `##RMINCOME` | Real Median Income (annual) | MEHOINUSA672N | Annual |

### Macro - Labor Force

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CIVLABOR` | Civilian Labor Force (monthly) | CLF16OV | Monthly |
| `##LABORPARTIC` | Civilian Labor Force Participation Rate (monthly) | CIVPART | Monthly |
| `##NONFARMEMPL` | All Employees: Total nonfarm (monthly) | PAYEMS | Monthly |
| `##POPUL` | Total Population: All Ages including Armed Forces Overseas (monthly) | POP | Monthly |
| `##UNWANT` | Not in Labor Force, Want a Job Now (monthly) | NILFWJN | Monthly |

### Macro - Manufacturing

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##INV2SHIP` | Ratio of Total Inventories to Shipments for All Manufacturing Industries (monthly) | AMTMUS | Monthly |
| `##ORDERSCAP` | Manufacturers' New Orders: Nondefense Capital Goods ex.Aircraft (monthly) | NEWORDER | Monthly |
| `##ORDERSDUR` | Manufacturers' New Orders: Durable Goods (monthly) | DGORDER | Monthly |
| `##ORDERSUNFILL` | Value of Unfilled Orders for All Manufacturing ex. Transportation (monthly) | AMXTUO | Monthly |
| `##WAGES` | Wages in manufacturing (monthly) | AHETPI | Monthly |

### Macro - Money, M1, M2

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##ADJMBASE` | Monetary Base; Total (monthly) | BOGMBASE | Monthly |
| `##M1` | M1 Money Stock (monthly) | M1SL | Monthly |
| `##M2` | M2 Money Stock (monthly) | M2SL | Monthly |
| `##USCURRACCT` | Balance on Current Account (quarterly) | IEABC | Quarterly |
| `##VELM1` | Velocity of M1 Money Stock (quarterly) | M1V | Quarterly |
| `##VELM2` | Velocity of M2 Money Stock (quarterly) | M2V | Quarterly |

### Macro - Other Business Activity

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CAPUTIL` | Capacity Utilization: Total Industry (monthly) | TCU | Monthly |
| `##CONSTR` | Total Construction Spending (monthly) | TTLCONS | Monthly |
| `##HSTARTS` | Housing Starts (Total) (monthly) | HOUST | Monthly |
| `##INDPRO` | Industrial Production Index (monthly) | INDPRO | Monthly |
| `##INV2SLS` | Total Business: Inventories to Sales Ratio (monthly) | ISRATIO | Monthly |
| `##INVTOT` | Total Business Inventories (monthly) | BUSINV | Monthly |
| `##SALESRET` | Retail Sales: Total (Excluding Food Services) (monthly) | RSXFS | Monthly |
| `##SALESRETFD` | Real Retail and Food Services Sales (monthly) | RRSFS | Monthly |

### Macro - Price Index, CPI, PPI, HPI

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CPI` | CPI All Urban Consumers: All Items (monthly) | CPIAUCSL | Monthly |
| `##HPRICES` | S&P Case-Shiller 20-City Home Price Index(c) (monthly) | CSUSHPINSA | Monthly |
| `##PPI` | Producer Price Index: Finished Goods (monthly) | WPSFD49207 | Monthly |

### Macro - Sentiment

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##RECPROB` | Smoothed U.S. Recession Probabilities (monthly) | RECPROUSM156N | Monthly |
| `##UMCSENT` | University of Michigan: Consumer Sentiment(c) (monthly) | UMCSENT | Monthly |
| `##INFLEXP` | University of Michigan Inflation Expectation(c) (monthly) | MICH | Monthly |

### Macro - Unemployment

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CLAIMSCONTINUE` | Continued Claims (Insured Unemployment) (weekly) | CCSA | Weekly |
| `##CLAIMSNEW` | Initial Claims (weekly) | ICSA | Weekly |
| `##UNDURATION` | Median Duration of Unemployment (monthly) | UEMPMED | Monthly |
| `##UNRATE` | Civilian Unemployment Rate (monthly) | UNRATE | Monthly |
| `##UNTEEN` | Unemployment Rate - 16 to 19 years (monthly) | LNS14000012 | Monthly |
| `##UNTOT` | Total unemployed, including under-employed (monthly) | U6RATE | Monthly |

### Macro - Vehicle, Automobile

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##INV2SLSAUTO` | Auto Inventory/Sales Ratio (monthly) | AISRSA | Monthly |
| `##PRODAUTO` | Domestic Auto Production (monthly) | DAUPSA | Monthly |
| `##SALESALLVEH` | Total Vehicle Sales (monthly) | TOTALSA | Monthly |
| `##SALESAUTO` | Light Weight Vehicle Sales: Autos & Light Trucks (monthly) | ALTSALES | Monthly |

## Macro Series IDs (Unadjusted)

### Macro - Currency

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##NBDI` | Nominal Broad U.S. Dollar Index (daily) | DTWEXBGS | Weekday |
| `##RBDI` | Real Broad Dollar Index (monthly) | RTWEXBGS | Monthly |

### Macro - Interbank Rate

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CAB3MO` | 3-Month Interbank Rate for Canada (monthly) | IR3TIB01CAM156N | Monthly |
| `##EUB3MO` | 3-Month Interbank Rate for the Euro Area (monthly) | IR3TIB01EZM156N | Monthly |
| `##GBB3MO` | 3-Month Interbank Rate for the United Kingdom (monthly) | IR3TIB01GBM156N | Monthly |
| `##NOB3MO` | 3-Month Interbank Rates for Norway (monthly) | IR3TIB01NOM156N | Monthly |
| `##PLB3MO` | 3-Month Interbank Rates for Poland (monthly) | IR3TIB01PLM156N | Monthly |
| `##SEB3MO` | 3-Month Interbank Rates for Sweden (monthly) | IR3TIB01SEM156N | Monthly |

### Macro - Interest, Mortgage, Prime, TED

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##SOFR3MO` | 90-Day Average SOFR (daily) | SOFR90DAYAVG | Weekday |
| `##USR10YR` | 10-Year US Real Interest Rate (monthly) |  | Monthly |
| `##FEDFUNDS` | Effective Federal Funds Rate (daily) | DFF | Weekday |
| `##MORT30Y` | 30-Year Fixed Rate Mortgage Average in the United States (weekly) | MORTGAGE30US | Weekly |
| `##PRIME` | Bank Prime Loan Rate (monthly) | MPRIME | Monthly |

### Macro - Treasury notes (T-notes)

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CAT10YR` | 10-Year Government Bond Yield for Canada (monthly) | IRLTLT01CAM156N | Monthly |
| `##CHT10YR` | 10-Year Government Bond Yield for Switzerland (monthly) | IRLTLT01CHM156N | Monthly |
| `##EUT10YR` | 10-Year Government Bond Yield for the Euro Area (monthly) | IRLTLT01EZM156N | Monthly |
| `##GBT10YR` | 10-Year Government Bond Yield for the United Kingdom (monthly) | IRLTLT01GBM156N | Monthly |
| `##UST6MO` | 6-Month Treasury Constant Maturity Rate (USD) (daily) | DGS6MO | Weekday |
| `##UST2YR` | 2-Year Treasury Constant Maturity Rate (USD) (daily) | DGS2 | Weekday |
| `##UST3YR` | 3-Year Treasury Constant Maturity Rate (USD) (daily) | DGS3 | Weekday |
| `##UST5YR` | 5-Year Treasury Constant Maturity Rate (USD) (daily) | DGS5 | Weekday |
| `##UST7YR` | 7-Year Treasury Constant Maturity Rate (USD) (daily) | DGS7 | Weekday |
| `##UST10YR` | 10-Year Treasury Constant Maturity Rate (USD) (daily) | DGS10 | Weekday |

### Macro - FX Rates

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `#USDAUD` | USD to AUD |  |  |
| `#USDBAM` | USD to BAM |  |  |
| `#USDBGN` | USD to BGN |  |  |
| `#USDCAD` | USD to CAD |  |  |
| `#USDCHF` | USD to CHF |  |  |
| `#USDCZK` | USD to CZK |  |  |
| `#USDDKK` | USD to DKK |  |  |
| `#USDEUR` | USD to EUR |  |  |
| `#USDGBP` | USD to GBP |  |  |
| `#USDHKD` | USD to HKD |  |  |
| `#USDHRK` | USD to HRK |  |  |
| `#USDHUF` | USD to HUF |  |  |
| `#USDILS` | USD to ILS |  |  |
| `#USDISK` | USD to ISK |  |  |
| `#USDJPY` | USD to JPY |  |  |
| `#USDLVL` | USD to LVL |  |  |
| `#USDMKD` | USD to MKD |  |  |
| `#USDMXN` | USD to MXN |  |  |
| `#USDNOK` | USD to NOK |  |  |
| `#USDNZD` | USD to NZD |  |  |
| `#USDPLN` | USD to PLN |  |  |
| `#USDRON` | USD to RON |  |  |
| `#USDRSD` | USD to RSD |  |  |
| `#USDRUB` | USD to RUB |  |  |
| `#USDSEK` | USD to SEK |  |  |
| `#USDSGD` | USD to SGD |  |  |
| `#USDSKK` | USD to SKK |  |  |
| `#USDTRY` | USD to TRY |  |  |
| `#USDUAH` | USD to UAH |  |  |
| `#USDZAR` | USD to ZAR |  |  |

### Macro - Corporate Bonds

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##CORPAAA` | BofA Merrill Lynch US Corporate AAA Effective Yield(c) (daily) | BAMLC0A1CAAAEY | Weekday |
| `##CORPB` | BofA Merrill Lynch US High Yield B Effective Yield(c) (daily) | BAMLH0A2HYBEY | Weekday |
| `##CORPBB` | BofA Merrill Lynch US High Yield BB Effective Yield(c) (daily) | BAMLH0A1HYBBEY | Weekday |
| `##CORPBBB` | BofA Merrill Lynch US Corporate BBB Effective Yield(c) (daily) | BAMLC0A4CBBBEY | Weekday |
| `##CORPBBBOAS` | BofA Merrill Lynch US Corporate BBB Option-Adjusted Spread (daily) | BAMLC0A4CBBB | Weekday |
| `##CORPBBOAS` | BofA Merrill Lynch US High Yield Master II Opt-Adj Spread (daily) | BAMLH0A0HYM2 | Weekday |
| `##CORPJNK` | BofA Merrill Lynch US High Yield CCC or Below Effective Yield(c) (daily) | BAMLH0A3HYCEY | Weekday |

### Macro - Oil, Gold Price

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##OIL` | Crude Oil Prices: West Texas Intermediate (WTI) - Cushing, OK (daily) | DCOILWTICO | Weekday |

### Macro - Stress Index

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##STRESS` | St. Louis Fed Financial Stress Index(c) (weekly) | STLFSI4 | Weekly |

### Macro - Treasury bills (T-bills)

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##UST1MO` | 1-Month Treasury Constant Maturity Rate (USD) (daily) | DGS1MO | Weekday |
| `##UST3MO` | 3-Month Treasury Constant Maturity Rate (USD) (daily) | DGS3MO | Weekday |
| `##UST1YR` | 1-Year Treasury Constant Maturity Rate (USD) (daily) | DGS1 | Weekday |

### Macro - Vacancy Rates

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##HVACANCY` | Home Vacancy Rate for the United States (annual) | USHVAC | Annual |
| `##RVACANCY` | Rental Vacancy Rate for the United States (annual) | USRVAC | Annual |

### Macro - Treasury bonds (T-bonds)

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `##UST20YR` | 20-Year Treasury Constant Maturity Rate (USD) (daily) | DGS20 | Weekday |
| `##UST30YR` | 30-Year Treasury Constant Maturity Rate (USD) (daily) | DGS30 | Weekday |

### Compustat Macro - TO BE DEPRECATED

| ID | Description | FRED ID | Period |
|---|---|---|---|
| `#BOND20YR` | 20-Year Treasury Yield (monthly) |  | Monthly |
| `#BOND30YR` | 30-Year Treasury Yield (monthly) |  | Monthly |
| `#CABGDP2` | Total Current Account Balance of the United States as a percentage of GDP (*quarterly data, 3 equal monthly values) |  | Quarterly* |
| `#CPI` | Consumer Price Index for Urban Consumers, All Items (monthly) |  | Monthly |
| `#EMPLOY` | Total Non-Farm Employment, Thousands of People (monthly) |  | Monthly |
| `#FEDFUNDS` | Fed Funds Rate, in percentage points (monthly) |  | Monthly |
| `#GDP` | Real Gross Domestic Product, Billions of Chained 2009 Dollars  (*quarterly data, 3 equal monthly values) |  | Quarterly* |
| `#HOUSE` | Total New Housing Starts, Privately Owned Residences, in thousands of units (monthly) |  | Monthly |
| `#M1` | M1 Money Stock, in billions of dollars (monthly) |  | Monthly |
| `#M2` | M2 Money Stock, in billions of dollars (monthly) |  | Monthly |
| `#NOTE10YR` | 10-Year Treasury Yield (monthly) |  | Monthly |
| `#NOTE2YR` | 2-Year Treasury Yield (monthly) |  | Monthly |
| `#NOTE3YR` | 3-Year Treasury Yield (monthly) |  | Monthly |
| `#NOTE5YR` | 5-Year Treasury Yield (monthly) |  | Monthly |
| `#NOTE7YR` | 7-Year Treasury Yield (monthly) |  | Monthly |
| `#POPT` | Total U.S. Population  (*annual data, 12 equal monthly values) |  | Annual* |
| `#PPI` | Producer Price Index (PPI), Finished Goods (monthly) |  | Monthly |
| `#PRIME` | Prime Rate, in percentage points (monthly) |  | Monthly |
| `#RTLSALES` | Retail Sales, excluding Food Services, in millions of dollars (monthly) |  | Monthly |
| `#TBILL12M` | 12-Month Treasury Yield (monthly) |  | Monthly |
| `#TBILL3M` | 3-Month Treasury Yield (monthly) |  | Monthly |
| `#TBILL6M` | 6-Month Treasury Yield (monthly) |  | Monthly |
| `#UNEMP` | Unemployment Rate, in percentage points (monthly) |  | Monthly |

## Group

Membership tests against a custom list, the current universe, or by company name.

### Functions

#### `CoName("name")`
Returns true if the company name matches the pattern, false otherwise. Wildcards
are supported: `*` matches any string, `?` matches any single character.

#### `InList("MyListName")`
Returns true if the stock is in the named custom list, false otherwise. Create
custom lists under Tools -> Lists -> Custom. Prefix with `!` to exclude the list.

```p123
InList("MyList")
```

#### `Universe(uname)`
Returns true if the stock is in the named universe, false otherwise. Use a
built-in universe ID (see [Universe IDs](#universe-ids)) or a custom universe
name.

```p123
Universe(SP500)
```

| Factor | Description | Period |
|---|---|---|
| `EvenID` | Returns 1 (TRUE) if the internal ID of the stock or ETF is Even, 0 (FALSE) otherwise. Can be used for data-mining to create two samples from the universe. |  |


## Math

Scalar math functions and NA/negative/zero replacement helpers. Most math
functions return NA when any input is NA.

### Functions

#### `Abs(expr)`
Evaluates to the absolute value of `expr`.

#### `Log10(val)`
Returns the base-10 logarithm of `val`.

#### `%(a, b)`
Calculates percent change as `100 * ((a - b) / abs(b))`.

#### `Gr%(a, b [, years])`
Annualized growth rate, `100 * (pow(1 + (a - b) / abs(b), 1/years) - 1)`. When
`years` is 1 or omitted it reduces to the plain percent change `100 * ((a - b) / abs(b))`.

#### `Mod(val, modulo)`
Modulus operation: returns the remainder of `val / modulo`.

#### `LN(val)`
Returns the natural logarithm of `val`.

#### `Negate(expr)`
Changes the sign of the expression (for example `Negate(5)` returns -5).

#### `Pow(number, power)`
Returns `number` raised to `power`.

#### `Trunc(val)`
Rounds `val` toward zero.

#### `Bound(expression, min, max [, returnNA])`
Constrains a value between a minimum and a maximum. When returnNA is true, the
function returns NA if the expression falls outside the bounds instead of
clamping it.

#### `LBound(expression, min [, returnNA])`
Constrains a value to a minimum (lower bound). When returnNA is true it returns
NA if the expression is below the minimum.

#### `UBound(expression, max [, returnNA])`
Constrains a value to a maximum (upper bound). When returnNA is true it returns
NA if the expression is above the maximum.

#### `IsNA(expr1, expr2)`
Returns `expr1` if it is not NA, otherwise returns `expr2`.

#### `IsNeg(expr1, expr2)`
Returns `expr1` if it is not negative, otherwise returns `expr2`.

#### `IsNegOrNA(expr1, expr2)`
Returns `expr1` if it is neither negative nor NA, otherwise returns `expr2`.

#### `IsZero(expr1, expr2)`
Returns `expr1` if it is not zero, otherwise returns `expr2`.

| Factor | Description | Period |
|---|---|---|
| `Random` | Random: Returns a random number uniformly distributed between 0 and 1 |  |


## Regression

Linear-regression builders. Call one of these first to compute a regression, then
read the result with the Regression Stats factors and functions below.

### Functions

#### `LinRegXYVals(x0, y0, x1, y1, ..., x50, y50)`
Operates a regression on a set of paired X-Y values.

#### `LinRegVals(y0, y1, ..., y50)`
Operates a regression on a set of Y values (X is the implied index).

## Regression Stats

Read the result of a previously computed regression (see the Regression functions
above). The factors return scalar statistics; the functions take an offset or X
input.

### Functions

#### `EstimateXY(X)`
Returns the Y estimate for the given X from a previously computed XY regression.

#### `EstimateY(offset)`
Returns the Y estimate for a previously computed regression. The meaning of
`offset` depends on the regression.

#### `RegGr%([period=1])`
Returns the growth for a previously computed time-series regression. The `period`
argument annualizes the growth.

#### `SurpriseY(offset)`
Returns the surprise of the estimated Y versus the actual value for a previously
computed regression.

| Factor | Description | Period |
|---|---|---|
| `R2` | Returns the R^2 for a previously computed regression |  |
| `R` | Returns the R for a previously computed regression |  |
| `Samples` | Returns the number of samples for a previously computed regression |  |
| `SlopeConf%` | Confidence is defined as 100 * (1-SlopePVal) for a previously computed regression |  |
| `Slope` | Returns the Slope for a previously computed regression |  |
| `SlopePVal` | Returns the P-value of the slope for a previously computed regression |  |
| `SlopeSE` | Returns the Slope Standard Error for a previously computed regression |  |
| `SlopeTStat` | Returns the t Stat of the slope for a previously computed regression |  |
| `SE` | Returns the SE of the Y estimate for a previously computed regression |  |
| `Intercept` | Returns the Y-Intercept for a previously computed regression |  |
| `InterceptSE` | Returns the Y-Intercept Standard Error for a previously computed regression |  |


## Set

Small-set statistics over up to 20 inline values. NAs are discarded.

### Functions

#### `Avg(x1, x2[, .., x20])`
Returns the average of the listed values. Up to 20 parameters; NAs are discarded.

#### `Max(x1, x2[, .., x20])`
Returns the largest of the listed values. Up to 20 parameters; NAs are discarded.

#### `Min(x1, x2[, .., x20])`
Returns the smallest of the listed values. Up to 20 parameters; NAs are discarded.

#### `Median(x1, x2[, .., x20])`
Returns the median of the listed values. Up to 20 parameters; NAs are discarded.

#### `StdDev(x1, x2[, .., x20])`
Returns the standard deviation of the listed values.

#### `RelStdDev(x1, x2[, .., x20])`
Returns the relative standard deviation (standard deviation divided by the mean)
of the listed values.

#### `InSet(expression, x1[, .., x20])`
Returns true if `expression` equals any of the listed values. For example, to
screen for stocks in one of three industries:

```p123
InSet(Industry, ADVERT, CASINO, HOTELS)
```

#### `Higher(x1, x2[, .., x20])`
Returns the count of positions where `xi > xi+1`. For example, to find stocks
whose price rose on at least 2 of the last 3 days:

```p123
Higher(Close(0), Close(1), Close(2), Close(3)) >= 2
```

#### `Lower(x1, x2[, .., x20])`
Returns the count of positions where `xi < xi+1`. For example, to find stocks
whose price fell on at least 2 of the last 3 days:

```p123
Lower(Close(0), Close(1), Close(2), Close(3)) >= 2
```

## Utility

Dates, variables, foreign-exchange, conditional evaluation, and series access.

### Functions

#### `BarsSince(date)`
Returns the number of bars since the given date. `date` is a number formatted
YYYYMMDD.

#### `DaysSince(date)`
Returns the number of calendar days since the given date. `date` is a number
formatted YYYYMMDD.

#### `DaysDiff(from, to)`
Returns the number of calendar days between the two dates. Both are numbers
formatted YYYYMMDD.

#### `Holiday(weekday)`
Returns true if `weekday` is a holiday, false otherwise. Use negative values to
check for upcoming holidays. (Future calendar dates are not supported.)

#### `Between(value, min, max)`
Returns true if `value` is between `min` and `max` inclusive, false otherwise.

#### `MonthBars(bars[, "cid"])`
Returns true if the as-of date is the nth trading day of the month. Negative
offsets count from the end of the month (for example -2 is the second-to-last
trading day). In multi-country regions the country code must be supplied.
Intended for strategies, not screens or ranking systems.

#### `SetVar(@myvar, expression)`
Sets the variable `@myvar` to the expression and returns true. The variable can
then be used in subsequent rules.

#### `Eval(condition, expr1, expr2)`
Evaluates `expr1` if `condition` is non-zero, otherwise evaluates `expr2`.

#### `GetSeries("ticker/series")`
Returns a series ID for use in functions that take a `series` parameter. You can
pass any stock, ETF, or index ticker, or a custom series. If you use a stock
ticker, the function may stop working when the ticker changes.

| Factor | Description | Period |
|---|---|---|
| `AsOfDate` | Returns the current trading day as a number in the following format YYYYMMDD |  |
| `PrevBarDaysAgo` | Returns the number of bars from previous trading day. See Full Description for an example how to buy on a specific weekday. |  |
| `Year` | Returns the Year of the current trading day. |  |
| `Month` | Returns the month 1-12 of the current trading day. |  |
| `MonthDay` | Returns the day of the month 1-31 of the current trading day. |  |
| `WeekDay` | Returns the week day of the current trading day (1 = Sunday, 2 = Monday, ..., 7 = Saturday). See Full Description for an example how to buy on a specific weekday. |  |
| `FXRate` | FXRate gives you the foreign exchange rate used to convert the currency of the stock (or ETF) to the currency in the screen/ranking system/simulation. |  |

## Constants

The constants below are enumeration values passed as function arguments or used
as named numeric literals. They are additional vocabulary and are not counted in
the official factor totals.

### Dividend Date

| Code | Description |
|---|---|
| `#AnnDate` | Announce date |
| `#ExDate` | Ex date |
| `#PayDate` | Pay date |

### Dividend Type

| Code | Description |
|---|---|
| `#AllDiv` | Any kind of dividend |
| `#Regular` | Regular dividend (used to calculate Yield) |
| `#Special` | Special dividend (not used to calculate Yield) |

### Formula Functions Include NA Parameter

| Code | Description |
|---|---|
| `#ExclNA` | Exclude NA values |
| `#InclNA` | Include NA values |
| `#NANeutral` | NA Neutral |

### Numerical Constants

| Code | Description |
|---|---|
| `#Month3` | Returns 62, the approximate number of bars in 3 months |
| `#Month6` | Returns 125, the approximate number of bars in 6 months |
| `NA` | NA value |
| `TRUE` | TRUE or 1 |
| `FALSE` | FALSE or 0 |
| `#Year` | Returns 251, the approximate number of bars in a year |
| `#Year2` | Returns 501, the approximate number of bars in two years |
| `#Month` | Returns 21, the approximate number of bars in a month |
| `#Week` | Returns 5, the approximate number of bars in a week |

### Streak

| Code | Description |
|---|---|
| `#Increasing` | Increasing values streak |
| `#NotIncreasing` | Decreasing or equal values streak |
| `#NotPositive` | Negative or zero values streak |
| `#Positive` | Positive values streak |

### Actual Item (actual_item)

| Code | Description |
|---|---|
| `#CAPX` | Capital Expenditure |
| `#EBIT` | EBIT |
| `#EBITDA` | EBITDA |
| `#EPS` | Earnings Per Share |
| `#EPS_GAAP` | Reported Earnings Per Share |
| `#FCF` | Free Cash Flow |
| `#FFO` | Funds From Operations |
| `#NET` | Net Profit |
| `#PTI` | Pre-Tax Profit |
| `#SALES` | Sales |
| `#SHS_REPURCH` | Share Repurchase |
| `#SOE` | Stock Option Expense |

### Consensus Estimate (cons_item)

| Code | Description |
|---|---|
| `#CAPXNTM` | CapEx Next Twelve Months |
| `#CAPXQ` | CapEx Quarter |
| `#CAPXY` | CapEx Annual |
| `#EBITDANTM` | EBITDA Next Twelve Months |
| `#EBITDAQ` | EBITDA Quarter |
| `#EBITDAY` | EBITDA Annual |
| `#EPSNTM` | EPS Next Twelve Months |
| `#EPSQ` | EPS Quarter |
| `#EPSY` | EPS Annual |
| `#FCFNTM` | FCF Next Twelve Months |
| `#FCFQ` | FCF Quarter |
| `#FCFY` | FCF Annual |
| `#LTG` | Long Term Growth |
| `#PT` | Price Target |
| `#SALENTM` | Sales Next Twelve Months |
| `#SALEQ` | Sales Quarter |
| `#SALEY` | Sales Annual |

### Consensus Recommendation (rec_stat)

| Code | Description |
|---|---|
| `#AvgRec` | Average of all Recommendation |
| `#BuyCnt` | Number of Buy Recommendations |
| `#HoldCnt` | Number of Hold Recommendations |
| `#OverCnt` | Number of Overweight Recommendations |
| `#RecCnt` | Number of Recommendations |
| `#SellCnt` | Number of Sell Recommendations |
| `#UnderCnt` | Number of Underweight Recommendations |

### Corporate Actions (ca_retvalue)

| Code | Description |
|---|---|
| `#ACTIONCNT` | Number of actions that matched or 0 |
| `#ACTIONTYPE` | The corporate action type |
| `#ANNCEDAYS` | Number of days since the announce date or NA |
| `#CLOSEDAYS` | Number of days since the close/expiry date or NA |
| `#TRUEFALSE` | TRUE if a match is found, FALSE otherwise |

### Corporate Actions (ca_status)

| Code | Description |
|---|---|
| `#APPROVAL` | Approval |
| `#COMPLETION` | Completion |
| `#MEETING` | Meeting |
| `#OTHER` | Other ICE Data status |
| `#REJECTION` | Rejection |
| `#STATUSANY` | Any status |
| `#STATUSFAIL` | Either #TERMINATION or #REJECTION |
| `#STATUSNA` | Status not specified |
| `#STATUSOK` | Either #COMPLETION or #APPROVAL |
| `#TERMINATION` | Termination |

### Corporate Actions (ca_type)

| Code | Description |
|---|---|
| `#BUYOFF` | Buy Offer |
| `#LIQUIDATION` | Liquidation |
| `#MANDA` | Any of the individual actions except #SPLIT |
| `#MANDAEXSPIN` | Any of the individual actions except #SPLIT  & #SPINOFF |
| `#MERGER` | Merger |
| `#MERGEREL` | Merger Elect |
| `#NEWOFFER` | New Offer |
| `#SPINOFF` | Spinoff |
| `#SPLIT` | Split |

### Filing Period

| Code | Description |
|---|---|
| `ANN` | Annual |
| `QTR` | Interim |
| `TTM` | Trailing Twelve Months |

### N/A during preliminaries

| Code | Description |
|---|---|
| `FALLBACK` | Fallback to previous period |
| `KEEPNA` | Keep NA values |
| `ZERONA` | Set NA values to 0 |

### Country IDs

| Code | Description |
|---|---|
| `ALB` | Albania |
| `DZA` | Algeria |
| `AND` | Andorra |
| `ATG` | Antigua And Barbuda |
| `ARG` | Argentina |
| `ARM` | Armenia |
| `AUS` | Australia |
| `AUT` | Austria |
| `BHS` | Bahamas |
| `BHR` | Bahrain |
| `BGD` | Bangladesh |
| `BRB` | Barbados |
| `BLR` | Belarus |
| `BEL` | Belgium |
| `BLZ` | Belize |
| `BMU` | Bermuda |
| `BOL` | Bolivia |
| `BIH` | Bosnia and Herzegovina |
| `BWA` | Botswana |
| `BRA` | Brazil |
| `BGR` | Bulgaria |
| `KHM` | Cambodia |
| `CAN` | Canada |
| `CYM` | Cayman Islands |
| `CHL` | Chile |
| `CHN` | China |
| `COL` | Colombia |
| `CRI` | Costa Rica |
| `CIV` | Cote d'Ivoire |
| `HRV` | Croatia (hrvatska) |
| `CUW` | Curacao |
| `CYP` | Cyprus |
| `CZE` | Czech Republic |
| `DNK` | Denmark |
| `DOM` | Dominican Republic |
| `ECU` | Ecuador |
| `EGY` | Egypt |
| `EST` | Estonia |
| `FRO` | Faroe Islands |
| `FIN` | Finland |
| `FRA` | France |
| `DEU` | Germany |
| `GHA` | Ghana |
| `GIB` | Gibraltar |
| `GRC` | Greece |
| `GLP` | Guadeloupe |
| `GGY` | Guernsey |
| `VAT` | Holy See |
| `HKG` | Hong Kong |
| `HUN` | Hungary |
| `ISL` | Iceland |
| `IND` | India |
| `IDN` | Indonesia |
| `IRN` | Iran |
| `IRQ` | Iraq |
| `IRL` | Ireland |
| `IMN` | Isle of Man |
| `ISR` | Israel |
| `ITA` | Italy |
| `JAM` | Jamaica |
| `JPN` | Japan |
| `JEY` | Jersey |
| `JOR` | Jordan |
| `KAZ` | Kazakhstan |
| `KEN` | Kenya |
| `KWT` | Kuwait |
| `LAO` | Laos |
| `LVA` | Latvia |
| `LBN` | Lebanon |
| `LIE` | Liechtenstein |
| `LTU` | Lithuania |
| `LUX` | Luxembourg |
| `MKD` | Macedonia |
| `MWI` | Malawi |
| `MYS` | Malaysia |
| `MLT` | Malta |
| `MUS` | Mauritius |
| `MYT` | Mayotte |
| `MEX` | Mexico |
| `MDA` | Moldova |
| `MCO` | Monaco |
| `MNG` | Mongolia |
| `MNE` | Montenegro |
| `MSR` | Montserrat |
| `MAR` | Morocco |
| `NAM` | Namibia |
| `NPL` | Nepal |
| `NLD` | Netherlands |
| `NZL` | New Zealand |
| `NGA` | Nigeria |
| `NOR` | Norway |
| `OMN` | Oman |
| `PAK` | Pakistan |
| `PAN` | Panama |
| `PNG` | Papua New Guinea |
| `PER` | Peru |
| `PHL` | Philippines |
| `POL` | Poland |
| `PRT` | Portugal |
| `QAT` | Qatar |
| `ROU` | Romania |
| `RUS` | Russia |
| `RWA` | Rwanda |
| `VCT` | Saint Vincent and Grenadines |
| `SMR` | San Marino |
| `SAU` | Saudi Arabia |
| `SRB` | Serbia |
| `SGP` | Singapore |
| `SVK` | Slovakia |
| `SVN` | Slovenia |
| `ZAF` | South Africa |
| `KOR` | South Korea |
| `ESP` | Spain |
| `LKA` | Sri Lanka |
| `SPM` | St. Pierre and Miquelon |
| `SJM` | Svalbard and Jan Mayen |
| `SWZ` | Swaziland |
| `SWE` | Sweden |
| `CHE` | Switzerland |
| `SYR` | Syria |
| `TWN` | Taiwan |
| `TZA` | Tanzania United Republic Of |
| `THA` | Thailand |
| `TTO` | Trinidad and Tobago |
| `TUN` | Tunisia |
| `TUR` | Turkey |
| `TCA` | Turks and Caicos Islands |
| `UGA` | Uganda |
| `UKR` | Ukraine |
| `ARE` | United Arab Emirates |
| `GBR` | United Kingdom |
| `USA` | United States |
| `URY` | Uruguay |
| `VEN` | Venezuela |
| `VNM` | Viet Nam |
| `VGB` | Virgin Islands (British) |
| `VIR` | Virgin Islands (u.s.) |
| `ZMB` | Zambia |
| `ZWE` | Zimbabwe |

### Universe IDs

| Code | Description |
|---|---|
| `ALLFUND` | All Fundamentals |
| `ALLSTOCKS` | All Stocks |

### Universe IDs - Major USA

| Code | Description |
|---|---|
| `DJIA` | Dow Jones Industrial Average |
| `NOOTC` | No OTC Exchange |
| `Prussell1000` | Prussell 1000 |
| `Prussell2000` | Prussell 2000 |
| `Prussell3000` | Prussell 3000 |
| `SP1500` | iShares S&P1500 CompositeCap (IVV+IJH+IJR) |
| `SP500` | iShares S&P500 LargeCap (IVV) |

### Universe IDs - Other USA

| Code | Description |
|---|---|
| `$ADR` | American Depositary Receipt |
| `LargeCap` | Large Cap |
| `MasterLP` | Master Limited Partnerships |
| `MicroCap` | MicroCap |
| `MidCap` | Mid Cap |
| `NASD` | NASDAQ Exchange |
| `NASDAQ100` | Nasdaq 100 |
| `NYSE` | NY Stock Exchange |
| `NYSEMKT` | NYSE MKT (AMEX) |
| `OTC` | Over The Counter |
| `SmallCap` | Small Cap |
| `SP400` | iShares S&P400 MidCap (IJH) |
| `SP600` | iShares S&P600 SmallCap (IJR) |

### Formula Functions Sort Parameter

| Code | Description |
|---|---|
| `#ASC` | Sort ascending |
| `#DESC` | Sort descending |

### Formula Functions Sort Style Parameter

| Code | Description |
|---|---|
| `#Neutral` | Neutral |
| `#Top` | Top (Positive Bias) |

### Formula Functions Scope Parameter

| Code | Description |
|---|---|
| `#All` | Operate within selected universe |
| `#Industry` | Operate within Industries in selected universe |
| `#Sector` | Operate within Sectors in selected universe |
| `#SubIndustry` | Operate within Sub-Industries in selected universe |
| `#SubSector` | Operate within Sub-Sectors in selected universe |
| `#SP500` | Operate within the SP500 stocks |
| `#Previous` | Operate on the results from previous rule |
| `#GroupVar` | Operates on groups based on value of variable @Group |
| `#Family` | Operate within each ETF Family |
| `#AssetClass` | Operate within each ETF Class |
| `#Region` | Operate within each ETF Region |
| `#Country` | Operate within each ETF Country |
| `#Method` | Operate within each ETF Method |
| `#Style` | Operate within each ETF Style |
| `#Size` | Operate within each ETF Size |
| `#ETFSector` | Operate within each ETF Sector |

### Aggregate Method Parameter

| Code | Description |
|---|---|
| `#Avg` | Average the values (default, recommended) |
| `#CapAvg` | Cap weighted average the values |

### Aggregate Outlier Handler Parameter

| Code | Description |
|---|---|
| `#Exclude` | Excludes outliers from the aggregation (default) |
| `#Winsor` | The outliers are set to the highest/lowest value that are not outliers |

## Operators

These are the formula-language operators. They are part of the vocabulary but are
not counted as functions or factors.

### Boolean operators

- `And` — `Expr1 And Expr2` evaluates to 1 when both Expr1 and Expr2 are non-zero.
- `Or` — `Expr1 Or Expr2` evaluates to 1 when one or both expressions are non-zero.

### Logical operators

| Operator | Meaning |
|---|---|
| = | Equals |
| != | Not equals |
| ! | Negate |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

### Math operators

| Operator | Meaning |
|---|---|
| + | Add |
| - | Subtract |
| * | Multiply |
| / | Divide |
| ^ | Power (x^y is x raised to the power of y) |

### Precedence operators

Use parentheses `( )` to change the order in which operations are calculated.
For example, `( 10 + 5 ) / 5` evaluates to 3, while `10 + 5 / 5` evaluates to 11.
When in doubt, use parentheses.

### Rule comments

`//` starts a comment. Everything after `//` on a line is ignored, for example
`Close(0) > 5 // this is a comment`.

### Show/Set Variable operator

The `:` operator: the rule `@myvar:expression` sets the variable `@myvar` to the
expression, returns the expression, and displays `@myvar` in the screen report.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `IsNull` | `IsNA` | The NA-replacement function is `IsNA(expr1, expr2)`. |
| `Average` | `Avg` | The set-average function is abbreviated `Avg`. |
| `Power` | `Pow` | The power function is `Pow(number, power)`; the caret is the power operator. |
| `Ln` | `LN` | The natural-log function is uppercase `LN`. |

## FRED Mapping Note

The macro series `##RBDI` (Real Broad Dollar Index) maps to FRED series
`RTWEXBGS` (the FRED name for the Real Broad Dollar Index). An earlier curated
table also mapped `##USR10YR` (10-Year US Real Interest Rate) to `RTWEXBGS`; that
was a duplicated row that does not match the series meaning, so the FRED ID for
`##USR10YR` is intentionally left blank pending a verified mapping.

## See Also

- [universe-operations.md](universe-operations.md) — universe-wide aggregation (the counterpart to the Set functions).
- [universe-filters.md](universe-filters.md) — universe filtering by ticker / RBICS, and the universe IDs listed here.
- [technical.md](technical.md) — `Close`, `Open`, and other price functions that accept the series IDs above.
- [advanced-functions.md](advanced-functions.md) — `FRank`, `Aggregate`, and other higher-order functions.

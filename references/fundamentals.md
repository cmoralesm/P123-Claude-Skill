# Fundamentals — Portfolio123 Reference

Fundamentals covers company-level data that is not a line item from the financial
statements: Actuals (press-release earnings/sales), company identity and
location, corporate actions and splits, dividends, filing-period metadata,
listing identifiers, insider and institutional ownership, and short interest.
For balance-sheet, income-statement, and cash-flow line items see
[financials.md](financials.md); for ratios derived from fundamentals see
[ratios-statistics.md](ratios-statistics.md); for analyst estimates see
[estimates.md](estimates.md).

Coverage: 61 functions / 124 factors — extracted from the official Factor
Reference on 2026-06-09.

## Contents

- [Actuals](#actuals)
- [Company](#company)
- [Corporate Actions](#corporate-actions)
- [Dividends](#dividends)
- [Filings Related](#filings-related)
- [Listing Related](#listing-related)
- [Insider & Institutional](#insider--institutional)
- [Short Interest](#short-interest)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Actuals

Actuals are companies' historical financial data (earnings, sales, net income)
collected primarily from press releases and brokers, as opposed to fundamentals
that come from official filings. They are never restated, can be more frequent
than filings, and are primarily used to compute surprises versus analyst
estimates. The generic `Actual...` functions take an `actual_item` code (for
example `#EBIT`, `#CAPX` — see the Actual Item constants in
[misc.md](misc.md#constants)); the `SalesActual`, `EPSActual`, and `EBITDAActual`
functions are convenience wrappers for those items.

### Functions

#### Actual Functions

The generic Actual functions retrieve a chosen actual item over a period. Pass an
`actual_item` constant as the first argument; `Actual` and `ActualA` also take an
`offset` (and `Actual` a period `type`).

| Function | Description | Arguments |
|---|---|---|
| `Actual` | Retrieve the actual item for a specific period indicated by the offset and period type | actual_item, offset, type |
| `ActualQ` | Retrieve the actual item for the most recent quarter | actual_item |
| `ActualPQ` | Retrieve the actual item for the previous quarter | actual_item |
| `ActualPYQ` | Retrieve the actual item for the previous year quarter | actual_item |
| `ActualTTM` | Retrieve the actual item for the most recent twelve months (TTM) | actual_item |
| `ActualPTM` | Retrieve the actual item for the previous twelve months (PTM) | actual_item |
| `ActualA` | Retrieve the actual annual item for a specific year indicated by the offset with zero being the most recent | actual_item |
| `ActualPY` | Retrieve the actual item for the previous year | actual_item |
| `ActualGr%PQ` | Calculates the most recent quarter growth for a particular actual item | actual_item |
| `ActualGr%PYQ` | Calculates the most recent quarter vs. prior year quarter growth for a particular actual item | actual_item |
| `ActualGr%TTM` | Calculates the most recent twelve months (TTM) growth for a particular actual item | actual_item |
| `ActualGr%A` | Calculates the most recent year growth for a particular actual item | actual_item |

#### `SalesActual(offset, type)`
Historical (actual) sales for the interim or annual period selected by `offset`
and `type`.

#### `EPSActual(offset, type)`
Historical (actual) earnings per share for the interim or annual period selected
by `offset` and `type`.

#### `EBITDAActual(offset, type)`
Historical (actual) EBITDA for the interim or annual period selected by `offset`
and `type`.

### Factors

#### Sales Actual

| Factor | Description | Period |
|---|---|---|
| `SalesActualTTM` | Sales Actual Trailing Twelve Months (TTM) | Trailing 12 Months |
| `SalesActualPTM` | Sales Actual Previous Twelve Months (PTM) | Previous Trailing 12 Months |
| `SalesActualGr%TTM` | Sales Actual Growth Trailing Twelve Months (TTM) | Growth TTM |
| `SalesActualGr%PYQ` | Sales Actual Growth Previous Year Q (PYQ) | Growth PYQ |
| `SalesActualQ1` | Sales Actual, 1 Quarter Ago | 1 Quarter Ago |
| `SalesActualQ2` | Sales Actual, 2 Quarters Ago | 2 Quarters Ago |
| `SalesActualQ3` | Sales Actual, 3 Quarters Ago | 3 Quarters Ago |
| `SalesActualQ4` | Sales Actual, 4 Quarters Ago | 4 Quarters Ago |
| `SalesActualQ5` | Sales Actual, 5 Quarters Ago | 5 Quarters Ago |

#### EPS Actual

| Factor | Description | Period |
|---|---|---|
| `EPSActualTTM` | EPS Actual Trailing Twelve Months (TTM) | Trailing 12 Months |
| `EPSActualPTM` | EPS Actual Previous Twelve Months (PTM) | Previous Trailing 12 Months |
| `EPSActualGr%TTM` | EPS Actual Growth Trailing Twelve Months (TTM) | Growth TTM |
| `EPSActualGr%PYQ` | EPS Actual Growth Previous Year Quarter (PYQ) | Growth PYQ |
| `HistQ1EPSActual` | Historical EPS (Actual), 1 Quarter ago | 1 Quarter Ago |
| `HistQ2EPSActual` | Historical EPS (Actual), 2 Quarters ago | 2 Quarters Ago |
| `HistQ3EPSActual` | Historical EPS (Actual), 3 Quarters ago | 3 Quarters Ago |
| `HistQ4EPSActual` | Historical EPS (Actual), 4 Quarters ago | 4 Quarters Ago |
| `HistQ5EPSActual` | Historical EPS (Actual), 5 Quarters ago | 5 Quarters Ago |

#### EBITDA Actual

| Factor | Description | Period |
|---|---|---|
| `EBITDAActualTTM` | EBITDA Actual trailing twelve months | Trailing 12 Months |
| `EBITDAActualPTM` | EBITDA Actual previous twelve months | Previous Trailing 12 Months |
| `EBITDAActualGr%TTM` | EBITDA Actual growth trailing twelve months (TTM) | Growth TTM |
| `EBITDAActualGr%PYQ` | EBITDA Actual growth previous year quarter (PYQ) | Growth PYQ |

#### Actual Latest

| Factor | Description | Period |
|---|---|---|
| `LatestActualDays` | Calendar days since analysts actuals for the most recent quarter were available from the data vendor.  NOTE: analysts actuals can precede SEC filings | Latest Quarter |
| `LatestActualPeriodDate` | Period date of latest analysts actuals, represented as a number YYYYMMDD.  NOTE: analysts actuals can precede SEC filings | Latest Quarter |

## Company

Company identity and location: country of domicile, exchange country, and
employee counts.

### Functions

#### `Country("cid, cid, cid, ...")`
Filter companies by country of domicile. Pass one or more country IDs (see the
Country IDs constants in [misc.md](misc.md#constants)).

```p123
Country("CHN,HKG,TWN,JPN,SGP,THA")
```

#### `ExchCountry("cid, cid, cid, ...")`
Filter by the country of the exchange on which the security trades (as opposed to
`Country`, which is the country of domicile). For example, `Country("CAN")` is
true for a Canadian company trading on a U.S. exchange, but `ExchCountry("CAN")`
is true only when it trades on a Canadian exchange.

```p123
Country("GBR") and !ExchCountry("GBR")
```

#### `NoEmp(offset, type[, NAHandling])`
Number of employees for the period selected by `offset` and `type`.

### Factors

#### Country Code

| Factor | Description | Period |
|---|---|---|
| `CountryCode` | Country of domicile |  |

#### Number of employees

| Factor | Description | Period |
|---|---|---|
| `NoEmpA` | Number of employees. | Latest Year |
| `NoEmpPY` | Number of employees. | Previous Year |
| `NoEmpGr%A` | Number of employees. | Growth Annual |
| `NoEmpGr%3Y` | Number of employees. | Three Year Annualized Growth |
| `NoEmpGr%5Y` | Number of employees. | Five Year Annualized Growth |
| `NoEmpGr%10Y` | Number of employees. | Ten Year Annualized Growth |
| `NoEmp3YAvg` | Number of employees. | Three Year Average |
| `NoEmp5YAvg` | Number of employees. | Five Year Average |

#### Number of Periods

| Factor | Description | Period |
|---|---|---|
| `#APeriods` | Number of Historical Periods, Annual | Annual Periods |
| `#QPeriods` | Number of Historical Periods, Quarterly | Interim Periods |

#### Earnings Release

| Factor | Description | Period |
|---|---|---|
| `DaysLate` | Returns 0 or the number of days the filing is late (over 40 days for Q and over 75 for K). If the company has no filing data NA is returned. NOTE: This is an estimate. See the Full Description for more details | Next Quarter |
| `WeeksToQ` | Number of weeks until the next earnings release. Typical values are 0-13. Stocks that return 0 are due to report anytime in the next 7 days. It's an estimate based on previous year date. | Weeks To Quarter |
| `WeeksToY` | Number of weeks until the next annual earnings release. Typical values are 0-52. Stocks that return 0 are due to report anytime in the next 7 days. It's an estimate based on previous year date. | Weeks To Year |
| `WeeksIntoQ` | Number of weeks into the most recent quarter. A value of 0 indicates the last earnings report was less than a week ago.  When it reaches values > 11 an earnings report should be announced soon.  NOTE: See WeeksToQ for more precise way to find companies about to report | Weeks Into Quarter |

## Corporate Actions

Corporate actions (mergers, spinoffs, splits) from ICE Data. The screening
functions find the corporate action with the closest announce date to the
point-in-time observation date; they are mainly used to avoid or sell stocks
involved in an acquisition or significant spinoff.

### Functions

#### `PendingCorpAct(ca_type [, ca_retvalue])`
Screen for stocks with a pending corporate action of the given type. Pass a
`ca_type` constant; the optional `ca_retvalue` selects what is returned (see the
Corporate Actions constants in [misc.md](misc.md#constants)).

#### `PastCorpAct(ca_type [, ca_status, lookback, ca_retvalue])`
Screen for stocks with a past corporate action of the given type within the
`lookback` window. `ca_status` and `ca_retvalue` are constants (see
[misc.md](misc.md#constants)).

#### `Splits(days [, countFlag])`
Find stocks that split within the lookback window. With the countFlag argument
false (the default) it returns the cumulative split ratio (or 1 for no split);
with countFlag true it returns the number of splits. Use negative `days` to find
future splits in a simulation.

```p123
Splits(30) > 2
Splits(365, TRUE) > 1
```

#### `SplitCount(days)`
Number of splits within the lookback window of `days`.

#### `SplitFactor(days)`
Cumulative split factor within the lookback window of `days`. Use negative `days`
to find future splits in a simulation.

### Factors

#### Corporate Actions (ICE Data)

| Factor | Description | Period |
|---|---|---|
| `DaysFromMergerAnn` | Returns the days since a M&A (incl spinoff) corporate action has been announced or NA. Equivalent to PendingCorpAct(#MANDA, #ANNCEDAYS) |  |

#### Dividends Days

| Factor | Description | Period |
|---|---|---|
| `DaysFromDivEx` | Days since the last dividend ex-date. Always a positive number or NA |  |
| `DaysFromDivPay` | Days since the last dividend payment date. Always a positive number or NA. If in-between ex-date and pay-date NA is returned. |  |
| `DaysToDivEx` | Days until the next dividend ex-date. Always a positive number or NA. If in-between ex-date and pay-date NA is returned. |  |
| `DaysToDivPay` | Days until next dividend payment date. Always a positive number or NA. |  |

#### Future Dividend and Split Factor

| Factor | Description | Period |
|---|---|---|
| `FutureDivSplitFactor` | Returns the product of all the splits and dividends in the future of the observation date (As-Of Date) |  |

#### Future Dividend Factor

| Factor | Description | Period |
|---|---|---|
| `FutureDivFactor` | Returns the product of all the dividends in the future of the observation date (As-Of Date) |  |

#### Future Split Factor

| Factor | Description | Period |
|---|---|---|
| `FutureSplitFactor` | Returns the product of all the splits in the future of the observation date (As-Of Date) |  |

## Dividends

Per-share dividend data from the corporate-actions feed (as opposed to `DivPaid`,
which uses cash-flow-statement data). By default these include regular dividends
with ex-dates in the period.

### Functions

#### `DivPS(offset, type [, div_type, div_dt, cnt_flag])`
Sum (or, with `cnt_flag` true, count) the per-share dividends during a filing
period. `div_type` (`#Regular`, `#Special`, `#AllDiv`), `div_dt` (`#ExDate`,
`#PayDate`, `#AnnDate`), and `cnt_flag` are optional (see the dividend constants
in [misc.md](misc.md#constants)).

```p123
DivPS(0, TTM) > DivPS(1, TTM)
```

#### `DivPSDays(days [, offset, div_type, div_dt, cnt_flag])`
Sum (or count) the per-share dividends over a window specified in `days`.

```p123
DivPSDays(90, 0) > DivPSDays(90, 90)
```

### Factors

#### Dividend Growth

| Factor | Description | Period |
|---|---|---|
| `Div%ChgA` | Dividend Percent Change, Year Over Year (%) | Latest Year |
| `Div%ChgPYQ` | Dividend Percent Change, Quarter vs Quarter a year ago (%) | Latest Quarter vs 1 Year Ago |
| `Div%ChgTTM` | Dividend Percent Change, TTM (%) | Trailing Twelve Months |
| `Div3YCGr%` | Dividend Growth Rate, 3 Years (uses corporate action data) | 3 Years |
| `Div5YCGr%` | Dividend, 5 Year Growth Rate (uses corporate action data) | 5 Years |

#### Dividends in a Filing Period

| Factor | Description | Period |
|---|---|---|
| `DivPS5YAvg` | Annual average of regular dividends per share for the past 5 fiscal years using ex-dates. | 5 Years |
| `DivPSNextQ` | Sum of all regular dividends with ex-dates falling in the ongoing quarter. If the company has not yet announced the dividends it returns 0 | Next Quarter |
| `DivPSNextQCnt` | Count of all regular dividends with ex-dates in the ongoing quarter. If the company has not yet announced the dividends it returns 0 | Next Quarter |
| `DivPSQ` | Sum of all regular dividends with ex-dates in the most recent quarter. This is equivalent to DivPS(0,QTR,#Regular,#ExDate) | Latest Quarter |
| `DivPSTTM` | Sum of all regular dividends with ex-date in the past 4 quarters. It is equivalent to DivPS(0,TTM,#Regular,#ExDate) | Trailing 12 Months |

#### Dividends in a Time Period

| Factor | Description | Period |
|---|---|---|
| `DivPS52W` | Returns the sum of all regular dividends with ex-dates in the past calendar year.  It's equivalent to DivPSDays(365,0,#Regular,#ExDate) | 52 Weeks |

#### Indicated Annual Dividend

| Factor | Description | Period |
|---|---|---|
| `IAD` | Indicated Annual Dividend. This is a forward looking number used to calculate yield. It can also be used to find companies increasing their dividends. | Next Year |
| `IAD13W` | Indicated Annual Dividend 3 months ago. It can be used to find companies increasing their dividends. | 13 Weeks Ago |
| `IAD26W` | Indicated Annual Dividend 6 months ago. It can be used to find companies increasing their dividends. | 26 Weeks Ago |
| `IAD52W` | Indicated Annual Dividend 1 year ago. It can be used to find companies increasing their dividends. | 52 Weeks Ago |

## Filings Related

Metadata about the filing periods: interim day counts, interim month length, the
share of line items missing, and how recent the latest data is.

### Functions

#### `ActualInterimDays(offset)`
Days in the filing period for the given interim `offset` (usually 91 or 92 for
quarterly, 182 or 183 for semiannual).

#### `InterimMonths(offset)`
Months in the filing period for the given interim `offset`. Always returns 3 (for
quarterly reporters) or 6 (for semiannual reporters).

#### `PerNAPct(offset, type)`
Returns the percent of pulled line items that are missing. TTM returns an average
across the periods.

### Factors

#### Percent of NAs in Period

| Factor | Description | Period |
|---|---|---|
| `PerNAPctQ` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Latest Quarter |
| `PerNAPctPQ` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Previous Quarter |
| `PerNAPctPYQ` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Previous Quarter 1 Year Ago |
| `PerNAPctTTM` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Trailing 12 Months |
| `PerNAPctPTM` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Previous Trailing 12 Months |
| `PerNAPctA` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Latest Year |
| `PerNAPctPY` | Returns the percent of line items pulled that are missing. TTM returns an average of the periods. | Previous Year |

#### Complete Flag

| Factor | Description | Period |
|---|---|---|
| `CompleteStmt` | Complete Statement. Set to TRUE (1) if the latest filing is final and, typically, filed with SEC. FALSE (0) if it contains pre-announcement data. When CompleteStmt is FALSE our''fallback'' mechanism kicks in for most ratios that evaluate to N/A because of incomplete data. | Latest Quarter |

#### Stale Flag

| Factor | Description | Period |
|---|---|---|
| `StaleStmt` | Returns 1 (TRUE) when there's no data in the database for the latest period that is publicly available from a press release or SEC filing | Latest Quarter |

#### Latest in Database

| Factor | Description | Period |
|---|---|---|
| `AnnounceDaysPYQ` | Returns the number of days it took the company to announce the Prev Year Q filing (announce date - period end) | Previous Year Q |
| `AnnounceDaysQ` | Returns the number of days it took the company to announce the latest filing (announce date - period end) | Latest Quarter |
| `PeriodDateA` | Latest Annual Period Date. Represented internally as a number YYYYMMDD and displays as YYYY-MM-DD in screen reports. | Latest Year |
| `PeriodDateQ` | Latest Interim Period Date. Represented internally as a number YYYYMMDD and displays as YYYY-MM-DD in screen reports. | Latest Quarter |
| `QtrComplete` | Latest Quarter Updated by SEC filings | Latest Quarter |

#### Latest (Any Source)

| Factor | Description | Period |
|---|---|---|
| `LatestFilingDate` | The date the latest period was first filed by the company with the SEC. This date may be before any data appears for the as-of date of your analysis due to vendor delays in processing the filing. | Latest Quarter |
| `LatestNewsDate` | The earliest date of either the press release from the company or the date any data appears in the database | Latest Quarter |
| `LatestPeriodDate` | The latest period that has been announced by the company. This data may not have been processed yet by Compustat and/or may not have been filed with the SEC. | Latest Quarter |

## Listing Related

Listing identifiers and flags: ticker, FIGI, exchange code, ADR/MLP/OTC/primary
flags, and security type.

### Functions

#### `Ticker("ticker1, ticker2, ...")`
Returns true if the stock's ticker is in the list, false otherwise. Separate with
commas or spaces; wildcards `*` (any string) and `?` (any character) are
supported.

#### `FIGI("figi1, figi2...")`
Returns true if the stock's FIGI is in the list, false otherwise. Searches the
global share-class-level FIGIs.

### Factors

#### Exchange Code

| Factor | Description | Period |
|---|---|---|
| `ExchangeCode` | Returns the point in time exchange code where the listing trades |  |

#### FIGI Identifier

| Factor | Description | Period |
|---|---|---|
| `ccFIGI` | Returns the Country Composite level FIGI identifier. |  |
| `scFIGI` | Returns the Global Share Class level FIGI identifier. |  |

#### Is ADR

| Factor | Description | Period |
|---|---|---|
| `IsADR` | Returns 1 (TRUE) if the stock is an American Depository Receipt (ADR) |  |

#### Is MLP

| Factor | Description | Period |
|---|---|---|
| `IsMLP` | Returns 1 (TRUE) if the stock is a Master Limited Partnership (MLP) in USA or Canada. |  |

#### Is Over The Counter (OTC)

| Factor | Description | Period |
|---|---|---|
| `IsOTC` | Returns 1 (TRUE) if the stock trades OTC in the USA. |  |

#### Is Primary

| Factor | Description | Period |
|---|---|---|
| `IsPrimary` | Returns 1 (TRUE) if the stock is the primary listing for the company, i.e. not a foreign stock. |  |

#### Security Type

| Factor | Description | Period |
|---|---|---|
| `SecurityType` | Returns the code of the security. For example: Common, Unit, MLP, BDC, etc. See Full Description for the codes |  |

#### Unique Stock Identifier

| Factor | Description | Period |
|---|---|---|
| `StockID` | Returns the internal ID of the current stock or ETF. Can be used to create any number samples in conjunction with modulus function Mod() |  |

## Insider & Institutional

Aggregate insider and institutional ownership, updated from monthly (insider) and
quarterly (institutional) snapshots. Complete ownership data begins around
December 2004. The functions take a month offset (insider) or period offset
(institutional); the factors are point-in-time snapshots.

### Insider Functions

Insider ownership covers shares owned by a company's officers, directors, and
beneficial owners, aggregated and updated monthly. Each function takes a
`mo_offset` argument.

| Function | Description | Arguments |
|---|---|---|
| `InsiderBuySh12M` | Shares bought by insiders past 12 months (in millions) | mo_offset |
| `InsiderBuySh1M` | Shares bought by insiders past 1 month (in millions) | mo_offset |
| `InsiderBuySh3M` | Shares bought by insiders past 3 months (in millions) | mo_offset |
| `InsiderBuySh6M` | Shares bought by insiders past 6 months (in millions) | mo_offset |
| `InsiderBuyTran12M` | Buy transactions by insiders past 12 months (in millions) | mo_offset |
| `InsiderBuyTran1M` | Buy transactions by insiders past 1 month (in millions) | mo_offset |
| `InsiderBuyTran3M` | Buy transactions by insiders past 3 months (in millions) | mo_offset |
| `InsiderBuyTran6M` | Buy transactions by insiders past 6 months (in millions) | mo_offset |
| `InsiderSellSh12M` | Shares sold by insiders past 12 months (in millions) | mo_offset |
| `InsiderSellSh1M` | Shares sold by insiders past 1 month (in millions) | mo_offset |
| `InsiderSellSh3M` | Shares sold by insiders past 3 months (in millions) | mo_offset |
| `InsiderSellSh6M` | Shares sold by insiders past 6 months (in millions) | mo_offset |
| `InsiderSellTran12M` | Sell transactions by insiders past 12 months | mo_offset |
| `InsiderSellTran1M` | Sell transactions by insiders past 1 month | mo_offset |
| `InsiderSellTran3M` | Sell transactions by insiders past 3 months | mo_offset |
| `InsiderSellTran6M` | Sell transactions by insiders past 6 months | mo_offset |
| `InsiderUniqBuy1M` | Unique number of insiders buying past 1 month | mo_offset |
| `InsiderUniqBuy3M` | Unique number of insiders buying past 3 months | mo_offset |
| `InsiderUniqSell1M` | Unique number of insiders selling past 1 month | mo_offset |
| `InsiderUniqSell3M` | Unique number of insiders selling past 3 months | mo_offset |

### Institutional Functions

Institutional ownership covers entities such as mutual funds, pension funds, hedge
funds, and investment banks, snapshotted quarterly. Each function takes a
`period_offset` argument.

| Function | Description | Arguments |
|---|---|---|
| `InstitutionalBuyers` | The number of investors who purchased shares of the company during the period | period_offset |
| `InstitutionalClosed` | The number of investors who sold all shares and closed their holding position in the company during the period | period_offset |
| `InstitutionalHolders` | The total number of investors who own shares of the company | period_offset |
| `InstitutionalNewBuyers` | The number of investors who opened a new position in the company by purchasing shares during the period | period_offset |
| `InstitutionalPctChg` | The net shares changed as a percent of shares outstanding | period_offset |
| `InstitutionalPctOwn` | The percentage of shares outstanding of the company owned by institutional shareholders | period_offset |
| `InstitutionalSellers` | The number of investors who sold shares of the company during the period | period_offset |
| `InstitutionalShsBought` | The number of shares of the company purchased by investors during the period (in millions) | period_offset |
| `InstitutionalShsHeld` | The number of shares of the company held by investors at the end of the period (in millions) | period_offset |
| `InstitutionalShsNet` | The net number of shares of the company transacted by investors during the period (in millions) | period_offset |
| `InstitutionalShsSold` | The number of shares of the company sold by investors during the period (in millions) | period_offset |

### Factors

#### Insider Factors

| Factor | Description | Period |
|---|---|---|
| `Ins#ShrPurch` | Insider total shares purchased past 6 months (positive number in millions) |  |
| `Ins#ShrSold` | Insider total shares sold in the past 6 months (negative number in millions) |  |
| `InsBuyTrans` | Insider number of BUY transactions in the past 6 months |  |
| `Insider#Own` | Common stock in millions held by the officers and directors of the company plus beneficial owners who own more than 5 percent |  |
| `Insider%Own` | Percent of common stock held by the officers and directors of the company plus beneficial owners who own more than 5 percent |  |
| `InsNetShrPurch` | Insider total shares net in the past 6 months (positive or negative number in millions) |  |
| `InsNetTrans` | Insider NET number of transactions in the past 6 months |  |
| `InsSelTrans` | Insider number of SELL transactions in the past 6 months |  |

#### Institutional Factors

| Factor | Description | Period |
|---|---|---|
| `#Institution` | The total number of investors who own shares of the company | Most Recent |
| `Inst#ShsOwn` | The number of shares of the company held by investors in the latest period (in millions) |  |
| `Inst#ShsOwnPQ` | The number of shares of the company held by investors in the previous period (in millions) | Previous Quarter |
| `Inst#ShsPurch` | The number of shares of the company purchased by investors during the latest period (in millions) |  |
| `Inst#ShsPurchPQ` | The number of shares of the company purchased by investors during the previous period (in millions) | Previous Quarter |
| `Inst#ShsSold` | The number of shares of the company sold by investors during the latest period (in millions) |  |
| `Inst#ShsSoldPQ` | The number of shares of the company sold by investors during the previous period (in millions) | Previous Quarter |
| `Inst%Own` | The percentage of shares outstanding of the company owned by institutional shareholders in the latest period |  |
| `Inst%OwnPQ` | The percentage of shares outstanding of the company owned by institutional shareholders in the previous period | Previous Quarter |
| `InstNetPurch` | The net number of shares of the company transacted by investors during the latest period (in millions) |  |
| `InstNetPurchPQ` | The net number of shares of the company transacted by investors during the previous period (in millions) | Previous Quarter |

## Short Interest

Short interest level and ratios: shares short, percent of float, percent of shares
outstanding, days-to-cover ratio, and percent change.

### Factors

#### Short Interest

| Factor | Description | Period |
|---|---|---|
| `SICM` | Short Interest, Current Month Position (millions)  USA only | Latest |
| `SIPM` | Short Interest, Previous Month (millions)  USA only | 1 Month Ago |
| `SIPM2` | Short Interest, 2 Months Ago (millions)  USA only | 2 Months Ago |
| `SIPM3` | Short Interest, 3 Months Ago (millions)  USA only | 3 Months Ago |

#### Short Interest Percent of Float

| Factor | Description | Period |
|---|---|---|
| `SI%Float` | Short Interest, Percent of Float (%)  USA only | Latest |
| `SI%FloatPM` | Short Interest, Percent of Float, 1 Month Ago (%)  USA only | 1 Month Ago |
| `SI%FloatPM2` | Short Interest, Percent of Float, 2 Months Ago (%)  USA only | 2 Months Ago |
| `SI%FloatPM3` | Short Interest, Percent of Float, 3 Months Ago (%)  USA only | 3 Months Ago |

#### Short Interest Percent of Shares Outstanding

| Factor | Description | Period |
|---|---|---|
| `SI%ShsOut` | Short Interest, Percent of Shares Outstanding (%)  USA only | Latest |
| `SI%ShsOutPM` | Short Interest, Percent of Shares Outstanding, 1 Month Ago (%)  USA only | 1 Month Ago |
| `SI%ShsOutPM2` | Short Interest, Percent of Shares Outstanding, 2 Months Ago (%)  USA only | 2 Months Ago |
| `SI%ShsOutPM3` | Short Interest, Percent of Shares Outstanding, 3 Months Ago (%)  USA only | 3 Months Ago |

#### Short Interest Ratio

| Factor | Description | Period |
|---|---|---|
| `SIRatio` | Short Interest Ratio  USA only | Latest |
| `SIRatioPM` | Short Interest Ratio, 1 Month Ago  USA only | 1 Month Ago |
| `SIRatioPM2` | Short Interest Ratio - 2 Months Ago  USA only | 2 Months Ago |
| `SIRatioPM3` | Short Interest Ratio - 3 Months Ago  USA only | 3 Months Ago |

#### Short Interest, Percent Change

| Factor | Description | Period |
|---|---|---|
| `SI1Mo%Chg` | Short Interest, One Month Percent Change (%)  USA only |  |

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `isADR` | `IsADR` | The ADR flag factor is `IsADR` with a capital initial in the dictionary. |
| `EmployeeCount` | `NoEmp` | The employee-count function is `NoEmp(offset, type)`. |
| `SplitRatio` | `SplitFactor` | Use `SplitFactor(days)` for the cumulative split factor, or `SplitCount(days)` for the number of splits. |
| `DividendPS` | `DivPS` | The per-share dividend function is abbreviated `DivPS`. |

## See Also

- [financials.md](financials.md) — balance-sheet, income-statement, and cash-flow line items, including `DivPaid`.
- [ratios-statistics.md](ratios-statistics.md) — ratios and statistics derived from fundamentals.
- [estimates.md](estimates.md) — analyst estimates and the surprise factors computed against Actuals.
- [misc.md](misc.md#constants) — the constant vocabularies referenced above (Actual Item, country IDs, corporate-action and dividend constants).

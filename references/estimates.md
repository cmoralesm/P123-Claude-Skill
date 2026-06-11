# Estimates - Portfolio123 Reference

<!-- name-whitelist: weekAgo cons_item rec_stat NAHandling -->

Analyst-estimate data: consensus EPS and sales estimates, EBITDA/CapEx/FCF estimates, estimate revisions, earnings and sales surprises (including SUE/SUS), historical estimates, and recommendations. Computed valuation ratios live in [Ratios & Statistics](ratios-statistics.md); raw filing data is in [Financials](financials.md); the formula language is summarized in [Technical](technical.md).

Coverage: **20 functions / 158 factors** - extracted from the official Factor Reference on 2026-06-09.

## Contents

- [Estimate Functions](#estimate-functions)
- [EPS Estimates](#eps-estimates)
- [Sales Estimates](#sales-estimates)
- [Other Estimates](#other-estimates)
- [EPS Revisions](#eps-revisions)
- [Surprises](#surprises)
- [Historical](#historical)
- [Recs & Opinions](#recs-opinions)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Estimate Functions

ConsEst functions return an aggregate statistic (consensus) of the estimates from the analysts covering the stock. Please note that many parameter combinations can have lots of N/As. For example most analysts give estimates for Current and Next Year EPS & Sales, but not two or three years out.

Consensus Statistics:

ConsEstCnt(...) Number of estimates

ConsEstHi(...) Highest estimate

ConsEstLow(...) Lowest estimate

ConsEstMean(...) Average estimate

ConsEstMedian(...) Median estimate

ConsEstStdDev(...) Standard Deviation of estimates

ConsEstRSD(...) Relative Standard Deviation of estimates

ConsEstUp(...) Number of analysts revising estimate up in past 75 days

ConsEstDn(...) Number of analysts revising estimate down in past 75 days

Parameters:

cons_item: use one of the values in the table below. Items with a * must use period=0

period: After an item ending with Y or Q, use a digit between 0 and 3 to specify the number of periods you want to look forward. For example, ConsEstMean(#SALEQ,1) is the mean estimate of sales for the next quarter. For items ending with NTM and for #LTG and #PT the period offset must always be 0. Default if missing is 0.

weekAgo: To see if an item has changed recently, use the weekAgo parameter. For example, to see which stocks have increased their sales estimate for the next year in the last 2 weeks, use ConsEstMean(#SALEY, 1, 0) > ConsEstMean(#SALEY, 1, 2). Note that the further you go back, the sparser the data gets.

| cons_item | Estimate | period |
|---|---|---|
| #EPSY | EPS annual |  |
| #EPSQ | EPS quarterly |  |
| #EPSNTM | EPS next twelve months | * |
| #SALEY | Sales annual |  |
| #SALEQ | Sales quarterly |  |
| #SALENTM | Sales next twelve months | * |
| #EBITDAY | EBITDA annual |  |
| #EBITDAQ | EBITDA quarterly |  |
| #EBITDANTM | EBITDA next twelve months | * |
| #CAPXY | CapEx annual |  |
| #CAPXQ | CapEx quarterly |  |
| #CAPXNTM | CapEx next twelve months | * |
| #FCFY | Free cash flow annual |  |
| #FCFQ | Free cash flow quarterly |  |
| #FCFNTM | Free cash flow next twelve months |  |
| #LTG | Long-term growth | * |
| #PT | Price target | * |

Items with a * must use period=0.

Examples:

ConsEstCnt(#EPSY,0): returns the number of estimates for Current Year Sales.

ConsEstMean(#EPSQ,1): returns the average Next Quarter EPS.

ConsEstHi(#EBITDAY,2): returns the high estimate for EBITDA in the year after Next Year.

The nine consensus functions differ only in the statistic returned:

#### `ConsEstRSD(cons_item [, period, weekAgo])`

Relative Standard Deviation of analysts estimates in percentage

#### `ConsEstDn(cons_item [, period, weekAgo])`

Number of analysts revising estimate down in past 75 days

#### `ConsEstHi(cons_item [, period, weekAgo])`

Consensus highest estimate

#### `ConsEstLow(cons_item [, period, weekAgo])`

Consensus lowest estimate

#### `ConsEstMean(cons_item [, period, weekAgo])`

Average of analyst estimates

#### `ConsEstMedian(cons_item [, period, weekAgo])`

Median of analyst estimates

#### `ConsEstStdDev(cons_item [, period, weekAgo])`

Standard Deviation of analysts estimates

#### `ConsEstUp(cons_item [, period, weekAgo])`

Number of analysts revising estimate up in past 75 days

#### `ConsEstCnt(cons_item [, period, weekAgo])`

Number of analysts providing estimates for an item


## EPS Estimates

### Factor variants

#### EPS Estimate Current Quarter

| Factor | Description | Period |
|---|---|---|
| `#AnalystsCurQ` | Number of analysts for current quarter EPS estimate. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `CurQEPSMean` |  | Latest |
| `CurQEPS1WkAgo` |  | Week Ago |
| `CurQEPS4WkAgo` |  | 4 Weeks Ago |
| `CurQEPS8WkAgo` |  | 8 Weeks Ago |
| `CurQEPS13WkAgo` |  | 13 Weeks Ago |
| `CurQEPSHigh` |  | Latest |
| `CurQEPSLow` |  | Latest |
| `CurQEPSStdDev` |  | Latest |

#### EPS Estimate Current Year

| Factor | Description | Period |
|---|---|---|
| `#AnalystsCurFY` | Number of analysts for current fiscal year EPS. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `CurFYEPSMean` | Current fiscal year EPS | Latest |
| `CurFYEPS1WkAgo` | Current fiscal year EPS | Week Ago |
| `CurFYEPS4WkAgo` | Current fiscal year EPS | 4 Weeks Ago |
| `CurFYEPS8WkAgo` | Current fiscal year EPS | 8 Weeks Ago |
| `CurFYEPS13WkAgo` | Current fiscal year EPS | 13 Weeks Ago |
| `CurFYEPSMedian` | Current fiscal year EPS | Latest |
| `CurFYEPSHigh` | Current fiscal year EPS | Latest |
| `CurFYEPSLow` | Current fiscal year EPS | Latest |
| `CurFYEPSStdDev` | Current fiscal year EPS | Latest |

#### EPS Estimate Next Quarter

| Factor | Description | Period |
|---|---|---|
| `#AnalystsNextQ` | Number of analysts for next fiscal quarter EPS. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `NextQEPSMean` |  | Latest |
| `NextQEPS1WkAgo` |  | Week Ago |
| `NextQEPS4WkAgo` |  | 4 Weeks Ago |
| `NextQEPS8WkAgo` |  | 8 Weeks Ago |
| `NextQEPS13WkAgo` |  | 13 Weeks Ago |
| `NextQEPSHigh` |  | Latest |
| `NextQEPSLow` |  | Latest |
| `NextQEPSStdDev` |  | Latest |

#### EPS Estimate Next Year

| Factor | Description | Period |
|---|---|---|
| `#AnalystsNextFY` | Number of analysts for next fiscal year EPS. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `NextFYEPSMean` |  | Latest |
| `NextFYEPS1WkAgo` |  | Week Ago |
| `NextFYEPS4WkAgo` |  | 4 Weeks Ago |
| `NextFYEPS8WkAgo` |  | 8 Weeks Ago |
| `NextFYEPS13WkAgo` |  | 13 Weeks Ago |
| `NextFYEPSMedian` |  | Latest |
| `NextFYEPSHigh` |  | Latest |
| `NextFYEPSLow` |  | Latest |
| `NextFYEPSStdDev` |  | Latest |

#### EPS Estimate Other Years

| Factor | Description | Period |
|---|---|---|
| `FY2EPSMean` | EPS mean estimate 2 years | 2 Years |
| `FY3EPSMean` | EPS estimate 3 years | 3 Years |


## Sales Estimates

### Factor variants

#### Sales Estimate Current Year

| Factor | Description | Period |
|---|---|---|
| `#AnalystsCurFYSales` | Number of analysts for current fiscal year sales. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `CurFYSalesMean` | Current fiscal year sales estimate | Latest |
| `CurFYSales1WkAgo` | Current fiscal year sales estimate | Week Ago |
| `CurFYSales4WkAgo` | Current fiscal year sales estimate | 4 Weeks Ago |
| `CurFYSales8WkAgo` | Current fiscal year sales estimate | 8 Weeks Ago |
| `CurFYSales13WkAgo` | Current fiscal year sales estimate | 13 Weeks Ago |
| `CurFYSalesMedian` | Current fiscal year sales estimate | Latest |
| `CurFYSalesStdDev` | Current fiscal year sales estimate | Latest |

#### Sales Estimate Next Year

| Factor | Description | Period |
|---|---|---|
| `#AnalystsNextFYSales` | Number of analysts for next fiscal year sales. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `NextFYSalesMean` |  | Latest |
| `NextFYSales1WkAgo` |  | Week Ago |
| `NextFYSales4WkAgo` |  | 4 Weeks Ago |
| `NextFYSales8WkAgo` |  | 8 Weeks Ago |
| `NextFYSales13WkAgo` |  | 13 Weeks Ago |
| `NextFYSalesMedian` |  | Latest |
| `NextFYSalesStdDev` |  | Latest |

#### Sales Estimate Other Years

| Factor | Description | Period |
|---|---|---|
| `FY2SalesMean` | Sales estimate 2 years | 2 Years |
| `FY3SalesMean` | Sales estimate 3 years | 3 Years |
| `NTMSalesMean` | Sales Estimate Next Twelve Months |  |


## Other Estimates

### Prebuilt factor families

#### CapEx Estimate Mean

CapEx annual estimate is the current average of multiple analyst estimates for Capital Expenditure for a specified fiscal year.

For example, if three analysts are covering next year's CapEx estimates for a company at $110,000,000, $120,000,000, and $160,000,000, the consensus estimate is $130,000,000.

Estimates for CapEx are available for current, next and other 2 fiscal years in the future:

CapExEstCY

CapExEstNY

CapExEstY2

CapExEstY3

| Factor | Description | Period |
|---|---|---|
| `CapExEstCY` | CapEx Estimate Mean Current Year |  |
| `CapExEstNY` | CapEx Estimate Mean Next Year |  |
| `CapExEstY2` | CapEx Estimate Mean 2 Years |  |
| `CapExEstY3` | CapEx Estimate Mean 3 Years |  |


#### EBITDA Estimate Mean

EBITDA annual estimate is the current average of multiple analyst estimates for Earnings Before Interest, Taxes, Depreciation and Amortization for a fiscal year. For example, if three analysts are covering next year's EBITDA estimates for a company at $5,000,000,000, $6,000,000,000, and $8,500,000,000, the consensus estimate is $6,500,000,000.

Estimates for EBITDA are available for current, next and other 2 years in the future:

EBITDAEstCY

EBITDAEstNY

EBITDAEstY2

EBITDAEstY3

| Factor | Description | Period |
|---|---|---|
| `EBITDAEstCY` | Average of analyst estimates for EBITDA for the Current Year | Current Year |
| `EBITDAEstNY` | Average of analyst estimates for EBITDA for the Next Year | Next Year |
| `EBITDAEstY2` | Average of analyst estimates for EBITDA for Year 2 | 2 Years |
| `EBITDAEstY3` | Average of analyst estimates for EBITDA for the Year 3 | 3 Years |


#### FCF Estimate Mean

FCF annual estimate is the current average of multiple analyst estimates for Free Cash Flow for a fiscal year. For example, if three analysts are covering next year's FCF estimates for a company at $110,000,000, $120,000,000, and $160,000,000, the consensus estimate is $130,000,000.

Estimates for FCF are available for current, next and other 2 years in the future.

FCF EstCY

FCF EstNY

FCF EstY2

FCF EstY3

| Factor | Description | Period |
|---|---|---|
| `FCFEstCY` | Free cash flow estimate mean current year | Current Year |
| `FCFEstNY` | Free cash flow estimate mean next year | Next Year |
| `FCFEstY2` | Free cash flow estimate mean 2 years | 2 years |
| `FCFEstY3` | Free cash flow estimate mean 3 years | 3 Years |



## EPS Revisions

### Factor variants

#### EPS Revisions Current Quarter

| Factor | Description | Period |
|---|---|---|
| `CurQDnRevLastWk` | Current Quarter Down Revisions, Last Week | Past Week |
| `CurQUpRevLastWk` | Current Quarter Up Revisions, Last Week | Past Week |
| `CurQDnRev4WkAgo` | Current Quarter Down Revisions, 4 Weeks ago | Past 4 Weeks |
| `CurQUpRev4WkAgo` | Current Quarter Up Revisions, 4 Weeks ago | Past 4 Weeks |

#### EPS Revisions Current Year

| Factor | Description | Period |
|---|---|---|
| `CurFYDnRevLastWk` | Current Fiscal Year Down Revisions, Last Week | Past Week |
| `CurFYUpRevLastWk` | Current Fiscal Year Up Revisions, Last Week | Past Week |
| `CurFYDnRev4WkAgo` | Current Fiscal Year Down Revisions, 4 Weeks ago | Past 4 Weeks |
| `CurFYUpRev4WkAgo` | Current Fiscal Year Up Revisions, 4 Weeks ago | Past 4 Weeks |

#### EPS Revisions Next Quarter

| Factor | Description | Period |
|---|---|---|
| `NextQDnRevLastWk` | Next Quarter Down Revisions, Last Week | Past Week |
| `NextQUpRevLastWk` | Next Quarter Up Revisions, Last Week | Past Week |
| `NextQDnRev4WkAgo` | Next Quarter Down Revisions, 4 Weeks ago | Past 4 Weeks |
| `NextQUpRev4WkAgo` | Next Quarter Up Revisions, 4 Weeks ago | Past 4 Weeks |

#### EPS Revisions Next Year

| Factor | Description | Period |
|---|---|---|
| `NextFYDnRevLastWk` | Next Fiscal Year Down Revisions, Last Week | Past Week |
| `NextFYUpRevLastWk` | Next Fiscal Year Up Revisions Last Week | Past Week |
| `NextFYDnRev4WkAgo` | Next Fiscal Year Down Revisions, 4 Weeks ago | Past 4 Weeks |
| `NextFYUpRev4WkAgo` | Next Fiscal Year Up Revisions, 4 Weeks ago | Past 4 Weeks |

#### Sum of EPS Revisions

| Factor | Description | Period |
|---|---|---|
| `TotRevisionsLastW` | Sum of  (No Analysts Up Revisions) - (No Analysts Dn revisions) in the past week. | Past Week |
| `TotRevisions4W` | Sum of  (No Analysts Up Revisions) - (No Analysts Dn revisions) in the past 4 weeks. | Past 4 Weeks |


## Surprises

### Functions

#### `EPSSurprise(offset, type)`

Surprise is calculated by dividing the difference between the actual result and the mean estimate at the time of the earnings announcement by the absolute value of the mean estimate.

Functions

EPSSurprise(offset, period)

SalesSurprise(offset, period)

Parameters

offset: 0 - N where 0 is latest period

period: ANN , QTR

Prebuilt Factors

Surprise%Q1
Surprise%Q2
Surprise%Q3
Surprise%Q4
Surprise%Q5
Surprise%Y1
Surprise%Y2
Surprise%Y3
Surprise%Y4
SalesSurp%Q1
SalesSurp%Q2
SalesSurp%Q3
SalesSurp%Q4
SalesSurp%Q5
SalesSurp%Y1
SalesSurp%Y2
SalesSurp%Y3
SalesSurp%Y4

Return the surprise for the estimate and period. For example Surprise%Q1 represent the most recent quarter surprise, Q2 two quarters a go, and so on. Surprise%Q1 is equivalent to EPSSurprise(0,QTR)


#### `SalesSurprise(offset, type)`

Sales Surprise in % Shares the definition of `EPSSurprise` above.

#### `EPSSUE(offset, type [, constraint])`

Standardized Unexpected (Earnings or Sales) for a given period is computed by dividing the unexpected results (Actual - Est) by the standard deviation of the estimates preceding the actual announcement:

SU = (Actual - Est) / SD

When analysts disagree, the standard deviation of estimates is high, and the degree to which actual earnings are considered as unexpected (the SU measure) would be rather low. Conversely, the higher the consensus among analysts, the lower the consensus standard deviation, which results in a higher surprise for a given level of unexpected results.

Functions

EPSSUE(offset , type , constraint=0)
SalesSUS(offset , type , constraint=0)

| Parameters |  |
|---|---|
| offset | period offset (most current is 0, previous is 1, etc) |
| type | QTR or ANN |
| constraint | Upper and lower bound. For Example a contraint of 5 would limit the value in the -5 to +5 range. |

Factors

SUEQ1-4, SUEY1-4: Standardized Unexpected Earnings for period
SUSQ1-4, SUSY1-4: Standardized Unexpected Sales for period

NOTE: pre-defined factors are constrainged to values between -10 to +10

Empirical Evidence

As shown in Kaestner(2006)'s paper[1], Cumulative Abnormal Returns (CAR) for portfolios grouped by SUE decile scores are positively correlated with SUE. For example Table 3 in the paper shows an abnormal return of 4.31% 60 days after the announcement for Portfolio 1 made up of the top decile SUE values.

However, the relationship is more complex when previous results of SUE are taken into account. Investors extrapolate the information too far into the future such that a series of past similar surprises causes an overreaction phenomenon, which drives stock prices below their fundamental value after a series of negative surprises, and above their fundamental value after a series of positive surprises.

This effect is shown in Table 6 where the highest CAR(60) of 4.94% occurs for Portfolio 1 (the top SUE decile) that followed a negative surprise (row labelled "1,-").

It also shows that the worst CAR(60) return of -1.97% for Portfolio 1 made up of stocks that had 4 prior positive surprises (row labelled "1,++++ "). In other words the effect of a positive surprise diminishes to the point of being inversely proportional the longer the positive trend continues.

References

1. Kaestner 2006, Anomalous Price Behavior Following Earnings Surprises: Does Representativeness Cause Overreaction?


#### `SalesSUS(offset, type [, constraint])`

Standardized Unexpected Sales general formula Shares the definition of `EPSSUE` above.

### Prebuilt factor families

#### Analyst EPS Surprise

| Factor | Description | Period |
|---|---|---|
| `Surprise%Q1` | Earnings Surprise (Estimated vs. Actual), 1 Quarter Ago (%) | Most Recent Quarter |
| `Surprise%Q2` | Earnings Surprise (Estimated vs. Actual), 2 Quarters Ago (%) | 2 Quarters Ago |
| `Surprise%Q3` | Earnings Surprise (Estimated vs. Actual), 3 Quarters Ago (%) | 3 Quarters Ago |
| `Surprise%Q4` | Earnings Surprise (Estimated vs. Actual), 4 Quarters Ago (%) | 4 Quarters Ago |
| `Surprise%Q5` | Earnings Surprise (Estimated vs. Actual), 5 Quarters Ago (%) | 5 Quarters Ago |
| `Surprise%Y1` | Earnings Surprise (Estimated vs. Actual), Most recent year (%) | Most Recent Year |
| `Surprise%Y2` | Earnings Surprise (Estimated vs. Actual), 2 Year Ago (%) | 2 Years Ago |
| `Surprise%Y3` | Earnings Surprise (Estimated vs. Actual), 3 Year Ago (%) | 3 Years Ago |
| `Surprise%Y4` | Earnings Surprise (Estimated vs. Actual), 4 Year Ago (%) | 4 Years Ago |
| `SalesSurp%Q1` | Sales Surprise (Estimated vs. Actual), 1 Quarter Ago (%) | Most Recent Quarter |
| `SalesSurp%Q2` | Sales Surprise (Estimated vs. Actual), 2 Quarters Ago (%) | 2 Quarters Ago |
| `SalesSurp%Q3` | Sales Surprise (Estimated vs. Actual), 3 Quarters Ago (%) | 3 Quarters Ago |
| `SalesSurp%Q4` | Sales Surprise (Estimated vs. Actual), 4 Quarters Ago (%) | 4 Quarters Ago |
| `SalesSurp%Q5` | Sales Surprise (Estimated vs. Actual), 5 Quarters Ago (%) | 5 Quarters Ago |
| `SalesSurp%Y1` | Sales Surprise (Estimated vs. Actual), Most recent year (%) | Most Recent Year |
| `SalesSurp%Y2` | Sales Surprise (Estimated vs. Actual), 2 Years Ago (%) | 2 Years Ago |
| `SalesSurp%Y3` | Sales Surprise (Estimated vs. Actual), 3 Years Ago (%) | 3 Years Ago |
| `SalesSurp%Y4` | Sales Surprise (Estimated vs. Actual), 4 Years Ago (%) | 4 Years Ago |


#### Unexpected Earnings (SUE)

| Factor | Description | Period |
|---|---|---|
| `SUEQ1` | Standardized Unexpected Earnings Most Recent Quarter | Most Recent Quarter |
| `SUEQ2` | Standardized Unexpected Earnings 2 Quarters Ago | 2 Quarter Ago |
| `SUEQ3` | Standardized Unexpected Earnings 3 Quarters Ago | 3 Quarters Ago |
| `SUEQ4` | Standardized Unexpected Earnings 4 Quarters Ago | 4 Quarter Ago |
| `SUEY1` | Standardized Unexpected Earnings Most Recent Year | Most Recent Year |
| `SUEY2` | Standardized Unexpected Earnings 2 Years Ago | 2 Years Ago |
| `SUEY3` | Standardized Unexpected Earnings 3 Years Ago | 3 Years Ago |
| `SUEY4` | Standardized Unexpected Earnings 4 Years Ago | 4 Years Ago |
| `SUSQ1` | Standardized Unexpected Sales Most Recent Quarter | Most Recent Quarter |
| `SUSQ2` | Standardized Unexpected Sales 2 Quarters Ago | 2 Quarter Ago |
| `SUSQ3` | Standardized Unexpected Sales 3 Quarters Ago | 3 Quarters Ago |
| `SUSQ4` | Standardized Unexpected Sales 4 Quarters Ago | 4 Quarter Ago |
| `SUSY1` | Standardized Unexpected Sales Most Recent Year | Most Recent Year |
| `SUSY2` | Standardized Unexpected Sales 2 Years Ago | 2 Years Ago |
| `SUSY3` | Standardized Unexpected Sales 3 Years Ago | 3 Years Ago |
| `SUSY4` | Standardized Unexpected Sales 4 Years Ago | 4 Years Ago |



## Historical

### Functions

#### `EPSEst(offset, type)`

EPSEst is the last mean estimate prior to the actual announcement of earnings per share. It can be used with EPSActual to calculate EPSSurprise. This is a historical record of the estimate prior to the last earnings announcement. For the current mean estimate, use CurQEPSMean instead.

EPSEst(offset , period)

offset: 0-10

period: ANN , QTR

Function that returns the last EPS estimate for past periods. 

HistQ1EPSEst

HistQ2EPSEst

HistQ3EPSEst

HistQ4EPSEst

HistQ5EPSEst

Pre-build factors to use in lieu of the function. HistQ1EPSEst represent the most recent quarter latest estimate, Q2 two quarters a go, and so on. HistQ1EPSEst is equivalent to EPSEst(0,QTR)


#### `EPSHistEstCnt(offset, type)`

Historical EPS Estimate Number of Analysts


#### `SalesHistEstCnt(offset, type)`

Historical Sales Estimate Number of Analysts


#### `EPSHistEstSD(offset, type)`

Historical EPS Estimate Standard Deviation


#### `SalesHistEstSD(offset, type)`

Historical Sales Estimate Standard Deviation


#### `SalesEst(offset, type)`

Historical Sales Estimate


### Prebuilt factor families

#### Historical EPS Estimate

| Factor | Description | Period |
|---|---|---|
| `HistQ1EPSEst` | Historical EPS Mean Estimate, 1 Quarter ago | 1 Quarter Ago |
| `HistQ2EPSEst` | Historical EPS Mean Estimate, 2 Quarters ago | 2 Quarters Ago |
| `HistQ3EPSEst` | Historical EPS Mean Estimate, 3 Quarters ago | 3 Quarters Ago |
| `HistQ4EPSEst` | Historical EPS Mean Estimate, 4 Quarters ago | 4 Quarters Ago |
| `HistQ5EPSEst` | Historical EPS Mean Estimate, 5 Quarters ago | 5 Quarters Ago |


### Factor variants

#### Historical Sales Estimate

| Factor | Description | Period |
|---|---|---|
| `SalesEstQ1` | Sales Estimate, 1 Quarter Ago | 1 Quarter Ago |
| `SalesEstQ2` | Sales Estimate, 2 Quarters Ago | 2 Quarters Ago |
| `SalesEstQ3` | Sales Estimate, 3 Quarters Ago | 3 Quarters Ago |
| `SalesEstQ4` | Sales Estimate, 4 Quarters Ago | 4 Quarters Ago |
| `SalesEstQ5` | Sales Estimate, 5 Quarters Ago | 5 Quarters Ago |

#### Historical EPS Difference

| Factor | Description | Period |
|---|---|---|
| `HistQ1Difference` | Historical Quarter Difference (Actual - Estimate), 1 Quarter Ago | 1 Quarter Ago |
| `HistQ2Difference` | Historical Quarter Difference (Actual - Estimate), 2 Quarters Ago | 2 Quarters Ago |
| `HistQ3Difference` | Historical Quarter Difference (Actual - Estimate), 3 Quarters Ago | 3 Quarters Ago |
| `HistQ4Difference` | Historical Quarter Difference (Actual - Estimate), 4 Quarters Ago | 4 Quarters Ago |
| `HistQ5Difference` | Historical Quarter Difference (Actual - Estimate), 5 Quarters Ago | 5 Quarters Ago |


## Recs & Opinions

### Functions

#### `ConsRec(rec_stat [, weekAgo])`

The consensus recommendation function enables users to handle analysts recommendations data. It allows to count the total number of reccomandations and each recommendation level. For example, if three analysts respectively give Buy, Hold and Hold reccomendations, ConsRec(#HoldCnt) will return 2.

ConsRec(rec_stat[, weekAgo])

The parameter supported by rec_stat are: #AvgRec, #RecCnt, #BuyCnt, #OverCnt, #HoldCnt, #UnderCnt, #SellCnt


### Prebuilt factor families

#### Average Recommendation

These are the average values of all analysts' opinions for a company. They are calculated by totaling all the opinion ratings and dividing by the total number of analysts offering opinions.

Factors

AvgRec

Average Recommendation

AvgRec1WkAgo

Average Recommendation 1 Weeks ago

AvgRec4WkAgo

Average Recommendation 4 Weeks ago

AvgRec8WkAgo

Average Recommendation 8 Weeks ago

AvgRec13WkAgo

Average Recommendation 13 Weeks ago

Scale

FactSet uses a scale 1 (strong buy), 1.5 (buy), 2 (hold), 2.5 (underperform), and 3 (sell).

CapitalIQ uses a scale of 1 (strong buy), 2 (buy), 3 (hold), 4 (underperform), and 5 (sell).

| Factor | Description | Period |
|---|---|---|
| `AvgRec` | Average Recommendation on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5. | Current |
| `AvgRec1WkAgo` | Average Recommendation 1 Weeks ago on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5. | 1 Week Ago |
| `AvgRec4WkAgo` | Average Recommendation 4 Weeks ago on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5. | 4 Weeks Ago |
| `AvgRec8WkAgo` | Average Recommendation 8 Weeks ago on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5. | 8 Weeks Ago |
| `AvgRec13WkAgo` | Average Recommendation 13 Weeks ago on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5. | 13 Weeks Ago |


### Factor variants

#### Long Term EPS Growth

| Factor | Description | Period |
|---|---|---|
| `#AnalystsLTGrthRt` | This is the number of analysts who are reporting a long term earnings per share growth rate. If a security has no analysts, this factor returns NA, not 0. |  |
| `LTGrthMean` | Long Term EPS Growth Rate (%) | Latest |
| `LTGrth1WkAgo` | Long Term EPS Growth Rate (%) | Week Ago |
| `LTGrth4WkAgo` | Long Term EPS Growth Rate (%) | 4 Weeks Ago |
| `LTGrth8WkAgo` | Long Term EPS Growth Rate (%) | 8 Weeks Ago |
| `LTGrth13WkAgo` | Long Term EPS Growth Rate (%) | 13 Weeks Ago |
| `LTGrthHigh` | Long Term EPS Growth Rate (%) | Latest |
| `LTGrthLow` | Long Term EPS Growth Rate (%) | Latest |
| `LTGrthStdDev` | Long Term EPS Growth Rate (%) | Latest |

#### Price Target

| Factor | Description | Period |
|---|---|---|
| `#AnalystsPriceTarget` | Number of analysts giving price target estimates. Note: if a security has no analysts, this factor returns NA, not 0. |  |
| `PriceTarget4WkAgo` | Analyst mean Price Target 4 weeks ago  NOTE: complete price target data is available starting in 2001 |  |
| `PriceTargetHi` | High analyst mean Price Target  NOTE: complete price target data is available starting in 2001 |  |
| `PriceTargetLo` | Low analyst mean Price Target  NOTE: complete price target data is available starting in 2001 |  |
| `PriceTargetMean` | Analyst mean Price Target 0-18 months out  NOTE: complete price target data is available starting in 2001 |  |
| `PriceTargetStdDev` | Analyst Price Target standard deviation  NOTE: complete price target data is available starting in 2001 |  |


## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `EstEPSCY` | `CurFYEPSMean` | Current-fiscal-year consensus EPS uses the CurFY/NextFY family. The legacy Est... family does not exist in the dictionary. |
| `EstEPSNY` | `NextFYEPSMean` | Next-fiscal-year consensus EPS is `NextFYEPSMean`. |
| `EstEPSCQ` | `CurQEPSMean` | Current-quarter consensus EPS is `CurQEPSMean`. |
| `EstEPSNQ` | `NextQEPSMean` | Next-quarter consensus EPS is `NextQEPSMean`. |
| `EstSalesCY` | `CurFYSalesMean` | Current-fiscal-year consensus sales is `CurFYSalesMean`. |
| `EstSalesNY` | `NextFYSalesMean` | Next-fiscal-year consensus sales is `NextFYSalesMean`. |
| `CurFYEPS` | `CurFYEPSMean` | The prebuilt consensus factor needs the statistic suffix: `CurFYEPSMean`, `CurFYEPSMedian`, `CurFYEPSHigh`, etc. |
| `NextFYEPS` | `NextFYEPSMean` | Add the statistic suffix: `NextFYEPSMean`, `NextFYEPSHigh`, and so on. |
| `EPSSurprise%` | `Surprise%Q1` | Prebuilt surprise factors are `Surprise%Q1`..`Surprise%Q5` / `Surprise%Y1`..; the function is `EPSSurprise(offset, type)`. |
| `AvgRecom` | `AvgRec` | Average recommendation is `AvgRec` (with `AvgRec1WkAgo`, `AvgRec4WkAgo`, etc.). |
| `ConsRecom` | `ConsRec` | The recommendation function is `ConsRec(rec_stat[, weekAgo])`. |

## See Also

- [Ratios & Statistics](ratios-statistics.md) - computed valuation, margin, and per-share ratios.
- [Financials](financials.md) - reported (actual) filing data behind the surprises.
- [Technical](technical.md) - price/volume functions and the formula language.

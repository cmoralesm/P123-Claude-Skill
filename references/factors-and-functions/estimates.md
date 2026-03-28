# Estimates

Data relating to consensus analyst estimates.

## Estimate Functions

Consensus estimate functions

### Consensus Relative Standard Deviation

Relative Standard Deviation of analysts estimates in percentage

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstRSD()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstRSD |


### Consensus Down

Number of analysts revising estimate down in past 75 days

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstDn()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstDn |


### Consensus High

Consensus highest estimate

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstHi()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstHi |


### Consensus Low

Consensus lowest estimate

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstLow()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstLow |


### Consensus Mean

Average of analyst estimates

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstMean()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstMean |


### Consensus Median

Median of analyst estimates

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstMedian()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstMedian |


### Consensus Standard Deviation

Standard Deviation of analysts estimates

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstStdDev()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstStdDev |


### Consensus Up

Number of analysts revising estimate up in past 75 days

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstUp()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstUp |


### Consensus Count

Number of analysts providing estimates for an item

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsEstCnt()` | cons_item [, period, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsEstCnt |


## EPS Estimates

Earnings per share consensus estimates with statistics, number of analysts, and previous values for trend analysts.

### EPS Estimate Current Quarter

Number of analysts for current quarter EPS estimate. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsCurQ` |  |  |  |
| `CurQEPSMean` |  | Latest |  |
| `CurQEPS1WkAgo` |  | Week Ago |  |
| `CurQEPS4WkAgo` |  | 4 Weeks Ago |  |
| `CurQEPS8WkAgo` |  | 8 Weeks Ago |  |
| `CurQEPS13WkAgo` |  | 13 Weeks Ago |  |
| `CurQEPSHigh` |  | Latest |  |
| `CurQEPSLow` |  | Latest |  |
| `CurQEPSStdDev` |  | Latest |  |


### EPS Estimate Current Year

Number of analysts for current fiscal year EPS. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsCurFY` |  |  |  |
| `CurFYEPSMean` |  | Latest |  |
| `CurFYEPS1WkAgo` |  | Week Ago |  |
| `CurFYEPS4WkAgo` |  | 4 Weeks Ago |  |
| `CurFYEPS8WkAgo` |  | 8 Weeks Ago |  |
| `CurFYEPS13WkAgo` |  | 13 Weeks Ago |  |
| `CurFYEPSMedian` |  | Latest |  |
| `CurFYEPSHigh` |  | Latest |  |
| `CurFYEPSLow` |  | Latest |  |
| `CurFYEPSStdDev` |  | Latest |  |


### EPS Estimate Next Quarter

Number of analysts for next fiscal quarter EPS. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsNextQ` |  |  |  |
| `NextQEPSMean` |  | Latest |  |
| `NextQEPS1WkAgo` |  | Week Ago |  |
| `NextQEPS4WkAgo` |  | 4 Weeks Ago |  |
| `NextQEPS8WkAgo` |  | 8 Weeks Ago |  |
| `NextQEPS13WkAgo` |  | 13 Weeks Ago |  |
| `NextQEPSHigh` |  | Latest |  |
| `NextQEPSLow` |  | Latest |  |
| `NextQEPSStdDev` |  | Latest |  |


### EPS Estimate Next Year

Number of analysts for next fiscal year EPS. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsNextFY` |  |  |  |
| `NextFYEPSMean` |  | Latest |  |
| `NextFYEPS1WkAgo` |  | Week Ago |  |
| `NextFYEPS4WkAgo` |  | 4 Weeks Ago |  |
| `NextFYEPS8WkAgo` |  | 8 Weeks Ago |  |
| `NextFYEPS13WkAgo` |  | 13 Weeks Ago |  |
| `NextFYEPSMedian` |  | Latest |  |
| `NextFYEPSHigh` |  | Latest |  |
| `NextFYEPSLow` |  | Latest |  |
| `NextFYEPSStdDev` |  | Latest |  |


### EPS Estimate Other Years

EPS mean estimate 2 years

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FY2EPSMean` |  | 2 Years |  |
| `FY3EPSMean` |  | 3 Years |  |


## Sales Estimates

Sales consensus estimates with statistics, number of analysts, and previous values for trend analysts.

### Sales Estimate Current Year

Number of analysts for current fiscal year sales. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsCurFYSales` |  |  |  |
| `CurFYSalesMean` |  | Latest |  |
| `CurFYSales1WkAgo` |  | Week Ago |  |
| `CurFYSales4WkAgo` |  | 4 Weeks Ago |  |
| `CurFYSales8WkAgo` |  | 8 Weeks Ago |  |
| `CurFYSales13WkAgo` |  | 13 Weeks Ago |  |
| `CurFYSalesMedian` |  | Latest |  |
| `CurFYSalesStdDev` |  | Latest |  |


### Sales Estimate Next Year

Number of analysts for next fiscal year sales. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsNextFYSales` |  |  |  |
| `NextFYSalesMean` |  | Latest |  |
| `NextFYSales1WkAgo` |  | Week Ago |  |
| `NextFYSales4WkAgo` |  | 4 Weeks Ago |  |
| `NextFYSales8WkAgo` |  | 8 Weeks Ago |  |
| `NextFYSales13WkAgo` |  | 13 Weeks Ago |  |
| `NextFYSalesMedian` |  | Latest |  |
| `NextFYSalesStdDev` |  | Latest |  |


### Sales Estimate Other Years

Sales estimate 2 years

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FY2SalesMean` |  | 2 Years |  |
| `FY3SalesMean` |  | 3 Years |  |
| `NTMSalesMean` |  |  |  |


## Other Estimates

Other consensus mean estimates

### CapEx Estimate Mean

CapEx Estimate Mean Current Year

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CapExEstCY` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapExEstCY |
| `CapExEstNY` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapExEstNY |
| `CapExEstY2` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapExEstY2 |
| `CapExEstY3` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapExEstY3 |


### EBITDA Estimate Mean

Average of analyst estimates for EBITDA for the Current Year

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EBITDAEstCY` |  | Current Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAEstCY |
| `EBITDAEstNY` |  | Next Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAEstNY |
| `EBITDAEstY2` |  | 2 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAEstY2 |
| `EBITDAEstY3` |  | 3 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAEstY3 |


### FCF Estimate Mean

Free cash flow estimate mean current year

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `FCFEstCY` |  | Current Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FCFEstCY |
| `FCFEstNY` |  | Next Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FCFEstNY |
| `FCFEstY2` |  | 2 years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FCFEstY2 |
| `FCFEstY3` |  | 3 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=FCFEstY3 |


## EPS Revisions

Factors to indicate number of analysts revisions EPS consensus estimate Up or Down. NOTE: Data is only updated in the weekend

### EPS Revisions Current Quarter

Current Quarter Down Revisions, Last Week

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CurQDnRevLastWk` |  | Past Week |  |
| `CurQUpRevLastWk` |  | Past Week |  |
| `CurQDnRev4WkAgo` |  | Past 4 Weeks |  |
| `CurQUpRev4WkAgo` |  | Past 4 Weeks |  |


### EPS Revisions Current Year

Current Fiscal Year Down Revisions, Last Week

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CurFYDnRevLastWk` |  | Past Week |  |
| `CurFYUpRevLastWk` |  | Past Week |  |
| `CurFYDnRev4WkAgo` |  | Past 4 Weeks |  |
| `CurFYUpRev4WkAgo` |  | Past 4 Weeks |  |


### EPS Revisions Next Quarter

Next Quarter Down Revisions, Last Week

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NextQDnRevLastWk` |  | Past Week |  |
| `NextQUpRevLastWk` |  | Past Week |  |
| `NextQDnRev4WkAgo` |  | Past 4 Weeks |  |
| `NextQUpRev4WkAgo` |  | Past 4 Weeks |  |


### EPS Revisions Next Year

Next Fiscal Year Down Revisions, Last Week

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NextFYDnRevLastWk` |  | Past Week |  |
| `NextFYUpRevLastWk` |  | Past Week |  |
| `NextFYDnRev4WkAgo` |  | Past 4 Weeks |  |
| `NextFYUpRev4WkAgo` |  | Past 4 Weeks |  |


### Sum of EPS Revisions

Sum of  (No Analysts Up Revisions) - (No Analysts Dn revisions) in the past week.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `TotRevisionsLastW` |  | Past Week |  |
| `TotRevisions4W` |  | Past 4 Weeks |  |


## Surprises

Analysts surprises

### Analyst EPS Surprise

EPS surprise (Est vs. Actual)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EPSSurprise()` | offset, type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSSurprise |
| `Surprise%Q1` |  | Most Recent Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Q1 |
| `Surprise%Q2` |  | 2 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Q2 |
| `Surprise%Q3` |  | 3 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Q3 |
| `Surprise%Q4` |  | 4 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Q4 |
| `Surprise%Q5` |  | 5 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Q5 |
| `Surprise%Y1` |  | Most Recent Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Y1 |
| `Surprise%Y2` |  | 2 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Y2 |
| `Surprise%Y3` |  | 3 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Y3 |
| `Surprise%Y4` |  | 4 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Surprise%Y4 |


### Analyst Sales Surprise

Sales Surprise in %

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SalesSurprise()` | offset, type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurprise |
| `SalesSurp%Q1` |  | Most Recent Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Q1 |
| `SalesSurp%Q2` |  | 2 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Q2 |
| `SalesSurp%Q3` |  | 3 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Q3 |
| `SalesSurp%Q4` |  | 4 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Q4 |
| `SalesSurp%Q5` |  | 5 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Q5 |
| `SalesSurp%Y1` |  | Most Recent Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Y1 |
| `SalesSurp%Y2` |  | 2 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Y2 |
| `SalesSurp%Y3` |  | 3 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Y3 |
| `SalesSurp%Y4` |  | 4 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSurp%Y4 |


### Unexpected Earnings (SUE)

Standardized Unexpected Earnings general formula

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EPSSUE()` | offset, type [, constraint] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSSUE |
| `SUEQ1` |  | Most Recent Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEQ1 |
| `SUEQ2` |  | 2 Quarter Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEQ2 |
| `SUEQ3` |  | 3 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEQ3 |
| `SUEQ4` |  | 4 Quarter Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEQ4 |
| `SUEY1` |  | Most Recent Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEY1 |
| `SUEY2` |  | 2 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEY2 |
| `SUEY3` |  | 3 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEY3 |
| `SUEY4` |  | 4 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUEY4 |


### Unexpected Sales (SUS)

Standardized Unexpected Sales general formula

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SalesSUS()` | offset, type [, constraint] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesSUS |
| `SUSQ1` |  | Most Recent Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSQ1 |
| `SUSQ2` |  | 2 Quarter Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSQ2 |
| `SUSQ3` |  | 3 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSQ3 |
| `SUSQ4` |  | 4 Quarter Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSQ4 |
| `SUSY1` |  | Most Recent Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSY1 |
| `SUSY2` |  | 2 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSY2 |
| `SUSY3` |  | 3 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSY3 |
| `SUSY4` |  | 4 Years Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SUSY4 |


## Historical

Analysts last estimates for previous periods and surprises compared to the Actuals

### Historical EPS Estimate

Historical mean EPS estimate.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EPSEst()` | offset, type |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSEst |
| `HistQ1EPSEst` |  | 1 Quarter Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HistQ1EPSEst |
| `HistQ2EPSEst` |  | 2 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HistQ2EPSEst |
| `HistQ3EPSEst` |  | 3 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HistQ3EPSEst |
| `HistQ4EPSEst` |  | 4 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HistQ4EPSEst |
| `HistQ5EPSEst` |  | 5 Quarters Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=HistQ5EPSEst |


### Historical Estimate Number of Analysts

Historical EPS Estimate Number of Analysts

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EPSHistEstCnt()` | offset, type |  |  |
| `SalesHistEstCnt()` | offset, type |  |  |


### Historical Estimate Standard Deviation

Historical EPS Estimate Standard Deviation

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EPSHistEstSD()` | offset, type |  |  |
| `SalesHistEstSD()` | offset, type |  |  |


### Historical Sales Estimate

Historical Sales Estimate

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SalesEst()` | offset, type |  |  |
| `SalesEstQ1` |  | 1 Quarter Ago |  |
| `SalesEstQ2` |  | 2 Quarters Ago |  |
| `SalesEstQ3` |  | 3 Quarters Ago |  |
| `SalesEstQ4` |  | 4 Quarters Ago |  |
| `SalesEstQ5` |  | 5 Quarters Ago |  |


### Historical EPS Difference

Historical Quarter Difference (Actual - Estimate), 1 Quarter Ago

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `HistQ1Difference` |  | 1 Quarter Ago |  |
| `HistQ2Difference` |  | 2 Quarters Ago |  |
| `HistQ3Difference` |  | 3 Quarters Ago |  |
| `HistQ4Difference` |  | 4 Quarters Ago |  |
| `HistQ5Difference` |  | 5 Quarters Ago |  |


## Recs & Opinions

Analysts average recommendation and long-term growth estimate.

### Long Term EPS Growth

This is the number of analysts who are reporting a long term earnings per share growth rate. If a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsLTGrthRt` |  |  |  |
| `LTGrthMean` |  | Latest |  |
| `LTGrth1WkAgo` |  | Week Ago |  |
| `LTGrth4WkAgo` |  | 4 Weeks Ago |  |
| `LTGrth8WkAgo` |  | 8 Weeks Ago |  |
| `LTGrth13WkAgo` |  | 13 Weeks Ago |  |
| `LTGrthHigh` |  | Latest |  |
| `LTGrthLow` |  | Latest |  |
| `LTGrthStdDev` |  | Latest |  |


### Price Target

Number of analysts giving price target estimates. Note: if a security has no analysts, this factor returns NA, not 0.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `#AnalystsPriceTarget` |  |  |  |
| `PriceTarget4WkAgo` |  |  |  |
| `PriceTargetHi` |  |  |  |
| `PriceTargetLo` |  |  |  |
| `PriceTargetMean` |  |  |  |
| `PriceTargetStdDev` |  |  |  |


### Average Recommendation

Average Recommendation on a 1-3 linear scale, where 1 is a strong buy, 3 a sell. For CapitalIQ the range is 1-5.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `AvgRec` |  | Current | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AvgRec |
| `AvgRec1WkAgo` |  | 1 Week Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AvgRec1WkAgo |
| `AvgRec4WkAgo` |  | 4 Weeks Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AvgRec4WkAgo |
| `AvgRec8WkAgo` |  | 8 Weeks Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AvgRec8WkAgo |
| `AvgRec13WkAgo` |  | 13 Weeks Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AvgRec13WkAgo |


### Recommendation Function

Consensus recommendation

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ConsRec()` | rec_stat [, weekAgo] |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ConsRec |


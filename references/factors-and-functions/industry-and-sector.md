# Industry & Sector

Industry and Sector functions

## Classification

Industry, sector and universe classifications.

### Industry

Which industry the stock belongs to. For example, to screen for stocks in the leisure products industry use: Industry=LEISURE

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Industry` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Industry |


### Industry Code

Industry Code. See Full Description for a complete list of codes

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IndCode` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IndCode |


### Industry Description

See Full Description for a complete list of names

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IndDescr` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IndDescr |


### Revere Industry Classification (RBICS)

Evaluates to TRUE if any combination of RBICS Sector, Sub-sector, Industry, and Sub-industry matches.

For example, RBICS(25, 401515) returns stocks in *either* Sector ENERGY or Industry DELIVERY. You can also use our mnemonics: RBICS(ENERGY, DELIVERY)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RBICS()` | rcode, rcode, rcode, ... |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RBICS |


### Sector

Which sector the stock belongs to. For example, to screen for stocks in the technology sector use: Sector=TECH

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Sector` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Sector |


### Sector Code

Sector Code. See Full Description for a complete list of codes

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SectorCode` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SectorCode |


### Sector Description

Sector Description. See Full Description for a complete list of names

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SectorDescr` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SectorDescr |


### SubIndustry

Which sub-industry the stock belongs to. For example, to screen for stocks in the diversified REITs sub-industry use: SubIndustry=REITDIV

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubIndustry` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubIndustry |


### SubIndustry Code

See Full Description for a complete list of codes

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubIndCode` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubIndCode |


### SubIndustry Description

See Full Description for a complete list of names

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubIndDescr` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubIndDescr |


### SubSector

Which sub-sector the stock belongs to.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubSector` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSector |


### SubSector Code

SubSector Code. See Full Description for a complete list of codes

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubSectorCode` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSectorCode |


### SubSector Description

SubSector Description. See Full Description for a complete list of names

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SubSectorDescr` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SubSectorDescr |


## Ind Aggregate Factors

Contains precalculated industry factors. The factors that end with Ind are calculated using the Aggregate cross-sectional function. See Full description for more details

### Descriptive

Number of constituents in a given industry.

#### Number of Constituents

Number of constituents in the industry

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NoConst` |  |  |  |


### Dividend

Aggregated dividend yield.

#### Yield, Industry

Dividend Yield Industry, 5 Year Average (%)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Yield5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Yield5YAvgInd |
| `YieldInd` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=YieldInd |


### Efficiency

Aggregated turnover and per-employee ratios.

#### Asset Turnover, Industry

Asset Turnover Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `AstTurnTTMInd` |  | Trailing Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=AstTurnTTMInd |


#### Income per Employee, Industry

Income Per Employee Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IncPerEmpTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IncPerEmpTTMInd |


#### Inventory Turnover, Industry

Inventory Turnover Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `InvTurnTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=InvTurnTTMInd |


#### Receivable Turnover, Industry

Receivables Turnover Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `RecTurnTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=RecTurnTTMInd |


#### Sales per Employee, Industry

Sales Per Employee Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `SalesPerEmpTTMInd` |  | Trailing Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesPerEmpTTMInd |


### Estimates

Aggregated mean estimate revisions for industries.

#### Estimate Revision Direction

Ratio ranging from -1 to +1 indicating the direction of revisions for the stock's industry. The extreme values 1 and -1 would indicate that every analyst's CurrY estimate in the industry have been revised upward and downward respectively in the past 4 Weeks.

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CurrYRevRatio4W` |  | Current Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CurrYRevRatio4W |
| `NextYRevRatio4W` |  | Next Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NextYRevRatio4W |


### Financial Strength

Aggregated ratios relating to quality, including payout and debt ratios.

#### Current Ratio, Industry

Current Ratio Industry, Quarterly

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CurRatioQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CurRatioQInd |


#### Interest Coverage, Industry

Interest Coverage Industry, TTM


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `IntCovTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=IntCovTTMInd |


#### Long Term Debt To Total Equity, Industry

Long Term Debt To Total Equity Industry, Quarterly

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `DbtLT2EqQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DbtLT2EqQInd |


#### Payout Ratio, Industry

Payout Ratio Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PayRatio5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PayRatio5YAvgInd |
| `PayRatio5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PayRatio5YInd |
| `PayRatioTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PayRatioTTMInd |


#### Quick Ratio, Industry

Quick Ratio Industry, Quarterly

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `QuickRatioQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=QuickRatioQInd |


#### Retention Rate, Industry

Retention Rate Industry, TTM (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Retn%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Retn%TTMInd |


#### Total Debt To Total Equity, Industry

Total Debt To Total Equity Industry, Quarterly

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `DbtTot2EqQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=DbtTot2EqQInd |


### Growth Rates

Aggregated industrial growth rates.

#### Industry Growth

Capital Spending Industry, 5 Year Growth Rate (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `CapSp5YCGr%Ind` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=CapSp5YCGr%Ind |
| `Div%ChgAInd` |  | Latest Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Div%ChgAInd |
| `Div3YCGr%Ind` |  | 3 Years |  |
| `Div5YCGr%Ind` |  | 5 Years |  |
| `EPSExclXorGr%3YInd` |  | 3 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSExclXorGr%3YInd |
| `EPSExclXorGr%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSExclXorGr%5YInd |
| `EPSExclXorGr%AInd` |  | Latest Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSExclXorGr%AInd |
| `EPSExclXorGr%PYQInd` |  | Latest Quarter vs 1 Year Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSExclXorGr%PYQInd |
| `EPSExclXorGr%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EPSExclXorGr%TTMInd |
| `SalesGr%3YInd` |  | 3 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesGr%3YInd |
| `SalesGr%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesGr%5YInd |
| `SalesGr%AInd` |  | Latest Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesGr%AInd |
| `SalesGr%PYQInd` |  | Latest Quarter vs 1 Year Ago | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesGr%PYQInd |
| `SalesGr%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=SalesGr%TTMInd |


### Institutional Ownership

Aggregated per industry institutional ownership rates.

#### Institutional % Owned, Industry

Institutional Percent Owned Industry, (%) average

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Inst%OwnInd` |  |  | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Inst%OwnInd |


### Price & Volume

Aggregated industrial price changes.

#### Price Percent Change, Industry

13 Week Price Percent Change Industry (%)

NOTE: See Full Description for important information

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr13W%ChgInd` |  | 13 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr13W%ChgInd |
| `Pr26W%ChgInd` |  | 26 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr26W%ChgInd |
| `Pr4W%ChgInd` |  | 4 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr4W%ChgInd |
| `Pr52W%ChgInd` |  | 52 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr52W%ChgInd |


#### Relative Price Percent Change, Industry

Relative Price Percent Change Industry, 13 Weeks (%)

NOTE: Not the same as our Industry & Sector which is cap-weighted

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr13WRel%ChgInd` |  | 13 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr13WRel%ChgInd |
| `Pr26WRel%ChgInd` |  | 26 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr26WRel%ChgInd |
| `Pr4WRel%ChgInd` |  | 4 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr4WRel%ChgInd |
| `Pr52WRel%ChgInd` |  | 52 Weeks | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr52WRel%ChgInd |


### Profitability

Aggregated margins and management efficiency ratios.

#### EBITDA Margin, Industry

EBITDA Margin Industry, 5 year average (%)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `EBITDAMgn%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAMgn%5YAvgInd |
| `EBITDAMgn%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=EBITDAMgn%5YInd |


#### Gross Profit Margin, Industry

Gross Margin Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `GMgn%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GMgn%5YAvgInd |
| `GMgn%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GMgn%5YInd |
| `GMgn%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=GMgn%TTMInd |


#### Net Profit Margin, Industry

Net Profit Margin Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `NPMgn%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NPMgn%5YAvgInd |
| `NPMgn%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NPMgn%5YInd |
| `NPMgn%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=NPMgn%TTMInd |


#### Pretax Margin, Industry

Pretax Margin Industry, 5 Year Average (%)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PTMgn%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PTMgn%5YAvgInd |
| `PTMgn%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PTMgn%5YInd |
| `PTMgn%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PTMgn%TTMInd |


#### Return On Assets, Industry

Return on Average Assets Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ROA%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROA%5YAvgInd |
| `ROA%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROA%TTMInd |


#### Return On Equity, Industry

Return on Average Common Equity Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ROE%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROE%5YAvgInd |
| `ROE%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROE%TTMInd |


#### Return On Investment, Industry

Return on Investment Industry, 5 Year Average (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ROI%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROI%5YAvgInd |
| `ROI%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ROI%TTMInd |


#### Tax Rate, Industry

Tax Rate Industry, Effective, TTM (%)


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `TaxRate%TTMInd` |  | Trailing Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=TaxRate%TTMInd |


#### Operating Margin, Industry

Operating Margin Industry, TTM (%)

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `OpMgn%TTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OpMgn%TTMInd |
| `OpMgn%5YAvgInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OpMgn%5YAvgInd |
| `OpMgn%5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=OpMgn%5YInd |


### Valuation

Per industry aggregates of prices to fundamental line items.

#### Price To Book, Industry

Price to Book Ratio Industry, Quarterly


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr2BookQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2BookQInd |


#### Price To Cash Flow, Industry

Price to Cash Flow Per Share Ratio Industry, TTM

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr2CashFlTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2CashFlTTMInd |


#### Price To Earnings (PE), Industry

Price To Earnings Ratio Industry, Excluding Extraordinary Items, TTM

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PEExclXorTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PEExclXorTTMInd |
| `PEHighInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PEHighInd |
| `PELowInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PELowInd |


#### Price To Free Cash Flow, Industry

Price To Free Cash Flow Per Share Ratio Industry, TTM

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr2FrCashFlTTMInd` |  | Trailing 12 Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2FrCashFlTTMInd |


#### Price To Sales, Industry

Price To Sales Next Twelve Months

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr2SalesNTMInd` |  | Trailing Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2SalesNTMInd |
| `Pr2SalesTTMInd` |  | Trailing Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2SalesTTMInd |


#### Price To Tangible Book, Industry

Price to Tangible Book Ratio Industry, Quarterly


| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Pr2TanBkQInd` |  | Latest Quarter | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Pr2TanBkQInd |


### Valuation Projected

#### PEG Ratio, Industry

Projected Price/Earnings to Long Term Growth Rate Industry

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `PEGLTInd` |  | Long Term Growth | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PEGLTInd |
| `PEGSTInd` |  | Next Year Growth | https://www.portfolio123.com/doc/doc_detail.jsp?factor=PEGSTInd |


#### Price To Earnings (PE) Projected, Industry

Next Year Projected P/E Ratio Industry

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `ProjPENextFYInd` |  | Next Fiscal Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ProjPENextFYInd |
| `ProjPENTMInd` |  | Next Twelve Months | https://www.portfolio123.com/doc/doc_detail.jsp?factor=ProjPENTMInd |


### Volatility

Aggregated betas per industry.

#### Beta, Industry

Beta1Y for the industry

| Factor | Params | Variant | Full Description |
|--------|--------|---------|------------------|
| `Beta1YInd` |  | 1 Year | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Beta1YInd |
| `Beta3YInd` |  | 3 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Beta3YInd |
| `Beta5YInd` |  | 5 Years | https://www.portfolio123.com/doc/doc_detail.jsp?factor=Beta5YInd |


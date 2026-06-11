# Industry & Sector — Portfolio123 Reference

Industry & Sector covers stock classification under the Revere Industry
Classification (RBICS) hierarchy — sector, sub-sector, industry, and
sub-industry — plus a large set of industry-aggregate factors that report a
ratio or growth rate averaged across the stock's industry. For ETF
classification vocabularies see [taxonomy.md](taxonomy.md); to restrict a
universe to specific RBICS codes see [universe-filters.md](universe-filters.md).

Coverage: 1 function / 91 factors — extracted from the official Factor Reference
on 2026-06-09. The Classification factors' full code lists live on detail pages
that require a Portfolio123 subscription to view (see
`build/data/details-skipped.json`), so those factors are documented from the
dictionary fields (name, description, examples embedded in the short
description) only. The RBICS function detail page is likewise subscription-gated;
its entry below is built from the dictionary fields.

## Contents

- [Classification](#classification)
- [Ind Aggregate Factors](#ind-aggregate-factors)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Classification

### Functions

#### `RBICS(rcode, rcode, rcode, ...)`
Evaluates to true if any combination of RBICS sector, sub-sector, industry, and
sub-industry matches one of the codes passed. You can pass numeric RBICS codes or
the supported mnemonics.

```p123
RBICS(25, 401515)
```

The example above returns stocks in *either* the sector with code 25 or the
industry with code 401515. (The full code list and mnemonics are on the
subscription-gated detail page.)

### Factors

These factors return a stock's RBICS classification. The string factors
(`Industry`, `Sector`, `SubIndustry`, `SubSector`) compare against classification
codes; the `...Code` factors return the numeric code and the `...Descr` factors
return the descriptive name. The complete code/name lists are on the
subscription-gated detail pages.

| Factor | Description | Period |
|---|---|---|
| `Sector` | Which sector the stock belongs to. Example: to screen the technology sector use Sector = TECH. |  |
| `SectorCode` | Sector code (numeric). See the subscription-gated detail page for the complete list of codes. |  |
| `SectorDescr` | Sector description (name). See the subscription-gated detail page for the complete list of names. |  |
| `SubSector` | Which sub-sector the stock belongs to. |  |
| `SubSectorCode` | Sub-sector code (numeric). See the subscription-gated detail page for the complete list of codes. |  |
| `SubSectorDescr` | Sub-sector description (name). See the subscription-gated detail page for the complete list of names. |  |
| `Industry` | Which industry the stock belongs to. Example: to screen the leisure products industry use Industry = LEISURE. |  |
| `IndCode` | Industry code (numeric). See the subscription-gated detail page for the complete list of codes. |  |
| `IndDescr` | Industry description (name). See the subscription-gated detail page for the complete list of names. |  |
| `SubIndustry` | Which sub-industry the stock belongs to. Example: to screen the diversified REITs sub-industry use SubIndustry = REITDIV. |  |
| `SubIndCode` | Sub-industry code (numeric). See the subscription-gated detail page for the complete list of codes. |  |
| `SubIndDescr` | Sub-industry description (name). See the subscription-gated detail page for the complete list of names. |  |

## Ind Aggregate Factors

Each factor reports a metric averaged across the stock's industry. The factor
names end in the "Ind" suffix (industry). Grouped below by the official
sub-group.

### Descriptive

| Factor | Description | Period |
|---|---|---|
| `NoConst` | Number of constituents in the industry |  |

### Dividend

| Factor | Description | Period |
|---|---|---|
| `Yield5YAvgInd` | Dividend Yield Industry, 5 Year Average (%) | 5 Years |
| `YieldInd` | Dividend Yield Industry (%) |  |

### Efficiency

| Factor | Description | Period |
|---|---|---|
| `AstTurnTTMInd` | Asset Turnover Industry, TTM | Trailing Twelve Months |
| `IncPerEmpTTMInd` | Income Per Employee Industry, TTM | Trailing 12 Months |
| `InvTurnTTMInd` | Inventory Turnover Industry, TTM | Trailing 12 Months |
| `RecTurnTTMInd` | Receivables Turnover Industry, TTM | Trailing 12 Months |
| `SalesPerEmpTTMInd` | Sales Per Employee Industry, TTM | Trailing Twelve Months |

### Estimates

| Factor | Description | Period |
|---|---|---|
| `CurrYRevRatio4W` | Ratio ranging from -1 to +1 indicating the direction of revisions for the stock's industry. The extreme values 1 and -1 would indicate that every analyst's CurrY estimate in the industry have been revised upward and downward respectively in the past 4 Weeks. | Current Year |
| `NextYRevRatio4W` | Ratio ranging from -1 to +1 indicating the direction of revisions for the stock's industry. The extreme values 1 and -1 would indicate that every analyst's NextY estimate in the industry have been revised upward and downward respectively in the past 4 Weeks. | Next Year |

### Financial Strength

| Factor | Description | Period |
|---|---|---|
| `CurRatioQInd` | Current Ratio Industry, Quarterly | Latest Quarter |
| `IntCovTTMInd` | Interest Coverage Industry, TTM | Trailing 12 Months |
| `DbtLT2EqQInd` | Long Term Debt To Total Equity Industry, Quarterly | Latest Quarter |
| `PayRatio5YAvgInd` | Payout Ratio Industry, 5 Year Average (%) | 5 Years |
| `PayRatio5YInd` | Payout Ratio Industry, 5 Year (%) | 5 Years |
| `PayRatioTTMInd` | Payout Ratio Industry, TTM (%) | Trailing 12 Months |
| `QuickRatioQInd` | Quick Ratio Industry, Quarterly | Latest Quarter |
| `Retn%TTMInd` | Retention Rate Industry, TTM (%) | Trailing 12 Months |
| `DbtTot2EqQInd` | Total Debt To Total Equity Industry, Quarterly | Latest Quarter |

### Growth Rates

| Factor | Description | Period |
|---|---|---|
| `CapSp5YCGr%Ind` | Capital Spending Industry, 5 Year Growth Rate (%) | 5 Years |
| `Div%ChgAInd` | Dividend Percent Change Industry, Year Over Year (%) | Latest Year |
| `Div3YCGr%Ind` | Dividend Growth Rate Industry, 3 Years (uses corporate action data) | 3 Years |
| `Div5YCGr%Ind` | Dividend Industry, 5 Year Growth Rate (uses corporate action data) | 5 Years |
| `EPSExclXorGr%3YInd` | EPS Growth Rate Industry, 3 Years (%) | 3 Years |
| `EPSExclXorGr%5YInd` | Earnings Per Share Industry, 5 Year Growth Rate (%) | 5 Years |
| `EPSExclXorGr%AInd` | EPS Percent Change Industry, Year Over Year (%) | Latest Year |
| `EPSExclXorGr%PYQInd` | EPS Percent Change Industry, Most Recent Quarter vs. Quarter 1 Year Ago (%) | Latest Quarter vs 1 Year Ago |
| `EPSExclXorGr%TTMInd` | EPS Percent Change Industry, TTM Over TTM (%) | Trailing 12 Months |
| `SalesGr%3YInd` | Sales Growth Rate Industry, 3 Years (%) | 3 Years |
| `SalesGr%5YInd` | Sales Industry, 5 Year Growth Rate (%) | 5 Years |
| `SalesGr%AInd` | Sales percent change for the industry, recent Y vs prior Y | Latest Year |
| `SalesGr%PYQInd` | Sales percent change for the industry, recent Q vs Q 1 year ago | Latest Quarter vs 1 Year Ago |
| `SalesGr%TTMInd` | Sales percent change for the industry, recent TTM vs prior TTM | Trailing 12 Months |

### Institutional Ownership

| Factor | Description | Period |
|---|---|---|
| `Inst%OwnInd` | Institutional Percent Owned Industry, (%) average |  |

### Price & Volume

| Factor | Description | Period |
|---|---|---|
| `Pr13W%ChgInd` | 13 Week Price Percent Change Industry (%)  NOTE: See Full Description for important information | 13 Weeks |
| `Pr26W%ChgInd` | 26 Week Price Percent Change Industry (%)  NOTE: See Full Description for important information | 26 Weeks |
| `Pr4W%ChgInd` | 4 Week Price Percent Change Industry (%)  NOTE: See Full Description for important information | 4 Weeks |
| `Pr52W%ChgInd` | 52 Week Price Percent Change Industry (%)  NOTE: See Full Description for important information | 52 Weeks |
| `Pr13WRel%ChgInd` | Relative Price Percent Change Industry, 13 Weeks (%)  NOTE: Not the same as our Industry & Sector which is cap-weighted | 13 Weeks |
| `Pr26WRel%ChgInd` | Relative Price Percent Change Industry, 26 Weeks (%)  NOTE: Not the same as our Industry & Sector which is cap-weighted | 26 Weeks |
| `Pr4WRel%ChgInd` | Relative Price Percent Change Industry, 4 Weeks (%)  NOTE: Not the same as our Industry & Sector which is cap-weighted | 4 Weeks |
| `Pr52WRel%ChgInd` | Relative Price Percent Change Industry, 52 Weeks (%)  NOTE: Not the same as our Industry & Sector which is cap-weighted | 52 Weeks |

### Profitability

| Factor | Description | Period |
|---|---|---|
| `EBITDAMgn%5YAvgInd` | EBITDA Margin Industry, 5 year average (%) | 5 Years |
| `EBITDAMgn%5YInd` | EBITDA Margin Industry, 5 year (%) | 5 Years |
| `GMgn%5YAvgInd` | Gross Margin Industry, 5 Year Average (%) | 5 Years |
| `GMgn%5YInd` | Gross Profit Margin Industry, 5 year (%) | 5 Years |
| `GMgn%TTMInd` | Gross Margin Industry, TTM (%) | Trailing 12 Months |
| `NPMgn%5YAvgInd` | Net Profit Margin Industry, 5 Year Average (%) | 5 Years |
| `NPMgn%5YInd` | Net Profit Margin Industry, 5 year (%) | 5 Years |
| `NPMgn%TTMInd` | Net Profit Margin Industry, TTM (%) | Trailing 12 Months |
| `PTMgn%5YAvgInd` | Pretax Margin Industry, 5 Year Average (%) | 5 Years |
| `PTMgn%5YInd` | Pretax Margin Industry, 5 year (%) | 5 Years |
| `PTMgn%TTMInd` | Pretax Margin Industry, TTM (%) | Trailing 12 Months |
| `ROA%5YAvgInd` | Return on Average Assets Industry, 5 Year Average (%) | 5 Years |
| `ROA%TTMInd` | Return on Assets Industry, TTM (%) | Trailing 12 Months |
| `ROE%5YAvgInd` | Return on Average Common Equity Industry, 5 Year Average (%) | 5 Years |
| `ROE%TTMInd` | Return on Average Common Equity Industry, TTM (%) | Trailing 12 Months |
| `ROI%5YAvgInd` | Return on Investment Industry, 5 Year Average (%) | 5 Years |
| `ROI%TTMInd` | Return on Investment Industry, TTM (%) | Trailing 12 Months |
| `TaxRate%TTMInd` | Tax Rate Industry, Effective, TTM (%) | Trailing Twelve Months |
| `OpMgn%TTMInd` | Operating Margin Industry, TTM (%) | Trailing 12 Months |
| `OpMgn%5YAvgInd` | Operating Margin Industry, 5 Year Average (%) | 5 Years |
| `OpMgn%5YInd` | Operating Margin Industry, 5 year (%) | 5 Years |

### Valuation

| Factor | Description | Period |
|---|---|---|
| `Pr2BookQInd` | Price to Book Ratio Industry, Quarterly | Latest Quarter |
| `Pr2CashFlTTMInd` | Price to Cash Flow Per Share Ratio Industry, TTM | Trailing 12 Months |
| `PEExclXorTTMInd` | Price To Earnings Ratio Industry, Excluding Extraordinary Items, TTM | Trailing 12 Months |
| `PEHighInd` | Price Earnings Ratio Industry, 5 year High | 5 Years |
| `PELowInd` | Price Earnings Ratio Industry, 5 year Low | 5 Years |
| `Pr2FrCashFlTTMInd` | Price To Free Cash Flow Per Share Ratio Industry, TTM | Trailing 12 Months |
| `Pr2SalesNTMInd` | Price To Sales Next Twelve Months | Trailing Twelve Months |
| `Pr2SalesTTMInd` | Price to Sales Ratio Industry, TTM | Trailing Twelve Months |
| `Pr2TanBkQInd` | Price to Tangible Book Ratio Industry, Quarterly | Latest Quarter |

### Valuation Projected

| Factor | Description | Period |
|---|---|---|
| `PEGLTInd` | Projected Price/Earnings to Long Term Growth Rate Industry | Long Term Growth |
| `PEGSTInd` | Price/Earnings to Next Year Growth Rate Industry | Next Year Growth |
| `ProjPENextFYInd` | Next Year Projected P/E Ratio Industry | Next Fiscal Year |
| `ProjPENTMInd` | Next Twelve Months Projected P/E Ratio Industry | Next Twelve Months |

### Volatility

| Factor | Description | Period |
|---|---|---|
| `Beta1YInd` | Beta1Y for the industry | 1 Year |
| `Beta3YInd` | Beta3Y for the industry | 3 Years |
| `Beta5YInd` | Beta5Y for the industry | 5 Years |

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `IndustryCode` | `IndCode` | The industry code factor is abbreviated `IndCode` (sector is `SectorCode`). |
| `GICS` | `RBICS` | Portfolio123 classifies stocks with RBICS, exposed via the `RBICS(...)` function and the classification factors. |
| `SectorName` | `SectorDescr` | The descriptive sector name factor is `SectorDescr`; `Sector` returns the code string. |

## See Also

- [taxonomy.md](taxonomy.md) — ETF classification vocabularies (asset class, region, sector, ...).
- [universe-filters.md](universe-filters.md) — `UnivRBICS` to restrict a universe to RBICS codes.
- [ratios-statistics.md](ratios-statistics.md) — the per-stock counterparts of the industry-aggregate ratios.

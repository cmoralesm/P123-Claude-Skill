# Ratios & Statistics - Portfolio123 Reference

<!-- name-whitelist: NAHandling -->

Computed ratios, valuation multiples, margins, per-share figures, efficiency and financial-strength statistics, and the advanced scoring models (Altman Z, Beneish M, Piotroski F). Raw filing line items live in [Financials](financials.md); the underlying formula language and operators are in [Technical](technical.md) and [Advanced Functions](advanced-functions.md). Analyst-estimate ratios are in [Estimates](estimates.md).

Coverage: **60 functions / 1,206 factors** - extracted from the official Factor Reference on 2026-06-09.

## Line-item function conventions

Most ratio functions in this category share the same calling convention. Unless an entry says otherwise:

| Parameter | Description |
|---|---|
| `offset` | Period offset: `0` is the most recent period, `1` the previous one, and so on (0-24 for interim, 0-19 for annual). |
| `type` | `QTR` (quarterly), `ANN` (annual), or `TTM` (trailing twelve months). For income and cash-flow values, TTM sums four quarters; for balance-sheet values, TTM averages the trailing four quarters. |
| `NAHandling` | Optional, controls preliminary-report N/A handling for the most recent period: `FALLBACK` (default - fall back to the prior period), `KEEPNA`, or `ZERONA`. |

Each function also has prebuilt factor variants (a base code plus a period suffix such as Q, PQ, TTM, A, or PY); those are listed in the factor tables under each subcategory. Quarterly values from income and cash-flow statements are annualized so they compare with 12-month figures.

## Contents

- [Valuation](#valuation)
- [Valuation Projected](#valuation-projected)
- [Yield](#yield)
- [Margins](#margins)
- [Profitability](#profitability)
- [Per Share Ratios](#per-share-ratios)
- [Efficiency](#efficiency)
- [Financial Strength](#financial-strength)
- [Other](#other)
- [Advanced](#advanced)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Valuation

### Functions

#### `EV2EBITDA(offset, type)`

The EV2EBITDA ratio compares the value of a company, debt and cash included, to the company's operating income plus depreciation and amortization.

Thanks to a normalization of financial structure and weight of non cash expenses, EV2EBITDA is less variable than PE and it is better suited to compare stocks from different sectors and industries. 

The lower the EV2EBITDA, the cheaper the valuation for a company. Another way to look at this ratio is how much cash can the company generate without reinvesting in hard assets.

Formula

`EV2EBITDA = EV / EBITDA`


#### `EV2Sales(offset, type)`

Enterprise value-to-sales compares the enterprise value of a company to its annual sales. The EV/sales multiple gives investors a quantifiable metric of how to value a company based on its sales, while taking account of both the company's equity and debt.

This ratio can be used for spotting recovery situations or for checking that a growth stock has not become overvalued. It comes in handy when a company begins to suffer losses and, as a result, has no earnings with which investors can assess the shares.

Enterprise value-to-sales is an expansion of the price-to-sales valuation, which uses market capitalization instead of enterprise value. It is perceived to be more accurate than P/S because the market capitalization alone does not take a company's debt and cash into account when valuing the company, while enterprise value does.

We don't recommend using EV ratios for financial companies, especially banks, because the nature of their balance sheet significantly distorts the enterprise value calculated with the standard definition.

Formula

`EV2Sales = EV / Sales`


#### `Pr2Book(offset, type)`

The price to book reflects the value that market participants attach to a company's equity relative to the book value of its equity. A stock's market value is a forward-looking metric that reflects a company's future cash flows. The book value of equity is an accounting measure based on the historic cost principle and reflects past issuances of equity, augmented by any profits or losses, and reduced by dividends and share buybacks.

The price to book value is the share Price divided by the book value per share. The BVPS is calculated as follows: (Common Equity less Intangibles divided by the Fully Diluted Shares Outstanding at the end of the period. Market value per share is obtained by simply looking at the share price quote in the market.

A lower P/B ratio could mean the stock is undervalued. However, it could also mean something is fundamentally wrong with the company. As with most ratios, this varies by industry. Another way to look at P/B ratio is the premium that would remain if the company went bankrupt immediately (for example, a 1.6 book value implies a 60% premium).

Formula

Price / BVPS


#### `Pr2CashFl(offset, type)`

The price-to-cash flow ratio measures the value of a stock's price relative to its cash flow per share. The ratio uses a definition of cash flow which adds back to net income before extraordinary items the main non-cash expenses: depreciation and amortization. It is especially useful for valuing stocks that have positive cash flow but are not profitable because of large non-cash charges.

The price-to-cash flow ratio measures how much cash a company generates relative to its stock price, rather than what it records in earnings relative to its stock price, as measured by the price-earnings ratio. The price-to-cash flow ratio is said to be a better investment valuation indicator than the price-earnings ratio, because cash flows cannot be manipulated as easily as earnings, which are affected by depreciation and other non-cash items. Some companies appear unprofitable because of large, non-cash expenses even though they have positive cash flows.


#### `Pr2CFInclRD(offset, type)`

Price-to-innovation-adjusted cash flow is a variation of the price-to-cash-flow ratio that takes a company's level of spending on research and development into account. Price-to-innovation-adjusted cash flow is calculated by adding any expenditure on R&D back into operating cash flow and then calculating the PCF ratio for that company.

Accounting standards require that R&D costs are categorized as expenses, which can diminish the book value of innovative companies in industries such as software development and biotech. R&D expenditures do not necessarily guarantee future innovative success, but R&D spending is regarded as a crucial part of innovation and technological advancement.

The price-to-innovation-adjusted cash flow calculation is extremely useful when evaluating company performance in industries such as software development, pharmaceuticals, and computers. In fact, some technology companies reinvest a significant portion of generated cash back into R&D, because they consider it as an investment in their continued growth. Heavy expenditures on R&D shows that a company is willing to take risks to further its growth. 

Note: R&D has a fallback to previous period during preliminary. If NA after the fallback, or NA for TTM & Q with complete data then fallback to the closest annual


#### `PEExclXor(offset, type)`

The price-to-earnings ratio measures a company's current share price relative to its per-share earnings. This definition excludes extraordinary items from EPS calculation.

The PE ratio is among the oldest and most used ratios in finance. Its importance is crucial in the dividend discount model, which states that the current price is the sum of all the discounted future cash flows. In its simplest form:

P = D/(r-g)

With P today stock price, r discount rate and g constant dividend growth.

Because not many companies pay a substantial dividend and dividends cannot be sustainably higher than earnings, the latter is used as a proxy for dividends.

A relatively low PE ratio shows what the market is discounting poor future earnings growth, while a high PE means that the market is discounting high future earnings growth.

Because this factor is heavily influenced by the company leverage, operational risk and profitability, it is best suited to compare stocks of the same industry.

Formula

`PEExclXor = Price / EPSExclXor`

If EPS is negative it returns NA


#### `PEInclXor(offset, type)`

The price-to-earnings ratio measures a company's current share price relative to its per-share earnings. This definition includes extraordinary items from EPS calculation.

The PE ratio is among the oldest and most used ratios in finance. Its importance is crucial in the dividend discount model, which states that the current price is the sum of all the discounted future cash flows. In its simplest form:

P = D/(r-g)

With P today stock price, r discount rate and g constant dividend growth.

Because not many companies pay a substantial dividend and dividends cannot be sustainably higher than earnings, the latter is often used as a proxy for dividends.

A relatively low PE ratio shows what the market is discounting poor future earnings growth, while a high PE means that the market is discounting high future earnings growth.

Because this factor is heavily influenced by the company's leverage, operational risk and profitability, it is best suited to compare stocks of the same industry.

Formula

`PEInclXor = Price / EPSInclXor`

If EPS is negative it returns NA


#### `PEInclRD(offset, type)`

Price-to-innovation-adjusted earnings is a variation of the price-to-earnings ratio that takes a company's level of spending on research and development into account. Price-to-innovation-adjusted earnings is calculated by adding any expenditure on R&D back into earnings and then calculating the PE ratio for that company.

Accounting standards require that R&D costs are categorized as expenses, which can diminish the book value of innovative companies in industries such as software development and biotech. R&D expenditures do not necessarily guarantee future innovative success, but R&D spending is regarded as a crucial part of innovation and technological advancement.

The price-to-innovation-adjusted earnings calculation is extremely useful when evaluating company performance in industries such as software development, pharmaceuticals, and computers. In fact, some technology companies reinvest a significant portion of profits back into R&D, because they consider it as an investment in their continued growth. Heavy expenditures on R&D shows that a company is willing to take risks to further its growth.

Note: R&D has a fallback to previous period during preliminary. If NA after the fallback, or NA for TTM & Q with complete data then fallback to the closest annual

Formula

`PEInclRD = Price / (EPSExclXor + RandDPS)`

If negative EPS it returns NA


#### `Pr2FrCashFl(offset, type)`

Price to free cash flow compares a company's per-share market price to its per-share amount of free cash flow. This metric is very similar to the valuation metric of price to cash flow but is considered more exact, owing to the fact that it uses free cash flow, which subtracts capital expenditures (CAPEX) from a company's total operating cash flow, thereby reflecting the actual cash flow available to fund non-asset-related growth. Companies use this metric when they need to expand their asset bases either in order to grow their businesses or simply to maintain acceptable levels of free cash flow.

The price to free cash flow ratio measures how much cash a company generates relative to its stock price, rather than what it records in earnings relative to its stock price, as measured by the price-earnings ratio. The price to free cash flow ratio is said to be a better investment valuation indicator than the price-earnings ratio, because cash flows cannot be manipulated as easily as earnings, which are affected by depreciation and other non-cash items. Some companies appear unprofitable because of large, non-cash expenses even though they have positive free cash flows.


#### `Pr2NetFrCashFl(offset, type)`

Price to free cash flow compares a company's per-share market price to its per-share amount of net free cash flow. This metric is very similar to the valuation metric of price to cash flow but is considered more exact, owing to the fact that it uses free cash flow, which subtracts capital expenditures (CAPEX) from a company's total operating cash flow, thereby reflecting the actual cash flow available to fund non-asset-related growth. Companies use this metric when they need to expand their asset bases either in order to grow their businesses or simply to maintain acceptable levels of free cash flow. This particular version of the ratio also subtracts dividends.

The price to free cash flow ratio measures how much cash a company generates relative to its stock price, rather than what it records in earnings relative to its stock price, as measured by the price-earnings ratio. The price to free cash flow ratio is said to be a better investment valuation indicator than the price-earnings ratio, because cash flows cannot be manipulated as easily as earnings, which are affected by depreciation and other non-cash items. Some companies appear unprofitable because of large, non-cash expenses even though they have positive free cash flows.


#### `Pr2Sales(offset, type)`

The price-to-sales ratio compares a company's stock price to its revenues. It shows what the market is willing to pay today for a stock based on its past or future sales.

The P/S ratio is calculated by dividing the company's fully diluted market capitalization by its total sales.

The ratio was first proposed in the 1980s as a way to evaluate high-growth-potential, high-R&D companies and has been widely used for such companies ever since then. These companies often have no positive earnings, so one can use P/S instead of P/E.

The PS ratio helps investors determine the market value of a stock as compared to the revenues. A high PS without significant Sales Growth could mean that a stock's price is high relative to sales and possibly overvalued. Conversely, a low PS with high Sales Growth might indicate that the current stock price is low.

Formula

`Pr2Sales = (SharesFD * Price) / Sales`


#### `Pr2TanBk(offset, type)`

The price to tangible book compares the price of a security to its hard, or tangible, book value as reported in the company's balance sheet. It is calculated as the Current Price divided by the latest quarterly Tangible Book Value Per Share. Tangible Book Value Per Share is defined as Common Equity less Intangibles divided by the Shares Outstanding at the end of the fiscal quarter. 

The price to tangible book value is the share Price divided by the tangible book value per share. The TBVPS is calculated as follows: Common Equity less Intangibles divided by the Fully Diluted Shares Outstanding at the end of the period. 

In theory, a stock's tangible book value per share represents the amount of money an investor would receive for each share if a company were to cease operations and liquidate all of its assets at the value recorded on the company's accounting books. As a rule of thumb, stocks that trade at higher price-to-tangible book value ratios have the potential to leave investors with greater share price losses than those that trade at lower ratios, since the tangible book value per share can reasonably be viewed as the lowest price at which a stock could trade.

Pr2TanBk is applicable mainly to financial and capital-intensive companies that own a relatively high proportion of hard assets and credit, as opposed to firms that engage in light manufacturing or service-oriented industries. For instance, Pr2TanBk is rather meaningless as a valuation measure in the technology sector, because much of a company's valuation derives from intellectual property, an intangible asset. An investor must also be careful with Pr2TanBk for companies that have long-held land: the land is stated at historical cost, not marked up each year on the balance sheet; and Pr2TanBk can result in a deceivingly high ratio.

Formula

Price / TanBVPS


#### `NAVAvg(bars [, offset])`

Monthly NAV average.  bars: 2-12 offset: 0-12


#### `NAVHist(offset)`

Historical monthly NAV.  offset: 0-12


#### `NAVDiscAvg(bars [, offset])`

Monthly NAV Discount average.  bars: 2-12 offset: 0-12


#### `NAVDiscHist(offset)`

Historical monthly NAV Discount.  offset: 0-12


### Factors with detailed definitions

#### `PEHigh`

The P/E Ratio for each of the past 60 months is calculated using the month end Price divided by the trailing twelve month Earnings Per Share (EPS) Excluding Extraordinary Items ending at least 1 month earlier than the pricing date. The highest of these 60 P/E values is the 5 Year High Price Earnings Ratio.

NOTE: If a trailing twelve month EPS value is less than or equal to zero, the corresponding month's P/E ratios are assigned an NA value. If there are less than 40 positive P/E values, then the 5 Year High P/E is assigned an NA.

*Period: 5 Years*


#### `PELow`

The P/E Ratio for each of the past 60 months is calculated using the month end Price divided by the trailing twelve month Earnings Per Share (EPS) Excluding Extraordinary Items ending at least 1 month earlier than the pricing date. The lowest of these 60 P/E values is the 5 Year Low Price Earnings Ratio.

NOTE: If a trailing twelve month EPS value is less than or equal to zero, the corresponding month's P/E ratios are assigned an NA value. If there are less than 40 positive P/E values, then the 5 Year Low P/E is assigned an NA.

*Period: 5 Years*


#### `PERelative`

PERelative is the position of the current PE on a line with the current PEHigh at one end and the PELow at the other end. It is expressed as a percentage, with PEHigh at 100 and PELow at 0.

If the current PE equals PEHigh, then PERelative equals 100. If the current PE equals PELow, then PERelative equals 0. If PEHigh is 10, PELow is 2, and the current PE is 7, then PERelative is 62.5.

The actual calculation of PERelative is the difference between the trailing twelve month P/E and the 5 year P/E Low divided by the difference between the 5 year P/E High and the 5 year P/E Low, multiplied by 100.

*Period: 5 Years*


### Factor variants

#### Enterprise value to EBITDA

| Factor | Description | Period |
|---|---|---|
| `EV2EBITDAQ` | Enterprise value to operating income plus depreciation and amortization. | Latest Quarter |
| `EV2EBITDAPQ` | Enterprise value to operating income plus depreciation and amortization. | Previous Quarter |
| `EV2EBITDAPYQ` | Enterprise value to operating income plus depreciation and amortization. | Previous Quarter 1 Year Ago |
| `EV2EBITDATTM` | Enterprise value to operating income plus depreciation and amortization. | Trailing 12 Months |
| `EV2EBITDAPTM` | Enterprise value to operating income plus depreciation and amortization. | Previous Trailing 12 Months |
| `EV2EBITDAA` | Enterprise value to operating income plus depreciation and amortization. | Latest Year |
| `EV2EBITDAPY` | Enterprise value to operating income plus depreciation and amortization. | Previous Year |

#### Enterprise value to Sales

| Factor | Description | Period |
|---|---|---|
| `EV2SalesQ` | Enterprise value to sales. | Latest Quarter |
| `EV2SalesPQ` | Enterprise value to sales. | Previous Quarter |
| `EV2SalesPYQ` | Enterprise value to sales. | Previous Quarter 1 Year Ago |
| `EV2SalesTTM` | Enterprise value to sales. | Trailing 12 Months |
| `EV2SalesPTM` | Enterprise value to sales. | Previous Trailing 12 Months |
| `EV2SalesA` | Enterprise value to sales. | Latest Year |
| `EV2SalesPY` | Enterprise value to sales. | Previous Year |

#### Price to Book Value

| Factor | Description | Period |
|---|---|---|
| `Pr2BookQ` | Market value relative to book value of equity. | Latest Quarter |
| `Pr2BookPQ` | Market value relative to book value of equity. | Previous Quarter |
| `Pr2BookPYQ` | Market value relative to book value of equity. | Previous Quarter 1 Year Ago |
| `Pr2BookA` | Market value relative to book value of equity. | Latest Year |
| `Pr2BookPY` | Market value relative to book value of equity. | Previous Year |

#### Price to Cash Flow

| Factor | Description | Period |
|---|---|---|
| `Pr2CashFlQ` | Stock price relative to cash flow per share. | Latest Quarter |
| `Pr2CashFlPQ` | Stock price relative to cash flow per share. | Previous Quarter |
| `Pr2CashFlPYQ` | Stock price relative to cash flow per share. | Previous Quarter 1 Year Ago |
| `Pr2CashFlTTM` | Stock price relative to cash flow per share. | Trailing 12 Months |
| `Pr2CashFlPTM` | Stock price relative to cash flow per share. | Previous Trailing 12 Months |
| `Pr2CashFlA` | Stock price relative to cash flow per share. | Latest Year |
| `Pr2CashFlPY` | Stock price relative to cash flow per share. | Previous Year |

#### Price to Cash Flow Incl R&D (aka Innovation Pr2CF)

| Factor | Description | Period |
|---|---|---|
| `Pr2CFInclRDQ` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Latest Quarter |
| `Pr2CFInclRDPQ` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Previous Quarter |
| `Pr2CFInclRDPYQ` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Previous Quarter 1 Year Ago |
| `Pr2CFInclRDTTM` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Trailing 12 Months |
| `Pr2CFInclRDPTM` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Previous Trailing 12 Months |
| `Pr2CFInclRDA` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Latest Year |
| `Pr2CFInclRDPY` | Adjusts P/CF ratio by adding R&D expenses back to operating cash flow. | Previous Year |

#### Price to Earnings (PE) Excl Xor

| Factor | Description | Period |
|---|---|---|
| `PEExclXorQ` | Share price relative to earnings per share excluding extraordinary items. | Latest Quarter |
| `PEExclXorPQ` | Share price relative to earnings per share excluding extraordinary items. | Previous Quarter |
| `PEExclXorPYQ` | Share price relative to earnings per share excluding extraordinary items. | Previous Quarter 1 Year Ago |
| `PEExclXorTTM` | Share price relative to earnings per share excluding extraordinary items. | Trailing 12 Months |
| `PEExclXorPTM` | Share price relative to earnings per share excluding extraordinary items. | Previous Trailing 12 Months |
| `PEExclXorA` | Share price relative to earnings per share excluding extraordinary items. | Latest Year |
| `PEExclXorPY` | Share price relative to earnings per share excluding extraordinary items. | Previous Year |

#### Price to Earnings (PE) Incl Xor

| Factor | Description | Period |
|---|---|---|
| `PEInclXorQ` | Share price relative to earnings per share including extraordinary items. | Latest Quarter |
| `PEInclXorPQ` | Share price relative to earnings per share including extraordinary items. | Previous Quarter |
| `PEInclXorPYQ` | Share price relative to earnings per share including extraordinary items. | Previous Quarter 1 Year Ago |
| `PEInclXorTTM` | Share price relative to earnings per share including extraordinary items. | Trailing 12 Months |
| `PEInclXorPTM` | Share price relative to earnings per share including extraordinary items. | Previous Trailing 12 Months |
| `PEInclXorA` | Share price relative to earnings per share including extraordinary items. | Latest Year |
| `PEInclXorPY` | Share price relative to earnings per share including extraordinary items. | Previous Year |

#### Price to Earnings Incl R&D (aka Innovation PE)

| Factor | Description | Period |
|---|---|---|
| `PEInclRDQ` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Latest Quarter |
| `PEInclRDPQ` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Previous Quarter |
| `PEInclRDPYQ` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Previous Quarter 1 Year Ago |
| `PEInclRDTTM` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Trailing 12 Months |
| `PEInclRDPTM` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Previous Trailing 12 Months |
| `PEInclRDA` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Latest Year |
| `PEInclRDPY` | Adjusts P/E ratio by adding R&D expenses back to earnings. | Previous Year |

#### Price to Free Cash Flow

| Factor | Description | Period |
|---|---|---|
| `Pr2FrCashFlQ` | Market price per share to free cash flow per share. | Latest Quarter |
| `Pr2FrCashFlPQ` | Market price per share to free cash flow per share. | Previous Quarter |
| `Pr2FrCashFlPYQ` | Market price per share to free cash flow per share. | Previous Quarter 1 Year Ago |
| `Pr2FrCashFlTTM` | Market price per share to free cash flow per share. | Trailing 12 Months |
| `Pr2FrCashFlPTM` | Market price per share to free cash flow per share. | Previous Trailing 12 Months |
| `Pr2FrCashFlA` | Market price per share to free cash flow per share. | Latest Year |
| `Pr2FrCashFlPY` | Market price per share to free cash flow per share. | Previous Year |

#### Price to Net Free Cash Flow

| Factor | Description | Period |
|---|---|---|
| `Pr2NetFrCashFlQ` | Market price per share to net free cash flow per share. | Latest Quarter |
| `Pr2NetFrCashFlPQ` | Market price per share to net free cash flow per share. | Previous Quarter |
| `Pr2NetFrCashFlPYQ` | Market price per share to net free cash flow per share. | Previous Quarter 1 Year Ago |
| `Pr2NetFrCashFlTTM` | Market price per share to net free cash flow per share. | Trailing 12 Months |
| `Pr2NetFrCashFlPTM` | Market price per share to net free cash flow per share. | Previous Trailing 12 Months |
| `Pr2NetFrCashFlA` | Market price per share to net free cash flow per share. | Latest Year |
| `Pr2NetFrCashFlPY` | Market price per share to net free cash flow per share. | Previous Year |

#### Price to Sales

| Factor | Description | Period |
|---|---|---|
| `Pr2SalesQ` | Market cap to total revenues. | Latest Quarter |
| `Pr2SalesPQ` | Market cap to total revenues. | Previous Quarter |
| `Pr2SalesPYQ` | Market cap to total revenues. | Previous Quarter 1 Year Ago |
| `Pr2SalesTTM` | Market cap to total revenues. | Trailing 12 Months |
| `Pr2SalesPTM` | Market cap to total revenues. | Previous Trailing 12 Months |
| `Pr2SalesA` | Market cap to total revenues. | Latest Year |
| `Pr2SalesPY` | Market cap to total revenues. | Previous Year |

#### Price to Tangible Book Value

| Factor | Description | Period |
|---|---|---|
| `Pr2TanBkQ` | Stock price to tangible book value per share (common equity minus intangibles). | Latest Quarter |
| `Pr2TanBkPQ` | Stock price to tangible book value per share (common equity minus intangibles). | Previous Quarter |
| `Pr2TanBkPYQ` | Stock price to tangible book value per share (common equity minus intangibles). | Previous Quarter 1 Year Ago |
| `Pr2TanBkA` | Stock price to tangible book value per share (common equity minus intangibles). | Latest Year |
| `Pr2TanBkPY` | Stock price to tangible book value per share (common equity minus intangibles). | Previous Year |

#### Net Asset Value (NAV)

| Factor | Description | Period |
|---|---|---|
| `NAV` | The NAV per share. This is a MONTHLY item. This item applies to closed-end funds only. | Latest |
| `NAVPM` | The NAV per share 1 month ago This is a MONTHLY item. This item applies to closed-end funds only. | 1 Month Ago |
| `NAVPM2` | The NAV per share 2 months ago. This is a MONTHLY item. This item applies to closed-end funds only. | 2 Months Ago |
| `NAVPM3` | The NAV per share 3 months ago. This is a MONTHLY item. This item applies to closed-end funds only. | 3 Months Ago |

#### Net Asset Value (NAV) Discount

| Factor | Description | Period |
|---|---|---|
| `NAVDisc` | The most recent NAV discount. Funds trading below their NAV will show positive discounts. | Latest |
| `NAVDiscPM` | The NAV discount 1 month ago. Funds trading below their NAV will show positive discounts. | 1 Month Ago |
| `NAVDiscPM2` | The NAV discount 2 months ago Funds trading below their NAV will show positive discounts. | 2 Months Ago |
| `NAVDiscPM3` | The NAV discount 3 months ago. Funds trading below their NAV will show positive discounts. | 3 Months Ago |


## Valuation Projected

### Factors with detailed definitions

#### `PEGLT`

Price to Earnings Growth or PEG is a simple valuation rule of thumb. It states: "The p/e ratio of any company that's fairly priced will equal its growth rate." A value less than 1.0 might reflect potentially undervalued companies and a value greater than 1.0 would result in potentially overvalued companies.

We have four version of PEG

PEGLT - uses long term growth rates

PEGLTY - uses long term growth rates and includes Yied

PEGST - uses short term growth rates

PEGSTY - uses short term growth rates and includes Yield

Long Term

This is the more widely used PEG ratio. It is calculated by dividing the projected PE over the next twelve months by the analysts long growth rate estimates.

PEGLT = ProjPENTM / LTGrthMean

PEGLTY = ProjPENTM / (LTGrthMean + Yield)

Short Term

This version uses the past 12 months earnings (EPSExclXorTTM) and next year's EPS consensus estimate (NextFYEPSMean) to calculate the growth rate. Since it only looks up to 2 years ahead it has the potential to be more precise. However since earnings can be highly manipulated, this PEG variation can be more volatile

PEGST = PEExclXorTTM / stg

PEGSTY = PEExclXorTTM / ( stg + Yield )

stg = gr%(NextFYEPSMean , EPSExclXorTTM, y_till_ny ))

y_till_ny = Eval( QtrComplete=4, 2 , 2 - QtrComplete * 0.25)

*Period: Long Term*


#### `PEGLTY`

Price to Earnings Growth or PEG is a simple valuation rule of thumb. It states: "The p/e ratio of any company that's fairly priced will equal its growth rate." A value less than 1.0 might reflect potentially undervalued companies and a value greater than 1.0 would result in potentially overvalued companies.

We have four version of PEG

PEGLT - uses long term growth rates

PEGLTY - uses long term growth rates and includes Yied

PEGST - uses short term growth rates

PEGSTY - uses short term growth rates and includes Yield

Long Term

This is the more widely used PEG ratio. It is calculated by dividing the projected PE over the next twelve months by the analysts long growth rate estimates.

PEGLT = ProjPENTM / LTGrthMean

PEGLTY = ProjPENTM / (LTGrthMean + Yield)

Short Term

This version uses the past 12 months earnings (EPSExclXorTTM) and next year's EPS consensus estimate (NextFYEPSMean) to calculate the growth rate. Since it only looks up to 2 years ahead it has the potential to be more precise. However since earnings can be highly manipulated, this PEG variation can be more volatile

PEGST = PEExclXorTTM / stg

PEGSTY = PEExclXorTTM / ( stg + Yield )

stg = gr%(NextFYEPSMean , EPSExclXorTTM, y_till_ny ))

y_till_ny = Eval( QtrComplete=4, 2 , 2 - QtrComplete * 0.25)

*Period: Long Term*


#### `PEGST`

Price to Earnings Growth or PEG is a simple valuation rule of thumb. It states: "The p/e ratio of any company that's fairly priced will equal its growth rate." A value less than 1.0 might reflect potentially undervalued companies and a value greater than 1.0 would result in potentially overvalued companies.

We have four version of PEG

PEGLT - uses long term growth rates

PEGLTY - uses long term growth rates and includes Yied

PEGST - uses short term growth rates

PEGSTY - uses short term growth rates and includes Yield

Long Term

This is the more widely used PEG ratio. It is calculated by dividing the projected PE over the next twelve months by the analysts long growth rate estimates.

PEGLT = ProjPENTM / LTGrthMean

PEGLTY = ProjPENTM / (LTGrthMean + Yield)

Short Term

This version uses the past 12 months earnings (EPSExclXorTTM) and next year's EPS consensus estimate (NextFYEPSMean) to calculate the growth rate. Since it only looks up to 2 years ahead it has the potential to be more precise. However since earnings can be highly manipulated, this PEG variation can be more volatile

PEGST = PEExclXorTTM / stg

PEGSTY = PEExclXorTTM / ( stg + Yield )

stg = gr%(NextFYEPSMean , EPSExclXorTTM, y_till_ny ))

y_till_ny = Eval( QtrComplete=4, 2 , 2 - QtrComplete * 0.25)

*Period: Next Year Growth*


#### `PEGSTY`

Price to Earnings Growth or PEG is a simple valuation rule of thumb. It states: "The p/e ratio of any company that's fairly priced will equal its growth rate." A value less than 1.0 might reflect potentially undervalued companies and a value greater than 1.0 would result in potentially overvalued companies.

We have four version of PEG

PEGLT - uses long term growth rates

PEGLTY - uses long term growth rates and includes Yied

PEGST - uses short term growth rates

PEGSTY - uses short term growth rates and includes Yield

Long Term

This is the more widely used PEG ratio. It is calculated by dividing the projected PE over the next twelve months by the analysts long growth rate estimates.

PEGLT = ProjPENTM / LTGrthMean

PEGLTY = ProjPENTM / (LTGrthMean + Yield)

Short Term

This version uses the past 12 months earnings (EPSExclXorTTM) and next year's EPS consensus estimate (NextFYEPSMean) to calculate the growth rate. Since it only looks up to 2 years ahead it has the potential to be more precise. However since earnings can be highly manipulated, this PEG variation can be more volatile

PEGST = PEExclXorTTM / stg

PEGSTY = PEExclXorTTM / ( stg + Yield )

stg = gr%(NextFYEPSMean , EPSExclXorTTM, y_till_ny ))

y_till_ny = Eval( QtrComplete=4, 2 , 2 - QtrComplete * 0.25)

*Period: Next Year Growth*


#### `ProjPECurFY`

This is the current fiscal year projected Price to Earnings (P/E) Ratios given to companies by analysts. It is calculated by taking the current price and dividing it by the mean EPS estimate for the current fiscal year.

*Period: Current Year*


#### `ProjPENextFY`

This is next fiscal years projected Price to Earnings (P/E) Ratios given to companies by analysts. It is calculated by taking the current price and dividing it by the mean EPS estimate for the next fiscal year.

*Period: Next Fiscal Year*


#### `Pr2SalesNTM`

Price to Sales is a valuation metric that divides the current market cap by the revenues for the period. The price-to-sales ratio is an indicator of the value placed on each dollar of a company's sales or revenues. A low value may indicate undervaluation and a high value overvaluation.

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).

Price to Sales Including Debt

This is a variation suggested by the Fool.com staff. It simply adds the Long Term Debt to the Market Cap. It's calculated as follows:

(MarketCap + DebtLT)/Sales 

NOTE: Most Banks and Finance companies do not report revenues when they announce their preliminary quarterly financial results in the press. When this happens, the trailing twelve month values will not be available (NA) until the complete quarter is released.

*Period: Next 12 Months*


### Factor variants

#### Price To Earnings (PE) Projected

| Factor | Description | Period |
|---|---|---|
| `ProjPENTM` | Next Twelve Months Projected P/E Ratio | Next Twelve Months |


## Yield

### Factors with detailed definitions

#### `Yield`

Yield (or Indicated Yield) represents the expected return an investor will get by buying the stock at the current price. It's calculated using the Indicated Annual Dividend (IAD) and dividing it by the latest price.

IAD comes from the data vendor whenever it is available. The calculation of IAD could be as straightforward as multiplying the last quarterly dividend by 4, but can be more involved or come from other sources, for example information in a press releases.

Formula

Yield = 100 * IAD / Price

*Period: Current*


#### `Yield5YAvg`

This value is the average of the dividend Yield over the last 60 months (approximated using 21 bars). Up to 60 samples of Indicated Annual Dividends (IAD) are used to calculate 60 yields, then averaged.

This is very similar to the value computed by the FHistAvg function which also spans 5 calendar year but uses 65 samples of Yield every 4 weeks.

FHistAvg("Yield",65,4)

*Period: 5 Years*


#### `EarnYield`

Earnings Yield is the ratio of a company's earnings to its market value, representing the percentage return an investor receives from current earnings. It is often preferred over the P/E ratio because losses simply produce negative yields rather than undefined values, eliminating missing or non-computable observations (NAs) in quantitative models and cross-sectional rankings. Higher earnings yield values are generally better, indicating cheaper valuation and potentially higher expected returns, while lower values imply a more expensive stock.

All else equal, the lower the ratio the less attractive a company is as an investment, because it means investors are putting money into the company but not receiving a very good return in exchange. A high earnings yield means a company is generating enough cash to satisfy its debt and other obligations, including taxes and dividend payouts.

Earnings yield might not be the best yield ratio for comparing stocks in different industries, because it doesn't normalize for capital structure, fixed asset investments, and taxes.

Formula

EarnYield = 100 * EPSExclXorTTM / Price


#### `EBITDAYield`

The EBITDA yield is a return measure that compares the EBITDA of a company to its enterprise value. The ratio is calculated by dividing the most recent 12 months EBITDA by the current enterprise value.

All else equal, the lower the ratio, the less attractive a company is as an investment, because it means investors are putting money into the company but not receiving a very good return in exchange. A high EBITDA yield means a company is generating enough cash to keep investing in the business and satisfy its debt and other obligations, including dividend payouts.

EBITDA measures the return a company is making without amortizing fixed assets, so EBITDA/EV can also be seen as a return on investment proxy for the company. A merit of this ratio is that EBITDA normalizes for differences in capital structure, taxation, and fixed asset accounting, while the enterprise value (EV) also normalizes for differences in a company's capital structure.

Formula

EBITDAYield = 100 * EBITDATTM / EV


#### `FCFYield`

Free cash flow yield is a return measure that compares the free cash flow of a company to its market value. A high free cash flow yield result means a company is generating enough cash to satisfy its debt and other obligations, including dividend payouts. Free cash flow, which excludes capital expenditures but considers other ongoing costs a business incurs to keep itself running, is an alternative representation of the returns shareholders receive from owning a business, and may be preferred to net income because it is more difficult to manipulate by management.

Formula:

The ratio is calculated by dividing the most recent trailing twelve months free cash flow by market cap.

FCFYield = FCFTTM / MktCap


#### `OCFYield`

Operating cash flow yield is a return measure that compares the operating cash flow of a company to its market value. The ratio is calculated by dividing the most recent 12 months operating cash flow by the Market Cap.

All else equal, the lower the ratio, the less attractive a company is as an investment, because it means investors are putting money into the company but not receiving a very good return in exchange. A high operating cash flow yield result means a company is generating enough cash to keep investing in the business and satisfy its debt and other obligations, including dividend payouts.

Operating cash flow measures the return a company is making without investing in new fixed assets, so operating cash flow yield can also be seen as a return on investment proxy for the company.

Formula

OCFYield = 100 * OperCashFl / MktCap


#### `OpIncYield`

The operating income yield is a return measure that compares the operating income of a company to its enterprise value. The ratio is calculated by dividing the most recent 12 months operating income by the current enterprise value.

All else equal, the lower the ratio the less attractive a company is as an investment, because it means investors are putting money into the company but not receiving a very good return in exchange. A high operating income yield means a company is generating enough cash to satisfy its debt and other obligations, including taxes and dividend payouts.

Operating income doesn't include interest and taxes, while the enterprise value (EV) normalizes for differences in a company's capital structure. Therefore operating income yield normalizes differences in capital structure and taxation.

Formula

OpIncYield = 100 * OpInc / EV


#### `ShareholderYield`

The shareholder yield is a return measure that compares the company cash and non-cash distributions and its market value. The ratio is calculated by summing to the dividend yield the buyback yield, calculated as minus net equity issuance divided by market capitalization.

All else equal, the lower the ratio the less attractive a company is as an investment, because it means investors are putting money into the company but not receiving a good cash return in exchange.

This ratio is a more accurate representation of return to the shareholder than the dividend yield because it includes all distributions (and dilutions) for the shareholders.

Formula

Yield + 100 * (EqPurch - EqIssued)/MktCap

Yield + 100 * (1-SharesQ/SharesPYQ)

Alternate when EqPurch or EqIssued is N/A



## Margins

### Functions

#### `EBITDAMgn%(offset, type[, NAHandling])`

EBITDA Margin measures operating profitability before non-cash expenses and financing effects as percentage of revenue. Shows how much operating cash a company generates per dollar of sales before capital structure impacts. Higher margins indicate better operational efficiency and pricing power.


#### `FCFLMgn%(offset, type[, NAHandling])`

This value measures the percent of free cash flow compared to the Total Revenues. It is calculated as Free Cash Flow divided by the Total Revenue for the period expressed as percentage.


#### `GMgn%(offset, type[, NAHandling])`

Gross margin (GMgn%) is a profitability metric that evaluates a company's gross profit relative to its revenue or sales, expressed as a percentage. The higher the gross margin, the more capital the company retains, which can be utilized to cover other expenses or reward shareholders.

We provide two versions of the gross margin metric: GMgn% and GMgn%_GAAP. The difference between these two lies in including depreciation and amortization expenses in the GAAP version, impacting the gross profit calculation.

Formulas

GMgn% = GrossProfit / Sales

GMgn%_GAAP = (GrossProfit - Depreciation and Amortization) / Sales

GMgn% offers a view of the company's operational efficiency, excluding depreciation and amortization, which are non-cash expenses. This can be useful for evaluating the core profitability of a company's business operations. On the other hand, GMgn%_GAAP, by including depreciation and amortization, provides a more conservative perspective, aligning closer with GAAP principles.


#### `GMgn%_GAAP(offset, type[, NAHandling])`

Gross margin (GMgn%) is a profitability metric that evaluates a company's gross profit relative to its revenue or sales, expressed as a percentage. The higher the gross margin, the more capital the company retains, which can be utilized to cover other expenses or reward shareholders.

We provide two versions of the gross margin metric: GMgn% and GMgn%_GAAP. The difference between these two lies in including depreciation and amortization expenses in the GAAP version, impacting the gross profit calculation.

Formulas

GMgn% = GrossProfit / Sales

GMgn%_GAAP = (GrossProfit - Depreciation and Amortization) / Sales

GMgn% offers a view of the company's operational efficiency, excluding depreciation and amortization, which are non-cash expenses. This can be useful for evaluating the core profitability of a company's business operations. On the other hand, GMgn%_GAAP, by including depreciation and amortization, provides a more conservative perspective, aligning closer with GAAP principles.


#### `NetFCFLMgn%(offset, type)`

This value measures the percent of net free cash flow compared to the total revenues. It is calculated as Net Free Cash Flow divided by the Total Revenue for the period expressed as percentage.


#### `NPMgn%(offset, type[, NAHandling])`

Also known as Return on Sales, this value is the Income After Taxes divided by Total Revenue for the period expressed as a percentage.


#### `OpMgn%(offset, type[, NAHandling])`

This value measures the percent of revenues remaining after paying all operating expenses. It is calculated as operating Income divided by Total Revenue for the period expressed as percentage. Operating Income is defined as Total Revenue minus Total Operating Expenses.


#### `PTMgn%(offset, type[, NAHandling])`

This value represents Income Before Taxes expressed as a percent of Total Revenue for the period expressed as percentage.


#### `SGA2Sales%(offset, type[, NAHandling])`

This is calculated by dividing the Selling, General and Administrative (SG&A) Expenses by the Total Sales for the period expressed as percentage. SG&A as reported includes research and development.


### Factors with detailed definitions

#### `EBITDAMgn%5Y`

This value is calculated by first determining the annual EBITD Margins for the 5 most recent fiscal years and then averaging the values.

*Period: 5 Years*


#### `GMgn%5Y`

This value is calculated by first determining the Gross Margin for each of the 5 most recent fiscal years and then averaging the values.

Gross Margin is Total Revenue minus Cost of Goods Sold divided by Total Revenue and is expressed as a percentage.

*Period: 5 Years*


#### `NPMgn%5Y`

This value is calculated by first determining the Net Profit Margin for each of the 5 most recent fiscal years and then averaging the values.

Net Profit Margin is the Income After Taxes divided by Total Revenue, expressed as a percentage.

*Period: 5 Years*


#### `OpMgn%5Y`

This value measures the percent of revenues remaining after paying all operating expenses. 

It is calculated by first determining the Operating Margin for each of the last 5 fiscal years and then averaging the values. 

Operating Margin is defined as Operating Income divided by Total Revenue and expressed as a percentage.

*Period: 5 Years*


#### `PTMgn%5Y`

This value is calculated by determining the Pretax Margin for each of the 5 most recent fiscal years and averaging the values. 

Pretax Margin is defined as the Income Before Taxes divided by the Total Revenue.

*Period: 5 Years*


### Factor variants

#### EBITDA Margin

| Factor | Description | Period |
|---|---|---|
| `EBITDAMgn%Q` | EBITDA as percentage of revenue. | Latest Quarter |
| `EBITDAMgn%PQ` | EBITDA as percentage of revenue. | Previous Quarter |
| `EBITDAMgn%PYQ` | EBITDA as percentage of revenue. | Previous Quarter 1 Year Ago |
| `EBITDAMgn%TTM` | EBITDA as percentage of revenue. | Trailing 12 Months |
| `EBITDAMgn%PTM` | EBITDA as percentage of revenue. | Previous Trailing 12 Months |
| `EBITDAMgn%A` | EBITDA as percentage of revenue. | Latest Year |
| `EBITDAMgn%PY` | EBITDA as percentage of revenue. | Previous Year |
| `EBITDAMgn%Gr%PQ` | EBITDA as percentage of revenue. | Q vs Previous Q Growth |
| `EBITDAMgn%Gr%PYQ` | EBITDA as percentage of revenue. | Q vs 1 year ago Q Growth |
| `EBITDAMgn%Gr%TTM` | EBITDA as percentage of revenue. | Trailing Twelve Months Growth |
| `EBITDAMgn%Gr%PQTTM` | EBITDA as percentage of revenue. | Trailing Twelve Months Growth 1Q Ago |
| `EBITDAMgn%Gr%A` | EBITDA as percentage of revenue. | Growth Annual |
| `EBITDAMgn%Gr%3Y` | EBITDA as percentage of revenue. | Three Year Annualized Growth |
| `EBITDAMgn%Gr%5Y` | EBITDA as percentage of revenue. | Five Year Annualized Growth |
| `EBITDAMgn%Gr%10Y` | EBITDA as percentage of revenue. | Ten Year Annualized Growth |
| `EBITDAMgn%RSD%ANN` | EBITDA as percentage of revenue. | Ten Year Relative Standard Deviation |
| `EBITDAMgn%RSD%TTM` | EBITDA as percentage of revenue. | Five Year Relative Standard Deviation |
| `EBITDAMgn%RegEstANN` | EBITDA as percentage of revenue. | Ten Year Regression Estimate |
| `EBITDAMgn%RegEstTTM` | EBITDA as percentage of revenue. | Five Year Regression Estimate |
| `EBITDAMgn%RegGr%ANN` | EBITDA as percentage of revenue. | Ten Year Regression Estimate |
| `EBITDAMgn%RegGr%TTM` | EBITDA as percentage of revenue. | Five Year Regression Growth |
| `EBITDAMgn%3YAvg` | EBITDA as percentage of revenue. | Three Year Average |
| `EBITDAMgn%5YAvg` | EBITDA as percentage of revenue. | Five Year Average |

#### Free Cash Flow Margin

| Factor | Description | Period |
|---|---|---|
| `FCFLMgn%Q` | Free cash flow as a percentage of total revenues. | Latest Quarter |
| `FCFLMgn%PQ` | Free cash flow as a percentage of total revenues. | Previous Quarter |
| `FCFLMgn%PYQ` | Free cash flow as a percentage of total revenues. | Previous Quarter 1 Year Ago |
| `FCFLMgn%TTM` | Free cash flow as a percentage of total revenues. | Trailing 12 Months |
| `FCFLMgn%PTM` | Free cash flow as a percentage of total revenues. | Previous Trailing 12 Months |
| `FCFLMgn%A` | Free cash flow as a percentage of total revenues. | Latest Year |
| `FCFLMgn%PY` | Free cash flow as a percentage of total revenues. | Previous Year |
| `FCFLMgn%Gr%PQ` | Free cash flow as a percentage of total revenues. | Q vs Previous Q Growth |
| `FCFLMgn%Gr%PYQ` | Free cash flow as a percentage of total revenues. | Q vs 1 year ago Q Growth |
| `FCFLMgn%Gr%TTM` | Free cash flow as a percentage of total revenues. | Trailing Twelve Months Growth |
| `FCFLMgn%Gr%PQTTM` | Free cash flow as a percentage of total revenues. | Trailing Twelve Months Growth 1Q Ago |
| `FCFLMgn%Gr%A` | Free cash flow as a percentage of total revenues. | Growth Annual |
| `FCFLMgn%Gr%3Y` | Free cash flow as a percentage of total revenues. | Three Year Annualized Growth |
| `FCFLMgn%Gr%5Y` | Free cash flow as a percentage of total revenues. | Five Year Annualized Growth |
| `FCFLMgn%Gr%10Y` | Free cash flow as a percentage of total revenues. | Ten Year Annualized Growth |
| `FCFLMgn%RSD%ANN` | Free cash flow as a percentage of total revenues. | Ten Year Relative Standard Deviation |
| `FCFLMgn%RSD%TTM` | Free cash flow as a percentage of total revenues. | Five Year Relative Standard Deviation |
| `FCFLMgn%RegEstANN` | Free cash flow as a percentage of total revenues. | Ten Year Regression Estimate |
| `FCFLMgn%RegEstTTM` | Free cash flow as a percentage of total revenues. | Five Year Regression Estimate |
| `FCFLMgn%RegGr%ANN` | Free cash flow as a percentage of total revenues. | Ten Year Regression Estimate |
| `FCFLMgn%RegGr%TTM` | Free cash flow as a percentage of total revenues. | Five Year Regression Growth |
| `FCFLMgn%3YAvg` | Free cash flow as a percentage of total revenues. | Three Year Average |
| `FCFLMgn%5YAvg` | Free cash flow as a percentage of total revenues. | Five Year Average |

#### Gross Profit Margin

| Factor | Description | Period |
|---|---|---|
| `GMgn%Q` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Latest Quarter |
| `GMgn%PQ` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Previous Quarter |
| `GMgn%PYQ` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Previous Quarter 1 Year Ago |
| `GMgn%TTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Trailing 12 Months |
| `GMgn%PTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Previous Trailing 12 Months |
| `GMgn%A` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Latest Year |
| `GMgn%PY` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Previous Year |
| `GMgn%Gr%PQ` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Q vs Previous Q Growth |
| `GMgn%Gr%PYQ` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Q vs 1 year ago Q Growth |
| `GMgn%Gr%TTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Trailing Twelve Months Growth |
| `GMgn%Gr%PQTTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Trailing Twelve Months Growth 1Q Ago |
| `GMgn%Gr%A` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Growth Annual |
| `GMgn%Gr%3Y` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Three Year Annualized Growth |
| `GMgn%Gr%5Y` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Five Year Annualized Growth |
| `GMgn%Gr%10Y` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Ten Year Annualized Growth |
| `GMgn%RSD%ANN` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Ten Year Relative Standard Deviation |
| `GMgn%RSD%TTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Five Year Relative Standard Deviation |
| `GMgn%RegEstANN` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Ten Year Regression Estimate |
| `GMgn%RegEstTTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Five Year Regression Estimate |
| `GMgn%RegGr%ANN` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Ten Year Regression Estimate |
| `GMgn%RegGr%TTM` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Five Year Regression Growth |
| `GMgn%3YAvg` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Three Year Average |
| `GMgn%5YAvg` | Gross profit relative to revenue as a percentage. GMgn% = (Gross Profit / Sales) * 100. | Five Year Average |

#### Gross Profit Margin GAAP

| Factor | Description | Period |
|---|---|---|
| `GMgn%_GAAPQ` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Latest Quarter |
| `GMgn%_GAAPPQ` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Previous Quarter |
| `GMgn%_GAAPPYQ` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Previous Quarter 1 Year Ago |
| `GMgn%_GAAPTTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Trailing 12 Months |
| `GMgn%_GAAPPTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Previous Trailing 12 Months |
| `GMgn%_GAAPA` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Latest Year |
| `GMgn%_GAAPPY` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Previous Year |
| `GMgn%_GAAPGr%PQ` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Q vs Previous Q Growth |
| `GMgn%_GAAPGr%PYQ` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Q vs 1 year ago Q Growth |
| `GMgn%_GAAPGr%TTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Trailing Twelve Months Growth |
| `GMgn%_GAAPGr%PQTTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Trailing Twelve Months Growth 1Q Ago |
| `GMgn%_GAAPGr%A` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Growth Annual |
| `GMgn%_GAAPGr%3Y` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Three Year Annualized Growth |
| `GMgn%_GAAPGr%5Y` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Five Year Annualized Growth |
| `GMgn%_GAAPGr%10Y` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Ten Year Annualized Growth |
| `GMgn%_GAAPRSD%ANN` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Ten Year Relative Standard Deviation |
| `GMgn%_GAAPRSD%TTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Five Year Relative Standard Deviation |
| `GMgn%_GAAPRegEstANN` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Ten Year Regression Estimate |
| `GMgn%_GAAPRegEstTTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Five Year Regression Estimate |
| `GMgn%_GAAPRegGr%ANN` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Ten Year Regression Estimate |
| `GMgn%_GAAPRegGr%TTM` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Five Year Regression Growth |
| `GMgn%_GAAP3YAvg` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Three Year Average |
| `GMgn%_GAAP5YAvg` | Gross profit relative to revenue as a percentage. GMgn%_GAAP = ((Gross Profit - D&A) / Sales) * 100. | Five Year Average |

#### Net Free Cash Flow Margin

| Factor | Description | Period |
|---|---|---|
| `NetFCFLMgn%Q` | Net free cash flow as a percentage of total revenues. | Latest Quarter |
| `NetFCFLMgn%PQ` | Net free cash flow as a percentage of total revenues. | Previous Quarter |
| `NetFCFLMgn%PYQ` | Net free cash flow as a percentage of total revenues. | Previous Quarter 1 Year Ago |
| `NetFCFLMgn%TTM` | Net free cash flow as a percentage of total revenues. | Trailing 12 Months |
| `NetFCFLMgn%PTM` | Net free cash flow as a percentage of total revenues. | Previous Trailing 12 Months |
| `NetFCFLMgn%A` | Net free cash flow as a percentage of total revenues. | Latest Year |
| `NetFCFLMgn%PY` | Net free cash flow as a percentage of total revenues. | Previous Year |
| `NetFCFLMgn%Gr%PQ` | Net free cash flow as a percentage of total revenues. | Q vs Previous Q Growth |
| `NetFCFLMgn%Gr%PYQ` | Net free cash flow as a percentage of total revenues. | Q vs 1 year ago Q Growth |
| `NetFCFLMgn%Gr%TTM` | Net free cash flow as a percentage of total revenues. | Trailing Twelve Months Growth |
| `NetFCFLMgn%Gr%PQTTM` | Net free cash flow as a percentage of total revenues. | Trailing Twelve Months Growth 1Q Ago |
| `NetFCFLMgn%Gr%A` | Net free cash flow as a percentage of total revenues. | Growth Annual |
| `NetFCFLMgn%Gr%3Y` | Net free cash flow as a percentage of total revenues. | Three Year Annualized Growth |
| `NetFCFLMgn%Gr%5Y` | Net free cash flow as a percentage of total revenues. | Five Year Annualized Growth |
| `NetFCFLMgn%Gr%10Y` | Net free cash flow as a percentage of total revenues. | Ten Year Annualized Growth |
| `NetFCFLMgn%RSD%ANN` | Net free cash flow as a percentage of total revenues. | Ten Year Relative Standard Deviation |
| `NetFCFLMgn%RSD%TTM` | Net free cash flow as a percentage of total revenues. | Five Year Relative Standard Deviation |
| `NetFCFLMgn%RegEstANN` | Net free cash flow as a percentage of total revenues. | Ten Year Regression Estimate |
| `NetFCFLMgn%RegEstTTM` | Net free cash flow as a percentage of total revenues. | Five Year Regression Estimate |
| `NetFCFLMgn%RegGr%ANN` | Net free cash flow as a percentage of total revenues. | Ten Year Regression Estimate |
| `NetFCFLMgn%RegGr%TTM` | Net free cash flow as a percentage of total revenues. | Five Year Regression Growth |
| `NetFCFLMgn%3YAvg` | Net free cash flow as a percentage of total revenues. | Three Year Average |
| `NetFCFLMgn%5YAvg` | Net free cash flow as a percentage of total revenues. | Five Year Average |

#### Net Profit Margin

| Factor | Description | Period |
|---|---|---|
| `NPMgn%Q` | Income after taxes as a percentage of total revenue. | Latest Quarter |
| `NPMgn%PQ` | Income after taxes as a percentage of total revenue. | Previous Quarter |
| `NPMgn%PYQ` | Income after taxes as a percentage of total revenue. | Previous Quarter 1 Year Ago |
| `NPMgn%TTM` | Income after taxes as a percentage of total revenue. | Trailing 12 Months |
| `NPMgn%PTM` | Income after taxes as a percentage of total revenue. | Previous Trailing 12 Months |
| `NPMgn%A` | Income after taxes as a percentage of total revenue. | Latest Year |
| `NPMgn%PY` | Income after taxes as a percentage of total revenue. | Previous Year |
| `NPMgn%Gr%PQ` | Income after taxes as a percentage of total revenue. | Q vs Previous Q Growth |
| `NPMgn%Gr%PYQ` | Income after taxes as a percentage of total revenue. | Q vs 1 year ago Q Growth |
| `NPMgn%Gr%TTM` | Income after taxes as a percentage of total revenue. | Trailing Twelve Months Growth |
| `NPMgn%Gr%PQTTM` | Income after taxes as a percentage of total revenue. | Trailing Twelve Months Growth 1Q Ago |
| `NPMgn%Gr%A` | Income after taxes as a percentage of total revenue. | Growth Annual |
| `NPMgn%Gr%3Y` | Income after taxes as a percentage of total revenue. | Three Year Annualized Growth |
| `NPMgn%Gr%5Y` | Income after taxes as a percentage of total revenue. | Five Year Annualized Growth |
| `NPMgn%Gr%10Y` | Income after taxes as a percentage of total revenue. | Ten Year Annualized Growth |
| `NPMgn%RSD%ANN` | Income after taxes as a percentage of total revenue. | Ten Year Relative Standard Deviation |
| `NPMgn%RSD%TTM` | Income after taxes as a percentage of total revenue. | Five Year Relative Standard Deviation |
| `NPMgn%RegEstANN` | Income after taxes as a percentage of total revenue. | Ten Year Regression Estimate |
| `NPMgn%RegEstTTM` | Income after taxes as a percentage of total revenue. | Five Year Regression Estimate |
| `NPMgn%RegGr%ANN` | Income after taxes as a percentage of total revenue. | Ten Year Regression Estimate |
| `NPMgn%RegGr%TTM` | Income after taxes as a percentage of total revenue. | Five Year Regression Growth |
| `NPMgn%PSQ` | Income after taxes as a percentage of total revenue. | Quarterly Per Share |
| `NPMgn%PSA` | Income after taxes as a percentage of total revenue. | Annual Per Share |
| `NPMgn%%SalesQ` | Income after taxes as a percentage of total revenue. | % of Quarterly Sales |
| `NPMgn%%SalesA` | Income after taxes as a percentage of total revenue. | % of Annual Sales |
| `NPMgn%%AssetsQ` | Income after taxes as a percentage of total revenue. | % of Quarterly Assets |
| `NPMgn%%AssetsA` | Income after taxes as a percentage of total revenue. | % of Annual Assets |
| `NPMgn%3YAvg` | Income after taxes as a percentage of total revenue. | Three Year Average |
| `NPMgn%5YAvg` | Income after taxes as a percentage of total revenue. | Five Year Average |

#### Operating Margin

| Factor | Description | Period |
|---|---|---|
| `OpMgn%Q` | Percent of revenues after operating expenses. | Latest Quarter |
| `OpMgn%PQ` | Percent of revenues after operating expenses. | Previous Quarter |
| `OpMgn%PYQ` | Percent of revenues after operating expenses. | Previous Quarter 1 Year Ago |
| `OpMgn%TTM` | Percent of revenues after operating expenses. | Trailing 12 Months |
| `OpMgn%PTM` | Percent of revenues after operating expenses. | Previous Trailing 12 Months |
| `OpMgn%A` | Percent of revenues after operating expenses. | Latest Year |
| `OpMgn%PY` | Percent of revenues after operating expenses. | Previous Year |
| `OpMgn%Gr%PQ` | Percent of revenues after operating expenses. | Q vs Previous Q Growth |
| `OpMgn%Gr%PYQ` | Percent of revenues after operating expenses. | Q vs 1 year ago Q Growth |
| `OpMgn%Gr%TTM` | Percent of revenues after operating expenses. | Trailing Twelve Months Growth |
| `OpMgn%Gr%PQTTM` | Percent of revenues after operating expenses. | Trailing Twelve Months Growth 1Q Ago |
| `OpMgn%Gr%A` | Percent of revenues after operating expenses. | Growth Annual |
| `OpMgn%Gr%3Y` | Percent of revenues after operating expenses. | Three Year Annualized Growth |
| `OpMgn%Gr%5Y` | Percent of revenues after operating expenses. | Five Year Annualized Growth |
| `OpMgn%Gr%10Y` | Percent of revenues after operating expenses. | Ten Year Annualized Growth |
| `OpMgn%RSD%ANN` | Percent of revenues after operating expenses. | Ten Year Relative Standard Deviation |
| `OpMgn%RSD%TTM` | Percent of revenues after operating expenses. | Five Year Relative Standard Deviation |
| `OpMgn%RegEstANN` | Percent of revenues after operating expenses. | Ten Year Regression Estimate |
| `OpMgn%RegEstTTM` | Percent of revenues after operating expenses. | Five Year Regression Estimate |
| `OpMgn%RegGr%ANN` | Percent of revenues after operating expenses. | Ten Year Regression Estimate |
| `OpMgn%RegGr%TTM` | Percent of revenues after operating expenses. | Five Year Regression Growth |
| `OpMgn%3YAvg` | Percent of revenues after operating expenses. | Three Year Average |
| `OpMgn%5YAvg` | Percent of revenues after operating expenses. | Five Year Average |

#### Pretax Margin

| Factor | Description | Period |
|---|---|---|
| `PTMgn%Q` | Income before taxes as a percentage of total revenue. | Latest Quarter |
| `PTMgn%PQ` | Income before taxes as a percentage of total revenue. | Previous Quarter |
| `PTMgn%PYQ` | Income before taxes as a percentage of total revenue. | Previous Quarter 1 Year Ago |
| `PTMgn%TTM` | Income before taxes as a percentage of total revenue. | Trailing 12 Months |
| `PTMgn%PTM` | Income before taxes as a percentage of total revenue. | Previous Trailing 12 Months |
| `PTMgn%A` | Income before taxes as a percentage of total revenue. | Latest Year |
| `PTMgn%PY` | Income before taxes as a percentage of total revenue. | Previous Year |
| `PTMgn%Gr%PQ` | Income before taxes as a percentage of total revenue. | Q vs Previous Q Growth |
| `PTMgn%Gr%PYQ` | Income before taxes as a percentage of total revenue. | Q vs 1 year ago Q Growth |
| `PTMgn%Gr%TTM` | Income before taxes as a percentage of total revenue. | Trailing Twelve Months Growth |
| `PTMgn%Gr%PQTTM` | Income before taxes as a percentage of total revenue. | Trailing Twelve Months Growth 1Q Ago |
| `PTMgn%Gr%A` | Income before taxes as a percentage of total revenue. | Growth Annual |
| `PTMgn%Gr%3Y` | Income before taxes as a percentage of total revenue. | Three Year Annualized Growth |
| `PTMgn%Gr%5Y` | Income before taxes as a percentage of total revenue. | Five Year Annualized Growth |
| `PTMgn%Gr%10Y` | Income before taxes as a percentage of total revenue. | Ten Year Annualized Growth |
| `PTMgn%RSD%ANN` | Income before taxes as a percentage of total revenue. | Ten Year Relative Standard Deviation |
| `PTMgn%RSD%TTM` | Income before taxes as a percentage of total revenue. | Five Year Relative Standard Deviation |
| `PTMgn%RegEstANN` | Income before taxes as a percentage of total revenue. | Ten Year Regression Estimate |
| `PTMgn%RegEstTTM` | Income before taxes as a percentage of total revenue. | Five Year Regression Estimate |
| `PTMgn%RegGr%ANN` | Income before taxes as a percentage of total revenue. | Ten Year Regression Estimate |
| `PTMgn%RegGr%TTM` | Income before taxes as a percentage of total revenue. | Five Year Regression Growth |
| `PTMgn%3YAvg` | Income before taxes as a percentage of total revenue. | Three Year Average |
| `PTMgn%5YAvg` | Income before taxes as a percentage of total revenue. | Five Year Average |

#### Selling,Gen,Admin to Sales %

| Factor | Description | Period |
|---|---|---|
| `SGA2Sales%Q` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Latest Quarter |
| `SGA2Sales%PQ` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Previous Quarter |
| `SGA2Sales%PYQ` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Previous Quarter 1 Year Ago |
| `SGA2Sales%TTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Trailing 12 Months |
| `SGA2Sales%PTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Previous Trailing 12 Months |
| `SGA2Sales%A` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Latest Year |
| `SGA2Sales%PY` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Previous Year |
| `SGA2Sales%Gr%PQ` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Q vs Previous Q Growth |
| `SGA2Sales%Gr%PYQ` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Q vs 1 year ago Q Growth |
| `SGA2Sales%Gr%TTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Trailing Twelve Months Growth |
| `SGA2Sales%Gr%PQTTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Trailing Twelve Months Growth 1Q Ago |
| `SGA2Sales%Gr%A` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Growth Annual |
| `SGA2Sales%Gr%3Y` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Three Year Annualized Growth |
| `SGA2Sales%Gr%5Y` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Five Year Annualized Growth |
| `SGA2Sales%Gr%10Y` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Ten Year Annualized Growth |
| `SGA2Sales%RSD%ANN` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Ten Year Relative Standard Deviation |
| `SGA2Sales%RSD%TTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Five Year Relative Standard Deviation |
| `SGA2Sales%RegEstANN` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Ten Year Regression Estimate |
| `SGA2Sales%RegEstTTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Five Year Regression Estimate |
| `SGA2Sales%RegGr%ANN` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Ten Year Regression Estimate |
| `SGA2Sales%RegGr%TTM` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Five Year Regression Growth |
| `SGA2Sales%3YAvg` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Three Year Average |
| `SGA2Sales%5YAvg` | Selling, general and administrative expenses (including R&D) as percentage of total sales. | Five Year Average |
| `SGA2Sales%5Y` | Operating Margin, 5 Year Factor (%) | 5 Years |


## Profitability

### Functions

#### `ROA%(offset, type[, NAHandling])`

This value is the Income Before Extraordinary Items divided by the Average Total Assets, expressed as a percentage. Average Total Assets is the average of the Total Assets at the beginning and the end of the period.

Formula:

ROA% = 100 * NetIncBXor / ( (a0 + a1)/2)

a0 = AstTot end of period

a1 = AstTot beginning of period

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).


#### `ROE%(offset, type[, NAHandling])`

This value is calculated as the Net Income Before Extraordinary Items for the period divided by the Average Common Equity and is expressed as a percentage. Average Common Equity is the average of the Common Equity at the beginning and the end of the period.

Formula:

ROE% = 100 * NetIncBXor / ( (e0 + e1)/2)

e0 = ComEq end of period

e1 = ComEq beginning of period

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).


#### `ROI%(offset, type[, NAHandling])`

This value is the ratio of Net Income Before Extraordinary Items plus the taxable portion of the Interest Expense, divided by the average Total Long Term Debt and Shareholders Equity, expressed as a percentage for the period. The denominator is measured as the average at the beginning and the end of the period.

Formula:

ROI% = 100 * ( NetIncBXor + IntExp * (1 - TaxRate) ) / (a0 + a1) / 2

a0 = ( DbtTot + EqTot ) end of period

a1 = ( DbtTot + EqTot ) beginning of period

TaxRate: country specific (ex: USA 21%, CAN 26.5%, IRL 12.5%)

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).


### Factor variants

#### Return on Assets

| Factor | Description | Period |
|---|---|---|
| `ROA%Q` | Net income before extraordinary items as a percentage of average total assets. | Latest Quarter |
| `ROA%PQ` | Net income before extraordinary items as a percentage of average total assets. | Previous Quarter |
| `ROA%PYQ` | Net income before extraordinary items as a percentage of average total assets. | Previous Quarter 1 Year Ago |
| `ROA%TTM` | Net income before extraordinary items as a percentage of average total assets. | Trailing 12 Months |
| `ROA%PTM` | Net income before extraordinary items as a percentage of average total assets. | Previous Trailing 12 Months |
| `ROA%A` | Net income before extraordinary items as a percentage of average total assets. | Latest Year |
| `ROA%PY` | Net income before extraordinary items as a percentage of average total assets. | Previous Year |
| `ROA%Gr%PQ` | Net income before extraordinary items as a percentage of average total assets. | Q vs Previous Q Growth |
| `ROA%Gr%PYQ` | Net income before extraordinary items as a percentage of average total assets. | Q vs 1 year ago Q Growth |
| `ROA%Gr%TTM` | Net income before extraordinary items as a percentage of average total assets. | Trailing Twelve Months Growth |
| `ROA%Gr%PQTTM` | Net income before extraordinary items as a percentage of average total assets. | Trailing Twelve Months Growth 1Q Ago |
| `ROA%Gr%A` | Net income before extraordinary items as a percentage of average total assets. | Growth Annual |
| `ROA%Gr%3Y` | Net income before extraordinary items as a percentage of average total assets. | Three Year Annualized Growth |
| `ROA%Gr%5Y` | Net income before extraordinary items as a percentage of average total assets. | Five Year Annualized Growth |
| `ROA%Gr%10Y` | Net income before extraordinary items as a percentage of average total assets. | Ten Year Annualized Growth |
| `ROA%RSD%ANN` | Net income before extraordinary items as a percentage of average total assets. | Ten Year Relative Standard Deviation |
| `ROA%RSD%TTM` | Net income before extraordinary items as a percentage of average total assets. | Five Year Relative Standard Deviation |
| `ROA%RegEstANN` | Net income before extraordinary items as a percentage of average total assets. | Ten Year Regression Estimate |
| `ROA%RegEstTTM` | Net income before extraordinary items as a percentage of average total assets. | Five Year Regression Estimate |
| `ROA%RegGr%ANN` | Net income before extraordinary items as a percentage of average total assets. | Ten Year Regression Estimate |
| `ROA%RegGr%TTM` | Net income before extraordinary items as a percentage of average total assets. | Five Year Regression Growth |
| `ROA%3YAvg` | Net income before extraordinary items as a percentage of average total assets. | Three Year Average |
| `ROA%5YAvg` | Net income before extraordinary items as a percentage of average total assets. | Five Year Average |

#### Return on Equity

| Factor | Description | Period |
|---|---|---|
| `ROE%Q` | Net income before extraordinary items as a percentage of average common equity. | Latest Quarter |
| `ROE%PQ` | Net income before extraordinary items as a percentage of average common equity. | Previous Quarter |
| `ROE%PYQ` | Net income before extraordinary items as a percentage of average common equity. | Previous Quarter 1 Year Ago |
| `ROE%TTM` | Net income before extraordinary items as a percentage of average common equity. | Trailing 12 Months |
| `ROE%PTM` | Net income before extraordinary items as a percentage of average common equity. | Previous Trailing 12 Months |
| `ROE%A` | Net income before extraordinary items as a percentage of average common equity. | Latest Year |
| `ROE%PY` | Net income before extraordinary items as a percentage of average common equity. | Previous Year |
| `ROE%Gr%PQ` | Net income before extraordinary items as a percentage of average common equity. | Q vs Previous Q Growth |
| `ROE%Gr%PYQ` | Net income before extraordinary items as a percentage of average common equity. | Q vs 1 year ago Q Growth |
| `ROE%Gr%TTM` | Net income before extraordinary items as a percentage of average common equity. | Trailing Twelve Months Growth |
| `ROE%Gr%PQTTM` | Net income before extraordinary items as a percentage of average common equity. | Trailing Twelve Months Growth 1Q Ago |
| `ROE%Gr%A` | Net income before extraordinary items as a percentage of average common equity. | Growth Annual |
| `ROE%Gr%3Y` | Net income before extraordinary items as a percentage of average common equity. | Three Year Annualized Growth |
| `ROE%Gr%5Y` | Net income before extraordinary items as a percentage of average common equity. | Five Year Annualized Growth |
| `ROE%Gr%10Y` | Net income before extraordinary items as a percentage of average common equity. | Ten Year Annualized Growth |
| `ROE%RSD%ANN` | Net income before extraordinary items as a percentage of average common equity. | Ten Year Relative Standard Deviation |
| `ROE%RSD%TTM` | Net income before extraordinary items as a percentage of average common equity. | Five Year Relative Standard Deviation |
| `ROE%RegEstANN` | Net income before extraordinary items as a percentage of average common equity. | Ten Year Regression Estimate |
| `ROE%RegEstTTM` | Net income before extraordinary items as a percentage of average common equity. | Five Year Regression Estimate |
| `ROE%RegGr%ANN` | Net income before extraordinary items as a percentage of average common equity. | Ten Year Regression Estimate |
| `ROE%RegGr%TTM` | Net income before extraordinary items as a percentage of average common equity. | Five Year Regression Growth |
| `ROE%3YAvg` | Net income before extraordinary items as a percentage of average common equity. | Three Year Average |
| `ROE%5YAvg` | Net income before extraordinary items as a percentage of average common equity. | Five Year Average |

#### Return on Investment

| Factor | Description | Period |
|---|---|---|
| `ROI%Q` | Net income plus after-tax interest expense as a percentage of average total capital. | Latest Quarter |
| `ROI%PQ` | Net income plus after-tax interest expense as a percentage of average total capital. | Previous Quarter |
| `ROI%PYQ` | Net income plus after-tax interest expense as a percentage of average total capital. | Previous Quarter 1 Year Ago |
| `ROI%TTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Trailing 12 Months |
| `ROI%PTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Previous Trailing 12 Months |
| `ROI%A` | Net income plus after-tax interest expense as a percentage of average total capital. | Latest Year |
| `ROI%PY` | Net income plus after-tax interest expense as a percentage of average total capital. | Previous Year |
| `ROI%Gr%PQ` | Net income plus after-tax interest expense as a percentage of average total capital. | Q vs Previous Q Growth |
| `ROI%Gr%PYQ` | Net income plus after-tax interest expense as a percentage of average total capital. | Q vs 1 year ago Q Growth |
| `ROI%Gr%TTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Trailing Twelve Months Growth |
| `ROI%Gr%PQTTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Trailing Twelve Months Growth 1Q Ago |
| `ROI%Gr%A` | Net income plus after-tax interest expense as a percentage of average total capital. | Growth Annual |
| `ROI%Gr%3Y` | Net income plus after-tax interest expense as a percentage of average total capital. | Three Year Annualized Growth |
| `ROI%Gr%5Y` | Net income plus after-tax interest expense as a percentage of average total capital. | Five Year Annualized Growth |
| `ROI%Gr%10Y` | Net income plus after-tax interest expense as a percentage of average total capital. | Ten Year Annualized Growth |
| `ROI%RSD%ANN` | Net income plus after-tax interest expense as a percentage of average total capital. | Ten Year Relative Standard Deviation |
| `ROI%RSD%TTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Five Year Relative Standard Deviation |
| `ROI%RegEstANN` | Net income plus after-tax interest expense as a percentage of average total capital. | Ten Year Regression Estimate |
| `ROI%RegEstTTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Five Year Regression Estimate |
| `ROI%RegGr%ANN` | Net income plus after-tax interest expense as a percentage of average total capital. | Ten Year Regression Estimate |
| `ROI%RegGr%TTM` | Net income plus after-tax interest expense as a percentage of average total capital. | Five Year Regression Growth |
| `ROI%3YAvg` | Net income plus after-tax interest expense as a percentage of average total capital. | Three Year Average |
| `ROI%5YAvg` | Net income plus after-tax interest expense as a percentage of average total capital. | Five Year Average |


## Per Share Ratios

### Functions

#### `BVPS(offset, type[, NAHandling])`

The per-share value of common equity.


#### `CapExPS(offset, type[, NAHandling])`

Capital Expenditures is the amount of cash spent on purchases of property, plant and equipment in the period. Generally, a higher number is desired because it can indicate that the company is investing capital for future growth. To calculate per share value it is divided by the fully-diluted (where available) average shares outstanding for the same period

Formula

CapEx: Straight from filing Line-Item

CapExPS: CapeEx / SharesFD

NOTE: CapitalIQ specifically excludes property, plant and equipment from acquisitions from this line.


#### `CashFlPS(offset, type[, NAHandling])`

Cash Flow is defined as the sum of Income After Taxes minus Preferred Dividends and Depreciation and Amortization. To calculate per share it is divided by the fully-diluted (where available) average shares outstanding for the same period.

Formula

CashFl = GetDepAndAmort + NetIncCFStmt

CashFlPS = CashFl / SharesFD


#### `CashPS(offset, type[, NAHandling])`

This is the Total Cash plus Short Term Investments divided by the fully-diluted (where available) Shares Outstanding for the same period.


#### `EPSExclXor(offset, type[, NAHandling])`

EPS Excluding Extraordinary Items is earnings per share including all expenses with the exception of those deemed extraordinary. This is what we use as our default for earnings per share in most functions.

This field is calculated using net income, including all expenses but excluding extraordinary items, subtracting preferred dividend payments, and using fully diluted shares.

The most common source of extraordinary items in recent accounting is discontinued operations.


#### `EPSInclXor(offset, type[, NAHandling])`

EPS Including Extraordinary Items is earnings per share including all expenses, including those deemed extraordinary.

This field is provided by CompuStat. It is calculated with net income, including all expenses and extraordinary items, and using fully diluted shares.

The most common source of extraordinary items in recent accounting is discontinued operations.


#### `EBITDAPS(offset, type[, NAHandling])`

Earnings before interest, taxes, depreciation and amortization on a per-share basis.


#### `FCFPS(offset, type[, NAHandling])`

This is the quarterly Free Cash Flow divided by the fully-diluted (where available) Average Shares Outstanding found on the Income Statement for the same period.


#### `NetFCFPS(offset, type)`

This is the quarterly Net Free Cash Flow divided by the fully-diluted (where available) Average Shares Outstanding found on the Income Statement for the same period.


#### `OCFPS(offset, type[, NAHandling])`

Operating Cashflow Per Share.


#### `OpIncPS(offset, type[, NAHandling])`

This value is calculated by dividing Operating Income by the fully-diluted (where available) Average Shares Outstanding for the same period. Operating Income is defined as Total Revenue for the most recent quarter minus Total Operating Expenses.


#### `SalesPS(offset, type[, NAHandling])`

This value is the Total Revenue divided by the fully-diluted (where available) Average Shares Outstanding for the same period.


### Factor variants

#### Book Value Per Share

| Factor | Description | Period |
|---|---|---|
| `BVPSQ` | The per-share value of common equity. | Latest Quarter |
| `BVPSPQ` | The per-share value of common equity. | Previous Quarter |
| `BVPSPYQ` | The per-share value of common equity. | Previous Quarter 1 Year Ago |
| `BVPSTTM` | The per-share value of common equity. | Trailing 12 Months |
| `BVPSPTM` | The per-share value of common equity. | Previous Trailing 12 Months |
| `BVPSA` | The per-share value of common equity. | Latest Year |
| `BVPSPY` | The per-share value of common equity. | Previous Year |
| `BVPSGr%PQ` | The per-share value of common equity. | Q vs Previous Q Growth |
| `BVPSGr%PYQ` | The per-share value of common equity. | Q vs 1 year ago Q Growth |
| `BVPSGr%TTM` | The per-share value of common equity. | Trailing Twelve Months Growth |
| `BVPSGr%PQTTM` | The per-share value of common equity. | Trailing Twelve Months Growth 1Q Ago |
| `BVPSGr%A` | The per-share value of common equity. | Growth Annual |
| `BVPSGr%3Y` | The per-share value of common equity. | Three Year Annualized Growth |
| `BVPSGr%5Y` | The per-share value of common equity. | Five Year Annualized Growth |
| `BVPSGr%10Y` | The per-share value of common equity. | Ten Year Annualized Growth |
| `BVPSRSD%ANN` | The per-share value of common equity. | Ten Year Relative Standard Deviation |
| `BVPSRSD%TTM` | The per-share value of common equity. | Five Year Relative Standard Deviation |
| `BVPSRegEstANN` | The per-share value of common equity. | Ten Year Regression Estimate |
| `BVPSRegEstTTM` | The per-share value of common equity. | Five Year Regression Estimate |
| `BVPSRegGr%ANN` | The per-share value of common equity. | Ten Year Regression Estimate |
| `BVPSRegGr%TTM` | The per-share value of common equity. | Five Year Regression Growth |
| `BVPS3YAvg` | The per-share value of common equity. | Three Year Average |
| `BVPS5YAvg` | The per-share value of common equity. | Five Year Average |

#### Capital Expenditures (CapEx) Per Share

| Factor | Description | Period |
|---|---|---|
| `CapExPSQ` | Capital expenditures divided by shares outstanding. | Latest Quarter |
| `CapExPSPQ` | Capital expenditures divided by shares outstanding. | Previous Quarter |
| `CapExPSPYQ` | Capital expenditures divided by shares outstanding. | Previous Quarter 1 Year Ago |
| `CapExPSTTM` | Capital expenditures divided by shares outstanding. | Trailing 12 Months |
| `CapExPSPTM` | Capital expenditures divided by shares outstanding. | Previous Trailing 12 Months |
| `CapExPSA` | Capital expenditures divided by shares outstanding. | Latest Year |
| `CapExPSPY` | Capital expenditures divided by shares outstanding. | Previous Year |
| `CapExPSGr%PQ` | Capital expenditures divided by shares outstanding. | Q vs Previous Q Growth |
| `CapExPSGr%PYQ` | Capital expenditures divided by shares outstanding. | Q vs 1 year ago Q Growth |
| `CapExPSGr%TTM` | Capital expenditures divided by shares outstanding. | Trailing Twelve Months Growth |
| `CapExPSGr%PQTTM` | Capital expenditures divided by shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `CapExPSGr%A` | Capital expenditures divided by shares outstanding. | Growth Annual |
| `CapExPSGr%3Y` | Capital expenditures divided by shares outstanding. | Three Year Annualized Growth |
| `CapExPSGr%5Y` | Capital expenditures divided by shares outstanding. | Five Year Annualized Growth |
| `CapExPSGr%10Y` | Capital expenditures divided by shares outstanding. | Ten Year Annualized Growth |
| `CapExPSRSD%ANN` | Capital expenditures divided by shares outstanding. | Ten Year Relative Standard Deviation |
| `CapExPSRSD%TTM` | Capital expenditures divided by shares outstanding. | Five Year Relative Standard Deviation |
| `CapExPSRegEstANN` | Capital expenditures divided by shares outstanding. | Ten Year Regression Estimate |
| `CapExPSRegEstTTM` | Capital expenditures divided by shares outstanding. | Five Year Regression Estimate |
| `CapExPSRegGr%ANN` | Capital expenditures divided by shares outstanding. | Ten Year Regression Estimate |
| `CapExPSRegGr%TTM` | Capital expenditures divided by shares outstanding. | Five Year Regression Growth |
| `CapExPS3YAvg` | Capital expenditures divided by shares outstanding. | Three Year Average |
| `CapExPS5YAvg` | Capital expenditures divided by shares outstanding. | Five Year Average |

#### Cash Flow Per Share

| Factor | Description | Period |
|---|---|---|
| `CashFlPSQ` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Latest Quarter |
| `CashFlPSPQ` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Previous Quarter |
| `CashFlPSPYQ` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Previous Quarter 1 Year Ago |
| `CashFlPSTTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Trailing 12 Months |
| `CashFlPSPTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Previous Trailing 12 Months |
| `CashFlPSA` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Latest Year |
| `CashFlPSPY` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Previous Year |
| `CashFlPSGr%PQ` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Q vs Previous Q Growth |
| `CashFlPSGr%PYQ` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Q vs 1 year ago Q Growth |
| `CashFlPSGr%TTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Trailing Twelve Months Growth |
| `CashFlPSGr%PQTTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `CashFlPSGr%A` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Growth Annual |
| `CashFlPSGr%3Y` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Three Year Annualized Growth |
| `CashFlPSGr%5Y` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Five Year Annualized Growth |
| `CashFlPSGr%10Y` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Ten Year Annualized Growth |
| `CashFlPSRSD%ANN` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Ten Year Relative Standard Deviation |
| `CashFlPSRSD%TTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Five Year Relative Standard Deviation |
| `CashFlPSRegEstANN` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Ten Year Regression Estimate |
| `CashFlPSRegEstTTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Five Year Regression Estimate |
| `CashFlPSRegGr%ANN` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Ten Year Regression Estimate |
| `CashFlPSRegGr%TTM` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Five Year Regression Growth |
| `CashFlPS3YAvg` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Three Year Average |
| `CashFlPS5YAvg` | Cash Flow / Fully-Diluted Average Shares Outstanding. | Five Year Average |

#### Cash Per Share

| Factor | Description | Period |
|---|---|---|
| `CashPSQ` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Latest Quarter |
| `CashPSPQ` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Previous Quarter |
| `CashPSPYQ` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Previous Quarter 1 Year Ago |
| `CashPSTTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Trailing 12 Months |
| `CashPSPTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Previous Trailing 12 Months |
| `CashPSA` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Latest Year |
| `CashPSPY` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Previous Year |
| `CashPSGr%PQ` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Q vs Previous Q Growth |
| `CashPSGr%PYQ` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Q vs 1 year ago Q Growth |
| `CashPSGr%TTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Trailing Twelve Months Growth |
| `CashPSGr%PQTTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `CashPSGr%A` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Growth Annual |
| `CashPSGr%3Y` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Three Year Annualized Growth |
| `CashPSGr%5Y` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Five Year Annualized Growth |
| `CashPSGr%10Y` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Ten Year Annualized Growth |
| `CashPSRSD%ANN` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Ten Year Relative Standard Deviation |
| `CashPSRSD%TTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Five Year Relative Standard Deviation |
| `CashPSRegEstANN` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Ten Year Regression Estimate |
| `CashPSRegEstTTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Five Year Regression Estimate |
| `CashPSRegGr%ANN` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Ten Year Regression Estimate |
| `CashPSRegGr%TTM` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Five Year Regression Growth |
| `CashPS3YAvg` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Three Year Average |
| `CashPS5YAvg` | Total cash plus short-term investments divided by fully-diluted shares outstanding. | Five Year Average |

#### Earnings Per Share (EPS) Excl Xor

| Factor | Description | Period |
|---|---|---|
| `EPSExclXorQ` | Earnings per share without extraordinary expenses. | Latest Quarter |
| `EPSExclXorPQ` | Earnings per share without extraordinary expenses. | Previous Quarter |
| `EPSExclXorPYQ` | Earnings per share without extraordinary expenses. | Previous Quarter 1 Year Ago |
| `EPSExclXorTTM` | Earnings per share without extraordinary expenses. | Trailing 12 Months |
| `EPSExclXorPTM` | Earnings per share without extraordinary expenses. | Previous Trailing 12 Months |
| `EPSExclXorA` | Earnings per share without extraordinary expenses. | Latest Year |
| `EPSExclXorPY` | Earnings per share without extraordinary expenses. | Previous Year |
| `EPSExclXorGr%PQ` | Earnings per share without extraordinary expenses. | Q vs Previous Q Growth |
| `EPSExclXorGr%PYQ` | Earnings per share without extraordinary expenses. | Q vs 1 year ago Q Growth |
| `EPSExclXorGr%TTM` | Earnings per share without extraordinary expenses. | Trailing Twelve Months Growth |
| `EPSExclXorGr%PQTTM` | Earnings per share without extraordinary expenses. | Trailing Twelve Months Growth 1Q Ago |
| `EPSExclXorGr%A` | Earnings per share without extraordinary expenses. | Growth Annual |
| `EPSExclXorGr%3Y` | Earnings per share without extraordinary expenses. | Three Year Annualized Growth |
| `EPSExclXorGr%5Y` | Earnings per share without extraordinary expenses. | Five Year Annualized Growth |
| `EPSExclXorGr%10Y` | Earnings per share without extraordinary expenses. | Ten Year Annualized Growth |
| `EPSExclXorRSD%ANN` | Earnings per share without extraordinary expenses. | Ten Year Relative Standard Deviation |
| `EPSExclXorRSD%TTM` | Earnings per share without extraordinary expenses. | Five Year Relative Standard Deviation |
| `EPSExclXorRegEstANN` | Earnings per share without extraordinary expenses. | Ten Year Regression Estimate |
| `EPSExclXorRegEstTTM` | Earnings per share without extraordinary expenses. | Five Year Regression Estimate |
| `EPSExclXorRegGr%ANN` | Earnings per share without extraordinary expenses. | Ten Year Regression Estimate |
| `EPSExclXorRegGr%TTM` | Earnings per share without extraordinary expenses. | Five Year Regression Growth |
| `EPSExclXor3YAvg` | Earnings per share without extraordinary expenses. | Three Year Average |
| `EPSExclXor5YAvg` | Earnings per share without extraordinary expenses. | Five Year Average |

#### Earnings Per Share (EPS) Incl Xor

| Factor | Description | Period |
|---|---|---|
| `EPSInclXorQ` | Earnings per share with all expenses including extraordinary items. | Latest Quarter |
| `EPSInclXorPQ` | Earnings per share with all expenses including extraordinary items. | Previous Quarter |
| `EPSInclXorPYQ` | Earnings per share with all expenses including extraordinary items. | Previous Quarter 1 Year Ago |
| `EPSInclXorTTM` | Earnings per share with all expenses including extraordinary items. | Trailing 12 Months |
| `EPSInclXorPTM` | Earnings per share with all expenses including extraordinary items. | Previous Trailing 12 Months |
| `EPSInclXorA` | Earnings per share with all expenses including extraordinary items. | Latest Year |
| `EPSInclXorPY` | Earnings per share with all expenses including extraordinary items. | Previous Year |
| `EPSInclXorGr%PQ` | Earnings per share with all expenses including extraordinary items. | Q vs Previous Q Growth |
| `EPSInclXorGr%PYQ` | Earnings per share with all expenses including extraordinary items. | Q vs 1 year ago Q Growth |
| `EPSInclXorGr%TTM` | Earnings per share with all expenses including extraordinary items. | Trailing Twelve Months Growth |
| `EPSInclXorGr%PQTTM` | Earnings per share with all expenses including extraordinary items. | Trailing Twelve Months Growth 1Q Ago |
| `EPSInclXorGr%A` | Earnings per share with all expenses including extraordinary items. | Growth Annual |
| `EPSInclXorGr%3Y` | Earnings per share with all expenses including extraordinary items. | Three Year Annualized Growth |
| `EPSInclXorGr%5Y` | Earnings per share with all expenses including extraordinary items. | Five Year Annualized Growth |
| `EPSInclXorGr%10Y` | Earnings per share with all expenses including extraordinary items. | Ten Year Annualized Growth |
| `EPSInclXorRSD%ANN` | Earnings per share with all expenses including extraordinary items. | Ten Year Relative Standard Deviation |
| `EPSInclXorRSD%TTM` | Earnings per share with all expenses including extraordinary items. | Five Year Relative Standard Deviation |
| `EPSInclXorRegEstANN` | Earnings per share with all expenses including extraordinary items. | Ten Year Regression Estimate |
| `EPSInclXorRegEstTTM` | Earnings per share with all expenses including extraordinary items. | Five Year Regression Estimate |
| `EPSInclXorRegGr%ANN` | Earnings per share with all expenses including extraordinary items. | Ten Year Regression Estimate |
| `EPSInclXorRegGr%TTM` | Earnings per share with all expenses including extraordinary items. | Five Year Regression Growth |
| `EPSInclXor3YAvg` | Earnings per share with all expenses including extraordinary items. | Three Year Average |
| `EPSInclXor5YAvg` | Earnings per share with all expenses including extraordinary items. | Five Year Average |

#### EBITDA Per Share

| Factor | Description | Period |
|---|---|---|
| `EBITDAPSQ` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Latest Quarter |
| `EBITDAPSPQ` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Previous Quarter |
| `EBITDAPSPYQ` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Previous Quarter 1 Year Ago |
| `EBITDAPSTTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Trailing 12 Months |
| `EBITDAPSPTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Previous Trailing 12 Months |
| `EBITDAPSA` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Latest Year |
| `EBITDAPSPY` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Previous Year |
| `EBITDAPSGr%PQ` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Q vs Previous Q Growth |
| `EBITDAPSGr%PYQ` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Q vs 1 year ago Q Growth |
| `EBITDAPSGr%TTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Trailing Twelve Months Growth |
| `EBITDAPSGr%PQTTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Trailing Twelve Months Growth 1Q Ago |
| `EBITDAPSGr%A` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Growth Annual |
| `EBITDAPSGr%3Y` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Three Year Annualized Growth |
| `EBITDAPSGr%5Y` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Five Year Annualized Growth |
| `EBITDAPSGr%10Y` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Ten Year Annualized Growth |
| `EBITDAPSRSD%ANN` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Ten Year Relative Standard Deviation |
| `EBITDAPSRSD%TTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Five Year Relative Standard Deviation |
| `EBITDAPSRegEstANN` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Ten Year Regression Estimate |
| `EBITDAPSRegEstTTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Five Year Regression Estimate |
| `EBITDAPSRegGr%ANN` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Ten Year Regression Estimate |
| `EBITDAPSRegGr%TTM` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Five Year Regression Growth |
| `EBITDAPS3YAvg` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Three Year Average |
| `EBITDAPS5YAvg` | Earnings before interest, taxes, depreciation and amortization on a per-share basis. | Five Year Average |

#### Free Cash Flow Per Share

| Factor | Description | Period |
|---|---|---|
| `FCFPSQ` | Free cash flow divided by fully-diluted average shares outstanding. | Latest Quarter |
| `FCFPSPQ` | Free cash flow divided by fully-diluted average shares outstanding. | Previous Quarter |
| `FCFPSPYQ` | Free cash flow divided by fully-diluted average shares outstanding. | Previous Quarter 1 Year Ago |
| `FCFPSTTM` | Free cash flow divided by fully-diluted average shares outstanding. | Trailing 12 Months |
| `FCFPSPTM` | Free cash flow divided by fully-diluted average shares outstanding. | Previous Trailing 12 Months |
| `FCFPSA` | Free cash flow divided by fully-diluted average shares outstanding. | Latest Year |
| `FCFPSPY` | Free cash flow divided by fully-diluted average shares outstanding. | Previous Year |
| `FCFPSGr%PQ` | Free cash flow divided by fully-diluted average shares outstanding. | Q vs Previous Q Growth |
| `FCFPSGr%PYQ` | Free cash flow divided by fully-diluted average shares outstanding. | Q vs 1 year ago Q Growth |
| `FCFPSGr%TTM` | Free cash flow divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth |
| `FCFPSGr%PQTTM` | Free cash flow divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `FCFPSGr%A` | Free cash flow divided by fully-diluted average shares outstanding. | Growth Annual |
| `FCFPSGr%3Y` | Free cash flow divided by fully-diluted average shares outstanding. | Three Year Annualized Growth |
| `FCFPSGr%5Y` | Free cash flow divided by fully-diluted average shares outstanding. | Five Year Annualized Growth |
| `FCFPSGr%10Y` | Free cash flow divided by fully-diluted average shares outstanding. | Ten Year Annualized Growth |
| `FCFPSRSD%ANN` | Free cash flow divided by fully-diluted average shares outstanding. | Ten Year Relative Standard Deviation |
| `FCFPSRSD%TTM` | Free cash flow divided by fully-diluted average shares outstanding. | Five Year Relative Standard Deviation |
| `FCFPSRegEstANN` | Free cash flow divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `FCFPSRegEstTTM` | Free cash flow divided by fully-diluted average shares outstanding. | Five Year Regression Estimate |
| `FCFPSRegGr%ANN` | Free cash flow divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `FCFPSRegGr%TTM` | Free cash flow divided by fully-diluted average shares outstanding. | Five Year Regression Growth |
| `FCFPS3YAvg` | Free cash flow divided by fully-diluted average shares outstanding. | Three Year Average |
| `FCFPS5YAvg` | Free cash flow divided by fully-diluted average shares outstanding. | Five Year Average |

#### Net Free Cash Flow Per Share

| Factor | Description | Period |
|---|---|---|
| `NetFCFPSQ` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Latest Quarter |
| `NetFCFPSPQ` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Previous Quarter |
| `NetFCFPSPYQ` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Previous Quarter 1 Year Ago |
| `NetFCFPSTTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Trailing 12 Months |
| `NetFCFPSPTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Previous Trailing 12 Months |
| `NetFCFPSA` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Latest Year |
| `NetFCFPSPY` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Previous Year |
| `NetFCFPSGr%PQ` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Q vs Previous Q Growth |
| `NetFCFPSGr%PYQ` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Q vs 1 year ago Q Growth |
| `NetFCFPSGr%TTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth |
| `NetFCFPSGr%PQTTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `NetFCFPSGr%A` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Growth Annual |
| `NetFCFPSGr%3Y` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Three Year Annualized Growth |
| `NetFCFPSGr%5Y` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Five Year Annualized Growth |
| `NetFCFPSGr%10Y` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Ten Year Annualized Growth |
| `NetFCFPSRSD%ANN` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Ten Year Relative Standard Deviation |
| `NetFCFPSRSD%TTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Five Year Relative Standard Deviation |
| `NetFCFPSRegEstANN` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `NetFCFPSRegEstTTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Five Year Regression Estimate |
| `NetFCFPSRegGr%ANN` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `NetFCFPSRegGr%TTM` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Five Year Regression Growth |
| `NetFCFPS3YAvg` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Three Year Average |
| `NetFCFPS5YAvg` | Net Free Cash Flow per Share is quarterly net free cash flow divided by fully-diluted average shares outstanding. | Five Year Average |

#### Operating Cashflow Per Share

| Factor | Description | Period |
|---|---|---|
| `OCFPSQ` | Operating Cashflow Per Share. | Latest Quarter |
| `OCFPSPQ` | Operating Cashflow Per Share. | Previous Quarter |
| `OCFPSPYQ` | Operating Cashflow Per Share. | Previous Quarter 1 Year Ago |
| `OCFPSTTM` | Operating Cashflow Per Share. | Trailing 12 Months |
| `OCFPSPTM` | Operating Cashflow Per Share. | Previous Trailing 12 Months |
| `OCFPSA` | Operating Cashflow Per Share. | Latest Year |
| `OCFPSPY` | Operating Cashflow Per Share. | Previous Year |
| `OCFPSGr%PQ` | Operating Cashflow Per Share. | Q vs Previous Q Growth |
| `OCFPSGr%PYQ` | Operating Cashflow Per Share. | Q vs 1 year ago Q Growth |
| `OCFPSGr%TTM` | Operating Cashflow Per Share. | Trailing Twelve Months Growth |
| `OCFPSGr%PQTTM` | Operating Cashflow Per Share. | Trailing Twelve Months Growth 1Q Ago |
| `OCFPSGr%A` | Operating Cashflow Per Share. | Growth Annual |
| `OCFPSGr%3Y` | Operating Cashflow Per Share. | Three Year Annualized Growth |
| `OCFPSGr%5Y` | Operating Cashflow Per Share. | Five Year Annualized Growth |
| `OCFPSGr%10Y` | Operating Cashflow Per Share. | Ten Year Annualized Growth |
| `OCFPSRSD%ANN` | Operating Cashflow Per Share. | Ten Year Relative Standard Deviation |
| `OCFPSRSD%TTM` | Operating Cashflow Per Share. | Five Year Relative Standard Deviation |
| `OCFPSRegEstANN` | Operating Cashflow Per Share. | Ten Year Regression Estimate |
| `OCFPSRegEstTTM` | Operating Cashflow Per Share. | Five Year Regression Estimate |
| `OCFPSRegGr%ANN` | Operating Cashflow Per Share. | Ten Year Regression Estimate |
| `OCFPSRegGr%TTM` | Operating Cashflow Per Share. | Five Year Regression Growth |
| `OCFPS3YAvg` | Operating Cashflow Per Share. | Three Year Average |
| `OCFPS5YAvg` | Operating Cashflow Per Share. | Five Year Average |

#### Operating Income Per Share

| Factor | Description | Period |
|---|---|---|
| `OpIncPSQ` | Operating income divided by fully-diluted average shares outstanding. | Latest Quarter |
| `OpIncPSPQ` | Operating income divided by fully-diluted average shares outstanding. | Previous Quarter |
| `OpIncPSPYQ` | Operating income divided by fully-diluted average shares outstanding. | Previous Quarter 1 Year Ago |
| `OpIncPSTTM` | Operating income divided by fully-diluted average shares outstanding. | Trailing 12 Months |
| `OpIncPSPTM` | Operating income divided by fully-diluted average shares outstanding. | Previous Trailing 12 Months |
| `OpIncPSA` | Operating income divided by fully-diluted average shares outstanding. | Latest Year |
| `OpIncPSPY` | Operating income divided by fully-diluted average shares outstanding. | Previous Year |
| `OpIncPSGr%PQ` | Operating income divided by fully-diluted average shares outstanding. | Q vs Previous Q Growth |
| `OpIncPSGr%PYQ` | Operating income divided by fully-diluted average shares outstanding. | Q vs 1 year ago Q Growth |
| `OpIncPSGr%TTM` | Operating income divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth |
| `OpIncPSGr%PQTTM` | Operating income divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `OpIncPSGr%A` | Operating income divided by fully-diluted average shares outstanding. | Growth Annual |
| `OpIncPSGr%3Y` | Operating income divided by fully-diluted average shares outstanding. | Three Year Annualized Growth |
| `OpIncPSGr%5Y` | Operating income divided by fully-diluted average shares outstanding. | Five Year Annualized Growth |
| `OpIncPSGr%10Y` | Operating income divided by fully-diluted average shares outstanding. | Ten Year Annualized Growth |
| `OpIncPSRSD%ANN` | Operating income divided by fully-diluted average shares outstanding. | Ten Year Relative Standard Deviation |
| `OpIncPSRSD%TTM` | Operating income divided by fully-diluted average shares outstanding. | Five Year Relative Standard Deviation |
| `OpIncPSRegEstANN` | Operating income divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `OpIncPSRegEstTTM` | Operating income divided by fully-diluted average shares outstanding. | Five Year Regression Estimate |
| `OpIncPSRegGr%ANN` | Operating income divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `OpIncPSRegGr%TTM` | Operating income divided by fully-diluted average shares outstanding. | Five Year Regression Growth |
| `OpIncPS3YAvg` | Operating income divided by fully-diluted average shares outstanding. | Three Year Average |
| `OpIncPS5YAvg` | Operating income divided by fully-diluted average shares outstanding. | Five Year Average |

#### Sales (Revenues) Per Share

| Factor | Description | Period |
|---|---|---|
| `SalesPSQ` | Total revenue divided by fully-diluted average shares outstanding. | Latest Quarter |
| `SalesPSPQ` | Total revenue divided by fully-diluted average shares outstanding. | Previous Quarter |
| `SalesPSPYQ` | Total revenue divided by fully-diluted average shares outstanding. | Previous Quarter 1 Year Ago |
| `SalesPSTTM` | Total revenue divided by fully-diluted average shares outstanding. | Trailing 12 Months |
| `SalesPSPTM` | Total revenue divided by fully-diluted average shares outstanding. | Previous Trailing 12 Months |
| `SalesPSA` | Total revenue divided by fully-diluted average shares outstanding. | Latest Year |
| `SalesPSPY` | Total revenue divided by fully-diluted average shares outstanding. | Previous Year |
| `SalesPSGr%PQ` | Total revenue divided by fully-diluted average shares outstanding. | Q vs Previous Q Growth |
| `SalesPSGr%PYQ` | Total revenue divided by fully-diluted average shares outstanding. | Q vs 1 year ago Q Growth |
| `SalesPSGr%TTM` | Total revenue divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth |
| `SalesPSGr%PQTTM` | Total revenue divided by fully-diluted average shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `SalesPSGr%A` | Total revenue divided by fully-diluted average shares outstanding. | Growth Annual |
| `SalesPSGr%3Y` | Total revenue divided by fully-diluted average shares outstanding. | Three Year Annualized Growth |
| `SalesPSGr%5Y` | Total revenue divided by fully-diluted average shares outstanding. | Five Year Annualized Growth |
| `SalesPSGr%10Y` | Total revenue divided by fully-diluted average shares outstanding. | Ten Year Annualized Growth |
| `SalesPSRSD%ANN` | Total revenue divided by fully-diluted average shares outstanding. | Ten Year Relative Standard Deviation |
| `SalesPSRSD%TTM` | Total revenue divided by fully-diluted average shares outstanding. | Five Year Relative Standard Deviation |
| `SalesPSRegEstANN` | Total revenue divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `SalesPSRegEstTTM` | Total revenue divided by fully-diluted average shares outstanding. | Five Year Regression Estimate |
| `SalesPSRegGr%ANN` | Total revenue divided by fully-diluted average shares outstanding. | Ten Year Regression Estimate |
| `SalesPSRegGr%TTM` | Total revenue divided by fully-diluted average shares outstanding. | Five Year Regression Growth |
| `SalesPS3YAvg` | Total revenue divided by fully-diluted average shares outstanding. | Three Year Average |
| `SalesPS5YAvg` | Total revenue divided by fully-diluted average shares outstanding. | Five Year Average |


## Efficiency

### Functions

#### `AstTurn(offset, type[, NAHandling])`

This value is calculated as the revenues divided by the average total assets for the same period.

Formula:

AstTurn = Sales / avg ( AstTot )

NOTE: Quarterly values from Income & Cash flow statements are annualized to make the resulting factor more readily comparable with the 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depending on the actual number of days in the period).


#### `IncPerEmp(offset, type[, NAHandling])`

Income per Employee.


#### `InvTurn(offset, type[, NAHandling])`

This value measures how quickly the Inventory is sold. It is defined as Cost of Goods Sold divided by Average Inventory for the same period. Average Inventory is the average of the Inventory at the beginning and the end of the quarter. 

Formula: CostG / Inventory

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).


#### `RecTurn(offset, type[, NAHandling])`

This is the ratio of Total Revenue divided by Average Accounts Receivables for the same period. 

IMPORTANT: Quarterly values from Income & Cashflow statements are annualized to make the resulting factor more readily comparable with 12 month factors. The annualization is done by multiplying the quarterly figures by approximately 4 (depends on the actual number of days in the period).


#### `SalesPerEmp(offset, type[, NAHandling])`

Sales Per Employee.


#### `SGA2GP(offset, type[, NAHandling])`

Selling General and Administrative costs to Gross Profit is a profitability ratio that assesses how much of the net revenues are absorbed by indirect costs. Companies that consistently spend under 30% of their Gross Profit on SG&A have a wide moat, and don't need to spend a lot on overhead to operate.


### Factor variants

#### Asset Turnover

| Factor | Description | Period |
|---|---|---|
| `AstTurnQ` | Revenue divided by the average total assets for the same period. | Latest Quarter |
| `AstTurnPQ` | Revenue divided by the average total assets for the same period. | Previous Quarter |
| `AstTurnPYQ` | Revenue divided by the average total assets for the same period. | Previous Quarter 1 Year Ago |
| `AstTurnTTM` | Revenue divided by the average total assets for the same period. | Trailing 12 Months |
| `AstTurnPTM` | Revenue divided by the average total assets for the same period. | Previous Trailing 12 Months |
| `AstTurnA` | Revenue divided by the average total assets for the same period. | Latest Year |
| `AstTurnPY` | Revenue divided by the average total assets for the same period. | Previous Year |
| `AstTurnGr%PQ` | Revenue divided by the average total assets for the same period. | Q vs Previous Q Growth |
| `AstTurnGr%PYQ` | Revenue divided by the average total assets for the same period. | Q vs 1 year ago Q Growth |
| `AstTurnGr%TTM` | Revenue divided by the average total assets for the same period. | Trailing Twelve Months Growth |
| `AstTurnGr%PQTTM` | Revenue divided by the average total assets for the same period. | Trailing Twelve Months Growth 1Q Ago |
| `AstTurnGr%A` | Revenue divided by the average total assets for the same period. | Growth Annual |
| `AstTurnGr%3Y` | Revenue divided by the average total assets for the same period. | Three Year Annualized Growth |
| `AstTurnGr%5Y` | Revenue divided by the average total assets for the same period. | Five Year Annualized Growth |
| `AstTurnGr%10Y` | Revenue divided by the average total assets for the same period. | Ten Year Annualized Growth |
| `AstTurnRSD%ANN` | Revenue divided by the average total assets for the same period. | Ten Year Relative Standard Deviation |
| `AstTurnRSD%TTM` | Revenue divided by the average total assets for the same period. | Five Year Relative Standard Deviation |
| `AstTurnRegEstANN` | Revenue divided by the average total assets for the same period. | Ten Year Regression Estimate |
| `AstTurnRegEstTTM` | Revenue divided by the average total assets for the same period. | Five Year Regression Estimate |
| `AstTurnRegGr%ANN` | Revenue divided by the average total assets for the same period. | Ten Year Regression Estimate |
| `AstTurnRegGr%TTM` | Revenue divided by the average total assets for the same period. | Five Year Regression Growth |
| `AstTurnPSQ` | Revenue divided by the average total assets for the same period. | Quarterly Per Share |
| `AstTurnPSA` | Revenue divided by the average total assets for the same period. | Annual Per Share |
| `AstTurn%SalesQ` | Revenue divided by the average total assets for the same period. | % of Quarterly Sales |
| `AstTurn%SalesA` | Revenue divided by the average total assets for the same period. | % of Annual Sales |
| `AstTurn%AssetsQ` | Revenue divided by the average total assets for the same period. | % of Quarterly Assets |
| `AstTurn%AssetsA` | Revenue divided by the average total assets for the same period. | % of Annual Assets |
| `AstTurn3YAvg` | Revenue divided by the average total assets for the same period. | Three Year Average |
| `AstTurn5YAvg` | Revenue divided by the average total assets for the same period. | Five Year Average |

#### Income Per Employee

| Factor | Description | Period |
|---|---|---|
| `IncPerEmpQ` | Income per Employee. | Latest Quarter |
| `IncPerEmpPQ` | Income per Employee. | Previous Quarter |
| `IncPerEmpPYQ` | Income per Employee. | Previous Quarter 1 Year Ago |
| `IncPerEmpTTM` | Income per Employee. | Trailing 12 Months |
| `IncPerEmpPTM` | Income per Employee. | Previous Trailing 12 Months |
| `IncPerEmpA` | Income per Employee. | Latest Year |
| `IncPerEmpPY` | Income per Employee. | Previous Year |
| `IncPerEmpGr%PQ` | Income per Employee. | Q vs Previous Q Growth |
| `IncPerEmpGr%PYQ` | Income per Employee. | Q vs 1 year ago Q Growth |
| `IncPerEmpGr%TTM` | Income per Employee. | Trailing Twelve Months Growth |
| `IncPerEmpGr%PQTTM` | Income per Employee. | Trailing Twelve Months Growth 1Q Ago |
| `IncPerEmpGr%A` | Income per Employee. | Growth Annual |
| `IncPerEmpGr%3Y` | Income per Employee. | Three Year Annualized Growth |
| `IncPerEmpGr%5Y` | Income per Employee. | Five Year Annualized Growth |
| `IncPerEmpGr%10Y` | Income per Employee. | Ten Year Annualized Growth |
| `IncPerEmpRSD%ANN` | Income per Employee. | Ten Year Relative Standard Deviation |
| `IncPerEmpRSD%TTM` | Income per Employee. | Five Year Relative Standard Deviation |
| `IncPerEmpRegEstANN` | Income per Employee. | Ten Year Regression Estimate |
| `IncPerEmpRegEstTTM` | Income per Employee. | Five Year Regression Estimate |
| `IncPerEmpRegGr%ANN` | Income per Employee. | Ten Year Regression Estimate |
| `IncPerEmpRegGr%TTM` | Income per Employee. | Five Year Regression Growth |
| `IncPerEmp3YAvg` | Income per Employee. | Three Year Average |
| `IncPerEmp5YAvg` | Income per Employee. | Five Year Average |

#### Inventory Turnover

| Factor | Description | Period |
|---|---|---|
| `InvTurnQ` | Measure of how quickly inventory is sold. | Latest Quarter |
| `InvTurnPQ` | Measure of how quickly inventory is sold. | Previous Quarter |
| `InvTurnPYQ` | Measure of how quickly inventory is sold. | Previous Quarter 1 Year Ago |
| `InvTurnTTM` | Measure of how quickly inventory is sold. | Trailing 12 Months |
| `InvTurnPTM` | Measure of how quickly inventory is sold. | Previous Trailing 12 Months |
| `InvTurnA` | Measure of how quickly inventory is sold. | Latest Year |
| `InvTurnPY` | Measure of how quickly inventory is sold. | Previous Year |
| `InvTurnGr%PQ` | Measure of how quickly inventory is sold. | Q vs Previous Q Growth |
| `InvTurnGr%PYQ` | Measure of how quickly inventory is sold. | Q vs 1 year ago Q Growth |
| `InvTurnGr%TTM` | Measure of how quickly inventory is sold. | Trailing Twelve Months Growth |
| `InvTurnGr%PQTTM` | Measure of how quickly inventory is sold. | Trailing Twelve Months Growth 1Q Ago |
| `InvTurnGr%A` | Measure of how quickly inventory is sold. | Growth Annual |
| `InvTurnGr%3Y` | Measure of how quickly inventory is sold. | Three Year Annualized Growth |
| `InvTurnGr%5Y` | Measure of how quickly inventory is sold. | Five Year Annualized Growth |
| `InvTurnGr%10Y` | Measure of how quickly inventory is sold. | Ten Year Annualized Growth |
| `InvTurnRSD%ANN` | Measure of how quickly inventory is sold. | Ten Year Relative Standard Deviation |
| `InvTurnRSD%TTM` | Measure of how quickly inventory is sold. | Five Year Relative Standard Deviation |
| `InvTurnRegEstANN` | Measure of how quickly inventory is sold. | Ten Year Regression Estimate |
| `InvTurnRegEstTTM` | Measure of how quickly inventory is sold. | Five Year Regression Estimate |
| `InvTurnRegGr%ANN` | Measure of how quickly inventory is sold. | Ten Year Regression Estimate |
| `InvTurnRegGr%TTM` | Measure of how quickly inventory is sold. | Five Year Regression Growth |
| `InvTurnPSQ` | Measure of how quickly inventory is sold. | Quarterly Per Share |
| `InvTurnPSA` | Measure of how quickly inventory is sold. | Annual Per Share |
| `InvTurn%SalesQ` | Measure of how quickly inventory is sold. | % of Quarterly Sales |
| `InvTurn%SalesA` | Measure of how quickly inventory is sold. | % of Annual Sales |
| `InvTurn%AssetsQ` | Measure of how quickly inventory is sold. | % of Quarterly Assets |
| `InvTurn%AssetsA` | Measure of how quickly inventory is sold. | % of Annual Assets |
| `InvTurn3YAvg` | Measure of how quickly inventory is sold. | Three Year Average |
| `InvTurn5YAvg` | Measure of how quickly inventory is sold. | Five Year Average |

#### Receivables Turnover

| Factor | Description | Period |
|---|---|---|
| `RecTurnQ` | Measure of how efficiently a company collects receivables. | Latest Quarter |
| `RecTurnPQ` | Measure of how efficiently a company collects receivables. | Previous Quarter |
| `RecTurnPYQ` | Measure of how efficiently a company collects receivables. | Previous Quarter 1 Year Ago |
| `RecTurnTTM` | Measure of how efficiently a company collects receivables. | Trailing 12 Months |
| `RecTurnPTM` | Measure of how efficiently a company collects receivables. | Previous Trailing 12 Months |
| `RecTurnA` | Measure of how efficiently a company collects receivables. | Latest Year |
| `RecTurnPY` | Measure of how efficiently a company collects receivables. | Previous Year |
| `RecTurnGr%PQ` | Measure of how efficiently a company collects receivables. | Q vs Previous Q Growth |
| `RecTurnGr%PYQ` | Measure of how efficiently a company collects receivables. | Q vs 1 year ago Q Growth |
| `RecTurnGr%TTM` | Measure of how efficiently a company collects receivables. | Trailing Twelve Months Growth |
| `RecTurnGr%PQTTM` | Measure of how efficiently a company collects receivables. | Trailing Twelve Months Growth 1Q Ago |
| `RecTurnGr%A` | Measure of how efficiently a company collects receivables. | Growth Annual |
| `RecTurnGr%3Y` | Measure of how efficiently a company collects receivables. | Three Year Annualized Growth |
| `RecTurnGr%5Y` | Measure of how efficiently a company collects receivables. | Five Year Annualized Growth |
| `RecTurnGr%10Y` | Measure of how efficiently a company collects receivables. | Ten Year Annualized Growth |
| `RecTurnRSD%ANN` | Measure of how efficiently a company collects receivables. | Ten Year Relative Standard Deviation |
| `RecTurnRSD%TTM` | Measure of how efficiently a company collects receivables. | Five Year Relative Standard Deviation |
| `RecTurnRegEstANN` | Measure of how efficiently a company collects receivables. | Ten Year Regression Estimate |
| `RecTurnRegEstTTM` | Measure of how efficiently a company collects receivables. | Five Year Regression Estimate |
| `RecTurnRegGr%ANN` | Measure of how efficiently a company collects receivables. | Ten Year Regression Estimate |
| `RecTurnRegGr%TTM` | Measure of how efficiently a company collects receivables. | Five Year Regression Growth |
| `RecTurnPSQ` | Measure of how efficiently a company collects receivables. | Quarterly Per Share |
| `RecTurnPSA` | Measure of how efficiently a company collects receivables. | Annual Per Share |
| `RecTurn%SalesQ` | Measure of how efficiently a company collects receivables. | % of Quarterly Sales |
| `RecTurn%SalesA` | Measure of how efficiently a company collects receivables. | % of Annual Sales |
| `RecTurn%AssetsQ` | Measure of how efficiently a company collects receivables. | % of Quarterly Assets |
| `RecTurn%AssetsA` | Measure of how efficiently a company collects receivables. | % of Annual Assets |
| `RecTurn3YAvg` | Measure of how efficiently a company collects receivables. | Three Year Average |
| `RecTurn5YAvg` | Measure of how efficiently a company collects receivables. | Five Year Average |

#### Sales Per Employee

| Factor | Description | Period |
|---|---|---|
| `SalesPerEmpQ` | Sales Per Employee. | Latest Quarter |
| `SalesPerEmpPQ` | Sales Per Employee. | Previous Quarter |
| `SalesPerEmpPYQ` | Sales Per Employee. | Previous Quarter 1 Year Ago |
| `SalesPerEmpTTM` | Sales Per Employee. | Trailing 12 Months |
| `SalesPerEmpPTM` | Sales Per Employee. | Previous Trailing 12 Months |
| `SalesPerEmpA` | Sales Per Employee. | Latest Year |
| `SalesPerEmpPY` | Sales Per Employee. | Previous Year |
| `SalesPerEmpGr%PQ` | Sales Per Employee. | Q vs Previous Q Growth |
| `SalesPerEmpGr%PYQ` | Sales Per Employee. | Q vs 1 year ago Q Growth |
| `SalesPerEmpGr%TTM` | Sales Per Employee. | Trailing Twelve Months Growth |
| `SalesPerEmpGr%PQTTM` | Sales Per Employee. | Trailing Twelve Months Growth 1Q Ago |
| `SalesPerEmpGr%A` | Sales Per Employee. | Growth Annual |
| `SalesPerEmpGr%3Y` | Sales Per Employee. | Three Year Annualized Growth |
| `SalesPerEmpGr%5Y` | Sales Per Employee. | Five Year Annualized Growth |
| `SalesPerEmpGr%10Y` | Sales Per Employee. | Ten Year Annualized Growth |
| `SalesPerEmpRSD%ANN` | Sales Per Employee. | Ten Year Relative Standard Deviation |
| `SalesPerEmpRSD%TTM` | Sales Per Employee. | Five Year Relative Standard Deviation |
| `SalesPerEmpRegEstANN` | Sales Per Employee. | Ten Year Regression Estimate |
| `SalesPerEmpRegEstTTM` | Sales Per Employee. | Five Year Regression Estimate |
| `SalesPerEmpRegGr%ANN` | Sales Per Employee. | Ten Year Regression Estimate |
| `SalesPerEmpRegGr%TTM` | Sales Per Employee. | Five Year Regression Growth |
| `SalesPerEmp3YAvg` | Sales Per Employee. | Three Year Average |
| `SalesPerEmp5YAvg` | Sales Per Employee. | Five Year Average |

#### Sales, General and Administrative Expense to Gross Profit

| Factor | Description | Period |
|---|---|---|
| `SGA2GPQ` | Indirect costs as percentage of gross profit. | Latest Quarter |
| `SGA2GPPQ` | Indirect costs as percentage of gross profit. | Previous Quarter |
| `SGA2GPPYQ` | Indirect costs as percentage of gross profit. | Previous Quarter 1 Year Ago |
| `SGA2GPTTM` | Indirect costs as percentage of gross profit. | Trailing 12 Months |
| `SGA2GPPTM` | Indirect costs as percentage of gross profit. | Previous Trailing 12 Months |
| `SGA2GPA` | Indirect costs as percentage of gross profit. | Latest Year |
| `SGA2GPPY` | Indirect costs as percentage of gross profit. | Previous Year |
| `SGA2GPGr%PQ` | Indirect costs as percentage of gross profit. | Q vs Previous Q Growth |
| `SGA2GPGr%PYQ` | Indirect costs as percentage of gross profit. | Q vs 1 year ago Q Growth |
| `SGA2GPGr%TTM` | Indirect costs as percentage of gross profit. | Trailing Twelve Months Growth |
| `SGA2GPGr%PQTTM` | Indirect costs as percentage of gross profit. | Trailing Twelve Months Growth 1Q Ago |
| `SGA2GPGr%A` | Indirect costs as percentage of gross profit. | Growth Annual |
| `SGA2GPGr%3Y` | Indirect costs as percentage of gross profit. | Three Year Annualized Growth |
| `SGA2GPGr%5Y` | Indirect costs as percentage of gross profit. | Five Year Annualized Growth |
| `SGA2GPGr%10Y` | Indirect costs as percentage of gross profit. | Ten Year Annualized Growth |
| `SGA2GPRSD%ANN` | Indirect costs as percentage of gross profit. | Ten Year Relative Standard Deviation |
| `SGA2GPRSD%TTM` | Indirect costs as percentage of gross profit. | Five Year Relative Standard Deviation |
| `SGA2GPRegEstANN` | Indirect costs as percentage of gross profit. | Ten Year Regression Estimate |
| `SGA2GPRegEstTTM` | Indirect costs as percentage of gross profit. | Five Year Regression Estimate |
| `SGA2GPRegGr%ANN` | Indirect costs as percentage of gross profit. | Ten Year Regression Estimate |
| `SGA2GPRegGr%TTM` | Indirect costs as percentage of gross profit. | Five Year Regression Growth |
| `SGA2GPPSQ` | Indirect costs as percentage of gross profit. | Quarterly Per Share |
| `SGA2GPPSA` | Indirect costs as percentage of gross profit. | Annual Per Share |
| `SGA2GP%SalesQ` | Indirect costs as percentage of gross profit. | % of Quarterly Sales |
| `SGA2GP%SalesA` | Indirect costs as percentage of gross profit. | % of Annual Sales |
| `SGA2GP%AssetsQ` | Indirect costs as percentage of gross profit. | % of Quarterly Assets |
| `SGA2GP%AssetsA` | Indirect costs as percentage of gross profit. | % of Annual Assets |
| `SGA2GP3YAvg` | Indirect costs as percentage of gross profit. | Three Year Average |
| `SGA2GP5YAvg` | Indirect costs as percentage of gross profit. | Five Year Average |


## Financial Strength

### Functions

#### `CurRatio(offset, type[, NAHandling])`

This is the ratio of Total Current Assets for the period divided by Total Current Liabilities for the same period.


#### `DbtS2NI(offset, type[, NAHandling])`

This ratio is calculated as follow

DbtS2NI = IntExp / NetIncBXor


#### `DepAmort2GP(offset, type[, NAHandling])`

The Depreciation & Amortization to Gross Profit Ratio is a financial metric used to evaluate the proportion of a company's gross profit consumed by depreciation and amortization expenses. Here's a breakdown of this concept:

A higher ratio indicates that a significant portion of the gross profit is being consumed by depreciation and amortization expenses. This might be typical for capital-intensive industries like manufacturing or telecommunications. A lower ratio suggests that depreciation and amortization are a smaller portion of gross profit, which might be expected in less capital-intensive industries like software or services.

This ratio can help understand how much of a company's gross earnings are being allocated to account for the aging and use of its fixed and intangible assets. It can also provide insights into the company's investment in assets and its strategy regarding capital expenditure.

Formula

DepAmort2GP = DepAmort/ GrossProfit


#### `IntCov(offset, type[, NAHandling])`

This ratio is calculated as follow

IntCov = OpInc / IntExp


#### `DbtLT2Ast(offset, type[, NAHandling])`

This ratio is the Total Long Term Debt as for the period divided by the Total Assets for the same period.


#### `DbtLT2Cap(offset, type[, NAHandling])`

This ratio is the Total Long Term Debt for the period divided by Total Capital for the same period. Total Capital is the sum of Short Term Debt, the Current Portion of Long Term Debt, Long Term Debt, and Total Common Equity.


#### `DbtLT2Eq(offset, type[, NAHandling])`

This is the Total Long Term Debt for the period divided by Total Common Equity for the same period.


#### `NI2CapEx(offset, type[, NAHandling])`

Net income to Capital Expenditures is an efficiency ratio that assesses how much of the company profits are reinvested into capital expenditure. For companies with average to low growth rates, a high Net Income to CapEx indicates that a higher portion of profits can be rewarded to shareholders or used to reduce debt, rather than being tied up to maintain the cash needs of a business.


#### `PayRatio(offset, type[, NAHandling])`

PayRatio, known as the dividend payout ratio, is the amount of dividends paid to stockholders relative to the amount of total net income of a company. The amount that is not paid out in dividends to stockholders is held by the company for growth. The amount that is kept by the company is called retained earnings Typically, PayRatio of 50% or less is regarded as adequate (which would mean that the company is retaining as much cash as it is paying out). At 100% or more, the company is distributing all of its earnings as dividends or even dipping into reserves from previous years.

Formula:

PayRatio = 100 * DivPaid / NetIncBXor

Evauates to NA if NetIncBXor is negative or DivPaid is 0 or negative

It's calculated as Total Dividends divided by Income Before Extraordinary Items for the period, multiplied by 100 to express the number in percentage points. Total dividends, in this case, includes dividends across all share classes and preferred shares. It does not include the value of non-cash dividends like stock dividends that were paid during the period, but it does otherwise include special dividends.

The 5-year average payout ratio is calculated by taking the payout ratios for each of the last five fiscal years, from the annual data feed, and averaging them.


#### `QuickRatio(offset, type[, NAHandling])`

Also known as the Acid Test Ratio, this ratio is defined as Current Assets less Inventory for the period divided by the Total Current Liabilities for the same period.


#### `Retn%(offset, type[, NAHandling])`

The Retention Ratio is the percentage of earnings kept by the company for reinvestment rather than distributed as dividends. Shows how much profit is retained for growth, expansion, or strengthening the balance sheet.

Formula: 100 - Payout Ratio


#### `DbtTot2Ast(offset, type[, NAHandling])`

This ratio is the Total Debt for the period divided by Total Assets for the same period. Total Debt is the sum of Short Term Debt, the Current Portion of Long Term Debt and Long Term Debt.


#### `DbtTot2Cap(offset, type[, NAHandling])`

This ratio is Total Debt divided by Total Capital. Total Capital is the sum of Short Term Debt, Current Portion of Long Term Debt, Long Term Debt, Capitalized Lease Obligations and Total Stockholder's Equity.


#### `DbtTot2Eq(offset, type[, NAHandling])`

This ratio is Total Debt for the period divided by Total Common Equity for the same period.


### Factors with detailed definitions

#### `PayRatio5Y`

PayRatio, known as the dividend payout ratio, is the amount of dividends paid to stockholders relative to the amount of total net income of a company. The amount that is not paid out in dividends to stockholders is held by the company for growth. The amount that is kept by the company is called retained earnings Typically, PayRatio of 50% or less is regarded as adequate (which would mean that the company is retaining as much cash as it is paying out). At 100% or more, the company is distributing all of its earnings as dividends or even dipping into reserves from previous years.

Formula:

PayRatio = 100 * DivPaid / NetIncBXor

Evauates to NA if NetIncBXor is negative or DivPaid is 0 or negative

It's calculated as Total Dividends divided by Income Before Extraordinary Items for the period, multiplied by 100 to express the number in percentage points. Total dividends, in this case, includes dividends across all share classes and preferred shares. It does not include the value of non-cash dividends like stock dividends that were paid during the period, but it does otherwise include special dividends.

The 5-year average payout ratio is calculated by taking the payout ratios for each of the last five fiscal years, from the annual data feed, and averaging them.

*Period: 5 Years*


#### `WCapPS2PrA`

This is Working Capital Per Share divided by the current price.

Working Capital Per Share is defined as the difference between Current Assets and Current Liabilities for the most recent fiscal year divided by the Balance Sheet Shares Outstanding at the end of that same period.

Many financial companies -- particularly banks -- do not report working capital items, so users should expect this item to be NA for those companies or industries.

*Period: Latest Year*


#### `WCapPS2PrQ`

This is Working Capital Per Share divided by the current Price. 

Working Capital Per Share is defined as the difference between Current Assets and Current Liabilities for the most recent fiscal quarter divided by the Balance Sheet Shares Outstanding at the end of that same period.

Many financial companies -- particularly banks -- do not report working capital items, so users should expect this item to be NA for those companies or industries.

*Period: Latest Quarter*


### Factor variants

#### Current Ratio

| Factor | Description | Period |
|---|---|---|
| `CurRatioQ` | Measures company's ability to pay short-term obligations using short-term assets. | Latest Quarter |
| `CurRatioPQ` | Measures company's ability to pay short-term obligations using short-term assets. | Previous Quarter |
| `CurRatioPYQ` | Measures company's ability to pay short-term obligations using short-term assets. | Previous Quarter 1 Year Ago |
| `CurRatioTTM` | Measures company's ability to pay short-term obligations using short-term assets. | Trailing 12 Months |
| `CurRatioPTM` | Measures company's ability to pay short-term obligations using short-term assets. | Previous Trailing 12 Months |
| `CurRatioA` | Measures company's ability to pay short-term obligations using short-term assets. | Latest Year |
| `CurRatioPY` | Measures company's ability to pay short-term obligations using short-term assets. | Previous Year |
| `CurRatioGr%PQ` | Measures company's ability to pay short-term obligations using short-term assets. | Q vs Previous Q Growth |
| `CurRatioGr%PYQ` | Measures company's ability to pay short-term obligations using short-term assets. | Q vs 1 year ago Q Growth |
| `CurRatioGr%TTM` | Measures company's ability to pay short-term obligations using short-term assets. | Trailing Twelve Months Growth |
| `CurRatioGr%PQTTM` | Measures company's ability to pay short-term obligations using short-term assets. | Trailing Twelve Months Growth 1Q Ago |
| `CurRatioGr%A` | Measures company's ability to pay short-term obligations using short-term assets. | Growth Annual |
| `CurRatioGr%3Y` | Measures company's ability to pay short-term obligations using short-term assets. | Three Year Annualized Growth |
| `CurRatioGr%5Y` | Measures company's ability to pay short-term obligations using short-term assets. | Five Year Annualized Growth |
| `CurRatioGr%10Y` | Measures company's ability to pay short-term obligations using short-term assets. | Ten Year Annualized Growth |
| `CurRatioRSD%ANN` | Measures company's ability to pay short-term obligations using short-term assets. | Ten Year Relative Standard Deviation |
| `CurRatioRSD%TTM` | Measures company's ability to pay short-term obligations using short-term assets. | Five Year Relative Standard Deviation |
| `CurRatioRegEstANN` | Measures company's ability to pay short-term obligations using short-term assets. | Ten Year Regression Estimate |
| `CurRatioRegEstTTM` | Measures company's ability to pay short-term obligations using short-term assets. | Five Year Regression Estimate |
| `CurRatioRegGr%ANN` | Measures company's ability to pay short-term obligations using short-term assets. | Ten Year Regression Estimate |
| `CurRatioRegGr%TTM` | Measures company's ability to pay short-term obligations using short-term assets. | Five Year Regression Growth |
| `CurRatio3YAvg` | Measures company's ability to pay short-term obligations using short-term assets. | Three Year Average |
| `CurRatio5YAvg` | Measures company's ability to pay short-term obligations using short-term assets. | Five Year Average |

#### Debt Service to Net Income

| Factor | Description | Period |
|---|---|---|
| `DbtS2NIQ` | Ratio of interest expense relative to earnings. | Latest Quarter |
| `DbtS2NIPQ` | Ratio of interest expense relative to earnings. | Previous Quarter |
| `DbtS2NIPYQ` | Ratio of interest expense relative to earnings. | Previous Quarter 1 Year Ago |
| `DbtS2NITTM` | Ratio of interest expense relative to earnings. | Trailing 12 Months |
| `DbtS2NIPTM` | Ratio of interest expense relative to earnings. | Previous Trailing 12 Months |
| `DbtS2NIA` | Ratio of interest expense relative to earnings. | Latest Year |
| `DbtS2NIPY` | Ratio of interest expense relative to earnings. | Previous Year |
| `DbtS2NIGr%PQ` | Ratio of interest expense relative to earnings. | Q vs Previous Q Growth |
| `DbtS2NIGr%PYQ` | Ratio of interest expense relative to earnings. | Q vs 1 year ago Q Growth |
| `DbtS2NIGr%TTM` | Ratio of interest expense relative to earnings. | Trailing Twelve Months Growth |
| `DbtS2NIGr%PQTTM` | Ratio of interest expense relative to earnings. | Trailing Twelve Months Growth 1Q Ago |
| `DbtS2NIGr%A` | Ratio of interest expense relative to earnings. | Growth Annual |
| `DbtS2NIGr%3Y` | Ratio of interest expense relative to earnings. | Three Year Annualized Growth |
| `DbtS2NIGr%5Y` | Ratio of interest expense relative to earnings. | Five Year Annualized Growth |
| `DbtS2NIGr%10Y` | Ratio of interest expense relative to earnings. | Ten Year Annualized Growth |
| `DbtS2NIRSD%ANN` | Ratio of interest expense relative to earnings. | Ten Year Relative Standard Deviation |
| `DbtS2NIRSD%TTM` | Ratio of interest expense relative to earnings. | Five Year Relative Standard Deviation |
| `DbtS2NIRegEstANN` | Ratio of interest expense relative to earnings. | Ten Year Regression Estimate |
| `DbtS2NIRegEstTTM` | Ratio of interest expense relative to earnings. | Five Year Regression Estimate |
| `DbtS2NIRegGr%ANN` | Ratio of interest expense relative to earnings. | Ten Year Regression Estimate |
| `DbtS2NIRegGr%TTM` | Ratio of interest expense relative to earnings. | Five Year Regression Growth |
| `DbtS2NI3YAvg` | Ratio of interest expense relative to earnings. | Three Year Average |
| `DbtS2NI5YAvg` | Ratio of interest expense relative to earnings. | Five Year Average |

#### Depreciation And Amort to Gross Profit

| Factor | Description | Period |
|---|---|---|
| `DepAmort2GPQ` | D&A expenses relative to gross profit | Latest Quarter |
| `DepAmort2GPPQ` | D&A expenses relative to gross profit | Previous Quarter |
| `DepAmort2GPPYQ` | D&A expenses relative to gross profit | Previous Quarter 1 Year Ago |
| `DepAmort2GPTTM` | D&A expenses relative to gross profit | Trailing 12 Months |
| `DepAmort2GPPTM` | D&A expenses relative to gross profit | Previous Trailing 12 Months |
| `DepAmort2GPA` | D&A expenses relative to gross profit | Latest Year |
| `DepAmort2GPPY` | D&A expenses relative to gross profit | Previous Year |
| `DepAmort2GPGr%PQ` | D&A expenses relative to gross profit | Q vs Previous Q Growth |
| `DepAmort2GPGr%PYQ` | D&A expenses relative to gross profit | Q vs 1 year ago Q Growth |
| `DepAmort2GPGr%TTM` | D&A expenses relative to gross profit | Trailing Twelve Months Growth |
| `DepAmort2GPGr%PQTTM` | D&A expenses relative to gross profit | Trailing Twelve Months Growth 1Q Ago |
| `DepAmort2GPGr%A` | D&A expenses relative to gross profit | Growth Annual |
| `DepAmort2GPGr%3Y` | D&A expenses relative to gross profit | Three Year Annualized Growth |
| `DepAmort2GPGr%5Y` | D&A expenses relative to gross profit | Five Year Annualized Growth |
| `DepAmort2GPGr%10Y` | D&A expenses relative to gross profit | Ten Year Annualized Growth |
| `DepAmort2GPRSD%ANN` | D&A expenses relative to gross profit | Ten Year Relative Standard Deviation |
| `DepAmort2GPRSD%TTM` | D&A expenses relative to gross profit | Five Year Relative Standard Deviation |
| `DepAmort2GPRegEstANN` | D&A expenses relative to gross profit | Ten Year Regression Estimate |
| `DepAmort2GPRegEstTTM` | D&A expenses relative to gross profit | Five Year Regression Estimate |
| `DepAmort2GPRegGr%ANN` | D&A expenses relative to gross profit | Ten Year Regression Estimate |
| `DepAmort2GPRegGr%TTM` | D&A expenses relative to gross profit | Five Year Regression Growth |
| `DepAmort2GPPSQ` | D&A expenses relative to gross profit | Quarterly Per Share |
| `DepAmort2GPPSA` | D&A expenses relative to gross profit | Annual Per Share |
| `DepAmort2GP%SalesQ` | D&A expenses relative to gross profit | % of Quarterly Sales |
| `DepAmort2GP%SalesA` | D&A expenses relative to gross profit | % of Annual Sales |
| `DepAmort2GP%AssetsQ` | D&A expenses relative to gross profit | % of Quarterly Assets |
| `DepAmort2GP%AssetsA` | D&A expenses relative to gross profit | % of Annual Assets |
| `DepAmort2GP3YAvg` | D&A expenses relative to gross profit | Three Year Average |
| `DepAmort2GP5YAvg` | D&A expenses relative to gross profit | Five Year Average |

#### Interest Coverage

| Factor | Description | Period |
|---|---|---|
| `IntCovQ` | Measure of ability to pay interest expenses. | Latest Quarter |
| `IntCovPQ` | Measure of ability to pay interest expenses. | Previous Quarter |
| `IntCovPYQ` | Measure of ability to pay interest expenses. | Previous Quarter 1 Year Ago |
| `IntCovTTM` | Measure of ability to pay interest expenses. | Trailing 12 Months |
| `IntCovPTM` | Measure of ability to pay interest expenses. | Previous Trailing 12 Months |
| `IntCovA` | Measure of ability to pay interest expenses. | Latest Year |
| `IntCovPY` | Measure of ability to pay interest expenses. | Previous Year |
| `IntCovGr%PQ` | Measure of ability to pay interest expenses. | Q vs Previous Q Growth |
| `IntCovGr%PYQ` | Measure of ability to pay interest expenses. | Q vs 1 year ago Q Growth |
| `IntCovGr%TTM` | Measure of ability to pay interest expenses. | Trailing Twelve Months Growth |
| `IntCovGr%PQTTM` | Measure of ability to pay interest expenses. | Trailing Twelve Months Growth 1Q Ago |
| `IntCovGr%A` | Measure of ability to pay interest expenses. | Growth Annual |
| `IntCovGr%3Y` | Measure of ability to pay interest expenses. | Three Year Annualized Growth |
| `IntCovGr%5Y` | Measure of ability to pay interest expenses. | Five Year Annualized Growth |
| `IntCovGr%10Y` | Measure of ability to pay interest expenses. | Ten Year Annualized Growth |
| `IntCovRSD%ANN` | Measure of ability to pay interest expenses. | Ten Year Relative Standard Deviation |
| `IntCovRSD%TTM` | Measure of ability to pay interest expenses. | Five Year Relative Standard Deviation |
| `IntCovRegEstANN` | Measure of ability to pay interest expenses. | Ten Year Regression Estimate |
| `IntCovRegEstTTM` | Measure of ability to pay interest expenses. | Five Year Regression Estimate |
| `IntCovRegGr%ANN` | Measure of ability to pay interest expenses. | Ten Year Regression Estimate |
| `IntCovRegGr%TTM` | Measure of ability to pay interest expenses. | Five Year Regression Growth |
| `IntCov3YAvg` | Measure of ability to pay interest expenses. | Three Year Average |
| `IntCov5YAvg` | Measure of ability to pay interest expenses. | Five Year Average |

#### Long Term Debt to Total Assets

| Factor | Description | Period |
|---|---|---|
| `DbtLT2AstQ` | Long-term debt relative to total assets. | Latest Quarter |
| `DbtLT2AstPQ` | Long-term debt relative to total assets. | Previous Quarter |
| `DbtLT2AstPYQ` | Long-term debt relative to total assets. | Previous Quarter 1 Year Ago |
| `DbtLT2AstTTM` | Long-term debt relative to total assets. | Trailing 12 Months |
| `DbtLT2AstPTM` | Long-term debt relative to total assets. | Previous Trailing 12 Months |
| `DbtLT2AstA` | Long-term debt relative to total assets. | Latest Year |
| `DbtLT2AstPY` | Long-term debt relative to total assets. | Previous Year |
| `DbtLT2AstGr%PQ` | Long-term debt relative to total assets. | Q vs Previous Q Growth |
| `DbtLT2AstGr%PYQ` | Long-term debt relative to total assets. | Q vs 1 year ago Q Growth |
| `DbtLT2AstGr%TTM` | Long-term debt relative to total assets. | Trailing Twelve Months Growth |
| `DbtLT2AstGr%PQTTM` | Long-term debt relative to total assets. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLT2AstGr%A` | Long-term debt relative to total assets. | Growth Annual |
| `DbtLT2AstGr%3Y` | Long-term debt relative to total assets. | Three Year Annualized Growth |
| `DbtLT2AstGr%5Y` | Long-term debt relative to total assets. | Five Year Annualized Growth |
| `DbtLT2AstGr%10Y` | Long-term debt relative to total assets. | Ten Year Annualized Growth |
| `DbtLT2AstRSD%ANN` | Long-term debt relative to total assets. | Ten Year Relative Standard Deviation |
| `DbtLT2AstRSD%TTM` | Long-term debt relative to total assets. | Five Year Relative Standard Deviation |
| `DbtLT2AstRegEstANN` | Long-term debt relative to total assets. | Ten Year Regression Estimate |
| `DbtLT2AstRegEstTTM` | Long-term debt relative to total assets. | Five Year Regression Estimate |
| `DbtLT2AstRegGr%ANN` | Long-term debt relative to total assets. | Ten Year Regression Estimate |
| `DbtLT2AstRegGr%TTM` | Long-term debt relative to total assets. | Five Year Regression Growth |
| `DbtLT2Ast3YAvg` | Long-term debt relative to total assets. | Three Year Average |
| `DbtLT2Ast5YAvg` | Long-term debt relative to total assets. | Five Year Average |

#### Long Term Debt to Total Capital

| Factor | Description | Period |
|---|---|---|
| `DbtLT2CapQ` | Long-term debt relative to total capital. | Latest Quarter |
| `DbtLT2CapPQ` | Long-term debt relative to total capital. | Previous Quarter |
| `DbtLT2CapPYQ` | Long-term debt relative to total capital. | Previous Quarter 1 Year Ago |
| `DbtLT2CapTTM` | Long-term debt relative to total capital. | Trailing 12 Months |
| `DbtLT2CapPTM` | Long-term debt relative to total capital. | Previous Trailing 12 Months |
| `DbtLT2CapA` | Long-term debt relative to total capital. | Latest Year |
| `DbtLT2CapPY` | Long-term debt relative to total capital. | Previous Year |
| `DbtLT2CapGr%PQ` | Long-term debt relative to total capital. | Q vs Previous Q Growth |
| `DbtLT2CapGr%PYQ` | Long-term debt relative to total capital. | Q vs 1 year ago Q Growth |
| `DbtLT2CapGr%TTM` | Long-term debt relative to total capital. | Trailing Twelve Months Growth |
| `DbtLT2CapGr%PQTTM` | Long-term debt relative to total capital. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLT2CapGr%A` | Long-term debt relative to total capital. | Growth Annual |
| `DbtLT2CapGr%3Y` | Long-term debt relative to total capital. | Three Year Annualized Growth |
| `DbtLT2CapGr%5Y` | Long-term debt relative to total capital. | Five Year Annualized Growth |
| `DbtLT2CapGr%10Y` | Long-term debt relative to total capital. | Ten Year Annualized Growth |
| `DbtLT2CapRSD%ANN` | Long-term debt relative to total capital. | Ten Year Relative Standard Deviation |
| `DbtLT2CapRSD%TTM` | Long-term debt relative to total capital. | Five Year Relative Standard Deviation |
| `DbtLT2CapRegEstANN` | Long-term debt relative to total capital. | Ten Year Regression Estimate |
| `DbtLT2CapRegEstTTM` | Long-term debt relative to total capital. | Five Year Regression Estimate |
| `DbtLT2CapRegGr%ANN` | Long-term debt relative to total capital. | Ten Year Regression Estimate |
| `DbtLT2CapRegGr%TTM` | Long-term debt relative to total capital. | Five Year Regression Growth |
| `DbtLT2Cap3YAvg` | Long-term debt relative to total capital. | Three Year Average |
| `DbtLT2Cap5YAvg` | Long-term debt relative to total capital. | Five Year Average |

#### Long Term Debt to Total Equity

| Factor | Description | Period |
|---|---|---|
| `DbtLT2EqQ` | Long-term debt relative to common equity. | Latest Quarter |
| `DbtLT2EqPQ` | Long-term debt relative to common equity. | Previous Quarter |
| `DbtLT2EqPYQ` | Long-term debt relative to common equity. | Previous Quarter 1 Year Ago |
| `DbtLT2EqTTM` | Long-term debt relative to common equity. | Trailing 12 Months |
| `DbtLT2EqPTM` | Long-term debt relative to common equity. | Previous Trailing 12 Months |
| `DbtLT2EqA` | Long-term debt relative to common equity. | Latest Year |
| `DbtLT2EqPY` | Long-term debt relative to common equity. | Previous Year |
| `DbtLT2EqGr%PQ` | Long-term debt relative to common equity. | Q vs Previous Q Growth |
| `DbtLT2EqGr%PYQ` | Long-term debt relative to common equity. | Q vs 1 year ago Q Growth |
| `DbtLT2EqGr%TTM` | Long-term debt relative to common equity. | Trailing Twelve Months Growth |
| `DbtLT2EqGr%PQTTM` | Long-term debt relative to common equity. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLT2EqGr%A` | Long-term debt relative to common equity. | Growth Annual |
| `DbtLT2EqGr%3Y` | Long-term debt relative to common equity. | Three Year Annualized Growth |
| `DbtLT2EqGr%5Y` | Long-term debt relative to common equity. | Five Year Annualized Growth |
| `DbtLT2EqGr%10Y` | Long-term debt relative to common equity. | Ten Year Annualized Growth |
| `DbtLT2EqRSD%ANN` | Long-term debt relative to common equity. | Ten Year Relative Standard Deviation |
| `DbtLT2EqRSD%TTM` | Long-term debt relative to common equity. | Five Year Relative Standard Deviation |
| `DbtLT2EqRegEstANN` | Long-term debt relative to common equity. | Ten Year Regression Estimate |
| `DbtLT2EqRegEstTTM` | Long-term debt relative to common equity. | Five Year Regression Estimate |
| `DbtLT2EqRegGr%ANN` | Long-term debt relative to common equity. | Ten Year Regression Estimate |
| `DbtLT2EqRegGr%TTM` | Long-term debt relative to common equity. | Five Year Regression Growth |
| `DbtLT2Eq3YAvg` | Long-term debt relative to common equity. | Three Year Average |
| `DbtLT2Eq5YAvg` | Long-term debt relative to common equity. | Five Year Average |

#### Net Income to Cap Expenditures

| Factor | Description | Period |
|---|---|---|
| `NI2CapExQ` | Profit is reinvested in capital expenditures. | Latest Quarter |
| `NI2CapExPQ` | Profit is reinvested in capital expenditures. | Previous Quarter |
| `NI2CapExPYQ` | Profit is reinvested in capital expenditures. | Previous Quarter 1 Year Ago |
| `NI2CapExTTM` | Profit is reinvested in capital expenditures. | Trailing 12 Months |
| `NI2CapExPTM` | Profit is reinvested in capital expenditures. | Previous Trailing 12 Months |
| `NI2CapExA` | Profit is reinvested in capital expenditures. | Latest Year |
| `NI2CapExPY` | Profit is reinvested in capital expenditures. | Previous Year |
| `NI2CapExGr%PQ` | Profit is reinvested in capital expenditures. | Q vs Previous Q Growth |
| `NI2CapExGr%PYQ` | Profit is reinvested in capital expenditures. | Q vs 1 year ago Q Growth |
| `NI2CapExGr%TTM` | Profit is reinvested in capital expenditures. | Trailing Twelve Months Growth |
| `NI2CapExGr%PQTTM` | Profit is reinvested in capital expenditures. | Trailing Twelve Months Growth 1Q Ago |
| `NI2CapExGr%A` | Profit is reinvested in capital expenditures. | Growth Annual |
| `NI2CapExGr%3Y` | Profit is reinvested in capital expenditures. | Three Year Annualized Growth |
| `NI2CapExGr%5Y` | Profit is reinvested in capital expenditures. | Five Year Annualized Growth |
| `NI2CapExGr%10Y` | Profit is reinvested in capital expenditures. | Ten Year Annualized Growth |
| `NI2CapExRSD%ANN` | Profit is reinvested in capital expenditures. | Ten Year Relative Standard Deviation |
| `NI2CapExRSD%TTM` | Profit is reinvested in capital expenditures. | Five Year Relative Standard Deviation |
| `NI2CapExRegEstANN` | Profit is reinvested in capital expenditures. | Ten Year Regression Estimate |
| `NI2CapExRegEstTTM` | Profit is reinvested in capital expenditures. | Five Year Regression Estimate |
| `NI2CapExRegGr%ANN` | Profit is reinvested in capital expenditures. | Ten Year Regression Estimate |
| `NI2CapExRegGr%TTM` | Profit is reinvested in capital expenditures. | Five Year Regression Growth |
| `NI2CapExPSQ` | Profit is reinvested in capital expenditures. | Quarterly Per Share |
| `NI2CapExPSA` | Profit is reinvested in capital expenditures. | Annual Per Share |
| `NI2CapEx%SalesQ` | Profit is reinvested in capital expenditures. | % of Quarterly Sales |
| `NI2CapEx%SalesA` | Profit is reinvested in capital expenditures. | % of Annual Sales |
| `NI2CapEx%AssetsQ` | Profit is reinvested in capital expenditures. | % of Quarterly Assets |
| `NI2CapEx%AssetsA` | Profit is reinvested in capital expenditures. | % of Annual Assets |
| `NI2CapEx3YAvg` | Profit is reinvested in capital expenditures. | Three Year Average |
| `NI2CapEx5YAvg` | Profit is reinvested in capital expenditures. | Five Year Average |

#### Payout Ratio

| Factor | Description | Period |
|---|---|---|
| `PayRatioQ` | Pividends paid relative to net income. | Latest Quarter |
| `PayRatioPQ` | Pividends paid relative to net income. | Previous Quarter |
| `PayRatioPYQ` | Pividends paid relative to net income. | Previous Quarter 1 Year Ago |
| `PayRatioTTM` | Pividends paid relative to net income. | Trailing 12 Months |
| `PayRatioPTM` | Pividends paid relative to net income. | Previous Trailing 12 Months |
| `PayRatioA` | Pividends paid relative to net income. | Latest Year |
| `PayRatioPY` | Pividends paid relative to net income. | Previous Year |
| `PayRatioGr%PQ` | Pividends paid relative to net income. | Q vs Previous Q Growth |
| `PayRatioGr%PYQ` | Pividends paid relative to net income. | Q vs 1 year ago Q Growth |
| `PayRatioGr%TTM` | Pividends paid relative to net income. | Trailing Twelve Months Growth |
| `PayRatioGr%PQTTM` | Pividends paid relative to net income. | Trailing Twelve Months Growth 1Q Ago |
| `PayRatioGr%A` | Pividends paid relative to net income. | Growth Annual |
| `PayRatioGr%3Y` | Pividends paid relative to net income. | Three Year Annualized Growth |
| `PayRatioGr%5Y` | Pividends paid relative to net income. | Five Year Annualized Growth |
| `PayRatioGr%10Y` | Pividends paid relative to net income. | Ten Year Annualized Growth |
| `PayRatioRSD%ANN` | Pividends paid relative to net income. | Ten Year Relative Standard Deviation |
| `PayRatioRSD%TTM` | Pividends paid relative to net income. | Five Year Relative Standard Deviation |
| `PayRatioRegEstANN` | Pividends paid relative to net income. | Ten Year Regression Estimate |
| `PayRatioRegEstTTM` | Pividends paid relative to net income. | Five Year Regression Estimate |
| `PayRatioRegGr%ANN` | Pividends paid relative to net income. | Ten Year Regression Estimate |
| `PayRatioRegGr%TTM` | Pividends paid relative to net income. | Five Year Regression Growth |
| `PayRatio3YAvg` | Pividends paid relative to net income. | Three Year Average |
| `PayRatio5YAvg` | Pividends paid relative to net income. | Five Year Average |

#### Quick  Ratio

| Factor | Description | Period |
|---|---|---|
| `QuickRatioQ` | Immediate liquidity excluding inventory. | Latest Quarter |
| `QuickRatioPQ` | Immediate liquidity excluding inventory. | Previous Quarter |
| `QuickRatioPYQ` | Immediate liquidity excluding inventory. | Previous Quarter 1 Year Ago |
| `QuickRatioTTM` | Immediate liquidity excluding inventory. | Trailing 12 Months |
| `QuickRatioPTM` | Immediate liquidity excluding inventory. | Previous Trailing 12 Months |
| `QuickRatioA` | Immediate liquidity excluding inventory. | Latest Year |
| `QuickRatioPY` | Immediate liquidity excluding inventory. | Previous Year |
| `QuickRatioGr%PQ` | Immediate liquidity excluding inventory. | Q vs Previous Q Growth |
| `QuickRatioGr%PYQ` | Immediate liquidity excluding inventory. | Q vs 1 year ago Q Growth |
| `QuickRatioGr%TTM` | Immediate liquidity excluding inventory. | Trailing Twelve Months Growth |
| `QuickRatioGr%PQTTM` | Immediate liquidity excluding inventory. | Trailing Twelve Months Growth 1Q Ago |
| `QuickRatioGr%A` | Immediate liquidity excluding inventory. | Growth Annual |
| `QuickRatioGr%3Y` | Immediate liquidity excluding inventory. | Three Year Annualized Growth |
| `QuickRatioGr%5Y` | Immediate liquidity excluding inventory. | Five Year Annualized Growth |
| `QuickRatioGr%10Y` | Immediate liquidity excluding inventory. | Ten Year Annualized Growth |
| `QuickRatioRSD%ANN` | Immediate liquidity excluding inventory. | Ten Year Relative Standard Deviation |
| `QuickRatioRSD%TTM` | Immediate liquidity excluding inventory. | Five Year Relative Standard Deviation |
| `QuickRatioRegEstANN` | Immediate liquidity excluding inventory. | Ten Year Regression Estimate |
| `QuickRatioRegEstTTM` | Immediate liquidity excluding inventory. | Five Year Regression Estimate |
| `QuickRatioRegGr%ANN` | Immediate liquidity excluding inventory. | Ten Year Regression Estimate |
| `QuickRatioRegGr%TTM` | Immediate liquidity excluding inventory. | Five Year Regression Growth |
| `QuickRatio3YAvg` | Immediate liquidity excluding inventory. | Three Year Average |
| `QuickRatio5YAvg` | Immediate liquidity excluding inventory. | Five Year Average |

#### Retention Rate

| Factor | Description | Period |
|---|---|---|
| `Retn%Q` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Latest Quarter |
| `Retn%PQ` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Previous Quarter |
| `Retn%PYQ` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Previous Quarter 1 Year Ago |
| `Retn%TTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Trailing 12 Months |
| `Retn%PTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Previous Trailing 12 Months |
| `Retn%A` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Latest Year |
| `Retn%PY` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Previous Year |
| `Retn%Gr%PQ` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Q vs Previous Q Growth |
| `Retn%Gr%PYQ` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Q vs 1 year ago Q Growth |
| `Retn%Gr%TTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Trailing Twelve Months Growth |
| `Retn%Gr%PQTTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Trailing Twelve Months Growth 1Q Ago |
| `Retn%Gr%A` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Growth Annual |
| `Retn%Gr%3Y` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Three Year Annualized Growth |
| `Retn%Gr%5Y` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Five Year Annualized Growth |
| `Retn%Gr%10Y` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Ten Year Annualized Growth |
| `Retn%RSD%ANN` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Ten Year Relative Standard Deviation |
| `Retn%RSD%TTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Five Year Relative Standard Deviation |
| `Retn%RegEstANN` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Ten Year Regression Estimate |
| `Retn%RegEstTTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Five Year Regression Estimate |
| `Retn%RegGr%ANN` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Ten Year Regression Estimate |
| `Retn%RegGr%TTM` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Five Year Regression Growth |
| `Retn%3YAvg` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Three Year Average |
| `Retn%5YAvg` | Percentage of earnings kept by the company for reinvestment rather than distributed as dividends. | Five Year Average |

#### Total Debt To Total Assets

| Factor | Description | Period |
|---|---|---|
| `DbtTot2AstQ` | Total debt relative to total assets. | Latest Quarter |
| `DbtTot2AstPQ` | Total debt relative to total assets. | Previous Quarter |
| `DbtTot2AstPYQ` | Total debt relative to total assets. | Previous Quarter 1 Year Ago |
| `DbtTot2AstTTM` | Total debt relative to total assets. | Trailing 12 Months |
| `DbtTot2AstPTM` | Total debt relative to total assets. | Previous Trailing 12 Months |
| `DbtTot2AstA` | Total debt relative to total assets. | Latest Year |
| `DbtTot2AstPY` | Total debt relative to total assets. | Previous Year |
| `DbtTot2AstGr%PQ` | Total debt relative to total assets. | Q vs Previous Q Growth |
| `DbtTot2AstGr%PYQ` | Total debt relative to total assets. | Q vs 1 year ago Q Growth |
| `DbtTot2AstGr%TTM` | Total debt relative to total assets. | Trailing Twelve Months Growth |
| `DbtTot2AstGr%PQTTM` | Total debt relative to total assets. | Trailing Twelve Months Growth 1Q Ago |
| `DbtTot2AstGr%A` | Total debt relative to total assets. | Growth Annual |
| `DbtTot2AstGr%3Y` | Total debt relative to total assets. | Three Year Annualized Growth |
| `DbtTot2AstGr%5Y` | Total debt relative to total assets. | Five Year Annualized Growth |
| `DbtTot2AstGr%10Y` | Total debt relative to total assets. | Ten Year Annualized Growth |
| `DbtTot2AstRSD%ANN` | Total debt relative to total assets. | Ten Year Relative Standard Deviation |
| `DbtTot2AstRSD%TTM` | Total debt relative to total assets. | Five Year Relative Standard Deviation |
| `DbtTot2AstRegEstANN` | Total debt relative to total assets. | Ten Year Regression Estimate |
| `DbtTot2AstRegEstTTM` | Total debt relative to total assets. | Five Year Regression Estimate |
| `DbtTot2AstRegGr%ANN` | Total debt relative to total assets. | Ten Year Regression Estimate |
| `DbtTot2AstRegGr%TTM` | Total debt relative to total assets. | Five Year Regression Growth |
| `DbtTot2Ast3YAvg` | Total debt relative to total assets. | Three Year Average |
| `DbtTot2Ast5YAvg` | Total debt relative to total assets. | Five Year Average |

#### Total Debt to Total Capital

| Factor | Description | Period |
|---|---|---|
| `DbtTot2CapQ` | Total debt relative to total capital. | Latest Quarter |
| `DbtTot2CapPQ` | Total debt relative to total capital. | Previous Quarter |
| `DbtTot2CapPYQ` | Total debt relative to total capital. | Previous Quarter 1 Year Ago |
| `DbtTot2CapTTM` | Total debt relative to total capital. | Trailing 12 Months |
| `DbtTot2CapPTM` | Total debt relative to total capital. | Previous Trailing 12 Months |
| `DbtTot2CapA` | Total debt relative to total capital. | Latest Year |
| `DbtTot2CapPY` | Total debt relative to total capital. | Previous Year |
| `DbtTot2CapGr%PQ` | Total debt relative to total capital. | Q vs Previous Q Growth |
| `DbtTot2CapGr%PYQ` | Total debt relative to total capital. | Q vs 1 year ago Q Growth |
| `DbtTot2CapGr%TTM` | Total debt relative to total capital. | Trailing Twelve Months Growth |
| `DbtTot2CapGr%PQTTM` | Total debt relative to total capital. | Trailing Twelve Months Growth 1Q Ago |
| `DbtTot2CapGr%A` | Total debt relative to total capital. | Growth Annual |
| `DbtTot2CapGr%3Y` | Total debt relative to total capital. | Three Year Annualized Growth |
| `DbtTot2CapGr%5Y` | Total debt relative to total capital. | Five Year Annualized Growth |
| `DbtTot2CapGr%10Y` | Total debt relative to total capital. | Ten Year Annualized Growth |
| `DbtTot2CapRSD%ANN` | Total debt relative to total capital. | Ten Year Relative Standard Deviation |
| `DbtTot2CapRSD%TTM` | Total debt relative to total capital. | Five Year Relative Standard Deviation |
| `DbtTot2CapRegEstANN` | Total debt relative to total capital. | Ten Year Regression Estimate |
| `DbtTot2CapRegEstTTM` | Total debt relative to total capital. | Five Year Regression Estimate |
| `DbtTot2CapRegGr%ANN` | Total debt relative to total capital. | Ten Year Regression Estimate |
| `DbtTot2CapRegGr%TTM` | Total debt relative to total capital. | Five Year Regression Growth |
| `DbtTot2Cap3YAvg` | Total debt relative to total capital. | Three Year Average |
| `DbtTot2Cap5YAvg` | Total debt relative to total capital. | Five Year Average |

#### Total Debt to Total Equity

| Factor | Description | Period |
|---|---|---|
| `DbtTot2EqQ` | Total debt relative to common equity. | Latest Quarter |
| `DbtTot2EqPQ` | Total debt relative to common equity. | Previous Quarter |
| `DbtTot2EqPYQ` | Total debt relative to common equity. | Previous Quarter 1 Year Ago |
| `DbtTot2EqTTM` | Total debt relative to common equity. | Trailing 12 Months |
| `DbtTot2EqPTM` | Total debt relative to common equity. | Previous Trailing 12 Months |
| `DbtTot2EqA` | Total debt relative to common equity. | Latest Year |
| `DbtTot2EqPY` | Total debt relative to common equity. | Previous Year |
| `DbtTot2EqGr%PQ` | Total debt relative to common equity. | Q vs Previous Q Growth |
| `DbtTot2EqGr%PYQ` | Total debt relative to common equity. | Q vs 1 year ago Q Growth |
| `DbtTot2EqGr%TTM` | Total debt relative to common equity. | Trailing Twelve Months Growth |
| `DbtTot2EqGr%PQTTM` | Total debt relative to common equity. | Trailing Twelve Months Growth 1Q Ago |
| `DbtTot2EqGr%A` | Total debt relative to common equity. | Growth Annual |
| `DbtTot2EqGr%3Y` | Total debt relative to common equity. | Three Year Annualized Growth |
| `DbtTot2EqGr%5Y` | Total debt relative to common equity. | Five Year Annualized Growth |
| `DbtTot2EqGr%10Y` | Total debt relative to common equity. | Ten Year Annualized Growth |
| `DbtTot2EqRSD%ANN` | Total debt relative to common equity. | Ten Year Relative Standard Deviation |
| `DbtTot2EqRSD%TTM` | Total debt relative to common equity. | Five Year Relative Standard Deviation |
| `DbtTot2EqRegEstANN` | Total debt relative to common equity. | Ten Year Regression Estimate |
| `DbtTot2EqRegEstTTM` | Total debt relative to common equity. | Five Year Regression Estimate |
| `DbtTot2EqRegGr%ANN` | Total debt relative to common equity. | Ten Year Regression Estimate |
| `DbtTot2EqRegGr%TTM` | Total debt relative to common equity. | Five Year Regression Growth |
| `DbtTot2Eq3YAvg` | Total debt relative to common equity. | Three Year Average |
| `DbtTot2Eq5YAvg` | Total debt relative to common equity. | Five Year Average |


## Other

### Factors with detailed definitions

#### `EPSStableQ`

Also known as the Coefficient of Variation, this value indicates the stability of earnings. For companies that report earnings quarterly, EPSStableQ is calculated by taking the standard deviation of the 20 most recent quarterly EPS values and dividing by the absolute value of the mean. The absolute value is used because otherwise stocks with the highest volatility and a negative EPS mean would get the highest score since EPSStableQ uses 'lower is better'.

The company must have at least 16 quarters of EPS values in order for this value to be calculated. If the are less than 16 (as would be the case of an IPO), the calculation is not performed since the resulting value would not be meaningful and will return N/A. For companies that report semi-annually, the calculation uses the 10 most recent semi-annual EPS values and the company must have at least 16 quarters of EPS values in order for this value to be calculated.

Formula

When there are no NAs EPSStableQ is equivalent to:

LoopRelStdDev("EPSExclXor(CTR, QTR)",20)/100

*Period: Previous Quarter*


#### `EV`

While market capitalization measures the total value of the publicly-traded equity, enterprise value goes further and attempts to measure the value of the entire company. Many see it as the minimum price someone seeking to acquire the company would have to pay. The formula we use is:

Formula:

MktCap + PfdEquity + NonControlInt + DbtTot - CashEquiv

Note that this is an estimate. In the real world, firms are often acquired at prices that reflect premiums above enterprise value. Also, it is possible for an extremely cash-heavy company to have a negative enterprise value (i.e. the market is, for one reason or another, not paying attention to the full amount of cash). In the latter case, we show Enterprise Value and Enterprise Value per share as NA.

Finally, note that the calculation of the per-share presentation of enterprise value uses non-diluted shares.


#### `EVPS`

While market capitalization measures the total value of the publicly-traded equity, enterprise value goes further and attempts to measure the value of the entire company. Many see it as the minimum price someone seeking to acquire the company would have to pay. The formula we use is:

Formula:

MktCap + PfdEquity + NonControlInt + DbtTot - CashEquiv

Note that this is an estimate. In the real world, firms are often acquired at prices that reflect premiums above enterprise value. Also, it is possible for an extremely cash-heavy company to have a negative enterprise value (i.e. the market is, for one reason or another, not paying attention to the full amount of cash). In the latter case, we show Enterprise Value and Enterprise Value per share as NA.

Finally, note that the calculation of the per-share presentation of enterprise value uses non-diluted shares.


#### `Float`

Float excludes holdings of insiders, such as officers and directors, and strategic 5% shareholders, such as private equity or venture capital investors.


#### `FloatPct`

Float excludes holdings of insiders, such as officers and directors, and strategic 5% shareholders, such as private equity or venture capital investors.


#### `EPS#Positive`

This value is the number of consecutive years that the company reported positive Earnings Per Share (EPSExclXor) starting with the most recent fiscal year.

This factor is equivalent to this formula except that LoopSum can only access 20 years of history (the factor can access entire history of 40+ years) 

IsNa(LoopSum("Eval(EPSExclXor(CTR, ann) > 0, 1, NA)", 20, 0, 1, FALSE, TRUE) , 0 )


#### `MktCap`

Market Capitalization (Market Cap) is the most recent market value of a company's outstanding shares. The Market Cap equals the current share price multiplied by the number of outstanding shares.

The investing community often uses market capitalization value to rank companies and compare their relative sizes in a particular industry or sector. To determine a company's market cap, take its current market share price and multiply the figure by the total number of shares outstanding.


#### `ValROETTM`

This is the trailing twelve month Return On Equity (ROE) divided by the trailing twelve month Price Earnings (P/E) ratio.

*Period: Trailing 12 Months*


#### `SusGr%`

The sustainable growth rate is the rate of growth that a company can expect to see in the long term. It can be calculated by multiplying a company's earnings retention rate by its return on equity.

The sustainable growth rate is an indicator of what stage a company is in during its life cycle. The position often determines corporate finance objectives, such as financing sources, dividend payout policies, and overall competitive strategy.

Creditors can also use the growth ratio to determine the likelihood of a company defaulting on its loans. A high growth rate may indicate that the company is focusing on investing in R&D and NPV-positive projects, which may delay debt repayment. A high-growth-rate company is generally considered riskier, as it likely sees greater earnings volatility from period to period.

How to Calculate the Sustainable Growth Rate?

The sustainable growth rate is calculated as the trailing twelve-month Retention Rate multiplied by the trailing twelve-month Return on Equity, divided by 100

Sustainable Growth Rate = Retention Rate * Return on Equity / 100

Where:

Retention Rate - [ (Net Income - Dividends) / Net Income) ]. This represents the percentage of earnings the company has not paid out in dividends. In other words, how much profit the company retains, where Net Income - Dividends is equal to Retained Earnings.

Return on Equity - (Net Income / Total Shareholder's Equity). This represents how much return investors have realized relative to the company's profit.

A very high growth rate signifies that a company is still growing quickly. As such, the company may be spending a lot of its earnings on research and development and may not have a lot of cash left over to make debt payments. Therefore, a growing company could benefit more from equity financing and issuing stock to finance its operations.

*Period: Trailing 12 Months*


### Factor variants

#### Income Trend

| Factor | Description | Period |
|---|---|---|
| `NoIncP4YN2Y` | Returns the number of yearly EPS increases using the past four years and the future two year estimates. Values range from 0-6 |  |
| `NoPosEBITDA5Y` | Number positive EBITDA past 5 Y | 5 Years |
| `NoPosEPS5Q` | Number of quarter with positive EPS of the previous 5 | 5 Quarters |

#### NAV Growth

| Factor | Description | Period |
|---|---|---|
| `NAV%Chg12M` | NAV percent change 12 months | 12 Months |
| `NAV%Chg1M` | NAV percent change 1 month | 1 Month |
| `NAV%Chg3M` | NAV percent change 3 months | 3 Months |
| `NAV%Chg6M` | NAV percent change 6 months | 6 Months |


## Advanced

### Scoring models and derived factors

#### `BeneishMScore`

- Based on the original Beneish paper

- Our version of DEPI uses Dep&Amort. See more details in the DEPI documentation

- This factor is computed on-the-fly. Overusing it as in the ranking, rules, etc, will make your simulations slower. See each component's documentation for details of actual implementation.

M-Score is a score created by Messod Beneish that uses fundamental financial data to measure the likelihood that a company is manipulating reported earnings. It's the result of research that compared a small group of companies known, mainly thorough SEC enforcement proceedings and subsequent earnings restatements, to have manipulated results with a larger sample of companies that were not known to have manipulated. M-Score is based on this formula of eight factors:

| M-Score= | -4.84 + 0.92*DRI + 0.528*GMI + 0.404*AQI + 0.892*SGI +0.115*DEPI - 0.172*SGAI - 0.327*LVGI + 4.679*TATA |
|---|---|

The model is framed such that higher numerical M-Score scores are associated with increased probability of manipulation. Beneish's papers suggest three possible cutoff scores based on the investor's expectation of the cost of erroneously failing to identify a manipulator (i.e. if an investor presumes it would take normal returns from 40 investments in non-manipulative companies to offset the loss likely to be experienced from an erroneous investment in one company that is later exposed as having manipulated results, we'd described the cost of error as 40:1). The cutoff scores are as follows:

| Presumed Cost of Error | Assume company is a potential Manipulator if |
|---|---|
| 40:1 | BeneishMScore > -1.49 |
| 20:1 | BeneishMScore > -1.78 |
| 10:1 | BeneishMScore > -1.89 |

NOTE: Beneish M-Score famously flagged Enron (Ticker "ENRNQ^04") as a manipulator. Around July 2001 the M-Score was around -0.6 indicating a high probability of manipulation

Related Factors:

BeneishMScore

MScoreAQI

MScoreDEPAMI

MScoreDEPI

MScoreDSRI

MScoreGMI

MScoreLVGI

MScoreSGAI

MScoreSGAI

MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreAQI`

From the original Beneish paper

Asset quality in a given year is the ratio of non-current assets other than property plant and equipment (PPE) to total assets and measures the proportion of total assets for which future benefits are potentially less certain. AQI is the ratio of asset quality in year t, relative to asset quality in year t-1. AQI is an aggregate measure of the change in the asset realization risk analysis suggested by Siegel (1991). If AQI is greater than 1 it indicates that the firm has potentially increased its involvement in cost deferral. I thus expect a positive relation between AQI and the probability of earnings manipulation. An increase in asset realization risk indicates an increased propensity to capitalize and thus defer costs.

Beneish Formula

(1 - ((Current Assets{t} + Net Plant{t}) / Total Assets{t})) /

(1 - ((Current Assets{t-1} + Net Plant{t-1}) / Total Assets{t-1}))

If meaningful data is not available, set score equal to neutral (1.00)

Our Formula

ISNA((1-((AstCurQ+ NetPlantQ)/ AstTotQ)) / 

(1-((AstCurPYQ+ NetPlantPYQ)/ AstTotPYQ)),1))

NOTE: If AstCurQ during preliminary reporting is N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreDEPAMI`

From the original Beneish paper

DEPI is the ratio of the rate of depreciation in year t-1 vs the corresponding rate in year t.The depreciation rate in a given year equals is equal to depreciation/(depreciation+net PPE). A DEPI greater than 1 it indicates that the rate at which assets are depreciated has slowed down--raising the possibility that the firm has revised upwards the estimates of assets useful lives or adopted a new method that is income increasing. I thus expect a positive relation between DEPI and the probability of manipulation.

Beneish Formula

(Depreciation{t-1} / (Depreciation{t-1} + Net Plant{t-1})) /

(Depreciation{t} / (Depreciation{t} + Net Plant{t}))

Our Formula

ISNA((DepAmortPTM / (DepAmortPTM + NetPlantPYQ)) / 

(DepAmortTTM / (DepAmortTTM + NetPlantQ)),1)

NOTE1: Our Beneish score uses this version of DEPI that uses Dep&Amort instead of just Depreciation due to the
limited Depreciation data from Compustat (only annual values starting in 2001)

NOTE2: If DepAmort during preliminary reporting is N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreDEPI`

From the original Beneish paper

DEPI is the ratio of the rate of depreciation in year t-1 vs the corresponding rate in year t.The depreciation rate in a given year equals is equal to depreciation/(depreciation+net PPE). A DEPI greater than 1 it indicates that the rate at which assets are depreciated has slowed down--raising the possibility that the firm has revised upwards the estimates of assets useful lives or adopted a new method that is income increasing. I thus expect a positive relation between DEPI and the probability of manipulation.

Beneish Formula

(Depreciation{t-1} / (Depreciation{t-1} + Net Plant{t-1})) /

(Depreciation{t} / (Depreciation{t} + Net Plant{t}))

Our Formula

ISNA((DepPTM(estimated) / (DepPTM(estimated) + NetPlantPYQ)) / 

(DepTTM(estimated) / (DepTTM(estimated) + NetPlantQ)),1)

NOTE1: This version of DEPI estimates the Depreciation component of Dep&Amort by looking
at the annual Depreciation values that Compustat makes available and calculating a ratio 
to extract Depreciation from Dep&Amort interim data.

NOTE2: If DepAmort during preliminary reporting is N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreDSRI`

From the original Beneish paper

DSRI is the ratio of days sales in receivable in the first year in which earnings manipulation is uncovered (year t) to the corresponding measure in year t-1. This variable gauges whether receivables and revenues are in or out-of-balance in two consecutive years. A large increase in days sales in receivables could be the result of a change in credit policy to spur sales in the face of increased competition, but disproportionate increases in receivables relative to sales may also be suggestive of revenue inflation. I thus expect a large increase in days sales in receivables to be associated with a higher likelihood that revenues and earnings are overstated

Beneish Formula

(Receivables{t}/Sales{t}) / (Receivables{t-1}/Sales{t-1})

Our Formula

(RecvblQ/SalesTTM) / (RecvblPYQ/SalesPTM)

NOTE: If Receivables during preliminary reporting are N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreGMI`

From the original Beneish paper

GMI is ratio of the gross margin in year t-1 to the gross margin in year t. When GMI is greater than 1, it indicates that gross margins have deteriorated. Lev and Thiagarajan(1993) suggest that gross margin deterioration is a negative signal about firms' prospects. If firms with poorer prospects are more likely to engage in earnings manipulation, I expect a positive relation between GMI and the probability of earnings manipulation. 

Beneish Formula

((Sales{t-1} - Cost of Goods Sold{t-1}) /Sales{t-1}) /

((Sales{t} - Cost of Goods Sold{t}) /Sales{t})

Our Formula

((GrossProfitPTM/SalesPTM)-(GrossProfitTTM/SalesTTM)) / 

abs(GrossProfitTTM/SalesTTM))+1)

NOTE1: If GrossProfit during preliminary reporting are N/A , the whole formula excludes the latest period

NOTE2:To accommodate the possibility of negative gross margins, we use the
(a-b)/abs(b) format. To stay consistent, we use the (a-b)/abs(b) approach across the board. But when we do this, we'll get a straightforward percent (expressed in decimal form). For example if we measure the percent change from 10 to 13, our formula will produce an answer of 0.30. However, the a/b approach Beneish used would produce the figure 1.30. We need the latter for use in the overall MScore equation; to multiply the GMI value by the appropriate coefficient. Accordingly, the formula we use to compute GMI is: ((a-b)/abs(b))+1 where a represents values for the t-1 period and b represents values for the t period.

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreLVGI`

From the original Beneish paper

LVGI is the ratio of total debt to total assets in year t relative to the corresponding ratio in year t-1. A LVGI greater than 1 indicates an increase in leverage. The variable is included to capture debt covenants incentives for earnings manipulation. Assuming that leverage follows a random walk, LVGI implicitly measures the leverage forecast error. I use the change in leverage in the firms' capital structure given evidence in Beneish and Press(1993) that such changes are associated with the stock market effect of default.

Beneish Formula

((Long-Term Debt{t} + Current Liabilities{t})/Total Assets{t}) /

((Long-Term Debt{t-1} + Current Liabilities{t-1})/Total Assets{t-1})

Our Formula

((DbtLTQ + CurLiabQ)/AstTotQ) /

((DbtLTPYQ + CurLiabPYQ)/AstTotPYQ)

NOTE: If AstTot during preliminary reporting are N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreSGAI`

From the original Beneish paper

SGAI is calculated as the ratio of SGA to sales in year t relative to the corresponding measure in year t-1. The variable is used following Lev and Thiagarajan's (1993) suggestion that analysts would interpret a disproportionate increase in sales as a negative signal about firms future prospects. I expect a positive relation between SGAI and the probability of manipulation.

Beneish Formula

(SG&A{t}/Sales{t}) / (SG&A{t-1}/Sales{t-1})

If meaningful data is not available, set score equal to neutral (1.00)

Our Formula

ISNA(((SGandATTM/SalesTTM)/(SGandAPTM/SalesPTM)),1)

NOTE: If SGandATTM during preliminary reporting is N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreSGI`

From the original Beneish paper

SGI is the ratio of sales in year t to sales in year t-1. Growth does not imply manipulation, but growth firms are viewed by professionals as more likely to commit financial statement fraud because their financial position and capital needs put pressure on managers to achieve earnings targets. In addition, concerns about controls and reporting tend to lag behind operations in periods of high growth. If growth firms face large stock prices losses at the first indication of a slowdown, they may have greater incentives to manipulate earnings. To this effect, Fridson (1993, pp. 7-8) states: "Almost invariably, companies try to dispel the impression that their growth is decelerating, since that perception can be so costly to them." I thus expect a positive relation between SGI and the probability of earnings manipulation.

Beneish Formula

Sales{t} / Sales{t-1}

Our Formula

SalesTTM/SalesPTM

NOTE: There's no fallback with Sales since it should always be there even during preliminary reports

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `MScoreTATA`

From the original Beneish paper

Total accruals are calculated as the change in working capital accounts other than cash less depreciation. Either total accruals or a partition thereof has been used in prior work to assess the extent to which managers make discretionary accounting choices to alter earnings(see for example Healy (1985), Jones (1991). I use total accruals to total assets to proxy for the extent to which cash underlies reported earnings, and expect higher positive accruals(less cash) to be associated with a higher likelihood of earnings manipulation

Beneish Formula

(Net Inc before xor Items{t} - Cash from Op{t}) / Total Assets{t}

Our Formula

(NetIncBXorTTM - OperCashFlttm) / AstTotQ

NOTE: If OperCashFl during preliminary reporting is N/A , the whole formula excludes the latest period

Related Factors:

BeneishMScore
MScoreAQI
MScoreDEPAMI
MScoreDEPI
MScoreDSRI
MScoreGMI
MScoreLVGI
MScoreSGAI
MScoreSGAI
MScoreTATA

*Period: Trailing 12 Months*


#### `PiotFScore`

The Piotroski F-Score, ranging from 0 (worst) to 9 (best) is the sum of a company's standing according to nine fundamental tests (each of which is scored 1 for pass and 0 for fail) identified by Joseph Piotroski as being useful in evaluating stocks that look cheap based on price-to-book. The approach starts with a presumption that such companies whose stocks are valued low are distressed and not likely to be adequately followed by analysts. Piotroski addresses the dearth of expert assessment through use of the nine tests, all of which can be readily calculated using basic financial data, to distinguish between firms that are genuinely distressed and those that are stronger.

For more information, please see the original research available on this link

NOTE: this factor is computed on-the-fly. Overusing it as in the ranking, rules, etc, will make your simulations slower.

Formula

These nine PASS/FAIL tests are added together resulting in a score from 0-9

| PASS/FAIL Test | Our Formula |
|---|---|
| Profitability |  |
| Positive ROA | ROA%TTM > 0 |
| Positive Op CF | OperCashFlTTM > 0 |
| Higher ROA | ROA%TTM > ROA%PTM |
| Op CF > Net Income | OperCashFlTTM > NetIncCFStmtTTM |
| Leverage Components |  |
| Lower Debt | DbtTot2AstQ < DbtTot2AstPYQ |
| Higher Curr Ratio | CurRatioQ > CurRatioPYQ |
| No Dilution | SharesQ <= SharesPYQ |
| Operating Efficiencies |  |
| Higher Gross Mgn | GMgn%TTM > GMgn%PTM |
| Higher Asset Turn | AstTurnTTM > AstTurnPTM |
| NA Fallback: If the most recent quarter has NA values, such as in preliminary reports, the most recent data is not used. |  |

*Period: Trailing 12 Months*


#### `AltmanZOrig`

There are three versions of the Altman Z-Score. In all cases higher values are better, but the cutoffs vary. See the descriptions of each below

AltmanZOrig

Z = 1.2 * AltmanX1 + 1.4 * AltmanX2 + 3.3 * AltmanX3 + 0.6 * AltmanX4 + 1.0 * AltmanX5

Initially, Altman worked with a cutoff of 2.675; scores below that were presumed to signify significant bankruptcy risk. The probability of accuracy was very high in the percentage of bankruptcies it predicted, but at the cost of too many (in Altman?s judgment) Type II errors (flagging firms as distressed that do not wind up filing bankruptcy). Accordingly, Altman recommends use of a cutoff of 1.81.

AltmanZPriv

Z = .717 * AltmanX1 + .847 * AltmanX2 + 3.107 * AltmanX3 + 0.42 * AltmanX4Rev + .998 * AltmanX5

While privately-owned companies are not included in our database, we understand that we must necessarily depart from literal application of the model if we are to make it useful to assess stock prospects. Accordingly, users may want to consider this variation in cases where they believe the current market value of equity may be temporarily distorted and not indicative of the value the equity is likely to have over a longer term. Altman recommends use of a score of 1.23 or greater

AltmanZNonManu

Z = 6.56 * AltmanX1 + 3.26 * AltmanX2 + 6.72 * AltmanX3 + 1.05 * AltmanX4 

Variables X1 through X4 are the same as in the original model. X5 is omitted in order to minimize potential industry effect, which can be troublesome as comparisons from one to another become less apples-to-apples. Altman recommends use of a cutoff score of 1.10.

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

Background

The Z-Score, created by Prof. Edward Altman, is a well-established model designed for and used to predict corporate bankruptcy at least a year in advance. Traditionally, as of the time Altman developed the model, credit analysis had been conducted mainly on a qualitative basis. And to the extent any quantitative work was done, the value of ratio analysis had been called into question by many in the academic community who favored more rigorous statistical techniques. Altman regarded the main innovations of his research as showing the value of ratio analysis and showing the value of an approach that used multiple factors in a single model, as opposed to the single-factor inquiries used by others who had been willing to work with ratios. It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

IMPORTANT CAVEATS:

The Altman Z Score models have been noticed in the equity investment community and many seek to use this as part of the stock selection and analysis process. Accordingly, we are making it available. It is very important to note, however, that the model was developed for purposes of predicting bankruptcy. Equity returns, a critical dependent variable in the research of others who developed valuable models for use by equity investors, was not considered as part of Altman?s research. Equity investors who are interested in the Z score are necessarily presuming there is a relationship between bankruptcy and poor share price performance. In a big-picture sense, we can logically assume this is the case. But Altman did not research the timing and pace at which share price deterioration preceded bankruptcy. Note, too, that even within the area of bankruptcy prediction, Altman later came up with what he regarded as a superior model, a Zeta score. But because this was developed for a particular client and sold to them for their proprietary use, had has not divulged its parameters with enough specificity to be implemented by anyone except the client.

Accordingly, we cannot and do not suggest that your use of Z-score in the manner prescribed by Altman will enhance your strategy design. If you wish to work with Z score, consider using it in different ways (i.e. different score cutoffs and combinations with other criteria) and/or as a consideration in individual company analysis.

*Period: Trailing 12 Months*


#### `AltmanZPriv`

There are three versions of the Altman Z-Score. In all cases higher values are better, but the cutoffs vary. See the descriptions of each below

AltmanZOrig

Z = 1.2 * AltmanX1 + 1.4 * AltmanX2 + 3.3 * AltmanX3 + 0.6 * AltmanX4 + 1.0 * AltmanX5

Initially, Altman worked with a cutoff of 2.675; scores below that were presumed to signify significant bankruptcy risk. The probability of accuracy was very high in the percentage of bankruptcies it predicted, but at the cost of too many (in Altman?s judgment) Type II errors (flagging firms as distressed that do not wind up filing bankruptcy). Accordingly, Altman recommends use of a cutoff of 1.81.

AltmanZPriv

Z = .717 * AltmanX1 + .847 * AltmanX2 + 3.107 * AltmanX3 + 0.42 * AltmanX4Rev + .998 * AltmanX5

While privately-owned companies are not included in our database, we understand that we must necessarily depart from literal application of the model if we are to make it useful to assess stock prospects. Accordingly, users may want to consider this variation in cases where they believe the current market value of equity may be temporarily distorted and not indicative of the value the equity is likely to have over a longer term. Altman recommends use of a score of 1.23 or greater

AltmanZNonManu

Z = 6.56 * AltmanX1 + 3.26 * AltmanX2 + 6.72 * AltmanX3 + 1.05 * AltmanX4 

Variables X1 through X4 are the same as in the original model. X5 is omitted in order to minimize potential industry effect, which can be troublesome as comparisons from one to another become less apples-to-apples. Altman recommends use of a cutoff score of 1.10.

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

Background

The Z-Score, created by Prof. Edward Altman, is a well-established model designed for and used to predict corporate bankruptcy at least a year in advance. Traditionally, as of the time Altman developed the model, credit analysis had been conducted mainly on a qualitative basis. And to the extent any quantitative work was done, the value of ratio analysis had been called into question by many in the academic community who favored more rigorous statistical techniques. Altman regarded the main innovations of his research as showing the value of ratio analysis and showing the value of an approach that used multiple factors in a single model, as opposed to the single-factor inquiries used by others who had been willing to work with ratios. It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

IMPORTANT CAVEATS:

The Altman Z Score models have been noticed in the equity investment community and many seek to use this as part of the stock selection and analysis process. Accordingly, we are making it available. It is very important to note, however, that the model was developed for purposes of predicting bankruptcy. Equity returns, a critical dependent variable in the research of others who developed valuable models for use by equity investors, was not considered as part of Altman?s research. Equity investors who are interested in the Z score are necessarily presuming there is a relationship between bankruptcy and poor share price performance. In a big-picture sense, we can logically assume this is the case. But Altman did not research the timing and pace at which share price deterioration preceded bankruptcy. Note, too, that even within the area of bankruptcy prediction, Altman later came up with what he regarded as a superior model, a Zeta score. But because this was developed for a particular client and sold to them for their proprietary use, had has not divulged its parameters with enough specificity to be implemented by anyone except the client.

Accordingly, we cannot and do not suggest that your use of Z-score in the manner prescribed by Altman will enhance your strategy design. If you wish to work with Z score, consider using it in different ways (i.e. different score cutoffs and combinations with other criteria) and/or as a consideration in individual company analysis.

*Period: Trailing 12 Months*


#### `AltmanZNonManu`

There are three versions of the Altman Z-Score. In all cases higher values are better, but the cutoffs vary. See the descriptions of each below

AltmanZOrig

Z = 1.2 * AltmanX1 + 1.4 * AltmanX2 + 3.3 * AltmanX3 + 0.6 * AltmanX4 + 1.0 * AltmanX5

Initially, Altman worked with a cutoff of 2.675; scores below that were presumed to signify significant bankruptcy risk. The probability of accuracy was very high in the percentage of bankruptcies it predicted, but at the cost of too many (in Altman?s judgment) Type II errors (flagging firms as distressed that do not wind up filing bankruptcy). Accordingly, Altman recommends use of a cutoff of 1.81.

AltmanZPriv

Z = .717 * AltmanX1 + .847 * AltmanX2 + 3.107 * AltmanX3 + 0.42 * AltmanX4Rev + .998 * AltmanX5

While privately-owned companies are not included in our database, we understand that we must necessarily depart from literal application of the model if we are to make it useful to assess stock prospects. Accordingly, users may want to consider this variation in cases where they believe the current market value of equity may be temporarily distorted and not indicative of the value the equity is likely to have over a longer term. Altman recommends use of a score of 1.23 or greater

AltmanZNonManu

Z = 6.56 * AltmanX1 + 3.26 * AltmanX2 + 6.72 * AltmanX3 + 1.05 * AltmanX4 

Variables X1 through X4 are the same as in the original model. X5 is omitted in order to minimize potential industry effect, which can be troublesome as comparisons from one to another become less apples-to-apples. Altman recommends use of a cutoff score of 1.10.

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

Background

The Z-Score, created by Prof. Edward Altman, is a well-established model designed for and used to predict corporate bankruptcy at least a year in advance. Traditionally, as of the time Altman developed the model, credit analysis had been conducted mainly on a qualitative basis. And to the extent any quantitative work was done, the value of ratio analysis had been called into question by many in the academic community who favored more rigorous statistical techniques. Altman regarded the main innovations of his research as showing the value of ratio analysis and showing the value of an approach that used multiple factors in a single model, as opposed to the single-factor inquiries used by others who had been willing to work with ratios. It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

It was created in the late 1960s based on multiple discriminant analysis conducted on a sample of 66 publicly traded companies, 33 of which had declared bankruptcy between 1946 and 33 of which did not. In selecting companies for the latter control sample, Altman aimed for a paired sample stratified by industry and size.

IMPORTANT CAVEATS:

The Altman Z Score models have been noticed in the equity investment community and many seek to use this as part of the stock selection and analysis process. Accordingly, we are making it available. It is very important to note, however, that the model was developed for purposes of predicting bankruptcy. Equity returns, a critical dependent variable in the research of others who developed valuable models for use by equity investors, was not considered as part of Altman?s research. Equity investors who are interested in the Z score are necessarily presuming there is a relationship between bankruptcy and poor share price performance. In a big-picture sense, we can logically assume this is the case. But Altman did not research the timing and pace at which share price deterioration preceded bankruptcy. Note, too, that even within the area of bankruptcy prediction, Altman later came up with what he regarded as a superior model, a Zeta score. But because this was developed for a particular client and sold to them for their proprietary use, had has not divulged its parameters with enough specificity to be implemented by anyone except the client.

Accordingly, we cannot and do not suggest that your use of Z-score in the manner prescribed by Altman will enhance your strategy design. If you wish to work with Z score, consider using it in different ways (i.e. different score cutoffs and combinations with other criteria) and/or as a consideration in individual company analysis.

*Period: Trailing 12 Months*


#### `AltmanX1`

This is a measure of the net liquid assets a firm has, its working capital. It measures readily available assets (cash and other assets expected to be converted to cash in the near term, such as receivables and inventories) over and above liabilities that are expected to be paid quickly (such as payables and short-term debt). It's scaled on to total assets in order to facilitate comparison among different size firms. Edward Altman, creator of the Altman Z score, maintains that deterioration in this ratio may indicate impending financial distress.

Our Formula

AltmanX1 = WorkCapQ / AstTotQ 

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

*Period: Trailing 12 Months*


#### `AltmanX2`

This is not the typical definition of retained earnings; the portion of annual profits not paid to shareholders as dividends. We use the balance sheet item showing the cumulative retained earnings over the life of the company, scaled by total assets to facilitate comparison among different size companies. The measure, used by Prof. Edward Altman as part of the Z Score he developed, discriminates against newer companies that have not had sufficient time to accumulate substantial retained earnings. That's intentional. Altman points out that short history tends to be associated with greater risk of failure. In addition, this ratio measures the extent to which firms financed their assets through retention of profits, as opposed to debt

Our Formula

AltmanX2 = RetainedEarnQ/AstTotQ

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

*Period: Trailing 12 Months*


#### `AltmanX3`

This metric, which measures the productivity of a firm's assets, independent of taxation or leverage, is logically equivalent to asset turnover except that it measures the rapidity with which assets are converted to EBIT rather than sales.

Our Formula

AltmanX3 = EBITTTM/ AstTotQ

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

*Period: Trailing 12 Months*


#### `AltmanX4`

This measures the extent to which the value of assets can deteriorate before triggering insolvency. We do not have access to the market value of preferred equity so we must necessarily use the book value of preferred.

Our Formula

AltmanX4 = (MktCap+PfdEquityQ)/ LiabTotQ

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

*Period: Trailing 12 Months*


#### `AltmanX4Rev`

Revised AltmanX4 used by AltmanZPriv

Our Formula

AltmanX4Rev = (ComEqQ+PfdEquityQ)/ LiabTotQ

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ

*Period: Trailing 12 Months*


#### `AltmanX5`

This is substantially the same as the conventional asset turnover metric except that it is scaled on the basis of the latest total asset figure, to be consistent with other measures used in the Z Score model developed by Professor Edward Altman. It measures the sales-generating ability of a firm's assets.

Our Formula

AltmanX5 = SalesTTM/ AstTotQ

NOTE: when N/A's are encountered during preliminary reports the preliminary data is excluded by falling back to previous quarter

Related Factors:

AltmanX1
AltmanX2
AltmanX3
AltmanX4
AltmanX5
AltmanX4Rev
AltmanZ Factors

*Period: Trailing 12 Months*



## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `PiotroskiF` | `PiotFScore` | Piotroski F-Score. The dictionary code is `PiotFScore`; the spelled-out form is not a code. |
| `AltmanZ` | `AltmanZOrig` | Use the specific variant: `AltmanZOrig`, `AltmanZPriv`, or `AltmanZNonManu`. A bare Altman Z is not a code. |
| `EarnYield%TTM` | `EarnYield` | Yield factors are computed at the current price, so they take no period suffix. |
| `FCFYield%TTM` | `FCFYield` | No period suffix; the yield is already a current-price figure. |
| `OCFYield%TTM` | `OCFYield` | No period suffix. |
| `EBITDAYield%TTM` | `EBITDAYield` | No period suffix. |
| `OpIncYield%TTM` | `OpIncYield` | No period suffix. |
| `ShrYield%TTM` | `ShareholderYield` | Shareholder yield (dividends + buybacks) is `ShareholderYield`, with no suffix. |
| `DivYield%TTM` | `Yield` | Indicated dividend yield is simply `Yield` (or `YieldInd`); there is no per-period dividend-yield factor. |
| `MarketCap` | `MktCap` | Market capitalization is `MktCap`. |
| `EnterpriseVal` | `EV` | Enterprise value is `EV` (per-share is `EVPS`). |
| `PEG` | `PEGLT` | Use `PEGLT` (long-term) or `PEGST` (short-term); a bare three-letter form is not a code. |
| `GrossMargin` | `GMgn%` | Gross margin function/base code is `GMgn%`. |
| `CurrentRatio` | `CurRatio` | Current ratio is `CurRatio`. |
| `PayoutRatio` | `PayRatio` | Dividend payout ratio is `PayRatio` (5-year average is `PayRatio5Y`). |

## See Also

- [Financials](financials.md) - raw filing line items the ratios are built from.
- [Estimates](estimates.md) - analyst-estimate consensus ratios and surprises.
- [Technical](technical.md) - price/volume functions and the formula language.
- [Advanced Functions](advanced-functions.md) - looping, regression, and helper operators.

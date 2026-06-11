<!-- name-whitelist: ItemName NAHandling barsAgo Q PQ PYQ PTM A PY Gr%PQ Gr%PYQ Gr%TTM Gr%A Gr%3Y Gr%5Y PSQ PSA %SalesQ %SalesA 3YAvg 5YAvg -->
# Financials — Portfolio123 Reference

This file documents the **Financials** category of the Portfolio123 Factor Reference: income-statement, balance-sheet, and cash-flow line items. Each line item is exposed both as a function (e.g. `Sales(0, TTM)`) and as a family of pre-built factors (e.g. `SalesTTM`, `SalesGr%PYQ`). For valuation and profitability ratios built on top of these items see [Ratios & Statistics](ratios-statistics.md); for analyst estimates see [Estimates](estimates.md); for the formula-language rules that govern the `offset`/`type` arguments see [Misc](misc.md).

Coverage: **101 functions / 2739 factors** — extracted from the official Factor Reference on 2026-06-09.

## How line-item functions work

Every Financials line item is available through two access methods: a function call and a set of pre-built factors.

```p123
ItemName(offset, type[, NAHandling])
```

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

For QTR and ANN types the value is taken straight from the filing at the given offset. TTM values are computed two ways: income-statement and cash-flow items sum the trailing four quarters, while balance-sheet items average the trailing four quarters.

Each item also auto-generates pre-built factors (no parentheses). The most common suffixes:

| Suffix | Meaning | Corresponding call |
|---|---|---|
| `Q` | Recent quarter | `(0, QTR)` |
| `PQ` | Prior quarter | `(1, QTR)` |
| `PYQ` | Prior-year quarter | `(4, QTR)` |
| `TTM` | Trailing twelve months | `(0, TTM)` |
| `PTM` | Prior trailing twelve months | `(4, TTM)` |
| `A` | Recent annual | `(0, ANN)` |
| `PY` | Prior year | `(1, ANN)` |
| `Gr%PQ` | Growth vs prior quarter | `(0, QTR) / (1, QTR)` |
| `Gr%PYQ` | Growth vs prior-year quarter | `(0, QTR) / (4, QTR)` |
| `Gr%TTM` | Growth vs prior TTM | `(0, TTM) / (4, TTM)` |
| `Gr%A` | Growth vs prior annual | `(0, ANN) / (1, ANN)` |
| `Gr%3Y` | 3-year annualized growth | `(0, ANN) / (3, ANN) annualized` |
| `Gr%5Y` | 5-year annualized growth | `(0, ANN) / (5, ANN) annualized` |
| `PSQ` | Per share (quarterly) | `(0, QTR) / Shares(0, QTR)` |
| `PSA` | Per share (annual) | `(0, ANN) / Shares(0, ANN)` |
| `%SalesQ` | Percent of quarterly sales | `(0, QTR) / Sales(0, QTR)` |
| `%SalesA` | Percent of annual sales | `(0, ANN) / Sales(0, ANN)` |
| `3YAvg` | 3-year average | `LoopAvg("function(CTR, ANN)", 3)` |
| `5YAvg` | 5-year average | `LoopAvg("function(CTR, ANN)", 5)` |

Availability varies by item; `PTM` uses interim periods (offset 4, not 1). The full per-item factor lists appear under each item below.

## Contents

- [How line-item functions work](#how-line-item-functions-work)
- [Income Statement](#income-statement)
- [Balance Sheet](#balance-sheet)
  - [Assets-Current](#assets-current)
  - [Assets-Noncurrent](#assets-noncurrent)
  - [Liabilities-Current](#liabilities-current)
  - [Liabilities-Noncurrent](#liabilities-noncurrent)
  - [Shareholders Equity](#shareholders-equity)
  - [Shares](#shares)
- [Cash Flow Statement](#cash-flow-statement)
  - [Operating](#operating)
  - [Investing](#investing)
  - [Financing](#financing)
  - [Summary](#summary)
- [Appendix: Vendor Line-Item Mapping](#appendix-vendor-line-item-mapping)
  - [Income Statement (mapping)](#income-statement-mapping)
  - [Balance Sheet (mapping)](#balance-sheet-mapping)
  - [Cash Flow Statement (mapping)](#cash-flow-statement-mapping)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

## Income Statement

#### `Amort(offset, type[, NAHandling])`
```p123
Amort(offset, type[, NAHandling])
```

Amortization of Intangibles is the reduction of value of an non-physical asset over time. It is intended to capture, for example, the nature of a copyright to typically grow less profitable as time goes on.

In practical terms, an external analyst will only rarely need to separate this from depreciation; the income statement effects of them are typically what we care about.

Nonetheless, cases where intangible assets are material relative to physical assets might make this useful. Disney's copyrights comes to mind, and Coca Cola's brand is another.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AmortQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Latest Quarter |
| `AmortPQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Previous Quarter |
| `AmortPYQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Previous Quarter 1 Year Ago |
| `AmortTTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Trailing 12 Months |
| `AmortPTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Previous Trailing 12 Months |
| `AmortA` | Write down value of non-physical assets like copyrights, patents, and brands. | Latest Year |
| `AmortPY` | Write down value of non-physical assets like copyrights, patents, and brands. | Previous Year |
| `AmortGr%PQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Q vs Previous Q Growth |
| `AmortGr%PYQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Q vs 1 year ago Q Growth |
| `AmortGr%TTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Trailing Twelve Months Growth |
| `AmortGr%PQTTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Trailing Twelve Months Growth 1Q Ago |
| `AmortGr%A` | Write down value of non-physical assets like copyrights, patents, and brands. | Growth Annual |
| `AmortGr%3Y` | Write down value of non-physical assets like copyrights, patents, and brands. | Three Year Annualized Growth |
| `AmortGr%5Y` | Write down value of non-physical assets like copyrights, patents, and brands. | Five Year Annualized Growth |
| `AmortGr%10Y` | Write down value of non-physical assets like copyrights, patents, and brands. | Ten Year Annualized Growth |
| `AmortRSD%ANN` | Write down value of non-physical assets like copyrights, patents, and brands. | Ten Year Relative Standard Deviation |
| `AmortRSD%TTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Five Year Relative Standard Deviation |
| `AmortRegEstANN` | Write down value of non-physical assets like copyrights, patents, and brands. | Ten Year Regression Estimate |
| `AmortRegEstTTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Five Year Regression Estimate |
| `AmortRegGr%ANN` | Write down value of non-physical assets like copyrights, patents, and brands. | Ten Year Regression Estimate |
| `AmortRegGr%TTM` | Write down value of non-physical assets like copyrights, patents, and brands. | Five Year Regression Growth |
| `AmortPSQ` | Write down value of non-physical assets like copyrights, patents, and brands. | Quarterly Per Share |
| `AmortPSA` | Write down value of non-physical assets like copyrights, patents, and brands. | Annual Per Share |
| `Amort%SalesQ` | Write down value of non-physical assets like copyrights, patents, and brands. | % of Quarterly Sales |
| `Amort%SalesA` | Write down value of non-physical assets like copyrights, patents, and brands. | % of Annual Sales |
| `Amort%AssetsQ` | Write down value of non-physical assets like copyrights, patents, and brands. | % of Quarterly Assets |
| `Amort%AssetsA` | Write down value of non-physical assets like copyrights, patents, and brands. | % of Annual Assets |
| `Amort3YAvg` | Write down value of non-physical assets like copyrights, patents, and brands. | Three Year Average |
| `Amort5YAvg` | Write down value of non-physical assets like copyrights, patents, and brands. | Five Year Average |

#### `CostG(offset, type[, NAHandling])`
```p123
CostG(offset, type[, NAHandling])
```

Cost of Goods Sold (COGS) represents the direct expenses related to producing goods sold by a company. This encompasses the material costs and labor directly involved in creating products and services. COGS does not account for indirect expenses like distribution and sales force costs. We offer two variations of COGS to accommodate different analytical needs: CostG and CostG_GAAP.

CostG reflects the traditional calculation of COGS, focusing solely on the direct costs associated with production. This version is calculated as:
`CostG = Direct Materials + Direct Labor`. It's primarily used when analyzing a company's core operational efficiency, excluding the effects of depreciation and amortization.

CostG_GAAP, on the other hand, includes depreciation and amortization expenses in addition to the direct costs. This calculation aligns with the Generally Accepted Accounting Principles (GAAP) and is formulated as:
`CostG_GAAP = Direct Materials + Direct Labor + Depreciation + Amortization`. This version is particularly useful for investors and traders seeking a more comprehensive view of a company's cost structure, including the consumption of capital and intangible assets over time.

The choice between CostG and CostG_GAAP depends on your trading or investment strategy. If you're focusing on short-term operational efficiencies and cost control, CostG might be more relevant. However, for a holistic, long-term investment analysis that accounts for the depreciation of physical assets and amortization of intangible assets, CostG_GAAP provides a more complete picture.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CostGQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Latest Quarter |
| `CostGPQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Previous Quarter |
| `CostGPYQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Previous Quarter 1 Year Ago |
| `CostGTTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Trailing 12 Months |
| `CostGPTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Previous Trailing 12 Months |
| `CostGA` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Latest Year |
| `CostGPY` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Previous Year |
| `CostGGr%PQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Q vs Previous Q Growth |
| `CostGGr%PYQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Q vs 1 year ago Q Growth |
| `CostGGr%TTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Trailing Twelve Months Growth |
| `CostGGr%PQTTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Trailing Twelve Months Growth 1Q Ago |
| `CostGGr%A` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Growth Annual |
| `CostGGr%3Y` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Three Year Annualized Growth |
| `CostGGr%5Y` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Five Year Annualized Growth |
| `CostGGr%10Y` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Ten Year Annualized Growth |
| `CostGRSD%ANN` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Ten Year Relative Standard Deviation |
| `CostGRSD%TTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Five Year Relative Standard Deviation |
| `CostGRegEstANN` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Ten Year Regression Estimate |
| `CostGRegEstTTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Five Year Regression Estimate |
| `CostGRegGr%ANN` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Ten Year Regression Estimate |
| `CostGRegGr%TTM` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Five Year Regression Growth |
| `CostGPSQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Quarterly Per Share |
| `CostGPSA` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Annual Per Share |
| `CostG%SalesQ` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | % of Quarterly Sales |
| `CostG%SalesA` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | % of Annual Sales |
| `CostG3YAvg` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Three Year Average |
| `CostG5YAvg` | Direct production expenses. CostG = Direct Materials + Direct Labor (excludes D&A). | Five Year Average |

#### `CostG_GAAP(offset, type[, NAHandling])`
```p123
CostG_GAAP(offset, type[, NAHandling])
```

Cost of Goods Sold (COGS) represents the direct expenses related to producing goods sold by a company. This encompasses the material costs and labor directly involved in creating products and services. COGS does not account for indirect expenses like distribution and sales force costs. We offer two variations of COGS to accommodate different analytical needs: CostG and CostG_GAAP.

CostG reflects the traditional calculation of COGS, focusing solely on the direct costs associated with production. This version is calculated as:
`CostG = Direct Materials + Direct Labor`. It's primarily used when analyzing a company's core operational efficiency, excluding the effects of depreciation and amortization.

CostG_GAAP, on the other hand, includes depreciation and amortization expenses in addition to the direct costs. This calculation aligns with the Generally Accepted Accounting Principles (GAAP) and is formulated as:
`CostG_GAAP = Direct Materials + Direct Labor + Depreciation + Amortization`. This version is particularly useful for investors and traders seeking a more comprehensive view of a company's cost structure, including the consumption of capital and intangible assets over time.

The choice between CostG and CostG_GAAP depends on your trading or investment strategy. If you're focusing on short-term operational efficiencies and cost control, CostG might be more relevant. However, for a holistic, long-term investment analysis that accounts for the depreciation of physical assets and amortization of intangible assets, CostG_GAAP provides a more complete picture.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CostG_GAAPQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Latest Quarter |
| `CostG_GAAPPQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Previous Quarter |
| `CostG_GAAPPYQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Previous Quarter 1 Year Ago |
| `CostG_GAAPTTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Trailing 12 Months |
| `CostG_GAAPPTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Previous Trailing 12 Months |
| `CostG_GAAPA` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Latest Year |
| `CostG_GAAPPY` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Previous Year |
| `CostG_GAAPGr%PQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Q vs Previous Q Growth |
| `CostG_GAAPGr%PYQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Q vs 1 year ago Q Growth |
| `CostG_GAAPGr%TTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Trailing Twelve Months Growth |
| `CostG_GAAPGr%PQTTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Trailing Twelve Months Growth 1Q Ago |
| `CostG_GAAPGr%A` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Growth Annual |
| `CostG_GAAPGr%3Y` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Three Year Annualized Growth |
| `CostG_GAAPGr%5Y` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Five Year Annualized Growth |
| `CostG_GAAPGr%10Y` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Ten Year Annualized Growth |
| `CostG_GAAPRSD%ANN` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Ten Year Relative Standard Deviation |
| `CostG_GAAPRSD%TTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Five Year Relative Standard Deviation |
| `CostG_GAAPRegEstANN` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Ten Year Regression Estimate |
| `CostG_GAAPRegEstTTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Five Year Regression Estimate |
| `CostG_GAAPRegGr%ANN` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Ten Year Regression Estimate |
| `CostG_GAAPRegGr%TTM` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Five Year Regression Growth |
| `CostG_GAAPPSQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Quarterly Per Share |
| `CostG_GAAPPSA` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Annual Per Share |
| `CostG_GAAP%SalesQ` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | % of Quarterly Sales |
| `CostG_GAAP%SalesA` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | % of Annual Sales |
| `CostG_GAAP3YAvg` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Three Year Average |
| `CostG_GAAP5YAvg` | Direct production expenses. CostG_GAAP = Direct Materials + Direct Labor + D&A. | Five Year Average |

#### `DepAmort(offset, type[, NAHandling])`
```p123
DepAmort(offset, type[, NAHandling])
```

Depreciation and Amortization from Income Statement is the sum of the depreciation and amortization expenses. Depreciation and amortization are typically either reported on the income statement or on the cash flow statement. This item is specifically what is reported on the income statement.

Other functions are available both for the specific cash-flow depreciation and depreciation from whereever it is reported.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DepAmortQ` | The sum of D&A expenses as reported specifically on income statement. | Latest Quarter |
| `DepAmortPQ` | The sum of D&A expenses as reported specifically on income statement. | Previous Quarter |
| `DepAmortPYQ` | The sum of D&A expenses as reported specifically on income statement. | Previous Quarter 1 Year Ago |
| `DepAmortTTM` | The sum of D&A expenses as reported specifically on income statement. | Trailing 12 Months |
| `DepAmortPTM` | The sum of D&A expenses as reported specifically on income statement. | Previous Trailing 12 Months |
| `DepAmortA` | The sum of D&A expenses as reported specifically on income statement. | Latest Year |
| `DepAmortPY` | The sum of D&A expenses as reported specifically on income statement. | Previous Year |
| `DepAmortGr%PQ` | The sum of D&A expenses as reported specifically on income statement. | Q vs Previous Q Growth |
| `DepAmortGr%PYQ` | The sum of D&A expenses as reported specifically on income statement. | Q vs 1 year ago Q Growth |
| `DepAmortGr%TTM` | The sum of D&A expenses as reported specifically on income statement. | Trailing Twelve Months Growth |
| `DepAmortGr%PQTTM` | The sum of D&A expenses as reported specifically on income statement. | Trailing Twelve Months Growth 1Q Ago |
| `DepAmortGr%A` | The sum of D&A expenses as reported specifically on income statement. | Growth Annual |
| `DepAmortGr%3Y` | The sum of D&A expenses as reported specifically on income statement. | Three Year Annualized Growth |
| `DepAmortGr%5Y` | The sum of D&A expenses as reported specifically on income statement. | Five Year Annualized Growth |
| `DepAmortGr%10Y` | The sum of D&A expenses as reported specifically on income statement. | Ten Year Annualized Growth |
| `DepAmortRSD%ANN` | The sum of D&A expenses as reported specifically on income statement. | Ten Year Relative Standard Deviation |
| `DepAmortRSD%TTM` | The sum of D&A expenses as reported specifically on income statement. | Five Year Relative Standard Deviation |
| `DepAmortRegEstANN` | The sum of D&A expenses as reported specifically on income statement. | Ten Year Regression Estimate |
| `DepAmortRegEstTTM` | The sum of D&A expenses as reported specifically on income statement. | Five Year Regression Estimate |
| `DepAmortRegGr%ANN` | The sum of D&A expenses as reported specifically on income statement. | Ten Year Regression Estimate |
| `DepAmortRegGr%TTM` | The sum of D&A expenses as reported specifically on income statement. | Five Year Regression Growth |
| `DepAmortPSQ` | The sum of D&A expenses as reported specifically on income statement. | Quarterly Per Share |
| `DepAmortPSA` | The sum of D&A expenses as reported specifically on income statement. | Annual Per Share |
| `DepAmort%SalesQ` | The sum of D&A expenses as reported specifically on income statement. | % of Quarterly Sales |
| `DepAmort%SalesA` | The sum of D&A expenses as reported specifically on income statement. | % of Annual Sales |
| `DepAmort3YAvg` | The sum of D&A expenses as reported specifically on income statement. | Three Year Average |
| `DepAmort5YAvg` | The sum of D&A expenses as reported specifically on income statement. | Five Year Average |

#### `EBIT(offset, type[, NAHandling])`
```p123
EBIT(offset, type[, NAHandling])
```

Earnings Before Interest and Taxes is operating income including depreciation and amortization.

Our data provider may make a distinction for certain stocks between EBIT and operating income. In particular, there are some things that may or may not be reported as operational expenses. For example, in reporting EBIT, our data provider may remove idle plant or moving expense from operating income regardless of where on the income statement a company reports them. We ignore those exceptions and simply use operating income as EBIT.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `EBITQ` | Operating income including depreciation and amortization. | Latest Quarter |
| `EBITPQ` | Operating income including depreciation and amortization. | Previous Quarter |
| `EBITPYQ` | Operating income including depreciation and amortization. | Previous Quarter 1 Year Ago |
| `EBITTTM` | Operating income including depreciation and amortization. | Trailing 12 Months |
| `EBITPTM` | Operating income including depreciation and amortization. | Previous Trailing 12 Months |
| `EBITA` | Operating income including depreciation and amortization. | Latest Year |
| `EBITPY` | Operating income including depreciation and amortization. | Previous Year |
| `EBITGr%PQ` | Operating income including depreciation and amortization. | Q vs Previous Q Growth |
| `EBITGr%PYQ` | Operating income including depreciation and amortization. | Q vs 1 year ago Q Growth |
| `EBITGr%TTM` | Operating income including depreciation and amortization. | Trailing Twelve Months Growth |
| `EBITGr%PQTTM` | Operating income including depreciation and amortization. | Trailing Twelve Months Growth 1Q Ago |
| `EBITGr%A` | Operating income including depreciation and amortization. | Growth Annual |
| `EBITGr%3Y` | Operating income including depreciation and amortization. | Three Year Annualized Growth |
| `EBITGr%5Y` | Operating income including depreciation and amortization. | Five Year Annualized Growth |
| `EBITGr%10Y` | Operating income including depreciation and amortization. | Ten Year Annualized Growth |
| `EBITRSD%ANN` | Operating income including depreciation and amortization. | Ten Year Relative Standard Deviation |
| `EBITRSD%TTM` | Operating income including depreciation and amortization. | Five Year Relative Standard Deviation |
| `EBITRegEstANN` | Operating income including depreciation and amortization. | Ten Year Regression Estimate |
| `EBITRegEstTTM` | Operating income including depreciation and amortization. | Five Year Regression Estimate |
| `EBITRegGr%ANN` | Operating income including depreciation and amortization. | Ten Year Regression Estimate |
| `EBITRegGr%TTM` | Operating income including depreciation and amortization. | Five Year Regression Growth |
| `EBITPSQ` | Operating income including depreciation and amortization. | Quarterly Per Share |
| `EBITPSA` | Operating income including depreciation and amortization. | Annual Per Share |
| `EBIT%SalesQ` | Operating income including depreciation and amortization. | % of Quarterly Sales |
| `EBIT%SalesA` | Operating income including depreciation and amortization. | % of Annual Sales |
| `EBIT3YAvg` | Operating income including depreciation and amortization. | Three Year Average |
| `EBIT5YAvg` | Operating income including depreciation and amortization. | Five Year Average |

#### `EBITDA(offset, type[, NAHandling])`
```p123
EBITDA(offset, type[, NAHandling])
```

Earnings Before Interest, Taxes, Depreciation and Amortization is operating income excluding depreciation and amortization. If this item is N/A, we add back depreciation and amortization to operating income to come up with EBITDA.

Our data provider may make a distinction for certain stocks between EBITDA and operating income before depreciation and amortization. In particular, there are some things that may or may not be reported as operational expenses. For example, in reporting EBITDA, our data provider may remove idle plant or moving expense from operating income regardless of where on the income statement a company reports them. We ignore those exceptions and simply use operating income before depreciation and amortization as EBITDA.

Users should also consider whether the effects of depreciation will muddy an estimate of operating income. This would be the primary reason for using EBITDA rather than one of the other options.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `EBITDAQ` | Operating income excluding non-cash expenses D&A. | Latest Quarter |
| `EBITDAPQ` | Operating income excluding non-cash expenses D&A. | Previous Quarter |
| `EBITDAPYQ` | Operating income excluding non-cash expenses D&A. | Previous Quarter 1 Year Ago |
| `EBITDATTM` | Operating income excluding non-cash expenses D&A. | Trailing 12 Months |
| `EBITDAPTM` | Operating income excluding non-cash expenses D&A. | Previous Trailing 12 Months |
| `EBITDAA` | Operating income excluding non-cash expenses D&A. | Latest Year |
| `EBITDAPY` | Operating income excluding non-cash expenses D&A. | Previous Year |
| `EBITDAGr%PQ` | Operating income excluding non-cash expenses D&A. | Q vs Previous Q Growth |
| `EBITDAGr%PYQ` | Operating income excluding non-cash expenses D&A. | Q vs 1 year ago Q Growth |
| `EBITDAGr%TTM` | Operating income excluding non-cash expenses D&A. | Trailing Twelve Months Growth |
| `EBITDAGr%PQTTM` | Operating income excluding non-cash expenses D&A. | Trailing Twelve Months Growth 1Q Ago |
| `EBITDAGr%A` | Operating income excluding non-cash expenses D&A. | Growth Annual |
| `EBITDAGr%3Y` | Operating income excluding non-cash expenses D&A. | Three Year Annualized Growth |
| `EBITDAGr%5Y` | Operating income excluding non-cash expenses D&A. | Five Year Annualized Growth |
| `EBITDAGr%10Y` | Operating income excluding non-cash expenses D&A. | Ten Year Annualized Growth |
| `EBITDARSD%ANN` | Operating income excluding non-cash expenses D&A. | Ten Year Relative Standard Deviation |
| `EBITDARSD%TTM` | Operating income excluding non-cash expenses D&A. | Five Year Relative Standard Deviation |
| `EBITDARegEstANN` | Operating income excluding non-cash expenses D&A. | Ten Year Regression Estimate |
| `EBITDARegEstTTM` | Operating income excluding non-cash expenses D&A. | Five Year Regression Estimate |
| `EBITDARegGr%ANN` | Operating income excluding non-cash expenses D&A. | Ten Year Regression Estimate |
| `EBITDARegGr%TTM` | Operating income excluding non-cash expenses D&A. | Five Year Regression Growth |
| `EBITDAPSQ` | Operating income excluding non-cash expenses D&A. | Quarterly Per Share |
| `EBITDAPSA` | Operating income excluding non-cash expenses D&A. | Annual Per Share |
| `EBITDA%SalesQ` | Operating income excluding non-cash expenses D&A. | % of Quarterly Sales |
| `EBITDA%SalesA` | Operating income excluding non-cash expenses D&A. | % of Annual Sales |
| `EBITDA3YAvg` | Operating income excluding non-cash expenses D&A. | Three Year Average |
| `EBITDA5YAvg` | Operating income excluding non-cash expenses D&A. | Five Year Average |

#### `FundsFromOp(offset, type[, NAHandling])`
```p123
FundsFromOp(offset, type[, NAHandling])
```

Represents the gross cash flow from the company's operations derived by reconciling net income before the effects of non-cash items.

For companies following the "Direct method" of cash flow presentation where cash flows from operation is derived through cash inflows and outflows, this item represents the total amount and as such, is equal to OperCashFl.

For companies adopting IFRS or other accounting standard aside from US GAAP, this Item includes Interest and/or dividends received and Interest paid reported outside cash flow from operations. Under US GAAP, said items are always included in cash flows from operations.

It includes:

- Net income (starting line)

- Depreciation, depletion & amortization (Cash Flow)

- Deferred taxes & investment tax credits (Cash Flow)

- Other operating funds (Cash Flow)

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `FundsFromOpQ` | Funds From Operations | Latest Quarter |
| `FundsFromOpPQ` | Funds From Operations | Previous Quarter |
| `FundsFromOpPYQ` | Funds From Operations | Previous Quarter 1 Year Ago |
| `FundsFromOpTTM` | Funds From Operations | Trailing 12 Months |
| `FundsFromOpPTM` | Funds From Operations | Previous Trailing 12 Months |
| `FundsFromOpA` | Funds From Operations | Latest Year |
| `FundsFromOpPY` | Funds From Operations | Previous Year |
| `FundsFromOpGr%PQ` | Funds From Operations | Q vs Previous Q Growth |
| `FundsFromOpGr%PYQ` | Funds From Operations | Q vs 1 year ago Q Growth |
| `FundsFromOpGr%TTM` | Funds From Operations | Trailing Twelve Months Growth |
| `FundsFromOpGr%PQTTM` | Funds From Operations | Trailing Twelve Months Growth 1Q Ago |
| `FundsFromOpGr%A` | Funds From Operations | Growth Annual |
| `FundsFromOpGr%3Y` | Funds From Operations | Three Year Annualized Growth |
| `FundsFromOpGr%5Y` | Funds From Operations | Five Year Annualized Growth |
| `FundsFromOpGr%10Y` | Funds From Operations | Ten Year Annualized Growth |
| `FundsFromOpRSD%ANN` | Funds From Operations | Ten Year Relative Standard Deviation |
| `FundsFromOpRSD%TTM` | Funds From Operations | Five Year Relative Standard Deviation |
| `FundsFromOpRegEstANN` | Funds From Operations | Ten Year Regression Estimate |
| `FundsFromOpRegEstTTM` | Funds From Operations | Five Year Regression Estimate |
| `FundsFromOpRegGr%ANN` | Funds From Operations | Ten Year Regression Estimate |
| `FundsFromOpRegGr%TTM` | Funds From Operations | Five Year Regression Growth |
| `FundsFromOpPSQ` | Funds From Operations | Quarterly Per Share |
| `FundsFromOpPSA` | Funds From Operations | Annual Per Share |
| `FundsFromOp%SalesQ` | Funds From Operations | % of Quarterly Sales |
| `FundsFromOp%SalesA` | Funds From Operations | % of Annual Sales |
| `FundsFromOp%AssetsQ` | Funds From Operations | % of Quarterly Assets |
| `FundsFromOp%AssetsA` | Funds From Operations | % of Annual Assets |
| `FundsFromOp3YAvg` | Funds From Operations | Three Year Average |
| `FundsFromOp5YAvg` | Funds From Operations | Five Year Average |

#### `GrossProfit(offset, type[, NAHandling])`
```p123
GrossProfit(offset, type[, NAHandling])
```

Gross profit is the profit a company makes after deducting the costs associated with producing and selling its products or the costs associated with its services. In Portfolio123, we distinguish between two versions of gross profit calculations: GrossProfit and GrossProfit_GAAP. The latter incorporates depreciation and amortization into the cost of goods sold (COGS), reflecting a more comprehensive measure of production costs under Generally Accepted Accounting Principles (GAAP).

The choice between using GrossProfit and GrossProfit_GAAP depends on the analytical needs of users focusing on trading systems and investment strategies. GrossProfit provides a direct measure of profitability excluding depreciation and amortization, ideal for analyzing operational efficiency. GrossProfit_GAAP, by including these non-cash expenses, offers a more conservative view of profitability, aligning closer with GAAP standards and potentially providing a more realistic assessment of long-term investment sustainability.

Formulas:

Sales - CostG for GrossProfit
Sales - CostG_GAAP for GrossProfit_GAAP

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `GrossProfitQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Latest Quarter |
| `GrossProfitPQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Previous Quarter |
| `GrossProfitPYQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Previous Quarter 1 Year Ago |
| `GrossProfitTTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Trailing 12 Months |
| `GrossProfitPTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Previous Trailing 12 Months |
| `GrossProfitA` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Latest Year |
| `GrossProfitPY` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Previous Year |
| `GrossProfitGr%PQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Q vs Previous Q Growth |
| `GrossProfitGr%PYQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Q vs 1 year ago Q Growth |
| `GrossProfitGr%TTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Trailing Twelve Months Growth |
| `GrossProfitGr%PQTTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Trailing Twelve Months Growth 1Q Ago |
| `GrossProfitGr%A` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Growth Annual |
| `GrossProfitGr%3Y` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Three Year Annualized Growth |
| `GrossProfitGr%5Y` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Five Year Annualized Growth |
| `GrossProfitGr%10Y` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Ten Year Annualized Growth |
| `GrossProfitRSD%ANN` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Ten Year Relative Standard Deviation |
| `GrossProfitRSD%TTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Five Year Relative Standard Deviation |
| `GrossProfitRegEstANN` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Ten Year Regression Estimate |
| `GrossProfitRegEstTTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Five Year Regression Estimate |
| `GrossProfitRegGr%ANN` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Ten Year Regression Estimate |
| `GrossProfitRegGr%TTM` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Five Year Regression Growth |
| `GrossProfitPSQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Quarterly Per Share |
| `GrossProfitPSA` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Annual Per Share |
| `GrossProfit%SalesQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | % of Quarterly Sales |
| `GrossProfit%SalesA` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | % of Annual Sales |
| `GrossProfit%AssetsQ` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | % of Quarterly Assets |
| `GrossProfit%AssetsA` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | % of Annual Assets |
| `GrossProfit3YAvg` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Three Year Average |
| `GrossProfit5YAvg` | Profit after deducting production/service costs. GrossProfit = Sales - CostG (excludes D&A). | Five Year Average |

#### `GrossProfit_GAAP(offset, type[, NAHandling])`
```p123
GrossProfit_GAAP(offset, type[, NAHandling])
```

Gross profit is the profit a company makes after deducting the costs associated with producing and selling its products or the costs associated with its services. In Portfolio123, we distinguish between two versions of gross profit calculations: GrossProfit and GrossProfit_GAAP. The latter incorporates depreciation and amortization into the cost of goods sold (COGS), reflecting a more comprehensive measure of production costs under Generally Accepted Accounting Principles (GAAP).

The choice between using GrossProfit and GrossProfit_GAAP depends on the analytical needs of users focusing on trading systems and investment strategies. GrossProfit provides a direct measure of profitability excluding depreciation and amortization, ideal for analyzing operational efficiency. GrossProfit_GAAP, by including these non-cash expenses, offers a more conservative view of profitability, aligning closer with GAAP standards and potentially providing a more realistic assessment of long-term investment sustainability.

Formulas:

Sales - CostG for GrossProfit
Sales - CostG_GAAP for GrossProfit_GAAP

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `GrossProfit_GAAPQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Latest Quarter |
| `GrossProfit_GAAPPQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Previous Quarter |
| `GrossProfit_GAAPPYQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Previous Quarter 1 Year Ago |
| `GrossProfit_GAAPTTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Trailing 12 Months |
| `GrossProfit_GAAPPTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Previous Trailing 12 Months |
| `GrossProfit_GAAPA` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Latest Year |
| `GrossProfit_GAAPPY` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Previous Year |
| `GrossProfit_GAAPGr%PQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Q vs Previous Q Growth |
| `GrossProfit_GAAPGr%PYQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Q vs 1 year ago Q Growth |
| `GrossProfit_GAAPGr%TTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Trailing Twelve Months Growth |
| `GrossProfit_GAAPGr%PQTTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Trailing Twelve Months Growth 1Q Ago |
| `GrossProfit_GAAPGr%A` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Growth Annual |
| `GrossProfit_GAAPGr%3Y` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Three Year Annualized Growth |
| `GrossProfit_GAAPGr%5Y` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Five Year Annualized Growth |
| `GrossProfit_GAAPGr%10Y` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Ten Year Annualized Growth |
| `GrossProfit_GAAPRSD%ANN` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Ten Year Relative Standard Deviation |
| `GrossProfit_GAAPRSD%TTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Five Year Relative Standard Deviation |
| `GrossProfit_GAAPRegEstANN` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Ten Year Regression Estimate |
| `GrossProfit_GAAPRegEstTTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Five Year Regression Estimate |
| `GrossProfit_GAAPRegGr%ANN` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Ten Year Regression Estimate |
| `GrossProfit_GAAPRegGr%TTM` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Five Year Regression Growth |
| `GrossProfit_GAAPPSQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Quarterly Per Share |
| `GrossProfit_GAAPPSA` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Annual Per Share |
| `GrossProfit_GAAP%SalesQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | % of Quarterly Sales |
| `GrossProfit_GAAP%SalesA` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | % of Annual Sales |
| `GrossProfit_GAAP%AssetsQ` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | % of Quarterly Assets |
| `GrossProfit_GAAP%AssetsA` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | % of Annual Assets |
| `GrossProfit_GAAP3YAvg` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Three Year Average |
| `GrossProfit_GAAP5YAvg` | Profit after deducting production/service costs. GrossProfit_GAAP = Sales - CostG_GAAP (includes D&A). | Five Year Average |

#### `Impair(offset, type[, NAHandling])`
```p123
Impair(offset, type[, NAHandling])
```

Represents the total charge against the carrying value of an asset to bring it to its fair value.

For Non-REIT companies, this represents the sum of the following: Goodwill, PP&E - Operating, Intangible assets, Fixed Financial Assets.

For REIT companies, this represents the sum of the following: Goodwill, PP&E - Operating, Properties, Intangible assets, Investments, Other

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `ImpairQ` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Latest Quarter |
| `ImpairPQ` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Previous Quarter |
| `ImpairPYQ` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Previous Quarter 1 Year Ago |
| `ImpairTTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Trailing 12 Months |
| `ImpairPTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Previous Trailing 12 Months |
| `ImpairA` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Latest Year |
| `ImpairPY` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Previous Year |
| `ImpairGr%PQ` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Q vs Previous Q Growth |
| `ImpairGr%PYQ` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Q vs 1 year ago Q Growth |
| `ImpairGr%TTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Trailing Twelve Months Growth |
| `ImpairGr%PQTTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Trailing Twelve Months Growth 1Q Ago |
| `ImpairGr%A` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Growth Annual |
| `ImpairGr%3Y` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Three Year Annualized Growth |
| `ImpairGr%5Y` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Five Year Annualized Growth |
| `ImpairGr%10Y` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Ten Year Annualized Growth |
| `ImpairRSD%ANN` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Ten Year Relative Standard Deviation |
| `ImpairRSD%TTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Five Year Relative Standard Deviation |
| `ImpairRegEstANN` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Ten Year Regression Estimate |
| `ImpairRegEstTTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Five Year Regression Estimate |
| `ImpairRegGr%ANN` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Ten Year Regression Estimate |
| `ImpairRegGr%TTM` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Five Year Regression Growth |
| `Impair3YAvg` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Three Year Average |
| `Impair5YAvg` | Represents the total charge against the carrying value of an asset to bring it to its fair value. | Five Year Average |

#### `IncAftTax(offset, type[, NAHandling])`
```p123
IncAftTax(offset, type[, NAHandling])
```

Income After Tax equals pre-tax income excluding extraordinary items less tax expense.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IncAftTaxQ` | Pre-tax income excluding extraordinary items less tax expense. | Latest Quarter |
| `IncAftTaxPQ` | Pre-tax income excluding extraordinary items less tax expense. | Previous Quarter |
| `IncAftTaxPYQ` | Pre-tax income excluding extraordinary items less tax expense. | Previous Quarter 1 Year Ago |
| `IncAftTaxTTM` | Pre-tax income excluding extraordinary items less tax expense. | Trailing 12 Months |
| `IncAftTaxPTM` | Pre-tax income excluding extraordinary items less tax expense. | Previous Trailing 12 Months |
| `IncAftTaxA` | Pre-tax income excluding extraordinary items less tax expense. | Latest Year |
| `IncAftTaxPY` | Pre-tax income excluding extraordinary items less tax expense. | Previous Year |
| `IncAftTaxGr%PQ` | Pre-tax income excluding extraordinary items less tax expense. | Q vs Previous Q Growth |
| `IncAftTaxGr%PYQ` | Pre-tax income excluding extraordinary items less tax expense. | Q vs 1 year ago Q Growth |
| `IncAftTaxGr%TTM` | Pre-tax income excluding extraordinary items less tax expense. | Trailing Twelve Months Growth |
| `IncAftTaxGr%PQTTM` | Pre-tax income excluding extraordinary items less tax expense. | Trailing Twelve Months Growth 1Q Ago |
| `IncAftTaxGr%A` | Pre-tax income excluding extraordinary items less tax expense. | Growth Annual |
| `IncAftTaxGr%3Y` | Pre-tax income excluding extraordinary items less tax expense. | Three Year Annualized Growth |
| `IncAftTaxGr%5Y` | Pre-tax income excluding extraordinary items less tax expense. | Five Year Annualized Growth |
| `IncAftTaxGr%10Y` | Pre-tax income excluding extraordinary items less tax expense. | Ten Year Annualized Growth |
| `IncAftTaxRSD%ANN` | Pre-tax income excluding extraordinary items less tax expense. | Ten Year Relative Standard Deviation |
| `IncAftTaxRSD%TTM` | Pre-tax income excluding extraordinary items less tax expense. | Five Year Relative Standard Deviation |
| `IncAftTaxRegEstANN` | Pre-tax income excluding extraordinary items less tax expense. | Ten Year Regression Estimate |
| `IncAftTaxRegEstTTM` | Pre-tax income excluding extraordinary items less tax expense. | Five Year Regression Estimate |
| `IncAftTaxRegGr%ANN` | Pre-tax income excluding extraordinary items less tax expense. | Ten Year Regression Estimate |
| `IncAftTaxRegGr%TTM` | Pre-tax income excluding extraordinary items less tax expense. | Five Year Regression Growth |
| `IncAftTaxPSQ` | Pre-tax income excluding extraordinary items less tax expense. | Quarterly Per Share |
| `IncAftTaxPSA` | Pre-tax income excluding extraordinary items less tax expense. | Annual Per Share |
| `IncAftTax%SalesQ` | Pre-tax income excluding extraordinary items less tax expense. | % of Quarterly Sales |
| `IncAftTax%SalesA` | Pre-tax income excluding extraordinary items less tax expense. | % of Annual Sales |
| `IncAftTax3YAvg` | Pre-tax income excluding extraordinary items less tax expense. | Three Year Average |
| `IncAftTax5YAvg` | Pre-tax income excluding extraordinary items less tax expense. | Five Year Average |

#### `IAC(offset, type[, NAHandling])`
```p123
IAC(offset, type[, NAHandling])
```

Income Available to Common is equal to income before extraordinary items and discontinued operations less preferred dividends.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IACQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Latest Quarter |
| `IACPQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Previous Quarter |
| `IACPYQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Previous Quarter 1 Year Ago |
| `IACTTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Trailing 12 Months |
| `IACPTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Previous Trailing 12 Months |
| `IACA` | Income before extraordinary items and discontinued operations less preferred dividends. | Latest Year |
| `IACPY` | Income before extraordinary items and discontinued operations less preferred dividends. | Previous Year |
| `IACGr%PQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Q vs Previous Q Growth |
| `IACGr%PYQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Q vs 1 year ago Q Growth |
| `IACGr%TTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Trailing Twelve Months Growth |
| `IACGr%PQTTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Trailing Twelve Months Growth 1Q Ago |
| `IACGr%A` | Income before extraordinary items and discontinued operations less preferred dividends. | Growth Annual |
| `IACGr%3Y` | Income before extraordinary items and discontinued operations less preferred dividends. | Three Year Annualized Growth |
| `IACGr%5Y` | Income before extraordinary items and discontinued operations less preferred dividends. | Five Year Annualized Growth |
| `IACGr%10Y` | Income before extraordinary items and discontinued operations less preferred dividends. | Ten Year Annualized Growth |
| `IACRSD%ANN` | Income before extraordinary items and discontinued operations less preferred dividends. | Ten Year Relative Standard Deviation |
| `IACRSD%TTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Five Year Relative Standard Deviation |
| `IACRegEstANN` | Income before extraordinary items and discontinued operations less preferred dividends. | Ten Year Regression Estimate |
| `IACRegEstTTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Five Year Regression Estimate |
| `IACRegGr%ANN` | Income before extraordinary items and discontinued operations less preferred dividends. | Ten Year Regression Estimate |
| `IACRegGr%TTM` | Income before extraordinary items and discontinued operations less preferred dividends. | Five Year Regression Growth |
| `IACPSQ` | Income before extraordinary items and discontinued operations less preferred dividends. | Quarterly Per Share |
| `IACPSA` | Income before extraordinary items and discontinued operations less preferred dividends. | Annual Per Share |
| `IAC%SalesQ` | Income before extraordinary items and discontinued operations less preferred dividends. | % of Quarterly Sales |
| `IAC%SalesA` | Income before extraordinary items and discontinued operations less preferred dividends. | % of Annual Sales |
| `IAC3YAvg` | Income before extraordinary items and discontinued operations less preferred dividends. | Three Year Average |
| `IAC5YAvg` | Income before extraordinary items and discontinued operations less preferred dividends. | Five Year Average |

#### `IncBTax(offset, type[, NAHandling])`
```p123
IncBTax(offset, type[, NAHandling])
```

Income Before Taxes includes all expenses except extraordinary and discontinued items, and is also calculated before the effects of non-consolidated subsidiaries.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IncBTaxQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Latest Quarter |
| `IncBTaxPQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Previous Quarter |
| `IncBTaxPYQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Previous Quarter 1 Year Ago |
| `IncBTaxTTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Trailing 12 Months |
| `IncBTaxPTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Previous Trailing 12 Months |
| `IncBTaxA` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Latest Year |
| `IncBTaxPY` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Previous Year |
| `IncBTaxGr%PQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Q vs Previous Q Growth |
| `IncBTaxGr%PYQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Q vs 1 year ago Q Growth |
| `IncBTaxGr%TTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Trailing Twelve Months Growth |
| `IncBTaxGr%PQTTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Trailing Twelve Months Growth 1Q Ago |
| `IncBTaxGr%A` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Growth Annual |
| `IncBTaxGr%3Y` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Three Year Annualized Growth |
| `IncBTaxGr%5Y` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Five Year Annualized Growth |
| `IncBTaxGr%10Y` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Ten Year Annualized Growth |
| `IncBTaxRSD%ANN` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Ten Year Relative Standard Deviation |
| `IncBTaxRSD%TTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Five Year Relative Standard Deviation |
| `IncBTaxRegEstANN` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Ten Year Regression Estimate |
| `IncBTaxRegEstTTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Five Year Regression Estimate |
| `IncBTaxRegGr%ANN` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Ten Year Regression Estimate |
| `IncBTaxRegGr%TTM` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Five Year Regression Growth |
| `IncBTaxPSQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Quarterly Per Share |
| `IncBTaxPSA` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Annual Per Share |
| `IncBTax%SalesQ` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | % of Quarterly Sales |
| `IncBTax%SalesA` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | % of Annual Sales |
| `IncBTax3YAvg` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Three Year Average |
| `IncBTax5YAvg` | Income Before Taxes includes all expenses except extraordinary and discontinued items. | Five Year Average |

#### `IncBXorAdjCSE(offset, type[, NAHandling])`
```p123
IncBXorAdjCSE(offset, type[, NAHandling])
```

Income Before Extraordinary Items Adjusted for Common Share Equivalents is net income available to common divided by fully diluted shares.

Income available to common is net income after all mandatory payments have been made. These payments include debt service and preferred dividend. Note, however, that interest or dividend cost savings from the theoretical conversion of debt or preferred shares to equity is also reflected as part of the dilution of shares.

Net income in this case is before extraordinary and discontinued items.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IncBXorAdjCSEQ` | Net income available to common divided by fully diluted shares. | Latest Quarter |
| `IncBXorAdjCSEPQ` | Net income available to common divided by fully diluted shares. | Previous Quarter |
| `IncBXorAdjCSEPYQ` | Net income available to common divided by fully diluted shares. | Previous Quarter 1 Year Ago |
| `IncBXorAdjCSETTM` | Net income available to common divided by fully diluted shares. | Trailing 12 Months |
| `IncBXorAdjCSEPTM` | Net income available to common divided by fully diluted shares. | Previous Trailing 12 Months |
| `IncBXorAdjCSEA` | Net income available to common divided by fully diluted shares. | Latest Year |
| `IncBXorAdjCSEPY` | Net income available to common divided by fully diluted shares. | Previous Year |
| `IncBXorAdjCSEGr%PQ` | Net income available to common divided by fully diluted shares. | Q vs Previous Q Growth |
| `IncBXorAdjCSEGr%PYQ` | Net income available to common divided by fully diluted shares. | Q vs 1 year ago Q Growth |
| `IncBXorAdjCSEGr%TTM` | Net income available to common divided by fully diluted shares. | Trailing Twelve Months Growth |
| `IncBXorAdjCSEGr%PQTTM` | Net income available to common divided by fully diluted shares. | Trailing Twelve Months Growth 1Q Ago |
| `IncBXorAdjCSEGr%A` | Net income available to common divided by fully diluted shares. | Growth Annual |
| `IncBXorAdjCSEGr%3Y` | Net income available to common divided by fully diluted shares. | Three Year Annualized Growth |
| `IncBXorAdjCSEGr%5Y` | Net income available to common divided by fully diluted shares. | Five Year Annualized Growth |
| `IncBXorAdjCSEGr%10Y` | Net income available to common divided by fully diluted shares. | Ten Year Annualized Growth |
| `IncBXorAdjCSERSD%ANN` | Net income available to common divided by fully diluted shares. | Ten Year Relative Standard Deviation |
| `IncBXorAdjCSERSD%TTM` | Net income available to common divided by fully diluted shares. | Five Year Relative Standard Deviation |
| `IncBXorAdjCSERegEstANN` | Net income available to common divided by fully diluted shares. | Ten Year Regression Estimate |
| `IncBXorAdjCSERegEstTTM` | Net income available to common divided by fully diluted shares. | Five Year Regression Estimate |
| `IncBXorAdjCSERegGr%ANN` | Net income available to common divided by fully diluted shares. | Ten Year Regression Estimate |
| `IncBXorAdjCSERegGr%TTM` | Net income available to common divided by fully diluted shares. | Five Year Regression Growth |
| `IncBXorAdjCSEPSQ` | Net income available to common divided by fully diluted shares. | Quarterly Per Share |
| `IncBXorAdjCSEPSA` | Net income available to common divided by fully diluted shares. | Annual Per Share |
| `IncBXorAdjCSE%SalesQ` | Net income available to common divided by fully diluted shares. | % of Quarterly Sales |
| `IncBXorAdjCSE%SalesA` | Net income available to common divided by fully diluted shares. | % of Annual Sales |
| `IncBXorAdjCSE3YAvg` | Net income available to common divided by fully diluted shares. | Three Year Average |
| `IncBXorAdjCSE5YAvg` | Net income available to common divided by fully diluted shares. | Five Year Average |

#### `IncBXorForCom(offset, type[, NAHandling])`
```p123
IncBXorForCom(offset, type[, NAHandling])
```

Income Before Extraordinary Avaliable For Common is income before extraordinary items and discontinued operations less preferred dividends, but before adding savings due to common stock equivalents.

The net income in this case is before extraordinary or discontinued items, but after mandatory payments like interest expense and preferred dividends. Unlike Income Before Extraordinaries Adjusted for Common Share Equivalents, this item does not reflect cost savings from unpaid interest expenses and preferred dividends that would occur with dilution.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IncBXorForComQ` | Income before extraordinary/discontinued items minus preferred dividends. | Latest Quarter |
| `IncBXorForComPQ` | Income before extraordinary/discontinued items minus preferred dividends. | Previous Quarter |
| `IncBXorForComPYQ` | Income before extraordinary/discontinued items minus preferred dividends. | Previous Quarter 1 Year Ago |
| `IncBXorForComTTM` | Income before extraordinary/discontinued items minus preferred dividends. | Trailing 12 Months |
| `IncBXorForComPTM` | Income before extraordinary/discontinued items minus preferred dividends. | Previous Trailing 12 Months |
| `IncBXorForComA` | Income before extraordinary/discontinued items minus preferred dividends. | Latest Year |
| `IncBXorForComPY` | Income before extraordinary/discontinued items minus preferred dividends. | Previous Year |
| `IncBXorForComGr%PQ` | Income before extraordinary/discontinued items minus preferred dividends. | Q vs Previous Q Growth |
| `IncBXorForComGr%PYQ` | Income before extraordinary/discontinued items minus preferred dividends. | Q vs 1 year ago Q Growth |
| `IncBXorForComGr%TTM` | Income before extraordinary/discontinued items minus preferred dividends. | Trailing Twelve Months Growth |
| `IncBXorForComGr%PQTTM` | Income before extraordinary/discontinued items minus preferred dividends. | Trailing Twelve Months Growth 1Q Ago |
| `IncBXorForComGr%A` | Income before extraordinary/discontinued items minus preferred dividends. | Growth Annual |
| `IncBXorForComGr%3Y` | Income before extraordinary/discontinued items minus preferred dividends. | Three Year Annualized Growth |
| `IncBXorForComGr%5Y` | Income before extraordinary/discontinued items minus preferred dividends. | Five Year Annualized Growth |
| `IncBXorForComGr%10Y` | Income before extraordinary/discontinued items minus preferred dividends. | Ten Year Annualized Growth |
| `IncBXorForComRSD%ANN` | Income before extraordinary/discontinued items minus preferred dividends. | Ten Year Relative Standard Deviation |
| `IncBXorForComRSD%TTM` | Income before extraordinary/discontinued items minus preferred dividends. | Five Year Relative Standard Deviation |
| `IncBXorForComRegEstANN` | Income before extraordinary/discontinued items minus preferred dividends. | Ten Year Regression Estimate |
| `IncBXorForComRegEstTTM` | Income before extraordinary/discontinued items minus preferred dividends. | Five Year Regression Estimate |
| `IncBXorForComRegGr%ANN` | Income before extraordinary/discontinued items minus preferred dividends. | Ten Year Regression Estimate |
| `IncBXorForComRegGr%TTM` | Income before extraordinary/discontinued items minus preferred dividends. | Five Year Regression Growth |
| `IncBXorForComPSQ` | Income before extraordinary/discontinued items minus preferred dividends. | Quarterly Per Share |
| `IncBXorForComPSA` | Income before extraordinary/discontinued items minus preferred dividends. | Annual Per Share |
| `IncBXorForCom%SalesQ` | Income before extraordinary/discontinued items minus preferred dividends. | % of Quarterly Sales |
| `IncBXorForCom%SalesA` | Income before extraordinary/discontinued items minus preferred dividends. | % of Annual Sales |
| `IncBXorForCom3YAvg` | Income before extraordinary/discontinued items minus preferred dividends. | Three Year Average |
| `IncBXorForCom5YAvg` | Income before extraordinary/discontinued items minus preferred dividends. | Five Year Average |

#### `IncTaxExp(offset, type[, NAHandling])`
```p123
IncTaxExp(offset, type[, NAHandling])
```

Income Tax Expense is the amount paid by the company during the period specified by the type and offset inputs.

Note that this is historical and is net. Tax credits or net-operating income are reflected in this and may have reduced the expense paid. A tax rate sharply below that of competitors should be regarded as unsubstainable.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IncTaxExpQ` | Net amount paid by the company during the period. | Latest Quarter |
| `IncTaxExpPQ` | Net amount paid by the company during the period. | Previous Quarter |
| `IncTaxExpPYQ` | Net amount paid by the company during the period. | Previous Quarter 1 Year Ago |
| `IncTaxExpTTM` | Net amount paid by the company during the period. | Trailing 12 Months |
| `IncTaxExpPTM` | Net amount paid by the company during the period. | Previous Trailing 12 Months |
| `IncTaxExpA` | Net amount paid by the company during the period. | Latest Year |
| `IncTaxExpPY` | Net amount paid by the company during the period. | Previous Year |
| `IncTaxExpGr%PQ` | Net amount paid by the company during the period. | Q vs Previous Q Growth |
| `IncTaxExpGr%PYQ` | Net amount paid by the company during the period. | Q vs 1 year ago Q Growth |
| `IncTaxExpGr%TTM` | Net amount paid by the company during the period. | Trailing Twelve Months Growth |
| `IncTaxExpGr%PQTTM` | Net amount paid by the company during the period. | Trailing Twelve Months Growth 1Q Ago |
| `IncTaxExpGr%A` | Net amount paid by the company during the period. | Growth Annual |
| `IncTaxExpGr%3Y` | Net amount paid by the company during the period. | Three Year Annualized Growth |
| `IncTaxExpGr%5Y` | Net amount paid by the company during the period. | Five Year Annualized Growth |
| `IncTaxExpGr%10Y` | Net amount paid by the company during the period. | Ten Year Annualized Growth |
| `IncTaxExpRSD%ANN` | Net amount paid by the company during the period. | Ten Year Relative Standard Deviation |
| `IncTaxExpRSD%TTM` | Net amount paid by the company during the period. | Five Year Relative Standard Deviation |
| `IncTaxExpRegEstANN` | Net amount paid by the company during the period. | Ten Year Regression Estimate |
| `IncTaxExpRegEstTTM` | Net amount paid by the company during the period. | Five Year Regression Estimate |
| `IncTaxExpRegGr%ANN` | Net amount paid by the company during the period. | Ten Year Regression Estimate |
| `IncTaxExpRegGr%TTM` | Net amount paid by the company during the period. | Five Year Regression Growth |
| `IncTaxExpPSQ` | Net amount paid by the company during the period. | Quarterly Per Share |
| `IncTaxExpPSA` | Net amount paid by the company during the period. | Annual Per Share |
| `IncTaxExp%SalesQ` | Net amount paid by the company during the period. | % of Quarterly Sales |
| `IncTaxExp%SalesA` | Net amount paid by the company during the period. | % of Annual Sales |
| `IncTaxExp3YAvg` | Net amount paid by the company during the period. | Three Year Average |
| `IncTaxExp5YAvg` | Net amount paid by the company during the period. | Five Year Average |

#### `IntExp(offset, type[, NAHandling])`
```p123
IntExp(offset, type[, NAHandling])
```

Interest Expense is the amount that the company paid to service its debt during the period selected by the type input.

This figure includes all debt service, including current, long-term and issuance costs.

Where a company reports a single, net figure for interest-related items, that figure is reported in this line. As a result, despite the name, this line could be negative, reflecting net interest income.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IntExpQ` | Amount paid to service all debt during the period. | Latest Quarter |
| `IntExpPQ` | Amount paid to service all debt during the period. | Previous Quarter |
| `IntExpPYQ` | Amount paid to service all debt during the period. | Previous Quarter 1 Year Ago |
| `IntExpTTM` | Amount paid to service all debt during the period. | Trailing 12 Months |
| `IntExpPTM` | Amount paid to service all debt during the period. | Previous Trailing 12 Months |
| `IntExpA` | Amount paid to service all debt during the period. | Latest Year |
| `IntExpPY` | Amount paid to service all debt during the period. | Previous Year |
| `IntExpGr%PQ` | Amount paid to service all debt during the period. | Q vs Previous Q Growth |
| `IntExpGr%PYQ` | Amount paid to service all debt during the period. | Q vs 1 year ago Q Growth |
| `IntExpGr%TTM` | Amount paid to service all debt during the period. | Trailing Twelve Months Growth |
| `IntExpGr%PQTTM` | Amount paid to service all debt during the period. | Trailing Twelve Months Growth 1Q Ago |
| `IntExpGr%A` | Amount paid to service all debt during the period. | Growth Annual |
| `IntExpGr%3Y` | Amount paid to service all debt during the period. | Three Year Annualized Growth |
| `IntExpGr%5Y` | Amount paid to service all debt during the period. | Five Year Annualized Growth |
| `IntExpGr%10Y` | Amount paid to service all debt during the period. | Ten Year Annualized Growth |
| `IntExpRSD%ANN` | Amount paid to service all debt during the period. | Ten Year Relative Standard Deviation |
| `IntExpRSD%TTM` | Amount paid to service all debt during the period. | Five Year Relative Standard Deviation |
| `IntExpRegEstANN` | Amount paid to service all debt during the period. | Ten Year Regression Estimate |
| `IntExpRegEstTTM` | Amount paid to service all debt during the period. | Five Year Regression Estimate |
| `IntExpRegGr%ANN` | Amount paid to service all debt during the period. | Ten Year Regression Estimate |
| `IntExpRegGr%TTM` | Amount paid to service all debt during the period. | Five Year Regression Growth |
| `IntExpPSQ` | Amount paid to service all debt during the period. | Quarterly Per Share |
| `IntExpPSA` | Amount paid to service all debt during the period. | Annual Per Share |
| `IntExp%SalesQ` | Amount paid to service all debt during the period. | % of Quarterly Sales |
| `IntExp%SalesA` | Amount paid to service all debt during the period. | % of Annual Sales |
| `IntExp3YAvg` | Amount paid to service all debt during the period. | Three Year Average |
| `IntExp5YAvg` | Amount paid to service all debt during the period. | Five Year Average |

#### `IntInc(offset, type[, NAHandling])`
```p123
IntInc(offset, type[, NAHandling])
```

Interest Income is the amount that the company made through loans in the period selected by the type input.

This line includes all interest income, both from current and long-term loans. Where a company reports interest items as a single net figure, it is reported as Interest Expense. Expect this line to be null in those cases.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IntIncQ` | Amount earned from loans during the period. | Latest Quarter |
| `IntIncPQ` | Amount earned from loans during the period. | Previous Quarter |
| `IntIncPYQ` | Amount earned from loans during the period. | Previous Quarter 1 Year Ago |
| `IntIncTTM` | Amount earned from loans during the period. | Trailing 12 Months |
| `IntIncPTM` | Amount earned from loans during the period. | Previous Trailing 12 Months |
| `IntIncA` | Amount earned from loans during the period. | Latest Year |
| `IntIncPY` | Amount earned from loans during the period. | Previous Year |
| `IntIncGr%PQ` | Amount earned from loans during the period. | Q vs Previous Q Growth |
| `IntIncGr%PYQ` | Amount earned from loans during the period. | Q vs 1 year ago Q Growth |
| `IntIncGr%TTM` | Amount earned from loans during the period. | Trailing Twelve Months Growth |
| `IntIncGr%PQTTM` | Amount earned from loans during the period. | Trailing Twelve Months Growth 1Q Ago |
| `IntIncGr%A` | Amount earned from loans during the period. | Growth Annual |
| `IntIncGr%3Y` | Amount earned from loans during the period. | Three Year Annualized Growth |
| `IntIncGr%5Y` | Amount earned from loans during the period. | Five Year Annualized Growth |
| `IntIncGr%10Y` | Amount earned from loans during the period. | Ten Year Annualized Growth |
| `IntIncRSD%ANN` | Amount earned from loans during the period. | Ten Year Relative Standard Deviation |
| `IntIncRSD%TTM` | Amount earned from loans during the period. | Five Year Relative Standard Deviation |
| `IntIncRegEstANN` | Amount earned from loans during the period. | Ten Year Regression Estimate |
| `IntIncRegEstTTM` | Amount earned from loans during the period. | Five Year Regression Estimate |
| `IntIncRegGr%ANN` | Amount earned from loans during the period. | Ten Year Regression Estimate |
| `IntIncRegGr%TTM` | Amount earned from loans during the period. | Five Year Regression Growth |
| `IntIncPSQ` | Amount earned from loans during the period. | Quarterly Per Share |
| `IntIncPSA` | Amount earned from loans during the period. | Annual Per Share |
| `IntInc%SalesQ` | Amount earned from loans during the period. | % of Quarterly Sales |
| `IntInc%SalesA` | Amount earned from loans during the period. | % of Annual Sales |
| `IntInc3YAvg` | Amount earned from loans during the period. | Three Year Average |
| `IntInc5YAvg` | Amount earned from loans during the period. | Five Year Average |

#### `NetIncBXor(offset, type[, NAHandling])`
```p123
NetIncBXor(offset, type[, NAHandling])
```

Net Income Before Extraordinary Items is the income of a company after all expenses for a period determined by the type input. It does not include provisions for common dividends, extraordinary items or discontinued operations, but otherwise reflects all expenses, including taxes and minority interest.

FactSet deducts preferred dividends paid.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetIncBXorQ` | Income after all expenses including taxes and minority interest. | Latest Quarter |
| `NetIncBXorPQ` | Income after all expenses including taxes and minority interest. | Previous Quarter |
| `NetIncBXorPYQ` | Income after all expenses including taxes and minority interest. | Previous Quarter 1 Year Ago |
| `NetIncBXorTTM` | Income after all expenses including taxes and minority interest. | Trailing 12 Months |
| `NetIncBXorPTM` | Income after all expenses including taxes and minority interest. | Previous Trailing 12 Months |
| `NetIncBXorA` | Income after all expenses including taxes and minority interest. | Latest Year |
| `NetIncBXorPY` | Income after all expenses including taxes and minority interest. | Previous Year |
| `NetIncBXorGr%PQ` | Income after all expenses including taxes and minority interest. | Q vs Previous Q Growth |
| `NetIncBXorGr%PYQ` | Income after all expenses including taxes and minority interest. | Q vs 1 year ago Q Growth |
| `NetIncBXorGr%TTM` | Income after all expenses including taxes and minority interest. | Trailing Twelve Months Growth |
| `NetIncBXorGr%PQTTM` | Income after all expenses including taxes and minority interest. | Trailing Twelve Months Growth 1Q Ago |
| `NetIncBXorGr%A` | Income after all expenses including taxes and minority interest. | Growth Annual |
| `NetIncBXorGr%3Y` | Income after all expenses including taxes and minority interest. | Three Year Annualized Growth |
| `NetIncBXorGr%5Y` | Income after all expenses including taxes and minority interest. | Five Year Annualized Growth |
| `NetIncBXorGr%10Y` | Income after all expenses including taxes and minority interest. | Ten Year Annualized Growth |
| `NetIncBXorRSD%ANN` | Income after all expenses including taxes and minority interest. | Ten Year Relative Standard Deviation |
| `NetIncBXorRSD%TTM` | Income after all expenses including taxes and minority interest. | Five Year Relative Standard Deviation |
| `NetIncBXorRegEstANN` | Income after all expenses including taxes and minority interest. | Ten Year Regression Estimate |
| `NetIncBXorRegEstTTM` | Income after all expenses including taxes and minority interest. | Five Year Regression Estimate |
| `NetIncBXorRegGr%ANN` | Income after all expenses including taxes and minority interest. | Ten Year Regression Estimate |
| `NetIncBXorRegGr%TTM` | Income after all expenses including taxes and minority interest. | Five Year Regression Growth |
| `NetIncBXorPSQ` | Income after all expenses including taxes and minority interest. | Quarterly Per Share |
| `NetIncBXorPSA` | Income after all expenses including taxes and minority interest. | Annual Per Share |
| `NetIncBXor%SalesQ` | Income after all expenses including taxes and minority interest. | % of Quarterly Sales |
| `NetIncBXor%SalesA` | Income after all expenses including taxes and minority interest. | % of Annual Sales |
| `NetIncBXor3YAvg` | Income after all expenses including taxes and minority interest. | Three Year Average |
| `NetIncBXor5YAvg` | Income after all expenses including taxes and minority interest. | Five Year Average |

#### `NetIncBXorNonC(offset, type[, NAHandling])`
```p123
NetIncBXorNonC(offset, type[, NAHandling])
```

Net Income Before Extraordinary Items and Non-Controlling Interest is the total amount that the company earned in the period specified by the type input, excluding extraordinary items and minority interest. It otherwise includes all pre- and post-tax outflows, including tax itself.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetIncBXorNonCQ` | Total earnings excluding extraordinary items and minority interest. | Latest Quarter |
| `NetIncBXorNonCPQ` | Total earnings excluding extraordinary items and minority interest. | Previous Quarter |
| `NetIncBXorNonCPYQ` | Total earnings excluding extraordinary items and minority interest. | Previous Quarter 1 Year Ago |
| `NetIncBXorNonCTTM` | Total earnings excluding extraordinary items and minority interest. | Trailing 12 Months |
| `NetIncBXorNonCPTM` | Total earnings excluding extraordinary items and minority interest. | Previous Trailing 12 Months |
| `NetIncBXorNonCA` | Total earnings excluding extraordinary items and minority interest. | Latest Year |
| `NetIncBXorNonCPY` | Total earnings excluding extraordinary items and minority interest. | Previous Year |
| `NetIncBXorNonCGr%PQ` | Total earnings excluding extraordinary items and minority interest. | Q vs Previous Q Growth |
| `NetIncBXorNonCGr%PYQ` | Total earnings excluding extraordinary items and minority interest. | Q vs 1 year ago Q Growth |
| `NetIncBXorNonCGr%TTM` | Total earnings excluding extraordinary items and minority interest. | Trailing Twelve Months Growth |
| `NetIncBXorNonCGr%PQTTM` | Total earnings excluding extraordinary items and minority interest. | Trailing Twelve Months Growth 1Q Ago |
| `NetIncBXorNonCGr%A` | Total earnings excluding extraordinary items and minority interest. | Growth Annual |
| `NetIncBXorNonCGr%3Y` | Total earnings excluding extraordinary items and minority interest. | Three Year Annualized Growth |
| `NetIncBXorNonCGr%5Y` | Total earnings excluding extraordinary items and minority interest. | Five Year Annualized Growth |
| `NetIncBXorNonCGr%10Y` | Total earnings excluding extraordinary items and minority interest. | Ten Year Annualized Growth |
| `NetIncBXorNonCRSD%ANN` | Total earnings excluding extraordinary items and minority interest. | Ten Year Relative Standard Deviation |
| `NetIncBXorNonCRSD%TTM` | Total earnings excluding extraordinary items and minority interest. | Five Year Relative Standard Deviation |
| `NetIncBXorNonCRegEstANN` | Total earnings excluding extraordinary items and minority interest. | Ten Year Regression Estimate |
| `NetIncBXorNonCRegEstTTM` | Total earnings excluding extraordinary items and minority interest. | Five Year Regression Estimate |
| `NetIncBXorNonCRegGr%ANN` | Total earnings excluding extraordinary items and minority interest. | Ten Year Regression Estimate |
| `NetIncBXorNonCRegGr%TTM` | Total earnings excluding extraordinary items and minority interest. | Five Year Regression Growth |
| `NetIncBXorNonCPSQ` | Total earnings excluding extraordinary items and minority interest. | Quarterly Per Share |
| `NetIncBXorNonCPSA` | Total earnings excluding extraordinary items and minority interest. | Annual Per Share |
| `NetIncBXorNonC%SalesQ` | Total earnings excluding extraordinary items and minority interest. | % of Quarterly Sales |
| `NetIncBXorNonC%SalesA` | Total earnings excluding extraordinary items and minority interest. | % of Annual Sales |
| `NetIncBXorNonC3YAvg` | Total earnings excluding extraordinary items and minority interest. | Three Year Average |
| `NetIncBXorNonC5YAvg` | Total earnings excluding extraordinary items and minority interest. | Five Year Average |

#### `ExpNonOp(offset, type[, NAHandling])`
```p123
ExpNonOp(offset, type[, NAHandling])
```

Non-Operating Expenses are expenses that are a result of secondary activities of companies. (Primary activities are those that are related to core businesses.)

This is, necesarilly, a broad line. Note that it could include both secondary businesses and financing and investing activities. Examples of items that are included are rental income, interest income (or loss), earnings (or losses) from nonconsolidated subsidiaries, and foreign exchange gains or losses.

This line is netted out; it could potentially be non-operating income. If the line is positive, it is income. A negative result is an expense.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `ExpNonOpQ` | Net result from secondary activities unrelated to core business. | Latest Quarter |
| `ExpNonOpPQ` | Net result from secondary activities unrelated to core business. | Previous Quarter |
| `ExpNonOpPYQ` | Net result from secondary activities unrelated to core business. | Previous Quarter 1 Year Ago |
| `ExpNonOpTTM` | Net result from secondary activities unrelated to core business. | Trailing 12 Months |
| `ExpNonOpPTM` | Net result from secondary activities unrelated to core business. | Previous Trailing 12 Months |
| `ExpNonOpA` | Net result from secondary activities unrelated to core business. | Latest Year |
| `ExpNonOpPY` | Net result from secondary activities unrelated to core business. | Previous Year |
| `ExpNonOpGr%PQ` | Net result from secondary activities unrelated to core business. | Q vs Previous Q Growth |
| `ExpNonOpGr%PYQ` | Net result from secondary activities unrelated to core business. | Q vs 1 year ago Q Growth |
| `ExpNonOpGr%TTM` | Net result from secondary activities unrelated to core business. | Trailing Twelve Months Growth |
| `ExpNonOpGr%PQTTM` | Net result from secondary activities unrelated to core business. | Trailing Twelve Months Growth 1Q Ago |
| `ExpNonOpGr%A` | Net result from secondary activities unrelated to core business. | Growth Annual |
| `ExpNonOpGr%3Y` | Net result from secondary activities unrelated to core business. | Three Year Annualized Growth |
| `ExpNonOpGr%5Y` | Net result from secondary activities unrelated to core business. | Five Year Annualized Growth |
| `ExpNonOpGr%10Y` | Net result from secondary activities unrelated to core business. | Ten Year Annualized Growth |
| `ExpNonOpRSD%ANN` | Net result from secondary activities unrelated to core business. | Ten Year Relative Standard Deviation |
| `ExpNonOpRSD%TTM` | Net result from secondary activities unrelated to core business. | Five Year Relative Standard Deviation |
| `ExpNonOpRegEstANN` | Net result from secondary activities unrelated to core business. | Ten Year Regression Estimate |
| `ExpNonOpRegEstTTM` | Net result from secondary activities unrelated to core business. | Five Year Regression Estimate |
| `ExpNonOpRegGr%ANN` | Net result from secondary activities unrelated to core business. | Ten Year Regression Estimate |
| `ExpNonOpRegGr%TTM` | Net result from secondary activities unrelated to core business. | Five Year Regression Growth |
| `ExpNonOpPSQ` | Net result from secondary activities unrelated to core business. | Quarterly Per Share |
| `ExpNonOpPSA` | Net result from secondary activities unrelated to core business. | Annual Per Share |
| `ExpNonOp%SalesQ` | Net result from secondary activities unrelated to core business. | % of Quarterly Sales |
| `ExpNonOp%SalesA` | Net result from secondary activities unrelated to core business. | % of Annual Sales |
| `ExpNonOp3YAvg` | Net result from secondary activities unrelated to core business. | Three Year Average |
| `ExpNonOp5YAvg` | Net result from secondary activities unrelated to core business. | Five Year Average |

#### `OpInc(offset, type[, NAHandling])`
```p123
OpInc(offset, type[, NAHandling])
```

Operating Income is equal to revenues less cost of goods sold; selling, general and administrative costs; and depreciation and amortization.

We recommend that users consider using this in lieu of EBIT or EBITDA. The lines that the data provider uses to calculate operating income are standard, safely comparable across industries and sectors and are all related to operations.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `OpIncQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Latest Quarter |
| `OpIncPQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Previous Quarter |
| `OpIncPYQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Previous Quarter 1 Year Ago |
| `OpIncTTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Trailing 12 Months |
| `OpIncPTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Previous Trailing 12 Months |
| `OpIncA` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Latest Year |
| `OpIncPY` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Previous Year |
| `OpIncGr%PQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Q vs Previous Q Growth |
| `OpIncGr%PYQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Q vs 1 year ago Q Growth |
| `OpIncGr%TTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Trailing Twelve Months Growth |
| `OpIncGr%PQTTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Trailing Twelve Months Growth 1Q Ago |
| `OpIncGr%A` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Growth Annual |
| `OpIncGr%3Y` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Three Year Annualized Growth |
| `OpIncGr%5Y` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Five Year Annualized Growth |
| `OpIncGr%10Y` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Ten Year Annualized Growth |
| `OpIncRSD%ANN` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Ten Year Relative Standard Deviation |
| `OpIncRSD%TTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Five Year Relative Standard Deviation |
| `OpIncRegEstANN` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Ten Year Regression Estimate |
| `OpIncRegEstTTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Five Year Regression Estimate |
| `OpIncRegGr%ANN` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Ten Year Regression Estimate |
| `OpIncRegGr%TTM` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Five Year Regression Growth |
| `OpIncPSQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Quarterly Per Share |
| `OpIncPSA` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Annual Per Share |
| `OpInc%SalesQ` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | % of Quarterly Sales |
| `OpInc%SalesA` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | % of Annual Sales |
| `OpInc3YAvg` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Three Year Average |
| `OpInc5YAvg` | Revenues minus cost of goods sold, SG&A, and depreciation/amortization. | Five Year Average |

#### `OpIncAftDepr(offset, type[, NAHandling])`
```p123
OpIncAftDepr(offset, type[, NAHandling])
```

Operating Income After Depreciation is equal to revenues less cost of goods sold; selling, general and administrative costs; and depreciation and amortization.

This line is identical to Operating Income.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `OpIncAftDeprQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Latest Quarter |
| `OpIncAftDeprPQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Previous Quarter |
| `OpIncAftDeprPYQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Previous Quarter 1 Year Ago |
| `OpIncAftDeprTTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Trailing 12 Months |
| `OpIncAftDeprPTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Previous Trailing 12 Months |
| `OpIncAftDeprA` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Latest Year |
| `OpIncAftDeprPY` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Previous Year |
| `OpIncAftDeprGr%PQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Q vs Previous Q Growth |
| `OpIncAftDeprGr%PYQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Q vs 1 year ago Q Growth |
| `OpIncAftDeprGr%TTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Trailing Twelve Months Growth |
| `OpIncAftDeprGr%PQTTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Trailing Twelve Months Growth 1Q Ago |
| `OpIncAftDeprGr%A` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Growth Annual |
| `OpIncAftDeprGr%3Y` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Three Year Annualized Growth |
| `OpIncAftDeprGr%5Y` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Five Year Annualized Growth |
| `OpIncAftDeprGr%10Y` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Ten Year Annualized Growth |
| `OpIncAftDeprRSD%ANN` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Ten Year Relative Standard Deviation |
| `OpIncAftDeprRSD%TTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Five Year Relative Standard Deviation |
| `OpIncAftDeprRegEstANN` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Ten Year Regression Estimate |
| `OpIncAftDeprRegEstTTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Five Year Regression Estimate |
| `OpIncAftDeprRegGr%ANN` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Ten Year Regression Estimate |
| `OpIncAftDeprRegGr%TTM` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Five Year Regression Growth |
| `OpIncAftDeprPSQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Quarterly Per Share |
| `OpIncAftDeprPSA` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Annual Per Share |
| `OpIncAftDepr%SalesQ` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | % of Quarterly Sales |
| `OpIncAftDepr%SalesA` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | % of Annual Sales |
| `OpIncAftDepr3YAvg` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Three Year Average |
| `OpIncAftDepr5YAvg` | Revenues minus COGS, SG&A, and depreciation/amortization. Identical to Operating Income. | Five Year Average |

#### `OpIncBDepr(offset, type[, NAHandling])`
```p123
OpIncBDepr(offset, type[, NAHandling])
```

Operating Income Before Depreciation is revenues less cost of goods sold less selling, general and administrative costs for the period specified by the type input.

This item differs from Operating Income by its inclusion of depreciation and amortization.

We recommend that users substitute this line for EBITDA. The lines used by the data provider to calculate this datum are standard and broadly comparable.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `OpIncBDeprQ` | Revenues minus COGS and SG&A. | Latest Quarter |
| `OpIncBDeprPQ` | Revenues minus COGS and SG&A. | Previous Quarter |
| `OpIncBDeprPYQ` | Revenues minus COGS and SG&A. | Previous Quarter 1 Year Ago |
| `OpIncBDeprTTM` | Revenues minus COGS and SG&A. | Trailing 12 Months |
| `OpIncBDeprPTM` | Revenues minus COGS and SG&A. | Previous Trailing 12 Months |
| `OpIncBDeprA` | Revenues minus COGS and SG&A. | Latest Year |
| `OpIncBDeprPY` | Revenues minus COGS and SG&A. | Previous Year |
| `OpIncBDeprGr%PQ` | Revenues minus COGS and SG&A. | Q vs Previous Q Growth |
| `OpIncBDeprGr%PYQ` | Revenues minus COGS and SG&A. | Q vs 1 year ago Q Growth |
| `OpIncBDeprGr%TTM` | Revenues minus COGS and SG&A. | Trailing Twelve Months Growth |
| `OpIncBDeprGr%PQTTM` | Revenues minus COGS and SG&A. | Trailing Twelve Months Growth 1Q Ago |
| `OpIncBDeprGr%A` | Revenues minus COGS and SG&A. | Growth Annual |
| `OpIncBDeprGr%3Y` | Revenues minus COGS and SG&A. | Three Year Annualized Growth |
| `OpIncBDeprGr%5Y` | Revenues minus COGS and SG&A. | Five Year Annualized Growth |
| `OpIncBDeprGr%10Y` | Revenues minus COGS and SG&A. | Ten Year Annualized Growth |
| `OpIncBDeprRSD%ANN` | Revenues minus COGS and SG&A. | Ten Year Relative Standard Deviation |
| `OpIncBDeprRSD%TTM` | Revenues minus COGS and SG&A. | Five Year Relative Standard Deviation |
| `OpIncBDeprRegEstANN` | Revenues minus COGS and SG&A. | Ten Year Regression Estimate |
| `OpIncBDeprRegEstTTM` | Revenues minus COGS and SG&A. | Five Year Regression Estimate |
| `OpIncBDeprRegGr%ANN` | Revenues minus COGS and SG&A. | Ten Year Regression Estimate |
| `OpIncBDeprRegGr%TTM` | Revenues minus COGS and SG&A. | Five Year Regression Growth |
| `OpIncBDeprPSQ` | Revenues minus COGS and SG&A. | Quarterly Per Share |
| `OpIncBDeprPSA` | Revenues minus COGS and SG&A. | Annual Per Share |
| `OpIncBDepr%SalesQ` | Revenues minus COGS and SG&A. | % of Quarterly Sales |
| `OpIncBDepr%SalesA` | Revenues minus COGS and SG&A. | % of Annual Sales |
| `OpIncBDepr3YAvg` | Revenues minus COGS and SG&A. | Three Year Average |
| `OpIncBDepr5YAvg` | Revenues minus COGS and SG&A. | Five Year Average |

#### `PfdDiv(offset, type[, NAHandling])`
```p123
PfdDiv(offset, type[, NAHandling])
```

Preferred Dividends is the total amount that was paid by the company to preferred shareholders in the time period specified by the type input.

Note that this is total preferred dividends paid across all preferred share issues. We do not offer per share information for preferred shares.

If a company owns preferred shares in another corporate entity then the income from preferred dividends is treated as part of investment income, not deducted from this line.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `PfdDivQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Latest Quarter |
| `PfdDivPQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Previous Quarter |
| `PfdDivPYQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Previous Quarter 1 Year Ago |
| `PfdDivTTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Trailing 12 Months |
| `PfdDivPTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Previous Trailing 12 Months |
| `PfdDivA` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Latest Year |
| `PfdDivPY` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Previous Year |
| `PfdDivGr%PQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Q vs Previous Q Growth |
| `PfdDivGr%PYQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Q vs 1 year ago Q Growth |
| `PfdDivGr%TTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Trailing Twelve Months Growth |
| `PfdDivGr%PQTTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Trailing Twelve Months Growth 1Q Ago |
| `PfdDivGr%A` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Growth Annual |
| `PfdDivGr%3Y` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Three Year Annualized Growth |
| `PfdDivGr%5Y` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Five Year Annualized Growth |
| `PfdDivGr%10Y` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Ten Year Annualized Growth |
| `PfdDivRSD%ANN` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Ten Year Relative Standard Deviation |
| `PfdDivRSD%TTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Five Year Relative Standard Deviation |
| `PfdDivRegEstANN` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Ten Year Regression Estimate |
| `PfdDivRegEstTTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Five Year Regression Estimate |
| `PfdDivRegGr%ANN` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Ten Year Regression Estimate |
| `PfdDivRegGr%TTM` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Five Year Regression Growth |
| `PfdDivPSQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Quarterly Per Share |
| `PfdDivPSA` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Annual Per Share |
| `PfdDiv%SalesQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | % of Quarterly Sales |
| `PfdDiv%SalesA` | Total amount paid to preferred shareholders across all preferred share issues during the period. | % of Annual Sales |
| `PfdDiv%AssetsQ` | Total amount paid to preferred shareholders across all preferred share issues during the period. | % of Quarterly Assets |
| `PfdDiv%AssetsA` | Total amount paid to preferred shareholders across all preferred share issues during the period. | % of Annual Assets |
| `PfdDiv3YAvg` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Three Year Average |
| `PfdDiv5YAvg` | Total amount paid to preferred shareholders across all preferred share issues during the period. | Five Year Average |

#### `RandD(offset, type[, NAHandling])`
```p123
RandD(offset, type[, NAHandling])
```

Research and Development expense is the amount spent by a company for investment in future products and services during a period specified by the type input.

CompuStat includes software development and amortization expenses in this line.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `RandDQ` | Spending on future products/services during the period. | Latest Quarter |
| `RandDPQ` | Spending on future products/services during the period. | Previous Quarter |
| `RandDPYQ` | Spending on future products/services during the period. | Previous Quarter 1 Year Ago |
| `RandDTTM` | Spending on future products/services during the period. | Trailing 12 Months |
| `RandDPTM` | Spending on future products/services during the period. | Previous Trailing 12 Months |
| `RandDA` | Spending on future products/services during the period. | Latest Year |
| `RandDPY` | Spending on future products/services during the period. | Previous Year |
| `RandDGr%PQ` | Spending on future products/services during the period. | Q vs Previous Q Growth |
| `RandDGr%PYQ` | Spending on future products/services during the period. | Q vs 1 year ago Q Growth |
| `RandDGr%TTM` | Spending on future products/services during the period. | Trailing Twelve Months Growth |
| `RandDGr%PQTTM` | Spending on future products/services during the period. | Trailing Twelve Months Growth 1Q Ago |
| `RandDGr%A` | Spending on future products/services during the period. | Growth Annual |
| `RandDGr%3Y` | Spending on future products/services during the period. | Three Year Annualized Growth |
| `RandDGr%5Y` | Spending on future products/services during the period. | Five Year Annualized Growth |
| `RandDGr%10Y` | Spending on future products/services during the period. | Ten Year Annualized Growth |
| `RandDRSD%ANN` | Spending on future products/services during the period. | Ten Year Relative Standard Deviation |
| `RandDRSD%TTM` | Spending on future products/services during the period. | Five Year Relative Standard Deviation |
| `RandDRegEstANN` | Spending on future products/services during the period. | Ten Year Regression Estimate |
| `RandDRegEstTTM` | Spending on future products/services during the period. | Five Year Regression Estimate |
| `RandDRegGr%ANN` | Spending on future products/services during the period. | Ten Year Regression Estimate |
| `RandDRegGr%TTM` | Spending on future products/services during the period. | Five Year Regression Growth |
| `RandDPSQ` | Spending on future products/services during the period. | Quarterly Per Share |
| `RandDPSA` | Spending on future products/services during the period. | Annual Per Share |
| `RandD%SalesQ` | Spending on future products/services during the period. | % of Quarterly Sales |
| `RandD%SalesA` | Spending on future products/services during the period. | % of Annual Sales |
| `RandD%AssetsQ` | Spending on future products/services during the period. | % of Quarterly Assets |
| `RandD%AssetsA` | Spending on future products/services during the period. | % of Annual Assets |
| `RandD3YAvg` | Spending on future products/services during the period. | Three Year Average |
| `RandD5YAvg` | Spending on future products/services during the period. | Five Year Average |

#### `SalesIntl(offset, type[, NAHandling])`
```p123
SalesIntl(offset, type[, NAHandling])
```

Represents sales generated from operations in foreign countries. Export sales are not included. Only Annual data is available. It excludes:

- Export sales

- Excise taxes

- Windfall profit taxes

- Value Added taxes (VAT)

- General and Services taxes (GST)

- Eliminations

- Corporate Revenue

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SalesIntlA` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Latest Year |
| `SalesIntlPY` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Previous Year |
| `SalesIntlGr%A` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Growth Annual |
| `SalesIntlGr%3Y` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Three Year Annualized Growth |
| `SalesIntlGr%5Y` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Five Year Annualized Growth |
| `SalesIntlGr%10Y` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Ten Year Annualized Growth |
| `SalesIntl3YAvg` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Three Year Average |
| `SalesIntl5YAvg` | Represents sales generated from operations in foreign countries. Export sales are not included. Annual values only. | Five Year Average |

#### `Sales(offset, type[, NAHandling])`
```p123
Sales(offset, type[, NAHandling])
```

Revenue, often referred to as Sales or Income, represents the total value of all goods and services sold or provided by a company within a specific period. It is a crucial line item on a company's income statement and is commonly known as the "Top Line." This figure serves as the starting point for income calculation. From this, various expenses are subtracted to determine the company's Profit or Net Income, providing insight into the financial performance of the business.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SalesQ` | Total value of goods/services sold in a period. | Latest Quarter |
| `SalesPQ` | Total value of goods/services sold in a period. | Previous Quarter |
| `SalesPYQ` | Total value of goods/services sold in a period. | Previous Quarter 1 Year Ago |
| `SalesTTM` | Total value of goods/services sold in a period. | Trailing 12 Months |
| `SalesPTM` | Total value of goods/services sold in a period. | Previous Trailing 12 Months |
| `SalesA` | Total value of goods/services sold in a period. | Latest Year |
| `SalesPY` | Total value of goods/services sold in a period. | Previous Year |
| `SalesGr%PQ` | Total value of goods/services sold in a period. | Q vs Previous Q Growth |
| `SalesGr%PYQ` | Total value of goods/services sold in a period. | Q vs 1 year ago Q Growth |
| `SalesGr%TTM` | Total value of goods/services sold in a period. | Trailing Twelve Months Growth |
| `SalesGr%PQTTM` | Total value of goods/services sold in a period. | Trailing Twelve Months Growth 1Q Ago |
| `SalesGr%A` | Total value of goods/services sold in a period. | Growth Annual |
| `SalesGr%3Y` | Total value of goods/services sold in a period. | Three Year Annualized Growth |
| `SalesGr%5Y` | Total value of goods/services sold in a period. | Five Year Annualized Growth |
| `SalesGr%10Y` | Total value of goods/services sold in a period. | Ten Year Annualized Growth |
| `SalesRSD%ANN` | Total value of goods/services sold in a period. | Ten Year Relative Standard Deviation |
| `SalesRSD%TTM` | Total value of goods/services sold in a period. | Five Year Relative Standard Deviation |
| `SalesRegEstANN` | Total value of goods/services sold in a period. | Ten Year Regression Estimate |
| `SalesRegEstTTM` | Total value of goods/services sold in a period. | Five Year Regression Estimate |
| `SalesRegGr%ANN` | Total value of goods/services sold in a period. | Ten Year Regression Estimate |
| `SalesRegGr%TTM` | Total value of goods/services sold in a period. | Five Year Regression Growth |
| `SalesPSQ` | Total value of goods/services sold in a period. | Quarterly Per Share |
| `SalesPSA` | Total value of goods/services sold in a period. | Annual Per Share |
| `Sales%AssetsQ` | Total value of goods/services sold in a period. | % of Quarterly Assets |
| `Sales%AssetsA` | Total value of goods/services sold in a period. | % of Annual Assets |
| `Sales3YAvg` | Total value of goods/services sold in a period. | Three Year Average |
| `Sales5YAvg` | Total value of goods/services sold in a period. | Five Year Average |

#### `SGandA(offset, type[, NAHandling])`
```p123
SGandA(offset, type[, NAHandling])
```

Selling, general, and administrative expenses (SG&A) in a company's income statement encompass all general and administrative expenses (G&A) along with both direct and indirect selling expenses of the business. We differentiate between two versions of this expense category: SG&A and SG&A_GAAP. The former includes most operational costs not directly tied to the creation of a product or the execution of a service, excluding Research and Development (R&D) expenses. In contrast, SG&A_GAAP, adhering to Generally Accepted Accounting Principles (GAAP), integrates R&D expenses, providing a comprehensive overview of a company's operational expenditures.

The choice between SG&A and SG&A_GAAP depends on the analytical focus: SG&A offers a view excluding R&D for strategies prioritizing direct operational costs, while SG&A_GAAP provides a fuller picture of all operational expenses, including R&D.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SGandAQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Latest Quarter |
| `SGandAPQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Previous Quarter |
| `SGandAPYQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Previous Quarter 1 Year Ago |
| `SGandATTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Trailing 12 Months |
| `SGandAPTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Previous Trailing 12 Months |
| `SGandAA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Latest Year |
| `SGandAPY` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Previous Year |
| `SGandAGr%PQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Q vs Previous Q Growth |
| `SGandAGr%PYQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Q vs 1 year ago Q Growth |
| `SGandAGr%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Trailing Twelve Months Growth |
| `SGandAGr%PQTTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Trailing Twelve Months Growth 1Q Ago |
| `SGandAGr%A` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Growth Annual |
| `SGandAGr%3Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Three Year Annualized Growth |
| `SGandAGr%5Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Five Year Annualized Growth |
| `SGandAGr%10Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Ten Year Annualized Growth |
| `SGandARSD%ANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Ten Year Relative Standard Deviation |
| `SGandARSD%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Five Year Relative Standard Deviation |
| `SGandARegEstANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Ten Year Regression Estimate |
| `SGandARegEstTTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Five Year Regression Estimate |
| `SGandARegGr%ANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Ten Year Regression Estimate |
| `SGandARegGr%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Five Year Regression Growth |
| `SGandAPSQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Quarterly Per Share |
| `SGandAPSA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Annual Per Share |
| `SGandA%SalesQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | % of Quarterly Sales |
| `SGandA%SalesA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | % of Annual Sales |
| `SGandA%AssetsQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | % of Quarterly Assets |
| `SGandA%AssetsA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | % of Annual Assets |
| `SGandA3YAvg` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Three Year Average |
| `SGandA5YAvg` | Expenses include all general/administrative costs plus direct/indirect selling expenses - excludes R&D expenses. | Five Year Average |

#### `SGandA_GAAP(offset, type[, NAHandling])`
```p123
SGandA_GAAP(offset, type[, NAHandling])
```

Selling, general, and administrative expenses (SG&A) in a company's income statement encompass all general and administrative expenses (G&A) along with both direct and indirect selling expenses of the business. We differentiate between two versions of this expense category: SG&A and SG&A_GAAP. The former includes most operational costs not directly tied to the creation of a product or the execution of a service, excluding Research and Development (R&D) expenses. In contrast, SG&A_GAAP, adhering to Generally Accepted Accounting Principles (GAAP), integrates R&D expenses, providing a comprehensive overview of a company's operational expenditures.

The choice between SG&A and SG&A_GAAP depends on the analytical focus: SG&A offers a view excluding R&D for strategies prioritizing direct operational costs, while SG&A_GAAP provides a fuller picture of all operational expenses, including R&D.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SGandA_GAAPQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Latest Quarter |
| `SGandA_GAAPPQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Previous Quarter |
| `SGandA_GAAPPYQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Previous Quarter 1 Year Ago |
| `SGandA_GAAPTTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Trailing 12 Months |
| `SGandA_GAAPPTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Previous Trailing 12 Months |
| `SGandA_GAAPA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Latest Year |
| `SGandA_GAAPPY` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Previous Year |
| `SGandA_GAAPGr%PQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Q vs Previous Q Growth |
| `SGandA_GAAPGr%PYQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Q vs 1 year ago Q Growth |
| `SGandA_GAAPGr%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Trailing Twelve Months Growth |
| `SGandA_GAAPGr%PQTTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Trailing Twelve Months Growth 1Q Ago |
| `SGandA_GAAPGr%A` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Growth Annual |
| `SGandA_GAAPGr%3Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Three Year Annualized Growth |
| `SGandA_GAAPGr%5Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Five Year Annualized Growth |
| `SGandA_GAAPGr%10Y` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Ten Year Annualized Growth |
| `SGandA_GAAPRSD%ANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Ten Year Relative Standard Deviation |
| `SGandA_GAAPRSD%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Five Year Relative Standard Deviation |
| `SGandA_GAAPRegEstANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Ten Year Regression Estimate |
| `SGandA_GAAPRegEstTTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Five Year Regression Estimate |
| `SGandA_GAAPRegGr%ANN` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Ten Year Regression Estimate |
| `SGandA_GAAPRegGr%TTM` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Five Year Regression Growth |
| `SGandA_GAAPPSQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Quarterly Per Share |
| `SGandA_GAAPPSA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Annual Per Share |
| `SGandA_GAAP%SalesQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | % of Quarterly Sales |
| `SGandA_GAAP%SalesA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | % of Annual Sales |
| `SGandA_GAAP%AssetsQ` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | % of Quarterly Assets |
| `SGandA_GAAP%AssetsA` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | % of Annual Assets |
| `SGandA_GAAP3YAvg` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Three Year Average |
| `SGandA_GAAP5YAvg` | Expenses include all general/administrative costs plus direct/indirect selling expenses - includes R&D expenses. | Five Year Average |

#### `SpcItems(offset, type[, NAHandling])`
```p123
SpcItems(offset, type[, NAHandling])
```

Special Items is the total of all pre-tax items that are non-recurring. Note that anything after the tax line is not included.

Examples of things that a company could report that would be included in this line are moving expenses, severance payments, write-offs or write-downs, or reserves for litigation.

Users may want to experiment with this item as an indicator of earnings quality.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SpcItemsQ` | Total pre-tax non-recurring items. | Latest Quarter |
| `SpcItemsPQ` | Total pre-tax non-recurring items. | Previous Quarter |
| `SpcItemsPYQ` | Total pre-tax non-recurring items. | Previous Quarter 1 Year Ago |
| `SpcItemsTTM` | Total pre-tax non-recurring items. | Trailing 12 Months |
| `SpcItemsPTM` | Total pre-tax non-recurring items. | Previous Trailing 12 Months |
| `SpcItemsA` | Total pre-tax non-recurring items. | Latest Year |
| `SpcItemsPY` | Total pre-tax non-recurring items. | Previous Year |
| `SpcItemsGr%PQ` | Total pre-tax non-recurring items. | Q vs Previous Q Growth |
| `SpcItemsGr%PYQ` | Total pre-tax non-recurring items. | Q vs 1 year ago Q Growth |
| `SpcItemsGr%TTM` | Total pre-tax non-recurring items. | Trailing Twelve Months Growth |
| `SpcItemsGr%PQTTM` | Total pre-tax non-recurring items. | Trailing Twelve Months Growth 1Q Ago |
| `SpcItemsGr%A` | Total pre-tax non-recurring items. | Growth Annual |
| `SpcItemsGr%3Y` | Total pre-tax non-recurring items. | Three Year Annualized Growth |
| `SpcItemsGr%5Y` | Total pre-tax non-recurring items. | Five Year Annualized Growth |
| `SpcItemsGr%10Y` | Total pre-tax non-recurring items. | Ten Year Annualized Growth |
| `SpcItemsRSD%ANN` | Total pre-tax non-recurring items. | Ten Year Relative Standard Deviation |
| `SpcItemsRSD%TTM` | Total pre-tax non-recurring items. | Five Year Relative Standard Deviation |
| `SpcItemsRegEstANN` | Total pre-tax non-recurring items. | Ten Year Regression Estimate |
| `SpcItemsRegEstTTM` | Total pre-tax non-recurring items. | Five Year Regression Estimate |
| `SpcItemsRegGr%ANN` | Total pre-tax non-recurring items. | Ten Year Regression Estimate |
| `SpcItemsRegGr%TTM` | Total pre-tax non-recurring items. | Five Year Regression Growth |
| `SpcItemsPSQ` | Total pre-tax non-recurring items. | Quarterly Per Share |
| `SpcItemsPSA` | Total pre-tax non-recurring items. | Annual Per Share |
| `SpcItems%SalesQ` | Total pre-tax non-recurring items. | % of Quarterly Sales |
| `SpcItems%SalesA` | Total pre-tax non-recurring items. | % of Annual Sales |
| `SpcItems%AssetsQ` | Total pre-tax non-recurring items. | % of Quarterly Assets |
| `SpcItems%AssetsA` | Total pre-tax non-recurring items. | % of Annual Assets |
| `SpcItems3YAvg` | Total pre-tax non-recurring items. | Three Year Average |
| `SpcItems5YAvg` | Total pre-tax non-recurring items. | Five Year Average |

#### `StkOptExp(offset, type[, NAHandling])`
```p123
StkOptExp(offset, type[, NAHandling])
```

Stock-based compensation represents employee compensation paid through equity instruments (stock options, restricted stock units, etc.) rather than cash. This creates a unique accounting situation where expenses are recognized without corresponding cash outflows. The accounting rules require companies to:

-
Record an expense on the income statement (StkOptExp) - showing the economic cost

-
Add it back on the cash flow statement (StkOptCF) - because no cash was actually spent

StkOptExp

StkOptExp is the expense companies record for employee stock compensation like stock options and restricted stock. This cost appears on the income statement as an operating expense that reduces earnings. The expense reflects the fair value of stock awards given to employees, spread out over the time period when employees earn the right to use them (the vesting period).

Key Characteristics:

-
Appears primarily within SG&A (Selling, General & Administrative) or R&D in the income statement, and reduces operating income and net income

-
Non-cash expense representing the fair value of equity awards

-
Recognized over the vesting period using fair value at grant date

-
Directly impacts reported earnings and EPS

StkOptCF

StkOptCF is the stock-based compensation adjustment that appears in the operating activities section of the cash flow statement. This function addresses the accounting treatment of stock-based compensation, which is a non-cash expense that reduces net income on the income statement but must be added back when calculating cash flow from operations.

Key Characteristics:

-
Appears in operating activities section of cash flow statement

-
Added back to net income when calculating cash from operations

-
Reconciles the non-cash expense from the income statement

-
No actual cash leaves the company for this expense

Key Differences

| Aspect | StkOptExp | StkOptCF |
| Financial Statement | Income Statement | Cash Flow Statement |
| Impact | Reduces net income | Increases operating cash flow |
| Purpose | Shows economic cost to shareholders | Adjusts for non-cash charge |
| Direction | Expense (negative) | Add-back (positive) |

Practical Applications

Financial Analysis Uses

-
Profitability Analysis: Use StkOptExp to understand true operating costs including dilution

-
Cash Flow Analysis: Use StkOptCF to calculate actual cash generation

-
Valuation Models: Both factors needed for accurate DCF and earnings adjustments

-
Peer Comparison: Compare compensation structures and their financial impacts

Common Analytical Adjustments

-
Adjusted EBITDA: Often adds back StkOptExp to show earnings before this non-cash charge

-
Free Cash Flow: StkOptCF ensures FCF reflects actual cash available

-
Non-GAAP Earnings: Companies may exclude StkOptExp from adjusted earnings metrics

-
Return on Capital: Consider whether to include StkOptExp in operating income calculations

Important Relationships

Expected Relationship

-
Over time, StkOptCF and StkOptExp should converge, but may differ in any given period due to grant timing, forfeitures, or classification nuances

-
Both represent the same economic transaction from different perspectives

-
Analysts often expect alignment, but timing mismatches can confuse without understanding these potential differences

Potential Differences

-
Timing: Recognition differences between statements

-
Classification: Expenses may be allocated differently

-
Tax Effects: Tax benefits may create variations

-
Forfeitures: Changes in forfeiture estimates affect amounts

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `StkOptExpQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Latest Quarter |
| `StkOptExpPQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Previous Quarter |
| `StkOptExpPYQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Previous Quarter 1 Year Ago |
| `StkOptExpTTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Trailing 12 Months |
| `StkOptExpPTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Previous Trailing 12 Months |
| `StkOptExpA` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Latest Year |
| `StkOptExpPY` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Previous Year |
| `StkOptExpGr%PQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Q vs Previous Q Growth |
| `StkOptExpGr%PYQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Q vs 1 year ago Q Growth |
| `StkOptExpGr%TTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Trailing Twelve Months Growth |
| `StkOptExpGr%PQTTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Trailing Twelve Months Growth 1Q Ago |
| `StkOptExpGr%A` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Growth Annual |
| `StkOptExpGr%3Y` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Three Year Annualized Growth |
| `StkOptExpGr%5Y` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Five Year Annualized Growth |
| `StkOptExpGr%10Y` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Ten Year Annualized Growth |
| `StkOptExpRSD%ANN` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Ten Year Relative Standard Deviation |
| `StkOptExpRSD%TTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Five Year Relative Standard Deviation |
| `StkOptExpRegEstANN` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Ten Year Regression Estimate |
| `StkOptExpRegEstTTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Five Year Regression Estimate |
| `StkOptExpRegGr%ANN` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Ten Year Regression Estimate |
| `StkOptExpRegGr%TTM` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Five Year Regression Growth |
| `StkOptExpPSQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Quarterly Per Share |
| `StkOptExpPSA` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Annual Per Share |
| `StkOptExp%SalesQ` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | % of Quarterly Sales |
| `StkOptExp%SalesA` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | % of Annual Sales |
| `StkOptExp3YAvg` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Three Year Average |
| `StkOptExp5YAvg` | Income statement SBC. Data begins around 2003, with full annual coverage starting in 2008, and interim in 2017 | Five Year Average |

#### `TxRate%(offset, type[, NAHandling])`
```p123
TxRate%(offset, type[, NAHandling])
```

Effective Tax Rate is tax expense divided by pre-tax income (and multiplied by 100). Both tax expense and pre-tax income are for the period specified by the type input.

This item is undefined (and will return an NA) when pre-tax income is zero or negative. Note that this item can be negative when tax expense is negative. This indicates that the company in question is enjoying tax credits or net-operating losses from prior periods. In either case, investors should expect that this is a temporary condition.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Formula**
```p123
TxRate% = 100 * a / b
a = IncTaxExp Income Tax Expense
b = IncBTax Income Before Taxes
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TxRate%Q` | Tax expense as percentage of pre-tax income. | Latest Quarter |
| `TxRate%PQ` | Tax expense as percentage of pre-tax income. | Previous Quarter |
| `TxRate%PYQ` | Tax expense as percentage of pre-tax income. | Previous Quarter 1 Year Ago |
| `TxRate%TTM` | Tax expense as percentage of pre-tax income. | Trailing 12 Months |
| `TxRate%PTM` | Tax expense as percentage of pre-tax income. | Previous Trailing 12 Months |
| `TxRate%A` | Tax expense as percentage of pre-tax income. | Latest Year |
| `TxRate%PY` | Tax expense as percentage of pre-tax income. | Previous Year |
| `TxRate%Gr%PQ` | Tax expense as percentage of pre-tax income. | Q vs Previous Q Growth |
| `TxRate%Gr%PYQ` | Tax expense as percentage of pre-tax income. | Q vs 1 year ago Q Growth |
| `TxRate%Gr%TTM` | Tax expense as percentage of pre-tax income. | Trailing Twelve Months Growth |
| `TxRate%Gr%PQTTM` | Tax expense as percentage of pre-tax income. | Trailing Twelve Months Growth 1Q Ago |
| `TxRate%Gr%A` | Tax expense as percentage of pre-tax income. | Growth Annual |
| `TxRate%Gr%3Y` | Tax expense as percentage of pre-tax income. | Three Year Annualized Growth |
| `TxRate%Gr%5Y` | Tax expense as percentage of pre-tax income. | Five Year Annualized Growth |
| `TxRate%Gr%10Y` | Tax expense as percentage of pre-tax income. | Ten Year Annualized Growth |
| `TxRate%RSD%ANN` | Tax expense as percentage of pre-tax income. | Ten Year Relative Standard Deviation |
| `TxRate%RSD%TTM` | Tax expense as percentage of pre-tax income. | Five Year Relative Standard Deviation |
| `TxRate%RegEstANN` | Tax expense as percentage of pre-tax income. | Ten Year Regression Estimate |
| `TxRate%RegEstTTM` | Tax expense as percentage of pre-tax income. | Five Year Regression Estimate |
| `TxRate%RegGr%ANN` | Tax expense as percentage of pre-tax income. | Ten Year Regression Estimate |
| `TxRate%RegGr%TTM` | Tax expense as percentage of pre-tax income. | Five Year Regression Growth |
| `TxRate%3YAvg` | Tax expense as percentage of pre-tax income. | Three Year Average |
| `TxRate%5YAvg` | Tax expense as percentage of pre-tax income. | Five Year Average |

## Balance Sheet

### Assets-Current

#### `Recvbl(offset, type[, NAHandling])`
```p123
Recvbl(offset, type[, NAHandling])
```

Receivables is a line item under current assets on a company's balance sheet, signifying amounts due to the company. These amounts are typically expected to be collected within the 12 months following the balance sheet date. This category encompasses money owed by customers, clients, or other entities, often arising from sales of goods or services on credit terms.

The reported figure for Receivable is usually presented net of allowances for doubtful accounts. This means that the company has already accounted for and deducted the estimated uncollectible amounts, providing a more realistic view of the receivables that the company expects to convert into cash.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `RecvblQ` | Amounts due to the company within 12 months, typically from credit sales. | Latest Quarter |
| `RecvblPQ` | Amounts due to the company within 12 months, typically from credit sales. | Previous Quarter |
| `RecvblPYQ` | Amounts due to the company within 12 months, typically from credit sales. | Previous Quarter 1 Year Ago |
| `RecvblTTM` | Amounts due to the company within 12 months, typically from credit sales. | Trailing 12 Months |
| `RecvblPTM` | Amounts due to the company within 12 months, typically from credit sales. | Previous Trailing 12 Months |
| `RecvblA` | Amounts due to the company within 12 months, typically from credit sales. | Latest Year |
| `RecvblPY` | Amounts due to the company within 12 months, typically from credit sales. | Previous Year |
| `RecvblGr%PQ` | Amounts due to the company within 12 months, typically from credit sales. | Q vs Previous Q Growth |
| `RecvblGr%PYQ` | Amounts due to the company within 12 months, typically from credit sales. | Q vs 1 year ago Q Growth |
| `RecvblGr%TTM` | Amounts due to the company within 12 months, typically from credit sales. | Trailing Twelve Months Growth |
| `RecvblGr%PQTTM` | Amounts due to the company within 12 months, typically from credit sales. | Trailing Twelve Months Growth 1Q Ago |
| `RecvblGr%A` | Amounts due to the company within 12 months, typically from credit sales. | Growth Annual |
| `RecvblGr%3Y` | Amounts due to the company within 12 months, typically from credit sales. | Three Year Annualized Growth |
| `RecvblGr%5Y` | Amounts due to the company within 12 months, typically from credit sales. | Five Year Annualized Growth |
| `RecvblGr%10Y` | Amounts due to the company within 12 months, typically from credit sales. | Ten Year Annualized Growth |
| `RecvblRSD%ANN` | Amounts due to the company within 12 months, typically from credit sales. | Ten Year Relative Standard Deviation |
| `RecvblRSD%TTM` | Amounts due to the company within 12 months, typically from credit sales. | Five Year Relative Standard Deviation |
| `RecvblRegEstANN` | Amounts due to the company within 12 months, typically from credit sales. | Ten Year Regression Estimate |
| `RecvblRegEstTTM` | Amounts due to the company within 12 months, typically from credit sales. | Five Year Regression Estimate |
| `RecvblRegGr%ANN` | Amounts due to the company within 12 months, typically from credit sales. | Ten Year Regression Estimate |
| `RecvblRegGr%TTM` | Amounts due to the company within 12 months, typically from credit sales. | Five Year Regression Growth |
| `RecvblPSQ` | Amounts due to the company within 12 months, typically from credit sales. | Quarterly Per Share |
| `RecvblPSA` | Amounts due to the company within 12 months, typically from credit sales. | Annual Per Share |
| `Recvbl%AssetsQ` | Amounts due to the company within 12 months, typically from credit sales. | % of Quarterly Assets |
| `Recvbl%AssetsA` | Amounts due to the company within 12 months, typically from credit sales. | % of Annual Assets |
| `Recvbl3YAvg` | Amounts due to the company within 12 months, typically from credit sales. | Three Year Average |
| `Recvbl5YAvg` | Amounts due to the company within 12 months, typically from credit sales. | Five Year Average |

#### `Cash(offset, type[, NAHandling])`
```p123
Cash(offset, type[, NAHandling])
```

Cash is the amount of cash and equivalents as reported by the company under current assets. Note that it does not include short-term investments.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CashQ` | Amount of cash and equivalents not including short-term investments. | Latest Quarter |
| `CashPQ` | Amount of cash and equivalents not including short-term investments. | Previous Quarter |
| `CashPYQ` | Amount of cash and equivalents not including short-term investments. | Previous Quarter 1 Year Ago |
| `CashTTM` | Amount of cash and equivalents not including short-term investments. | Trailing 12 Months |
| `CashPTM` | Amount of cash and equivalents not including short-term investments. | Previous Trailing 12 Months |
| `CashA` | Amount of cash and equivalents not including short-term investments. | Latest Year |
| `CashPY` | Amount of cash and equivalents not including short-term investments. | Previous Year |
| `CashGr%PQ` | Amount of cash and equivalents not including short-term investments. | Q vs Previous Q Growth |
| `CashGr%PYQ` | Amount of cash and equivalents not including short-term investments. | Q vs 1 year ago Q Growth |
| `CashGr%TTM` | Amount of cash and equivalents not including short-term investments. | Trailing Twelve Months Growth |
| `CashGr%PQTTM` | Amount of cash and equivalents not including short-term investments. | Trailing Twelve Months Growth 1Q Ago |
| `CashGr%A` | Amount of cash and equivalents not including short-term investments. | Growth Annual |
| `CashGr%3Y` | Amount of cash and equivalents not including short-term investments. | Three Year Annualized Growth |
| `CashGr%5Y` | Amount of cash and equivalents not including short-term investments. | Five Year Annualized Growth |
| `CashGr%10Y` | Amount of cash and equivalents not including short-term investments. | Ten Year Annualized Growth |
| `CashRSD%ANN` | Amount of cash and equivalents not including short-term investments. | Ten Year Relative Standard Deviation |
| `CashRSD%TTM` | Amount of cash and equivalents not including short-term investments. | Five Year Relative Standard Deviation |
| `CashRegEstANN` | Amount of cash and equivalents not including short-term investments. | Ten Year Regression Estimate |
| `CashRegEstTTM` | Amount of cash and equivalents not including short-term investments. | Five Year Regression Estimate |
| `CashRegGr%ANN` | Amount of cash and equivalents not including short-term investments. | Ten Year Regression Estimate |
| `CashRegGr%TTM` | Amount of cash and equivalents not including short-term investments. | Five Year Regression Growth |
| `CashPSQ` | Amount of cash and equivalents not including short-term investments. | Quarterly Per Share |
| `CashPSA` | Amount of cash and equivalents not including short-term investments. | Annual Per Share |
| `Cash%AssetsQ` | Amount of cash and equivalents not including short-term investments. | % of Quarterly Assets |
| `Cash%AssetsA` | Amount of cash and equivalents not including short-term investments. | % of Annual Assets |
| `Cash3YAvg` | Amount of cash and equivalents not including short-term investments. | Three Year Average |
| `Cash5YAvg` | Amount of cash and equivalents not including short-term investments. | Five Year Average |

#### `CashEquiv(offset, type[, NAHandling])`
```p123
CashEquiv(offset, type[, NAHandling])
```

Cash and Equivalents is total cash. It includes both cash and short-term investments.

For FactSet, the function is slightly more complicated. For most companies, it is the maximum of either cash (FF_CASH_ONLY) or cash and short-term investments (FF_CASH_ST). For financials, it is the maximum of either cash due (FF_CASH_DUE_FR_BK) or short term investments available to trade (FF_INVEST_OTH).

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CashEquivQ` | Total cash available. It includes both cash and short-term investments. | Latest Quarter |
| `CashEquivPQ` | Total cash available. It includes both cash and short-term investments. | Previous Quarter |
| `CashEquivPYQ` | Total cash available. It includes both cash and short-term investments. | Previous Quarter 1 Year Ago |
| `CashEquivTTM` | Total cash available. It includes both cash and short-term investments. | Trailing 12 Months |
| `CashEquivPTM` | Total cash available. It includes both cash and short-term investments. | Previous Trailing 12 Months |
| `CashEquivA` | Total cash available. It includes both cash and short-term investments. | Latest Year |
| `CashEquivPY` | Total cash available. It includes both cash and short-term investments. | Previous Year |
| `CashEquivGr%PQ` | Total cash available. It includes both cash and short-term investments. | Q vs Previous Q Growth |
| `CashEquivGr%PYQ` | Total cash available. It includes both cash and short-term investments. | Q vs 1 year ago Q Growth |
| `CashEquivGr%TTM` | Total cash available. It includes both cash and short-term investments. | Trailing Twelve Months Growth |
| `CashEquivGr%PQTTM` | Total cash available. It includes both cash and short-term investments. | Trailing Twelve Months Growth 1Q Ago |
| `CashEquivGr%A` | Total cash available. It includes both cash and short-term investments. | Growth Annual |
| `CashEquivGr%3Y` | Total cash available. It includes both cash and short-term investments. | Three Year Annualized Growth |
| `CashEquivGr%5Y` | Total cash available. It includes both cash and short-term investments. | Five Year Annualized Growth |
| `CashEquivGr%10Y` | Total cash available. It includes both cash and short-term investments. | Ten Year Annualized Growth |
| `CashEquivRSD%ANN` | Total cash available. It includes both cash and short-term investments. | Ten Year Relative Standard Deviation |
| `CashEquivRSD%TTM` | Total cash available. It includes both cash and short-term investments. | Five Year Relative Standard Deviation |
| `CashEquivRegEstANN` | Total cash available. It includes both cash and short-term investments. | Ten Year Regression Estimate |
| `CashEquivRegEstTTM` | Total cash available. It includes both cash and short-term investments. | Five Year Regression Estimate |
| `CashEquivRegGr%ANN` | Total cash available. It includes both cash and short-term investments. | Ten Year Regression Estimate |
| `CashEquivRegGr%TTM` | Total cash available. It includes both cash and short-term investments. | Five Year Regression Growth |
| `CashEquivPSQ` | Total cash available. It includes both cash and short-term investments. | Quarterly Per Share |
| `CashEquivPSA` | Total cash available. It includes both cash and short-term investments. | Annual Per Share |
| `CashEquiv%AssetsQ` | Total cash available. It includes both cash and short-term investments. | % of Quarterly Assets |
| `CashEquiv%AssetsA` | Total cash available. It includes both cash and short-term investments. | % of Annual Assets |
| `CashEquiv3YAvg` | Total cash available. It includes both cash and short-term investments. | Three Year Average |
| `CashEquiv5YAvg` | Total cash available. It includes both cash and short-term investments. | Five Year Average |

#### `AstCurOther(offset, type[, NAHandling])`
```p123
AstCurOther(offset, type[, NAHandling])
```

Other Current Assets is the total of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory.

The lion's share of this item is prepaid expenses and accrued income, though CompuStat also puts "sundry other" into it.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AstCurOtherQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Latest Quarter |
| `AstCurOtherPQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Previous Quarter |
| `AstCurOtherPYQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Previous Quarter 1 Year Ago |
| `AstCurOtherTTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Trailing 12 Months |
| `AstCurOtherPTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Previous Trailing 12 Months |
| `AstCurOtherA` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Latest Year |
| `AstCurOtherPY` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Previous Year |
| `AstCurOtherGr%PQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Q vs Previous Q Growth |
| `AstCurOtherGr%PYQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Q vs 1 year ago Q Growth |
| `AstCurOtherGr%TTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Trailing Twelve Months Growth |
| `AstCurOtherGr%PQTTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Trailing Twelve Months Growth 1Q Ago |
| `AstCurOtherGr%A` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Growth Annual |
| `AstCurOtherGr%3Y` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Three Year Annualized Growth |
| `AstCurOtherGr%5Y` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Five Year Annualized Growth |
| `AstCurOtherGr%10Y` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Ten Year Annualized Growth |
| `AstCurOtherRSD%ANN` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Ten Year Relative Standard Deviation |
| `AstCurOtherRSD%TTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Five Year Relative Standard Deviation |
| `AstCurOtherRegEstANN` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Ten Year Regression Estimate |
| `AstCurOtherRegEstTTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Five Year Regression Estimate |
| `AstCurOtherRegGr%ANN` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Ten Year Regression Estimate |
| `AstCurOtherRegGr%TTM` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Five Year Regression Growth |
| `AstCurOtherPSQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Quarterly Per Share |
| `AstCurOtherPSA` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Annual Per Share |
| `AstCurOther%AssetsQ` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | % of Quarterly Assets |
| `AstCurOther%AssetsA` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | % of Annual Assets |
| `AstCurOther3YAvg` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Three Year Average |
| `AstCurOther5YAvg` | Sum of all current assets that are not included in cash, cash equivalents, short-term investments, receivables or inventory. | Five Year Average |

#### `AstCur(offset, type[, NAHandling])`
```p123
AstCur(offset, type[, NAHandling])
```

This value is the sum of all current assets reported for the most recent fiscal quarter.

NOTE: Banks do not distinguish between current and long term assets. For these companies this value will be NA.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AstCurQ` | Sum of all assets expected to convert to cash within 12 months. | Latest Quarter |
| `AstCurPQ` | Sum of all assets expected to convert to cash within 12 months. | Previous Quarter |
| `AstCurPYQ` | Sum of all assets expected to convert to cash within 12 months. | Previous Quarter 1 Year Ago |
| `AstCurTTM` | Sum of all assets expected to convert to cash within 12 months. | Trailing 12 Months |
| `AstCurPTM` | Sum of all assets expected to convert to cash within 12 months. | Previous Trailing 12 Months |
| `AstCurA` | Sum of all assets expected to convert to cash within 12 months. | Latest Year |
| `AstCurPY` | Sum of all assets expected to convert to cash within 12 months. | Previous Year |
| `AstCurGr%PQ` | Sum of all assets expected to convert to cash within 12 months. | Q vs Previous Q Growth |
| `AstCurGr%PYQ` | Sum of all assets expected to convert to cash within 12 months. | Q vs 1 year ago Q Growth |
| `AstCurGr%TTM` | Sum of all assets expected to convert to cash within 12 months. | Trailing Twelve Months Growth |
| `AstCurGr%PQTTM` | Sum of all assets expected to convert to cash within 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `AstCurGr%A` | Sum of all assets expected to convert to cash within 12 months. | Growth Annual |
| `AstCurGr%3Y` | Sum of all assets expected to convert to cash within 12 months. | Three Year Annualized Growth |
| `AstCurGr%5Y` | Sum of all assets expected to convert to cash within 12 months. | Five Year Annualized Growth |
| `AstCurGr%10Y` | Sum of all assets expected to convert to cash within 12 months. | Ten Year Annualized Growth |
| `AstCurRSD%ANN` | Sum of all assets expected to convert to cash within 12 months. | Ten Year Relative Standard Deviation |
| `AstCurRSD%TTM` | Sum of all assets expected to convert to cash within 12 months. | Five Year Relative Standard Deviation |
| `AstCurRegEstANN` | Sum of all assets expected to convert to cash within 12 months. | Ten Year Regression Estimate |
| `AstCurRegEstTTM` | Sum of all assets expected to convert to cash within 12 months. | Five Year Regression Estimate |
| `AstCurRegGr%ANN` | Sum of all assets expected to convert to cash within 12 months. | Ten Year Regression Estimate |
| `AstCurRegGr%TTM` | Sum of all assets expected to convert to cash within 12 months. | Five Year Regression Growth |
| `AstCurPSQ` | Sum of all assets expected to convert to cash within 12 months. | Quarterly Per Share |
| `AstCurPSA` | Sum of all assets expected to convert to cash within 12 months. | Annual Per Share |
| `AstCur%AssetsQ` | Sum of all assets expected to convert to cash within 12 months. | % of Quarterly Assets |
| `AstCur%AssetsA` | Sum of all assets expected to convert to cash within 12 months. | % of Annual Assets |
| `AstCur3YAvg` | Sum of all assets expected to convert to cash within 12 months. | Three Year Average |
| `AstCur5YAvg` | Sum of all assets expected to convert to cash within 12 months. | Five Year Average |

#### `Inventory(offset, type[, NAHandling])`
```p123
Inventory(offset, type[, NAHandling])
```

Inventory is a current asset, representing merchandise or other material held for sale or intended to generate revenue.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InventoryQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Latest Quarter |
| `InventoryPQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Previous Quarter |
| `InventoryPYQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Previous Quarter 1 Year Ago |
| `InventoryTTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Trailing 12 Months |
| `InventoryPTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Previous Trailing 12 Months |
| `InventoryA` | Current asset representing merchandise or materials held for sale or revenue generation. | Latest Year |
| `InventoryPY` | Current asset representing merchandise or materials held for sale or revenue generation. | Previous Year |
| `InventoryGr%PQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Q vs Previous Q Growth |
| `InventoryGr%PYQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Q vs 1 year ago Q Growth |
| `InventoryGr%TTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Trailing Twelve Months Growth |
| `InventoryGr%PQTTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Trailing Twelve Months Growth 1Q Ago |
| `InventoryGr%A` | Current asset representing merchandise or materials held for sale or revenue generation. | Growth Annual |
| `InventoryGr%3Y` | Current asset representing merchandise or materials held for sale or revenue generation. | Three Year Annualized Growth |
| `InventoryGr%5Y` | Current asset representing merchandise or materials held for sale or revenue generation. | Five Year Annualized Growth |
| `InventoryGr%10Y` | Current asset representing merchandise or materials held for sale or revenue generation. | Ten Year Annualized Growth |
| `InventoryRSD%ANN` | Current asset representing merchandise or materials held for sale or revenue generation. | Ten Year Relative Standard Deviation |
| `InventoryRSD%TTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Five Year Relative Standard Deviation |
| `InventoryRegEstANN` | Current asset representing merchandise or materials held for sale or revenue generation. | Ten Year Regression Estimate |
| `InventoryRegEstTTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Five Year Regression Estimate |
| `InventoryRegGr%ANN` | Current asset representing merchandise or materials held for sale or revenue generation. | Ten Year Regression Estimate |
| `InventoryRegGr%TTM` | Current asset representing merchandise or materials held for sale or revenue generation. | Five Year Regression Growth |
| `InventoryPSQ` | Current asset representing merchandise or materials held for sale or revenue generation. | Quarterly Per Share |
| `InventoryPSA` | Current asset representing merchandise or materials held for sale or revenue generation. | Annual Per Share |
| `Inventory%AssetsQ` | Current asset representing merchandise or materials held for sale or revenue generation. | % of Quarterly Assets |
| `Inventory%AssetsA` | Current asset representing merchandise or materials held for sale or revenue generation. | % of Annual Assets |
| `Inventory3YAvg` | Current asset representing merchandise or materials held for sale or revenue generation. | Three Year Average |
| `Inventory5YAvg` | Current asset representing merchandise or materials held for sale or revenue generation. | Five Year Average |

#### `InvstST(offset, type[, NAHandling])`
```p123
InvstST(offset, type[, NAHandling])
```

Short-Term Investments is a current asset. It represents currently-marketable securities that either come due or are expected to be traded within 12 months of the date of the balance sheet.

Given the liquidity of the investments represented in this line, it is usually treated as cash for all but the most conservative analysis. It is already included in Total Cash and Equivalents.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InvstSTQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Latest Quarter |
| `InvstSTPQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Previous Quarter |
| `InvstSTPYQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Previous Quarter 1 Year Ago |
| `InvstSTTTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Trailing 12 Months |
| `InvstSTPTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Previous Trailing 12 Months |
| `InvstSTA` | Current asset representing marketable securities due or expected to be traded within 12 months. | Latest Year |
| `InvstSTPY` | Current asset representing marketable securities due or expected to be traded within 12 months. | Previous Year |
| `InvstSTGr%PQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Q vs Previous Q Growth |
| `InvstSTGr%PYQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Q vs 1 year ago Q Growth |
| `InvstSTGr%TTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Trailing Twelve Months Growth |
| `InvstSTGr%PQTTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `InvstSTGr%A` | Current asset representing marketable securities due or expected to be traded within 12 months. | Growth Annual |
| `InvstSTGr%3Y` | Current asset representing marketable securities due or expected to be traded within 12 months. | Three Year Annualized Growth |
| `InvstSTGr%5Y` | Current asset representing marketable securities due or expected to be traded within 12 months. | Five Year Annualized Growth |
| `InvstSTGr%10Y` | Current asset representing marketable securities due or expected to be traded within 12 months. | Ten Year Annualized Growth |
| `InvstSTRSD%ANN` | Current asset representing marketable securities due or expected to be traded within 12 months. | Ten Year Relative Standard Deviation |
| `InvstSTRSD%TTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Five Year Relative Standard Deviation |
| `InvstSTRegEstANN` | Current asset representing marketable securities due or expected to be traded within 12 months. | Ten Year Regression Estimate |
| `InvstSTRegEstTTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Five Year Regression Estimate |
| `InvstSTRegGr%ANN` | Current asset representing marketable securities due or expected to be traded within 12 months. | Ten Year Regression Estimate |
| `InvstSTRegGr%TTM` | Current asset representing marketable securities due or expected to be traded within 12 months. | Five Year Regression Growth |
| `InvstSTPSQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | Quarterly Per Share |
| `InvstSTPSA` | Current asset representing marketable securities due or expected to be traded within 12 months. | Annual Per Share |
| `InvstST%AssetsQ` | Current asset representing marketable securities due or expected to be traded within 12 months. | % of Quarterly Assets |
| `InvstST%AssetsA` | Current asset representing marketable securities due or expected to be traded within 12 months. | % of Annual Assets |
| `InvstST3YAvg` | Current asset representing marketable securities due or expected to be traded within 12 months. | Three Year Average |
| `InvstST5YAvg` | Current asset representing marketable securities due or expected to be traded within 12 months. | Five Year Average |

#### `WorkCap(offset, type[, NAHandling])`
```p123
WorkCap(offset, type[, NAHandling])
```

Working Capital is the amount that a company could reap by immediately settling its current accounts.

Working capital is current assets less current liabilities. For most companies, this is a positive number. A significantly negative number could indicate either rising debt levels or cash flow problems in the future.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `WorkCapQ` | Current assets less current liabilities. | Latest Quarter |
| `WorkCapPQ` | Current assets less current liabilities. | Previous Quarter |
| `WorkCapPYQ` | Current assets less current liabilities. | Previous Quarter 1 Year Ago |
| `WorkCapTTM` | Current assets less current liabilities. | Trailing 12 Months |
| `WorkCapPTM` | Current assets less current liabilities. | Previous Trailing 12 Months |
| `WorkCapA` | Current assets less current liabilities. | Latest Year |
| `WorkCapPY` | Current assets less current liabilities. | Previous Year |
| `WorkCapGr%PQ` | Current assets less current liabilities. | Q vs Previous Q Growth |
| `WorkCapGr%PYQ` | Current assets less current liabilities. | Q vs 1 year ago Q Growth |
| `WorkCapGr%TTM` | Current assets less current liabilities. | Trailing Twelve Months Growth |
| `WorkCapGr%PQTTM` | Current assets less current liabilities. | Trailing Twelve Months Growth 1Q Ago |
| `WorkCapGr%A` | Current assets less current liabilities. | Growth Annual |
| `WorkCapGr%3Y` | Current assets less current liabilities. | Three Year Annualized Growth |
| `WorkCapGr%5Y` | Current assets less current liabilities. | Five Year Annualized Growth |
| `WorkCapGr%10Y` | Current assets less current liabilities. | Ten Year Annualized Growth |
| `WorkCapRSD%ANN` | Current assets less current liabilities. | Ten Year Relative Standard Deviation |
| `WorkCapRSD%TTM` | Current assets less current liabilities. | Five Year Relative Standard Deviation |
| `WorkCapRegEstANN` | Current assets less current liabilities. | Ten Year Regression Estimate |
| `WorkCapRegEstTTM` | Current assets less current liabilities. | Five Year Regression Estimate |
| `WorkCapRegGr%ANN` | Current assets less current liabilities. | Ten Year Regression Estimate |
| `WorkCapRegGr%TTM` | Current assets less current liabilities. | Five Year Regression Growth |
| `WorkCapPSQ` | Current assets less current liabilities. | Quarterly Per Share |
| `WorkCapPSA` | Current assets less current liabilities. | Annual Per Share |
| `WorkCap%AssetsQ` | Current assets less current liabilities. | % of Quarterly Assets |
| `WorkCap%AssetsA` | Current assets less current liabilities. | % of Annual Assets |
| `WorkCap3YAvg` | Current assets less current liabilities. | Three Year Average |
| `WorkCap5YAvg` | Current assets less current liabilities. | Five Year Average |

### Assets-Noncurrent

#### `AccumDep(offset, type[, NAHandling])`
```p123
AccumDep(offset, type[, NAHandling])
```

Accumulated Depreciation is the total depreciation already recognized on the gross property, plant and equipment (GrossPlant).

Note that NetPlant has already had AccumDep factored into it.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AccumDepQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Latest Quarter |
| `AccumDepPQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Previous Quarter |
| `AccumDepPYQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Previous Quarter 1 Year Ago |
| `AccumDepTTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Trailing 12 Months |
| `AccumDepPTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Previous Trailing 12 Months |
| `AccumDepA` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Latest Year |
| `AccumDepPY` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Previous Year |
| `AccumDepGr%PQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Q vs Previous Q Growth |
| `AccumDepGr%PYQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Q vs 1 year ago Q Growth |
| `AccumDepGr%TTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Trailing Twelve Months Growth |
| `AccumDepGr%PQTTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Trailing Twelve Months Growth 1Q Ago |
| `AccumDepGr%A` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Growth Annual |
| `AccumDepGr%3Y` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Three Year Annualized Growth |
| `AccumDepGr%5Y` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Five Year Annualized Growth |
| `AccumDepGr%10Y` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Ten Year Annualized Growth |
| `AccumDepRSD%ANN` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Ten Year Relative Standard Deviation |
| `AccumDepRSD%TTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Five Year Relative Standard Deviation |
| `AccumDepRegEstANN` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Ten Year Regression Estimate |
| `AccumDepRegEstTTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Five Year Regression Estimate |
| `AccumDepRegGr%ANN` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Ten Year Regression Estimate |
| `AccumDepRegGr%TTM` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Five Year Regression Growth |
| `AccumDepPSQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Quarterly Per Share |
| `AccumDepPSA` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Annual Per Share |
| `AccumDep%AssetsQ` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | % of Quarterly Assets |
| `AccumDep%AssetsA` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | % of Annual Assets |
| `AccumDep3YAvg` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Three Year Average |
| `AccumDep5YAvg` | Total depreciation recognized on gross property, plant and equipment (GrossPlant). | Five Year Average |

#### `InvstEq(offset, type[, NAHandling])`
```p123
InvstEq(offset, type[, NAHandling])
```

Represents the total investments and advances of the company as of the balance sheet date. Typically, long-term investments are traditional investments in equity, bonds, preferred securities and interest-bearing deposits.

The company intends to hold these investments for more than a year as opposed to short-term investments which are expected to be sold within a year for liquidity purposes.

It includes affiliate companies as well as other long-term investments.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InvstEqQ` | Long-term equity investments. | Latest Quarter |
| `InvstEqPQ` | Long-term equity investments. | Previous Quarter |
| `InvstEqPYQ` | Long-term equity investments. | Previous Quarter 1 Year Ago |
| `InvstEqTTM` | Long-term equity investments. | Trailing 12 Months |
| `InvstEqPTM` | Long-term equity investments. | Previous Trailing 12 Months |
| `InvstEqA` | Long-term equity investments. | Latest Year |
| `InvstEqPY` | Long-term equity investments. | Previous Year |
| `InvstEqGr%PQ` | Long-term equity investments. | Q vs Previous Q Growth |
| `InvstEqGr%PYQ` | Long-term equity investments. | Q vs 1 year ago Q Growth |
| `InvstEqGr%TTM` | Long-term equity investments. | Trailing Twelve Months Growth |
| `InvstEqGr%PQTTM` | Long-term equity investments. | Trailing Twelve Months Growth 1Q Ago |
| `InvstEqGr%A` | Long-term equity investments. | Growth Annual |
| `InvstEqGr%3Y` | Long-term equity investments. | Three Year Annualized Growth |
| `InvstEqGr%5Y` | Long-term equity investments. | Five Year Annualized Growth |
| `InvstEqGr%10Y` | Long-term equity investments. | Ten Year Annualized Growth |
| `InvstEqRSD%ANN` | Long-term equity investments. | Ten Year Relative Standard Deviation |
| `InvstEqRSD%TTM` | Long-term equity investments. | Five Year Relative Standard Deviation |
| `InvstEqRegEstANN` | Long-term equity investments. | Ten Year Regression Estimate |
| `InvstEqRegEstTTM` | Long-term equity investments. | Five Year Regression Estimate |
| `InvstEqRegGr%ANN` | Long-term equity investments. | Ten Year Regression Estimate |
| `InvstEqRegGr%TTM` | Long-term equity investments. | Five Year Regression Growth |
| `InvstEqPSQ` | Long-term equity investments. | Quarterly Per Share |
| `InvstEqPSA` | Long-term equity investments. | Annual Per Share |
| `InvstEq%AssetsQ` | Long-term equity investments. | % of Quarterly Assets |
| `InvstEq%AssetsA` | Long-term equity investments. | % of Annual Assets |
| `InvstEq3YAvg` | Long-term equity investments. | Three Year Average |
| `InvstEq5YAvg` | Long-term equity investments. | Five Year Average |

#### `Goodwill(offset, type[, NAHandling])`
```p123
Goodwill(offset, type[, NAHandling])
```

Goodwill is the excess cost compared to equity in an acquisition. It is retained as an intangible asset on the balance sheet and is amortized over time.

Note that this is already included in the intangible assets line item.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `GoodwillQ` | Excess cost over equity in acquisitions. | Latest Quarter |
| `GoodwillPQ` | Excess cost over equity in acquisitions. | Previous Quarter |
| `GoodwillPYQ` | Excess cost over equity in acquisitions. | Previous Quarter 1 Year Ago |
| `GoodwillTTM` | Excess cost over equity in acquisitions. | Trailing 12 Months |
| `GoodwillPTM` | Excess cost over equity in acquisitions. | Previous Trailing 12 Months |
| `GoodwillA` | Excess cost over equity in acquisitions. | Latest Year |
| `GoodwillPY` | Excess cost over equity in acquisitions. | Previous Year |
| `GoodwillGr%PQ` | Excess cost over equity in acquisitions. | Q vs Previous Q Growth |
| `GoodwillGr%PYQ` | Excess cost over equity in acquisitions. | Q vs 1 year ago Q Growth |
| `GoodwillGr%TTM` | Excess cost over equity in acquisitions. | Trailing Twelve Months Growth |
| `GoodwillGr%PQTTM` | Excess cost over equity in acquisitions. | Trailing Twelve Months Growth 1Q Ago |
| `GoodwillGr%A` | Excess cost over equity in acquisitions. | Growth Annual |
| `GoodwillGr%3Y` | Excess cost over equity in acquisitions. | Three Year Annualized Growth |
| `GoodwillGr%5Y` | Excess cost over equity in acquisitions. | Five Year Annualized Growth |
| `GoodwillGr%10Y` | Excess cost over equity in acquisitions. | Ten Year Annualized Growth |
| `GoodwillRSD%ANN` | Excess cost over equity in acquisitions. | Ten Year Relative Standard Deviation |
| `GoodwillRSD%TTM` | Excess cost over equity in acquisitions. | Five Year Relative Standard Deviation |
| `GoodwillRegEstANN` | Excess cost over equity in acquisitions. | Ten Year Regression Estimate |
| `GoodwillRegEstTTM` | Excess cost over equity in acquisitions. | Five Year Regression Estimate |
| `GoodwillRegGr%ANN` | Excess cost over equity in acquisitions. | Ten Year Regression Estimate |
| `GoodwillRegGr%TTM` | Excess cost over equity in acquisitions. | Five Year Regression Growth |
| `GoodwillPSQ` | Excess cost over equity in acquisitions. | Quarterly Per Share |
| `GoodwillPSA` | Excess cost over equity in acquisitions. | Annual Per Share |
| `Goodwill%AssetsQ` | Excess cost over equity in acquisitions. | % of Quarterly Assets |
| `Goodwill%AssetsA` | Excess cost over equity in acquisitions. | % of Annual Assets |
| `Goodwill3YAvg` | Excess cost over equity in acquisitions. | Three Year Average |
| `Goodwill5YAvg` | Excess cost over equity in acquisitions. | Five Year Average |

#### `GrossPlant(offset, type[, NAHandling])`
```p123
GrossPlant(offset, type[, NAHandling])
```

Gross Plant Property and Equipment is the total amount of physical assets owned by a company unadjusted by depreciation.

Property plant and equipment adjusted for depreciation can be found in the separate Net Plant data item.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `GrossPlantQ` | Total value of physical assets owned before depreciation adjustments. | Latest Quarter |
| `GrossPlantPQ` | Total value of physical assets owned before depreciation adjustments. | Previous Quarter |
| `GrossPlantPYQ` | Total value of physical assets owned before depreciation adjustments. | Previous Quarter 1 Year Ago |
| `GrossPlantTTM` | Total value of physical assets owned before depreciation adjustments. | Trailing 12 Months |
| `GrossPlantPTM` | Total value of physical assets owned before depreciation adjustments. | Previous Trailing 12 Months |
| `GrossPlantA` | Total value of physical assets owned before depreciation adjustments. | Latest Year |
| `GrossPlantPY` | Total value of physical assets owned before depreciation adjustments. | Previous Year |
| `GrossPlantGr%PQ` | Total value of physical assets owned before depreciation adjustments. | Q vs Previous Q Growth |
| `GrossPlantGr%PYQ` | Total value of physical assets owned before depreciation adjustments. | Q vs 1 year ago Q Growth |
| `GrossPlantGr%TTM` | Total value of physical assets owned before depreciation adjustments. | Trailing Twelve Months Growth |
| `GrossPlantGr%PQTTM` | Total value of physical assets owned before depreciation adjustments. | Trailing Twelve Months Growth 1Q Ago |
| `GrossPlantGr%A` | Total value of physical assets owned before depreciation adjustments. | Growth Annual |
| `GrossPlantGr%3Y` | Total value of physical assets owned before depreciation adjustments. | Three Year Annualized Growth |
| `GrossPlantGr%5Y` | Total value of physical assets owned before depreciation adjustments. | Five Year Annualized Growth |
| `GrossPlantGr%10Y` | Total value of physical assets owned before depreciation adjustments. | Ten Year Annualized Growth |
| `GrossPlantRSD%ANN` | Total value of physical assets owned before depreciation adjustments. | Ten Year Relative Standard Deviation |
| `GrossPlantRSD%TTM` | Total value of physical assets owned before depreciation adjustments. | Five Year Relative Standard Deviation |
| `GrossPlantRegEstANN` | Total value of physical assets owned before depreciation adjustments. | Ten Year Regression Estimate |
| `GrossPlantRegEstTTM` | Total value of physical assets owned before depreciation adjustments. | Five Year Regression Estimate |
| `GrossPlantRegGr%ANN` | Total value of physical assets owned before depreciation adjustments. | Ten Year Regression Estimate |
| `GrossPlantRegGr%TTM` | Total value of physical assets owned before depreciation adjustments. | Five Year Regression Growth |
| `GrossPlantPSQ` | Total value of physical assets owned before depreciation adjustments. | Quarterly Per Share |
| `GrossPlantPSA` | Total value of physical assets owned before depreciation adjustments. | Annual Per Share |
| `GrossPlant%AssetsQ` | Total value of physical assets owned before depreciation adjustments. | % of Quarterly Assets |
| `GrossPlant%AssetsA` | Total value of physical assets owned before depreciation adjustments. | % of Annual Assets |
| `GrossPlant3YAvg` | Total value of physical assets owned before depreciation adjustments. | Three Year Average |
| `GrossPlant5YAvg` | Total value of physical assets owned before depreciation adjustments. | Five Year Average |

#### `AstIntan(offset, type[, NAHandling])`
```p123
AstIntan(offset, type[, NAHandling])
```

Intangible assets is the sum of assets that are not included in the tangible assets of property, plant and equipment.

This line is dominated by Goodwill for most companies. It also includes such intangibles as patents, trademarks, leases where the company is the lesee, distribution rights and franchise fees.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AstIntanQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Latest Quarter |
| `AstIntanPQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Previous Quarter |
| `AstIntanPYQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Previous Quarter 1 Year Ago |
| `AstIntanTTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Trailing 12 Months |
| `AstIntanPTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Previous Trailing 12 Months |
| `AstIntanA` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Latest Year |
| `AstIntanPY` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Previous Year |
| `AstIntanGr%PQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Q vs Previous Q Growth |
| `AstIntanGr%PYQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Q vs 1 year ago Q Growth |
| `AstIntanGr%TTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Trailing Twelve Months Growth |
| `AstIntanGr%PQTTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Trailing Twelve Months Growth 1Q Ago |
| `AstIntanGr%A` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Growth Annual |
| `AstIntanGr%3Y` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Three Year Annualized Growth |
| `AstIntanGr%5Y` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Five Year Annualized Growth |
| `AstIntanGr%10Y` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Ten Year Annualized Growth |
| `AstIntanRSD%ANN` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Ten Year Relative Standard Deviation |
| `AstIntanRSD%TTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Five Year Relative Standard Deviation |
| `AstIntanRegEstANN` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Ten Year Regression Estimate |
| `AstIntanRegEstTTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Five Year Regression Estimate |
| `AstIntanRegGr%ANN` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Ten Year Regression Estimate |
| `AstIntanRegGr%TTM` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Five Year Regression Growth |
| `AstIntanPSQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Quarterly Per Share |
| `AstIntanPSA` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Annual Per Share |
| `AstIntan%AssetsQ` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | % of Quarterly Assets |
| `AstIntan%AssetsA` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | % of Annual Assets |
| `AstIntan3YAvg` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Three Year Average |
| `AstIntan5YAvg` | Sum of assets that are not included in the tangible assets of property, plant and equipment. | Five Year Average |

#### `InvstAdvOther(offset, type[, NAHandling])`
```p123
InvstAdvOther(offset, type[, NAHandling])
```

Other Investments and Advances represents long-term receivables, including investments in unconsolidated companies.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InvstAdvOtherQ` | Long-term receivables including investments in unconsolidated companies. | Latest Quarter |
| `InvstAdvOtherPQ` | Long-term receivables including investments in unconsolidated companies. | Previous Quarter |
| `InvstAdvOtherPYQ` | Long-term receivables including investments in unconsolidated companies. | Previous Quarter 1 Year Ago |
| `InvstAdvOtherTTM` | Long-term receivables including investments in unconsolidated companies. | Trailing 12 Months |
| `InvstAdvOtherPTM` | Long-term receivables including investments in unconsolidated companies. | Previous Trailing 12 Months |
| `InvstAdvOtherA` | Long-term receivables including investments in unconsolidated companies. | Latest Year |
| `InvstAdvOtherPY` | Long-term receivables including investments in unconsolidated companies. | Previous Year |
| `InvstAdvOtherGr%PQ` | Long-term receivables including investments in unconsolidated companies. | Q vs Previous Q Growth |
| `InvstAdvOtherGr%PYQ` | Long-term receivables including investments in unconsolidated companies. | Q vs 1 year ago Q Growth |
| `InvstAdvOtherGr%TTM` | Long-term receivables including investments in unconsolidated companies. | Trailing Twelve Months Growth |
| `InvstAdvOtherGr%PQTTM` | Long-term receivables including investments in unconsolidated companies. | Trailing Twelve Months Growth 1Q Ago |
| `InvstAdvOtherGr%A` | Long-term receivables including investments in unconsolidated companies. | Growth Annual |
| `InvstAdvOtherGr%3Y` | Long-term receivables including investments in unconsolidated companies. | Three Year Annualized Growth |
| `InvstAdvOtherGr%5Y` | Long-term receivables including investments in unconsolidated companies. | Five Year Annualized Growth |
| `InvstAdvOtherGr%10Y` | Long-term receivables including investments in unconsolidated companies. | Ten Year Annualized Growth |
| `InvstAdvOtherRSD%ANN` | Long-term receivables including investments in unconsolidated companies. | Ten Year Relative Standard Deviation |
| `InvstAdvOtherRSD%TTM` | Long-term receivables including investments in unconsolidated companies. | Five Year Relative Standard Deviation |
| `InvstAdvOtherRegEstANN` | Long-term receivables including investments in unconsolidated companies. | Ten Year Regression Estimate |
| `InvstAdvOtherRegEstTTM` | Long-term receivables including investments in unconsolidated companies. | Five Year Regression Estimate |
| `InvstAdvOtherRegGr%ANN` | Long-term receivables including investments in unconsolidated companies. | Ten Year Regression Estimate |
| `InvstAdvOtherRegGr%TTM` | Long-term receivables including investments in unconsolidated companies. | Five Year Regression Growth |
| `InvstAdvOtherPSQ` | Long-term receivables including investments in unconsolidated companies. | Quarterly Per Share |
| `InvstAdvOtherPSA` | Long-term receivables including investments in unconsolidated companies. | Annual Per Share |
| `InvstAdvOther%AssetsQ` | Long-term receivables including investments in unconsolidated companies. | % of Quarterly Assets |
| `InvstAdvOther%AssetsA` | Long-term receivables including investments in unconsolidated companies. | % of Annual Assets |
| `InvstAdvOther3YAvg` | Long-term receivables including investments in unconsolidated companies. | Three Year Average |
| `InvstAdvOther5YAvg` | Long-term receivables including investments in unconsolidated companies. | Five Year Average |

#### `NetPlant(offset, type[, NAHandling])`
```p123
NetPlant(offset, type[, NAHandling])
```

Net Property Plant and Equipment is the total of the company's physical assets (not including raw materials or items for sale, which are included in inventory) less accumulated depreciation.

Gross plant and accumulated depreciation are both available as separate data items for those who wish to use them.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetPlantQ` | Total physical assets minus accumulated depreciation. | Latest Quarter |
| `NetPlantPQ` | Total physical assets minus accumulated depreciation. | Previous Quarter |
| `NetPlantPYQ` | Total physical assets minus accumulated depreciation. | Previous Quarter 1 Year Ago |
| `NetPlantTTM` | Total physical assets minus accumulated depreciation. | Trailing 12 Months |
| `NetPlantPTM` | Total physical assets minus accumulated depreciation. | Previous Trailing 12 Months |
| `NetPlantA` | Total physical assets minus accumulated depreciation. | Latest Year |
| `NetPlantPY` | Total physical assets minus accumulated depreciation. | Previous Year |
| `NetPlantGr%PQ` | Total physical assets minus accumulated depreciation. | Q vs Previous Q Growth |
| `NetPlantGr%PYQ` | Total physical assets minus accumulated depreciation. | Q vs 1 year ago Q Growth |
| `NetPlantGr%TTM` | Total physical assets minus accumulated depreciation. | Trailing Twelve Months Growth |
| `NetPlantGr%PQTTM` | Total physical assets minus accumulated depreciation. | Trailing Twelve Months Growth 1Q Ago |
| `NetPlantGr%A` | Total physical assets minus accumulated depreciation. | Growth Annual |
| `NetPlantGr%3Y` | Total physical assets minus accumulated depreciation. | Three Year Annualized Growth |
| `NetPlantGr%5Y` | Total physical assets minus accumulated depreciation. | Five Year Annualized Growth |
| `NetPlantGr%10Y` | Total physical assets minus accumulated depreciation. | Ten Year Annualized Growth |
| `NetPlantRSD%ANN` | Total physical assets minus accumulated depreciation. | Ten Year Relative Standard Deviation |
| `NetPlantRSD%TTM` | Total physical assets minus accumulated depreciation. | Five Year Relative Standard Deviation |
| `NetPlantRegEstANN` | Total physical assets minus accumulated depreciation. | Ten Year Regression Estimate |
| `NetPlantRegEstTTM` | Total physical assets minus accumulated depreciation. | Five Year Regression Estimate |
| `NetPlantRegGr%ANN` | Total physical assets minus accumulated depreciation. | Ten Year Regression Estimate |
| `NetPlantRegGr%TTM` | Total physical assets minus accumulated depreciation. | Five Year Regression Growth |
| `NetPlantPSQ` | Total physical assets minus accumulated depreciation. | Quarterly Per Share |
| `NetPlantPSA` | Total physical assets minus accumulated depreciation. | Annual Per Share |
| `NetPlant%AssetsQ` | Total physical assets minus accumulated depreciation. | % of Quarterly Assets |
| `NetPlant%AssetsA` | Total physical assets minus accumulated depreciation. | % of Annual Assets |
| `NetPlant3YAvg` | Total physical assets minus accumulated depreciation. | Three Year Average |
| `NetPlant5YAvg` | Total physical assets minus accumulated depreciation. | Five Year Average |

#### `AstNonCurOther(offset, type[, NAHandling])`
```p123
AstNonCurOther(offset, type[, NAHandling])
```

Other Non-Current Assets are assets that do not fit into either current assets or property plant and equipment.

CompuStat includes such factors as intangible assets, foreign exchange assets and reinsurance assets in addition to those assets explicitly reported on an "other" line as reported by the company.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AstNonCurOtherQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Latest Quarter |
| `AstNonCurOtherPQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Previous Quarter |
| `AstNonCurOtherPYQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Previous Quarter 1 Year Ago |
| `AstNonCurOtherTTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Trailing 12 Months |
| `AstNonCurOtherPTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Previous Trailing 12 Months |
| `AstNonCurOtherA` | Value of assets that do not fit into either current assets or property plant and equipment. | Latest Year |
| `AstNonCurOtherPY` | Value of assets that do not fit into either current assets or property plant and equipment. | Previous Year |
| `AstNonCurOtherGr%PQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Q vs Previous Q Growth |
| `AstNonCurOtherGr%PYQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Q vs 1 year ago Q Growth |
| `AstNonCurOtherGr%TTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Trailing Twelve Months Growth |
| `AstNonCurOtherGr%PQTTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Trailing Twelve Months Growth 1Q Ago |
| `AstNonCurOtherGr%A` | Value of assets that do not fit into either current assets or property plant and equipment. | Growth Annual |
| `AstNonCurOtherGr%3Y` | Value of assets that do not fit into either current assets or property plant and equipment. | Three Year Annualized Growth |
| `AstNonCurOtherGr%5Y` | Value of assets that do not fit into either current assets or property plant and equipment. | Five Year Annualized Growth |
| `AstNonCurOtherGr%10Y` | Value of assets that do not fit into either current assets or property plant and equipment. | Ten Year Annualized Growth |
| `AstNonCurOtherRSD%ANN` | Value of assets that do not fit into either current assets or property plant and equipment. | Ten Year Relative Standard Deviation |
| `AstNonCurOtherRSD%TTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Five Year Relative Standard Deviation |
| `AstNonCurOtherRegEstANN` | Value of assets that do not fit into either current assets or property plant and equipment. | Ten Year Regression Estimate |
| `AstNonCurOtherRegEstTTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Five Year Regression Estimate |
| `AstNonCurOtherRegGr%ANN` | Value of assets that do not fit into either current assets or property plant and equipment. | Ten Year Regression Estimate |
| `AstNonCurOtherRegGr%TTM` | Value of assets that do not fit into either current assets or property plant and equipment. | Five Year Regression Growth |
| `AstNonCurOtherPSQ` | Value of assets that do not fit into either current assets or property plant and equipment. | Quarterly Per Share |
| `AstNonCurOtherPSA` | Value of assets that do not fit into either current assets or property plant and equipment. | Annual Per Share |
| `AstNonCurOther%AssetsQ` | Value of assets that do not fit into either current assets or property plant and equipment. | % of Quarterly Assets |
| `AstNonCurOther%AssetsA` | Value of assets that do not fit into either current assets or property plant and equipment. | % of Annual Assets |
| `AstNonCurOther3YAvg` | Value of assets that do not fit into either current assets or property plant and equipment. | Three Year Average |
| `AstNonCurOther5YAvg` | Value of assets that do not fit into either current assets or property plant and equipment. | Five Year Average |

#### `IntanOther(offset, type[, NAHandling])`
```p123
IntanOther(offset, type[, NAHandling])
```

Represents all assets that cannot be classified as current assets, long-term receivables, investments in unconsolidated subsidiaries, other investments, and property, plant and equipment. It includes deferred charges, intangible assets, and other tangible assets.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `IntanOtherQ` | All non-classifiable assets. | Latest Quarter |
| `IntanOtherPQ` | All non-classifiable assets. | Previous Quarter |
| `IntanOtherPYQ` | All non-classifiable assets. | Previous Quarter 1 Year Ago |
| `IntanOtherTTM` | All non-classifiable assets. | Trailing 12 Months |
| `IntanOtherPTM` | All non-classifiable assets. | Previous Trailing 12 Months |
| `IntanOtherA` | All non-classifiable assets. | Latest Year |
| `IntanOtherPY` | All non-classifiable assets. | Previous Year |
| `IntanOtherGr%PQ` | All non-classifiable assets. | Q vs Previous Q Growth |
| `IntanOtherGr%PYQ` | All non-classifiable assets. | Q vs 1 year ago Q Growth |
| `IntanOtherGr%TTM` | All non-classifiable assets. | Trailing Twelve Months Growth |
| `IntanOtherGr%PQTTM` | All non-classifiable assets. | Trailing Twelve Months Growth 1Q Ago |
| `IntanOtherGr%A` | All non-classifiable assets. | Growth Annual |
| `IntanOtherGr%3Y` | All non-classifiable assets. | Three Year Annualized Growth |
| `IntanOtherGr%5Y` | All non-classifiable assets. | Five Year Annualized Growth |
| `IntanOtherGr%10Y` | All non-classifiable assets. | Ten Year Annualized Growth |
| `IntanOtherRSD%ANN` | All non-classifiable assets. | Ten Year Relative Standard Deviation |
| `IntanOtherRSD%TTM` | All non-classifiable assets. | Five Year Relative Standard Deviation |
| `IntanOtherRegEstANN` | All non-classifiable assets. | Ten Year Regression Estimate |
| `IntanOtherRegEstTTM` | All non-classifiable assets. | Five Year Regression Estimate |
| `IntanOtherRegGr%ANN` | All non-classifiable assets. | Ten Year Regression Estimate |
| `IntanOtherRegGr%TTM` | All non-classifiable assets. | Five Year Regression Growth |
| `IntanOtherPSQ` | All non-classifiable assets. | Quarterly Per Share |
| `IntanOtherPSA` | All non-classifiable assets. | Annual Per Share |
| `IntanOther%AssetsQ` | All non-classifiable assets. | % of Quarterly Assets |
| `IntanOther%AssetsA` | All non-classifiable assets. | % of Annual Assets |
| `IntanOther3YAvg` | All non-classifiable assets. | Three Year Average |
| `IntanOther5YAvg` | All non-classifiable assets. | Five Year Average |

#### `AstTot(offset, type[, NAHandling])`
```p123
AstTot(offset, type[, NAHandling])
```

Total Assets is the total value of assets as reported on the balance sheet.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AstTotQ` | Total value of assets as reported on the balance sheet. | Latest Quarter |
| `AstTotPQ` | Total value of assets as reported on the balance sheet. | Previous Quarter |
| `AstTotPYQ` | Total value of assets as reported on the balance sheet. | Previous Quarter 1 Year Ago |
| `AstTotTTM` | Total value of assets as reported on the balance sheet. | Trailing 12 Months |
| `AstTotPTM` | Total value of assets as reported on the balance sheet. | Previous Trailing 12 Months |
| `AstTotA` | Total value of assets as reported on the balance sheet. | Latest Year |
| `AstTotPY` | Total value of assets as reported on the balance sheet. | Previous Year |
| `AstTotGr%PQ` | Total value of assets as reported on the balance sheet. | Q vs Previous Q Growth |
| `AstTotGr%PYQ` | Total value of assets as reported on the balance sheet. | Q vs 1 year ago Q Growth |
| `AstTotGr%TTM` | Total value of assets as reported on the balance sheet. | Trailing Twelve Months Growth |
| `AstTotGr%PQTTM` | Total value of assets as reported on the balance sheet. | Trailing Twelve Months Growth 1Q Ago |
| `AstTotGr%A` | Total value of assets as reported on the balance sheet. | Growth Annual |
| `AstTotGr%3Y` | Total value of assets as reported on the balance sheet. | Three Year Annualized Growth |
| `AstTotGr%5Y` | Total value of assets as reported on the balance sheet. | Five Year Annualized Growth |
| `AstTotGr%10Y` | Total value of assets as reported on the balance sheet. | Ten Year Annualized Growth |
| `AstTotRSD%ANN` | Total value of assets as reported on the balance sheet. | Ten Year Relative Standard Deviation |
| `AstTotRSD%TTM` | Total value of assets as reported on the balance sheet. | Five Year Relative Standard Deviation |
| `AstTotRegEstANN` | Total value of assets as reported on the balance sheet. | Ten Year Regression Estimate |
| `AstTotRegEstTTM` | Total value of assets as reported on the balance sheet. | Five Year Regression Estimate |
| `AstTotRegGr%ANN` | Total value of assets as reported on the balance sheet. | Ten Year Regression Estimate |
| `AstTotRegGr%TTM` | Total value of assets as reported on the balance sheet. | Five Year Regression Growth |
| `AstTotPSQ` | Total value of assets as reported on the balance sheet. | Quarterly Per Share |
| `AstTotPSA` | Total value of assets as reported on the balance sheet. | Annual Per Share |
| `AstTot%AssetsQ` | Total value of assets as reported on the balance sheet. | % of Quarterly Assets |
| `AstTot%AssetsA` | Total value of assets as reported on the balance sheet. | % of Annual Assets |
| `AstTot3YAvg` | Total value of assets as reported on the balance sheet. | Three Year Average |
| `AstTot5YAvg` | Total value of assets as reported on the balance sheet. | Five Year Average |

### Liabilities-Current

#### `Payables(offset, type[, NAHandling])`
```p123
Payables(offset, type[, NAHandling])
```

Accounts Payable is the current portion of money that is owed by the company.

Note that this is the current portion of owed money; this only encompasses funds due within the 12 months following the balance sheet date. Non-current accounts payable (a rarer situation by far) is aggregated within Other Non-current Liabilities.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `PayablesQ` | Money owed by the company due within 12 months. | Latest Quarter |
| `PayablesPQ` | Money owed by the company due within 12 months. | Previous Quarter |
| `PayablesPYQ` | Money owed by the company due within 12 months. | Previous Quarter 1 Year Ago |
| `PayablesTTM` | Money owed by the company due within 12 months. | Trailing 12 Months |
| `PayablesPTM` | Money owed by the company due within 12 months. | Previous Trailing 12 Months |
| `PayablesA` | Money owed by the company due within 12 months. | Latest Year |
| `PayablesPY` | Money owed by the company due within 12 months. | Previous Year |
| `PayablesGr%PQ` | Money owed by the company due within 12 months. | Q vs Previous Q Growth |
| `PayablesGr%PYQ` | Money owed by the company due within 12 months. | Q vs 1 year ago Q Growth |
| `PayablesGr%TTM` | Money owed by the company due within 12 months. | Trailing Twelve Months Growth |
| `PayablesGr%PQTTM` | Money owed by the company due within 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `PayablesGr%A` | Money owed by the company due within 12 months. | Growth Annual |
| `PayablesGr%3Y` | Money owed by the company due within 12 months. | Three Year Annualized Growth |
| `PayablesGr%5Y` | Money owed by the company due within 12 months. | Five Year Annualized Growth |
| `PayablesGr%10Y` | Money owed by the company due within 12 months. | Ten Year Annualized Growth |
| `PayablesRSD%ANN` | Money owed by the company due within 12 months. | Ten Year Relative Standard Deviation |
| `PayablesRSD%TTM` | Money owed by the company due within 12 months. | Five Year Relative Standard Deviation |
| `PayablesRegEstANN` | Money owed by the company due within 12 months. | Ten Year Regression Estimate |
| `PayablesRegEstTTM` | Money owed by the company due within 12 months. | Five Year Regression Estimate |
| `PayablesRegGr%ANN` | Money owed by the company due within 12 months. | Ten Year Regression Estimate |
| `PayablesRegGr%TTM` | Money owed by the company due within 12 months. | Five Year Regression Growth |
| `PayablesPSQ` | Money owed by the company due within 12 months. | Quarterly Per Share |
| `PayablesPSA` | Money owed by the company due within 12 months. | Annual Per Share |
| `Payables%AssetsQ` | Money owed by the company due within 12 months. | % of Quarterly Assets |
| `Payables%AssetsA` | Money owed by the company due within 12 months. | % of Annual Assets |
| `Payables3YAvg` | Money owed by the company due within 12 months. | Three Year Average |
| `Payables5YAvg` | Money owed by the company due within 12 months. | Five Year Average |

#### `LiabCurOther(offset, type[, NAHandling])`
```p123
LiabCurOther(offset, type[, NAHandling])
```

Other Current Liabilities is the total of all liabilities due within 12 months of the date of the balance sheet that are not debt, trade accounts or income taxes payable.

The lion's share of the line is usually accrued expenses.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `LiabCurOtherQ` | All non-debt, non-payables liabilities due within 12 months. | Latest Quarter |
| `LiabCurOtherPQ` | All non-debt, non-payables liabilities due within 12 months. | Previous Quarter |
| `LiabCurOtherPYQ` | All non-debt, non-payables liabilities due within 12 months. | Previous Quarter 1 Year Ago |
| `LiabCurOtherTTM` | All non-debt, non-payables liabilities due within 12 months. | Trailing 12 Months |
| `LiabCurOtherPTM` | All non-debt, non-payables liabilities due within 12 months. | Previous Trailing 12 Months |
| `LiabCurOtherA` | All non-debt, non-payables liabilities due within 12 months. | Latest Year |
| `LiabCurOtherPY` | All non-debt, non-payables liabilities due within 12 months. | Previous Year |
| `LiabCurOtherGr%PQ` | All non-debt, non-payables liabilities due within 12 months. | Q vs Previous Q Growth |
| `LiabCurOtherGr%PYQ` | All non-debt, non-payables liabilities due within 12 months. | Q vs 1 year ago Q Growth |
| `LiabCurOtherGr%TTM` | All non-debt, non-payables liabilities due within 12 months. | Trailing Twelve Months Growth |
| `LiabCurOtherGr%PQTTM` | All non-debt, non-payables liabilities due within 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `LiabCurOtherGr%A` | All non-debt, non-payables liabilities due within 12 months. | Growth Annual |
| `LiabCurOtherGr%3Y` | All non-debt, non-payables liabilities due within 12 months. | Three Year Annualized Growth |
| `LiabCurOtherGr%5Y` | All non-debt, non-payables liabilities due within 12 months. | Five Year Annualized Growth |
| `LiabCurOtherGr%10Y` | All non-debt, non-payables liabilities due within 12 months. | Ten Year Annualized Growth |
| `LiabCurOtherRSD%ANN` | All non-debt, non-payables liabilities due within 12 months. | Ten Year Relative Standard Deviation |
| `LiabCurOtherRSD%TTM` | All non-debt, non-payables liabilities due within 12 months. | Five Year Relative Standard Deviation |
| `LiabCurOtherRegEstANN` | All non-debt, non-payables liabilities due within 12 months. | Ten Year Regression Estimate |
| `LiabCurOtherRegEstTTM` | All non-debt, non-payables liabilities due within 12 months. | Five Year Regression Estimate |
| `LiabCurOtherRegGr%ANN` | All non-debt, non-payables liabilities due within 12 months. | Ten Year Regression Estimate |
| `LiabCurOtherRegGr%TTM` | All non-debt, non-payables liabilities due within 12 months. | Five Year Regression Growth |
| `LiabCurOtherPSQ` | All non-debt, non-payables liabilities due within 12 months. | Quarterly Per Share |
| `LiabCurOtherPSA` | All non-debt, non-payables liabilities due within 12 months. | Annual Per Share |
| `LiabCurOther%AssetsQ` | All non-debt, non-payables liabilities due within 12 months. | % of Quarterly Assets |
| `LiabCurOther%AssetsA` | All non-debt, non-payables liabilities due within 12 months. | % of Annual Assets |
| `LiabCurOther3YAvg` | All non-debt, non-payables liabilities due within 12 months. | Three Year Average |
| `LiabCurOther5YAvg` | All non-debt, non-payables liabilities due within 12 months. | Five Year Average |

#### `LiabCur(offset, type[, NAHandling])`
```p123
LiabCur(offset, type[, NAHandling])
```

Total Current Liabilities is the total amount of liabilities expected to be repaid within the 12 months after the date of the balance sheet.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `LiabCurQ` | Total liabilities due within 12 months of the balance sheet date. | Latest Quarter |
| `LiabCurPQ` | Total liabilities due within 12 months of the balance sheet date. | Previous Quarter |
| `LiabCurPYQ` | Total liabilities due within 12 months of the balance sheet date. | Previous Quarter 1 Year Ago |
| `LiabCurTTM` | Total liabilities due within 12 months of the balance sheet date. | Trailing 12 Months |
| `LiabCurPTM` | Total liabilities due within 12 months of the balance sheet date. | Previous Trailing 12 Months |
| `LiabCurA` | Total liabilities due within 12 months of the balance sheet date. | Latest Year |
| `LiabCurPY` | Total liabilities due within 12 months of the balance sheet date. | Previous Year |
| `LiabCurGr%PQ` | Total liabilities due within 12 months of the balance sheet date. | Q vs Previous Q Growth |
| `LiabCurGr%PYQ` | Total liabilities due within 12 months of the balance sheet date. | Q vs 1 year ago Q Growth |
| `LiabCurGr%TTM` | Total liabilities due within 12 months of the balance sheet date. | Trailing Twelve Months Growth |
| `LiabCurGr%PQTTM` | Total liabilities due within 12 months of the balance sheet date. | Trailing Twelve Months Growth 1Q Ago |
| `LiabCurGr%A` | Total liabilities due within 12 months of the balance sheet date. | Growth Annual |
| `LiabCurGr%3Y` | Total liabilities due within 12 months of the balance sheet date. | Three Year Annualized Growth |
| `LiabCurGr%5Y` | Total liabilities due within 12 months of the balance sheet date. | Five Year Annualized Growth |
| `LiabCurGr%10Y` | Total liabilities due within 12 months of the balance sheet date. | Ten Year Annualized Growth |
| `LiabCurRSD%ANN` | Total liabilities due within 12 months of the balance sheet date. | Ten Year Relative Standard Deviation |
| `LiabCurRSD%TTM` | Total liabilities due within 12 months of the balance sheet date. | Five Year Relative Standard Deviation |
| `LiabCurRegEstANN` | Total liabilities due within 12 months of the balance sheet date. | Ten Year Regression Estimate |
| `LiabCurRegEstTTM` | Total liabilities due within 12 months of the balance sheet date. | Five Year Regression Estimate |
| `LiabCurRegGr%ANN` | Total liabilities due within 12 months of the balance sheet date. | Ten Year Regression Estimate |
| `LiabCurRegGr%TTM` | Total liabilities due within 12 months of the balance sheet date. | Five Year Regression Growth |
| `LiabCurPSQ` | Total liabilities due within 12 months of the balance sheet date. | Quarterly Per Share |
| `LiabCurPSA` | Total liabilities due within 12 months of the balance sheet date. | Annual Per Share |
| `LiabCur%AssetsQ` | Total liabilities due within 12 months of the balance sheet date. | % of Quarterly Assets |
| `LiabCur%AssetsA` | Total liabilities due within 12 months of the balance sheet date. | % of Annual Assets |
| `LiabCur3YAvg` | Total liabilities due within 12 months of the balance sheet date. | Three Year Average |
| `LiabCur5YAvg` | Total liabilities due within 12 months of the balance sheet date. | Five Year Average |

#### `DbtST(offset, type[, NAHandling])`
```p123
DbtST(offset, type[, NAHandling])
```

Short-Term Debt is the portion of debt reported as a current liability in the latest balance sheet of the period specified by the type and offset inputs. Short-term debt is due within 12 months after the date of the balance sheet.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DbtSTQ` | Debt due within 12 months, reported as current liability on balance sheet. | Latest Quarter |
| `DbtSTPQ` | Debt due within 12 months, reported as current liability on balance sheet. | Previous Quarter |
| `DbtSTPYQ` | Debt due within 12 months, reported as current liability on balance sheet. | Previous Quarter 1 Year Ago |
| `DbtSTTTM` | Debt due within 12 months, reported as current liability on balance sheet. | Trailing 12 Months |
| `DbtSTPTM` | Debt due within 12 months, reported as current liability on balance sheet. | Previous Trailing 12 Months |
| `DbtSTA` | Debt due within 12 months, reported as current liability on balance sheet. | Latest Year |
| `DbtSTPY` | Debt due within 12 months, reported as current liability on balance sheet. | Previous Year |
| `DbtSTGr%PQ` | Debt due within 12 months, reported as current liability on balance sheet. | Q vs Previous Q Growth |
| `DbtSTGr%PYQ` | Debt due within 12 months, reported as current liability on balance sheet. | Q vs 1 year ago Q Growth |
| `DbtSTGr%TTM` | Debt due within 12 months, reported as current liability on balance sheet. | Trailing Twelve Months Growth |
| `DbtSTGr%PQTTM` | Debt due within 12 months, reported as current liability on balance sheet. | Trailing Twelve Months Growth 1Q Ago |
| `DbtSTGr%A` | Debt due within 12 months, reported as current liability on balance sheet. | Growth Annual |
| `DbtSTGr%3Y` | Debt due within 12 months, reported as current liability on balance sheet. | Three Year Annualized Growth |
| `DbtSTGr%5Y` | Debt due within 12 months, reported as current liability on balance sheet. | Five Year Annualized Growth |
| `DbtSTGr%10Y` | Debt due within 12 months, reported as current liability on balance sheet. | Ten Year Annualized Growth |
| `DbtSTRSD%ANN` | Debt due within 12 months, reported as current liability on balance sheet. | Ten Year Relative Standard Deviation |
| `DbtSTRSD%TTM` | Debt due within 12 months, reported as current liability on balance sheet. | Five Year Relative Standard Deviation |
| `DbtSTRegEstANN` | Debt due within 12 months, reported as current liability on balance sheet. | Ten Year Regression Estimate |
| `DbtSTRegEstTTM` | Debt due within 12 months, reported as current liability on balance sheet. | Five Year Regression Estimate |
| `DbtSTRegGr%ANN` | Debt due within 12 months, reported as current liability on balance sheet. | Ten Year Regression Estimate |
| `DbtSTRegGr%TTM` | Debt due within 12 months, reported as current liability on balance sheet. | Five Year Regression Growth |
| `DbtSTPSQ` | Debt due within 12 months, reported as current liability on balance sheet. | Quarterly Per Share |
| `DbtSTPSA` | Debt due within 12 months, reported as current liability on balance sheet. | Annual Per Share |
| `DbtST%AssetsQ` | Debt due within 12 months, reported as current liability on balance sheet. | % of Quarterly Assets |
| `DbtST%AssetsA` | Debt due within 12 months, reported as current liability on balance sheet. | % of Annual Assets |
| `DbtST3YAvg` | Debt due within 12 months, reported as current liability on balance sheet. | Three Year Average |
| `DbtST5YAvg` | Debt due within 12 months, reported as current liability on balance sheet. | Five Year Average |

#### `TxPayable(offset, type[, NAHandling])`
```p123
TxPayable(offset, type[, NAHandling])
```

Tax Payable is a current liability reflecting taxes owed within the next 12 months following the date of the balance sheet.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TxPayableQ` | Current liability for taxes owed within 12 months of balance sheet date. | Latest Quarter |
| `TxPayablePQ` | Current liability for taxes owed within 12 months of balance sheet date. | Previous Quarter |
| `TxPayablePYQ` | Current liability for taxes owed within 12 months of balance sheet date. | Previous Quarter 1 Year Ago |
| `TxPayableTTM` | Current liability for taxes owed within 12 months of balance sheet date. | Trailing 12 Months |
| `TxPayablePTM` | Current liability for taxes owed within 12 months of balance sheet date. | Previous Trailing 12 Months |
| `TxPayableA` | Current liability for taxes owed within 12 months of balance sheet date. | Latest Year |
| `TxPayablePY` | Current liability for taxes owed within 12 months of balance sheet date. | Previous Year |
| `TxPayableGr%PQ` | Current liability for taxes owed within 12 months of balance sheet date. | Q vs Previous Q Growth |
| `TxPayableGr%PYQ` | Current liability for taxes owed within 12 months of balance sheet date. | Q vs 1 year ago Q Growth |
| `TxPayableGr%TTM` | Current liability for taxes owed within 12 months of balance sheet date. | Trailing Twelve Months Growth |
| `TxPayableGr%PQTTM` | Current liability for taxes owed within 12 months of balance sheet date. | Trailing Twelve Months Growth 1Q Ago |
| `TxPayableGr%A` | Current liability for taxes owed within 12 months of balance sheet date. | Growth Annual |
| `TxPayableGr%3Y` | Current liability for taxes owed within 12 months of balance sheet date. | Three Year Annualized Growth |
| `TxPayableGr%5Y` | Current liability for taxes owed within 12 months of balance sheet date. | Five Year Annualized Growth |
| `TxPayableGr%10Y` | Current liability for taxes owed within 12 months of balance sheet date. | Ten Year Annualized Growth |
| `TxPayableRSD%ANN` | Current liability for taxes owed within 12 months of balance sheet date. | Ten Year Relative Standard Deviation |
| `TxPayableRSD%TTM` | Current liability for taxes owed within 12 months of balance sheet date. | Five Year Relative Standard Deviation |
| `TxPayableRegEstANN` | Current liability for taxes owed within 12 months of balance sheet date. | Ten Year Regression Estimate |
| `TxPayableRegEstTTM` | Current liability for taxes owed within 12 months of balance sheet date. | Five Year Regression Estimate |
| `TxPayableRegGr%ANN` | Current liability for taxes owed within 12 months of balance sheet date. | Ten Year Regression Estimate |
| `TxPayableRegGr%TTM` | Current liability for taxes owed within 12 months of balance sheet date. | Five Year Regression Growth |
| `TxPayablePSQ` | Current liability for taxes owed within 12 months of balance sheet date. | Quarterly Per Share |
| `TxPayablePSA` | Current liability for taxes owed within 12 months of balance sheet date. | Annual Per Share |
| `TxPayable%AssetsQ` | Current liability for taxes owed within 12 months of balance sheet date. | % of Quarterly Assets |
| `TxPayable%AssetsA` | Current liability for taxes owed within 12 months of balance sheet date. | % of Annual Assets |
| `TxPayable3YAvg` | Current liability for taxes owed within 12 months of balance sheet date. | Three Year Average |
| `TxPayable5YAvg` | Current liability for taxes owed within 12 months of balance sheet date. | Five Year Average |

### Liabilities-Noncurrent

#### `CapLease(offset, type[, NAHandling])`
```p123
CapLease(offset, type[, NAHandling])
```

Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt.

Capitalized leases differ from operating leases in that the lessee assumes both ownership and the right of use, whereas an operating lease only transfers the right of use. Property and equipment held under capitalized leases are recognized as depreciable and impairable assets, and the contractual payment obligations are recognized as liabilities, of which the amount due within one year is included in Current Portion of Long-Term Debt.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CapLeaseQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Latest Quarter |
| `CapLeasePQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Previous Quarter |
| `CapLeasePYQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Previous Quarter 1 Year Ago |
| `CapLeaseTTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Trailing 12 Months |
| `CapLeasePTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Previous Trailing 12 Months |
| `CapLeaseA` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Latest Year |
| `CapLeasePY` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Previous Year |
| `CapLeaseGr%PQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Q vs Previous Q Growth |
| `CapLeaseGr%PYQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Q vs 1 year ago Q Growth |
| `CapLeaseGr%TTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Trailing Twelve Months Growth |
| `CapLeaseGr%PQTTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Trailing Twelve Months Growth 1Q Ago |
| `CapLeaseGr%A` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Growth Annual |
| `CapLeaseGr%3Y` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Three Year Annualized Growth |
| `CapLeaseGr%5Y` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Five Year Annualized Growth |
| `CapLeaseGr%10Y` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Ten Year Annualized Growth |
| `CapLeaseRSD%ANN` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Ten Year Relative Standard Deviation |
| `CapLeaseRSD%TTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Five Year Relative Standard Deviation |
| `CapLeaseRegEstANN` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Ten Year Regression Estimate |
| `CapLeaseRegEstTTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Five Year Regression Estimate |
| `CapLeaseRegGr%ANN` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Ten Year Regression Estimate |
| `CapLeaseRegGr%TTM` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Five Year Regression Growth |
| `CapLeasePSQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Quarterly Per Share |
| `CapLeasePSA` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Annual Per Share |
| `CapLease%AssetsQ` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | % of Quarterly Assets |
| `CapLease%AssetsA` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | % of Annual Assets |
| `CapLease3YAvg` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Three Year Average |
| `CapLease5YAvg` | Represents all obligations incurred through the contractual leasing of long-term assets, by which the periodic lease payments resemble payments on interest and debt capital. As such, capitalized leases are considered to be a form of long-term debt. | Five Year Average |

#### `TxDfdIC(offset, type[, NAHandling])`
```p123
TxDfdIC(offset, type[, NAHandling])
```

Deferred Taxes and Investment Credits is accumulated taxes deferred due to timing issues and investment tax credits. It is a liability (the taxes will be repaid in the future) but this line specifically excludes the current portion of tax credits.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TxDfdICQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Latest Quarter |
| `TxDfdICPQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Previous Quarter |
| `TxDfdICPYQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Previous Quarter 1 Year Ago |
| `TxDfdICTTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Trailing 12 Months |
| `TxDfdICPTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Previous Trailing 12 Months |
| `TxDfdICA` | Accumulated deferred taxes from timing differences plus investment tax credits. | Latest Year |
| `TxDfdICPY` | Accumulated deferred taxes from timing differences plus investment tax credits. | Previous Year |
| `TxDfdICGr%PQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Q vs Previous Q Growth |
| `TxDfdICGr%PYQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Q vs 1 year ago Q Growth |
| `TxDfdICGr%TTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Trailing Twelve Months Growth |
| `TxDfdICGr%PQTTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Trailing Twelve Months Growth 1Q Ago |
| `TxDfdICGr%A` | Accumulated deferred taxes from timing differences plus investment tax credits. | Growth Annual |
| `TxDfdICGr%3Y` | Accumulated deferred taxes from timing differences plus investment tax credits. | Three Year Annualized Growth |
| `TxDfdICGr%5Y` | Accumulated deferred taxes from timing differences plus investment tax credits. | Five Year Annualized Growth |
| `TxDfdICGr%10Y` | Accumulated deferred taxes from timing differences plus investment tax credits. | Ten Year Annualized Growth |
| `TxDfdICRSD%ANN` | Accumulated deferred taxes from timing differences plus investment tax credits. | Ten Year Relative Standard Deviation |
| `TxDfdICRSD%TTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Five Year Relative Standard Deviation |
| `TxDfdICRegEstANN` | Accumulated deferred taxes from timing differences plus investment tax credits. | Ten Year Regression Estimate |
| `TxDfdICRegEstTTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Five Year Regression Estimate |
| `TxDfdICRegGr%ANN` | Accumulated deferred taxes from timing differences plus investment tax credits. | Ten Year Regression Estimate |
| `TxDfdICRegGr%TTM` | Accumulated deferred taxes from timing differences plus investment tax credits. | Five Year Regression Growth |
| `TxDfdICPSQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | Quarterly Per Share |
| `TxDfdICPSA` | Accumulated deferred taxes from timing differences plus investment tax credits. | Annual Per Share |
| `TxDfdIC%AssetsQ` | Accumulated deferred taxes from timing differences plus investment tax credits. | % of Quarterly Assets |
| `TxDfdIC%AssetsA` | Accumulated deferred taxes from timing differences plus investment tax credits. | % of Annual Assets |
| `TxDfdIC3YAvg` | Accumulated deferred taxes from timing differences plus investment tax credits. | Three Year Average |
| `TxDfdIC5YAvg` | Accumulated deferred taxes from timing differences plus investment tax credits. | Five Year Average |

#### `DbtLT(offset, type[, NAHandling])`
```p123
DbtLT(offset, type[, NAHandling])
```

Long Term Debt is all debt that is due more than 12 months after the date of the latest balance sheet, as selected by the type and offset inputs. This measure specifically excludes the current portion of long-term debt.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DbtLTQ` | Debt due more than 12 months from balance sheet date. | Latest Quarter |
| `DbtLTPQ` | Debt due more than 12 months from balance sheet date. | Previous Quarter |
| `DbtLTPYQ` | Debt due more than 12 months from balance sheet date. | Previous Quarter 1 Year Ago |
| `DbtLTTTM` | Debt due more than 12 months from balance sheet date. | Trailing 12 Months |
| `DbtLTPTM` | Debt due more than 12 months from balance sheet date. | Previous Trailing 12 Months |
| `DbtLTA` | Debt due more than 12 months from balance sheet date. | Latest Year |
| `DbtLTPY` | Debt due more than 12 months from balance sheet date. | Previous Year |
| `DbtLTGr%PQ` | Debt due more than 12 months from balance sheet date. | Q vs Previous Q Growth |
| `DbtLTGr%PYQ` | Debt due more than 12 months from balance sheet date. | Q vs 1 year ago Q Growth |
| `DbtLTGr%TTM` | Debt due more than 12 months from balance sheet date. | Trailing Twelve Months Growth |
| `DbtLTGr%PQTTM` | Debt due more than 12 months from balance sheet date. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLTGr%A` | Debt due more than 12 months from balance sheet date. | Growth Annual |
| `DbtLTGr%3Y` | Debt due more than 12 months from balance sheet date. | Three Year Annualized Growth |
| `DbtLTGr%5Y` | Debt due more than 12 months from balance sheet date. | Five Year Annualized Growth |
| `DbtLTGr%10Y` | Debt due more than 12 months from balance sheet date. | Ten Year Annualized Growth |
| `DbtLTRSD%ANN` | Debt due more than 12 months from balance sheet date. | Ten Year Relative Standard Deviation |
| `DbtLTRSD%TTM` | Debt due more than 12 months from balance sheet date. | Five Year Relative Standard Deviation |
| `DbtLTRegEstANN` | Debt due more than 12 months from balance sheet date. | Ten Year Regression Estimate |
| `DbtLTRegEstTTM` | Debt due more than 12 months from balance sheet date. | Five Year Regression Estimate |
| `DbtLTRegGr%ANN` | Debt due more than 12 months from balance sheet date. | Ten Year Regression Estimate |
| `DbtLTRegGr%TTM` | Debt due more than 12 months from balance sheet date. | Five Year Regression Growth |
| `DbtLTPSQ` | Debt due more than 12 months from balance sheet date. | Quarterly Per Share |
| `DbtLTPSA` | Debt due more than 12 months from balance sheet date. | Annual Per Share |
| `DbtLT%AssetsQ` | Debt due more than 12 months from balance sheet date. | % of Quarterly Assets |
| `DbtLT%AssetsA` | Debt due more than 12 months from balance sheet date. | % of Annual Assets |
| `DbtLT3YAvg` | Debt due more than 12 months from balance sheet date. | Three Year Average |
| `DbtLT5YAvg` | Debt due more than 12 months from balance sheet date. | Five Year Average |

#### `LiabNonCurOther(offset, type[, NAHandling])`
```p123
LiabNonCurOther(offset, type[, NAHandling])
```

Other Non-Current Liabilities is a liability line on the balance sheet. It is a total of all liabilities that are not current (of any type), debt, deferred taxes, investment tax credits, or minority interest. It also excludes shareholders equity lines.

The line is made up of, among other things, long-term accounts payable, negative goodwill, unearned income and dividends payable.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `LiabNonCurOtherQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Latest Quarter |
| `LiabNonCurOtherPQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Previous Quarter |
| `LiabNonCurOtherPYQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Previous Quarter 1 Year Ago |
| `LiabNonCurOtherTTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Trailing 12 Months |
| `LiabNonCurOtherPTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Previous Trailing 12 Months |
| `LiabNonCurOtherA` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Latest Year |
| `LiabNonCurOtherPY` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Previous Year |
| `LiabNonCurOtherGr%PQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Q vs Previous Q Growth |
| `LiabNonCurOtherGr%PYQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Q vs 1 year ago Q Growth |
| `LiabNonCurOtherGr%TTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Trailing Twelve Months Growth |
| `LiabNonCurOtherGr%PQTTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Trailing Twelve Months Growth 1Q Ago |
| `LiabNonCurOtherGr%A` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Growth Annual |
| `LiabNonCurOtherGr%3Y` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Three Year Annualized Growth |
| `LiabNonCurOtherGr%5Y` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Five Year Annualized Growth |
| `LiabNonCurOtherGr%10Y` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Ten Year Annualized Growth |
| `LiabNonCurOtherRSD%ANN` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Ten Year Relative Standard Deviation |
| `LiabNonCurOtherRSD%TTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Five Year Relative Standard Deviation |
| `LiabNonCurOtherRegEstANN` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Ten Year Regression Estimate |
| `LiabNonCurOtherRegEstTTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Five Year Regression Estimate |
| `LiabNonCurOtherRegGr%ANN` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Ten Year Regression Estimate |
| `LiabNonCurOtherRegGr%TTM` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Five Year Regression Growth |
| `LiabNonCurOtherPSQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Quarterly Per Share |
| `LiabNonCurOtherPSA` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Annual Per Share |
| `LiabNonCurOther%AssetsQ` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | % of Quarterly Assets |
| `LiabNonCurOther%AssetsA` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | % of Annual Assets |
| `LiabNonCurOther3YAvg` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Three Year Average |
| `LiabNonCurOther5YAvg` | All long-term liabilities excluding debt, deferred taxes, investment tax credits, and minority interest. | Five Year Average |

#### `DbtTot(offset, type[, NAHandling])`
```p123
DbtTot(offset, type[, NAHandling])
```

Total debt is the sum of current and long-term debt as reported on the latest balance sheet specified by the offset and type inputs.

For this item we simply sum the current and long-term debt figures.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DbtTotQ` | Sum of all debt obligations as reported on the balance sheet. | Latest Quarter |
| `DbtTotPQ` | Sum of all debt obligations as reported on the balance sheet. | Previous Quarter |
| `DbtTotPYQ` | Sum of all debt obligations as reported on the balance sheet. | Previous Quarter 1 Year Ago |
| `DbtTotTTM` | Sum of all debt obligations as reported on the balance sheet. | Trailing 12 Months |
| `DbtTotPTM` | Sum of all debt obligations as reported on the balance sheet. | Previous Trailing 12 Months |
| `DbtTotA` | Sum of all debt obligations as reported on the balance sheet. | Latest Year |
| `DbtTotPY` | Sum of all debt obligations as reported on the balance sheet. | Previous Year |
| `DbtTotGr%PQ` | Sum of all debt obligations as reported on the balance sheet. | Q vs Previous Q Growth |
| `DbtTotGr%PYQ` | Sum of all debt obligations as reported on the balance sheet. | Q vs 1 year ago Q Growth |
| `DbtTotGr%TTM` | Sum of all debt obligations as reported on the balance sheet. | Trailing Twelve Months Growth |
| `DbtTotGr%PQTTM` | Sum of all debt obligations as reported on the balance sheet. | Trailing Twelve Months Growth 1Q Ago |
| `DbtTotGr%A` | Sum of all debt obligations as reported on the balance sheet. | Growth Annual |
| `DbtTotGr%3Y` | Sum of all debt obligations as reported on the balance sheet. | Three Year Annualized Growth |
| `DbtTotGr%5Y` | Sum of all debt obligations as reported on the balance sheet. | Five Year Annualized Growth |
| `DbtTotGr%10Y` | Sum of all debt obligations as reported on the balance sheet. | Ten Year Annualized Growth |
| `DbtTotRSD%ANN` | Sum of all debt obligations as reported on the balance sheet. | Ten Year Relative Standard Deviation |
| `DbtTotRSD%TTM` | Sum of all debt obligations as reported on the balance sheet. | Five Year Relative Standard Deviation |
| `DbtTotRegEstANN` | Sum of all debt obligations as reported on the balance sheet. | Ten Year Regression Estimate |
| `DbtTotRegEstTTM` | Sum of all debt obligations as reported on the balance sheet. | Five Year Regression Estimate |
| `DbtTotRegGr%ANN` | Sum of all debt obligations as reported on the balance sheet. | Ten Year Regression Estimate |
| `DbtTotRegGr%TTM` | Sum of all debt obligations as reported on the balance sheet. | Five Year Regression Growth |
| `DbtTotPSQ` | Sum of all debt obligations as reported on the balance sheet. | Quarterly Per Share |
| `DbtTotPSA` | Sum of all debt obligations as reported on the balance sheet. | Annual Per Share |
| `DbtTot%AssetsQ` | Sum of all debt obligations as reported on the balance sheet. | % of Quarterly Assets |
| `DbtTot%AssetsA` | Sum of all debt obligations as reported on the balance sheet. | % of Annual Assets |
| `DbtTot3YAvg` | Sum of all debt obligations as reported on the balance sheet. | Three Year Average |
| `DbtTot5YAvg` | Sum of all debt obligations as reported on the balance sheet. | Five Year Average |

#### `LiabTot(offset, type[, NAHandling])`
```p123
LiabTot(offset, type[, NAHandling])
```

Total Liabilities is the sum total of all lines on the right side of the balance sheet that are not part of shareholders equity.

Liabilities typically include accounts payable and debt. Note that non-controlling interest is now split between redeemable and non-redeemable; only redeemable is included in this figure.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `LiabTotQ` | Sum of all balance sheet obligations excluding shareholders equity. | Latest Quarter |
| `LiabTotPQ` | Sum of all balance sheet obligations excluding shareholders equity. | Previous Quarter |
| `LiabTotPYQ` | Sum of all balance sheet obligations excluding shareholders equity. | Previous Quarter 1 Year Ago |
| `LiabTotTTM` | Sum of all balance sheet obligations excluding shareholders equity. | Trailing 12 Months |
| `LiabTotPTM` | Sum of all balance sheet obligations excluding shareholders equity. | Previous Trailing 12 Months |
| `LiabTotA` | Sum of all balance sheet obligations excluding shareholders equity. | Latest Year |
| `LiabTotPY` | Sum of all balance sheet obligations excluding shareholders equity. | Previous Year |
| `LiabTotGr%PQ` | Sum of all balance sheet obligations excluding shareholders equity. | Q vs Previous Q Growth |
| `LiabTotGr%PYQ` | Sum of all balance sheet obligations excluding shareholders equity. | Q vs 1 year ago Q Growth |
| `LiabTotGr%TTM` | Sum of all balance sheet obligations excluding shareholders equity. | Trailing Twelve Months Growth |
| `LiabTotGr%PQTTM` | Sum of all balance sheet obligations excluding shareholders equity. | Trailing Twelve Months Growth 1Q Ago |
| `LiabTotGr%A` | Sum of all balance sheet obligations excluding shareholders equity. | Growth Annual |
| `LiabTotGr%3Y` | Sum of all balance sheet obligations excluding shareholders equity. | Three Year Annualized Growth |
| `LiabTotGr%5Y` | Sum of all balance sheet obligations excluding shareholders equity. | Five Year Annualized Growth |
| `LiabTotGr%10Y` | Sum of all balance sheet obligations excluding shareholders equity. | Ten Year Annualized Growth |
| `LiabTotRSD%ANN` | Sum of all balance sheet obligations excluding shareholders equity. | Ten Year Relative Standard Deviation |
| `LiabTotRSD%TTM` | Sum of all balance sheet obligations excluding shareholders equity. | Five Year Relative Standard Deviation |
| `LiabTotRegEstANN` | Sum of all balance sheet obligations excluding shareholders equity. | Ten Year Regression Estimate |
| `LiabTotRegEstTTM` | Sum of all balance sheet obligations excluding shareholders equity. | Five Year Regression Estimate |
| `LiabTotRegGr%ANN` | Sum of all balance sheet obligations excluding shareholders equity. | Ten Year Regression Estimate |
| `LiabTotRegGr%TTM` | Sum of all balance sheet obligations excluding shareholders equity. | Five Year Regression Growth |
| `LiabTotPSQ` | Sum of all balance sheet obligations excluding shareholders equity. | Quarterly Per Share |
| `LiabTotPSA` | Sum of all balance sheet obligations excluding shareholders equity. | Annual Per Share |
| `LiabTot%AssetsQ` | Sum of all balance sheet obligations excluding shareholders equity. | % of Quarterly Assets |
| `LiabTot%AssetsA` | Sum of all balance sheet obligations excluding shareholders equity. | % of Annual Assets |
| `LiabTot3YAvg` | Sum of all balance sheet obligations excluding shareholders equity. | Three Year Average |
| `LiabTot5YAvg` | Sum of all balance sheet obligations excluding shareholders equity. | Five Year Average |

### Shareholders Equity

#### `BookVal(offset, type[, NAHandling])`
```p123
BookVal(offset, type[, NAHandling])
```

Book value is purchase price less depreciation of an asset. In the case of a company, it is assets less liabilities. We report our data provider's common equity line (not shareholder equity) as book value.

The typical calculation of book value for a company is total assets less total liabilities, which results in shareholder's equity. There are several lines on the right side of the balance sheet, though, that are potentially distortions. First, some companies have a value that is not asset, liability or equity: minority interest. Furthermore, some activities result in "equity" lines that are not value-additive: Preferred shares, in particular, function much as debt, yet are included in the equity section. (And minority interest has the potential to also appear in the equity section.)

Rather than second guess all the right-side lines that could affect book value, we just draw on common sense and report common equity rather than shareholder's equity.

A side note: Some definitions of book value deduct intangible assets. We have a separate function, tangible book value, that makes that adjustment.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `BookValQ` | Value of common equity excluding preferred shares and minority interests. | Latest Quarter |
| `BookValPQ` | Value of common equity excluding preferred shares and minority interests. | Previous Quarter |
| `BookValPYQ` | Value of common equity excluding preferred shares and minority interests. | Previous Quarter 1 Year Ago |
| `BookValTTM` | Value of common equity excluding preferred shares and minority interests. | Trailing 12 Months |
| `BookValPTM` | Value of common equity excluding preferred shares and minority interests. | Previous Trailing 12 Months |
| `BookValA` | Value of common equity excluding preferred shares and minority interests. | Latest Year |
| `BookValPY` | Value of common equity excluding preferred shares and minority interests. | Previous Year |
| `BookValGr%PQ` | Value of common equity excluding preferred shares and minority interests. | Q vs Previous Q Growth |
| `BookValGr%PYQ` | Value of common equity excluding preferred shares and minority interests. | Q vs 1 year ago Q Growth |
| `BookValGr%TTM` | Value of common equity excluding preferred shares and minority interests. | Trailing Twelve Months Growth |
| `BookValGr%PQTTM` | Value of common equity excluding preferred shares and minority interests. | Trailing Twelve Months Growth 1Q Ago |
| `BookValGr%A` | Value of common equity excluding preferred shares and minority interests. | Growth Annual |
| `BookValGr%3Y` | Value of common equity excluding preferred shares and minority interests. | Three Year Annualized Growth |
| `BookValGr%5Y` | Value of common equity excluding preferred shares and minority interests. | Five Year Annualized Growth |
| `BookValGr%10Y` | Value of common equity excluding preferred shares and minority interests. | Ten Year Annualized Growth |
| `BookValRSD%ANN` | Value of common equity excluding preferred shares and minority interests. | Ten Year Relative Standard Deviation |
| `BookValRSD%TTM` | Value of common equity excluding preferred shares and minority interests. | Five Year Relative Standard Deviation |
| `BookValRegEstANN` | Value of common equity excluding preferred shares and minority interests. | Ten Year Regression Estimate |
| `BookValRegEstTTM` | Value of common equity excluding preferred shares and minority interests. | Five Year Regression Estimate |
| `BookValRegGr%ANN` | Value of common equity excluding preferred shares and minority interests. | Ten Year Regression Estimate |
| `BookValRegGr%TTM` | Value of common equity excluding preferred shares and minority interests. | Five Year Regression Growth |
| `BookValPSQ` | Value of common equity excluding preferred shares and minority interests. | Quarterly Per Share |
| `BookValPSA` | Value of common equity excluding preferred shares and minority interests. | Annual Per Share |
| `BookVal%AssetsQ` | Value of common equity excluding preferred shares and minority interests. | % of Quarterly Assets |
| `BookVal%AssetsA` | Value of common equity excluding preferred shares and minority interests. | % of Annual Assets |
| `BookVal3YAvg` | Value of common equity excluding preferred shares and minority interests. | Three Year Average |
| `BookVal5YAvg` | Value of common equity excluding preferred shares and minority interests. | Five Year Average |

#### `CapSurplus(offset, type[, NAHandling])`
```p123
CapSurplus(offset, type[, NAHandling])
```

Capital surplus represents an amount above the par value chosen by the company for the shares that it issued.

The lion's share of this line is generally excess paid-in capital. CompuStat's documentation says the following about what is included and excluded from this data point:

This item includes the effect of and is adjusted for:

- Capital recorded upon reorganization or re-capitalization of the company

- Donations received from stockholders

- Gain on resale or cancellation of reacquired capital stock

- installments on common stock

- Miscellaneous paid-in-capital

- Notes receivable from sale of subscription stock

- Premium on capital stock (excess over par or stated value)

- Reduction in par or stated value of capital stock

- Reserve account for shares to be repurchased (reported in the Equity section)

- Residual from conversion of a class of common into the main class

- Stock of a subsidiary held by the parent company (reported in the Equity section)

- Unrealized stock appreciation

- Deferred compensation effect when reported in the Equity section of the Balance Sheet.

This item excludes:

- Excess over par of common treasury stock, included in Treasury Stock - Total Dollar Amount

- Excess over par of nonredeemable preferred treasury stock, included in Treasury Stock - Total Dollar Amount

- Issuable stock, included in Retained Earnings

- Miscellaneous notes receivable, included in Retained Earnings

- Reserve for shares to be issued, included in Retained Earnings

In practical terms, this is the closest that we have to paid-in capital, largely because of the way that this data is reported today by companies.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CapSurplusQ` | Amount shareholders paid above par value for shares. | Latest Quarter |
| `CapSurplusPQ` | Amount shareholders paid above par value for shares. | Previous Quarter |
| `CapSurplusPYQ` | Amount shareholders paid above par value for shares. | Previous Quarter 1 Year Ago |
| `CapSurplusTTM` | Amount shareholders paid above par value for shares. | Trailing 12 Months |
| `CapSurplusPTM` | Amount shareholders paid above par value for shares. | Previous Trailing 12 Months |
| `CapSurplusA` | Amount shareholders paid above par value for shares. | Latest Year |
| `CapSurplusPY` | Amount shareholders paid above par value for shares. | Previous Year |
| `CapSurplusGr%PQ` | Amount shareholders paid above par value for shares. | Q vs Previous Q Growth |
| `CapSurplusGr%PYQ` | Amount shareholders paid above par value for shares. | Q vs 1 year ago Q Growth |
| `CapSurplusGr%TTM` | Amount shareholders paid above par value for shares. | Trailing Twelve Months Growth |
| `CapSurplusGr%PQTTM` | Amount shareholders paid above par value for shares. | Trailing Twelve Months Growth 1Q Ago |
| `CapSurplusGr%A` | Amount shareholders paid above par value for shares. | Growth Annual |
| `CapSurplusGr%3Y` | Amount shareholders paid above par value for shares. | Three Year Annualized Growth |
| `CapSurplusGr%5Y` | Amount shareholders paid above par value for shares. | Five Year Annualized Growth |
| `CapSurplusGr%10Y` | Amount shareholders paid above par value for shares. | Ten Year Annualized Growth |
| `CapSurplusRSD%ANN` | Amount shareholders paid above par value for shares. | Ten Year Relative Standard Deviation |
| `CapSurplusRSD%TTM` | Amount shareholders paid above par value for shares. | Five Year Relative Standard Deviation |
| `CapSurplusRegEstANN` | Amount shareholders paid above par value for shares. | Ten Year Regression Estimate |
| `CapSurplusRegEstTTM` | Amount shareholders paid above par value for shares. | Five Year Regression Estimate |
| `CapSurplusRegGr%ANN` | Amount shareholders paid above par value for shares. | Ten Year Regression Estimate |
| `CapSurplusRegGr%TTM` | Amount shareholders paid above par value for shares. | Five Year Regression Growth |
| `CapSurplusPSQ` | Amount shareholders paid above par value for shares. | Quarterly Per Share |
| `CapSurplusPSA` | Amount shareholders paid above par value for shares. | Annual Per Share |
| `CapSurplus%AssetsQ` | Amount shareholders paid above par value for shares. | % of Quarterly Assets |
| `CapSurplus%AssetsA` | Amount shareholders paid above par value for shares. | % of Annual Assets |
| `CapSurplus3YAvg` | Amount shareholders paid above par value for shares. | Three Year Average |
| `CapSurplus5YAvg` | Amount shareholders paid above par value for shares. | Five Year Average |

#### `ComEq(offset, type[, NAHandling])`
```p123
ComEq(offset, type[, NAHandling])
```

Common equity is common shareholder's interest in the company as reported in the shareholder's equity section of the balance sheet. It is the sum of common stock, capital surplus and retained earnings.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `ComEqQ` | Common shareholders' ownership interest. | Latest Quarter |
| `ComEqPQ` | Common shareholders' ownership interest. | Previous Quarter |
| `ComEqPYQ` | Common shareholders' ownership interest. | Previous Quarter 1 Year Ago |
| `ComEqTTM` | Common shareholders' ownership interest. | Trailing 12 Months |
| `ComEqPTM` | Common shareholders' ownership interest. | Previous Trailing 12 Months |
| `ComEqA` | Common shareholders' ownership interest. | Latest Year |
| `ComEqPY` | Common shareholders' ownership interest. | Previous Year |
| `ComEqGr%PQ` | Common shareholders' ownership interest. | Q vs Previous Q Growth |
| `ComEqGr%PYQ` | Common shareholders' ownership interest. | Q vs 1 year ago Q Growth |
| `ComEqGr%TTM` | Common shareholders' ownership interest. | Trailing Twelve Months Growth |
| `ComEqGr%PQTTM` | Common shareholders' ownership interest. | Trailing Twelve Months Growth 1Q Ago |
| `ComEqGr%A` | Common shareholders' ownership interest. | Growth Annual |
| `ComEqGr%3Y` | Common shareholders' ownership interest. | Three Year Annualized Growth |
| `ComEqGr%5Y` | Common shareholders' ownership interest. | Five Year Annualized Growth |
| `ComEqGr%10Y` | Common shareholders' ownership interest. | Ten Year Annualized Growth |
| `ComEqRSD%ANN` | Common shareholders' ownership interest. | Ten Year Relative Standard Deviation |
| `ComEqRSD%TTM` | Common shareholders' ownership interest. | Five Year Relative Standard Deviation |
| `ComEqRegEstANN` | Common shareholders' ownership interest. | Ten Year Regression Estimate |
| `ComEqRegEstTTM` | Common shareholders' ownership interest. | Five Year Regression Estimate |
| `ComEqRegGr%ANN` | Common shareholders' ownership interest. | Ten Year Regression Estimate |
| `ComEqRegGr%TTM` | Common shareholders' ownership interest. | Five Year Regression Growth |
| `ComEqPSQ` | Common shareholders' ownership interest. | Quarterly Per Share |
| `ComEqPSA` | Common shareholders' ownership interest. | Annual Per Share |
| `ComEq%AssetsQ` | Common shareholders' ownership interest. | % of Quarterly Assets |
| `ComEq%AssetsA` | Common shareholders' ownership interest. | % of Annual Assets |
| `ComEq3YAvg` | Common shareholders' ownership interest. | Three Year Average |
| `ComEq5YAvg` | Common shareholders' ownership interest. | Five Year Average |

#### `NonControlInt(offset, type[, NAHandling])`
```p123
NonControlInt(offset, type[, NAHandling])
```

Total Non-Controlling Interest is a line reflecting the whole of what was minority interest prior to 2009.

FactSet retained this as minority interest, and this is therefore the correct line to be used with that database.

When using CompuStat, users may prefer NonControlIntRed and NonControlIntNonRed, which are redeemable non-controlling interest, which is is part of liabilities, and non-redeemable non-controlling interest, which is part of shareholders equity. Using either should be fine, but be cautious of double accounting.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NonControlIntQ` | Formerly minority interest (pre-2009). | Latest Quarter |
| `NonControlIntPQ` | Formerly minority interest (pre-2009). | Previous Quarter |
| `NonControlIntPYQ` | Formerly minority interest (pre-2009). | Previous Quarter 1 Year Ago |
| `NonControlIntTTM` | Formerly minority interest (pre-2009). | Trailing 12 Months |
| `NonControlIntPTM` | Formerly minority interest (pre-2009). | Previous Trailing 12 Months |
| `NonControlIntA` | Formerly minority interest (pre-2009). | Latest Year |
| `NonControlIntPY` | Formerly minority interest (pre-2009). | Previous Year |
| `NonControlIntGr%PQ` | Formerly minority interest (pre-2009). | Q vs Previous Q Growth |
| `NonControlIntGr%PYQ` | Formerly minority interest (pre-2009). | Q vs 1 year ago Q Growth |
| `NonControlIntGr%TTM` | Formerly minority interest (pre-2009). | Trailing Twelve Months Growth |
| `NonControlIntGr%PQTTM` | Formerly minority interest (pre-2009). | Trailing Twelve Months Growth 1Q Ago |
| `NonControlIntGr%A` | Formerly minority interest (pre-2009). | Growth Annual |
| `NonControlIntGr%3Y` | Formerly minority interest (pre-2009). | Three Year Annualized Growth |
| `NonControlIntGr%5Y` | Formerly minority interest (pre-2009). | Five Year Annualized Growth |
| `NonControlIntGr%10Y` | Formerly minority interest (pre-2009). | Ten Year Annualized Growth |
| `NonControlIntRSD%ANN` | Formerly minority interest (pre-2009). | Ten Year Relative Standard Deviation |
| `NonControlIntRSD%TTM` | Formerly minority interest (pre-2009). | Five Year Relative Standard Deviation |
| `NonControlIntRegEstANN` | Formerly minority interest (pre-2009). | Ten Year Regression Estimate |
| `NonControlIntRegEstTTM` | Formerly minority interest (pre-2009). | Five Year Regression Estimate |
| `NonControlIntRegGr%ANN` | Formerly minority interest (pre-2009). | Ten Year Regression Estimate |
| `NonControlIntRegGr%TTM` | Formerly minority interest (pre-2009). | Five Year Regression Growth |
| `NonControlIntPSQ` | Formerly minority interest (pre-2009). | Quarterly Per Share |
| `NonControlIntPSA` | Formerly minority interest (pre-2009). | Annual Per Share |
| `NonControlInt%AssetsQ` | Formerly minority interest (pre-2009). | % of Quarterly Assets |
| `NonControlInt%AssetsA` | Formerly minority interest (pre-2009). | % of Annual Assets |
| `NonControlInt3YAvg` | Formerly minority interest (pre-2009). | Three Year Average |
| `NonControlInt5YAvg` | Formerly minority interest (pre-2009). | Five Year Average |

#### `PfdEquity(offset, type[, NAHandling])`
```p123
PfdEquity(offset, type[, NAHandling])
```

Preferred Equity is the net number of preferred shares multiplied by the par or stated value per share as presented in the company's balance sheet.

There are several things worth considering before using this in a model:

First, as a practical matter for a company preferred equity functions more as debt without an expiration date than it does like common equity. The line is further muddied by the presence of convertible options attached to many preferred shares. The requirement to pay preferred dividends is almost as serious as it is to repay debt.

Second, because of its similarity in practical effect to other obligations like accounts payable and debt, this line should probably be removed from total equity when using shareholders equity. In fact, in order to avoid this and other adjustments (particularly non-redeemable non-controlling interest) we advise that users consider simply using common equity in lieu of shareholders equity.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `PfdEquityQ` | Net preferred shares multiplied by par/stated value per share. | Latest Quarter |
| `PfdEquityPQ` | Net preferred shares multiplied by par/stated value per share. | Previous Quarter |
| `PfdEquityPYQ` | Net preferred shares multiplied by par/stated value per share. | Previous Quarter 1 Year Ago |
| `PfdEquityTTM` | Net preferred shares multiplied by par/stated value per share. | Trailing 12 Months |
| `PfdEquityPTM` | Net preferred shares multiplied by par/stated value per share. | Previous Trailing 12 Months |
| `PfdEquityA` | Net preferred shares multiplied by par/stated value per share. | Latest Year |
| `PfdEquityPY` | Net preferred shares multiplied by par/stated value per share. | Previous Year |
| `PfdEquityGr%PQ` | Net preferred shares multiplied by par/stated value per share. | Q vs Previous Q Growth |
| `PfdEquityGr%PYQ` | Net preferred shares multiplied by par/stated value per share. | Q vs 1 year ago Q Growth |
| `PfdEquityGr%TTM` | Net preferred shares multiplied by par/stated value per share. | Trailing Twelve Months Growth |
| `PfdEquityGr%PQTTM` | Net preferred shares multiplied by par/stated value per share. | Trailing Twelve Months Growth 1Q Ago |
| `PfdEquityGr%A` | Net preferred shares multiplied by par/stated value per share. | Growth Annual |
| `PfdEquityGr%3Y` | Net preferred shares multiplied by par/stated value per share. | Three Year Annualized Growth |
| `PfdEquityGr%5Y` | Net preferred shares multiplied by par/stated value per share. | Five Year Annualized Growth |
| `PfdEquityGr%10Y` | Net preferred shares multiplied by par/stated value per share. | Ten Year Annualized Growth |
| `PfdEquityRSD%ANN` | Net preferred shares multiplied by par/stated value per share. | Ten Year Relative Standard Deviation |
| `PfdEquityRSD%TTM` | Net preferred shares multiplied by par/stated value per share. | Five Year Relative Standard Deviation |
| `PfdEquityRegEstANN` | Net preferred shares multiplied by par/stated value per share. | Ten Year Regression Estimate |
| `PfdEquityRegEstTTM` | Net preferred shares multiplied by par/stated value per share. | Five Year Regression Estimate |
| `PfdEquityRegGr%ANN` | Net preferred shares multiplied by par/stated value per share. | Ten Year Regression Estimate |
| `PfdEquityRegGr%TTM` | Net preferred shares multiplied by par/stated value per share. | Five Year Regression Growth |
| `PfdEquityPSQ` | Net preferred shares multiplied by par/stated value per share. | Quarterly Per Share |
| `PfdEquityPSA` | Net preferred shares multiplied by par/stated value per share. | Annual Per Share |
| `PfdEquity%AssetsQ` | Net preferred shares multiplied by par/stated value per share. | % of Quarterly Assets |
| `PfdEquity%AssetsA` | Net preferred shares multiplied by par/stated value per share. | % of Annual Assets |
| `PfdEquity3YAvg` | Net preferred shares multiplied by par/stated value per share. | Three Year Average |
| `PfdEquity5YAvg` | Net preferred shares multiplied by par/stated value per share. | Five Year Average |

#### `RetainedEarn(offset, type[, NAHandling])`
```p123
RetainedEarn(offset, type[, NAHandling])
```

Retained earnings are the portion of a company's net income that is kept rather than paid out as dividends. The line is part of Shareholder's Equity.

In theory, this should be equal to net earnings less dividends paid for the entire lifetime of the company. However, as a practical matter, accountants generally back into this number as Total Assets less Total Liabilities and other Shareholder's Equity items.

In general, a positive Retained Earnings is normal, as a company reinvests in its own operations and projects. Nonetheless, negative Retained Earnings is not unusual, so users should assume that this item can be below zero when designing models. Companies with negative Retained Earnings fall into two categories: Either they're young and are still paying off initial investment, or they've had a number of bad years, possibly including a decrease in the value of assets.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `RetainedEarnQ` | Net income kept rather than distributed as dividends. | Latest Quarter |
| `RetainedEarnPQ` | Net income kept rather than distributed as dividends. | Previous Quarter |
| `RetainedEarnPYQ` | Net income kept rather than distributed as dividends. | Previous Quarter 1 Year Ago |
| `RetainedEarnTTM` | Net income kept rather than distributed as dividends. | Trailing 12 Months |
| `RetainedEarnPTM` | Net income kept rather than distributed as dividends. | Previous Trailing 12 Months |
| `RetainedEarnA` | Net income kept rather than distributed as dividends. | Latest Year |
| `RetainedEarnPY` | Net income kept rather than distributed as dividends. | Previous Year |
| `RetainedEarnGr%PQ` | Net income kept rather than distributed as dividends. | Q vs Previous Q Growth |
| `RetainedEarnGr%PYQ` | Net income kept rather than distributed as dividends. | Q vs 1 year ago Q Growth |
| `RetainedEarnGr%TTM` | Net income kept rather than distributed as dividends. | Trailing Twelve Months Growth |
| `RetainedEarnGr%PQTTM` | Net income kept rather than distributed as dividends. | Trailing Twelve Months Growth 1Q Ago |
| `RetainedEarnGr%A` | Net income kept rather than distributed as dividends. | Growth Annual |
| `RetainedEarnGr%3Y` | Net income kept rather than distributed as dividends. | Three Year Annualized Growth |
| `RetainedEarnGr%5Y` | Net income kept rather than distributed as dividends. | Five Year Annualized Growth |
| `RetainedEarnGr%10Y` | Net income kept rather than distributed as dividends. | Ten Year Annualized Growth |
| `RetainedEarnRSD%ANN` | Net income kept rather than distributed as dividends. | Ten Year Relative Standard Deviation |
| `RetainedEarnRSD%TTM` | Net income kept rather than distributed as dividends. | Five Year Relative Standard Deviation |
| `RetainedEarnRegEstANN` | Net income kept rather than distributed as dividends. | Ten Year Regression Estimate |
| `RetainedEarnRegEstTTM` | Net income kept rather than distributed as dividends. | Five Year Regression Estimate |
| `RetainedEarnRegGr%ANN` | Net income kept rather than distributed as dividends. | Ten Year Regression Estimate |
| `RetainedEarnRegGr%TTM` | Net income kept rather than distributed as dividends. | Five Year Regression Growth |
| `RetainedEarnPSQ` | Net income kept rather than distributed as dividends. | Quarterly Per Share |
| `RetainedEarnPSA` | Net income kept rather than distributed as dividends. | Annual Per Share |
| `RetainedEarn%AssetsQ` | Net income kept rather than distributed as dividends. | % of Quarterly Assets |
| `RetainedEarn%AssetsA` | Net income kept rather than distributed as dividends. | % of Annual Assets |
| `RetainedEarn3YAvg` | Net income kept rather than distributed as dividends. | Three Year Average |
| `RetainedEarn5YAvg` | Net income kept rather than distributed as dividends. | Five Year Average |

#### `EqTot(offset, type[, NAHandling])`
```p123
EqTot(offset, type[, NAHandling])
```

Shareholders Equity is typically total assets less total liabilities as reported on the latest balance sheet as specified by the offset and type inputs.

Shareholders equity generally includes the par of common and preferred shares, paid-in capital and retained earnings/losses.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `EqTotQ` | Total assets minus total liabilities on the balance sheet. | Latest Quarter |
| `EqTotPQ` | Total assets minus total liabilities on the balance sheet. | Previous Quarter |
| `EqTotPYQ` | Total assets minus total liabilities on the balance sheet. | Previous Quarter 1 Year Ago |
| `EqTotTTM` | Total assets minus total liabilities on the balance sheet. | Trailing 12 Months |
| `EqTotPTM` | Total assets minus total liabilities on the balance sheet. | Previous Trailing 12 Months |
| `EqTotA` | Total assets minus total liabilities on the balance sheet. | Latest Year |
| `EqTotPY` | Total assets minus total liabilities on the balance sheet. | Previous Year |
| `EqTotGr%PQ` | Total assets minus total liabilities on the balance sheet. | Q vs Previous Q Growth |
| `EqTotGr%PYQ` | Total assets minus total liabilities on the balance sheet. | Q vs 1 year ago Q Growth |
| `EqTotGr%TTM` | Total assets minus total liabilities on the balance sheet. | Trailing Twelve Months Growth |
| `EqTotGr%PQTTM` | Total assets minus total liabilities on the balance sheet. | Trailing Twelve Months Growth 1Q Ago |
| `EqTotGr%A` | Total assets minus total liabilities on the balance sheet. | Growth Annual |
| `EqTotGr%3Y` | Total assets minus total liabilities on the balance sheet. | Three Year Annualized Growth |
| `EqTotGr%5Y` | Total assets minus total liabilities on the balance sheet. | Five Year Annualized Growth |
| `EqTotGr%10Y` | Total assets minus total liabilities on the balance sheet. | Ten Year Annualized Growth |
| `EqTotRSD%ANN` | Total assets minus total liabilities on the balance sheet. | Ten Year Relative Standard Deviation |
| `EqTotRSD%TTM` | Total assets minus total liabilities on the balance sheet. | Five Year Relative Standard Deviation |
| `EqTotRegEstANN` | Total assets minus total liabilities on the balance sheet. | Ten Year Regression Estimate |
| `EqTotRegEstTTM` | Total assets minus total liabilities on the balance sheet. | Five Year Regression Estimate |
| `EqTotRegGr%ANN` | Total assets minus total liabilities on the balance sheet. | Ten Year Regression Estimate |
| `EqTotRegGr%TTM` | Total assets minus total liabilities on the balance sheet. | Five Year Regression Growth |
| `EqTotPSQ` | Total assets minus total liabilities on the balance sheet. | Quarterly Per Share |
| `EqTotPSA` | Total assets minus total liabilities on the balance sheet. | Annual Per Share |
| `EqTot%AssetsQ` | Total assets minus total liabilities on the balance sheet. | % of Quarterly Assets |
| `EqTot%AssetsA` | Total assets minus total liabilities on the balance sheet. | % of Annual Assets |
| `EqTot3YAvg` | Total assets minus total liabilities on the balance sheet. | Three Year Average |
| `EqTot5YAvg` | Total assets minus total liabilities on the balance sheet. | Five Year Average |

#### `TanBV(offset, type[, NAHandling])`
```p123
TanBV(offset, type[, NAHandling])
```

Tangible Book Value is the purchase price of material assets held by the company.

Our book value is the value of Common Equity. (See that documentation for an explanation.) Tangible book value is book value less intangible assets.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TanBVQ` | Common equity minus intangible assets. | Latest Quarter |
| `TanBVPQ` | Common equity minus intangible assets. | Previous Quarter |
| `TanBVPYQ` | Common equity minus intangible assets. | Previous Quarter 1 Year Ago |
| `TanBVTTM` | Common equity minus intangible assets. | Trailing 12 Months |
| `TanBVPTM` | Common equity minus intangible assets. | Previous Trailing 12 Months |
| `TanBVA` | Common equity minus intangible assets. | Latest Year |
| `TanBVPY` | Common equity minus intangible assets. | Previous Year |
| `TanBVGr%PQ` | Common equity minus intangible assets. | Q vs Previous Q Growth |
| `TanBVGr%PYQ` | Common equity minus intangible assets. | Q vs 1 year ago Q Growth |
| `TanBVGr%TTM` | Common equity minus intangible assets. | Trailing Twelve Months Growth |
| `TanBVGr%PQTTM` | Common equity minus intangible assets. | Trailing Twelve Months Growth 1Q Ago |
| `TanBVGr%A` | Common equity minus intangible assets. | Growth Annual |
| `TanBVGr%3Y` | Common equity minus intangible assets. | Three Year Annualized Growth |
| `TanBVGr%5Y` | Common equity minus intangible assets. | Five Year Annualized Growth |
| `TanBVGr%10Y` | Common equity minus intangible assets. | Ten Year Annualized Growth |
| `TanBVRSD%ANN` | Common equity minus intangible assets. | Ten Year Relative Standard Deviation |
| `TanBVRSD%TTM` | Common equity minus intangible assets. | Five Year Relative Standard Deviation |
| `TanBVRegEstANN` | Common equity minus intangible assets. | Ten Year Regression Estimate |
| `TanBVRegEstTTM` | Common equity minus intangible assets. | Five Year Regression Estimate |
| `TanBVRegGr%ANN` | Common equity minus intangible assets. | Ten Year Regression Estimate |
| `TanBVRegGr%TTM` | Common equity minus intangible assets. | Five Year Regression Growth |
| `TanBVPSQ` | Common equity minus intangible assets. | Quarterly Per Share |
| `TanBVPSA` | Common equity minus intangible assets. | Annual Per Share |
| `TanBV%AssetsQ` | Common equity minus intangible assets. | % of Quarterly Assets |
| `TanBV%AssetsA` | Common equity minus intangible assets. | % of Annual Assets |
| `TanBV3YAvg` | Common equity minus intangible assets. | Three Year Average |
| `TanBV5YAvg` | Common equity minus intangible assets. | Five Year Average |

### Shares

#### `SharesCur(barsAgo)`
```p123
SharesCur(barsAgo)
```

This function returns the most recent available shares outstanding, taken from the daily pricing database rather than the financial statements. The offset is in "bars" which in this case is trading days. A zero is the most recent day's shares outstanding, while any higher number is the figure from that many bars in the past.

NOTE: Returns only the # of shares from the current primary stock. Using SharesCur with companies with multiple share classes for things like MarketCap will not be correct.

This version of shares outstanding has the potential to be updated not only on the regular earnings reporting schedule, but also with information that might become available in between those announcements: This includes proxies, buybacks, announced conversions of options and any other corporate event that might impact the number of outstanding shares.

While there is no upper limit to the number of bars, the data itself starts in mid-1998. Prior to 2002, ADRs use the latest interim financial-statement figures instead of the daily shares outstanding numbers because of missing data in that time period.

This line is net of treasury shares.

| Parameter | Description |
|---|---|
| `barsAgo` | Trading-day offset: 0 is the most recent day's shares outstanding; higher numbers return the figure that many bars in the past. |

#### `Shares(offset, type[, NAHandling])`
```p123
Shares(offset, type[, NAHandling])
```

These factor/functions return the number of undiluted shares outstanding.

The factor form is a direct read of the shares line from the data provider, and it does not fall back if absent. If a fallback is desired, use, for example, Shares(0, QTR, FALLBACK).

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SharesQ` | Undiluted shares outstanding. | Latest Quarter |
| `SharesPQ` | Undiluted shares outstanding. | Previous Quarter |
| `SharesPYQ` | Undiluted shares outstanding. | Previous Quarter 1 Year Ago |
| `SharesTTM` | Undiluted shares outstanding. | Trailing 12 Months |
| `SharesPTM` | Undiluted shares outstanding. | Previous Trailing 12 Months |
| `SharesA` | Undiluted shares outstanding. | Latest Year |
| `SharesPY` | Undiluted shares outstanding. | Previous Year |
| `SharesGr%PQ` | Undiluted shares outstanding. | Q vs Previous Q Growth |
| `SharesGr%PYQ` | Undiluted shares outstanding. | Q vs 1 year ago Q Growth |
| `SharesGr%TTM` | Undiluted shares outstanding. | Trailing Twelve Months Growth |
| `SharesGr%PQTTM` | Undiluted shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `SharesGr%A` | Undiluted shares outstanding. | Growth Annual |
| `SharesGr%3Y` | Undiluted shares outstanding. | Three Year Annualized Growth |
| `SharesGr%5Y` | Undiluted shares outstanding. | Five Year Annualized Growth |
| `SharesGr%10Y` | Undiluted shares outstanding. | Ten Year Annualized Growth |
| `SharesRSD%ANN` | Undiluted shares outstanding. | Ten Year Relative Standard Deviation |
| `SharesRSD%TTM` | Undiluted shares outstanding. | Five Year Relative Standard Deviation |
| `SharesRegEstANN` | Undiluted shares outstanding. | Ten Year Regression Estimate |
| `SharesRegEstTTM` | Undiluted shares outstanding. | Five Year Regression Estimate |
| `SharesRegGr%ANN` | Undiluted shares outstanding. | Ten Year Regression Estimate |
| `SharesRegGr%TTM` | Undiluted shares outstanding. | Five Year Regression Growth |
| `Shares3YAvg` | Undiluted shares outstanding. | Three Year Average |
| `Shares5YAvg` | Undiluted shares outstanding. | Five Year Average |

#### `SharesFD(offset, type[, NAHandling])`
```p123
SharesFD(offset, type[, NAHandling])
```

SharesFD is the number of fully diluted shares, and, in the interests of fiscal conservativism, is the figure that we use for most per-share valuations on the site.

The factor form is a direct read of the shares line from the data provider, and it does not fall back if absent. If a fallback is desired, use, for example, SharesFD(0, QTR, FALLBACK).

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `SharesFDQ` | Fully diluted shares outstanding. | Latest Quarter |
| `SharesFDPQ` | Fully diluted shares outstanding. | Previous Quarter |
| `SharesFDPYQ` | Fully diluted shares outstanding. | Previous Quarter 1 Year Ago |
| `SharesFDTTM` | Fully diluted shares outstanding. | Trailing 12 Months |
| `SharesFDPTM` | Fully diluted shares outstanding. | Previous Trailing 12 Months |
| `SharesFDA` | Fully diluted shares outstanding. | Latest Year |
| `SharesFDPY` | Fully diluted shares outstanding. | Previous Year |
| `SharesFDGr%PQ` | Fully diluted shares outstanding. | Q vs Previous Q Growth |
| `SharesFDGr%PYQ` | Fully diluted shares outstanding. | Q vs 1 year ago Q Growth |
| `SharesFDGr%TTM` | Fully diluted shares outstanding. | Trailing Twelve Months Growth |
| `SharesFDGr%PQTTM` | Fully diluted shares outstanding. | Trailing Twelve Months Growth 1Q Ago |
| `SharesFDGr%A` | Fully diluted shares outstanding. | Growth Annual |
| `SharesFDGr%3Y` | Fully diluted shares outstanding. | Three Year Annualized Growth |
| `SharesFDGr%5Y` | Fully diluted shares outstanding. | Five Year Annualized Growth |
| `SharesFDGr%10Y` | Fully diluted shares outstanding. | Ten Year Annualized Growth |
| `SharesFDRSD%ANN` | Fully diluted shares outstanding. | Ten Year Relative Standard Deviation |
| `SharesFDRSD%TTM` | Fully diluted shares outstanding. | Five Year Relative Standard Deviation |
| `SharesFDRegEstANN` | Fully diluted shares outstanding. | Ten Year Regression Estimate |
| `SharesFDRegEstTTM` | Fully diluted shares outstanding. | Five Year Regression Estimate |
| `SharesFDRegGr%ANN` | Fully diluted shares outstanding. | Ten Year Regression Estimate |
| `SharesFDRegGr%TTM` | Fully diluted shares outstanding. | Five Year Regression Growth |
| `SharesFD3YAvg` | Fully diluted shares outstanding. | Three Year Average |
| `SharesFD5YAvg` | Fully diluted shares outstanding. | Five Year Average |

## Cash Flow Statement

### Operating

#### `TxAcrudChg(offset, type[, NAHandling])`
```p123
TxAcrudChg(offset, type[, NAHandling])
```

Change in Accrued Income Taxes reflects increases and decreases in accrued taxes on the balance sheet. This is a payable account and is therefore a liability. However, this function refers to increases or decreases, as it is a cash flow line.

This function is positive when accrued taxes increased and negative when they decreased.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TxAcrudChgQ` | Balance sheet changes in tax liabilities. | Latest Quarter |
| `TxAcrudChgPQ` | Balance sheet changes in tax liabilities. | Previous Quarter |
| `TxAcrudChgPYQ` | Balance sheet changes in tax liabilities. | Previous Quarter 1 Year Ago |
| `TxAcrudChgTTM` | Balance sheet changes in tax liabilities. | Trailing 12 Months |
| `TxAcrudChgPTM` | Balance sheet changes in tax liabilities. | Previous Trailing 12 Months |
| `TxAcrudChgA` | Balance sheet changes in tax liabilities. | Latest Year |
| `TxAcrudChgPY` | Balance sheet changes in tax liabilities. | Previous Year |
| `TxAcrudChgGr%PQ` | Balance sheet changes in tax liabilities. | Q vs Previous Q Growth |
| `TxAcrudChgGr%PYQ` | Balance sheet changes in tax liabilities. | Q vs 1 year ago Q Growth |
| `TxAcrudChgGr%TTM` | Balance sheet changes in tax liabilities. | Trailing Twelve Months Growth |
| `TxAcrudChgGr%PQTTM` | Balance sheet changes in tax liabilities. | Trailing Twelve Months Growth 1Q Ago |
| `TxAcrudChgGr%A` | Balance sheet changes in tax liabilities. | Growth Annual |
| `TxAcrudChgGr%3Y` | Balance sheet changes in tax liabilities. | Three Year Annualized Growth |
| `TxAcrudChgGr%5Y` | Balance sheet changes in tax liabilities. | Five Year Annualized Growth |
| `TxAcrudChgGr%10Y` | Balance sheet changes in tax liabilities. | Ten Year Annualized Growth |
| `TxAcrudChgRSD%ANN` | Balance sheet changes in tax liabilities. | Ten Year Relative Standard Deviation |
| `TxAcrudChgRSD%TTM` | Balance sheet changes in tax liabilities. | Five Year Relative Standard Deviation |
| `TxAcrudChgRegEstANN` | Balance sheet changes in tax liabilities. | Ten Year Regression Estimate |
| `TxAcrudChgRegEstTTM` | Balance sheet changes in tax liabilities. | Five Year Regression Estimate |
| `TxAcrudChgRegGr%ANN` | Balance sheet changes in tax liabilities. | Ten Year Regression Estimate |
| `TxAcrudChgRegGr%TTM` | Balance sheet changes in tax liabilities. | Five Year Regression Growth |
| `TxAcrudChgPSQ` | Balance sheet changes in tax liabilities. | Quarterly Per Share |
| `TxAcrudChgPSA` | Balance sheet changes in tax liabilities. | Annual Per Share |
| `TxAcrudChg%SalesQ` | Balance sheet changes in tax liabilities. | % of Quarterly Sales |
| `TxAcrudChg%SalesA` | Balance sheet changes in tax liabilities. | % of Annual Sales |
| `TxAcrudChg%AssetsQ` | Balance sheet changes in tax liabilities. | % of Quarterly Assets |
| `TxAcrudChg%AssetsA` | Balance sheet changes in tax liabilities. | % of Annual Assets |
| `TxAcrudChg3YAvg` | Balance sheet changes in tax liabilities. | Three Year Average |
| `TxAcrudChg5YAvg` | Balance sheet changes in tax liabilities. | Five Year Average |

#### `RecvblChg(offset, type[, NAHandling])`
```p123
RecvblChg(offset, type[, NAHandling])
```

The Change in Receivables is a financial metric that captures the fluctuation in the 'Receivables' line item on a company's balance sheet over a given period. Receivables typically represents money owed to a company by its customers for goods or services that have been delivered or used but not yet paid for.

Understanding the change in this metric is useful for assessing a company's cash flow and its efficiency in collecting payments. If Accounts Receivable is increasing, it might indicate that the company is selling more on credit terms or facing challenges in collecting payments. Conversely, a decrease might suggest prompt payment collection or fewer credit sales.

An increase in Accounts Receivable is denoted by a negative value, while a decrease is shown as a positive value.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `RecvblChgQ` | Changes in receivables balance over a period. | Latest Quarter |
| `RecvblChgPQ` | Changes in receivables balance over a period. | Previous Quarter |
| `RecvblChgPYQ` | Changes in receivables balance over a period. | Previous Quarter 1 Year Ago |
| `RecvblChgTTM` | Changes in receivables balance over a period. | Trailing 12 Months |
| `RecvblChgPTM` | Changes in receivables balance over a period. | Previous Trailing 12 Months |
| `RecvblChgA` | Changes in receivables balance over a period. | Latest Year |
| `RecvblChgPY` | Changes in receivables balance over a period. | Previous Year |
| `RecvblChgGr%PQ` | Changes in receivables balance over a period. | Q vs Previous Q Growth |
| `RecvblChgGr%PYQ` | Changes in receivables balance over a period. | Q vs 1 year ago Q Growth |
| `RecvblChgGr%TTM` | Changes in receivables balance over a period. | Trailing Twelve Months Growth |
| `RecvblChgGr%PQTTM` | Changes in receivables balance over a period. | Trailing Twelve Months Growth 1Q Ago |
| `RecvblChgGr%A` | Changes in receivables balance over a period. | Growth Annual |
| `RecvblChgGr%3Y` | Changes in receivables balance over a period. | Three Year Annualized Growth |
| `RecvblChgGr%5Y` | Changes in receivables balance over a period. | Five Year Annualized Growth |
| `RecvblChgGr%10Y` | Changes in receivables balance over a period. | Ten Year Annualized Growth |
| `RecvblChgRSD%ANN` | Changes in receivables balance over a period. | Ten Year Relative Standard Deviation |
| `RecvblChgRSD%TTM` | Changes in receivables balance over a period. | Five Year Relative Standard Deviation |
| `RecvblChgRegEstANN` | Changes in receivables balance over a period. | Ten Year Regression Estimate |
| `RecvblChgRegEstTTM` | Changes in receivables balance over a period. | Five Year Regression Estimate |
| `RecvblChgRegGr%ANN` | Changes in receivables balance over a period. | Ten Year Regression Estimate |
| `RecvblChgRegGr%TTM` | Changes in receivables balance over a period. | Five Year Regression Growth |
| `RecvblChgPSQ` | Changes in receivables balance over a period. | Quarterly Per Share |
| `RecvblChgPSA` | Changes in receivables balance over a period. | Annual Per Share |
| `RecvblChg%SalesQ` | Changes in receivables balance over a period. | % of Quarterly Sales |
| `RecvblChg%SalesA` | Changes in receivables balance over a period. | % of Annual Sales |
| `RecvblChg%AssetsQ` | Changes in receivables balance over a period. | % of Quarterly Assets |
| `RecvblChg%AssetsA` | Changes in receivables balance over a period. | % of Annual Assets |
| `RecvblChg3YAvg` | Changes in receivables balance over a period. | Three Year Average |
| `RecvblChg5YAvg` | Changes in receivables balance over a period. | Five Year Average |

#### `AccruedExp(offset, type[, NAHandling])`
```p123
AccruedExp(offset, type[, NAHandling])
```

Accrued Expenses is the change in the balance sheet lines of accrued liabilities for the period specified by the type input.

A positive number reflects an increase in the balance sheet account; a negative number is a decrease.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AccruedExpQ` | Change in accrued liabilities on a company's balance sheet. | Latest Quarter |
| `AccruedExpPQ` | Change in accrued liabilities on a company's balance sheet. | Previous Quarter |
| `AccruedExpPYQ` | Change in accrued liabilities on a company's balance sheet. | Previous Quarter 1 Year Ago |
| `AccruedExpTTM` | Change in accrued liabilities on a company's balance sheet. | Trailing 12 Months |
| `AccruedExpPTM` | Change in accrued liabilities on a company's balance sheet. | Previous Trailing 12 Months |
| `AccruedExpA` | Change in accrued liabilities on a company's balance sheet. | Latest Year |
| `AccruedExpPY` | Change in accrued liabilities on a company's balance sheet. | Previous Year |
| `AccruedExpGr%PQ` | Change in accrued liabilities on a company's balance sheet. | Q vs Previous Q Growth |
| `AccruedExpGr%PYQ` | Change in accrued liabilities on a company's balance sheet. | Q vs 1 year ago Q Growth |
| `AccruedExpGr%TTM` | Change in accrued liabilities on a company's balance sheet. | Trailing Twelve Months Growth |
| `AccruedExpGr%PQTTM` | Change in accrued liabilities on a company's balance sheet. | Trailing Twelve Months Growth 1Q Ago |
| `AccruedExpGr%A` | Change in accrued liabilities on a company's balance sheet. | Growth Annual |
| `AccruedExpGr%3Y` | Change in accrued liabilities on a company's balance sheet. | Three Year Annualized Growth |
| `AccruedExpGr%5Y` | Change in accrued liabilities on a company's balance sheet. | Five Year Annualized Growth |
| `AccruedExpGr%10Y` | Change in accrued liabilities on a company's balance sheet. | Ten Year Annualized Growth |
| `AccruedExpRSD%ANN` | Change in accrued liabilities on a company's balance sheet. | Ten Year Relative Standard Deviation |
| `AccruedExpRSD%TTM` | Change in accrued liabilities on a company's balance sheet. | Five Year Relative Standard Deviation |
| `AccruedExpRegEstANN` | Change in accrued liabilities on a company's balance sheet. | Ten Year Regression Estimate |
| `AccruedExpRegEstTTM` | Change in accrued liabilities on a company's balance sheet. | Five Year Regression Estimate |
| `AccruedExpRegGr%ANN` | Change in accrued liabilities on a company's balance sheet. | Ten Year Regression Estimate |
| `AccruedExpRegGr%TTM` | Change in accrued liabilities on a company's balance sheet. | Five Year Regression Growth |
| `AccruedExpPSQ` | Change in accrued liabilities on a company's balance sheet. | Quarterly Per Share |
| `AccruedExpPSA` | Change in accrued liabilities on a company's balance sheet. | Annual Per Share |
| `AccruedExp%SalesQ` | Change in accrued liabilities on a company's balance sheet. | % of Quarterly Sales |
| `AccruedExp%SalesA` | Change in accrued liabilities on a company's balance sheet. | % of Annual Sales |
| `AccruedExp%AssetsQ` | Change in accrued liabilities on a company's balance sheet. | % of Quarterly Assets |
| `AccruedExp%AssetsA` | Change in accrued liabilities on a company's balance sheet. | % of Annual Assets |
| `AccruedExp3YAvg` | Change in accrued liabilities on a company's balance sheet. | Three Year Average |
| `AccruedExp5YAvg` | Change in accrued liabilities on a company's balance sheet. | Five Year Average |

#### `InvtyChg(offset, type[, NAHandling])`
```p123
InvtyChg(offset, type[, NAHandling])
```

Inventory Change is the change in the current inventory account. It is part of the change in working capital on the cash flow statement, and it is negative for increases and positive for decreases.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InvtyChgQ` | Change in current inventory account from cash flow statement. | Latest Quarter |
| `InvtyChgPQ` | Change in current inventory account from cash flow statement. | Previous Quarter |
| `InvtyChgPYQ` | Change in current inventory account from cash flow statement. | Previous Quarter 1 Year Ago |
| `InvtyChgTTM` | Change in current inventory account from cash flow statement. | Trailing 12 Months |
| `InvtyChgPTM` | Change in current inventory account from cash flow statement. | Previous Trailing 12 Months |
| `InvtyChgA` | Change in current inventory account from cash flow statement. | Latest Year |
| `InvtyChgPY` | Change in current inventory account from cash flow statement. | Previous Year |
| `InvtyChgGr%PQ` | Change in current inventory account from cash flow statement. | Q vs Previous Q Growth |
| `InvtyChgGr%PYQ` | Change in current inventory account from cash flow statement. | Q vs 1 year ago Q Growth |
| `InvtyChgGr%TTM` | Change in current inventory account from cash flow statement. | Trailing Twelve Months Growth |
| `InvtyChgGr%PQTTM` | Change in current inventory account from cash flow statement. | Trailing Twelve Months Growth 1Q Ago |
| `InvtyChgGr%A` | Change in current inventory account from cash flow statement. | Growth Annual |
| `InvtyChgGr%3Y` | Change in current inventory account from cash flow statement. | Three Year Annualized Growth |
| `InvtyChgGr%5Y` | Change in current inventory account from cash flow statement. | Five Year Annualized Growth |
| `InvtyChgGr%10Y` | Change in current inventory account from cash flow statement. | Ten Year Annualized Growth |
| `InvtyChgRSD%ANN` | Change in current inventory account from cash flow statement. | Ten Year Relative Standard Deviation |
| `InvtyChgRSD%TTM` | Change in current inventory account from cash flow statement. | Five Year Relative Standard Deviation |
| `InvtyChgRegEstANN` | Change in current inventory account from cash flow statement. | Ten Year Regression Estimate |
| `InvtyChgRegEstTTM` | Change in current inventory account from cash flow statement. | Five Year Regression Estimate |
| `InvtyChgRegGr%ANN` | Change in current inventory account from cash flow statement. | Ten Year Regression Estimate |
| `InvtyChgRegGr%TTM` | Change in current inventory account from cash flow statement. | Five Year Regression Growth |
| `InvtyChgPSQ` | Change in current inventory account from cash flow statement. | Quarterly Per Share |
| `InvtyChgPSA` | Change in current inventory account from cash flow statement. | Annual Per Share |
| `InvtyChg%SalesQ` | Change in current inventory account from cash flow statement. | % of Quarterly Sales |
| `InvtyChg%SalesA` | Change in current inventory account from cash flow statement. | % of Annual Sales |
| `InvtyChg%AssetsQ` | Change in current inventory account from cash flow statement. | % of Quarterly Assets |
| `InvtyChg%AssetsA` | Change in current inventory account from cash flow statement. | % of Annual Assets |
| `InvtyChg3YAvg` | Change in current inventory account from cash flow statement. | Three Year Average |
| `InvtyChg5YAvg` | Change in current inventory account from cash flow statement. | Five Year Average |

#### `OtherWCChg(offset, type[, NAHandling])`
```p123
OtherWCChg(offset, type[, NAHandling])
```

Other Net Working Capital Change is a total of all change-in-working capital lines that are not included in in other, specific lines in the operating cash flow section of the cash-flow statement.

Inventory, accounts payable and accounts receivable all have their own lines. This line reflects all other changes in working capital accounts on the balance sheet for the duration of the period specified by the type input.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `OtherWCChgQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Latest Quarter |
| `OtherWCChgPQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Previous Quarter |
| `OtherWCChgPYQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Previous Quarter 1 Year Ago |
| `OtherWCChgTTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Trailing 12 Months |
| `OtherWCChgPTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Previous Trailing 12 Months |
| `OtherWCChgA` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Latest Year |
| `OtherWCChgPY` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Previous Year |
| `OtherWCChgGr%PQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Q vs Previous Q Growth |
| `OtherWCChgGr%PYQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Q vs 1 year ago Q Growth |
| `OtherWCChgGr%TTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Trailing Twelve Months Growth |
| `OtherWCChgGr%PQTTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Trailing Twelve Months Growth 1Q Ago |
| `OtherWCChgGr%A` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Growth Annual |
| `OtherWCChgGr%3Y` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Three Year Annualized Growth |
| `OtherWCChgGr%5Y` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Five Year Annualized Growth |
| `OtherWCChgGr%10Y` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Ten Year Annualized Growth |
| `OtherWCChgRSD%ANN` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Ten Year Relative Standard Deviation |
| `OtherWCChgRSD%TTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Five Year Relative Standard Deviation |
| `OtherWCChgRegEstANN` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Ten Year Regression Estimate |
| `OtherWCChgRegEstTTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Five Year Regression Estimate |
| `OtherWCChgRegGr%ANN` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Ten Year Regression Estimate |
| `OtherWCChgRegGr%TTM` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Five Year Regression Growth |
| `OtherWCChgPSQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Quarterly Per Share |
| `OtherWCChgPSA` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Annual Per Share |
| `OtherWCChg%SalesQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | % of Quarterly Sales |
| `OtherWCChg%SalesA` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | % of Annual Sales |
| `OtherWCChg%AssetsQ` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | % of Quarterly Assets |
| `OtherWCChg%AssetsA` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | % of Annual Assets |
| `OtherWCChg3YAvg` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Three Year Average |
| `OtherWCChg5YAvg` | All working capital changes not captured in specific line items (inventory, accounts payable, accounts receivable). | Five Year Average |

#### `PayablesChg(offset, type[, NAHandling])`
```p123
PayablesChg(offset, type[, NAHandling])
```

Change to Accounts Payable is the change in the balance sheet lines of accounts payable for the period specified by the type input.

A positive number reflects an increase in the balance sheet account; a negative number is a decrease.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `PayablesChgQ` | Change in accounts payable balance for the period. | Latest Quarter |
| `PayablesChgPQ` | Change in accounts payable balance for the period. | Previous Quarter |
| `PayablesChgPYQ` | Change in accounts payable balance for the period. | Previous Quarter 1 Year Ago |
| `PayablesChgTTM` | Change in accounts payable balance for the period. | Trailing 12 Months |
| `PayablesChgPTM` | Change in accounts payable balance for the period. | Previous Trailing 12 Months |
| `PayablesChgA` | Change in accounts payable balance for the period. | Latest Year |
| `PayablesChgPY` | Change in accounts payable balance for the period. | Previous Year |
| `PayablesChgGr%PQ` | Change in accounts payable balance for the period. | Q vs Previous Q Growth |
| `PayablesChgGr%PYQ` | Change in accounts payable balance for the period. | Q vs 1 year ago Q Growth |
| `PayablesChgGr%TTM` | Change in accounts payable balance for the period. | Trailing Twelve Months Growth |
| `PayablesChgGr%PQTTM` | Change in accounts payable balance for the period. | Trailing Twelve Months Growth 1Q Ago |
| `PayablesChgGr%A` | Change in accounts payable balance for the period. | Growth Annual |
| `PayablesChgGr%3Y` | Change in accounts payable balance for the period. | Three Year Annualized Growth |
| `PayablesChgGr%5Y` | Change in accounts payable balance for the period. | Five Year Annualized Growth |
| `PayablesChgGr%10Y` | Change in accounts payable balance for the period. | Ten Year Annualized Growth |
| `PayablesChgRSD%ANN` | Change in accounts payable balance for the period. | Ten Year Relative Standard Deviation |
| `PayablesChgRSD%TTM` | Change in accounts payable balance for the period. | Five Year Relative Standard Deviation |
| `PayablesChgRegEstANN` | Change in accounts payable balance for the period. | Ten Year Regression Estimate |
| `PayablesChgRegEstTTM` | Change in accounts payable balance for the period. | Five Year Regression Estimate |
| `PayablesChgRegGr%ANN` | Change in accounts payable balance for the period. | Ten Year Regression Estimate |
| `PayablesChgRegGr%TTM` | Change in accounts payable balance for the period. | Five Year Regression Growth |
| `PayablesChgPSQ` | Change in accounts payable balance for the period. | Quarterly Per Share |
| `PayablesChgPSA` | Change in accounts payable balance for the period. | Annual Per Share |
| `PayablesChg%SalesQ` | Change in accounts payable balance for the period. | % of Quarterly Sales |
| `PayablesChg%SalesA` | Change in accounts payable balance for the period. | % of Annual Sales |
| `PayablesChg%AssetsQ` | Change in accounts payable balance for the period. | % of Quarterly Assets |
| `PayablesChg%AssetsA` | Change in accounts payable balance for the period. | % of Annual Assets |
| `PayablesChg3YAvg` | Change in accounts payable balance for the period. | Three Year Average |
| `PayablesChg5YAvg` | Change in accounts payable balance for the period. | Five Year Average |

#### `TxDfd(offset, type[, NAHandling])`
```p123
TxDfd(offset, type[, NAHandling])
```

Deferred Taxes is an expense from the operations section of the cash flow statement that refers to repayment of the deferred tax liability line.

This item includes investment tax credits. CompuStat intends this to be a long-term item, not a current item, but they might include some current items when a company reports current and long-term deferred tax expense together.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `TxDfdQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Latest Quarter |
| `TxDfdPQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Previous Quarter |
| `TxDfdPYQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Previous Quarter 1 Year Ago |
| `TxDfdTTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Trailing 12 Months |
| `TxDfdPTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Previous Trailing 12 Months |
| `TxDfdA` | Expense from repaying deferred tax liabilities (on cash flow statement). | Latest Year |
| `TxDfdPY` | Expense from repaying deferred tax liabilities (on cash flow statement). | Previous Year |
| `TxDfdGr%PQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Q vs Previous Q Growth |
| `TxDfdGr%PYQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Q vs 1 year ago Q Growth |
| `TxDfdGr%TTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Trailing Twelve Months Growth |
| `TxDfdGr%PQTTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Trailing Twelve Months Growth 1Q Ago |
| `TxDfdGr%A` | Expense from repaying deferred tax liabilities (on cash flow statement). | Growth Annual |
| `TxDfdGr%3Y` | Expense from repaying deferred tax liabilities (on cash flow statement). | Three Year Annualized Growth |
| `TxDfdGr%5Y` | Expense from repaying deferred tax liabilities (on cash flow statement). | Five Year Annualized Growth |
| `TxDfdGr%10Y` | Expense from repaying deferred tax liabilities (on cash flow statement). | Ten Year Annualized Growth |
| `TxDfdRSD%ANN` | Expense from repaying deferred tax liabilities (on cash flow statement). | Ten Year Relative Standard Deviation |
| `TxDfdRSD%TTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Five Year Relative Standard Deviation |
| `TxDfdRegEstANN` | Expense from repaying deferred tax liabilities (on cash flow statement). | Ten Year Regression Estimate |
| `TxDfdRegEstTTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Five Year Regression Estimate |
| `TxDfdRegGr%ANN` | Expense from repaying deferred tax liabilities (on cash flow statement). | Ten Year Regression Estimate |
| `TxDfdRegGr%TTM` | Expense from repaying deferred tax liabilities (on cash flow statement). | Five Year Regression Growth |
| `TxDfdPSQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | Quarterly Per Share |
| `TxDfdPSA` | Expense from repaying deferred tax liabilities (on cash flow statement). | Annual Per Share |
| `TxDfd%SalesQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | % of Quarterly Sales |
| `TxDfd%SalesA` | Expense from repaying deferred tax liabilities (on cash flow statement). | % of Annual Sales |
| `TxDfd%AssetsQ` | Expense from repaying deferred tax liabilities (on cash flow statement). | % of Quarterly Assets |
| `TxDfd%AssetsA` | Expense from repaying deferred tax liabilities (on cash flow statement). | % of Annual Assets |
| `TxDfd3YAvg` | Expense from repaying deferred tax liabilities (on cash flow statement). | Three Year Average |
| `TxDfd5YAvg` | Expense from repaying deferred tax liabilities (on cash flow statement). | Five Year Average |

#### `DepAmortCF(offset, type[, NAHandling])`
```p123
DepAmortCF(offset, type[, NAHandling])
```

Depreciation and Amortization from Cash Flow Statement is the sum of depreciation and amortization as specifically reported on the cash flow statement. Note that, if as sometimes happens, a company reports depreciation and/or amortization on the income statement then this line will be zero.

This line refers to the change in depreciation and amortization that is part of income-statement expense but is not a cash item. As such, it is normally added back to an indirect cash-flow statement. Note that this line is therefore normally positive.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Formula**
```p123
Straight from filing Line-Item
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DepAmortCFQ` | Depreciation and Amortization as reported on cash flow statement. | Latest Quarter |
| `DepAmortCFPQ` | Depreciation and Amortization as reported on cash flow statement. | Previous Quarter |
| `DepAmortCFPYQ` | Depreciation and Amortization as reported on cash flow statement. | Previous Quarter 1 Year Ago |
| `DepAmortCFTTM` | Depreciation and Amortization as reported on cash flow statement. | Trailing 12 Months |
| `DepAmortCFPTM` | Depreciation and Amortization as reported on cash flow statement. | Previous Trailing 12 Months |
| `DepAmortCFA` | Depreciation and Amortization as reported on cash flow statement. | Latest Year |
| `DepAmortCFPY` | Depreciation and Amortization as reported on cash flow statement. | Previous Year |
| `DepAmortCFGr%PQ` | Depreciation and Amortization as reported on cash flow statement. | Q vs Previous Q Growth |
| `DepAmortCFGr%PYQ` | Depreciation and Amortization as reported on cash flow statement. | Q vs 1 year ago Q Growth |
| `DepAmortCFGr%TTM` | Depreciation and Amortization as reported on cash flow statement. | Trailing Twelve Months Growth |
| `DepAmortCFGr%PQTTM` | Depreciation and Amortization as reported on cash flow statement. | Trailing Twelve Months Growth 1Q Ago |
| `DepAmortCFGr%A` | Depreciation and Amortization as reported on cash flow statement. | Growth Annual |
| `DepAmortCFGr%3Y` | Depreciation and Amortization as reported on cash flow statement. | Three Year Annualized Growth |
| `DepAmortCFGr%5Y` | Depreciation and Amortization as reported on cash flow statement. | Five Year Annualized Growth |
| `DepAmortCFGr%10Y` | Depreciation and Amortization as reported on cash flow statement. | Ten Year Annualized Growth |
| `DepAmortCFRSD%ANN` | Depreciation and Amortization as reported on cash flow statement. | Ten Year Relative Standard Deviation |
| `DepAmortCFRSD%TTM` | Depreciation and Amortization as reported on cash flow statement. | Five Year Relative Standard Deviation |
| `DepAmortCFRegEstANN` | Depreciation and Amortization as reported on cash flow statement. | Ten Year Regression Estimate |
| `DepAmortCFRegEstTTM` | Depreciation and Amortization as reported on cash flow statement. | Five Year Regression Estimate |
| `DepAmortCFRegGr%ANN` | Depreciation and Amortization as reported on cash flow statement. | Ten Year Regression Estimate |
| `DepAmortCFRegGr%TTM` | Depreciation and Amortization as reported on cash flow statement. | Five Year Regression Growth |
| `DepAmortCFPSQ` | Depreciation and Amortization as reported on cash flow statement. | Quarterly Per Share |
| `DepAmortCFPSA` | Depreciation and Amortization as reported on cash flow statement. | Annual Per Share |
| `DepAmortCF%SalesQ` | Depreciation and Amortization as reported on cash flow statement. | % of Quarterly Sales |
| `DepAmortCF%SalesA` | Depreciation and Amortization as reported on cash flow statement. | % of Annual Sales |
| `DepAmortCF%AssetsQ` | Depreciation and Amortization as reported on cash flow statement. | % of Quarterly Assets |
| `DepAmortCF%AssetsA` | Depreciation and Amortization as reported on cash flow statement. | % of Annual Assets |
| `DepAmortCF3YAvg` | Depreciation and Amortization as reported on cash flow statement. | Three Year Average |
| `DepAmortCF5YAvg` | Depreciation and Amortization as reported on cash flow statement. | Five Year Average |

#### `NetIncCFStmt(offset, type[, NAHandling])`
```p123
NetIncCFStmt(offset, type[, NAHandling])
```

Net Income from Cash Flow Statement is the top line of the cash flow statement.

The operations portion of a cash flow statement when using the indirect method of accounting will begin with net income, the bottom line from the income statement. Expect for rare situations involving extraordinary or discontinued items, this figure should match the income statement. It is, however, explicitly what is reported on the cash flow statement.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetIncCFStmtQ` | Top line of the cash flow statement using indirect method. | Latest Quarter |
| `NetIncCFStmtPQ` | Top line of the cash flow statement using indirect method. | Previous Quarter |
| `NetIncCFStmtPYQ` | Top line of the cash flow statement using indirect method. | Previous Quarter 1 Year Ago |
| `NetIncCFStmtTTM` | Top line of the cash flow statement using indirect method. | Trailing 12 Months |
| `NetIncCFStmtPTM` | Top line of the cash flow statement using indirect method. | Previous Trailing 12 Months |
| `NetIncCFStmtA` | Top line of the cash flow statement using indirect method. | Latest Year |
| `NetIncCFStmtPY` | Top line of the cash flow statement using indirect method. | Previous Year |
| `NetIncCFStmtGr%PQ` | Top line of the cash flow statement using indirect method. | Q vs Previous Q Growth |
| `NetIncCFStmtGr%PYQ` | Top line of the cash flow statement using indirect method. | Q vs 1 year ago Q Growth |
| `NetIncCFStmtGr%TTM` | Top line of the cash flow statement using indirect method. | Trailing Twelve Months Growth |
| `NetIncCFStmtGr%PQTTM` | Top line of the cash flow statement using indirect method. | Trailing Twelve Months Growth 1Q Ago |
| `NetIncCFStmtGr%A` | Top line of the cash flow statement using indirect method. | Growth Annual |
| `NetIncCFStmtGr%3Y` | Top line of the cash flow statement using indirect method. | Three Year Annualized Growth |
| `NetIncCFStmtGr%5Y` | Top line of the cash flow statement using indirect method. | Five Year Annualized Growth |
| `NetIncCFStmtGr%10Y` | Top line of the cash flow statement using indirect method. | Ten Year Annualized Growth |
| `NetIncCFStmtRSD%ANN` | Top line of the cash flow statement using indirect method. | Ten Year Relative Standard Deviation |
| `NetIncCFStmtRSD%TTM` | Top line of the cash flow statement using indirect method. | Five Year Relative Standard Deviation |
| `NetIncCFStmtRegEstANN` | Top line of the cash flow statement using indirect method. | Ten Year Regression Estimate |
| `NetIncCFStmtRegEstTTM` | Top line of the cash flow statement using indirect method. | Five Year Regression Estimate |
| `NetIncCFStmtRegGr%ANN` | Top line of the cash flow statement using indirect method. | Ten Year Regression Estimate |
| `NetIncCFStmtRegGr%TTM` | Top line of the cash flow statement using indirect method. | Five Year Regression Growth |
| `NetIncCFStmtPSQ` | Top line of the cash flow statement using indirect method. | Quarterly Per Share |
| `NetIncCFStmtPSA` | Top line of the cash flow statement using indirect method. | Annual Per Share |
| `NetIncCFStmt%SalesQ` | Top line of the cash flow statement using indirect method. | % of Quarterly Sales |
| `NetIncCFStmt%SalesA` | Top line of the cash flow statement using indirect method. | % of Annual Sales |
| `NetIncCFStmt%AssetsQ` | Top line of the cash flow statement using indirect method. | % of Quarterly Assets |
| `NetIncCFStmt%AssetsA` | Top line of the cash flow statement using indirect method. | % of Annual Assets |
| `NetIncCFStmt3YAvg` | Top line of the cash flow statement using indirect method. | Three Year Average |
| `NetIncCFStmt5YAvg` | Top line of the cash flow statement using indirect method. | Five Year Average |

#### `OperCashFl(offset, type[, NAHandling])`
```p123
OperCashFl(offset, type[, NAHandling])
```

Cash From Operations is the total change in cash position due to operating activities.

This figure is, perhaps, the most conservative method of find out how much income is generated by a company's core business. It is also an important figure in the calculation of free cash flow.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `OperCashFlQ` | Total cash change from operating activities. | Latest Quarter |
| `OperCashFlPQ` | Total cash change from operating activities. | Previous Quarter |
| `OperCashFlPYQ` | Total cash change from operating activities. | Previous Quarter 1 Year Ago |
| `OperCashFlTTM` | Total cash change from operating activities. | Trailing 12 Months |
| `OperCashFlPTM` | Total cash change from operating activities. | Previous Trailing 12 Months |
| `OperCashFlA` | Total cash change from operating activities. | Latest Year |
| `OperCashFlPY` | Total cash change from operating activities. | Previous Year |
| `OperCashFlGr%PQ` | Total cash change from operating activities. | Q vs Previous Q Growth |
| `OperCashFlGr%PYQ` | Total cash change from operating activities. | Q vs 1 year ago Q Growth |
| `OperCashFlGr%TTM` | Total cash change from operating activities. | Trailing Twelve Months Growth |
| `OperCashFlGr%PQTTM` | Total cash change from operating activities. | Trailing Twelve Months Growth 1Q Ago |
| `OperCashFlGr%A` | Total cash change from operating activities. | Growth Annual |
| `OperCashFlGr%3Y` | Total cash change from operating activities. | Three Year Annualized Growth |
| `OperCashFlGr%5Y` | Total cash change from operating activities. | Five Year Annualized Growth |
| `OperCashFlGr%10Y` | Total cash change from operating activities. | Ten Year Annualized Growth |
| `OperCashFlRSD%ANN` | Total cash change from operating activities. | Ten Year Relative Standard Deviation |
| `OperCashFlRSD%TTM` | Total cash change from operating activities. | Five Year Relative Standard Deviation |
| `OperCashFlRegEstANN` | Total cash change from operating activities. | Ten Year Regression Estimate |
| `OperCashFlRegEstTTM` | Total cash change from operating activities. | Five Year Regression Estimate |
| `OperCashFlRegGr%ANN` | Total cash change from operating activities. | Ten Year Regression Estimate |
| `OperCashFlRegGr%TTM` | Total cash change from operating activities. | Five Year Regression Growth |
| `OperCashFlPSQ` | Total cash change from operating activities. | Quarterly Per Share |
| `OperCashFlPSA` | Total cash change from operating activities. | Annual Per Share |
| `OperCashFl%SalesQ` | Total cash change from operating activities. | % of Quarterly Sales |
| `OperCashFl%SalesA` | Total cash change from operating activities. | % of Annual Sales |
| `OperCashFl%AssetsQ` | Total cash change from operating activities. | % of Quarterly Assets |
| `OperCashFl%AssetsA` | Total cash change from operating activities. | % of Annual Assets |
| `OperCashFl3YAvg` | Total cash change from operating activities. | Three Year Average |
| `OperCashFl5YAvg` | Total cash change from operating activities. | Five Year Average |

#### `StkOptCF(offset, type[, NAHandling])`
```p123
StkOptCF(offset, type[, NAHandling])
```

Stock-based compensation represents employee compensation paid through equity instruments (stock options, restricted stock units, etc.) rather than cash. This creates a unique accounting situation where expenses are recognized without corresponding cash outflows. The accounting rules require companies to:

-
Record an expense on the income statement (StkOptExp) - showing the economic cost

-
Add it back on the cash flow statement (StkOptCF) - because no cash was actually spent

StkOptExp

StkOptExp is the expense companies record for employee stock compensation like stock options and restricted stock. This cost appears on the income statement as an operating expense that reduces earnings. The expense reflects the fair value of stock awards given to employees, spread out over the time period when employees earn the right to use them (the vesting period).

Key Characteristics:

-
Appears primarily within SG&A (Selling, General & Administrative) or R&D in the income statement, and reduces operating income and net income

-
Non-cash expense representing the fair value of equity awards

-
Recognized over the vesting period using fair value at grant date

-
Directly impacts reported earnings and EPS

StkOptCF

StkOptCF is the stock-based compensation adjustment that appears in the operating activities section of the cash flow statement. This function addresses the accounting treatment of stock-based compensation, which is a non-cash expense that reduces net income on the income statement but must be added back when calculating cash flow from operations.

Key Characteristics:

-
Appears in operating activities section of cash flow statement

-
Added back to net income when calculating cash from operations

-
Reconciles the non-cash expense from the income statement

-
No actual cash leaves the company for this expense

Key Differences

| Aspect | StkOptExp | StkOptCF |
| Financial Statement | Income Statement | Cash Flow Statement |
| Impact | Reduces net income | Increases operating cash flow |
| Purpose | Shows economic cost to shareholders | Adjusts for non-cash charge |
| Direction | Expense (negative) | Add-back (positive) |

Practical Applications

Financial Analysis Uses

-
Profitability Analysis: Use StkOptExp to understand true operating costs including dilution

-
Cash Flow Analysis: Use StkOptCF to calculate actual cash generation

-
Valuation Models: Both factors needed for accurate DCF and earnings adjustments

-
Peer Comparison: Compare compensation structures and their financial impacts

Common Analytical Adjustments

-
Adjusted EBITDA: Often adds back StkOptExp to show earnings before this non-cash charge

-
Free Cash Flow: StkOptCF ensures FCF reflects actual cash available

-
Non-GAAP Earnings: Companies may exclude StkOptExp from adjusted earnings metrics

-
Return on Capital: Consider whether to include StkOptExp in operating income calculations

Important Relationships

Expected Relationship

-
Over time, StkOptCF and StkOptExp should converge, but may differ in any given period due to grant timing, forfeitures, or classification nuances

-
Both represent the same economic transaction from different perspectives

-
Analysts often expect alignment, but timing mismatches can confuse without understanding these potential differences

Potential Differences

-
Timing: Recognition differences between statements

-
Classification: Expenses may be allocated differently

-
Tax Effects: Tax benefits may create variations

-
Forfeitures: Changes in forfeiture estimates affect amounts

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `StkOptCFQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Latest Quarter |
| `StkOptCFPQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Previous Quarter |
| `StkOptCFPYQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Previous Quarter 1 Year Ago |
| `StkOptCFTTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Trailing 12 Months |
| `StkOptCFPTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Previous Trailing 12 Months |
| `StkOptCFA` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Latest Year |
| `StkOptCFPY` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Previous Year |
| `StkOptCFGr%PQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Q vs Previous Q Growth |
| `StkOptCFGr%PYQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Q vs 1 year ago Q Growth |
| `StkOptCFGr%TTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Trailing Twelve Months Growth |
| `StkOptCFGr%PQTTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Trailing Twelve Months Growth 1Q Ago |
| `StkOptCFGr%A` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Growth Annual |
| `StkOptCFGr%3Y` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Three Year Annualized Growth |
| `StkOptCFGr%5Y` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Five Year Annualized Growth |
| `StkOptCFGr%10Y` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Ten Year Annualized Growth |
| `StkOptCFRSD%ANN` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Ten Year Relative Standard Deviation |
| `StkOptCFRSD%TTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Five Year Relative Standard Deviation |
| `StkOptCFRegEstANN` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Ten Year Regression Estimate |
| `StkOptCFRegEstTTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Five Year Regression Estimate |
| `StkOptCFRegGr%ANN` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Ten Year Regression Estimate |
| `StkOptCFRegGr%TTM` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Five Year Regression Growth |
| `StkOptCFPSQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Quarterly Per Share |
| `StkOptCFPSA` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Annual Per Share |
| `StkOptCF%SalesQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | % of Quarterly Sales |
| `StkOptCF%SalesA` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | % of Annual Sales |
| `StkOptCF%AssetsQ` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | % of Quarterly Assets |
| `StkOptCF%AssetsA` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | % of Annual Assets |
| `StkOptCF3YAvg` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Three Year Average |
| `StkOptCF5YAvg` | Cashflow statement SBC. Data begins around 2006, with full annual coverage starting in 2013, and interim in 2021 | Five Year Average |

### Investing

#### `Acquis(offset, type[, NAHandling])`
```p123
Acquis(offset, type[, NAHandling])
```

Acquisitions is a line representing the cash outflow of funds in the current year, or a carryover from the prior year, for the purchase of companies.

This line is actually an amalgam of various other possible lines, including the acquisition of equity ownership (including in companies already accounted for as non-controlling interest), long-term debt or property plant and equipment.

Users should be cautious when using this together with other line items that they are not double accounting. Note also that this is not a net function; divestures is available as a separate function.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `AcquisQ` | Cash outflows for purchasing companies or equity stakes. | Latest Quarter |
| `AcquisPQ` | Cash outflows for purchasing companies or equity stakes. | Previous Quarter |
| `AcquisPYQ` | Cash outflows for purchasing companies or equity stakes. | Previous Quarter 1 Year Ago |
| `AcquisTTM` | Cash outflows for purchasing companies or equity stakes. | Trailing 12 Months |
| `AcquisPTM` | Cash outflows for purchasing companies or equity stakes. | Previous Trailing 12 Months |
| `AcquisA` | Cash outflows for purchasing companies or equity stakes. | Latest Year |
| `AcquisPY` | Cash outflows for purchasing companies or equity stakes. | Previous Year |
| `AcquisGr%PQ` | Cash outflows for purchasing companies or equity stakes. | Q vs Previous Q Growth |
| `AcquisGr%PYQ` | Cash outflows for purchasing companies or equity stakes. | Q vs 1 year ago Q Growth |
| `AcquisGr%TTM` | Cash outflows for purchasing companies or equity stakes. | Trailing Twelve Months Growth |
| `AcquisGr%PQTTM` | Cash outflows for purchasing companies or equity stakes. | Trailing Twelve Months Growth 1Q Ago |
| `AcquisGr%A` | Cash outflows for purchasing companies or equity stakes. | Growth Annual |
| `AcquisGr%3Y` | Cash outflows for purchasing companies or equity stakes. | Three Year Annualized Growth |
| `AcquisGr%5Y` | Cash outflows for purchasing companies or equity stakes. | Five Year Annualized Growth |
| `AcquisGr%10Y` | Cash outflows for purchasing companies or equity stakes. | Ten Year Annualized Growth |
| `AcquisRSD%ANN` | Cash outflows for purchasing companies or equity stakes. | Ten Year Relative Standard Deviation |
| `AcquisRSD%TTM` | Cash outflows for purchasing companies or equity stakes. | Five Year Relative Standard Deviation |
| `AcquisRegEstANN` | Cash outflows for purchasing companies or equity stakes. | Ten Year Regression Estimate |
| `AcquisRegEstTTM` | Cash outflows for purchasing companies or equity stakes. | Five Year Regression Estimate |
| `AcquisRegGr%ANN` | Cash outflows for purchasing companies or equity stakes. | Ten Year Regression Estimate |
| `AcquisRegGr%TTM` | Cash outflows for purchasing companies or equity stakes. | Five Year Regression Growth |
| `AcquisPSQ` | Cash outflows for purchasing companies or equity stakes. | Quarterly Per Share |
| `AcquisPSA` | Cash outflows for purchasing companies or equity stakes. | Annual Per Share |
| `Acquis%SalesQ` | Cash outflows for purchasing companies or equity stakes. | % of Quarterly Sales |
| `Acquis%SalesA` | Cash outflows for purchasing companies or equity stakes. | % of Annual Sales |
| `Acquis%AssetsQ` | Cash outflows for purchasing companies or equity stakes. | % of Quarterly Assets |
| `Acquis%AssetsA` | Cash outflows for purchasing companies or equity stakes. | % of Annual Assets |
| `Acquis3YAvg` | Cash outflows for purchasing companies or equity stakes. | Three Year Average |
| `Acquis5YAvg` | Cash outflows for purchasing companies or equity stakes. | Five Year Average |

#### `CapEx(offset, type[, NAHandling])`
```p123
CapEx(offset, type[, NAHandling])
```

Capital Expenditures is the amount of cash spent on purchases of property, plant and equipment in the period. Generally, a higher number is desired because it can indicate that the company is investing capital for future growth. To calculate per share value it is divided by the fully-diluted (where available) average shares outstanding for the same period

CapExPS: CapeEx / SharesFD

NOTE: CapitalIQ specifically excludes property, plant and equipment from acquisitions from this line.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Formula**
```p123
CapEx: Straight from filing Line-Item
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CapExQ` | Expenditures on property, plant, and equipment investments. | Latest Quarter |
| `CapExPQ` | Expenditures on property, plant, and equipment investments. | Previous Quarter |
| `CapExPYQ` | Expenditures on property, plant, and equipment investments. | Previous Quarter 1 Year Ago |
| `CapExTTM` | Expenditures on property, plant, and equipment investments. | Trailing 12 Months |
| `CapExPTM` | Expenditures on property, plant, and equipment investments. | Previous Trailing 12 Months |
| `CapExA` | Expenditures on property, plant, and equipment investments. | Latest Year |
| `CapExPY` | Expenditures on property, plant, and equipment investments. | Previous Year |
| `CapExGr%PQ` | Expenditures on property, plant, and equipment investments. | Q vs Previous Q Growth |
| `CapExGr%PYQ` | Expenditures on property, plant, and equipment investments. | Q vs 1 year ago Q Growth |
| `CapExGr%TTM` | Expenditures on property, plant, and equipment investments. | Trailing Twelve Months Growth |
| `CapExGr%PQTTM` | Expenditures on property, plant, and equipment investments. | Trailing Twelve Months Growth 1Q Ago |
| `CapExGr%A` | Expenditures on property, plant, and equipment investments. | Growth Annual |
| `CapExGr%3Y` | Expenditures on property, plant, and equipment investments. | Three Year Annualized Growth |
| `CapExGr%5Y` | Expenditures on property, plant, and equipment investments. | Five Year Annualized Growth |
| `CapExGr%10Y` | Expenditures on property, plant, and equipment investments. | Ten Year Annualized Growth |
| `CapExRSD%ANN` | Expenditures on property, plant, and equipment investments. | Ten Year Relative Standard Deviation |
| `CapExRSD%TTM` | Expenditures on property, plant, and equipment investments. | Five Year Relative Standard Deviation |
| `CapExRegEstANN` | Expenditures on property, plant, and equipment investments. | Ten Year Regression Estimate |
| `CapExRegEstTTM` | Expenditures on property, plant, and equipment investments. | Five Year Regression Estimate |
| `CapExRegGr%ANN` | Expenditures on property, plant, and equipment investments. | Ten Year Regression Estimate |
| `CapExRegGr%TTM` | Expenditures on property, plant, and equipment investments. | Five Year Regression Growth |
| `CapExPSQ` | Expenditures on property, plant, and equipment investments. | Quarterly Per Share |
| `CapExPSA` | Expenditures on property, plant, and equipment investments. | Annual Per Share |
| `CapEx%SalesQ` | Expenditures on property, plant, and equipment investments. | % of Quarterly Sales |
| `CapEx%SalesA` | Expenditures on property, plant, and equipment investments. | % of Annual Sales |
| `CapEx%AssetsQ` | Expenditures on property, plant, and equipment investments. | % of Quarterly Assets |
| `CapEx%AssetsA` | Expenditures on property, plant, and equipment investments. | % of Annual Assets |
| `CapEx3YAvg` | Expenditures on property, plant, and equipment investments. | Three Year Average |
| `CapEx5YAvg` | Expenditures on property, plant, and equipment investments. | Five Year Average |

#### `CashFrInvest(offset, type[, NAHandling])`
```p123
CashFrInvest(offset, type[, NAHandling])
```

Cash From Investing is the net sum of all investing cash flow items. Together with cash from operating and cash from financing, it is the summary of one of the three main sections of the cash flow statement.

Investing activities include capital expenditures and investments in equities and debt of securities that are not issued by the company.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CashFrInvestQ` | Net cash flows from investing activities. | Latest Quarter |
| `CashFrInvestPQ` | Net cash flows from investing activities. | Previous Quarter |
| `CashFrInvestPYQ` | Net cash flows from investing activities. | Previous Quarter 1 Year Ago |
| `CashFrInvestTTM` | Net cash flows from investing activities. | Trailing 12 Months |
| `CashFrInvestPTM` | Net cash flows from investing activities. | Previous Trailing 12 Months |
| `CashFrInvestA` | Net cash flows from investing activities. | Latest Year |
| `CashFrInvestPY` | Net cash flows from investing activities. | Previous Year |
| `CashFrInvestGr%PQ` | Net cash flows from investing activities. | Q vs Previous Q Growth |
| `CashFrInvestGr%PYQ` | Net cash flows from investing activities. | Q vs 1 year ago Q Growth |
| `CashFrInvestGr%TTM` | Net cash flows from investing activities. | Trailing Twelve Months Growth |
| `CashFrInvestGr%PQTTM` | Net cash flows from investing activities. | Trailing Twelve Months Growth 1Q Ago |
| `CashFrInvestGr%A` | Net cash flows from investing activities. | Growth Annual |
| `CashFrInvestGr%3Y` | Net cash flows from investing activities. | Three Year Annualized Growth |
| `CashFrInvestGr%5Y` | Net cash flows from investing activities. | Five Year Annualized Growth |
| `CashFrInvestGr%10Y` | Net cash flows from investing activities. | Ten Year Annualized Growth |
| `CashFrInvestRSD%ANN` | Net cash flows from investing activities. | Ten Year Relative Standard Deviation |
| `CashFrInvestRSD%TTM` | Net cash flows from investing activities. | Five Year Relative Standard Deviation |
| `CashFrInvestRegEstANN` | Net cash flows from investing activities. | Ten Year Regression Estimate |
| `CashFrInvestRegEstTTM` | Net cash flows from investing activities. | Five Year Regression Estimate |
| `CashFrInvestRegGr%ANN` | Net cash flows from investing activities. | Ten Year Regression Estimate |
| `CashFrInvestRegGr%TTM` | Net cash flows from investing activities. | Five Year Regression Growth |
| `CashFrInvestPSQ` | Net cash flows from investing activities. | Quarterly Per Share |
| `CashFrInvestPSA` | Net cash flows from investing activities. | Annual Per Share |
| `CashFrInvest%SalesQ` | Net cash flows from investing activities. | % of Quarterly Sales |
| `CashFrInvest%SalesA` | Net cash flows from investing activities. | % of Annual Sales |
| `CashFrInvest%AssetsQ` | Net cash flows from investing activities. | % of Quarterly Assets |
| `CashFrInvest%AssetsA` | Net cash flows from investing activities. | % of Annual Assets |
| `CashFrInvest3YAvg` | Net cash flows from investing activities. | Three Year Average |
| `CashFrInvest5YAvg` | Net cash flows from investing activities. | Five Year Average |

#### `Divest(offset, type[, NAHandling])`
```p123
Divest(offset, type[, NAHandling])
```

Divestitures is a line representing the cash inflow of funds in the current year, or a carryover from the prior year, for the sale of companies.

This line is actually an amalgam of various other possible lines, including the divestiture of equity ownership (including in companies already accounted for as non-controlling interest), long-term debt or property plant and equipment.

Users should be cautious when using this together with other line items that they are not double accounting. Note also that this is not a net function; acquisitions is available as a separate function.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DivestQ` | Cash inflow from selling companies/subsidiaries. | Latest Quarter |
| `DivestPQ` | Cash inflow from selling companies/subsidiaries. | Previous Quarter |
| `DivestPYQ` | Cash inflow from selling companies/subsidiaries. | Previous Quarter 1 Year Ago |
| `DivestTTM` | Cash inflow from selling companies/subsidiaries. | Trailing 12 Months |
| `DivestPTM` | Cash inflow from selling companies/subsidiaries. | Previous Trailing 12 Months |
| `DivestA` | Cash inflow from selling companies/subsidiaries. | Latest Year |
| `DivestPY` | Cash inflow from selling companies/subsidiaries. | Previous Year |
| `DivestGr%PQ` | Cash inflow from selling companies/subsidiaries. | Q vs Previous Q Growth |
| `DivestGr%PYQ` | Cash inflow from selling companies/subsidiaries. | Q vs 1 year ago Q Growth |
| `DivestGr%TTM` | Cash inflow from selling companies/subsidiaries. | Trailing Twelve Months Growth |
| `DivestGr%PQTTM` | Cash inflow from selling companies/subsidiaries. | Trailing Twelve Months Growth 1Q Ago |
| `DivestGr%A` | Cash inflow from selling companies/subsidiaries. | Growth Annual |
| `DivestGr%3Y` | Cash inflow from selling companies/subsidiaries. | Three Year Annualized Growth |
| `DivestGr%5Y` | Cash inflow from selling companies/subsidiaries. | Five Year Annualized Growth |
| `DivestGr%10Y` | Cash inflow from selling companies/subsidiaries. | Ten Year Annualized Growth |
| `DivestRSD%ANN` | Cash inflow from selling companies/subsidiaries. | Ten Year Relative Standard Deviation |
| `DivestRSD%TTM` | Cash inflow from selling companies/subsidiaries. | Five Year Relative Standard Deviation |
| `DivestRegEstANN` | Cash inflow from selling companies/subsidiaries. | Ten Year Regression Estimate |
| `DivestRegEstTTM` | Cash inflow from selling companies/subsidiaries. | Five Year Regression Estimate |
| `DivestRegGr%ANN` | Cash inflow from selling companies/subsidiaries. | Ten Year Regression Estimate |
| `DivestRegGr%TTM` | Cash inflow from selling companies/subsidiaries. | Five Year Regression Growth |
| `DivestPSQ` | Cash inflow from selling companies/subsidiaries. | Quarterly Per Share |
| `DivestPSA` | Cash inflow from selling companies/subsidiaries. | Annual Per Share |
| `Divest%SalesQ` | Cash inflow from selling companies/subsidiaries. | % of Quarterly Sales |
| `Divest%SalesA` | Cash inflow from selling companies/subsidiaries. | % of Annual Sales |
| `Divest%AssetsQ` | Cash inflow from selling companies/subsidiaries. | % of Quarterly Assets |
| `Divest%AssetsA` | Cash inflow from selling companies/subsidiaries. | % of Annual Assets |
| `Divest3YAvg` | Cash inflow from selling companies/subsidiaries. | Three Year Average |
| `Divest5YAvg` | Cash inflow from selling companies/subsidiaries. | Five Year Average |

#### `InvstOther(offset, type[, NAHandling])`
```p123
InvstOther(offset, type[, NAHandling])
```

Other Investing Activities is a sum of miscellaneous lines on the investing section of the cash flow statement for the period specified by the type input.

This line could contain any number of items that are not classified elsewhere. The list of things that will not be included is probably shorter: Changes in investing activities; changes in investments; and changes in property, plant and equipment. Things that could be part of this line include changes in real estate investments, foreign exchange currency effects, and costs associated with deconsolidation of subsidiaries.

The number of this line will be positive for increases in investments and negative for decreases.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `InvstOtherQ` | Miscellaneous investing cash flows not classified elsewhere. | Latest Quarter |
| `InvstOtherPQ` | Miscellaneous investing cash flows not classified elsewhere. | Previous Quarter |
| `InvstOtherPYQ` | Miscellaneous investing cash flows not classified elsewhere. | Previous Quarter 1 Year Ago |
| `InvstOtherTTM` | Miscellaneous investing cash flows not classified elsewhere. | Trailing 12 Months |
| `InvstOtherPTM` | Miscellaneous investing cash flows not classified elsewhere. | Previous Trailing 12 Months |
| `InvstOtherA` | Miscellaneous investing cash flows not classified elsewhere. | Latest Year |
| `InvstOtherPY` | Miscellaneous investing cash flows not classified elsewhere. | Previous Year |
| `InvstOtherGr%PQ` | Miscellaneous investing cash flows not classified elsewhere. | Q vs Previous Q Growth |
| `InvstOtherGr%PYQ` | Miscellaneous investing cash flows not classified elsewhere. | Q vs 1 year ago Q Growth |
| `InvstOtherGr%TTM` | Miscellaneous investing cash flows not classified elsewhere. | Trailing Twelve Months Growth |
| `InvstOtherGr%PQTTM` | Miscellaneous investing cash flows not classified elsewhere. | Trailing Twelve Months Growth 1Q Ago |
| `InvstOtherGr%A` | Miscellaneous investing cash flows not classified elsewhere. | Growth Annual |
| `InvstOtherGr%3Y` | Miscellaneous investing cash flows not classified elsewhere. | Three Year Annualized Growth |
| `InvstOtherGr%5Y` | Miscellaneous investing cash flows not classified elsewhere. | Five Year Annualized Growth |
| `InvstOtherGr%10Y` | Miscellaneous investing cash flows not classified elsewhere. | Ten Year Annualized Growth |
| `InvstOtherRSD%ANN` | Miscellaneous investing cash flows not classified elsewhere. | Ten Year Relative Standard Deviation |
| `InvstOtherRSD%TTM` | Miscellaneous investing cash flows not classified elsewhere. | Five Year Relative Standard Deviation |
| `InvstOtherRegEstANN` | Miscellaneous investing cash flows not classified elsewhere. | Ten Year Regression Estimate |
| `InvstOtherRegEstTTM` | Miscellaneous investing cash flows not classified elsewhere. | Five Year Regression Estimate |
| `InvstOtherRegGr%ANN` | Miscellaneous investing cash flows not classified elsewhere. | Ten Year Regression Estimate |
| `InvstOtherRegGr%TTM` | Miscellaneous investing cash flows not classified elsewhere. | Five Year Regression Growth |
| `InvstOtherPSQ` | Miscellaneous investing cash flows not classified elsewhere. | Quarterly Per Share |
| `InvstOtherPSA` | Miscellaneous investing cash flows not classified elsewhere. | Annual Per Share |
| `InvstOther%SalesQ` | Miscellaneous investing cash flows not classified elsewhere. | % of Quarterly Sales |
| `InvstOther%SalesA` | Miscellaneous investing cash flows not classified elsewhere. | % of Annual Sales |
| `InvstOther%AssetsQ` | Miscellaneous investing cash flows not classified elsewhere. | % of Quarterly Assets |
| `InvstOther%AssetsA` | Miscellaneous investing cash flows not classified elsewhere. | % of Annual Assets |
| `InvstOther3YAvg` | Miscellaneous investing cash flows not classified elsewhere. | Three Year Average |
| `InvstOther5YAvg` | Miscellaneous investing cash flows not classified elsewhere. | Five Year Average |

### Financing

#### `CashFrFin(offset, type[, NAHandling])`
```p123
CashFrFin(offset, type[, NAHandling])
```

Cash From Financing is the sum total of all cash flow items from financing activities. Together with cash from operations and cash from investing, it is the summary of one of the three major portions of the cash flow statement.

Financing activities generally includes the issuance and retirement of equity and debt instruments issued by the company.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CashFrFinQ` | Sum of all financing activity cash flows. | Latest Quarter |
| `CashFrFinPQ` | Sum of all financing activity cash flows. | Previous Quarter |
| `CashFrFinPYQ` | Sum of all financing activity cash flows. | Previous Quarter 1 Year Ago |
| `CashFrFinTTM` | Sum of all financing activity cash flows. | Trailing 12 Months |
| `CashFrFinPTM` | Sum of all financing activity cash flows. | Previous Trailing 12 Months |
| `CashFrFinA` | Sum of all financing activity cash flows. | Latest Year |
| `CashFrFinPY` | Sum of all financing activity cash flows. | Previous Year |
| `CashFrFinGr%PQ` | Sum of all financing activity cash flows. | Q vs Previous Q Growth |
| `CashFrFinGr%PYQ` | Sum of all financing activity cash flows. | Q vs 1 year ago Q Growth |
| `CashFrFinGr%TTM` | Sum of all financing activity cash flows. | Trailing Twelve Months Growth |
| `CashFrFinGr%PQTTM` | Sum of all financing activity cash flows. | Trailing Twelve Months Growth 1Q Ago |
| `CashFrFinGr%A` | Sum of all financing activity cash flows. | Growth Annual |
| `CashFrFinGr%3Y` | Sum of all financing activity cash flows. | Three Year Annualized Growth |
| `CashFrFinGr%5Y` | Sum of all financing activity cash flows. | Five Year Annualized Growth |
| `CashFrFinGr%10Y` | Sum of all financing activity cash flows. | Ten Year Annualized Growth |
| `CashFrFinRSD%ANN` | Sum of all financing activity cash flows. | Ten Year Relative Standard Deviation |
| `CashFrFinRSD%TTM` | Sum of all financing activity cash flows. | Five Year Relative Standard Deviation |
| `CashFrFinRegEstANN` | Sum of all financing activity cash flows. | Ten Year Regression Estimate |
| `CashFrFinRegEstTTM` | Sum of all financing activity cash flows. | Five Year Regression Estimate |
| `CashFrFinRegGr%ANN` | Sum of all financing activity cash flows. | Ten Year Regression Estimate |
| `CashFrFinRegGr%TTM` | Sum of all financing activity cash flows. | Five Year Regression Growth |
| `CashFrFinPSQ` | Sum of all financing activity cash flows. | Quarterly Per Share |
| `CashFrFinPSA` | Sum of all financing activity cash flows. | Annual Per Share |
| `CashFrFin%SalesQ` | Sum of all financing activity cash flows. | % of Quarterly Sales |
| `CashFrFin%SalesA` | Sum of all financing activity cash flows. | % of Annual Sales |
| `CashFrFin%AssetsQ` | Sum of all financing activity cash flows. | % of Quarterly Assets |
| `CashFrFin%AssetsA` | Sum of all financing activity cash flows. | % of Annual Assets |
| `CashFrFin3YAvg` | Sum of all financing activity cash flows. | Three Year Average |
| `CashFrFin5YAvg` | Sum of all financing activity cash flows. | Five Year Average |

#### `ChangeDebt(offset, type[, NAHandling])`
```p123
ChangeDebt(offset, type[, NAHandling])
```

ChangeDebt is a total of two CompuStat lines: Debt Issued minus Debt Retired. A positive result means that the company issued more debt than it retired; a negative number means the reverse.

Users should consider that this line could be either positive or negative when evaluating this line in their models.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `ChangeDebtQ` | Net debt activity during the period. | Latest Quarter |
| `ChangeDebtPQ` | Net debt activity during the period. | Previous Quarter |
| `ChangeDebtPYQ` | Net debt activity during the period. | Previous Quarter 1 Year Ago |
| `ChangeDebtTTM` | Net debt activity during the period. | Trailing 12 Months |
| `ChangeDebtPTM` | Net debt activity during the period. | Previous Trailing 12 Months |
| `ChangeDebtA` | Net debt activity during the period. | Latest Year |
| `ChangeDebtPY` | Net debt activity during the period. | Previous Year |
| `ChangeDebtGr%PQ` | Net debt activity during the period. | Q vs Previous Q Growth |
| `ChangeDebtGr%PYQ` | Net debt activity during the period. | Q vs 1 year ago Q Growth |
| `ChangeDebtGr%TTM` | Net debt activity during the period. | Trailing Twelve Months Growth |
| `ChangeDebtGr%PQTTM` | Net debt activity during the period. | Trailing Twelve Months Growth 1Q Ago |
| `ChangeDebtGr%A` | Net debt activity during the period. | Growth Annual |
| `ChangeDebtGr%3Y` | Net debt activity during the period. | Three Year Annualized Growth |
| `ChangeDebtGr%5Y` | Net debt activity during the period. | Five Year Annualized Growth |
| `ChangeDebtGr%10Y` | Net debt activity during the period. | Ten Year Annualized Growth |
| `ChangeDebtRSD%ANN` | Net debt activity during the period. | Ten Year Relative Standard Deviation |
| `ChangeDebtRSD%TTM` | Net debt activity during the period. | Five Year Relative Standard Deviation |
| `ChangeDebtRegEstANN` | Net debt activity during the period. | Ten Year Regression Estimate |
| `ChangeDebtRegEstTTM` | Net debt activity during the period. | Five Year Regression Estimate |
| `ChangeDebtRegGr%ANN` | Net debt activity during the period. | Ten Year Regression Estimate |
| `ChangeDebtRegGr%TTM` | Net debt activity during the period. | Five Year Regression Growth |
| `ChangeDebtPSQ` | Net debt activity during the period. | Quarterly Per Share |
| `ChangeDebtPSA` | Net debt activity during the period. | Annual Per Share |
| `ChangeDebt%SalesQ` | Net debt activity during the period. | % of Quarterly Sales |
| `ChangeDebt%SalesA` | Net debt activity during the period. | % of Annual Sales |
| `ChangeDebt%AssetsQ` | Net debt activity during the period. | % of Quarterly Assets |
| `ChangeDebt%AssetsA` | Net debt activity during the period. | % of Annual Assets |
| `ChangeDebt3YAvg` | Net debt activity during the period. | Three Year Average |
| `ChangeDebt5YAvg` | Net debt activity during the period. | Five Year Average |

#### `ChangeEq(offset, type[, NAHandling])`
```p123
ChangeEq(offset, type[, NAHandling])
```

Change in Equity is a net item reflecting both issuance and retirement of equity instruments. It is positive when the company has issued more equity than it has retired over the period defined by the type input.

This line reflects all possible issuance or retirement of all equity instruments. It includes the issuance or retirement of all share classes, preferred stock and the exercise of options.

Note that this is an aggregate line. Users should be careful not to double account while using it.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `ChangeEqQ` | Net equity activity during the period. | Latest Quarter |
| `ChangeEqPQ` | Net equity activity during the period. | Previous Quarter |
| `ChangeEqPYQ` | Net equity activity during the period. | Previous Quarter 1 Year Ago |
| `ChangeEqTTM` | Net equity activity during the period. | Trailing 12 Months |
| `ChangeEqPTM` | Net equity activity during the period. | Previous Trailing 12 Months |
| `ChangeEqA` | Net equity activity during the period. | Latest Year |
| `ChangeEqPY` | Net equity activity during the period. | Previous Year |
| `ChangeEqGr%PQ` | Net equity activity during the period. | Q vs Previous Q Growth |
| `ChangeEqGr%PYQ` | Net equity activity during the period. | Q vs 1 year ago Q Growth |
| `ChangeEqGr%TTM` | Net equity activity during the period. | Trailing Twelve Months Growth |
| `ChangeEqGr%PQTTM` | Net equity activity during the period. | Trailing Twelve Months Growth 1Q Ago |
| `ChangeEqGr%A` | Net equity activity during the period. | Growth Annual |
| `ChangeEqGr%3Y` | Net equity activity during the period. | Three Year Annualized Growth |
| `ChangeEqGr%5Y` | Net equity activity during the period. | Five Year Annualized Growth |
| `ChangeEqGr%10Y` | Net equity activity during the period. | Ten Year Annualized Growth |
| `ChangeEqRSD%ANN` | Net equity activity during the period. | Ten Year Relative Standard Deviation |
| `ChangeEqRSD%TTM` | Net equity activity during the period. | Five Year Relative Standard Deviation |
| `ChangeEqRegEstANN` | Net equity activity during the period. | Ten Year Regression Estimate |
| `ChangeEqRegEstTTM` | Net equity activity during the period. | Five Year Regression Estimate |
| `ChangeEqRegGr%ANN` | Net equity activity during the period. | Ten Year Regression Estimate |
| `ChangeEqRegGr%TTM` | Net equity activity during the period. | Five Year Regression Growth |
| `ChangeEqPSQ` | Net equity activity during the period. | Quarterly Per Share |
| `ChangeEqPSA` | Net equity activity during the period. | Annual Per Share |
| `ChangeEq%SalesQ` | Net equity activity during the period. | % of Quarterly Sales |
| `ChangeEq%SalesA` | Net equity activity during the period. | % of Annual Sales |
| `ChangeEq%AssetsQ` | Net equity activity during the period. | % of Quarterly Assets |
| `ChangeEq%AssetsA` | Net equity activity during the period. | % of Annual Assets |
| `ChangeEq3YAvg` | Net equity activity during the period. | Three Year Average |
| `ChangeEq5YAvg` | Net equity activity during the period. | Five Year Average |

#### `DivPaid(offset, type[, NAHandling])`
```p123
DivPaid(offset, type[, NAHandling])
```

Dividends Paid is total of dividends paid during a period indicated by the type as reported in the financing section of the cash flow statement.

This is a sum of all dividends in millions paid across all share classes and preferred shares. Per-share dividends are available elsewhere. Debt service is not included.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DivPaidQ` | Total dividends paid across all share classes and preferred shares. | Latest Quarter |
| `DivPaidPQ` | Total dividends paid across all share classes and preferred shares. | Previous Quarter |
| `DivPaidPYQ` | Total dividends paid across all share classes and preferred shares. | Previous Quarter 1 Year Ago |
| `DivPaidTTM` | Total dividends paid across all share classes and preferred shares. | Trailing 12 Months |
| `DivPaidPTM` | Total dividends paid across all share classes and preferred shares. | Previous Trailing 12 Months |
| `DivPaidA` | Total dividends paid across all share classes and preferred shares. | Latest Year |
| `DivPaidPY` | Total dividends paid across all share classes and preferred shares. | Previous Year |
| `DivPaidGr%PQ` | Total dividends paid across all share classes and preferred shares. | Q vs Previous Q Growth |
| `DivPaidGr%PYQ` | Total dividends paid across all share classes and preferred shares. | Q vs 1 year ago Q Growth |
| `DivPaidGr%TTM` | Total dividends paid across all share classes and preferred shares. | Trailing Twelve Months Growth |
| `DivPaidGr%PQTTM` | Total dividends paid across all share classes and preferred shares. | Trailing Twelve Months Growth 1Q Ago |
| `DivPaidGr%A` | Total dividends paid across all share classes and preferred shares. | Growth Annual |
| `DivPaidGr%3Y` | Total dividends paid across all share classes and preferred shares. | Three Year Annualized Growth |
| `DivPaidGr%5Y` | Total dividends paid across all share classes and preferred shares. | Five Year Annualized Growth |
| `DivPaidGr%10Y` | Total dividends paid across all share classes and preferred shares. | Ten Year Annualized Growth |
| `DivPaidRSD%ANN` | Total dividends paid across all share classes and preferred shares. | Ten Year Relative Standard Deviation |
| `DivPaidRSD%TTM` | Total dividends paid across all share classes and preferred shares. | Five Year Relative Standard Deviation |
| `DivPaidRegEstANN` | Total dividends paid across all share classes and preferred shares. | Ten Year Regression Estimate |
| `DivPaidRegEstTTM` | Total dividends paid across all share classes and preferred shares. | Five Year Regression Estimate |
| `DivPaidRegGr%ANN` | Total dividends paid across all share classes and preferred shares. | Ten Year Regression Estimate |
| `DivPaidRegGr%TTM` | Total dividends paid across all share classes and preferred shares. | Five Year Regression Growth |
| `DivPaidPSQ` | Total dividends paid across all share classes and preferred shares. | Quarterly Per Share |
| `DivPaidPSA` | Total dividends paid across all share classes and preferred shares. | Annual Per Share |
| `DivPaid%SalesQ` | Total dividends paid across all share classes and preferred shares. | % of Quarterly Sales |
| `DivPaid%SalesA` | Total dividends paid across all share classes and preferred shares. | % of Annual Sales |
| `DivPaid%AssetsQ` | Total dividends paid across all share classes and preferred shares. | % of Quarterly Assets |
| `DivPaid%AssetsA` | Total dividends paid across all share classes and preferred shares. | % of Annual Assets |
| `DivPaid3YAvg` | Total dividends paid across all share classes and preferred shares. | Three Year Average |
| `DivPaid5YAvg` | Total dividends paid across all share classes and preferred shares. | Five Year Average |

#### `EqIssued(offset, type[, NAHandling])`
```p123
EqIssued(offset, type[, NAHandling])
```

Equity Issued is a line from the financing section of the cash flow statement that indicates the total cash funds received through the issuance of equity instruments created during the period selected with the type input.

This line includes the funds received from all avenues of equity creation; sales, conversions of convertibles and option activation are the primary methods. All equity instruments are included, including all equity share classes and all preferred share issues. Two actions are specifically excluded, though: Issuance of warrants and the sale of stock in subsidiary companies.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `EqIssuedQ` | Cash received from issuing equity instruments. | Latest Quarter |
| `EqIssuedPQ` | Cash received from issuing equity instruments. | Previous Quarter |
| `EqIssuedPYQ` | Cash received from issuing equity instruments. | Previous Quarter 1 Year Ago |
| `EqIssuedTTM` | Cash received from issuing equity instruments. | Trailing 12 Months |
| `EqIssuedPTM` | Cash received from issuing equity instruments. | Previous Trailing 12 Months |
| `EqIssuedA` | Cash received from issuing equity instruments. | Latest Year |
| `EqIssuedPY` | Cash received from issuing equity instruments. | Previous Year |
| `EqIssuedGr%PQ` | Cash received from issuing equity instruments. | Q vs Previous Q Growth |
| `EqIssuedGr%PYQ` | Cash received from issuing equity instruments. | Q vs 1 year ago Q Growth |
| `EqIssuedGr%TTM` | Cash received from issuing equity instruments. | Trailing Twelve Months Growth |
| `EqIssuedGr%PQTTM` | Cash received from issuing equity instruments. | Trailing Twelve Months Growth 1Q Ago |
| `EqIssuedGr%A` | Cash received from issuing equity instruments. | Growth Annual |
| `EqIssuedGr%3Y` | Cash received from issuing equity instruments. | Three Year Annualized Growth |
| `EqIssuedGr%5Y` | Cash received from issuing equity instruments. | Five Year Annualized Growth |
| `EqIssuedGr%10Y` | Cash received from issuing equity instruments. | Ten Year Annualized Growth |
| `EqIssuedRSD%ANN` | Cash received from issuing equity instruments. | Ten Year Relative Standard Deviation |
| `EqIssuedRSD%TTM` | Cash received from issuing equity instruments. | Five Year Relative Standard Deviation |
| `EqIssuedRegEstANN` | Cash received from issuing equity instruments. | Ten Year Regression Estimate |
| `EqIssuedRegEstTTM` | Cash received from issuing equity instruments. | Five Year Regression Estimate |
| `EqIssuedRegGr%ANN` | Cash received from issuing equity instruments. | Ten Year Regression Estimate |
| `EqIssuedRegGr%TTM` | Cash received from issuing equity instruments. | Five Year Regression Growth |
| `EqIssuedPSQ` | Cash received from issuing equity instruments. | Quarterly Per Share |
| `EqIssuedPSA` | Cash received from issuing equity instruments. | Annual Per Share |
| `EqIssued%SalesQ` | Cash received from issuing equity instruments. | % of Quarterly Sales |
| `EqIssued%SalesA` | Cash received from issuing equity instruments. | % of Annual Sales |
| `EqIssued%AssetsQ` | Cash received from issuing equity instruments. | % of Quarterly Assets |
| `EqIssued%AssetsA` | Cash received from issuing equity instruments. | % of Annual Assets |
| `EqIssued3YAvg` | Cash received from issuing equity instruments. | Three Year Average |
| `EqIssued5YAvg` | Cash received from issuing equity instruments. | Five Year Average |

#### `EqPurch(offset, type[, NAHandling])`
```p123
EqPurch(offset, type[, NAHandling])
```

Equity Purchased is a financing cash flow line that is the total paid in outflow relating to equity instruments during a period selected by the type input.

Activities that appear in this line tend to be either the repurchase of equities that become treasury shares or the conversion of convertible securities into equities where the company has to pay for the result. The line specifically excludes the purchase of warrants or the reduction of shares in a subsidiary.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `EqPurchQ` | Cash outflow from equity repurchases. | Latest Quarter |
| `EqPurchPQ` | Cash outflow from equity repurchases. | Previous Quarter |
| `EqPurchPYQ` | Cash outflow from equity repurchases. | Previous Quarter 1 Year Ago |
| `EqPurchTTM` | Cash outflow from equity repurchases. | Trailing 12 Months |
| `EqPurchPTM` | Cash outflow from equity repurchases. | Previous Trailing 12 Months |
| `EqPurchA` | Cash outflow from equity repurchases. | Latest Year |
| `EqPurchPY` | Cash outflow from equity repurchases. | Previous Year |
| `EqPurchGr%PQ` | Cash outflow from equity repurchases. | Q vs Previous Q Growth |
| `EqPurchGr%PYQ` | Cash outflow from equity repurchases. | Q vs 1 year ago Q Growth |
| `EqPurchGr%TTM` | Cash outflow from equity repurchases. | Trailing Twelve Months Growth |
| `EqPurchGr%PQTTM` | Cash outflow from equity repurchases. | Trailing Twelve Months Growth 1Q Ago |
| `EqPurchGr%A` | Cash outflow from equity repurchases. | Growth Annual |
| `EqPurchGr%3Y` | Cash outflow from equity repurchases. | Three Year Annualized Growth |
| `EqPurchGr%5Y` | Cash outflow from equity repurchases. | Five Year Annualized Growth |
| `EqPurchGr%10Y` | Cash outflow from equity repurchases. | Ten Year Annualized Growth |
| `EqPurchRSD%ANN` | Cash outflow from equity repurchases. | Ten Year Relative Standard Deviation |
| `EqPurchRSD%TTM` | Cash outflow from equity repurchases. | Five Year Relative Standard Deviation |
| `EqPurchRegEstANN` | Cash outflow from equity repurchases. | Ten Year Regression Estimate |
| `EqPurchRegEstTTM` | Cash outflow from equity repurchases. | Five Year Regression Estimate |
| `EqPurchRegGr%ANN` | Cash outflow from equity repurchases. | Ten Year Regression Estimate |
| `EqPurchRegGr%TTM` | Cash outflow from equity repurchases. | Five Year Regression Growth |
| `EqPurchPSQ` | Cash outflow from equity repurchases. | Quarterly Per Share |
| `EqPurchPSA` | Cash outflow from equity repurchases. | Annual Per Share |
| `EqPurch%SalesQ` | Cash outflow from equity repurchases. | % of Quarterly Sales |
| `EqPurch%SalesA` | Cash outflow from equity repurchases. | % of Annual Sales |
| `EqPurch%AssetsQ` | Cash outflow from equity repurchases. | % of Quarterly Assets |
| `EqPurch%AssetsA` | Cash outflow from equity repurchases. | % of Annual Assets |
| `EqPurch3YAvg` | Cash outflow from equity repurchases. | Three Year Average |
| `EqPurch5YAvg` | Cash outflow from equity repurchases. | Five Year Average |

#### `DbtLTIssued(offset, type[, NAHandling])`
```p123
DbtLTIssued(offset, type[, NAHandling])
```

Long-Term Debt Issued reflects the cash flow line that indicates the amount of non-current debt issued during the period indicated by the type input.

In general, this line includes issuance of all debt with a maturity date greater than 12-months past the date of the financial statements. If there is ambiguity in the reporting -- if current and long-term debt issuance is combined in a company's report, for example -- then the figure will be included in this line by default.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DbtLTIssuedQ` | Cash inflow from issuing debt with maturity over 12 months. | Latest Quarter |
| `DbtLTIssuedPQ` | Cash inflow from issuing debt with maturity over 12 months. | Previous Quarter |
| `DbtLTIssuedPYQ` | Cash inflow from issuing debt with maturity over 12 months. | Previous Quarter 1 Year Ago |
| `DbtLTIssuedTTM` | Cash inflow from issuing debt with maturity over 12 months. | Trailing 12 Months |
| `DbtLTIssuedPTM` | Cash inflow from issuing debt with maturity over 12 months. | Previous Trailing 12 Months |
| `DbtLTIssuedA` | Cash inflow from issuing debt with maturity over 12 months. | Latest Year |
| `DbtLTIssuedPY` | Cash inflow from issuing debt with maturity over 12 months. | Previous Year |
| `DbtLTIssuedGr%PQ` | Cash inflow from issuing debt with maturity over 12 months. | Q vs Previous Q Growth |
| `DbtLTIssuedGr%PYQ` | Cash inflow from issuing debt with maturity over 12 months. | Q vs 1 year ago Q Growth |
| `DbtLTIssuedGr%TTM` | Cash inflow from issuing debt with maturity over 12 months. | Trailing Twelve Months Growth |
| `DbtLTIssuedGr%PQTTM` | Cash inflow from issuing debt with maturity over 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLTIssuedGr%A` | Cash inflow from issuing debt with maturity over 12 months. | Growth Annual |
| `DbtLTIssuedGr%3Y` | Cash inflow from issuing debt with maturity over 12 months. | Three Year Annualized Growth |
| `DbtLTIssuedGr%5Y` | Cash inflow from issuing debt with maturity over 12 months. | Five Year Annualized Growth |
| `DbtLTIssuedGr%10Y` | Cash inflow from issuing debt with maturity over 12 months. | Ten Year Annualized Growth |
| `DbtLTIssuedRSD%ANN` | Cash inflow from issuing debt with maturity over 12 months. | Ten Year Relative Standard Deviation |
| `DbtLTIssuedRSD%TTM` | Cash inflow from issuing debt with maturity over 12 months. | Five Year Relative Standard Deviation |
| `DbtLTIssuedRegEstANN` | Cash inflow from issuing debt with maturity over 12 months. | Ten Year Regression Estimate |
| `DbtLTIssuedRegEstTTM` | Cash inflow from issuing debt with maturity over 12 months. | Five Year Regression Estimate |
| `DbtLTIssuedRegGr%ANN` | Cash inflow from issuing debt with maturity over 12 months. | Ten Year Regression Estimate |
| `DbtLTIssuedRegGr%TTM` | Cash inflow from issuing debt with maturity over 12 months. | Five Year Regression Growth |
| `DbtLTIssuedPSQ` | Cash inflow from issuing debt with maturity over 12 months. | Quarterly Per Share |
| `DbtLTIssuedPSA` | Cash inflow from issuing debt with maturity over 12 months. | Annual Per Share |
| `DbtLTIssued%SalesQ` | Cash inflow from issuing debt with maturity over 12 months. | % of Quarterly Sales |
| `DbtLTIssued%SalesA` | Cash inflow from issuing debt with maturity over 12 months. | % of Annual Sales |
| `DbtLTIssued%AssetsQ` | Cash inflow from issuing debt with maturity over 12 months. | % of Quarterly Assets |
| `DbtLTIssued%AssetsA` | Cash inflow from issuing debt with maturity over 12 months. | % of Annual Assets |
| `DbtLTIssued3YAvg` | Cash inflow from issuing debt with maturity over 12 months. | Three Year Average |
| `DbtLTIssued5YAvg` | Cash inflow from issuing debt with maturity over 12 months. | Five Year Average |

#### `DbtLTReduced(offset, type[, NAHandling])`
```p123
DbtLTReduced(offset, type[, NAHandling])
```

Long-Term Debt Reduced reflects the cash flow line that indicates the amount of non-current debt retired during the period indicated by the type input.

In general, this line includes retirement of all debt with a maturity date greater than 12-months past the date of the financial statements. If there is ambiguity in the reporting -- if current and long-term debt issuance is combined in a company's report, for example -- then the figure will be included in this line by default.

As debt matures it is moved from the long-term debt line to the current line. That change is part of this cash-flow line. The reclassification of debt that has been pre-paid or that has been converted into equities is also included here.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `DbtLTReducedQ` | Cash outflow from retiring debt with maturity over 12 months. | Latest Quarter |
| `DbtLTReducedPQ` | Cash outflow from retiring debt with maturity over 12 months. | Previous Quarter |
| `DbtLTReducedPYQ` | Cash outflow from retiring debt with maturity over 12 months. | Previous Quarter 1 Year Ago |
| `DbtLTReducedTTM` | Cash outflow from retiring debt with maturity over 12 months. | Trailing 12 Months |
| `DbtLTReducedPTM` | Cash outflow from retiring debt with maturity over 12 months. | Previous Trailing 12 Months |
| `DbtLTReducedA` | Cash outflow from retiring debt with maturity over 12 months. | Latest Year |
| `DbtLTReducedPY` | Cash outflow from retiring debt with maturity over 12 months. | Previous Year |
| `DbtLTReducedGr%PQ` | Cash outflow from retiring debt with maturity over 12 months. | Q vs Previous Q Growth |
| `DbtLTReducedGr%PYQ` | Cash outflow from retiring debt with maturity over 12 months. | Q vs 1 year ago Q Growth |
| `DbtLTReducedGr%TTM` | Cash outflow from retiring debt with maturity over 12 months. | Trailing Twelve Months Growth |
| `DbtLTReducedGr%PQTTM` | Cash outflow from retiring debt with maturity over 12 months. | Trailing Twelve Months Growth 1Q Ago |
| `DbtLTReducedGr%A` | Cash outflow from retiring debt with maturity over 12 months. | Growth Annual |
| `DbtLTReducedGr%3Y` | Cash outflow from retiring debt with maturity over 12 months. | Three Year Annualized Growth |
| `DbtLTReducedGr%5Y` | Cash outflow from retiring debt with maturity over 12 months. | Five Year Annualized Growth |
| `DbtLTReducedGr%10Y` | Cash outflow from retiring debt with maturity over 12 months. | Ten Year Annualized Growth |
| `DbtLTReducedRSD%ANN` | Cash outflow from retiring debt with maturity over 12 months. | Ten Year Relative Standard Deviation |
| `DbtLTReducedRSD%TTM` | Cash outflow from retiring debt with maturity over 12 months. | Five Year Relative Standard Deviation |
| `DbtLTReducedRegEstANN` | Cash outflow from retiring debt with maturity over 12 months. | Ten Year Regression Estimate |
| `DbtLTReducedRegEstTTM` | Cash outflow from retiring debt with maturity over 12 months. | Five Year Regression Estimate |
| `DbtLTReducedRegGr%ANN` | Cash outflow from retiring debt with maturity over 12 months. | Ten Year Regression Estimate |
| `DbtLTReducedRegGr%TTM` | Cash outflow from retiring debt with maturity over 12 months. | Five Year Regression Growth |
| `DbtLTReducedPSQ` | Cash outflow from retiring debt with maturity over 12 months. | Quarterly Per Share |
| `DbtLTReducedPSA` | Cash outflow from retiring debt with maturity over 12 months. | Annual Per Share |
| `DbtLTReduced%SalesQ` | Cash outflow from retiring debt with maturity over 12 months. | % of Quarterly Sales |
| `DbtLTReduced%SalesA` | Cash outflow from retiring debt with maturity over 12 months. | % of Annual Sales |
| `DbtLTReduced%AssetsQ` | Cash outflow from retiring debt with maturity over 12 months. | % of Quarterly Assets |
| `DbtLTReduced%AssetsA` | Cash outflow from retiring debt with maturity over 12 months. | % of Annual Assets |
| `DbtLTReduced3YAvg` | Cash outflow from retiring debt with maturity over 12 months. | Three Year Average |
| `DbtLTReduced5YAvg` | Cash outflow from retiring debt with maturity over 12 months. | Five Year Average |

### Summary

#### `CashFl(offset, type[, NAHandling])`
```p123
CashFl(offset, type[, NAHandling])
```

Cash Flow is defined as the sum of Income After Taxes minus Preferred Dividends and Depreciation and Amortization. To calculate per share it is divided by the fully-diluted (where available) average shares outstanding for the same period.

CashFlPS = CashFl / SharesFD

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Formula**
```p123
CashFl = GetDepAndAmort + NetIncCFStmt
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `CashFlQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Latest Quarter |
| `CashFlPQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Previous Quarter |
| `CashFlPYQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Previous Quarter 1 Year Ago |
| `CashFlTTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Trailing 12 Months |
| `CashFlPTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Previous Trailing 12 Months |
| `CashFlA` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Latest Year |
| `CashFlPY` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Previous Year |
| `CashFlGr%PQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Q vs Previous Q Growth |
| `CashFlGr%PYQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Q vs 1 year ago Q Growth |
| `CashFlGr%TTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Trailing Twelve Months Growth |
| `CashFlGr%PQTTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Trailing Twelve Months Growth 1Q Ago |
| `CashFlGr%A` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Growth Annual |
| `CashFlGr%3Y` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Three Year Annualized Growth |
| `CashFlGr%5Y` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Five Year Annualized Growth |
| `CashFlGr%10Y` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Ten Year Annualized Growth |
| `CashFlRSD%ANN` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Ten Year Relative Standard Deviation |
| `CashFlRSD%TTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Five Year Relative Standard Deviation |
| `CashFlRegEstANN` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Ten Year Regression Estimate |
| `CashFlRegEstTTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Five Year Regression Estimate |
| `CashFlRegGr%ANN` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Ten Year Regression Estimate |
| `CashFlRegGr%TTM` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Five Year Regression Growth |
| `CashFlPSQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Quarterly Per Share |
| `CashFlPSA` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Annual Per Share |
| `CashFl%SalesQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | % of Quarterly Sales |
| `CashFl%SalesA` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | % of Annual Sales |
| `CashFl%AssetsQ` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | % of Quarterly Assets |
| `CashFl%AssetsA` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | % of Annual Assets |
| `CashFl3YAvg` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Three Year Average |
| `CashFl5YAvg` | Income After Taxes - Preferred Dividends + Depreciation & Amortization | Five Year Average |

#### `FCF(offset, type[, NAHandling])`
```p123
FCF(offset, type[, NAHandling])
```

Free cash flow represents the cash a company generates after accounting for cash outflows to support operations and maintain its capital assets. Unlike earnings or net income, free cash flow is a measure of profitability that excludes the non-cash expenses of the income statement and includes spending on equipment and assets as well as changes in working capital from the balance sheet. It is calculated as cash from operations less capital expenditures.

Free cash flow represents the cash flow available for the company to repay creditors or pay dividends.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Formula**
```p123
OperCashFl - CapEx
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `FCFQ` | Cash generated after accounting for operational support and capital asset maintenance. | Latest Quarter |
| `FCFPQ` | Cash generated after accounting for operational support and capital asset maintenance. | Previous Quarter |
| `FCFPYQ` | Cash generated after accounting for operational support and capital asset maintenance. | Previous Quarter 1 Year Ago |
| `FCFTTM` | Cash generated after accounting for operational support and capital asset maintenance. | Trailing 12 Months |
| `FCFPTM` | Cash generated after accounting for operational support and capital asset maintenance. | Previous Trailing 12 Months |
| `FCFA` | Cash generated after accounting for operational support and capital asset maintenance. | Latest Year |
| `FCFPY` | Cash generated after accounting for operational support and capital asset maintenance. | Previous Year |
| `FCFGr%PQ` | Cash generated after accounting for operational support and capital asset maintenance. | Q vs Previous Q Growth |
| `FCFGr%PYQ` | Cash generated after accounting for operational support and capital asset maintenance. | Q vs 1 year ago Q Growth |
| `FCFGr%TTM` | Cash generated after accounting for operational support and capital asset maintenance. | Trailing Twelve Months Growth |
| `FCFGr%PQTTM` | Cash generated after accounting for operational support and capital asset maintenance. | Trailing Twelve Months Growth 1Q Ago |
| `FCFGr%A` | Cash generated after accounting for operational support and capital asset maintenance. | Growth Annual |
| `FCFGr%3Y` | Cash generated after accounting for operational support and capital asset maintenance. | Three Year Annualized Growth |
| `FCFGr%5Y` | Cash generated after accounting for operational support and capital asset maintenance. | Five Year Annualized Growth |
| `FCFGr%10Y` | Cash generated after accounting for operational support and capital asset maintenance. | Ten Year Annualized Growth |
| `FCFRSD%ANN` | Cash generated after accounting for operational support and capital asset maintenance. | Ten Year Relative Standard Deviation |
| `FCFRSD%TTM` | Cash generated after accounting for operational support and capital asset maintenance. | Five Year Relative Standard Deviation |
| `FCFRegEstANN` | Cash generated after accounting for operational support and capital asset maintenance. | Ten Year Regression Estimate |
| `FCFRegEstTTM` | Cash generated after accounting for operational support and capital asset maintenance. | Five Year Regression Estimate |
| `FCFRegGr%ANN` | Cash generated after accounting for operational support and capital asset maintenance. | Ten Year Regression Estimate |
| `FCFRegGr%TTM` | Cash generated after accounting for operational support and capital asset maintenance. | Five Year Regression Growth |
| `FCFPSQ` | Cash generated after accounting for operational support and capital asset maintenance. | Quarterly Per Share |
| `FCFPSA` | Cash generated after accounting for operational support and capital asset maintenance. | Annual Per Share |
| `FCF%SalesQ` | Cash generated after accounting for operational support and capital asset maintenance. | % of Quarterly Sales |
| `FCF%SalesA` | Cash generated after accounting for operational support and capital asset maintenance. | % of Annual Sales |
| `FCF%AssetsQ` | Cash generated after accounting for operational support and capital asset maintenance. | % of Quarterly Assets |
| `FCF%AssetsA` | Cash generated after accounting for operational support and capital asset maintenance. | % of Annual Assets |
| `FCF3YAvg` | Cash generated after accounting for operational support and capital asset maintenance. | Three Year Average |
| `FCF5YAvg` | Cash generated after accounting for operational support and capital asset maintenance. | Five Year Average |

#### `NetChgCash(offset, type[, NAHandling])`
```p123
NetChgCash(offset, type[, NAHandling])
```

Net Change in Cash Position is the total change to the cash position of the balance sheet for the period identified by the type input.

This is the grand total of the entire cash flow statement. It is positive for an increase in cash and negative for a decrease.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |
| `NAHandling` | Optional. Controls missing values in preliminary reports: FALLBACK (default, pull the prior period's value), KEEPNA (preserve the NA), or ZERONA (convert the NA to 0). |

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetChgCashQ` | Total change in cash for the period. | Latest Quarter |
| `NetChgCashPQ` | Total change in cash for the period. | Previous Quarter |
| `NetChgCashPYQ` | Total change in cash for the period. | Previous Quarter 1 Year Ago |
| `NetChgCashTTM` | Total change in cash for the period. | Trailing 12 Months |
| `NetChgCashPTM` | Total change in cash for the period. | Previous Trailing 12 Months |
| `NetChgCashA` | Total change in cash for the period. | Latest Year |
| `NetChgCashPY` | Total change in cash for the period. | Previous Year |
| `NetChgCashGr%PQ` | Total change in cash for the period. | Q vs Previous Q Growth |
| `NetChgCashGr%PYQ` | Total change in cash for the period. | Q vs 1 year ago Q Growth |
| `NetChgCashGr%TTM` | Total change in cash for the period. | Trailing Twelve Months Growth |
| `NetChgCashGr%PQTTM` | Total change in cash for the period. | Trailing Twelve Months Growth 1Q Ago |
| `NetChgCashGr%A` | Total change in cash for the period. | Growth Annual |
| `NetChgCashGr%3Y` | Total change in cash for the period. | Three Year Annualized Growth |
| `NetChgCashGr%5Y` | Total change in cash for the period. | Five Year Annualized Growth |
| `NetChgCashGr%10Y` | Total change in cash for the period. | Ten Year Annualized Growth |
| `NetChgCashRSD%ANN` | Total change in cash for the period. | Ten Year Relative Standard Deviation |
| `NetChgCashRSD%TTM` | Total change in cash for the period. | Five Year Relative Standard Deviation |
| `NetChgCashRegEstANN` | Total change in cash for the period. | Ten Year Regression Estimate |
| `NetChgCashRegEstTTM` | Total change in cash for the period. | Five Year Regression Estimate |
| `NetChgCashRegGr%ANN` | Total change in cash for the period. | Ten Year Regression Estimate |
| `NetChgCashRegGr%TTM` | Total change in cash for the period. | Five Year Regression Growth |
| `NetChgCashPSQ` | Total change in cash for the period. | Quarterly Per Share |
| `NetChgCashPSA` | Total change in cash for the period. | Annual Per Share |
| `NetChgCash%SalesQ` | Total change in cash for the period. | % of Quarterly Sales |
| `NetChgCash%SalesA` | Total change in cash for the period. | % of Annual Sales |
| `NetChgCash%AssetsQ` | Total change in cash for the period. | % of Quarterly Assets |
| `NetChgCash%AssetsA` | Total change in cash for the period. | % of Annual Assets |
| `NetChgCash3YAvg` | Total change in cash for the period. | Three Year Average |
| `NetChgCash5YAvg` | Total change in cash for the period. | Five Year Average |

#### `NetFCF(offset, type)`
```p123
NetFCF(offset, type)
```

Net free cash flow represents the cash a company generates after accounting for cash outflows to support operations, maintain its capital assets and maintaining the current level of dividend distribution. Unlike earnings or net income, free cash flow is a measure of profitability that excludes the non-cash expenses of the income statement and includes spending on equipment and assets as well as changes in working capital from the balance sheet. It is calculated as cash from operations less capital expenditures less dividends paid.

Net Free cash flow represents the cash flow available for the company to repay creditors or increase dividends.

| Parameter | Description |
|---|---|
| `offset` | Period offset: 0 is the most recent, 1 the prior period, and so on (0-24 for interim QTR/TTM, 0-19 for annual). |
| `type` | Period type: QTR (interim quarter), ANN (annual), or TTM (trailing twelve months). |

**Formula**
```p123
OperCashFl - CapEx - DivPaid
```

**Pre-built factors**

| Factor | Description | Period |
|---|---|---|
| `NetFCFQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Latest Quarter |
| `NetFCFPQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Previous Quarter |
| `NetFCFPYQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Previous Quarter 1 Year Ago |
| `NetFCFTTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Trailing 12 Months |
| `NetFCFPTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Previous Trailing 12 Months |
| `NetFCFA` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Latest Year |
| `NetFCFPY` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Previous Year |
| `NetFCFGr%PQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Q vs Previous Q Growth |
| `NetFCFGr%PYQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Q vs 1 year ago Q Growth |
| `NetFCFGr%TTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Trailing Twelve Months Growth |
| `NetFCFGr%PQTTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Trailing Twelve Months Growth 1Q Ago |
| `NetFCFGr%A` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Growth Annual |
| `NetFCFGr%3Y` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Three Year Annualized Growth |
| `NetFCFGr%5Y` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Five Year Annualized Growth |
| `NetFCFGr%10Y` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Ten Year Annualized Growth |
| `NetFCFRSD%ANN` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Ten Year Relative Standard Deviation |
| `NetFCFRSD%TTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Five Year Relative Standard Deviation |
| `NetFCFRegEstANN` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Ten Year Regression Estimate |
| `NetFCFRegEstTTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Five Year Regression Estimate |
| `NetFCFRegGr%ANN` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Ten Year Regression Estimate |
| `NetFCFRegGr%TTM` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Five Year Regression Growth |
| `NetFCFPSQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Quarterly Per Share |
| `NetFCFPSA` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Annual Per Share |
| `NetFCF%SalesQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | % of Quarterly Sales |
| `NetFCF%SalesA` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | % of Annual Sales |
| `NetFCF%AssetsQ` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | % of Quarterly Assets |
| `NetFCF%AssetsA` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | % of Annual Assets |
| `NetFCF3YAvg` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Three Year Average |
| `NetFCF5YAvg` | Cash generated after supporting operations, maintaining capital assets, and paying dividends. | Five Year Average |

## Appendix: Vendor Line-Item Mapping

Mapping of Portfolio123 functions to their Compustat and FactSet equivalents, from the official Line-Item Reference Spreadsheet ("Line Items," as of 7/28/2025). Rows are grouped by financial statement. Every Portfolio123 function listed is verified present in the factor dictionary.

### Income Statement (mapping)

| Item | Compustat | FactSet | P123 Function |
|---|---|---|---|
| Sales | SALE | ff_sales | `Sales` |
| Sales International (Annual data only) | — | ff_sales_intl | `SalesIntl` |
| Cost of Goods Sold | COGS | ff_cogs_xdep | `CostG` |
| Gross Profit | SALE - COGS | ff_sales - ff_cogs_xdep | `GrossProfit` |
| Sales General and Administrative Expense | XSGA - XRD | ff_sga - ff_rd_exp | `SGandA` |
| Research and Development expense | XRD | ff_rd_exp | `RandD` |
| Operating Income Before Depreciation | OIBDP | ff_oper_inc_bef_dep | `OpIncBDepr` |
| Amortization of Intangibles | AM | ff_amort_intang | `Amort` |
| Impairment Charges | — | ff_impair | `Impair` |
| Depreciation and Amortization - Total | DP | ff_dep_amort_exp | `DepAmort` |
| Operating Income After Depreciation | OIADP | IsNA(ff_ebit_oper, ff_oper_inc) | `OpIncAftDepr` |
| Interest Expense | XINT | ff_int_exp_debt | `IntExp` |
| Interest Income | IDIT | ff_int_inc | `IntInc` |
| Non-Operating Expenses | NOPI | ff_non_oper_inc | `ExpNonOp` |
| Special Items | SPI | ff_spec_items | `SpcItems` |
| Stock Option Expense (millions) | — | ff_stk_opt_exp | `StkOptExp` |
| Income Before Taxes | PI | ff_ptx_inc | `IncBTax` |
| Income Tax Expense | TXT | ff_inc_tax | `IncTaxExp` |
| Tax Rate, Effective (%) | TXT / PI | ff_inc_tax / ff_ptx_inc | `TxRate%` |
| Income After Taxes | PI - TXT | ff_ptx_inc - ff_inc_tax | `IncAftTax` |
| Net Income Before Extraordinary Items and Non-Controlling Interest | IBMII | Unavailable | `NetIncBXorNonC` |
| Net Income Before Extraordinary Items | IB | ff_net_inc_basic_beft_xord | `NetIncBXor` |
| Preferred Dividends | DVP | ff_div_pfd | `PfdDiv` |
| Income Available to Common Before Extraordinary Items | IBCOM | ff_net_inc_dil | `IncBXorForCom` |
| Income Before Extraordinary Items Adj for Common Share Equivs | IBADJ | Unavailable | `IncBXorAdjCSE` |
| EPS Excluding Extraordinary Items | EPSFX | IsNA(ff_eps, ff_eps_dil, ff_eps_xord, ff_eps_basic) | `EPSExclXor` |
| EPS Including Extraordinary Items | EPSFI | ff_eps_xord | `EPSInclXor` |
| Funds From Operations (millions) | FFO | ff_funds_oper_gross | `FundsFromOp` |

### Balance Sheet (mapping)

| Item | Compustat | FactSet | P123 Function |
|---|---|---|---|
| Cash | CH | ff_cash_only | `Cash` |
| Short Term Investments | IVST | Max(ff_invest_st_tot, ff_trade_acct) | `InvstST` |
| Cash and Equivalents | CHE | See CashEquiv documentation | `CashEquiv` |
| Receivables | RECT | ff_receiv_st | `Recvbl` |
| Inventories Total | INVT | ff_inven | `Inventory` |
| Other Current Assets | ACO | ff_assets_curr_oth | `AstCurOther` |
| Assets, Current | ACT | ff_assets_curr | `AstCur` |
| Gross Plant | PPEGT | ff_ppe_gross | `GrossPlant` |
| Depreciation, Accumulated | DPACT | ff_ppe_dep | `AccumDep` |
| Net Plant | PPENT | ff_ppe_net | `NetPlant` |
| Investments and Advances - Equity | IVAEQ | ff_invest_adv | `InvstEq` |
| Investments and Advances - Other | IVAO | ff_invest_oth | `InvstAdvOther` |
| Goodwill | GDWL | ff_gw | `Goodwill` |
| Intangibles - Other | INTANO | ff_assets_oth_intang | `IntanOther` |
| Intangible Assets | INTAN | IsNA(ff_intang, ff_com_eq - ff_bps_tang * ff_com_shs_out) | `AstIntan` |
| Other Assets | AO | ff_assets_oth | `AstNonCurOther` |
| Assets, Total | AT | ff_assets | `AstTot` |
| Accounts Payable | AP | ff_pay_acct | `Payables` |
| Short-Term Debt | DLC | ff_debt_st | `DbtST` |
| Tax Payable | TXP | ff_pay_tax | `TxPayable` |
| Other Current Liabilities | LCO | ff_liabs_curr_oth | `LiabCurOther` |
| Liabilities, Current | LCT | ff_liabs_curr | `LiabCur` |
| Capital Lease Obligations | — | ff_cap_lease | `CapLease` |
| Long Term Debt | DLTT | ff_debt_lt | `DbtLT` |
| Deferred Taxes and Investment Credits | TXDITC | ff_dfd_tax_cr | `TxDfdIC` |
| Other Liabilities | LO | ff_liabs_oth | `LiabNonCurOther` |
| Liabilities, Total | LT | ff_liabs | `LiabTot` |
| Non-Controlling Interest | MIBT | ff_min_int_accum | `NonControlInt` |
| Preferred Equity | PSTK | ff_pfd_stk | `PfdEquity` |
| Common Equity | CEQ | ff_com_eq | `ComEq` |
| Shareholders Equity | SEQ | ff_shldrs_eq | `EqTot` |
| Accounts Payable - Increase (Decrease) | Unavailable (Use AccruedExp instead) | ff_pay_acct_cf | `PayablesChg` |
| Common Shares Outstanding | CSHO | ff_com_shs_out | `Shares` |
| Retained Earnings | RE | ff_com_eq_retain_earn | `RetainedEarn` |
| Working Capital | ACT - LCT | ff_assets_curr - ff_liabs_curr | `WorkCap` |
| Debt Total | DLTT + DLC | ff_debt_lt + ff_debt_st | `DbtTot` |
| Tangible Book Value | CEQ - INTAN | ff_com_eq - ff_intang | `TanBV` |
| Book Value | CEQ | ff_com_eq | `BookVal` |

### Cash Flow Statement (mapping)

| Item | Compustat | FactSet | P123 Function |
|---|---|---|---|
| Net Income from Cash Flow Statement | IBC | ff_net_inc_cf | `NetIncCFStmt` |
| Depreciation and Amortization from Cash Flow Statement | DPC | ff_dep_exp_cf | `DepAmortCF` |
| Change in Accounts Receivable | RECCH | ff_receiv_cf | `RecvblChg` |
| Inventory Increase (Decrease) | INVCH | ff_inven_cf | `InvtyChg` |
| Change in Accounts Payable and Accrued Liabilities | APALCH | ff_accr_exp_cf | `AccruedExp` |
| Deferred Taxes | TXDC | ff_dfd_tax_xitc_cf | `TxDfd` |
| Change in Accrued Income Taxes | TXACH | ff_pay_tax_cf | `TxAcrudChg` |
| Other Net Working Capital Change | AOLOCH | ff_wkcap_chg | `OtherWCChg` |
| Stock Option Expense | — | ff_stk_opt_cf | `StkOptCF` |
| Operating Cash Flow | OANCF | ff_oper_cf | `OperCashFl` |
| Capital Expenditures | CAPX | ff_capex | `CapEx` |
| Acquisitions | AQC | ff_acq_bus_cf | `Acquis` |
| Divestitures | SPPE | ff_sale_assets_bus_cf | `Divest` |
| Other Investing Activities | IVACO | ff_invest_activ_cf | `InvstOther` |
| Net Cash Flow from Investing Activities | IVNCF | ff_invest_cf | `CashFrInvest` |
| Dividends Paid | DV | ff_div_cf | `DivPaid` |
| Long-Term Debt Issued | DLTIS | ff_debt_lt_iss_cf | `DbtLTIssued` |
| Long-Term Debt Reduced | DLTR | ff_debt_lt_reduct_cf | `DbtLTReduced` |
| Change in Debt | DLTIS - DLTR | ff_debt_lt_iss_cf - ff_debt_lt_reduct_cf | `ChangeDebt` |
| Sale of Common and Preferred Stock | SSTK | ff_stk_sale_cf | `EqIssued` |
| Purchase of Common and Preferred Stock | PRSTKC | ff_stk_purch_cf | `EqPurch` |
| Change in Equity | SSTK - PRSTKC | ff_stk_sale_cf - ff_stk_purch_cf | `ChangeEq` |
| Net Cash Flow from Financing Activities | FINCF | ff_fin_cf | `CashFrFin` |
| Net Change in Cash Position | CHECH | ff_chg_cash_cf | `NetChgCash` |
| Free Cash Flow | OANCF - CAPX | ff_oper_cf - ff_capex | `FCF` |
| Net Free Cash Flow | OANCF - CAPX - DV | ff_oper_cf - ff_capex - ff_div_cf | `NetFCF` |

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `Revenue` | `Sales` | The revenue line item is `Sales`. |
| `NetIncome` | `NetIncBXor` | Net income before extraordinary items is `NetIncBXor`. |
| `TotalAssets` | `AstTot` | Total assets is `AstTot`. |
| `TotalDebt` | `DbtTot` | Total debt is `DbtTot`. |
| `FreeCashFlow` | `FCF` | Free cash flow is `FCF`. |
| `CapitalExpenditures` | `CapEx` | Capital expenditures is `CapEx`. |
| `SharesOutstanding` | `Shares` | Common shares outstanding from the statements is `Shares`; use `SharesCur` for the daily-database figure. |
| `BookValue` | `BookVal` | Book value is `BookVal`. |
| `RetainedEarnings` | `RetainedEarn` | Retained earnings is `RetainedEarn`. |
| `OperatingIncome` | `OpInc` | Operating income is `OpInc`. |
| `GrossMargin` | `GrossProfit` | The gross-profit dollar figure is `GrossProfit`; the margin ratio lives in Ratios & Statistics. |
| `Receivables` | `Recvbl` | Accounts receivable is `Recvbl`. |
| `Inventories` | `Inventory` | Inventory is `Inventory`, singular. |

## See Also

- [Ratios & Statistics](ratios-statistics.md) — valuation, margin, profitability, and financial-strength ratios built on these line items.
- [Estimates](estimates.md) — analyst estimate and revision factors.
- [Fundamentals](fundamentals.md) — company descriptors and per-share/dividend items.
- [Misc](misc.md) — formula-language operators, NA handling, and the `offset`/`type` period system.

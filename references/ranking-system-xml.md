# Ranking System XML — Portfolio123 Reference

> **ALWAYS read this file before generating ranking-system XML.** P123 ranking systems use a
> strict tag hierarchy; the schema and the factor names below were validated against working
> ranking systems and re-verified against the official factor dictionary. Getting a tag or a
> factor name wrong produces an import error or a silently broken node.

This file is standalone: everything needed to write a valid ranking system is here. Factor names
also appear in the category references ([Financials](financials.md),
[Ratios & Statistics](ratios-statistics.md), [Technical](technical.md),
[Estimates](estimates.md)); when in doubt, confirm a name there.

## Contents

- [Critical rules](#critical-rules)
- [Tag Reference](#tag-reference)
- [Scope: Industry vs. Universe](#scope-industry-vs-universe)
- [RankType Direction Quick Reference](#ranktype-direction-quick-reference)
- [Verified Factor Names](#verified-factor-names)
- [Common Formula Expressions](#common-formula-expressions)
- [Worked Example — Penman & Pope](#worked-example--penman--pope)
- [Known Formula Errors to Avoid](#known-formula-errors-to-avoid)
- [See Also](#see-also)

---

## Critical rules

- `<RankingSystem>` is the root node — nothing else can be the root.
- There is no `<RankPerformance>` wrapper; composites sit directly inside `<RankingSystem>`.
- `%` characters in factor names are fine inside `<Factor>` and `<Formula>` tags — do not escape
  them.
- Use `<Composite>` for grouping nodes, never `<SNode>`.
- Use `<StockFactor>` / `<Factor>` for pre-built P123 factors.
- Use `<StockFormula>` / `<Formula>` for custom formula expressions.
- Use `<IndFactor>` / `<Factor>` for industry-level factors.
- Test for missing data with `expression = NA` inside a formula — `IsNA` is a two-argument
  replacement function, not a single-argument boolean (see
  [Known Formula Errors](#known-formula-errors-to-avoid)).

---

## Tag Reference

<!-- name-whitelist: Name RankType Scope Description Weight -->

### `<RankingSystem>`

Root element. Required attribute `RankType="Higher"` (always Higher at the root).

```xml
<RankingSystem RankType="Higher">
  <!-- composites and leaf nodes -->
</RankingSystem>
```

### `<Composite>`

Groups child nodes into a weighted composite; composites may nest.

| Attribute | Values | Notes |
|---|---|---|
| `Name` | any string | Display name in the P123 UI. |
| `Weight` | number | Relative weight within the parent; need not sum to 100 (P123 normalizes). |
| `RankType` | `Higher` / `Lower` | Higher = higher values rank better; Lower = lower values rank better. |

```xml
<Composite Name="Valuation" Weight="30" RankType="Higher">
  <!-- child nodes -->
</Composite>
```

### `<StockFactor>`

Leaf node using a pre-built P123 factor (no formula expression).

| Attribute | Values | Notes |
|---|---|---|
| `Weight` | number | Relative weight within the parent composite. |
| `RankType` | `Higher` / `Lower` | Direction for this factor. |
| `Scope` | `Universe` / `Industry` / `Sector` / `SubIndustry` | Cross-sectional ranking scope. |

Child tag `<Factor>` holds the factor name.

```xml
<StockFactor Weight="50" RankType="Lower" Scope="Industry">
  <Factor>PEExclXorTTM</Factor>
</StockFactor>
```

### `<StockFormula>`

Leaf node using a custom formula expression.

| Attribute | Values | Notes |
|---|---|---|
| `Weight` | number | Relative weight within the parent composite. |
| `RankType` | `Higher` / `Lower` | Direction for this formula. |
| `Name` | any string | Display name in the P123 UI. |
| `Description` | any string | Optional; may be `""`. |
| `Scope` | `Universe` / `Industry` / `Sector` / `SubIndustry` | Cross-sectional ranking scope. |

Child tag `<Formula>` holds the expression.

```xml
<StockFormula Weight="40" RankType="Higher" Name="EBITDA to EV" Description="" Scope="Universe">
  <Formula>OpIncBDeprTTM/EV</Formula>
</StockFormula>
```

### `<IndFactor>`

Leaf node for industry-level factors (industry momentum, etc.).

```xml
<IndFactor Weight="60" RankType="Higher">
  <Factor>Pr52W%ChgInd</Factor>
</IndFactor>
```

---

## Scope: Industry vs. Universe

| Use `Scope="Industry"` | Use `Scope="Universe"` |
|---|---|
| Margins (`OpMgn%TTM`, `GMgn%TTM`) | Absolute valuation (P/E, EV/EBITDA) |
| Asset turnover (`AstTurnTTM`) | Momentum / price ratios |
| Return on capital (`ROI%TTM`, `ROE%TTM`) | Accruals |
| Debt ratios (`DbtTot2CapQ`) | Cash flow quality |
| P/E (to compare within sector) | Forward estimates |

Margins and returns vary structurally by industry, so ranking them within the industry is more
meaningful. Valuation multiples and price momentum are more comparable across the whole universe.

---

## RankType Direction Quick Reference

Each row was spot-checked against the corresponding factor's detail-page or short description in
the category slices.

| Factor / metric | RankType | Reasoning |
|---|---|---|
| P/E ratio | `Lower` | Cheaper is better. |
| EV/EBITDA | `Lower` | Cheaper is better. |
| Price/Book (`Pr2BookQ`) | `Lower` | Cheaper is better. |
| Earnings yield (`1/PEExclXorTTM`) | `Higher` | Higher yield is better. |
| EBITDA/EV (`OpIncBDeprTTM/EV`) | `Higher` | Higher yield is better. |
| ROI / ROE (`ROI%TTM`, `ROE%TTM`) | `Higher` | More profitable is better. |
| Operating margin (`OpMgn%TTM`) | `Higher` | Higher margin is better. |
| Asset turnover (`AstTurnTTM`) | `Higher` | More efficient is better. |
| Accruals | `Lower` | Lower accruals = cleaner earnings. |
| Asset growth | `Lower` | Less aggressive expansion is better. |
| Debt/Capital (`DbtTot2CapQ`) | `Lower` | Less leverage is better. |
| Interest coverage (`IntCovTTM`) | `Higher` | More coverage is better. |
| Price volatility (`PctDev`) | `Lower` | Lower volatility is better. |
| Momentum (price change) | `Higher` | Stronger momentum is better. |
| EPS surprise (`Surprise%Q1`) | `Higher` | Positive surprise is better. |

---

## Verified Factor Names

All names below are confirmed present in the official dictionary. `%` in a name is part of the
name and is used as-is inside `<Factor>` and `<Formula>` tags.

### Valuation (pre-built factors)

| Factor | Description |
|---|---|
| `PEExclXorTTM` | P/E excluding extraordinary items, TTM. |
| `Pr2BookQ` | Price to book (quarterly). |
| `Pr2TanBkQ` | Price to tangible book. |
| `Pr2SalesTTM` | Price to sales, TTM. |
| `EV2SalesTTM` | EV to sales, TTM. |
| `EV2EBITDATTM` | EV/EBITDA, TTM (pre-built); or use `OpIncBDeprTTM/EV` in a formula node. |

### Valuation (formula expressions for `<StockFormula>`)

| Formula | Description |
|---|---|
| `1/PEExclXorTTM` | Earnings yield, TTM. |
| `CurFYEPSMean/Price` | Forward earnings yield. |
| `OpIncBDeprTTM/EV` | EBITDA/EV (yield form). |
| `GrossProfitTTM/EV` | Gross profit to EV. |
| `NetFCFPSTTM/Price` | Free cash flow yield. |
| `(OperCashFlTTM-CapExTTM+0.8*IntExpTTM)/EV` | Unlevered FCF to EV. |
| `(Price*SharesFDQ)/CurFYSalesMean` | Forward price/sales. |

### Profitability

| Factor | Description |
|---|---|
| `ROI%TTM` | Return on investment, TTM. |
| `ROI%5YAvg` | ROI, 5-year average. |
| `ROE%TTM` | Return on equity, TTM. |
| `ROE%5YAvg` | ROE, 5-year average. |
| `OpMgn%TTM` | Operating margin, TTM. |
| `OpMgn%5YAvg` | Operating margin, 5-year average. |
| `GMgn%TTM` | Gross margin, TTM. |
| `GMgn%5YAvg` | Gross margin, 5-year average. |
| `NPMgn%TTM` | Net profit margin, TTM. |
| `AstTurnTTM` | Asset turnover, TTM. |
| `AstTurn5YAvg` | Asset turnover, 5-year average. |

### Quality / Accruals (formula expressions)

| Formula | Description |
|---|---|
| `(NetIncBXorTTM-OperCashFlTTM)/AstTotTTM` | Accruals to total assets (no pre-built accruals factor exists). |
| `Eval(NetIncBXor(0,TTM) = NA OR NetIncBXor(0,TTM)=0, 0, OperCashFlTTM/Abs(NetIncBXor(0,TTM)))` | Cash flow quality. |

### Leverage / Solvency

| Factor | Description |
|---|---|
| `IntCovTTM` | Interest coverage, TTM. |
| `IntCov5YAvg` | Interest coverage, 5-year average. |
| `DbtTotQ` | Total debt, latest quarter. |
| `DbtTotTTM` | Total debt, TTM. |
| `DbtTot2CapQ` | Total debt to capital (quarterly). |
| `DbtTot2EqQ` | Total debt to equity. |
| `AltmanZOrig` | Altman Z-score, public manufacturing (cutoff > 1.81). |
| `AltmanZPriv` | Altman Z-score, private firms. |
| `AltmanZNonManu` | Altman Z-score, non-manufacturing firms. |

### Growth

| Factor | Description |
|---|---|
| `EPSExclXorGr%PYQ` | EPS growth vs. prior-year quarter. |
| `EPSExclXorGr%TTM` | EPS growth, TTM. |
| `EPSExclXorGr%5Y` | EPS growth, 5-year. |
| `SalesGr%PYQ` | Sales growth vs. prior-year quarter. |
| `SalesGr%TTM` | Sales growth, TTM. |
| `SalesGr%5Y` | Sales growth, 5-year. |
| `OpIncGr%PYQ` | Operating income growth vs. prior-year quarter. |
| `OpIncGr%TTM` | Operating income growth, TTM. |
| `OpIncGr%5Y` | Operating income growth, 5-year. |

### Momentum (formula expressions)

| Formula | Description |
|---|---|
| `Close(0)/Close(120)` | 6-month price return. |
| `Close(0)/Close(160)` | 8-month price return. |
| `Close(0)/Close(252)` | 12-month price return. |
| `UpDownRatio(120,0)` | Up/down volume ratio, 120 days. |
| `PctDev(252,1)` | Price volatility, 12 months. |

### Sentiment / Estimates

| Factor | Description |
|---|---|
| `Surprise%Q1` | EPS surprise, most recent quarter. |
| `Surprise%Q2` | EPS surprise, two quarters ago. |
| `AvgRec` | Average analyst recommendation. |

### Sentiment (formula expressions)

| Formula | Description |
|---|---|
| `%(CurFYEPSMean, CurFYEPS4WkAgo)` | EPS estimate revision, current year. |
| `%(CurQEPSMean, CurQEPS4WkAgo)` | EPS estimate revision, current quarter. |
| `CurQEPSStdDev/Abs(CurQEPSMean)` | EPS estimate variability. |
| `AvgRec/AvgRec4WkAgo` | Change in analyst recommendation. |

### Industry Momentum (use `<IndFactor>`)

| Factor | Description |
|---|---|
| `Pr26W%ChgInd` | Industry 26-week price change. |
| `Pr52W%ChgInd` | Industry 52-week price change. |

---

## Common Formula Expressions

P123 cash-flow pre-built factor names drop the function parentheses; the function forms also
exist and take `(offset, type)` arguments.

| Name | Description |
|---|---|
| `OperCashFlTTM` | Operating cash flow, TTM (function form `OperCashFl(0,TTM)`). |
| `CapExTTM` | Capital expenditures, TTM (function form `CapEx(0,TTM)`). |
| `IntExpTTM` | Interest expense, TTM. |
| `GrossProfitTTM` | Gross profit, TTM. |
| `OpIncBDeprTTM` | Operating income before depreciation (EBITDA), TTM. |
| `NetFCFPSTTM` | Net free cash flow per share, TTM. |
| `SharesFDQ` | Fully diluted shares, latest quarter. |
| `SharesFDTTM` | Fully diluted shares, TTM. |
| `Shares(0,QTR)` | Common shares outstanding (function form). |
| `SharesFD(0,QTR)` | Fully diluted shares (function form). |
| `NetIncBXorTTM` | Net income before extraordinary items, TTM (function form `NetIncBXor(0,TTM)`). |
| `AstTotTTM` | Total assets, TTM (function form `AstTot(0,TTM)`). |
| `EV` | Enterprise value. |
| `Price` | Current price. |

---

## Worked Example — Penman & Pope

A five-factor ranking system. Note the cash-flow-quality and asset-growth formulas use
`expression = NA` (not single-argument `IsNA`), and accruals are computed from a formula because
no pre-built accruals factor exists.

```xml
<RankingSystem RankType="Higher">
	<Composite Name="Valuation" Weight="30" RankType="Higher">
		<Composite Name="Earnings Yield" Weight="40" RankType="Higher">
			<StockFormula Weight="60" RankType="Higher" Name="Earnings Yield TTM" Description="" Scope="Universe">
				<Formula>1/PEExclXorTTM</Formula>
			</StockFormula>
			<StockFormula Weight="40" RankType="Higher" Name="Forward Earnings Yield" Description="" Scope="Universe">
				<Formula>CurFYEPSMean/Price</Formula>
			</StockFormula>
		</Composite>
		<Composite Name="Book To Price" Weight="35" RankType="Higher">
			<StockFactor Weight="100" RankType="Lower" Scope="Industry">
				<Factor>Pr2BookQ</Factor>
			</StockFactor>
		</Composite>
		<Composite Name="EV Yield" Weight="25" RankType="Higher">
			<StockFormula Weight="60" RankType="Higher" Name="EBITDA to EV" Description="" Scope="Universe">
				<Formula>OpIncBDeprTTM/EV</Formula>
			</StockFormula>
			<StockFactor Weight="40" RankType="Lower" Scope="Universe">
				<Factor>EV2SalesTTM</Factor>
			</StockFactor>
		</Composite>
	</Composite>
	<Composite Name="Operating Profitability" Weight="30" RankType="Higher">
		<Composite Name="Return on Investment" Weight="40" RankType="Higher">
			<StockFactor Weight="50" RankType="Higher" Scope="Industry">
				<Factor>ROI%TTM</Factor>
			</StockFactor>
			<StockFactor Weight="50" RankType="Higher" Scope="Industry">
				<Factor>ROI%5YAvg</Factor>
			</StockFactor>
		</Composite>
		<Composite Name="Operating Margin" Weight="30" RankType="Higher">
			<StockFactor Weight="60" RankType="Higher" Scope="Industry">
				<Factor>OpMgn%TTM</Factor>
			</StockFactor>
			<StockFactor Weight="40" RankType="Higher" Scope="Industry">
				<Factor>OpMgn%5YAvg</Factor>
			</StockFactor>
		</Composite>
		<Composite Name="Asset Turnover" Weight="30" RankType="Higher">
			<StockFactor Weight="50" RankType="Higher" Scope="Industry">
				<Factor>AstTurnTTM</Factor>
			</StockFactor>
			<StockFactor Weight="50" RankType="Higher" Scope="Industry">
				<Factor>AstTurn5YAvg</Factor>
			</StockFactor>
		</Composite>
	</Composite>
	<Composite Name="Earnings Quality" Weight="20" RankType="Higher">
		<Composite Name="Accruals" Weight="50" RankType="Higher">
			<StockFormula Weight="100" RankType="Lower" Name="Accruals to Assets" Description="" Scope="Universe">
				<Formula>(NetIncBXorTTM-OperCashFlTTM)/AstTotTTM</Formula>
			</StockFormula>
		</Composite>
		<Composite Name="Cash Flow Quality" Weight="50" RankType="Higher">
			<StockFormula Weight="100" RankType="Higher" Name="OpCF to Net Income" Description="" Scope="Universe">
				<Formula>Eval(NetIncBXor(0,TTM) = NA OR NetIncBXor(0,TTM)=0, 0, OperCashFlTTM/Abs(NetIncBXor(0,TTM)))</Formula>
			</StockFormula>
		</Composite>
	</Composite>
	<Composite Name="Investment Risk" Weight="10" RankType="Higher">
		<Composite Name="Asset Growth" Weight="60" RankType="Higher">
			<StockFormula Weight="100" RankType="Lower" Name="Total Asset Growth" Description="" Scope="Universe">
				<Formula>Eval(AstTot(1,TTM) = NA OR AstTot(1,TTM)=0, 0, AstTot(0,TTM)/AstTot(1,TTM)-1)</Formula>
			</StockFormula>
		</Composite>
		<Composite Name="CapEx Intensity" Weight="40" RankType="Higher">
			<StockFormula Weight="100" RankType="Lower" Name="CapEx to Sales" Description="" Scope="Universe">
				<Formula>Eval(Sales(0,TTM) = NA OR Sales(0,TTM)=0, 0, CapExTTM/Sales(0,TTM))</Formula>
			</StockFormula>
		</Composite>
	</Composite>
	<Composite Name="Financial Leverage" Weight="10" RankType="Higher">
		<Composite Name="Interest Coverage" Weight="50" RankType="Higher">
			<StockFactor Weight="60" RankType="Higher" Scope="Universe">
				<Factor>IntCovTTM</Factor>
			</StockFactor>
			<StockFactor Weight="40" RankType="Higher" Scope="Universe">
				<Factor>IntCov5YAvg</Factor>
			</StockFactor>
		</Composite>
		<Composite Name="Debt Load" Weight="50" RankType="Higher">
			<StockFactor Weight="100" RankType="Lower" Scope="Industry">
				<Factor>DbtTot2CapQ</Factor>
			</StockFactor>
		</Composite>
	</Composite>
</RankingSystem>
```

---

## Known Formula Errors to Avoid

Each row was re-validated against the dictionary: the correct name is present and the wrong name
is absent (or, where the wrong token is a real function, the row was dropped from the v2 list and
recorded in the build notes).

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `ROIC%TTM` | `ROI%TTM` | P123 uses ROI, not ROIC, for the pre-built factor. |
| `Accruals%AstTTM` | `(NetIncBXorTTM-OperCashFlTTM)/AstTotTTM` | No pre-built accruals factor; compute it. |
| `AccrualsTTM` | `(NetIncBXorTTM-OperCashFlTTM)/AstTotTTM` | Not a valid factor name; compute accruals from a formula. |
| `OpCashFl(0,TTM)` | `OperCashFl(0,TTM)` | The cash-flow function is `OperCashFl`. |
| `EVToEBITDATTM` | `EV2EBITDATTM` | Correct pre-built name; or use `OpIncBDeprTTM/EV`. |
| `IntCov%TTM` | `IntCovTTM` | No `%` in the interest-coverage factor name. |
| `EarnYield%TTM` | `1/PEExclXorTTM` | No pre-built earnings-yield factor. |
| `<SNode>` | `<Composite>` | Wrong tag; causes a root-node error. |
| `<RankPerformance>` | (omit entirely) | Not part of this schema. |
| `IsNA(NetIncBXor(0,TTM))` | `NetIncBXor(0,TTM) = NA` | `IsNA` is a two-argument replacement function; test for NA with `= NA`. |
| `AltmanZ` | `AltmanZOrig` | Use `AltmanZOrig`, `AltmanZPriv`, or `AltmanZNonManu`. |
| `GrMgn%TTM` | `GMgn%TTM` | Correct pre-built gross-margin name. |
| `NetMgn%TTM` | `NPMgn%TTM` | Correct pre-built net-margin name. |
| `DebtToEqQ` | `DbtTot2EqQ` | Correct debt/equity name. |
| `NetInc(0,TTM)` | `NetIncBXor(0,TTM)` | The plain net-income function does not exist; use `NetIncBXor`. |
| `ShOutDil(0,QTR)` | `SharesFD(0,QTR)` | The diluted-shares function form is `SharesFD`. |
| `ShOutDilQ` | `SharesFDQ` | The diluted-shares pre-built form is `SharesFDQ`. |
| `ShOut(0,QTR)` | `Shares(0,QTR)` | The shares-outstanding function form is `Shares`. |
| `TotDebt` | `DbtTotQ` / `DbtTotTTM` | The total-debt factor names start with `DbtTot`. |

---

## See Also

- [Financials](financials.md) — balance-sheet, income, and cash-flow factor names.
- [Ratios & Statistics](ratios-statistics.md) — valuation, profitability, and growth ratios.
- [Technical](technical.md) — price and momentum formulas for ranking nodes.
- [Advanced Functions](advanced-functions.md) — `FRank`, `ZScore`, and NA handling in formulas.

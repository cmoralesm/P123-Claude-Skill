# P123 Ranking System XML Reference

## Overview

P123 ranking systems are defined in XML using a strict tag hierarchy. This reference
documents the correct schema, validated against working ranking systems.

**Critical rules learned from trial and error:**
- `<RankingSystem>` is the root node — nothing else can be root
- No `<RankPerformance>` wrapper — composites sit directly inside `<RankingSystem>`
- `%` characters in factor names work fine inside `<Factor>` and `<Formula>` tags
- Use `<Composite>` for grouping nodes, never `<SNode>`
- Use `<StockFactor>/<Factor>` for pre-built P123 factors
- Use `<StockFormula>/<Formula>` for custom formula expressions
- Use `<IndFactor>/<Factor>` for industry-level factors

---

## Tag Reference

### `<RankingSystem>`
Root element. Required attribute: `RankType="Higher"` (always Higher at root level).

```xml
<RankingSystem RankType="Higher">
  ...
</RankingSystem>
```

---

### `<Composite>`
Groups child nodes into a weighted composite. Can nest composites inside composites.

**Attributes:**
| Attribute | Values | Notes |
|-----------|--------|-------|
| `Name` | any string | Display name in P123 UI |
| `Weight` | number | Relative weight within parent. Does not need to sum to 100 — P123 normalizes. |
| `RankType` | `"Higher"` / `"Lower"` | Higher = higher values rank better. Lower = lower values rank better. |

```xml
<Composite Name="Valuation" Weight="30" RankType="Higher">
  ...child nodes...
</Composite>
```

---

### `<StockFactor>`
Leaf node using a **pre-built P123 factor** (no formula expression needed).

**Attributes:**
| Attribute | Values | Notes |
|-----------|--------|-------|
| `Weight` | number | Relative weight within parent composite |
| `RankType` | `"Higher"` / `"Lower"` | Direction for this factor |
| `Scope` | `"Universe"` / `"Industry"` / `"Sector"` / `"SubIndustry"` | Cross-sectional ranking scope |

**Child tag:** `<Factor>` containing the P123 factor name.

```xml
<StockFactor Weight="50" RankType="Lower" Scope="Industry">
  <Factor>PEExclXorTTM</Factor>
</StockFactor>
```

---

### `<StockFormula>`
Leaf node using a **custom formula expression**.

**Attributes:**
| Attribute | Values | Notes |
|-----------|--------|-------|
| `Weight` | number | Relative weight within parent composite |
| `RankType` | `"Higher"` / `"Lower"` | Direction for this formula |
| `Name` | any string | Display name in P123 UI |
| `Description` | any string | Optional description, can be `""` |
| `Scope` | `"Universe"` / `"Industry"` / `"Sector"` / `"SubIndustry"` | Cross-sectional ranking scope |

**Child tag:** `<Formula>` containing the P123 formula expression.

```xml
<StockFormula Weight="40" RankType="Higher" Name="EBITDA to EV" Description="" Scope="Universe">
  <Formula>OpIncBDeprTTM/EV</Formula>
</StockFormula>
```

---

### `<IndFactor>`
Leaf node for **industry-level** factors (industry momentum, etc.).

```xml
<IndFactor Weight="60" RankType="Higher">
  <Factor>Pr52W%ChgInd</Factor>
</IndFactor>
```

---

## Scope: When to Use Industry vs Universe

| Use `Scope="Industry"` | Use `Scope="Universe"` |
|------------------------|------------------------|
| Margins (OpMgn, GMgn) | Absolute valuation (P/E, EV/EBITDA) |
| Turnover (AstTurn) | Momentum / price ratios |
| Return on capital (ROI, ROE) | Accruals |
| Debt ratios (DbtTot2CapQ) | Cash flow quality |
| PE ratio (to compare within sector) | Forward estimates |

**Reasoning:** Margins and returns vary structurally by industry. Ranking a retailer's
OpMgn against a software company's is meaningless. Valuation multiples and price
momentum are more meaningful cross-sectionally.

---

## RankType Direction Quick Reference

| Factor | RankType | Reasoning |
|--------|----------|-----------|
| PE ratio | `Lower` | Cheaper is better |
| EV/EBITDA | `Lower` | Cheaper is better |
| P/Book | `Lower` | Cheaper is better |
| Earnings Yield (1/PE) | `Higher` | Higher yield is better |
| EBITDA/EV | `Higher` | Higher yield is better |
| ROI, ROE | `Higher` | More profitable is better |
| Operating Margin | `Higher` | Higher margin is better |
| Asset Turnover | `Higher` | More efficient is better |
| Accruals | `Lower` | Lower accruals = cleaner earnings |
| Asset Growth | `Lower` | Less aggressive expansion is better |
| Debt/Capital | `Lower` | Less leverage is better |
| Interest Coverage | `Higher` | More coverage is better |
| Beta | `Lower` | Lower risk is better |
| Price Volatility | `Lower` | Lower volatility is better |
| Momentum (price change) | `Higher` | Stronger momentum is better |
| EPS Surprise | `Higher` | Positive surprise is better |
| Estimate Revision | `Higher` | Upward revision is better |

---

## Verified Working Factor Names

These have been confirmed to work in P123 XML. Many pre-built factors use `%` in
their names — this is fine inside `<Factor>` tags.

### Valuation
| XML Factor Name | Description |
|----------------|-------------|
| `PEExclXorTTM` | P/E excl. extraordinary items TTM |
| `Pr2BookQ` | Price to book (quarterly) |
| `Pr2TanBkQ` | Price to tangible book |
| `Pr2SalesTTM` | Price to sales TTM |
| `EV2SalesTTM` | EV to sales TTM |
| `EV2EBITDATTM` | EV/EBITDA TTM (pre-built) — use `OpIncBDeprTTM/EV` in formulas for safety |

### Valuation — Formula expressions (use in `<StockFormula>`)
| Formula | Description |
|---------|-------------|
| `1/PEExclXorTTM` | Earnings yield TTM |
| `CurFYEPSMean/Price` | Forward earnings yield |
| `OpIncBDeprTTM/EV` | EBITDA/EV (yields-based) |
| `GrossProfitTTM/EV` | Gross profit to EV |
| `NetFCFPSTTM/Price` | FCF yield |
| `(OperCashFlTTM-CapExTTM+0.8*IntExpTTM)/EV` | Unlevered FCF to EV |
| `(Price*SharesFDQ)/CurFYSalesMean` | Forward P/S |

### Profitability
| XML Factor Name | Description |
|----------------|-------------|
| `ROI%TTM` | Return on investment TTM |
| `ROI%5YAvg` | ROI 5-year average |
| `ROE%TTM` | Return on equity TTM |
| `ROE%5YAvg` | ROE 5-year average |
| `OpMgn%TTM` | Operating margin TTM |
| `OpMgn%5YAvg` | Operating margin 5-year avg |
| `GMgn%TTM` | **Gross margin TTM** (NOT `GrMgn%TTM`) |
| `GMgn%5YAvg` | Gross margin 5-year avg |
| `NPMgn%TTM` | Net profit margin TTM (NOT `NetMgn%TTM`) |
| `AstTurnTTM` | Asset turnover TTM |
| `AstTurn5YAvg` | Asset turnover 5-year avg |

### Quality / Accruals — Formula expressions
| Formula | Description |
|---------|-------------|
| `AccrualsTTM/AstTot(0,TTM)` | Accruals to total assets |
| `Eval(NetIncBXor(0,TTM) = NA OR NetIncBXor(0,TTM)=0, 0, OperCashFlTTM/Abs(NetIncBXor(0,TTM)))` | Cash flow quality |

### Leverage / Solvency
| XML Factor Name | Description |
|----------------|-------------|
| `IntCovTTM` | Interest coverage TTM |
| `IntCov5YAvg` | Interest coverage 5-year avg |
| `DbtTotQ` | **Total debt latest quarter** (NOT `TotDebtQ`) |
| `DbtTotTTM` | Total debt TTM (NOT `TotDebtTTM`) |
| `DbtTot2CapQ` | Total debt to capital (quarterly) |
| `DbtTot2EqQ` | Total debt to equity (NOT `DebtToEqQ`) |
| `AltmanZOrig` | Altman Z-score public manufacturing (NOT `AltmanZ`) — cutoff > 1.81 |
| `AltmanZPriv` | Altman Z-score private firms |
| `AltmanZNonManu` | Altman Z-score non-manufacturing firms |

### Growth
| XML Factor Name | Description |
|----------------|-------------|
| `EPSExclXorGr%PYQ` | EPS growth vs prior year quarter |
| `EPSExclXorGr%TTM` | EPS growth TTM |
| `EPSExclXorGr%5Y` | EPS growth 5-year |
| `SalesGr%PYQ` | Sales growth vs prior year quarter |
| `SalesGr%TTM` | Sales growth TTM |
| `SalesGr%5Y` | Sales growth 5-year |
| `OpIncGr%PYQ` | Operating income growth vs PYQ |
| `OpIncGr%TTM` | Operating income growth TTM |
| `OpIncGr%5Y` | Operating income growth 5-year |

### Momentum — Formula expressions
| Formula | Description |
|---------|-------------|
| `Close(0)/Close(120)` | 6-month price return |
| `Close(0)/Close(160)` | 8-month price return |
| `Close(0)/Close(252)` | 12-month price return |
| `UpDownRatio(120,0)` | Up/down volume ratio 120 days |
| `PctDev(252,1)` | Price volatility 12 months |

### Sentiment / Estimates
| XML Factor Name | Description |
|----------------|-------------|
| `Surprise%Q1` | EPS surprise most recent quarter |
| `Surprise%Q2` | EPS surprise 2 quarters ago |
| `AvgRec` | Average analyst recommendation |

### Sentiment — Formula expressions
| Formula | Description |
|---------|-------------|
| `%(CurFYEPSMean, CurFYEPS4WkAgo)` | EPS estimate revision current year |
| `%(CurQEPSMean, CurQEPS4WkAgo)` | EPS estimate revision current quarter |
| `CurQEPSStdDev/Abs(CurQEPSMean)` | EPS estimate variability |
| `AvgRec/AvgRec4WkAgo` | Change in analyst recommendation |

### Industry Momentum — use `<IndFactor>` tag
| XML Factor Name | Description |
|----------------|-------------|
| `Pr26W%ChgInd` | Industry 26-week price change |
| `Pr52W%ChgInd` | Industry 52-week price change |

---

## Common Formula Expressions (cash flow items)

Note: P123 cash flow pre-built factor names drop parentheses:

| XML Name | Description |
|----------|-------------|
| `OperCashFlTTM` | Operating cash flow TTM (NOT `OpCashFl(0,TTM)`) |
| `CapExTTM` | Capital expenditures TTM (NOT `CapEx(0,TTM)`) |
| `IntExpTTM` | Interest expense TTM |
| `GrossProfitTTM` | Gross profit TTM |
| `OpIncBDeprTTM` | Operating income before depreciation (EBITDA) TTM |
| `NetFCFPSTTM` | Net free cash flow per share TTM |
| `AccrualsTTM` | Accruals TTM |
| `SharesFDQ` | Fully diluted shares latest quarter (NOT `ShOutDilQ`) |
| `SharesFDTTM` | Fully diluted shares TTM (NOT `ShOutDilTTM`) |
| `Shares(0,QTR)` | Common shares outstanding — function form (NOT `ShOut()`) |
| `SharesFD(0,QTR)` | Fully diluted shares — function form (NOT `ShOutDil()`) |
| `EV` | Enterprise value |
| `Price` | Current price |

---

## Full Working Example — Penman & Pope Ranking System

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
				<Formula>AccrualsTTM/AstTot(0,TTM)</Formula>
			</StockFormula>
		</Composite>
		<Composite Name="Cash Flow Quality" Weight="50" RankType="Higher">
			<StockFormula Weight="100" RankType="Higher" Name="OpCF to Net Income" Description="" Scope="Universe">
				<Formula>Eval((NetIncBXor(0,TTM) = NA OR NetIncBXor(0,TTM)=0, 0, OperCashFlTTM/Abs(NetIncBXor(0,TTM)))</Formula>
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

| Wrong | Correct | Note |
|-------|---------|------|
| `ROIC%TTM` | `ROI%TTM` | P123 uses ROI not ROIC as pre-built |
| `ROIC(0,TTM)` | `ROI%TTM` | No function form for ROIC |
| `Accruals%AstTTM` | `AccrualsTTM/AstTot(0,TTM)` | No pre-built accruals ratio |
| `OpCashFl(0,TTM)` | `OperCashFl(0,TTM)` in formulas, `OperCashFlTTM` as pre-built factor in screens | `OpCashFl` is invalid in all contexts |
| `CapEx(0,TTM)` | `CapExTTM` | Pre-built name differs from function |
| `EVToEBITDATTM` | `EV2EBITDATTM` | Correct pre-built name; or use `OpIncBDeprTTM/EV` in formula nodes |
| `IntCov%TTM` | `IntCovTTM` | No % in this pre-built name |
| `IntCov(0,TTM)` | `IntCovTTM` | Use pre-built, not function form |
| `EarnYield%TTM` | `1/PEExclXorTTM` | No pre-built earnings yield factor |
| `AstTurn(0,TTM)` | `AstTurnTTM` | Pre-built name differs from function |
| `<SNode>` | `<Composite>` | Wrong tag — causes root node error |
| `<RankPerformance>` | *(omit entirely)* | Not used in this XML schema |
| `&#37;` | `%` | % does not need escaping in Formula tags |
| `AltmanZ` | `AltmanZOrig` | Invalid — use `AltmanZOrig` (public mfg), `AltmanZPriv`, or `AltmanZNonManu` |
| `GrMgn%TTM` | `GMgn%TTM` | Correct pre-built gross margin factor name |
| `NetMgn%TTM` | `NPMgn%TTM` | Correct pre-built net margin factor name |
| `DebtToEqQ` | `DbtTot2EqQ` | Correct debt/equity factor name |
| `TotDebt(0,QTR)` | `DbtTot(0,QTR)` | `TotDebt` is invalid — use `DbtTot` |
| `NetInc(0,TTM)` | `NetIncBXor(0,TTM)` | Plain `NetInc` does not exist in P123 |
| `ShOutDil(0,QTR)` | `SharesFD(0,QTR)` | `ShOutDil` is invalid — use `SharesFD` |
| `ShOutDilQ` | `SharesFDQ` | `ShOutDil` pre-built form is also invalid |
| `ShOut(0,QTR)` | `Shares(0,QTR)` | `ShOut` is invalid — use `Shares` |
| `TotDebt` | `DbtTotQ` / `DbtTotTTM` / `DbtTotA` | Pre-built names for total debt |

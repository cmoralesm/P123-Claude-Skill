<!-- name-whitelist: RankType Scope StockFactor StockFormula RankingSystem Composite Factor Formula
Description Name Weight Compustat Q A PYQ PTM RSD% RSD%TTM RSD%ANN noBars noNAs -->
# Factor Replication - Portfolio123 Reference

A recipe book, not a literature review. Each row names a well-known anomaly, states its economic
definition in one line, and gives the Portfolio123 implementation: the pre-built factor where one
exists, otherwise the formula. The author-and-year label is a retrieval key - "build me Novy-Marx
gross profitability" - not the subject matter.

**No performance figures appear anywhere in this file, by design.** No alphas, no t-statistics, no
return magnitudes. This skill exists to stop invented facts, and an unverifiable alpha is an
invented fact. Report what a factor *is*, never what it earned.

Every identifier below exists in the extracted Factor Reference dictionary and every formula was
checked with the offline formula validator. Where P123 genuinely cannot express a paper's
construction, the row says so and gives the closest honest proxy instead of faking one. For the
node schema these recipes plug into, read [Ranking System XML](ranking-system-xml.md) first.

## Contents

- [How to read a recipe](#how-to-read-a-recipe)
- [Value](#value)
- [Quality and Profitability](#quality-and-profitability)
- [Earnings Quality and Distress](#earnings-quality-and-distress)
- [Momentum and Revisions](#momentum-and-revisions)
- [Low Risk](#low-risk)
- [Size and Liquidity](#size-and-liquidity)
- [Investment, Issuance and Payout](#investment-issuance-and-payout)
- [Worked Example - Quality Sleeve](#worked-example--quality-sleeve)
- [Where P123 Cannot Match the Paper](#where-p123-cannot-match-the-paper)
- [Two real factors, one right answer](#two-real-factors-one-right-answer)
- [Common Mistakes](#common-mistakes)
- [See Also](#see-also)

---

## How to read a recipe

The **Node** column gives the two ranking-node attributes that decide whether a factor points the
way the construction intended: `RankType` (`Higher` = high values rank best, `Lower` = low values
rank best) and `Scope` (`Universe` = ranked against the whole universe, `Industry` = ranked
against industry peers only).

Scope follows one rule throughout: **quantities that vary structurally by industry are ranked
within the industry; prices and returns are ranked across the universe.** Margins, returns on
capital, asset turnover and leverage are industry-relative. Valuation multiples, momentum,
volatility, accruals and estimate revisions are not. The scope table in
[Ranking System XML](ranking-system-xml.md#scope-industry-vs-universe) lists P/E on both sides -
under Universe as an absolute valuation multiple, under Industry as a within-sector comparison.
This file resolves that one ambiguity in favour of `Scope="Universe"` for every valuation multiple,
and follows the table everywhere else, leverage (`DbtTot2CapQ`) included. Do not invent a third
convention. Where a published sort disagrees with any of it, the recipe says so.

**Prefer the yield form of a valuation ratio.** A negative denominator makes a price multiple
negative, and a negative multiple is the *best* value under `RankType="Lower"`, which silently
promotes loss-makers to the top of a value factor. The inverted yield form ranks them last, which
is what a cross-sectional sort needs.

Period suffixes carry the data frequency. `TTM` covers the last four quarters, `A` the latest
fiscal year, `Q` the latest quarter, `PYQ` the year-ago quarter, `PTM` the prior trailing twelve
months. Constructions built on annual Compustat imply the annual family; anything that must react
inside a year implies the trailing-twelve family. The two families are not interchangeable on the
balance sheet: income and cash-flow items **sum** the trailing four quarters, balance-sheet items
**average** them (see [Financials](financials.md)). That is why `AstTotQ` and `AstTotTTM` are
different denominators.

**Do not add a reporting lag.** P123 is point-in-time: a factor is evaluated with the data that
was public on the as-of date. The six-to-eighteen-month lag academic sorts apply is a substitute
for point-in-time data, not part of the economics. Replicating it with `FHist` throws away
information P123 already handles correctly.

NA behaviour is part of a recipe, not an afterthought. Guard a ratio whose denominator can be zero
or missing with `Eval(expr = NA, ...)` - never with a one-argument `IsNA`, which does not exist.

---

## Value

Valuation is ranked across the universe: the cross-industry spread in multiples is the signal, not
noise to be neutralized.

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| Book-to-market - Fama & French (1992) | Common equity over market value of equity. | `BookValQ / MktCap`, or `Pr2BookQ` ranked `Lower` | `Higher` / Universe |
| Earnings yield - Basu (1977) | Trailing earnings per share over price. | `EarnYield` | `Higher` / Universe |
| Cash-flow yield - Lakonishok, Shleifer & Vishny (1994) | Earnings plus depreciation over market value. | `CashFlTTM / MktCap`, or `Pr2CashFlTTM` ranked `Lower` | `Higher` / Universe |
| Operating-cash-flow yield | Operating cash flow over market cap. | `OCFYield` | `Higher` / Universe |
| Free-cash-flow yield | Free cash flow over market cap. | `FCFYield` | `Higher` / Universe |
| Enterprise multiple | EBITDA over enterprise value. | `EBITDAYield`, or `EV2EBITDATTM` ranked `Lower` | `Higher` / Universe |
| Sales yield | Revenue over market cap. | `SalesTTM / MktCap`, or `Pr2SalesTTM` ranked `Lower` | `Higher` / Universe |

Translation traps:

- **Which book value.** P123 documents `BookVal` as common equity excluding preferred shares and
  minority interests; the academic definition is stockholders' equity plus balance-sheet deferred
  taxes less preferred, so the two differ by the deferred-tax term. Worse, the official detail
  page for `Pr2Book` describes its per-share denominator as "common equity less intangibles" -
  word for word the wording P123 uses for the separate `Pr2TanBkQ` factor. The intangible
  treatment inside `Pr2BookQ` is therefore ambiguous in P123's own documentation. Build
  book-to-market from `BookValQ` when the definition has to be exact; use `Pr2TanBkQ` only when
  the construction explicitly nets out intangibles.
- **Quarterly versus annual book.** `Pr2BookQ` and `BookValQ` use the latest quarter; `Pr2BookA`
  and `BookValA` are the fiscal-year analogues, closer to an annual-Compustat construction.
- **Negative book equity inverts the sort.** A negative ratio ranks at the *top* under `Lower` on
  the multiple. Exclude it with a `BookValQ > 0` universe or screen rule.
- **Losses.** `1/PEExclXorTTM` returns NA for a loss-maker and drops the stock out of the node;
  P123's own detail page for `EarnYield` says it is preferred over P/E precisely because losses
  produce negative yields rather than undefined values. `EarnYield` takes **no period suffix**.
- **The pre-built yields are not on one scale.** `EarnYield` is `100 * EPSExclXorTTM / Price`,
  `OCFYield` is `100 * OperCashFl / MktCap` and `EBITDAYield` is `100 * EBITDATTM / EV` - all
  percentages - but `FCFYield` is documented as `FCFTTM / MktCap`, a plain ratio. Summing them
  inside one formula node mis-weights `FCFYield` by two orders of magnitude. Ranking them as
  separate nodes is unaffected.
- **Two different scalings.** `EBITDAYield`, `OpIncYield` and `EV2SalesTTM` are scaled by
  **enterprise value**; `EarnYield`, `OCFYield`, `FCFYield`, `Pr2SalesTTM` and `ShareholderYield`
  are scaled by **market cap**. Mixing the two inside one composite double-counts leverage.
- **Cash flow is not free cash flow.** P123 defines the `CashFl` line item as income after taxes
  less preferred dividends plus depreciation and amortization - the earnings-plus-depreciation
  definition. `FCFYield` nets out capital expenditure and is a different measure; `OCFYield` is
  the cash-flow-statement alternative and a defensible modern substitute, but not that
  definition either. Pick one and say which.
- **Sales yield has the fewest missing and fewest sign-flipped observations** - revenue is never
  negative - and is the most distorted by capital structure: a heavily indebted firm looks cheap
  on `Pr2SalesTTM` and expensive on `EV2SalesTTM`.

---

## Quality and Profitability

Profitability, margins and returns on capital are ranked within the industry.

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| F-Score - Piotroski (2000) | Nine binary accounting tests summed to 0–9. | `PiotFScore` | `Higher` / Universe |
| Gross profitability - Novy-Marx (2013) | Gross profit over total assets. | `GrossProfitTTM / AstTotQ` | `Higher` / Industry |
| Operating profitability - Fama & French (2015) | Revenue less cost of goods, overheads and interest, over book equity. | `(SalesTTM - CostGTTM - SGandATTM - RandDTTM - IntExpTTM) / BookValQ` | `Higher` / Industry |
| Return on equity and on capital | Profit over common equity, or over total capital. | `ROE%TTM`, `ROI%TTM` | `Higher` / Industry |
| Margin stability | Dispersion of a margin across years. | `OpMgn%RSD%TTM` (five-year), `OpMgn%RSD%ANN` (ten-year) | `Lower` / Industry |

Translation traps:

- **`PiotFScore` is P123's nine tests, not Piotroski's.** The official definition is
  `ROA%TTM > 0`, `OperCashFlTTM > 0`, `ROA%TTM > ROA%PTM`,
  `OperCashFlTTM > NetIncCFStmtTTM`, `DbtTot2AstQ < DbtTot2AstPYQ`, `CurRatioQ > CurRatioPYQ`,
  `SharesQ <= SharesPYQ`, `GMgn%TTM > GMgn%PTM`, `AstTurnTTM > AstTurnPTM`. Four deliberate
  deviations follow: the comparisons are trailing-twelve versus prior-trailing-twelve rather than
  fiscal year versus prior fiscal year; leverage is measured on **total** debt to assets rather
  than long-term debt; `ROA%TTM` is scaled by **average** total assets rather than
  beginning-of-year assets; and the ninth test is "no dilution" on the share count rather than an
  equity-offering indicator. P123's own note says the factor is computed on the fly and will slow
  simulations that lean on it.
- **The score belongs inside the cheap bucket.** The construction applies it to stocks that look
  cheap on price-to-book, not across the whole market. Pair it with a rule such as
  `FRank("Pr2BookQ", #All, #ASC) > 80` rather than ranking the score alone.
- **Novy-Marx denominator.** `GMgn%TTM` is gross profit divided by **sales** - a margin - and
  substituting it is the most common error in this recipe. Scale by `AstTotQ`, the period-end
  balance-sheet value; `AstTotTTM` is the four-quarter **average** and a different number.
  `GrossProfit%AssetsA` is the pre-built annual form, and `GrossProfitA / AstTotA` the explicit
  annual formula.
- **Which gross profit.** `GrossProfit` is `Sales - CostG` and excludes depreciation and
  amortization from cost of goods. `GrossProfit_GAAP` folds D&A back in and is a different
  measure; do not substitute it.
- **Scope on both profitability sorts.** Novy-Marx gross profitability and Fama & French (2015)
  operating profitability are both published as unconditional sorts across the cross-section.
  This file ranks both `Scope="Industry"` to stay consistent with the skill's scope convention for
  returns on assets; `Scope="Universe"` reproduces the published sorts. Say which one you built.
- **`SGandA` excludes R&D.** P123 documents the line item as general/administrative plus selling
  expenses, **excluding** research and development. The operating-profitability formula above adds
  `RandDTTM` back so the overhead deduction is complete; drop that term if the construction you
  are replicating treats R&D as an investment rather than an expense.
- **Book equity versus shareholders' equity.** `BookValQ` is common equity excluding preferred and
  minority interests - the same denominator the book-to-market recipe uses, which keeps a
  value-plus-profitability system internally consistent. `EqTotQ` is total assets less total
  liabilities, i.e. shareholders' equity including preferred; it is the other defensible choice.
  Negative book equity inverts the sign of either.
- **Return denominators are period averages.** `ROE%TTM` is net income before extraordinary items
  over *average* common equity; `ROI%TTM` is net income plus after-tax interest over *average*
  total capital (debt plus equity). A large mid-year acquisition depresses both for a year
  relative to a point-in-time denominator. P123 has no return-on-invested-capital factor under any
  spelling - `ROI%TTM` is the nearest equivalent, see
  [Ranking System XML](ranking-system-xml.md#known-formula-errors-to-avoid).
- **`RSD%` is a *relative* standard deviation**, i.e. dispersion divided by the absolute mean -
  P123 documents the identical calculation for `LoopRelStdDev` as `100 * (SD / Abs(mean))`. A
  company whose average margin is near zero therefore returns an enormous value that dominates the
  node. Pair it with a level filter (`OpMgn%TTM > 0`), or use plain
  `LoopStdDev("OpMgn%(CTR, ANN)", 10)`. `RSD%TTM` suffixes are five-year statistics and `RSD%ANN`
  suffixes ten-year; siblings exist for every margin and return (`GMgn%RSD%TTM`, `ROE%RSD%TTM`).
  There is no published label for this construction - it is a style, not a replication, so do not
  attach an author to it.

---

## Earnings Quality and Distress

Accruals, manipulation and distress scores are ranked across the universe.

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| Accruals - Sloan (1996) | Earnings not backed by operating cash flow, scaled by assets. | `(NetIncBXorTTM - OperCashFlTTM) / AstTotTTM`, or `MScoreTATA` | `Lower` / Universe |
| Earnings manipulation - Beneish (1999) | Eight-ratio manipulation score. | `BeneishMScore` (screen rule, see traps) | `Lower` / Universe |
| Distress - Altman (1968) | Five-ratio bankruptcy score. | `AltmanZOrig` | `Higher` / Universe |

Translation traps:

- **P123 ships accruals; two files must agree on this.** `MScoreTATA` is documented as
  `(NetIncBXorTTM - OperCashFlTTM) / AstTotQ` - the same numerator as the formula above, scaled by
  period-end rather than average assets. `AstTotTTM` (the four-quarter average) is closer to the
  paper's average-total-assets scaling; `MScoreTATA` needs no other Beneish component and carries
  P123's own rule for excluding the latest period when operating cash flow is missing in a
  preliminary report. Pick one and say which; they are not the same number.
- **Neither is the paper's construction.** Sloan's original accrual is the **balance-sheet** change
  in non-cash working capital less depreciation. The cash-flow-statement form used here is the
  standard modern substitute - state that you built the substitute.
- **Use the M-Score as a rule, not a rank node.** P123 publishes thresholds: scores of `-1.89` or
  lower are safest, `-1.49` or higher riskiest. A percentile rank destroys the information those
  thresholds carry, so prefer `BeneishMScore < -1.89` as a screen or universe rule. If it must be
  a node, `RankType="Lower"` - a higher score means a higher manipulation probability.
- **Components are individually addressable.** `MScoreDSRI`, `MScoreGMI`, `MScoreAQI`,
  `MScoreSGI`, `MScoreDEPI`, `MScoreSGAI`, `MScoreLVGI` and `MScoreTATA` all exist as separate
  factors, so a reweighted or partial score needs no custom accounting. `MScoreDEPAMI` is the
  variant of the depreciation index computed from reported depreciation and amortization, where
  `MScoreDEPI` uses an estimate for depreciation. The score is computed on the fly - prefer one
  rule over eight component nodes.

---

## Momentum and Revisions

All of these rank across the universe.

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| 12-1 momentum - Jegadeesh & Titman (1993), skip convention from Carhart (1997) | Prior-year return, skipping the most recent month. | `Ret%Chg(231, 21)` | `Higher` / Universe |
| Intermediate momentum - Novy-Marx (2012) | Return from twelve to seven months ago. | `Ret%Chg(105, 147)` | `Higher` / Universe |
| Recent momentum - Novy-Marx (2012), the other leg | Return from six months ago to two months ago. | `Ret%Chg(84, 42)` | `Higher` / Universe |
| Short-term reversal | Most recent month's return. | `Ret%Chg(21, 0)` | `Lower` / Universe |
| Residual momentum (proxy only) | Momentum net of market exposure. | `Ret%Chg(231, 21) - Beta1Y * Ret%Chg(231, 21, #Bench)` | `Higher` / Universe |
| 52-week-high proximity - George & Hwang (2004) | Price relative to the highest price of the past year. | `Close(0) / HighVal(252)` | `Higher` / Universe |
| Estimate revisions - Chan, Jegadeesh & Lakonishok (1996) | Change in the consensus forecast. | `TotRevisions4W` | `Higher` / Universe |
| Post-earnings drift - Bernard & Thomas (1989) | Earnings surprise, while the drift window is open. | `Eval(WeeksIntoQ <= 8, SUEQ1, NA)` | `Higher` / Universe |

Translation traps:

- **Read the `Ret%Chg` arguments carefully.** `Ret%Chg(bars, offset)` is the return over `bars`
  bars **ending** `offset` bars ago. The literal 12-1 window - twelve months ago to one month ago
  - is eleven months of return ending 21 bars back, so `Ret%Chg(231, 21)`. The widely used
  `Ret%Chg(252, 21)`, which this skill's other files use as the momentum idiom, is a
  **thirteen-month** span: twelve months of return ending one month ago. Both are defensible
  implementations; they are not the same signal, and only the first matches the eleven-month
  convention.
- **The skip is Carhart's, not Jegadeesh & Titman's.** JT (1993) sort on J-month past returns for
  J of 3, 6, 9 and 12 with the holding period starting immediately; the eleven-month window ending
  a month back is the UMD convention of Fama & French (1996) and Carhart (1997). Build
  `Ret%Chg(231, 21)` when the user asks for "12-1 momentum", which is what they almost always
  mean - but do not cite JT (1993) as the authority for the skip.
- **The two Novy-Marx legs are not the same length.** `Ret%Chg(105, 147)` spans bars 252 to 147
  back (twelve to seven months, 105 bars) and the recent leg spans bars 126 to 42 back (six to two
  months, 84 bars): `Ret%Chg(84, 42)`. The recent leg ends **two** months back, not one, because it
  also skips the short-term-reversal month. Using `Ret%Chg(252, 21)` as the "recent" leg both
  double-counts the intermediate window inside it and puts the reversal month back in.
- **`Ret%Chg` includes dividends.** The momentum literature generally sorts on price-only returns.
  `Pr52W%Chg` is P123's price-only 52-week change, but it has no skip, so there is no pre-built
  price-only 12-1 factor. Bars are trading days, so in a multi-country universe one bar count
  spans different calendar windows.
- **Residual momentum is a proxy, not the construction.** The published version regresses returns
  on a multi-factor model and cumulates the residuals; the dictionary contains no factor-return
  series, only index, sector-index and macro series. The formula above subtracts the
  beta-predicted benchmark return, with `#Bench` as the single factor. `Beta3Y` is a longer-window
  alternative but needs a documented minimum of 70 weekly observations, so guard young listings
  with `Eval(Beta3Y = NA, Beta1Y, Beta3Y)`. Do not call the output "residual momentum" - call it
  beta-adjusted or benchmark-relative momentum. `Pr52WRel%Chg` is the pre-built
  benchmark-relative price change, with no skip and no beta adjustment.
- **The 52-week-high ratio, not the percent factor, is the safe node.** `HighVal(period [, offset,
  series])` locates the highest close in a series adjusted for splits **and** dividends up to the
  as-of date, so `Close(0) / HighVal(252)` is a total-return proximity ratio where the published
  measure used the raw price high; the two diverge most for high payers. The pre-built `Pct52WH`
  measures the same idea on the weekly series, but its sign convention is not stated on any detail
  page - its sibling function is documented in [Technical](technical.md) with the example
  `HighPct(252) < -20` meaning "drawn down more than 20% from the 1-year high", which implies
  percent-from-high factors are zero or negative and therefore want `RankType="Higher"`. Prefer
  the explicit ratio when the direction has to be certain.
- **Revision breadth is better behaved than revision percentage.** `TotRevisions4W` counts
  analysts revising up minus analysts revising down. The percentage form
  `%(CurFYEPSMean, CurFYEPS13WkAgo)` is
  well-behaved on negative estimates because P123's `%` operator is `100 * ((a - b) / Abs(b))`,
  but it still explodes when the prior consensus is near zero. Subtracting by hand and dividing by
  the raw prior estimate flips the sign on loss-makers. Filter thin coverage
  (`#AnalystsCurFY >= 3`) before either form; a single analyst moves the mean by construction.
- **`SUEQ1` standardizes by analyst dispersion.** P123 defines standardized unexpected earnings as
  (actual less estimate) divided by the standard deviation of the estimates preceding the
  announcement, with pre-built factors clipped to the range -10 to +10. The published measure
  standardizes by the dispersion of the forecast error from a seasonal-random-walk time-series
  model - same name, different denominator, and a stock with one analyst has near-zero dispersion
  and an extreme `SUEQ1`. Prior quarters are `SUEQ2`–`SUEQ4`; the unstandardized percentage
  surprise is `Surprise%Q1` and the revenue analogue `SUSQ1`.
- **Drift is measured from the announcement.** `WeeksIntoQ` counts weeks since the last report and
  opens the window; `WeeksToQ` counts weeks to the next one and closes it; `LatestActualDays`
  counts calendar days since the vendor's actuals appeared. `SUEQ1` alone encodes none of this.

---

## Low Risk

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| Betting against beta - Frazzini & Pedersen (2014) | Low-beta stocks held against high-beta ones. | `Beta1Y` (long leg only) | `Lower` / Universe |
| Low volatility | Volatility of total returns. | `TRSD1YD` | `Lower` / Universe |
| Idiosyncratic volatility - Ang, Hodrick, Xing & Zhang (2006) | Residual volatility from a market-model regression. | `Eval(LinRegXY("Ret%Chg(5, CTR*5, #Bench)", "Ret%Chg(5, CTR*5)", 52), SE, NA)` | `Lower` / Universe |

Translation traps:

- **A low-beta ranking is one leg, not the strategy.** The published portfolio is long low-beta,
  short high-beta, levered so the two legs carry equal beta. Leverage and beta-neutrality are
  portfolio-construction decisions inside a Strategy, not attributes of a ranking node. Ranking on
  `Beta1Y` gives you the long leg and nothing else - say so rather than calling the rank "betting
  against beta".
- **The beta estimator differs.** P123 documents `Beta1Y` as `BetaFunc(5, 52, 0)`: 52 weekly
  returns against the country's main benchmark, all 52 samples required, ordinary least squares,
  no shrinkage. `Beta3Y` is `BetaFunc(5, 156, 70)` and `Beta5Y` is `BetaFunc(5, 261, 100)`. The
  published beta is built from separate volatility and correlation windows and then shrunk toward
  one; `BetaFunc(period, samples [, min_samples, offset, series])` lets you set the return
  frequency, sample count, minimum samples and reference series, but it cannot reproduce that
  two-window construction.
- **`min_samples = 0` means *all* samples are required**, not "no minimum". That is the default,
  and it is why a long-window `BetaFunc` call returns NA for most stocks.
- **`TRSD1YD` is annualized daily total-return standard deviation**, documented as
  `PctDev(251, 1, 0, 0, TRUE)` - note 251, not 252. Let `PctDev(samples, bars [, offset,
  min_samples, annualize])` annualize with its fifth argument rather than multiplying by a root of
  the sample count by hand. Shorter windows: `TRSD30D`, `TRSD90D`. `PctDev(52, 5)` is the
  un-annualized weekly version.
- **Idiosyncratic volatility here is one-factor and weekly.** The published measure regresses
  **daily** excess returns on three factors within a single month. The recipe above regresses 52
  weekly stock returns on the matching benchmark returns and reads `SE`, the standard error of the
  Y estimate. `SE`, `Slope`, `Intercept` and `Samples` report on the nearest completed regression,
  so they must sit in the same expression as the `LinRegXY` call. The `Eval` wrapper is correct
  and not the dead-branch trap: unlike `SetVar`, `LinRegXY` genuinely returns FALSE when the
  regression cannot be computed, so the `NA` branch is reachable. P123 documents regression
  functions as **Ultimate-subscription only**; on other plans fall back to `TRSD30D` as a
  total-volatility stand-in and say that is what you did. Swap `#Bench` for an explicit series
  with `GetSeries` when the country benchmark is not the right reference.

---

## Size and Liquidity

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| Size - Banz (1981) | Market capitalization. | `MktCap` | `Lower` / Universe |
| Dollar-volume liquidity (a filter, not an anomaly) | Average daily traded value. | `AvgDailyTot(63)` | Universe rule, not a ranked node |
| Illiquidity - Amihud (2002) | Average daily absolute return per unit of traded value. | `LoopAvg("Abs(Ret%Chg(1, CTR)) / AvgDailyTot(1, CTR)", 21)` | `Higher` / Universe |

Translation traps:

- **Size is usually a control, not a ranked factor.** Published size portfolios use fixed exchange
  breakpoints; a P123 rank is relative to whatever universe is attached, so the same rank means
  different companies in `SP500` and in `Prussell3000`. When the breakpoint is the point, write a
  universe rule (`MktCap > 250`, in millions) or an explicit percentile
  (`FRank("MktCap", #All, #ASC)`) instead of a weighted size node.
- **Liquidity is a filter, not a direction.** No documented anomaly says high traded value
  predicts high returns - papers impose liquidity as a tradability screen, and ranking on it tilts
  the whole portfolio toward mega-caps. Write it as a universe or buy rule
  (`AvgDailyTot(63) > 1000000`, in the system's currency) rather than as a weighted node. The
  Amihud row below is the opposite sign on purpose: *il*liquidity is the priced quantity, which is
  why it alone carries `RankType="Higher"`.
- **The illiquidity loop is per-bar.** `AvgDailyTot(noBars [, offset])` is the average traded value
  (price times volume) over `noBars` bars, so `AvgDailyTot(1, CTR)` is that one day's traded value
  and `Ret%Chg(1, CTR)` that day's return. Raise the iteration count for a longer window. `LoopAvg`
  skips NA samples by default (`noNAs` defaults to 0, "NAs are skipped"), but the Factor Reference
  does not document what a zero-volume bar does to the division - verify before relying on it.
  The result is scale-free for ranking but is not on the same scale as any published figure, and
  it is mechanically correlated with size.
- **Scales differ.** `MktCap` is in millions of the system's currency; `AvgDailyTot` returns a raw
  price-times-volume figure. Do not build ratios across the two without checking units.

---

## Investment, Issuance and Payout

| Anomaly | Definition | P123 implementation | Node |
|---|---|---|---|
| Asset growth - Cooper, Gulen & Schill (2008) | Year-over-year growth in total assets. | `AstTotGr%A` | `Lower` / Universe |
| Capital investment | Capital expenditure relative to the asset base. | `CapExTTM / AstTotQ`, or `CapEx%AssetsA` | `Lower` / Universe |
| Net share issuance - Pontiff & Woodgate (2008) | Growth in shares outstanding. | `Eval(SharesPYQ = NA, NA, 100 * (SharesQ / SharesPYQ - 1))` | `Lower` / Universe |
| Buyback yield | Net cash returned through repurchases. | `100 * (EqPurchTTM - EqIssuedTTM) / MktCap` | `Higher` / Universe |
| Dividend yield | Indicated annual dividend over price. | `Yield` | `Higher` / Universe |
| Shareholder yield | Dividend yield plus buyback yield. | `ShareholderYield` | `Higher` / Universe |

Translation traps:

- **Asset growth is an annual sort.** `AstTotGr%A` is exactly year-over-year growth in total
  assets. Do not substitute `AstTotGr%TTM`: `TTM` on a balance-sheet item is the average of the
  trailing four quarters, so its growth compares two overlapping averages rather than two
  balance-sheet dates, and the series is smoothed in a way the published one is not. The
  conservative-investment factor of Fama & French (2015) is the same measurement, so one node
  serves both labels.
- **Undiluted versus diluted share counts.** `SharesQ` and `SharesPYQ` are undiluted;
  `SharesFDQ / SharesFDPYQ - 1` is the fully diluted version and picks up option overhang the
  plain count does not. State which one you used.
- **Check split handling before trusting an issuance factor.** The published measure uses
  split-adjusted share growth; the Factor Reference does not state whether the pre-built share
  counts are restated for splits. Verify on a stock that split inside your window, or use the
  cash-flow form, which is immune to splits but mixes option exercise and acquisition-funded
  issuance into the same number.
- **`Yield` is forward-looking.** P123 documents it as `100 * IAD / Price`, built from the vendor's
  **indicated** annual dividend - a projection of the next twelve months, not dividends already
  paid. For a trailing yield use `DivPS52W / Price * 100` (regular dividends with ex-dates in the
  past calendar year) or `DivPSTTM / Price * 100` (the past four filing quarters). A newly
  initiated dividend shows up immediately in `Yield` and a year late in the trailing forms.
  `Yield` takes no period suffix. Five-year average: `Yield5YAvg`.
- **`ShareholderYield` can switch definition underneath you.** It is documented as
  `Yield + 100 * (EqPurch - EqIssued) / MktCap`, falling back to
  `Yield + 100 * (1 - SharesQ / SharesPYQ)` when the cash-flow items are NA. It therefore inherits
  `Yield`'s forward dividend basis on one half and a trailing basis on the other. If the
  construction is specifically about repurchase cash flow, build the buyback yield yourself so the
  definition cannot change. Net buybacks come from the financing section, so a debt-funded
  repurchase counts in full - pair it with a leverage node (`DbtTot2CapQ`, `RankType="Lower"`,
  `Scope="Industry"`, since capital structure varies structurally by industry) if that matters to
  the thesis.

---

## Worked Example - Quality Sleeve

Three recipes wired into one composite, showing the scope rule in action: profitability ranks
within the industry, the score and accruals rank across the universe.

```xml
<RankingSystem RankType="Higher">
	<Composite Name="Quality" Weight="100" RankType="Higher">
		<StockFormula Weight="40" RankType="Higher" Name="Gross Profitability" Description="" Scope="Industry">
			<Formula>GrossProfitTTM/AstTotQ</Formula>
		</StockFormula>
		<StockFactor Weight="35" RankType="Higher" Scope="Universe">
			<Factor>PiotFScore</Factor>
		</StockFactor>
		<StockFormula Weight="25" RankType="Lower" Name="Accruals to Assets" Description="" Scope="Universe">
			<Formula>(NetIncBXorTTM-OperCashFlTTM)/AstTotTTM</Formula>
		</StockFormula>
	</Composite>
</RankingSystem>
```

Swapping `PiotFScore` for `BeneishMScore` with `RankType="Lower"` turns the sleeve from a
financial-strength screen into a manipulation screen; the other two nodes are unchanged.

---

## Where P123 Cannot Match the Paper

State the limit in one line and give the proxy. Do not fake these.

| Construction | Why it cannot be reproduced | Closest honest proxy |
|---|---|---|
| Multi-factor residuals: three- or four-factor alphas, residual momentum, residual volatility | No factor-return series exists in the dictionary - only index, sector-index and macro series - and `LinRegXY` is bivariate | Single-factor regression against `#Bench`, or the beta-adjusted momentum formula above |
| Betting-against-beta as published | Leverage and beta targeting are Strategy construction settings, not ranking-node attributes | Rank the low-beta long leg and state that the short leg and the leverage are omitted |
| The published beta estimator | `BetaFunc` uses one window and no shrinkage | `Beta1Y`, with the estimator difference disclosed |
| NYSE-breakpoint size or value deciles | A rank is relative to the attached universe, not an exchange | A universe rule on `MktCap`, stated in currency units |
| Surprise standardized by time-series forecast error | `SUEQ1` standardizes by analyst dispersion | `SUEQ1` or `Surprise%Q1`, with the different denominator disclosed |
| Value-weighted long-short decile spreads with a specific rebalancing overlap | A ranking system produces a rank, not a portfolio; weighting and holding period live in the Strategy | Build the rank, then set weighting and rebalance frequency - see [Strategy](strategy.md) |
| Compustat items P123 does not carry | The dictionary is the universe of available data | Check the vendor line-item mapping in [Financials](financials.md) before concluding an item is missing |

---

## Two real factors, one right answer

Every name in both columns below exists. These are the substitutions that quietly change the
factor being built.

| Tempting choice | Use instead | Why |
|---|---|---|
| `GMgn%TTM` | `GrossProfitTTM` over `AstTotQ` | Gross profitability scales gross profit by assets; `GMgn%TTM` scales it by sales, which is a margin. |
| `AstTotTTM` as the profitability denominator | `AstTotQ` | On a balance-sheet item `TTM` is the four-quarter average, not the period-end value. |
| `AstTotGr%TTM` | `AstTotGr%A` | The TTM form compares two overlapping four-quarter averages, not two balance-sheet dates. |
| `PEExclXorTTM` ranked `Lower` | `EarnYield` ranked `Higher` | A loss makes P/E non-computable and drops the stock out of the node; the yield form ranks it last instead. |
| `EV2EBITDATTM` ranked `Lower` | `EBITDAYield` ranked `Higher` | Negative EBITDA makes the multiple negative, which is the *best* rank under `Lower`. |
| `FCFYield` summed with `EarnYield` | Separate nodes | `FCFYield` is a plain ratio; the other yields are percentages, so a sum mis-weights it a hundredfold. |
| `Pr2BookQ` when the definition must be exact | `BookValQ` over `MktCap` | P123's own detail page describes `Pr2Book`'s denominator with the tangible-book wording. |
| `SUEQ1` presented as the paper's measure | `SUEQ1`, denominator disclosed | P123 standardizes by analyst dispersion, not by time-series forecast-error dispersion. |
| `Pct52WH` when direction must be certain | `Close(0)` over `HighVal(252)` | The pre-built factor's sign convention is not stated on any detail page. |
| `Ret%Chg(252, 21)` called 12-1 momentum | `Ret%Chg(231, 21)` | The 252 form spans thirteen months; the 12-1 convention is eleven months ending a month back. |
| `MScoreTATA` and the average-assets formula used interchangeably | Pick one, name it | They share a numerator but divide by `AstTotQ` and `AstTotTTM` respectively. |

---

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `PiotroskiScore` / `FScore` | `PiotFScore` | The only Piotroski factor; returns 0–9. |
| `GrossProfitability` | `GrossProfitTTM` over `AstTotQ` | No pre-built ratio; the annual pre-built form is `GrossProfit%AssetsA`. |
| `BeneishM` / `MScore` | `BeneishMScore` | Components are `MScoreDSRI`, `MScoreGMI`, `MScoreAQI`, `MScoreSGI`, `MScoreDEPI`, `MScoreDEPAMI`, `MScoreSGAI`, `MScoreLVGI`, `MScoreTATA`. |
| `Accruals` / `AccrualsTTM` | `MScoreTATA`, or the difference of `NetIncBXorTTM` and `OperCashFlTTM` over assets | P123 ships the accruals numerator as the Beneish TATA component; no factor is named for accruals. |
| `ROIC%TTM` | `ROI%TTM` | P123 has no ROIC factor. |
| `EarningsYield` / `CFYield` | `EarnYield`, `OCFYield`, `FCFYield` | Spelled-out yield names do not exist. |
| `Beta` | `Beta1Y`, `Beta3Y`, `Beta5Y` | No bare beta factor; `BetaFunc` is the parameterized function. |
| `BetaFunc(52, 104)` | `Beta1Y`, or `BetaFunc(5, 52, 0)` | Read as 104 samples of 52-bar returns - about twenty years of history - and `min_samples` defaults to "all required", so it returns NA for almost every stock. |
| `IdioVol` / `ResidVol` | `LinRegXY` then `SE` | No pre-built idiosyncratic-volatility factor; build it from a regression. |
| `High52W` / `Pr52WHigh` | `HighVal`, `Pct52WH` | `HighVal` returns the level, `Pct52WH` the percent away from it. |
| `PctFromHigh` | `Pct52WH` | `PctFromHi` exists but is a Strategy position factor measured from the entry-to-date high, not a 52-week price factor. |
| `Mom12M` | `Ret%Chg(231, 21)` | Momentum is a function call here; mind the offset semantics. |
| `AssetGrowth` | `AstTotGr%A` | Growth suffixes attach to the line-item name. |
| `SharesOut` | `SharesQ`, `SharesFDQ` | Undiluted and fully diluted respectively. |
| `BuybackYield` | `100 * (EqPurchTTM - EqIssuedTTM) / MktCap` | No pre-built buyback yield; `ShareholderYield` bundles it with the dividend yield. |
| `DivYield` / `DivYield%TTM` | `Yield` | Dividend yield takes no period suffix and uses the indicated annual dividend. |
| `IsNA(AstTotPYQ)` | `AstTotPYQ = NA` | `IsNA` is a two-argument replacement function, not a boolean test. |
| `Sqrt` in a volatility formula | `PctDev(251, 1, 0, 0, TRUE)` | P123 has no square-root function; let `PctDev` annualize, or write `x^0.5`. |
| Reporting an alpha, t-statistic or annual return for any recipe here | The factor definition alone | This file carries no performance figures; none can be verified from the skill's sources. |

---

## See Also

- [SKILL.md](../SKILL.md) - verified factor starting points by style, and the anti-hallucination
  table.
- [Ranking System XML](ranking-system-xml.md) - node schema, weights, `RankType` and the scope
  table these recipes follow.
- [Ratios & Statistics](ratios-statistics.md) - valuation, profitability, margins, yields, and the
  Piotroski, Beneish and Altman families.
- [Financials](financials.md) - line items, period-suffix semantics, and the vendor mapping.
- [Technical](technical.md) - returns, beta, volatility, and the high/low functions.
- [Estimates](estimates.md) - consensus, revisions, surprises, and standardized surprise.
- [Advanced Functions](advanced-functions.md) - `FRank`, loop functions, regressions, NA handling.
- [Strategy](strategy.md) - turning a rank into a rebalanced portfolio.

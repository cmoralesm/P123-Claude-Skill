# P123 Formula Language Quick Reference

## Table of Contents
1. [Syntax Basics](#basics)
2. [Operators](#operators)
3. [Variables (SetVar / ShowVar)](#setvar)
4. [Conditional Logic (Eval) & NA Replacement](#eval)
5. [Cross-Sectional Functions (FRank, ZScore, Aggregate, FOrder, FCount, FSum, FMedian)](#cross-sectional)
6. [Historical Functions (FHist, FHistAvg, FHistRank, FHistZScore)](#fhist)
7. [Ranking System Functions (NodeRank, Rating)](#noderank)
8. [NA Handling](#na-handling)
9. [Math & Utility Functions](#math)
10. [Common Patterns & Idioms](#patterns)

---

## Syntax Basics <a name="basics"></a>

P123 formulas are used in: screen rules, ranking system factors, data retrieval, and universe definitions.

### Operators <a name="operators"></a>

**Math**: `+`, `-`, `*`, `/`, `^` (power)
**Comparison**: `=`, `!=`, `>`, `<`, `>=`, `<=`
**Logical**: `AND`, `OR`, `!` (negate)
**Precedence**: `( )` — always use parentheses when in doubt
**Comments**: `//` — everything after is ignored

### Data Types

- Numbers: `5`, `3.14`, `-20`
- Strings: `"text in quotes"`
- Boolean: `TRUE` (1), `FALSE` (0)
- NA: `NA` — missing/unavailable value
- Constants: `#Year` (251), `#Month` (21), `#Month3` (62), `#Month6` (125), `#Week` (5)

### Bars vs Days

- **Bars** = trading days (~251/year). Used by most technical functions.
- **Calendar days** = includes weekends/holidays. Used by `_D` variants and Account/Portfolio functions.
- Most functions use bars unless explicitly stated otherwise.

---

## Variables (SetVar / ShowVar) <a name="setvar"></a>

```
SetVar(@variableName, expression)
```

Variables start with `@`. They're evaluated once and reused. Multiple SetVar calls chain:

```
SetVar(@pe, PEExclXorTTM)
SetVar(@roe, ROE%TTM)
@pe < 20 AND @roe > 15
```

**Display variable in screen report** (two ways):
```
@myvar:expression              // colon syntax — sets, displays, returns value
ShowVar(@myvar, expression)    // ShowVar — sets and displays in report
```

---

## Conditional Logic (Eval) & NA Replacement <a name="eval"></a>

```
Eval(condition, value_if_true, value_if_false)
```

```
// Use alternate metric when PE is NA
IsNA(PEExclXorTTM, Pr2SalesTTM)

// Sector-specific thresholds
Eval(Sector = 40, DbtTot2EqQ < 15, DbtTot2EqQ < 2)

// Nested Eval for multiple conditions
Eval(MktCap > 10000, 1,
  Eval(MktCap > 2000, 2,
    Eval(MktCap > 500, 3, 4)))
```

### NA/Neg Replacement Functions

```
IsNA(expr1, expr2)          // returns expr1 if not NA, else expr2
IsNeg(expr1, expr2)         // returns expr1 if not negative, else expr2
IsNegOrNA(expr1, expr2)     // returns expr1 if not negative and not NA, else expr2
IsZero(expr1, expr2)        // returns expr1 if not zero, else expr2
```

---

## Cross-Sectional Functions <a name="cross-sectional"></a>

### FRank — Percentile rank across a group

```
FRank("formula" [, scope=#All, sort=#DESC, incl_na=#InclNA, sort_style=#Top])
```

Returns: 0–100 percentile rank.

- **scope**: `#All`, `#Sector`, `#Industry`, `#SubIndustry`
- **sort**: `#DESC` (default — higher=better), `#ASC` (lower=better, e.g. PE)
- **incl_na**: `#InclNA` (default), `#ExclNA`, `#NANeutral` (assign 50)
- **sort_style**: `#Top` (default — ties get highest rank), `#Neutral`

```
// Top quintile by PE (lower is better → #ASC)
FRank("PEExclXorTTM", #All, #ASC) > 80

// Top decile momentum within sector
FRank(`Ret%Chg(252)`, #Sector, #DESC) > 90

// With neutral NA handling
FRank("PEExclXorTTM", #All, #ASC, #NANeutral) > 80
```

**Backticks for complex expressions**:
```
FRank(`Ret%Chg(252, 21)`, #All, #DESC) > 80
```

### ZScore — Standardized score across a group

```
ZScore("formula" [, scope=#All, outlier_pct=7.5, na_value=0, max_zscore=3.5])
```

```
ZScore("PEExclXorTTM", #All)
ZScore("ROE%TTM", #Sector)
```

### Aggregate — Group average (simple or cap-weighted)

```
Aggregate("formula", scope [, method, outlier_pct, outlier_handl, excl_zero, excl_adrs, median_fallback])
```

- **method**: `#Avg` (default — simple average), `#CapAvg` (cap-weighted)
- **outlier_pct**: trim % each side (default 16.5%)
- **outlier_handl**: `#Exclude` (default), `#Winsor`

**Note**: Aggregate only supports `#Avg` and `#CapAvg`. For other stats use `FMedian()`, `FSum()`, `FCount()`.

```
// Industry average PE
Aggregate("PEExclXorTTM", #Industry, #Avg)

// Cap-weighted sector ROE
Aggregate("ROE%TTM", #Sector, #CapAvg)
```

### FOrder, FCount, FSum, FMedian

```
FOrder("formula" [, scope, sort, distinct, incl_na])  // ordinal position (1, 2, 3...)
FCount("formula" [, scope])                            // count where formula is true
FSum("formula" [, scope])                              // sum across scope
FMedian("formula" [, scope, excl_zero])                // median across scope
```

---

## Historical Functions (FHist) <a name="fhist"></a>

### FHist — Point-in-time value

```
FHist("formula", weeksAgo)
```

Returns the value of `formula` as it was N weeks in the past (single observation).

### FHistAvg — Average of historical samples

```
FHistAvg("formula", samples [, weeks_increment=1, NA_pct=20])
```

Returns the **average** of `samples` historical observations spaced `weeks_increment` weeks apart.

Also available: `FHistMax()`, `FHistMin()`, `FHistMed()`, `FHistSum()`, `FHistStdDev()`, `FHistRelStdDev()`

```
// PE value exactly 1 year ago
FHist("PEExclXorTTM", 52)

// Average quarterly ROE over past year (4 samples, 13 weeks apart)
FHistAvg("ROE%TTM", 4, 13)

// Average PE over 5 years (5 annual samples)
FHistAvg("PEExclXorTTM", 5, 52)
```

### FHistRank — Percentile rank vs own history

```
FHistRank("formula", samples [, weeks_increment=1, sort=#DESC, sort_style=#Top, NA_value=NA, NA_pct=20])
```

Returns 0–100 percentile of current vs historical values.

```
// Is current PE historically high? (100 = at peak)
FHistRank("PEExclXorTTM", 52, 1)
```

### FHistZScore — Z-Score vs own history

```
FHistZScore("formula", samples [, weeks_increment=1, clip=3.5, NA_value=NA, NA_pct=20])
```

```
FHistZScore("OpMgn%TTM", 52, 1) > 1
```

### FHistRel — Relative position vs history (0–1)

```
FHistRel("formula", samples [, weeks_increment=1, NA_value=NA, NA_pct=20])
```

---

## Ranking System Functions <a name="noderank"></a>

### NodeRank — Access sub-ranks within current ranking system

```
NodeRank("NodeName")
```

```
NodeRank("Value") > 80
NodeRank("Quality") > 50
```

### Rating / RatingPos — Rank from a different ranking system

```
Rating("Ranking System Name")       // returns rank value
RatingPos("Ranking System Name")    // returns rank position
```

### Other ranking functions

```
GetRank("ticker")              // rank of specific ticker
GetRankPos("ticker")           // rank position of specific ticker
RankPrev(weeksAgo)             // historical weekly rank
RankPosPrev(weeksAgo)          // historical weekly rank position
RankBars                       // bars since rank was last calculated
```

---

## NA Handling <a name="na-handling"></a>

### Fundamental function NA parameter

Every fundamental function accepts NAHandling as last parameter:
- `FALLBACK` (default): falls back to previous period if current is NA
- `KEEPNA`: keeps NA (doesn't fall back)
- `ZERONA`: replaces NA with 0

```
Sales(0, QTR, KEEPNA)
Cash(0, QTR, ZERONA)
OpInc(0, TTM)             // default: FALLBACK
```

### Replacing NAs

```
IsNA(PEExclXorTTM, 999)                // replace NA with 999
Eval(PEExclXorTTM = NA, 999, PEExclXorTTM)  // equivalent

Bound(PEExclXorTTM, 0, 200)            // clip to range [0, 200]
Bound(PEExclXorTTM, 0, 200, TRUE)      // return NA if outside range
LBound(expression, min)                 // lower bound only
UBound(expression, max)                 // upper bound only
```

---

## Math & Utility Functions <a name="math"></a>

```
Abs(expr)                     // absolute value
Negate(expr)                  // negate value
Avg(x1, x2 [, .., x20])      // average of up to 20 values
Max(x1, x2 [, .., x20])      // maximum
Min(x1, x2 [, .., x20])      // minimum
Higher(x1, x2 [, .., x20])   // same as Max
Lower(x1, x2 [, .., x20])    // same as Min
Median(x1, x2 [, .., x20])   // median of a set
Bound(expr, min, max)         // clip to range
LBound(expr, min)             // lower bound
UBound(expr, max)             // upper bound
Between(value, min, max)      // TRUE if min <= value <= max
InSet(expr, x1 [, x2...])    // TRUE if expr matches any value
Log(expr)                     // natural log
Log10(expr)                   // base 10 log
Pow(base, exp)                // power
Mod(a, b)                     // modulus
Trunc(expr)                   // truncate to integer
Gr%(a, b [, years])           // percent growth, optionally annualized
%(a, b)                       // percent = 100 * (a-b) / abs(b)
Random()                      // random number 0-100 (NOTE: not Rand)
BarsSince(date)               // bars since YYYYMMDD date
DaysSince(date)               // calendar days since date
DaysDiff(from, to)            // calendar days between two dates
```

### Date and Filing Factors

```
FYEndMonth                    // fiscal year end month (1-12)
InterimMonths(offset)         // months in interim period (3 or 6)
#APeriods                     // number of historical annual periods
#QPeriods                     // number of historical quarterly periods
```

---

## Common Patterns & Idioms <a name="patterns"></a>

### Multi-factor composite in a screen rule

```
SetVar(@val, FRank("PEExclXorTTM", #All, #ASC))
SetVar(@mom, FRank(`Ret%Chg(252, 21)`, #All, #DESC))
SetVar(@qual, FRank("ROE%TTM", #All, #DESC))
(@val + @mom + @qual) / 3 > 70
```

### Betting Against Beta (BAB) style

```
SetVar(@beta, BetaFunc(52, 104))
SetVar(@rank_beta, FRank(`BetaFunc(52, 104)`, #All, #ASC))
@rank_beta > 50    // low beta half
```

### Piotroski F-Score components

```
SetVar(@f1, Eval(NetIncBXor(0,TTM) > 0, 1, 0))
SetVar(@f2, Eval(OperCashFl(0,TTM) > 0, 1, 0))
SetVar(@f3, Eval(ROA%TTM > FHist("ROA%TTM", 52), 1, 0))
SetVar(@f4, Eval(OperCashFl(0,TTM) > NetIncBXor(0,TTM), 1, 0))
@f1 + @f2 + @f3 + @f4 >= 3
```

### Earnings momentum / SUE

```
SetVar(@surprise, EPSSurprise(0, QTR))
SetVar(@sue, EPSSUE(0, QTR))
@surprise > 0 AND @sue > 1
```

### Liquidity filter

```
MktCap > 500
AvgDailyTot(63) > 500         // avg daily dollar volume > $500K over 63 bars
Close(0) > 5                  // minimum share price
```

### Sector/Industry filtering

```
Sector != 30                  // exclude Financials
Industry != 302520            // exclude REITs
```

### Using benchmarks and indices

```
Close(0, GetSeries("SPY"))    // SPY price
Close(0, #Bench)              // benchmark price
Close(0, #Industry)           // industry index price
Ret%Chg(252) > Ret%Chg(252, 0, GetSeries("SPY"))  // beat SPY total return
```

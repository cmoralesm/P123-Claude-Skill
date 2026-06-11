# Universe Operations — Portfolio123 Reference

Universe Operations are aggregation functions that compute a statistic (average,
count, sum, etc.) across every stock in the current universe that passes a
`"criteria"` rule. They are the universe-wide counterpart to per-stock data; for
filtering the universe by ticker or RBICS see
[universe-filters.md](universe-filters.md), and for the small-set statistics
functions (`Avg`, `Max`, `Median`, ...) see [misc.md](misc.md). Each function
takes a quoted `"criteria"` formula and, for value statistics, a quoted
`"formula"` to evaluate over the matching stocks.

Coverage: 8 functions / 0 factors — extracted from the official Factor Reference
on 2026-06-09. These functions have no individual detail pages in the official
documentation (`doc_index.jsp`), so each entry below is built from the dictionary
fields (code, signature, description) only — no Parameters or Examples sections
are invented.

## Universe Operations

### Functions

#### `UnivAvg("criteria", "formula")`
Calculate the simple average of the values of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivCapAvg("criteria", "formula")`
Calculate the cap-weighted average of the values of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivCnt("criteria")`
Count stocks that pass `"criteria"`.

#### `UnivMax("criteria", "formula")`
Calculate the maximum value of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivMedian("criteria", "formula")`
Calculate the median of the values of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivMin("criteria", "formula")`
Calculate the minimum value of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivStdDev("criteria", "formula")`
Calculate the standard deviation of the values of `"formula"` for the stocks that pass `"criteria"`.

#### `UnivSum("criteria", "formula")`
Calculate the sum of the values of `"formula"` for the stocks that pass `"criteria"`.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `UnivCount` | `UnivCnt` | The count function is abbreviated `UnivCnt`. |
| `UnivStDev` | `UnivStdDev` | The standard-deviation function is `UnivStdDev` (lowercase-then-capital spelling of "StdDev"). |

## See Also

- [universe-filters.md](universe-filters.md) — filter the universe by ticker or RBICS.
- [misc.md](misc.md) — the small-set statistics functions (`Avg`, `Max`, `Median`), universe IDs, and operators.
- [technical.md](technical.md) — cross-sectional ranking functions.

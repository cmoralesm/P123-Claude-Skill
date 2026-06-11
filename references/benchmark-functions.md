# Benchmark Functions — Portfolio123 Reference

Benchmark Functions return historical price data for the benchmark assigned to
the current screen, simulation, or portfolio. For stock-level price history
(`Close`, `Open`, and the other price functions) see [technical.md](technical.md);
for the `#Bench` time series ID used in series-aware functions see [misc.md](misc.md).

Coverage: 1 function / 0 factors — extracted from the official Factor Reference
on 2026-06-09. This function has no individual detail page in the official
documentation (`doc_index.jsp`), so the entry below is built from the dictionary
fields (code, signature, description) only — no Parameters or Examples sections
are invented.

## Benchmark Close

### Functions

#### `BenchClose(barsAgo)`
Historical close price of the benchmark. The barsAgo argument is the number of
bars back from the current bar:

```p123
BenchClose(0)
BenchClose(10)
```

`BenchClose(0)` gets the last close; `BenchClose(10)` gets the close 10 bars ago.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `BenchmarkClose` | `BenchClose` | The function name is abbreviated `BenchClose`. |
| `BenchPrice` | `BenchClose` | Only the benchmark close is available as a benchmark function; no generic price-named variant exists. |

## See Also

- [technical.md](technical.md) — stock-level price functions such as `Close` and `Open`.
- [misc.md](misc.md) — the `#Bench` benchmark time series ID for series-aware functions.

# Universe Filters - Portfolio123 Reference

Universe Filters narrow the current universe to (or away from) a fixed list of
tickers or an RBICS classification. They are used as universe rules, not as
ranking factors. For statistics computed across the universe see
[universe-operations.md](universe-operations.md); for the per-stock RBICS
classification factors and the `RBICS(...)` membership test see
[industry-sector.md](industry-sector.md).

Coverage: 3 functions / 0 factors - extracted from the official Factor Reference
on 2026-06-09. These functions have no individual detail pages in the official
documentation (`doc_index.jsp`), so each entry below is built from the dictionary
fields (code, signature, description) only - no Parameters or Examples sections
are invented.

## Exclude by ticker

### Functions

#### `UnivExclude("tic1, tic2...")`
Exclude stocks in universe with specific tickers.

## Filter by RBICS

### Functions

#### `UnivRBICS(rcode, rcode, rcode, ...)`
Only use stocks in universe with specific RBICS. Pass one or more RBICS codes
(numeric codes or the supported mnemonics - see the `RBICS(...)` membership test
in [industry-sector.md](industry-sector.md), which shares this classification).

## Filter by ticker

### Functions

#### `UnivSubset("tic1, tic2...")`
Only use stocks in universe with specific tickers.

## Common Mistakes

| Wrong (do not use) | Correct | Note |
|---|---|---|
| `UnivInclude` | `UnivSubset` | To restrict the universe to a ticker list use `UnivSubset`; no "include"-named variant exists. |
| `UnivFilter` | `UnivRBICS` | The RBICS universe filter is `UnivRBICS`; no generic filter-named variant exists. |

## See Also

- [universe-operations.md](universe-operations.md) - statistics across the universe.
- [industry-sector.md](industry-sector.md) - the `RBICS(...)` membership test and classification factors.
- [misc.md](misc.md) - built-in universe IDs (e.g. `SP500`, `ALLFUND`).

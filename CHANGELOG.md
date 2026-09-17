# Changelog

## [4.0.0] - 2026-07-27

Correctness release. Four defects found by a practitioner using v3.0.0 against live P123 work
are fixed in SKILL.md and five reference files - the `data_series_info` 405 came in with the
fourth report and is written up as its own bullet - along with three adjacent errors caught while
verifying them (the `data_prices` `end` default, a mislabelled `PctDev` example, and a stale
"no earnings-yield factor" row). No re-extraction: the dictionary, the factor and function
counts, the API surface and all 9 scripts are unchanged from 3.0.0.

### Fixed
- **The `^` power operator was missing from the formula-language guidance.** v3 documented
  `Pow(number, power)` and nothing else, so the skill produced `Pow(x, 0.5)` for roots - and,
  worse, invented `Sqrt(x)`. P123 has **no `Sqrt` and no `Exp` function**: a square root is
  `x^0.5` and an n-th root is `x^(1/n)` (parentheses required - `x^1/3` parses as `(x^1)/3`).
  `x^y` and `Pow(x, y)` are the same operation; `^` is now the documented idiom. Its precedence
  is documented too: `^` outranks every other operator, including the `:` variable operator, so
  `2 * x^3` is `2 * (x^3)` and `@v:x^2` binds `x^2`. Where the official reference is silent -
  how a leading minus binds, whether `a^b^c` associates left or right - the files now say so and
  require explicit parentheses instead of guessing.
- **`SetVar` and `ShowVar` return TRUE (1), never the assigned value.** v3's one-line `SetVar`
  entry said the function "returns true" and stopped there; the consequences were never drawn,
  and the skill wrapped assignments in `Eval(SetVar(@x, f), A, NA)`. That condition is TRUE for
  every stock, so the `NA` branch is unreachable dead code and the call collapses to
  `SetVar(@x, f) * A` - the inline form, which is what returning 1 is *for*. Two further
  consequences are now documented: `SetVar(@x, f) > 10` tests `1 > 10`, and a bare `SetVar` sell
  rule always fires (negate it, `!SetVar(@x, 1 + 2)`). The `Eval` wrapper around `LinReg` is
  explicitly exempted - `LinReg` can return FALSE, so its third argument is reachable.
- **`Weight="0"` on a ranking-system node is legal and must not be "corrected".** P123
  documents the node weight as `[0] - 100 where 0 indicates equal weight`, with `0` as the
  default when the attribute is omitted; zero does not disable a node. When no sibling carries a
  positive weight, the parent's weight splits evenly among them. v3's XML reference said only
  "relative weight within the parent", which led the skill to flag valid systems as broken and
  rewrite them.
- **`p123api` upload options are snake_case Python kwargs, not the camelCase query
  parameters.** v3's api.md listed `headerRow`, `existingData`, `dateFormat`,
  `decimalSeparator`, `onError`, `onDuplicates` and `columnSeparator` as "query options (set by
  wrapper kwargs)" without giving the kwargs, so calls like `headerRow=True` raise
  `TypeError: ... got an unexpected keyword argument`. The wrapper builds the camelCase URL
  itself from `contains_header_row`, `existing_data`, `date_format`, `decimal_separator`,
  `ignore_errors`, `ignore_duplicates` and `column_separator`. Three traps are now called out:
  the header kwarg is `contains_header_row`, not `header_row`; `ignore_errors` /
  `ignore_duplicates` are **inverted** booleans (`ignore_errors=True` sends `onError=continue`,
  and no `on_error` kwarg exists); and the two upload methods are asymmetric -
  `contains_header_row` is data-series only, `column_separator` is stock-factor only, and
  `strategy_transaction_import` accepts neither.
- **`data_series_info` is backed by no endpoint.** The spec defines three Data Series operations
  (`POST /dataSeries`, `POST /dataSeries/upload/{id}`, `DELETE /dataSeries/{id}`) and no `GET`,
  so a series cannot be looked up by name or id - verifiable against `api-docs.yml`. The method
  is absent from `p123api` 2.3.0 and appears in the 2.4.x line with nothing behind it; it was
  reported returning `405 Method Not Allowed` on a live licensed account, which api.md now
  records as an observation rather than deriving it from the spec. This is a spec-level gap, not
  an account-permission problem. Workaround: persist the `dataSeriesId` returned at creation
  time. Contrast `stock_factor_info`, which works because `GET /stockFactor` *is* in the spec.
- **`data_prices` end date.** v3 said `end` "is optional in the wrapper and defaults to today".
  It is typed `Optional[str]` but has **no default value**, so it must be supplied; pass `None`
  explicitly for "through today". Omitting it raises `TypeError: ... missing 1 required
  positional argument: 'end'`.
- **`ranking-system-xml.md` denied a factor that exists.** Its Known Formula Errors table
  redirected `EarnYield%TTM` to `1/PEExclXorTTM` with the note "No pre-built earnings-yield
  factor", contradicting `EarnYield` in the dictionary and in three other skill files. The row
  now points at `EarnYield`, and `EarnYield` is listed among the file's verified valuation
  factors with its documented formula `100 * EPSExclXorTTM / Price`; `1/PEExclXorTTM` stays as
  the formula-node alternative, now with the caveat that it inherits P/E's NA behaviour on losses.
- **`technical.md` volatility example mislabelled.** `PctDev(52, 5)` was captioned "Annualized
  12-month volatility"; annualization is the function's fifth argument and was not being passed.
  The example now shows the raw SD, the `PctDev(52, 5, 0, 0, TRUE)` form, and manual
  annualization as `PctDev(52, 5) * 52^0.5`.

### Added
- **`references/ranking-system-xml.md` → `## Weights`**: the sibling-weight split table (all
  positive / all zero-or-omitted / mixed) and a worked four-child `Weight="0"` composite. The
  mixed row is deliberately non-committal about the resulting split, which no source documents.
- **`references/api.md` → `## Upload Workflow`**: end-to-end create-then-upload example with the
  `dataSeriesId` persisted, every kwarg annotated with the name it is *not*, and the exact URL
  the wrapper builds from that call.
- Two kwarg → query-parameter mapping tables in api.md (Data Series, Stock Factor) with values
  and server defaults; full argument names in the Wrapper Method Map rows for
  `data_series_upload`, `stock_factor_upload`, `strategy_transaction_import` and the
  keyword-only `stock_factor_info`; a wrapper version-drift note (this file is verified against
  2.3.0; 2.4.x adds `data_series_info`).
- Worked `^` examples where they are needed: `MktCap^0.5` and the sign-preserving power form in
  misc.md, the 5-year CAGR `LoopProd(...)^(1/5) - 1` in advanced-functions.md, and manual
  volatility annualization in technical.md.
- 15 new Common Mistakes / anti-hallucination rows across all six edited files, covering `Sqrt`,
  `Exp`, `Power`, `Eval(SetVar(...), A, NA)`, `Eval(ShowVar(...), A, NA)`, `SetVar(...) > 10`,
  the bare `SetVar` sell rule, `Sqrt(MktCap)` in ranking XML, and the camelCase-as-kwarg upload
  errors; misc.md's `Power` row retargeted to `x^y`, and SKILL.md's shared
  `Average`/`Power`/`Ln` row split so that the Correct column for `Power` reads `x^y`, never
  `Pow`.
- **6 new evaluation prompts** (`evals/evals.json`, ids 13–18), one or two per fix; 18 total.

### Changed
- SKILL.md "Formula language essentials" now leads with `SetVar` return-value semantics and a
  math stanza covering `^`, its precedence, and the absence of a square-root function; the
  ranking-XML always-read paragraph names node-weight semantics and states inline that
  `Weight="0"` is legal, leaving the split rules to the reference file.
- `references/misc.md`: `## Math` intro, `Pow`, `SetVar`, `Eval`, the math-operator table note
  and the Show/Set Variable operator section rewritten around `^`-first and TRUE-returning
  assignment; `advanced-functions.md`'s `ShowVar` entry expanded to match.
- `references/api.md`: the Data Series and Stock Factor sections, the
  `strategy_transaction_import` entry and the `file=`/`data=` pitfall rewritten with full
  signatures and the snake_case/camelCase boundary.

### Credits
- All four defects were reported by a Portfolio123 practitioner running the v3.0.0 skill on
  production research work - formulas, ranking systems and API uploads on a live licensed
  account. Each report was re-verified before it was written up: formula semantics against the
  2026-06-09 Factor Reference extraction, and every wrapper signature and endpoint against the
  installed `p123api` 2.3.0 `client.py` and the OpenAPI spec. Two items rest on the reporter's
  own evidence, as v3's XML schema always has: the ranking-node weight range (the Factor
  Reference does not cover ranking-system XML) and the live `data_series_info` 405, observed on
  their licensed account. Thank you!

### Roadmap
- DataMiner operations reference - still uncovered; carried forward from the v3.1 candidate list.

## [3.0.0] - 2026-06-10

Ground-up rebuild. The curated 8-file skill is replaced by a complete, extraction-verified,
category-structured reference.

### Added
- **Full dictionary coverage**: all 4,463 factors and 465 functions of the official P123
  Factor Reference (extracted 2026-06-09), restructured into the 13 official categories plus
  an API reference - 15 reference files total, each with verified header counts, official
  subcategory ordering, and per-file Common Mistakes tables.
- **473 uncounted vocabulary entries** documented for the first time: formula constants,
  country IDs, universe IDs, time/macro series IDs (with FRED mappings), and operators.
- **Complete REST API reference** (`references/api.md`): all 28 paths / 33 operations / 9 tags
  of the OpenAPI 3.1.0 spec, the full 38-method `p123api` wrapper map (generated from the
  wrapper source), authentication/quota semantics, AI Factor usage, and a Known Pitfalls
  section (spec-vs-wrapper discrepancies documented; the wrapper wins).
- **9 runnable example scripts** + `p123_helpers.py`: auth check, screen run, backtests,
  rank performance, ranks-to-CSV, bulk universe download, price history, AI Factor predict,
  and a safety-gated strategy rebalance dry-run (`--execute` + typed confirmation required
  for the only mutating path). Credentials via `P123_API_ID`/`P123_API_KEY` env vars.
- **12 evaluation prompts** (`evals/evals.json`) covering formulas, name recall, screens,
  ranking XML, API workflows, and reference routing.
- Vendor line-item mapping appendix (Item ↔ Compustat ↔ FactSet ↔ P123 function) in
  `financials.md`, from P123's official "Line Items" sheet (as of 7/28/2025).

### Fixed (carried from v2 or resolved during the rebuild)
- **Ranking-system XML schema**: ships the corrected, validated schema (v2 fix) with every
  factor name re-verified; the broken v1 schema is gone. SKILL.md enforces the
  "always read `ranking-system-xml.md` before generating XML" rule.
- **`screen_run` per-rule `type` bug** (issue #5 / PR #6): long-only screens must not carry a
  per-rule `type`; documented in api.md and respected by all scripts and examples.
- **`IsNA` arity** adjudicated from the official dictionary: `IsNA(expr1, expr2)` is a
  two-argument replacement function; test for NA with `expression = NA`. All examples conform.
- **Estimate naming families** adjudicated: the `CurFYEPSMean`/`NextFYEPSMean`/`CurQEPSMean`
  family is correct; the legacy `EstEPSCY`-style family does not exist and now lives in
  Common Mistakes tables only. Duplicate `EstSalesCY`/`EstSalesNY` rows removed.
- **`PiotFScore` vs `PiotroskiF`** adjudicated: `PiotFScore` is the only valid code.
- **`##USR10YR`/`##RBDI` FRED double-mapping** resolved: `##RBDI → RTWEXBGS` kept;
  the `##USR10YR` mapping was a duplicated row and is dropped pending verification.
- Dropped v1/v2 fabrications after dictionary checks: `AccrualsTTM`, `Streak`, `LatestRank`,
  `RegEst`, formula-language `DataSeries(...)`; corrected `SectorCount → SecCount`
  (`SecCount` is valid, contrary to a v1 claim).
- Repository hygiene: `gitignore` renamed to a working `.gitignore`; the broken
  `p123_skill.zip` (wrong internal layout) is deleted; `portfolio123.skill` is regenerated
  from this tree with the official skill-creator packaging tool.

### Changed
- SKILL.md rewritten: routing table over 16 files, formula-language essentials, a
  cross-category anti-hallucination table, and an API quick start matching the verified
  payload shapes.
- README rewritten with install instructions for Claude Code, claude.ai, Cursor, and Codex.

### Removed
- DataMiner coverage (out of scope for v3.0; see Roadmap).
- The v1 curated reference files (superseded by the category files).

### Credits
- Community PRs #3 (full-coverage structure), #4 (buy/sell rule examples), and #6 + issue #5
  (screen_run payload fix, regional universe IDs) informed this release; every datum from
  them was re-verified against the extraction before inclusion. Thank you!
- Regional universe IDs from PR #6 could not be verified against the Factor Reference
  dictionary and are listed as unverified in `api.md` pending a live check.

### Roadmap
- **v3.1 candidate**: DataMiner operations reference (YAML jobs, screen/rank/data downloads)
  - intentionally excluded from v3.0.
- Context-availability matrices for the 19 `vocabType` usage contexts (optional material
  identified during extraction).

## [2.0.0] - 2026-03-22 (partial overlay, never released standalone)
- Corrected ranking-system XML schema (validated against working P123 systems).
- Expanded AI Factor API documentation.

## [1.0.0] - 2026-03-XX
- Initial release: 8 curated reference files, basic API coverage.

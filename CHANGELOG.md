# Changelog

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

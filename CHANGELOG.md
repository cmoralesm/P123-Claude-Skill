# Changelog

## [4.1.1] - 2026-09-17

Closes the last open item carried from 3.0.0: the regional universe IDs reported in issue #5 /
PR #6 were documented but never verified, because no local artifact contains them and the OpenAPI
spec does not enumerate universes at all (`UniverseDef` is just "name or id"). They were confirmed
against the live API instead.

### Fixed
- **Regional universe IDs are verified, not "reported".** All 19 IDs from issue #5 / PR #6 resolve
  on the live API, plus `TSX`, `TSXV`, `CanadaTrust` and `ALLFUNDCDRCAD`. `api.md` now lists them
  by region as verified on 2026-09-17 instead of warning that they are unconfirmed.
- **`CDR` is not a universe ID.** It was reported alongside the others; the server answers
  `Universe <CDR> not found`. The Canadian-dollar CDR universe is `ALLFUNDCDRCAD`. Removed.
- **`ALLFUND` is US-listed, not global** (the second half of issue #5, never incorporated until
  now). Its dictionary label "All Fundamentals" reads as if it spanned every market; it holds
  US-listed securities, foreign companies included through their US lines and ADRs. Corrected in
  `misc.md` and documented in `api.md` with the live evidence.
- **Cross-region `p123Uid` trap** found while verifying the above: the same company carries a
  different UID per listing - Royal Bank of Canada is `7652` (`RY`, in `ALLFUND`) and `47778`
  (`RY:CAN`, in the Canadian and North American universes). Joining on `p123Uid` across regions
  silently misses those pairs.

### Added
- **How to probe a universe ID for free.** An unknown ID returns `Universe <X> not found`; a real
  ID outside your subscription returns `Universe <X> is not in your subscribed regions`. Both are
  HTTP 400 and neither consumes credits, so an ID can be checked without a regional data licence.

## [4.1.0] - 2026-09-17

First public release since 3.0.0. It ships the 4.0.0 defect fixes, which were finished on
2026-07-28 but never published, plus this release's own work: a factor-replication reference, and
a refresh of the API and wrapper documentation after Portfolio123 extended its REST surface on
2026-08-28 and the `p123api` wrapper went to 3.1.0. No re-extraction: the 2026-06-09 dictionary,
the factor and function counts and all 9 scripts' call sites are unchanged. Read the 4.0.0 entry
below as part of this release.

### Added
- **`references/factor-replication.md`** - the 16th reference file, and the first that answers
  "build me *this paper's* factor" rather than "what is this name". 35 recipes across Value,
  Quality and Profitability, Earnings Quality and Distress, Momentum and Revisions, Low Risk,
  Size and Liquidity, and Investment/Issuance/Payout. Each row gives the economic definition in
  one line, the P123 implementation (pre-built factor where one exists, otherwise the formula),
  and the ranking node's `RankType` and `Scope`. Around them: per-family translation traps, a
  worked Quality-sleeve ranking XML, 7 constructions P123 **cannot** reproduce with the closest
  honest proxy for each, an 11-row "two real factors, one right answer" table for substitutions
  that quietly change the factor being built, and a 19-row Common Mistakes table.
  **No performance figures appear anywhere in the file, by design** - no alphas, no
  t-statistics, no return magnitudes. This skill exists to stop invented facts, and none of those
  numbers is verifiable from its sources.
- **`references/api.md` → `## Spec Changes (2026-08-28)`**: the whole 33 → 39 operation diff in
  one place - the six new operations with what each is for, plus the same-revision changes that
  added no path (`preproc` on `POST /data/universe`, the `Currency` enum, `StockFactorParams`
  losing `description` and gaining `maxDays`/`fhistRange`, `BookTradingSystemParams` gaining
  `grossExposure`, `AccessToken` moving to `components/parameters`, and every `operationId` being
  renamed) - and an explicit statement of what the new spec invalidates in 4.0.0.
- **`references/api.md` → `## Migrating from p123api 2.x`**, plus `### Return types` and
  `### Keyword-only lookups` under the Wrapper Method Map. The migration table is derived by
  diffing the installed 2.3.0 and 3.1.0 sources, not from release notes.
- **SKILL.md**: a routing-table row for `factor-replication.md` and a paragraph under the
  style table pointing named constructions at it.
- **6 new evaluation prompts** (`evals/evals.json`, ids 19–24), each written to fail a 4.0.0-era
  model: gross profitability with the wrong denominator, an invented accruals factor, `GET
  /dataSeries` declared nonexistent, `Ret%Chg(252, 21)` called 12-1 momentum, `BetaFunc(52, 104)`
  as a low-volatility node, and dict indexing into a 3.1.0 typed result. 24 total.

### Fixed
- **`api.md` said there is no `GET /dataSeries`. There is, since 2026-08-28.** 4.0.0 documented
  the 28-path / 33-operation spec and used the absence of any Data Series read operation to
  explain a `405 Method Not Allowed` reported from a live account. The lookup now exists, so the
  absence explains nothing going forward. The passage is corrected in place and says so; the 405
  observation is kept in Known Pitfalls as history, because it was real against the older surface,
  and `data_series_info` is now documented as a working keyword-only method
  (`data_series_info(*, id=None, name=None)`) returning a `DataSeriesInfoResult`. The matching
  `AccessToken`-under-`components/schemas` quirk is corrected the same way, as a fact about spec
  copies captured before 2026-08-28.
- **`SKILL.md` recommended a low-volatility factor that returns NA for almost every stock.**
  The Low volatility row read `BetaFunc(52, 104)`, which asks for 104 samples of 52-bar returns -
  about twenty years of history - and `BetaFunc`'s `min_samples` defaults to 0, meaning *all*
  samples are required. The row is now `TRSD1YD`, `PctDev(52, 5)`, `Beta1Y` (which P123 documents
  as equivalent to `BetaFunc(5, 52, 0)`).
- **`ranking-system-xml.md` denied an accruals factor that exists.** Four places said P123 ships
  no pre-built accruals factor, which `MScoreTATA` contradicts - P123 documents it as
  `(NetIncBXorTTM - OperCashFlTTM) / AstTotQ`, the standard accruals numerator, carried as the
  Beneish TATA component. The table note, the Penman & Pope prose and both Known Formula Errors
  rows now say no factor is *named* for accruals and point at `MScoreTATA`, noting that it divides
  by `AstTotQ` where the average-assets form divides by `AstTotTTM`.
- **The momentum window was mislabelled in two reference files.** An example comment in
  `technical.md` called `Ret%Chg(252, 21)` "12-1 month momentum (skip the most recent month)", and
  `misc.md`'s `SetVar` example repeated the label. 252 bars ending 21 bars back spans thirteen
  months, not twelve; the eleven-month formation window is `Ret%Chg(231, 21)`. Both comments now
  describe what the call computes and point at the 231 form. `SKILL.md`'s Momentum row gained
  `Ret%Chg(231, 21)` beside the idiom, and eval 15's prompt - which used "12-1 momentum" purely as
  a label for the `SetVar` exercise - now names the window instead.
- **The free-trial licence waiver was overstated in four places.** The spec grants a no-licence
  trial (IBM, MSFT, INTC, 5 years) on `POST /data` **only**. `POST /data/universe` carries no such
  clause in either the 2026-06 or the 2026-09 capture, and neither does
  `GET /data/prices/{identifier}`. `README.md`, `scripts/README.md`,
  `scripts/06_data_universe_download.py` and `SKILL.md` all extended the waiver beyond `POST /data`
  - 4.0.0 was wrong about this against the spec it was built on too, and `api.md` had already been
  corrected for 4.1. A reader running the universe example on a trial account would have hit a
  licence failure.
- **`technical.md` kept `BetaFunc(52, 104)` as a recommended example** while the rest of the
  release documented it as an error. It is the skill's authoritative page for `BetaFunc`, so the
  example is now `BetaFunc(5, 52, 0)` with `Beta1Y` named as the preferred form, the signature
  entry explains that the first argument is bars *per return* and that `min_samples` defaults to
  "all required", and a Common Mistakes row carries the reversed-argument trap.
- **Eval 18 asserted the pre-2026-08-28 Data Series story** that eval 22 was added to refute - that
  no `GET` operation exists and `data_series_info` returns `405`. Its upload content (`data=`,
  `contains_header_row`, `existing_data`, `date_format`) is unchanged; the lookup half now expects
  `data_series_info(name=...)` returning a `DataSeriesInfoResult`.
- **Four stale or unsourced claims in `api.md`**, all carried over from the 2.3.0 documentation:
  the `file=`/`data=` pitfall counted two docstrings still saying `:param file:` where 3.1.0 has
  one (`strategy_transaction_import`; the other two were rewritten Google-style and say `data`);
  Quotas & Costs said `data_universe` with `asOfDt` keeps no `raw_obj` when it attaches one and
  deletes `cost`/`quotaRemaining` out of it, because `raw_obj` aliases the response dict instead of
  copying it; `RankingMethod` was said to print as its member name, which `IntEnum` stopped doing
  in Python 3.11; and the AI Factor `params` list omitted `universe` (declared on `PredictParams`
  in both captures) while listing `pitMethod` (declared in neither).
- **Six recipe-level corrections in `factor-replication.md`.** The skip-a-month formation window
  is no longer attributed to Jegadeesh & Titman (1993), who sort on J-month returns with no skip;
  the row and the traps now name Carhart (1997) for the convention. The Novy-Marx recent-momentum
  leg is `Ret%Chg(84, 42)` (six to two months), not `Ret%Chg(105, 21)`, and the invented rule that
  the two legs must be equal length is gone. The scope disclosure that was written for gross
  profitability now covers Fama & French (2015) operating profitability as well. Dollar-volume
  liquidity is presented as a universe rule rather than as an anomaly ranked `Higher`, which
  contradicted the Amihud row directly beneath it. The cross-reference to Ranking System XML no
  longer claims the two scope conventions are identical - it names the P/E ambiguity it resolves
  and adds leverage. And a bolded "beats" header, the only comparative performance claim in a file
  that carries none, is retitled to the property the text actually argues.

### Changed
- **`references/api.md` - 643 to 1040 lines, verified operation by operation against the
  2026-09-03 spec capture.** All **39 operations** documented (39/39, none missing, none extra)
  across **32 paths / 9 tags / 111 component schemas**. The Wrapper Method Map is now **44 rows**,
  one per public `p123api` 3.1.0 method, and 3.1.0 is the first release in which every operation
  has exactly one wrapper method behind it, so no map row is endpoint-less any more.
- **Wrapper documentation moved from `p123api` 2.3.0 to 3.1.0**, every signature, default and
  return type re-read from the installed source. The breaking changes are documented rather than
  assumed: Python floor 3.10, pandas demoted from a dependency to the `[pandas]` extra and
  imported lazily, nine methods returning attribute-only typed objects instead of dicts
  (`res['id']` now raises `TypeError`), `cost`/`quotaRemaining` also exposed as `client.cost` /
  `client.quotaRemaining`, four keyword-only lookup methods whose id kwarg is `id` rather than
  `<thing>_id`, `ClientItemNotFoundException` for 404s, and uploads taking `IO[bytes]`.
- **`scripts/`** - no call site changed, because none of the nine scripts calls a method whose
  return type changed and no kwarg they pass was renamed. What changed: `p123_helpers.py`'s
  `print_quota` takes an optional `client` argument and reads `client.cost` /
  `client.quotaRemaining` as a third source, which is the only source that works for `screen_run`,
  `screen_backtest`, `aifactor_predict`, `data_prices` and `data_universe` with an `asOfDt` -
  none of which keeps a usable raw object after the DataFrame conversion. Scripts 02, 03, 06 and
  08 pass it; 04, 05 and 09 are untouched and still work, since the parameter defaults to `None`.
  01 is unchanged and 07 changed only in its docstring, which previously claimed to print quota
  through `print_quota` without ever calling it. Install guidance across the helpers, the scripts,
  `scripts/README.md`, `SKILL.md` and `README.md` now says `pip install "p123api[pandas]"` and
  names Python 3.10+.
- **Line endings normalised.** Eight files picked up CRLF during editing (`references/api.md`,
  `scripts/README.md`, `p123_helpers.py` and scripts 02, 03, 06, 07, 08), which made them read as
  whole-file rewrites in a diff. They are back to LF, matching the rest of the tree. The three
  CRLF files inherited from v3 (`estimates.md`, `financials.md`, `ratios-statistics.md`) are
  untouched and still CRLF - see BUILD-STATE NEW-3.
- **Counts refreshed** in `SKILL.md` (front matter 33 → 39 operations; 38 → 44 wrapper methods)
  and in `README.md` (spec counts, wrapper version and method count, 15 → 16 reference files,
  eval count). `README.md` is also rebuilt on the copy published at 3.0.0 rather than the local
  one, so the banner image and the copy-edit pass that never came back to the tree survive, and it
  now opens with the author's Portfolio123 coaching and consulting credential.
- `scripts/README.md` gained a `name-whitelist` header listing the 6 genuine API identifiers it
  names (`check_names.py` flagged 7 occurrences of them at baseline), so it passes the gate like
  the reference files do. No prose was reworded for it.

### Known unresolved
Three facts are stated in `api.md` as open rather than adjudicated, because each needs one live
call to settle and this release spent zero API credits:
- `POST /rank/create` returns a bare `int32` per the spec, but the wrapper decodes an object and
  reads `id` off it.
- `GET /rank` names the XML field `nodes` in the spec; the wrapper's result type declares `xml`.
- `contains_header_row` now defaults to `True` against a server default of `false`, so a
  headerless CSV would lose its first data row on 3.1.0. It is the only 2.x → 3.x change that
  alters results rather than raising, and it has not been observed live.

### Roadmap
- DataMiner operations reference - still uncovered; carried forward from the v3.1 candidate list.

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
  **Superseded by 4.1.0**: P123 added `GET /dataSeries` on 2026-08-28. The bullet above was true
  of the spec it was written against and is kept as the record of what 4.0.0 shipped; the current
  behaviour is in the 4.1.0 entry and in `references/api.md`.
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

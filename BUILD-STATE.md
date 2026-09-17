# Build State Tracker

Claude Code: update this file after completing each phase/gate (see ../PLAN.md).

## v4.1.0 - replication reference + API refresh (2026-09-17)

**No re-extraction, no re-build.** `v4.1/` started as a byte-for-byte copy of `v4/` (the finished
but unpublished 4.0.0 tree). The 2026-06-09 Factor Reference extraction is unchanged and remains
the source of truth for every factor and function name. What moved under the release is external:
Portfolio123 extended its REST surface on 2026-08-28, and the `p123api` wrapper went to 3.1.0.

**Input.** Two drivers, neither of them a defect report:

1. **Spec drift.** The live OpenAPI document served at `api.portfolio123.com/docs/api-docs.yml`
   went from 28 paths / 33 operations to **32 paths / 39 operations**. 4.0.0 shipped a passage
   stating that the spec defines no `GET` under the Data Series tag, and used that absence to
   explain a `405` reported from a live account. `GET /dataSeries` now exists, so that passage is
   false as a statement about the current API. Correcting it honestly - in place, saying what
   changed and when, rather than deleting the paragraph - is the headline of this release.
2. **Wrapper drift.** `p123api` 3.1.0 is a breaking release against the 2.3.0 line 4.0.0
   documented: Python 3.10+, pandas demoted to an extra, nine methods returning typed objects
   instead of dicts, four keyword-only lookups, six new methods.

| # | Item | Ground truth used | Files edited |
|---|---|---|---|
| 1 | API surface 33 → 39 operations; `GET /dataSeries` correction | `buildnotes/api-docs.live.yml` (live capture, 2026-09-03), diffed against the 2026-06-09 `api-docs.yml` | `references/api.md` |
| 2 | Wrapper 2.3.0 → 3.1.0 | installed `p123api` 3.1.0 `client.py` / `types.py` (AST-read), diffed against the installed 2.3.0 | `references/api.md`, `scripts/` (7 files) |
| 3 | Factor-replication reference | `build/data/dictionary-by-code.json`, `build/data/details.json`, offline `p123_ref_*` validators | `references/factor-replication.md` (new), `SKILL.md` |
| 4 | Contradictions the new file exposed elsewhere | `details.json` (`MScoreTATA`, `BetaFunc`, `Ret%Chg`) | `references/ranking-system-xml.md`, `references/technical.md`, `SKILL.md` |

**Diff vs. v4 (`diff -rq v4 v4.1`, `__pycache__` excluded): 1 new file, 16 modified files - 12
content files plus the 4 release-paperwork files listed after the table.** The table below covers
the 12; the numbers include the 2026-09-17 repair pass recorded at the end of this section.

| File | Substance |
|---|---|
| `references/factor-replication.md` | **NEW, 523 lines.** 35 recipes across 7 anomaly families; per-family translation traps; worked Quality-sleeve XML; 7 constructions P123 cannot reproduce, each with a proxy; an 11-row real-factor-vs-real-factor substitution table; 19-row Common Mistakes table. No performance figures anywhere, by design. |
| `references/api.md` | 643 → 1040 lines (+476/-120, 23 hunks). New `## Spec Changes (2026-08-28)`, `## Migrating from p123api 2.x`, `### Return types`, `### Keyword-only lookups`. Wrapper Method Map rebuilt to 44 rows. Every "does not exist" claim about the older spec corrected in place and dated. |
| `references/ranking-system-xml.md` | +6/-5. Four spots claimed no pre-built accruals factor exists; `MScoreTATA` contradicts that. Now: no factor is *named* for accruals, with the `AstTotQ` vs `AstTotTTM` denominator difference stated. |
| `references/technical.md` | +13/-4. `Ret%Chg(252, 21)` was captioned "12-1 month momentum"; it spans thirteen months. Comment rewritten, pointing at `Ret%Chg(231, 21)`. Repair pass: the `BetaFunc` example and signature entry, plus a Common Mistakes row. |
| `references/misc.md` | +2/-1 (repair pass). The `SetVar` example's "12-1 momentum" caption - NEW-11. |
| `SKILL.md` | Routing row for `factor-replication.md`; named-constructions paragraph under the style table; Low volatility row `BetaFunc(52, 104)` → `TRSD1YD` / `PctDev(52, 5)` / `Beta1Y`; Momentum row gains `Ret%Chg(231, 21)`; front matter 33 → 39 operations; 38 → 44 wrapper methods; install line gains the `[pandas]` extra; free-trial claim on script 07 narrowed. |
| `scripts/p123_helpers.py` | `print_quota(result, client=None)` gains `client.cost` / `client.quotaRemaining` as a third source; install and credential docstrings updated for 3.1.0. |
| `scripts/02, 03, 06, 08` | Docstrings updated; `client` passed to `print_quota`. `04`, `05` and `09` are untouched, `01` too; `07` changed only in its docstring. The new parameter defaults to `None`. |
| `scripts/07_price_history.py` | Docstring only: the quota paragraph (it had claimed to print quota via `print_quota`, which it never calls) and, in the repair pass, the free-trial claim. |
| `scripts/README.md` | Wrapper-version paragraph, `pip install "p123api[pandas]"`, rewritten quota paragraph, plus a `name-whitelist` header (**6** API identifiers; `check_names.py` flagged 7 occurrences of them at baseline) so the file passes Gate 1. No prose reworded for the gate. |

Release paperwork edited afterwards: `README.md` (rebuilt - see Decisions), `CHANGELOG.md`
(4.1.0 entry + a "superseded by 4.1.0" marker on the 4.0.0 `data_series_info` bullet), this file,
`evals/evals.json` (+6 evals, ids 19–24 → 24 total; ids 15 and 18 also revised in the repair pass).

### Verification actually run (2026-09-17)

First-hand on the v4.1 tree; results as observed, not as reported by the editing agents.

| Check | Tool | Result |
|---|---|---|
| Live spec counts | `yaml.safe_load` on `buildnotes/api-docs.live.yml` | **32 paths / 39 operations / 9 tags / 111 component schemas**, OpenAPI 3.1.0 |
| Spec diff vs. the 2026-06-09 capture | set difference on (path, method) | **6 added, 0 removed**: `GET /dataSeries`, `GET /rank`, `POST /rank/create`, `GET /strategy`, `POST /strategy/{id}/copy`, `POST /strategy/{id}/copy-book`. Stale capture: 28/33/9/102 |
| Wrapper public method count | `ast` walk of the installed 3.1.0 `client.py`, `@overload` stubs excluded | **44** (39 endpoint-backed incl. `auth`, 5 helpers). Installed version confirmed `3.1.0`; file is 1258 lines |
| Name validation (Gate 1) | `build/check_names.py` | **PASS, exit 0 on all 19 shipped markdown files**: 16 reference files, `SKILL.md`, `scripts/README.md`, `README.md`. `README.md` was **red** at baseline (2 unknown names) and is now clean |
| Fence balance | ad-hoc, 21 markdown files | **PASS** - all even |
| Table column counts within each table block | ad-hoc (`\|`-split, escaped `\\\|` respected) | **PASS** - 0 mismatched blocks |
| Relative links + `#anchors` across the tree | ad-hoc GitHub-slug checker (gate2 2.3 logic) | **PASS on every v4.1-introduced link**; the single failure is NEW-2, the pre-existing `estimates.md` → `#recs-opinions` anchor inherited from v3 in an untouched file |
| `evals.json` schema + JSON validity | `json.load` + shape check | **PASS** - 24 evals, ids 1–24 contiguous, every object `{id, prompt, expected_output, expectations}`; of the inherited 1–18, only 15 and 18 differ from v4 |
| Scripts compile | `py_compile` on all 10 `.py` files | **PASS**; `__pycache__/` removed afterwards |
| Every formula and identifier written into `SKILL.md` and `evals.json` | offline `p123_ref_validate_formula` / `p123_ref_lookup` (MCP, **0 credits**) | **PASS** - 53 formulas checked across three batches, `unknown_total: 0`, `pitfall_total: 0` |
| Every formula touched by the repair pass | offline `p123_ref_validate_formula`, `context="ranking"` (**0 credits**) | **PASS** - 14 formulas, `unknown_total: 0`, `pitfall_total: 0`, including the new `Ret%Chg(84, 42)`, `BetaFunc(5, 52, 0)` / `(5, 156, 70)` / `(5, 261, 100)` and `AvgDailyTot(63) > 1000000` |
| Line endings | `tr -cd '\r'` on every `.md` / `.py` in `v4`, `v4.1` | **LF everywhere except** the three v3-inherited CRLF files (NEW-3), which match `v4` byte for byte. The eight files converted to CRLF during the 4.1 edits were normalised back |
| `Beta1Y` ≡ `BetaFunc(5, 52, 0)` and the `min_samples` default | `build/data/details.json` → `BetaFunc` full description | **CONFIRMED** verbatim: "BetaFunc(period, samples[, min_samples=0, offset=0])", "0 means all samples are required", "Beta1Y … equivalent to BetaFunc(5, 52, 0)" |

### Findings

| ID | Severity | Finding | Status |
|---|---|---|---|
| NEW-7 | Major | `references/api.md` carries `2026-08-28` and `2026-09-03` as dates of record. Both come from the release brief, **not** from a repo artifact: `buildnotes/api-docs.live.yml` has no capture header and the spec carries no changelog. The operation diff itself is proven by set difference against the older capture; only the two dates are unsourced. They also form the `## Spec Changes (2026-08-28)` heading and its Contents anchor, so changing them is a three-place edit. | **DISCLOSED** - owner to confirm both dates before tagging, or the heading and anchor change with them |
| NEW-8 | Minor | Two spec-versus-wrapper disagreements are stated as open rather than adjudicated, because the spec and the installed source genuinely disagree and one live call settles each: `POST /rank/create` returns a bare `int32` per the spec while the wrapper decodes an object and reads `id`; `GET /rank` names the XML field `nodes` in the spec while the wrapper's result type declares `xml`. | **ACCEPTED** - disclosed in `api.md` and in CHANGELOG §Known unresolved; this release spent 0 API credits |
| NEW-9 | Minor | `contains_header_row` defaults to `True` in 3.1.0 against a documented server default of `false`, so a headerless CSV would silently lose its first data row. Derived from the 3.1.0 source, **not** observed live. It is the only 2.x → 3.x change that alters results rather than raising. | **DISCLOSED** - in `api.md`, CHANGELOG §Known unresolved; confirm with one upload when convenient |
| NEW-11 | Major | **One surviving instance of the corrected momentum mislabel.** `references/misc.md:662` commented `SetVar(@r, Ret%Chg(252, 21)) * @r * Abs(@r)` as "Signed square of **12-1 momentum**", contradicting `technical.md`, `factor-replication.md` and the new eval 21 inside the same tree. | **FIXED** (repair pass, 2026-09-17) - the comment now names the window (252 bars ending 21 bars back, a thirteen-month span) and points at `factor-replication.md`. `grep -rn '12-1' v4.1` now returns only correct uses |
| NEW-10 | Minor | `build/data/client-methods.json` still records `public_method_count: 38` from the 2026-06-09 extraction, and `build/gate2_checks.py` globs `v3/references` with a hard-coded 15-entry `ALL_FILES` list, so `factor-replication.md` is invisible to Gate 2. Both live outside the v4.1 tree and were **not** modified. The "44 methods" figure in this release therefore rests on the AST enumeration above, not on a repo artifact. | **OPEN** - build-tooling debt, carried forward |

**Whitelist discipline (the NEW-1 precedent, applied to the new file).**
`references/factor-replication.md`'s `name-whitelist` header lists 21 tokens and **not one of them
is an invented factor or function name**. They are: ranking-XML attribute and element names
(`RankType`, `Scope`, `StockFactor`, `StockFormula`, `RankingSystem`, `Composite`, `Factor`,
`Formula`, `Description`, `Name`, `Weight`), period suffixes used as prose tokens (`Q`, `A`,
`PYQ`, `PTM`, `RSD%`, `RSD%TTM`, `RSD%ANN`), the vendor name `Compustat`, and the two official
`BetaFunc`/`PctDev` parameter names `noBars` and `noNAs`. Every trap name the file teaches against
- `GrossProfitability`, `AccrualsTTM`, `Accruals`, `BeneishM`, `MScore`, `ROIC%TTM`,
`EarningsYield`, `IdioVol`, `Mom12M`, `AssetGrowth`, `BuybackYield` and the rest - lives only in
the exempted first column of the Common Mistakes table, where the gate cannot read it as a roster
of valid names. This is the rule v4.0.0 set in NEW-1: reword rather than whitelist, and never put
an invented identifier where a model will read it as vocabulary.

**Common Mistakes table, wrong-side column.** Checked against `dictionary-by-code.json`: the
file's `Wrong (do not use)` column holds **25 names, 0 of which exist in the dictionary**. Gate 2
check 2.1 (no-contradiction) therefore cannot fail on this file once the gate is re-pointed.

### Repair pass (2026-09-17) - four adversarial verifier audits

Four verifiers audited the finished v4.1 tree (API truth vs. the live spec and the installed
wrapper; `factor-replication.md` fidelity; regression and collateral damage; the public face -
README, SKILL.md and CHANGELOG numbers). Twenty-one findings. Every claim was re-derived from
ground truth before acting; two findings were dismissed as wrong. The repairs applied:

**1. The free-trial licence waiver, three files (major).** `api.md` had already been corrected for
4.1 - the spec grants the no-licence trial on `POST /data` only - but `README.md`,
`scripts/README.md` and `scripts/06_data_universe_download.py` still extended it to
`/data/universe`, the last of them in a script a trial user would run and watch fail. Re-verified
by parsing both captures: `POST /data`'s description contains "You can try it without a license
with IBM, MSFT, & INTC and 5Y history"; `/data/universe`'s is byte-identical in the 2026-06 and
2026-09 captures and contains no such clause. All three narrowed to `POST /data`. The adjacent
`07_price_history.py` claims (`README.md`, `scripts/README.md`, `SKILL.md` and the script's own
docstring) were narrowed the same way: `GET /data/prices/{identifier}` carries no licence clause
either, so "works on the free trial" was never established - the file now says only that IBM is
one of the three tickers the `POST /data` waiver names.

**2. `technical.md` kept `BetaFunc(52, 104)` as a recommendation (major).** Three other places in
the same release call it an error (`factor-replication.md`'s Common Mistakes row, `SKILL.md`'s Low
volatility row, eval 24), and `technical.md` is the authoritative page for the function. The
example is now `BetaFunc(5, 52, 0)`; the signature entry explains that the first argument is bars
*per return*, quotes `details.json` on `min_samples` defaulting to "all required", and gives the
`Beta1Y` / `Beta3Y` / `Beta5Y` equivalents; a Common Mistakes row carries the reversed-argument
trap. BUILD-STATE listed `technical.md` as a target for this contradiction and never edited it.

**3. NEW-11, `misc.md` (major).** Fixed; see the Findings table.

**4. Eval 18 contradicted eval 22 (major).** Eval 18 was inherited byte-identical from 4.0.0 and
still required the model to state that the spec defines no `GET` for Data Series and that
`data_series_info` returns `405` - the exact claim eval 22 was added to refute, and the headline
correction of this release. A model could not pass both. Its `expected_output` and fourth
expectation now expect `data_series_info(name=...)` → `DataSeriesInfoResult`; the upload half
(`data=`, `contains_header_row`, `existing_data`, `date_format`) is unchanged.

**5. Four stale wrapper/spec claims in `api.md` (minor).** Each re-derived from the installed
3.1.0 source or the live capture: (a) `grep -n ':param file:' client.py` returns **one** hit in
3.1.0 (line 698, `strategy_transaction_import`) against two in 2.3.0, so "two of the three
docstrings" was a 2.3.0 number; (b) `data_universe` with `asOfDt` takes `raw_obj = ret` as an
**alias**, deletes `dt`/`cost`/`quotaRemaining`/`data` out of that same dict, then attaches it
unconditionally - so `attrs['raw_obj']` exists but is stripped, where `data` and `rank_ranks` take
`dict(ret)` copies first; (c) `RankingMethod`, run on the venv's Python 3.12, gives `str(m) == '2'`
and only `repr(m)` shows the member name, because `IntEnum.__str__` became `int.__str__` in 3.11;
(d) the AI Factor `params` list omitted `universe` and added `pitMethod`, where parsing
`PredictParams` in **both** captures gives exactly `precision, universe, asOfDt, includeNames,
includeFeatures, figi` - `universe` restored, `pitMethod` moved to an explicitly-sourced sentence
attributing it to the live-tested curated reference and stating the spec does not declare it.

**6. Six recipe-level corrections in `factor-replication.md`.** The skip-a-month window was
attributed to Jegadeesh & Titman (1993), who sort on J-month past returns with the holding period
starting immediately; the eleven-month window ending a month back is the Fama & French (1996) /
Carhart (1997) UMD convention. The row and both dependent sentences now name the convention rather
than JT (1993) as authority. The Novy-Marx recent-momentum leg was `Ret%Chg(105, 21)` (six to one
month) justified by an invented rule - "the two legs must be the same length" - that is not a
property of the paper; the paper's recent leg ends **two** months back, so the row is now
`Ret%Chg(84, 42)` and the rule is replaced by a statement of the actual asymmetry. The scope
disclosure written for Novy-Marx gross profitability now covers the Fama & French (2015)
operating-profitability row, which had the same divergence undisclosed. Dollar-volume liquidity
carried `RankType="Higher"` directly above Amihud illiquidity carrying `RankType="Higher"` -
monotone opposites, both presented as anomaly directions; it is now a universe rule, not a ranked
node, and the trap says why. The scope cross-reference claimed the Ranking System XML table holds
the identical convention when that table splits on P/E and puts leverage under Industry; it now
names the ambiguity it resolves, adds leverage, and the buyback-yield trap's leverage node gained
its missing `Scope`. And "**Revision breadth beats revision percentage**" - the only comparative
performance claim in a file that carries none - is retitled to "is better behaved than", which is
what the three sentences under it argue.

**7. Line endings (minor).** Eight files had been converted to CRLF during the 4.1 edits
(`references/api.md`, `scripts/README.md`, `p123_helpers.py`, scripts 02, 03, 06, 07, 08), so
`diff -ru v4 v4.1` read them as whole-file rewrites - `api.md` alone showed as a 643-line delete
plus a 1,024-line insert. Normalised back to LF; the whole-tree diff is now 1,832 lines and
`api.md` shows 120 deletions, which is reviewable. The verifier also claimed NEW-3's three files
contain no CR bytes; that is wrong -
`tr -cd '\r'` gives 689 / 5,332 / 3,280 for `estimates.md`, `financials.md` and
`ratios-statistics.md` in v3, v4 **and** v4.1 alike. NEW-3 stands as written and stays OPEN.

**8. Paperwork counts.** The diff summary above said "1 new file, 9 modified files" against an
actual 16; `check_names.py` flags 7 *occurrences* of **6** distinct identifiers in
`scripts/README.md`, so both this file and CHANGELOG said 7 identifiers; `api.md` and
`factor-replication.md` line counts moved; and CHANGELOG's 4.1.0 entry omitted four real changes
(the `SKILL.md` momentum row, the `SKILL.md`/`README.md` install line, the eval 15 rewording and
`07_price_history.py`'s docstring) while leaving scripts 01 and 07 out of its enumeration. All
corrected.

**Dismissed.** Two findings did not survive re-verification:

- *"NEW-3 names three files that contain no CR bytes at all."* False; measured above. The
  verifier's own CRLF finding was otherwise correct and was acted on.
- *"README should drop the banner image and the `docs/` row."* The asset is real on the published
  repo and the banner is the landing page's first element on a page whose business purpose is
  client acquisition; deleting it to satisfy a tree listing is the wrong trade. Instead the
  `docs/` row now says the asset lives on the published repo rather than in this release
  directory, which is what is actually true, and the owner checklist keeps the pre-push
  verification. See NEW-12.

### Findings added by the repair pass

| ID | Severity | Finding | Status |
|---|---|---|---|
| NEW-12 | Minor | `README.md:3` loads the banner from `https://raw.githubusercontent.com/cmoralesm/P123-Claude-Skill/main/docs/p123-skill.jpg`. Nothing in this repo proves that path exists on `main`; the 3.0.0 published README used the same URL, which is suggestive, not proof. The sibling `p123-mcp` repo moved to a **relative** banner path precisely because the absolute `raw.githubusercontent` form breaks while a repository is private. The `docs/` row in the "What's inside" tree now states the asset is repo-only. | **OPEN** - owner: fetch the raw URL before tagging, or add `docs/p123-skill.jpg` to the tree and reference it relatively |
| NEW-13 | Major | **Files were written outside `v4.1/` during the build window, in trees the brief marks never-modify.** `buildnotes/pkg/` (21:09) contains `portfolio123.skill`, 206,257 bytes, built from **v4.0.0 content** - its `references/` has 15 files with no `factor-replication.md`, its `api.md` is 643 lines against v4.1's 1038, and its `README.md` is the 4.0.0 text. `buildnotes/release-notes-v4.0.0.md` (21:11) and `build/data/gate2-report.md` (21:22) were written in the same window. This file's "Packaging: `portfolio123.skill` **not** regenerated" line is true of the folder root and silent about the package under `buildnotes/`. A stale 4.0.0 package sitting in the repo can be mistaken for the 4.1.0 one. | **OPEN, not actionable here** - outside `v4.1/`, which is the only tree this pass may modify. Owner: delete or rename `buildnotes/pkg/portfolio123.skill`, decide whether `buildnotes/pkg/` and the refreshed `build/data/gate2-report.md` are wanted, and reconcile the Packaging line with what is on disk |

### Not run for v4.1 (do not assume these are green)

- **Re-extraction / Gate 0**: not re-run. Dictionary and detail pages are the 2026-06-09
  artifacts. Only the OpenAPI document was re-captured (2026-09-03, by the brief).
- **`gate2_checks.py`**: still not runnable as-shipped - `REFS` is hardcoded to `v3/references`
  and `ALL_FILES` is a 15-entry list that predates `factor-replication.md` (NEW-10). Its 2.3 link
  check was reproduced ad-hoc above; 2.1, 2.2 and 2.4 were **not** re-run.
- **`quick_validate.py` (skill-creator)**: not run.
- **Packaging**: `portfolio123.skill` **not** regenerated. The package at the folder root is still
  the 3.0.0 build.
- **Live API smoke tests**: none. This release spent **0 API credits**; all formula and identifier
  validation went through the offline `p123_ref_*` tools. The three open items (NEW-8, NEW-9) are
  exactly the ones a live call would settle.
- **`p123api` 2.4.x**: never installed. The migration table is a 2.3.0 → 3.1.0 diff; the 2.4.x
  line is not documented in 4.1 beyond the historical note that `data_series_info` first appeared
  there.
- **The banner image**: `docs/p123-skill.jpg` is referenced by `README.md` but lives in the
  published GitHub repo, not in this tree. It must exist at that path on `main` when 4.1.0 is
  pushed, or the landing page shows a broken image.

### Decisions

- **`README.md` was rebuilt on the published 3.0.0 copy**
  (`buildnotes/README-as-published-on-github-v3.0.0.md`), not on the local `v4/README.md`. The
  published file carries the banner image and a copy-edit pass that never came back to the tree;
  the local file carries the accurate 4.0.0 content. Folding the second into the first keeps both.
  Everything the local file said that is still true survives; every count was re-verified against
  this tree rather than copied.
- **Positioning block added at the top of `README.md`**, mirroring the sibling `p123-mcp` repo:
  banner, License badge, then a blockquote naming the author as a Verified Portfolio123 Coach and
  Consultant with links to QuantSolvings coaching, consulting, training and contact. The old
  standalone QuantSolvings attribution paragraph was **merged into it**, not kept alongside, so
  the page does not say the same thing twice. Only the License badge was added: this repo has no
  PyPI package and no CI workflow, and a badge for something that does not exist is worse than no
  badge.
- **The independence disclaimer now separates author from artifact** - "the **author** is a
  Verified Portfolio123 Coach and Consultant; **the skill itself** is not affiliated with…" -
  so the credential and the disclaimer do not read as a contradiction. **Open for the owner**: the
  programme's exact official name. Nothing in this repo corroborates the credential, and no
  external source was consulted; the wording follows the `p123-mcp` README verbatim.
- **The 4.0.0 CHANGELOG entry was not rewritten.** It is the record of what 4.0.0 shipped and was
  true of the spec it was built against. The one bullet that reads as a standing fact about the
  API - `data_series_info` / the 405 - gained a "**Superseded by 4.1.0**" marker pointing at the
  new entry and at `api.md`. Historical counts in the 4.0.0 and 3.0.0 entries (28 paths / 33
  operations, 38 methods, `p123api` 2.3.0) are left alone for the same reason.
- **`SKILL.md` front matter description**: edited only where it had become false - "the full REST
  API (33 operations)" → "(39 operations)". "13 category files" is still correct, because
  `factor-replication.md` is not a category file (the references directory is 16 files: 13
  categories plus `api.md`, `ranking-system-xml.md` and `factor-replication.md`). The description
  already triggers on academic factor replication, so nothing was added for triggering.
- **`evals/evals.json`**: 6 new evals, ids 19–24, continuing the existing shape. Each is written
  to fail a 4.0.0-era model specifically: the gross-profitability denominator (4.0.0's SKILL.md
  offers `GMgn%TTM` as the quality factor), an invented accruals name (`AccrualsTTM` is a
  documented v1/v2 fabrication and 4.0.0's XML file denied any accruals factor), `GET /dataSeries`
  (4.0.0 says it does not exist), `Ret%Chg(252, 21)` as 12-1 momentum (4.0.0 says exactly that in
  two files), `BetaFunc(52, 104)` (4.0.0's own recommendation), and dict indexing into a 3.1.0
  typed result (4.0.0 documents 2.3.0, where everything is a dict).

### Owner checklist for 4.1.0

- [x] ~~**Fix `references/misc.md:662`** - the last "12-1 momentum" mislabel in the tree (NEW-11).~~
      Done in the 2026-09-17 repair pass.
- [ ] **Decide what to do with `buildnotes/pkg/`** - it holds a `portfolio123.skill` built from
      **4.0.0** content, written during this build window in a tree the brief marks never-modify.
      Delete it, or rename it so it cannot be mistaken for the 4.1.0 package, and reconcile the
      "Packaging: not regenerated" line below with what is on disk. Also decide whether the
      refreshed `build/data/gate2-report.md` is wanted (NEW-13).
- [ ] **Confirm the two dates** `2026-08-28` (spec revision) and `2026-09-03` (capture) - NEW-7.
      If either is wrong, fix it in `api.md` (prose, the `## Spec Changes (2026-08-28)` heading
      and its Contents anchor), `CHANGELOG.md`, `README.md` and `BUILD-STATE.md`.
- [ ] **Confirm the credential wording** - the official programme name for "Verified Portfolio123
      Coach and Consultant" as it should appear in `README.md`.
- [ ] **Verify the banner** (NEW-12): fetch
      `https://raw.githubusercontent.com/cmoralesm/P123-Claude-Skill/main/docs/p123-skill.jpg`
      before pushing. If it 404s, add `docs/p123-skill.jpg` to the tree and switch `README.md:3` to
      a relative path, as the sibling `p123-mcp` repo did. The banner is the landing page's first
      element on a page written to attract coaching and consulting clients - do not tag with it
      unverified.
- [ ] Settle NEW-8 and NEW-9 with three live calls (`rank_create`, `rank_get`, one headerless
      upload), then promote the three "unresolved" statements in `api.md` to facts.
- [ ] Re-point `gate2_checks.py` at `v4.1/references`, add `factor-replication.md` to `ALL_FILES`,
      fix its `github_slug` whitespace collapse (NEW-2), and run 2.1/2.2/2.4 - NEW-10.
- [ ] Refresh `build/data/client-methods.json` from the installed 3.1.0 source (38 → 44).
- [ ] Run `quick_validate.py` on `v4.1/`, then repackage `portfolio123.skill` from `v4.1/` staged
      as `portfolio123/` and re-audit the zip (no `.env`, no `evals/`, no `__pycache__`).
- [ ] Copy `v4.1/` over the repo root, commit, tag `v4.1.0`, release with notes from CHANGELOG.md
      covering **both** the 4.1.0 and 4.0.0 entries - 4.0.0 was never published.
- [ ] Still open from 4.0.0: NEW-6 (live `SetVar` confirmation); from 3.0.0: MIN-2 and
      MIN-7 / R4.4 sign-offs below.

---

## v4.0.0 - defect-fix release (2026-07-27)

**No re-extraction, no re-build.** `v4/` started as a byte-for-byte copy of the shipped `v3/`
tree; only the files listed below were edited. Every Phase 0–6 artifact below (extraction,
dictionary, gates, packaging) belongs to the 3.0.0 build and was **not** re-run. The 2026-06-09
extraction remains the source of truth and is unchanged.

**Input.** Four defects reported by a P123 practitioner running the shipped v3.0.0 skill on live
research work (formulas, ranking systems, `p123api` uploads on a licensed account). Not a code
audit, not a re-verification sweep - a bug list from production use, re-checked against the
existing ground-truth artifacts, where those artifacts cover the claim, before any file was
touched. One of the four (the weight rule) is not covered by any of them; see NEW-4.

| # | Defect | Ground truth used | Files edited |
|---|---|---|---|
| 1 | `^` power operator undocumented; skill emitted `Pow(x, 0.5)` and invented `Sqrt` | `build/data/details.json` (`Pow`, operator entries), `dictionary-by-code.json` (`Sqrt`/`Exp` absent) | SKILL.md, misc.md, technical.md, advanced-functions.md, ranking-system-xml.md |
| 2 | `SetVar`/`ShowVar` return TRUE, not the value; skill wrapped them in a dead `Eval` branch | `details.json` (`SetVar`, `ShowVar`, `Eval`, `LinReg`, `:` operator) | SKILL.md, misc.md, advanced-functions.md |
| 3 | `Weight="0"` on a ranking node flagged as an error; it means equal weight | **reporter's evidence only** - the quoted range `[0] - 100 where 0 indicates equal weight` appears in no local artifact (the Factor Reference does not cover ranking-system XML, and `api-docs.yml` has no ranking-node weight schema); same provenance class as the v2/v3 XML schema itself, which was validated against working systems rather than the extraction | SKILL.md, ranking-system-xml.md |
| 4 | Upload kwargs documented as camelCase; `data_series_info` 405 undocumented | installed `p123api` 2.3.0 `client.py` (AST-read signatures), `api-docs.yml` (no `GET /dataSeries`) | api.md |

**Diff vs. v3 (`diff -ru v3 v4`, content files only, after the 2026-07-28 repair pass): 6 files,
39 hunks, +409/-44 lines.**

| File | +/- | Hunks | Substance |
|---|---|---|---|
| `SKILL.md` | +21/-4 | 4 | essentials fence (SetVar semantics + math/`^` stanza), 3 new anti-hallucination rows (the `Average`/`Power`/`Ln` row split so `Power` → `x^y`), ranking-XML paragraph gains node-weight semantics |
| `references/api.md` | +187/-26 | 15 | Data Series + Stock Factor sections rewritten with full signatures and 2 kwarg→query tables; new `## Upload Workflow`; version-drift note; 4 Wrapper Method Map rows expanded; 2 new pitfalls + 2 corrected; 5 Common Mistakes rows |
| `references/misc.md` | +121/-7 | 6 | `## Math` intro, `Pow`, `SetVar` (incl. the NEW-6 provenance caveat), `Eval`, math-operator precedence note, Show/Set Variable operator; 5 new Common Mistakes rows |
| `references/ranking-system-xml.md` | +47/-4 | 8 | new `## Weights` section + Contents anchor, critical-rules bullet, 3 `Weight` attribute rows, `EarnYield` added to Verified Factor Names + its Known Formula Errors row corrected, 1 new Known Formula Errors row |
| `references/advanced-functions.md` | +24/-2 | 4 | `ShowVar` rewrite, `LoopProd(...)^(1/5)` CAGR example, `LinReg`-keeps-its-`Eval` paragraph, 1 Common Mistakes row |
| `references/technical.md` | +9/-1 | 2 | `PctDev` example block (also fixes a v3 mislabelling: `PctDev(52, 5)` was captioned "Annualized"), 1 Common Mistakes row |

`scripts/` and the other 9 reference files are untouched - re-confirmed by the diff (no hunks)
and by a grep for `data_series|stock_factor|upload|SetVar|ShowVar` under `scripts/` (0 hits).
Release paperwork edited afterwards: `CHANGELOG.md` (4.0.0 entry), `README.md` (version +
feature summary + eval count), this file, `evals/evals.json` (+6 evals, ids 13–18 → 18 total).
`SKILL.md` frontmatter deliberately unchanged - see "Decisions" below.

### Verification actually run (2026-07-27)

Re-run first-hand on the v4 tree with the existing build tooling; results as observed, not as
reported by the editing agents.

| Check | Tool | Result |
|---|---|---|
| XML fences parse | `build/verify_xml_fences.py` | **PASS** - ranking-system-xml.md, 7 fences, 0 failures |
| Relative links + `#anchors` across all 20 markdown files | ad-hoc GitHub-slug checker (gate2 2.3 logic, slug bug fixed - see below) | **PASS on every v4-introduced link**; 1 pre-existing failure inherited from v3 (below) |
| Fence balance | ad-hoc | **PASS** (all files even) |
| Table column counts within each table block | ad-hoc (`\|`-split, escaped `\\\|` respected) | **PASS** - 0 mismatched blocks, including api.md's new 4-column tables |
| `evals.json` schema + JSON validity | `json.load` + shape check | **PASS** - 18 evals, ids 1–18 contiguous, every object `{id, prompt, expected_output, expectations}` |
| Wrapper signatures quoted in api.md | AST/regex read of installed `p123api` 2.3.0 `client.py` | **PASS** - `data_series_upload`, `stock_factor_upload`, `strategy_transaction_import`, `stock_factor_info` (3 overloads, keyword-only), `data_prices(..., end: Optional[str])` with no default all match the file |
| Name validation (Gate 1) | `build/check_names.py` | **PASS on all 15 reference files + SKILL.md** after the repair pass (was FAIL on 2 files - see NEW-1) |

### Findings

| ID | Severity | Finding | Status |
|---|---|---|---|
| NEW-1 | Major | `check_names.py` failed on `misc.md` (9 unknown names) and `ranking-system-xml.md` (2). All 11 were **new v4 prose**, not new claims: backticked `Sqrt` / `Exp` / `Power` outside the exempted "Wrong (do not use)" column (misc.md 427, 428, 461, 462, 1144, 1178, 1180; rxml 463), plus placeholder tokens `X` (misc.md 653), `A` (misc.md 697) and the example composite name `Quality` (rxml 157). v3 was clean on both files, so this was a v4 regression in the gate, not in the content. | **FIXED** (repair pass) - resolved by rewording, not whitelisting; see below |
| NEW-2 | Minor | Pre-existing broken anchor, inherited from v3 and **not** introduced here: the Contents entry at `references/estimates.md:18` targets `#recs-opinions` but the "Recs & Opinions" heading at line 585 slugs to `recs--opinions` (GitHub keeps both spaces around the dropped `&`). Gate 2 missed it because `gate2_checks.py:github_slug` collapses `\s+` to a single hyphen. The four v4-adjacent `&` anchors (`#quotas--costs`, `#insider--institutional`, `#watchlists-holdings--opinions`, `#worked-example--penman--pope`) are correctly double-hyphenated. | **OPEN** - out of this release's scope (untouched file) |
| NEW-3 | Minor | CRLF line endings in `estimates.md`, `financials.md`, `ratios-statistics.md`. Present identically in v3; none of the three was edited for v4. | **OPEN** - pre-existing, cosmetic |
| NEW-4 | Minor | The `Weight="0"` rule ships on **single-source evidence**: the reporter's quote of P123's node-weight range. Nothing in `build/data/`, `build/cache/` or `api-docs.yml` documents ranking-node weights at all, so it could not be corroborated here. The mixed zero/positive row in the new Weights table is deliberately non-committal for the same reason. Precedent: the whole ranking XML schema has this provenance (v2.0.0, "validated against working P123 systems"). | **ACCEPTED** - disclosed here, in CHANGELOG §Credits and (since the repair pass) in README "Accuracy & verification"; confirm against a live ranking system when convenient |
| NEW-5 | Major | `ranking-system-xml.md` shipped a second, undisclosed XML-syntax claim: that P123's Ranking System text editor writes `Weight="50%"` and that the percent form is equally accepted, with an instruction never to normalize between the two forms. Unlike NEW-4 this was not traceable even to the reporter - it appears in no local artifact, in no v3 file, in no defect report, and in no example in the file itself, while all three attribute tables type `Weight` as `number`. An unsourced syntax fact that the skill is told never to correct is asymmetrically unsafe. | **FIXED** (repair pass) - paragraph deleted from `ranking-system-xml.md` and the matching CHANGELOG "Added" clause removed. The three attribute tables keep `number`, which is now consistent |
| NEW-6 | Minor | The inline `SetVar` idiom (`SetVar(@r, f) * @r * Abs(@r)`) relies on `@r` being readable to the right of its own call in the **same** formula. `details.json` (`SetVar`, `ShowVar`) documents only "used in **subsequent rules**", and every official example - including the `AccountOpenBar` one in `build/cache/…041ed859.html` - defines in one rule and reads in the next. Same-formula slipstreaming is documented for the `:` operator only, which is the operator v4 tells the reader not to use here. The inline form is nonetheless the *only* option in single-formula contexts (ranking nodes, API `formulas`). | **DISCLOSED** (repair pass) - `misc.md` → `SetVar` now carries a provenance caveat, prefers the documented two-rule form where a rule list exists, and keeps the inline form for single-formula contexts; `advanced-functions.md` → `ShowVar` points at it. Confirm with one live screen run when convenient. **Risk downgraded (owner pass, 2026-07-28):** the v3 idiom this release retires, `Eval(SetVar(@r, f), @r * Abs(@r), NA)`, reads `@r` inside the same formula as well, and the reporter names it as the form the skill was already emitting in working use - so same-expression visibility is presupposed by both forms, not introduced by inlining, and no `Eval` fallback would recover anything if it failed. The caveat in `misc.md` now says so, to stop a future pass from "fixing" the inline form by reverting to the wrapper |

**NEW-1 remedy (applied 2026-07-28, repair pass).** Three options existed: whitelist the trap
names, teach `check_names.py` to exempt more table columns, or reword. The second is out of
bounds - `build/check_names.py` is shipped tooling outside the v4 tree - and the first was
rejected during drafting because `<!-- name-whitelist: ... -->` sits at the top of a file the
model reads, so listing `Sqrt Exp Power` there reads as a roster of valid names, and it would
blind the gate to a future edit that used `Sqrt` as a recommendation in the very file where the
trap matters most. **Rewording was applied instead**: prose that negates a nonexistent function
now says "P123 has no square-root function" / "no exponential function" rather than backticking
the invented token, and the note columns of Common Mistakes rows do the same. The tokens
themselves survive where they belong - in the exempted "Wrong (do not use)" first column of
misc.md, SKILL.md and ranking-system-xml.md - so the anti-hallucination surface is unchanged.
Placeholders `X` / `A` were rewritten as "the right operand" / "its second argument"; rxml's
`Quality` was un-backticked (it is an attribute value, not a code). The inert `1wkRet` whitelist
entry was dropped: `check_names.py`'s token regex is letter-initial, so it never matched
anything. Gate 1 is now green on all 15 reference files + SKILL.md.

### Repair pass (2026-07-28) - four adversarial verifier audits

Four verifiers audited the finished tree (factual accuracy vs. ground truth; cross-file
consistency and markdown integrity; regression/collateral damage; release paperwork). Sixteen
findings; the repairs applied:

| Finding | File | Repair |
|---|---|---|
| Gate 1 red (NEW-1) | `misc.md`, `ranking-system-xml.md` | Reworded, not whitelisted - see the NEW-1 remedy above. Gate 1 now green on all 16 files. |
| `EarnYield%TTM` → `1/PEExclXorTTM` "no pre-built earnings-yield factor" | `ranking-system-xml.md` | **False and four-way contradictory.** `dictionary-by-code.json['EarnYield']` exists (Ratios & Statistics → Yield → Earnings Yield), and SKILL.md, `ratios-statistics.md` and `misc.md` all use it. Row retargeted to `EarnYield`; `EarnYield` added to the file's Verified Factor Names with its documented formula (`100 * EPSExclXorTTM / Price`); `1/PEExclXorTTM` kept as the formula-node alternative, with the detail page's own caveat that a loss yields a negative `EarnYield` where P/E can go NA. |
| `Weight="50%"` accepted-form claim | `ranking-system-xml.md` | **Deleted** - see NEW-5. |
| "P123's own published sample XML has this shape" | `ranking-system-xml.md` (Weights table, mixed row) | Clause deleted: no P123-published ranking XML exists in `build/`. The row's substantive verdict (legal input, split undocumented, do not rewrite) is unchanged and needs no source. |
| Unbounded "`0` means equal weight" | `ranking-system-xml.md` ×3 attribute tables, `SKILL.md` | Notes now read "`0` or omitted is legal and does not disable the node - see [Weights] for the split rules", which is true of the mixed case too. SKILL.md states the legality inline and defers the split. |
| `Power` → `Pow` in the always-loaded table | `SKILL.md` | Row split: `Average`/`Ln` → `Avg`/`LN`, and `Power`/`Pow(x, y)` → `x^y`. The Correct column never says `Pow` now (eval 13 expects exactly this). |
| Same-formula `SetVar` visibility | `misc.md`, `advanced-functions.md`, `SKILL.md` | Provenance caveat added - see NEW-6. The inline form is retained (it is the only option in single-formula contexts) but the documented two-rule form is named as preferred where a rule list exists. |
| `PctDev(52, 5) * 52^0.5` presented beside `PctDev(52, 5, 0, 0, TRUE)` | `technical.md` | Annotated as approximate. `details.json` `PctDev` documents annualization as sqrt(periods/year) with a 251-day year (21 bars → sqrt(12), 1 bar → sqrt(251)); 251/5 ≈ 50.2, not 52, so the two forms differ by ~1.8%. `annualize=TRUE` is now marked as the form to prefer. |
| 405 stated as derived from the spec | `api.md` ×3 | Split: "no `GET` under the Data Series tag" is verified against `api-docs.yml`; the `405` is labelled a live observation, since 2.4.x's `data_series_info` URL cannot be read from the installed 2.3.0. |
| README claimed the weight rule was verified against a source | `README.md` | Rewritten to disclose both single-source items (weight range, 405) and point at NEW-4 / §Credits. |
| README claimed a green name gate | `README.md` | True again after NEW-1; wording tightened to name the two real exemptions (Wrong columns, `name-whitelist` comments). |
| `Weight=\"0\"` escaping artifact | `README.md` line 113 | Backslashes dropped - they are literal inside a markdown code span. |
| CHANGELOG "four defects … three adjacent errors" | `CHANGELOG.md` | The 405 came from the reporter, not from adjacent verification. Summary reworded and the three genuine adjacent errors named (`data_prices` `end`, the `PctDev` caption, the `EarnYield` row); the `EarnYield` fix added as its own Fixed bullet. |

Two findings were **dismissed**: (a) the proposal to type `Weight` as `number or number%` in the
three attribute tables - moot once NEW-5 was deleted, and `number` is the only form any artifact
or example in the file uses; (b) the proposal to strip the `x^1/3` parse note and the bare-`SetVar`
sell-rule sentence from SKILL.md purely for token budget - evals 14 and 16 test exactly those two
behaviours, and the block was trimmed instead (the duplicated `Eval(SetVar(...), X, NA)` warning
was removed from the fence, since it is already a row in the anti-hallucination table 60 lines
below; the `@v:x^2` precedence aside went with it). The essentials block is 2,219 chars, down from
2,301 before the repair pass and up from v3's 1,404 - the residual growth is the two fixes the
release exists for, so it stays.

### Not run for v4 (do not assume these are green)

- **Re-extraction / Gate 0**: not re-run. Dictionary, detail pages and `api-docs.yml` are the
  2026-06-09 artifacts.
- **`gate2_checks.py`**: not run as-shipped - its paths are hardcoded to `v3/references`. Its
  2.3 link check was reproduced ad-hoc above; 2.1 (no-contradiction), 2.2 (slice coverage) and
  2.4 (header counts) were **not** re-run. 2.1's risk was reduced by the repair pass: `Sqrt` /
  `Exp` / `Power` now appear only in Wrong columns, not in backticked prose.
- **`quick_validate.py` (skill-creator)**: not run.
- **Packaging**: `portfolio123.skill` **not** regenerated from `v4/`. The package at the folder
  root is still the 3.0.0 build.
- **Live API smoke tests**: none. No script changed, and the `data_series_info` 405 is recorded
  from the reporter's own account, not re-observed here.
- **`p123api` 2.4.2**: not installed locally. api.md's signatures are verified against the
  installed 2.3.0 only, and the file says so.

### Decisions

- `SKILL.md` frontmatter left byte-identical. It carries no version field, and the description
  already triggers on `SetVar`, `Eval`, ranking system XML, formula syntax and `p123api` - the
  four fixes narrow existing behaviour rather than adding a new surface, so nothing needed to
  change for triggering and the description was not lengthened.
- `evals/evals.json` was excluded from the content-edit phase by design and written here: 6 new
  discriminating evals, ids 13–18, continuing the existing shape. Each is written to fail a model
  that reproduces the reported v3 behaviour (`Pow(x, 0.5)` / `Sqrt`, `Eval(SetVar(...), X, NA)`,
  "`Weight=\"0\"` is an error", `headerRow=True`).
- One SKILL.md example line from the `^` edit spec
  (`(PEExclXorTTM * Pr2SalesTTM)^0.5`) was dropped during application to keep the always-loaded
  essentials block short; the geometric-mean case survives in misc.md's `Pow` entry.

### Owner checklist for 4.0.0

- [x] Resolve NEW-1 - done in the repair pass by rewording; Gate 1 green on all 16 files.
- [ ] NEW-6: confirm same-formula `SetVar` reuse with one live screen run, then drop the
      provenance caveat in `misc.md` → `SetVar` (or keep the two-rule form as the primary
      recommendation if it does not hold).
- [ ] Re-point `gate2_checks.py` at `v4/references` and run 2.1/2.2/2.4; fix its `github_slug`
      whitespace collapse first (NEW-2), or NEW-2 will stay invisible.
- [ ] Run `quick_validate.py` on `v4/`, then repackage `portfolio123.skill` from `v4/` staged as
      `portfolio123/` (folder name drives the package name) and re-audit the zip (no `.env`, no
      `evals/`, no `__pycache__`).
- [ ] Copy `v4/` over the repo root, commit, tag `v4.0.0`, release with notes from CHANGELOG.md.
- [ ] Thank the reporting practitioner in the release notes (credited in CHANGELOG.md §Credits).
- [ ] Still open from 3.0.0: MIN-2 and MIN-7 / R4.4 sign-offs below.

---

## v3.0.0 build (2026-06-09 / 2026-06-10)

| Phase | Description | Status | Notes |
|---|---|---|---|
| 0 | Extraction pipeline + Gate 0 | **PASS** (2026-06-09) | See "Phase 0" section below |
| 1 | Agents A–E launched | **DONE** (2026-06-09) | 5 agents in parallel; see "Phases 1–2" below |
| 2 | Gate 1 self-checks | **PASS** (2026-06-09) | Agent self-checks + independent orchestrator re-runs |
| 3 | Gate 2 cross-file consistency | **PASS** (2026-06-09) | `build/data/gate2-report.md` |
| 4 | Gate 3 scripts | **PASS** (2026-06-09) | See "Gate 3" section below |
| 5 | SKILL.md + README + CHANGELOG + evals + Gate 4 validation | **PASS** (2026-06-10) | See "Phase 5" section below |
| 6 | Packaging + Gate 5 independent verification | **PASS** (2026-06-10) | Round 2 clean; packaged + install-tested |

## Gate 5 - Verification round 1 (2026-06-10)

Verifier V (fresh adversarial agent) report: `VERIFICATION-REPORT.md` (folder root). All
sources re-verified live (S5 MD5 match), 26-entry sample clean with 10 live confirmations,
independent name-sweep clean, scripts compile and are safety-gated. Findings and fixes:

| ID | Severity | Finding | Fix (2026-06-10) |
|---|---|---|---|
| BLK-1 | Blocker | `v3/.env` (credentials) would ship inside `portfolio123.skill` (packager has no `.env` exclusion) | `.env` moved out of `v3/` to the folder root; packaging will also stage a copy that never contains it |
| MAJ-1 | Major | `#Previous1`/`#GroupVar2` shipped as "verified scope constants" - PR #3 misparse of live-page footnote superscripts | Scope table rewritten with the 16 official constants verbatim from the dictionary; footnote restrictions kept as labeled official footnotes; whitelist entries removed |
| MAJ-2 | Major | evals.json eval 4 expected a nonexistent `RankingSystem2` root, contradicting ranking-system-xml.md | Eval 4 rewritten to the validated schema (RankingSystem root, StockFormula/Composite, RankType Lower/Higher) |
| MIN-1 | Minor | Unsourced "formula names are case-insensitive" claim (strategy.md) | Claim removed; canonical-casing guidance kept |
| MIN-2 | Minor | PR #4 behavior semantics shipped with disclosed provenance but no artifact source | Accepted as-is (provenance disclosed in strategy.md); flagged for owner review |
| MIN-3 | Minor | SKILL.md `Ret%Chg(252, 21)` comment misstated the window | Comment corrected to "over 252 bars, ending 21 bars ago" |
| MIN-4 | Minor | misc.md referenced unshipped `build/notes/agent-E.md` | Note made self-contained; pointer removed |
| MIN-5 | Minor | BUILD-STATE.md absent from README tree | Added to README tree |
| MIN-6 | Minor | api.md said "PyPI 2.2.0"; PyPI now serves 2.3.0 | Wording updated (2.3.0 at build time; install >= 2.2.0) |
| MIN-7 | Minor | R4.4 resolved by documented deviation, not the planned live call | Accepted; owner sign-off item on the release checklist |

Post-fix re-checks: `check_names.py` clean on all changed files + SKILL.md; evals.json valid
(12 evals); Gate 2 re-run: PASS. Verification round 2 (fresh verifier, changed scope) launched.

## Gate 5 - Verification round 2 + packaging (2026-06-10)

- **Round 2: PASS, zero blockers/majors remaining, zero new findings** (fresh verifier;
  results appended to `VERIFICATION-REPORT.md` → "Round 2 - changed-scope re-verification").
  BLK-1/MAJ-1/MAJ-2 confirmed fixed with programmatic evidence (16-constant exact set match;
  eval-4 expectations traced to ranking-system-xml.md lines; no .env in v3/).
- **Packaging (plan/06 §7):** `v3/` staged as `build/stage/portfolio123/` (folder name drives
  the package name - the packager uses the directory name, not the frontmatter) and packaged
  with the official skill-creator tool → `portfolio123.skill` (184,679 B, replaces the stale
  v1 package at the folder root). Zip audit: 32 entries, single top-level `portfolio123/`
  dir, **no .env**, no evals/ (auto-excluded), no __pycache__.
- **Install test:** unzipped to a temp dir; `quick_validate.py` → "Skill is valid!"; all 16
  SKILL.md link targets (15 references + scripts/README.md) resolve in the unpacked tree.
- `p123_skill.zip` (broken internal layout, superseded) deleted per decision R5.5.
- Note: `v3/.env` was relocated to the folder root (outside the repo tree) - the owner's
  API credentials never ship in the package or the repo.
- 2026-06-10 (post-release-prep): README tree line for `evals/evals.json` annotated
  "(repo only; excluded from the .skill package)" - caught by the Insights-article
  fact-check pass; `portfolio123.skill` regenerated and re-audited (32 entries, no .env).

## Release checklist (owner actions - decision R5.3)

- [ ] Review `VERIFICATION-REPORT.md` (rounds 1 + 2) and this file.
- [ ] Owner sign-off on the two accepted deviations: MIN-2 (PR #4 behavior semantics shipped
      with disclosed provenance) and MIN-7 / R4.4 (AI Factor cost documented from both
      sources; resolve later with one live `aifactor_predict` using your predictor id, then
      update api.md → AI Factor and script 08's docstring).
- [ ] Copy/replace the GitHub repo contents with `v3/` (repo root = skill root). Do NOT copy
      any `.env`.
- [ ] Commit; tag `v3.0.0`; create a GitHub Release with notes from CHANGELOG.md.
- [ ] Add the regenerated `portfolio123.skill` to the repo/release.
- [ ] Update repo description/topics (counts: 4,463 factors / 465 functions; topics:
      `claude-skill`, `portfolio123`, `factor-investing`, `quantitative-finance`).
- [ ] Close PRs #3/#4/#6 and issue #5 with thanks + release link (their verified content is
      incorporated and credited in CHANGELOG.md §Credits).
- [ ] Verify README install instructions against the final repo tree (no placeholders -
      verified in round 1/2, re-check after the repo copy).
- [ ] Optional: announcement (P123 forum / LinkedIn) - outside this plan's scope.

## Phase 5 - Skill assembly + Gate 4 (2026-06-10)

- `v3/SKILL.md` rewritten: frontmatter `name: portfolio123`, description 992 chars (limit
  1,024), no angle brackets, no DataMiner; body 205 lines (limit 500); routing table covers
  all 15 reference files + scripts/README.md; formula essentials with only
  dictionary-verified names (every name and signature checked against
  `dictionary-by-code.json` before inclusion - `DivPSA` was caught as nonexistent and
  replaced with `DivPSTTM`); 23-row cross-category Common Mistakes table; ranking-XML
  always-read rule; API quick start with the PR-#6-correct payload (no per-rule `type`);
  `check_names.py` exit 0 (120 candidates).
- `v3/README.md` rewritten from scratch (no placeholders): coverage numbers from the
  extraction report, install instructions for Claude Code / claude.ai upload / Cursor /
  Codex, structure tree matching reality, example prompts, accuracy & verification
  statement, contributing, MIT, independence disclaimer.
- `v3/CHANGELOG.md`: full v3.0.0 entry (added/fixed/changed/removed/credits/roadmap;
  DataMiner = v3.1 candidate); v2/v1 history stubs.
- `v3/evals/evals.json`: 12 evals per plan/06 Gate 4 list, each with prompt,
  expected_output, and 3-4 objective expectations.
- **Gate 4: PASS** - official `quick_validate.py` (skill-creator tooling, copied to
  `build/tools/scripts/` from the plugin install; the S9 path `~/.claude/skills/` does not
  exist on this machine - substitution logged): "Skill is valid!"; evals schema-complete;
  DataMiner absent; routing complete.

## Phase 0 - Extraction pipeline (run 2026-06-09)

- Pipeline scripts written and run: `build/extract_factors.py`, `extract_details.py`,
  `extract_line_items.py`, `validate_extraction.py`, `make_slices.py`, `fetch_inputs.py`;
  helpers `build/check_names.py` (Gate 1/2 name validator) and `build/gen_tables.py`
  (deterministic table renderer). Full log: `build/data/extraction-report.md`.
- **Gate 0: PASS.** 0.1 PASS (465 fn / 4,463 fac, category sums == footer); 0.2 PASS (no drift
  vs baseline); 0.3 PASS (5,401 dictionary entries); 0.4 PASS (0 orphans); 0.5 PASS
  (850/850 accessible detail pages = 100%); 0.6 PASS (10-entry sample dumped to
  `build/data/gate0-manual-sample.md`; 6 entries additionally re-verified verbatim against the
  live page in fresh fetches); 0.7 PASS (line-items.csv, 142 rows, header
  `Item,Compustat Equivalent,FactSet Equivalent,Portfolio123 Function` at row 3);
  0.8 PASS (live api-docs.yml MD5 == local after newline normalization:
  `9be5372c966944b9d8ddf6e388149143`).
- **Findings logged at extraction time:**
  - `_vdfs` field 1 is either `'()'` (function marker) or a factor **suffix** concatenated to
    field 0 to form the full code (e.g. `EV2EBITDA`+`Q`). Full codes are the dictionary keys.
  - 473 entries live under tree nodes whose anchors report 0/0 (constants, Country IDs,
    Universe IDs, Time/Macro Series IDs, operators - all under Misc). They are NOT counted in
    the official 465/4,463 totals; marked `counted: false` in artifacts. 5,401 = 4,928 + 473.
  - 14 detail pages are login-gated ("An active subscription is required..."): the
    Industry & Sector classification factors (IndCode, Industry, RBICS, Sector, SubSector,
    UnivRBICS, ...). Listed in `build/data/details-skipped.json`; these ship as
    dictionary-sourced rows only. Success rate is computed over the 850 accessible pages.
  - doc_index.jsp has NO detail pages for Universe Operations (8 fn), Universe Filters
    (UnivExclude, UnivSubset), Benchmark Functions (BenchClose) - documented from dictionary
    signature/short_desc fields.
  - p123api master public-method count is **38** (programmatic AST count,
    `build/data/client-methods.json`), vs registry baseline "37 measured 2026-06-09".
    `stock_factor_info` has two `@overload` stubs + one implementation (deduped).
  - Live api-docs.yml re-fetched at build time: identical to the local copy.
- Agent input pre-fetch (`build/fetch_inputs.py`): p123api client.py/README/setup.py,
  ai-factor-reference.md (16,418 B - matches registry), PR #3/#4/#6 diffs → `build/inputs/`.
- Agent briefs written: `build/briefs/common.md` + `agent-A..E.md`. Agent working notes go to
  `build/notes/agent-X.md` (consolidated here by the orchestrator after Gate 1 - avoids
  concurrent writes to this file).

## Phases 1–2 - Build agents + Gate 1 (2026-06-09)

All 15 reference files + 11 script files built by agents A–E in parallel. Gate 1 self-checks
re-run independently by the orchestrator on every file: `check_names.py` exit 0 on all 15;
slice coverage 100% on all 13 category files (only nominal "misses": the two Misc operator
entries whose dictionary "code" is a symbol list - rendered as full operator tables instead);
33/33 API operations + 38/38 wrapper methods in api.md; all 10 scripts `py_compile` clean;
6/6 XML fences parse. Full agent notes: `build/notes/agent-{A..E}.md`.

**Adjudications (Gate 2 dispute registry - one verdict, evidence in agent notes):**

| Dispute | Verdict | Evidence |
|---|---|---|
| IsNA arity | `IsNA(expr1, expr2)` two-argument replacement; test NA with `expr = NA` | dictionary signature `expr1, expr2`; Misc/Math detail page; PR #4's own fix (Agent D) |
| PiotFScore vs PiotroskiF | `PiotFScore` | only `Piot*` code in dictionary (Agent C) |
| EstEPSCQ… vs CurFYEPSMean… | `CurFYEPSMean` family | `EstEPS*`/`EstSales*` count = 0 in dictionary (Agent C) |
| GetSeries vs DataSeries | `GetSeries` in formulas; `DataSeries`/`StockFactor` dropped as formula tokens | dictionary; api.md references the features by API method only (Agent A) |
| ##USR10YR / ##RBDI → RTWEXBGS | `##RBDI → RTWEXBGS` kept; `##USR10YR` mapping dropped (blank, with note) | FRED series name "Real Broad Dollar Index"; both rows shared numeric_id=1320 (Agent E) |
| Regional universe IDs (PR #6) | NOT shipped as verified (absent from dictionary); listed as PR-#6-reported only | Agents A + E independent checks |
| v1/v2 fabrications dropped | `AccrualsTTM`, `Streak`, `LatestRank`, `RegEst`, `DataSeries(...)` formula form; `SecCount` is VALID (`SectorCount` is not) | Agent D notes |
| AI Factor cost (R4.4) | Documented with both sources (spec `cost: 1` vs live-tested `20`); could NOT be resolved live - a predictor id from the owner's account is required and the API has no list-predictors operation. api.md advises budgeting 20 credits and confirming via the response's `cost`/`quotaRemaining`. Marker replaced 2026-06-09. | api.md → AI Factor |

## Gates 2–3 (2026-06-09)

- **Gate 2 PASS** (`build/gate2_checks.py`, report `build/data/gate2-report.md`): 0 wrong-name
  contradictions across all 15 files; slice coverage 100% on all 13 category files (the six Misc
  operator entries with symbol-list codes are rendered as operator tables - manually verified);
  0 bad relative links; all 13 header coverage lines match slice counts. Tooling note: the
  name-token regex was extended for mid-token `#` codes (`EPS#Positive`, `Inst#ShsOwn`...).
- **Gate 3 PASS:**
  - Compile: `py_compile` clean on all 10 script files.
  - Static sanity: 13 distinct `client.*` methods used by scripts, all present in the
    programmatic method list (`build/verify_scripts_static.py`); Agent A cross-checked every
    params key against api-docs.yml + client.py (no disagreements on keys actually used).
  - **Live smoke (read-only, owner credentials from v3/.env mapped to P123_API_ID/P123_API_KEY):**
    1. `01_auth_check.py` - PASS (authentication succeeded, Bearer token obtained). No cost.
    2. `07_price_history.py --start 2026-05-01 --end 2026-05-15` - PASS (IBM, 11 rows of EOD
       bars returned). Free-trial ticker; no cost surfaced by the wrapper's pandas path.
    3. `02_screen_run.py --universe SP500 --rule "Close(0) > 200" --max-holdings 10` - PASS
       (10 rows returned, payload shape per PR #6: no per-rule `type`).
    No mutating call was executed (script 09 not run beyond `--help`-level checks; Ground Rule 5).
  - R4.4 outcome recorded above; api.md and script 08 docstring consistent.

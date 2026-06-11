# Build State Tracker

Claude Code: update this file after completing each phase/gate (see ../PLAN.md).

| Phase | Description | Status | Notes |
|---|---|---|---|
| 0 | Extraction pipeline + Gate 0 | **PASS** (2026-06-09) | See "Phase 0" section below |
| 1 | Agents A–E launched | **DONE** (2026-06-09) | 5 agents in parallel; see "Phases 1–2" below |
| 2 | Gate 1 self-checks | **PASS** (2026-06-09) | Agent self-checks + independent orchestrator re-runs |
| 3 | Gate 2 cross-file consistency | **PASS** (2026-06-09) | `build/data/gate2-report.md` |
| 4 | Gate 3 scripts | **PASS** (2026-06-09) | See "Gate 3" section below |
| 5 | SKILL.md + README + CHANGELOG + evals + Gate 4 validation | **PASS** (2026-06-10) | See "Phase 5" section below |
| 6 | Packaging + Gate 5 independent verification | **PASS** (2026-06-10) | Round 2 clean; packaged + install-tested |

## Gate 5 — Verification round 1 (2026-06-10)

Verifier V (fresh adversarial agent) report: `VERIFICATION-REPORT.md` (folder root). All
sources re-verified live (S5 MD5 match), 26-entry sample clean with 10 live confirmations,
independent name-sweep clean, scripts compile and are safety-gated. Findings and fixes:

| ID | Severity | Finding | Fix (2026-06-10) |
|---|---|---|---|
| BLK-1 | Blocker | `v3/.env` (credentials) would ship inside `portfolio123.skill` (packager has no `.env` exclusion) | `.env` moved out of `v3/` to the folder root; packaging will also stage a copy that never contains it |
| MAJ-1 | Major | `#Previous1`/`#GroupVar2` shipped as "verified scope constants" — PR #3 misparse of live-page footnote superscripts | Scope table rewritten with the 16 official constants verbatim from the dictionary; footnote restrictions kept as labeled official footnotes; whitelist entries removed |
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

## Gate 5 — Verification round 2 + packaging (2026-06-10)

- **Round 2: PASS, zero blockers/majors remaining, zero new findings** (fresh verifier;
  results appended to `VERIFICATION-REPORT.md` → "Round 2 — changed-scope re-verification").
  BLK-1/MAJ-1/MAJ-2 confirmed fixed with programmatic evidence (16-constant exact set match;
  eval-4 expectations traced to ranking-system-xml.md lines; no .env in v3/).
- **Packaging (plan/06 §7):** `v3/` staged as `build/stage/portfolio123/` (folder name drives
  the package name — the packager uses the directory name, not the frontmatter) and packaged
  with the official skill-creator tool → `portfolio123.skill` (184,679 B, replaces the stale
  v1 package at the folder root). Zip audit: 32 entries, single top-level `portfolio123/`
  dir, **no .env**, no evals/ (auto-excluded), no __pycache__.
- **Install test:** unzipped to a temp dir; `quick_validate.py` → "Skill is valid!"; all 16
  SKILL.md link targets (15 references + scripts/README.md) resolve in the unpacked tree.
- `p123_skill.zip` (broken internal layout, superseded) deleted per decision R5.5.
- Note: `v3/.env` was relocated to the folder root (outside the repo tree) — the owner's
  API credentials never ship in the package or the repo.

## Release checklist (owner actions — decision R5.3)

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
- [ ] Verify README install instructions against the final repo tree (no placeholders —
      verified in round 1/2, re-check after the repo copy).
- [ ] Optional: announcement (P123 forum / LinkedIn) — outside this plan's scope.

## Phase 5 — Skill assembly + Gate 4 (2026-06-10)

- `v3/SKILL.md` rewritten: frontmatter `name: portfolio123`, description 992 chars (limit
  1,024), no angle brackets, no DataMiner; body 205 lines (limit 500); routing table covers
  all 15 reference files + scripts/README.md; formula essentials with only
  dictionary-verified names (every name and signature checked against
  `dictionary-by-code.json` before inclusion — `DivPSA` was caught as nonexistent and
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
- **Gate 4: PASS** — official `quick_validate.py` (skill-creator tooling, copied to
  `build/tools/scripts/` from the plugin install; the S9 path `~/.claude/skills/` does not
  exist on this machine — substitution logged): "Skill is valid!"; evals schema-complete;
  DataMiner absent; routing complete.

## Phase 0 — Extraction pipeline (run 2026-06-09)

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
    Universe IDs, Time/Macro Series IDs, operators — all under Misc). They are NOT counted in
    the official 465/4,463 totals; marked `counted: false` in artifacts. 5,401 = 4,928 + 473.
  - 14 detail pages are login-gated ("An active subscription is required..."): the
    Industry & Sector classification factors (IndCode, Industry, RBICS, Sector, SubSector,
    UnivRBICS, ...). Listed in `build/data/details-skipped.json`; these ship as
    dictionary-sourced rows only. Success rate is computed over the 850 accessible pages.
  - doc_index.jsp has NO detail pages for Universe Operations (8 fn), Universe Filters
    (UnivExclude, UnivSubset), Benchmark Functions (BenchClose) — documented from dictionary
    signature/short_desc fields.
  - p123api master public-method count is **38** (programmatic AST count,
    `build/data/client-methods.json`), vs registry baseline "37 measured 2026-06-09".
    `stock_factor_info` has two `@overload` stubs + one implementation (deduped).
  - Live api-docs.yml re-fetched at build time: identical to the local copy.
- Agent input pre-fetch (`build/fetch_inputs.py`): p123api client.py/README/setup.py,
  ai-factor-reference.md (16,418 B — matches registry), PR #3/#4/#6 diffs → `build/inputs/`.
- Agent briefs written: `build/briefs/common.md` + `agent-A..E.md`. Agent working notes go to
  `build/notes/agent-X.md` (consolidated here by the orchestrator after Gate 1 — avoids
  concurrent writes to this file).

## Phases 1–2 — Build agents + Gate 1 (2026-06-09)

All 15 reference files + 11 script files built by agents A–E in parallel. Gate 1 self-checks
re-run independently by the orchestrator on every file: `check_names.py` exit 0 on all 15;
slice coverage 100% on all 13 category files (only nominal "misses": the two Misc operator
entries whose dictionary "code" is a symbol list — rendered as full operator tables instead);
33/33 API operations + 38/38 wrapper methods in api.md; all 10 scripts `py_compile` clean;
6/6 XML fences parse. Full agent notes: `build/notes/agent-{A..E}.md`.

**Adjudications (Gate 2 dispute registry — one verdict, evidence in agent notes):**

| Dispute | Verdict | Evidence |
|---|---|---|
| IsNA arity | `IsNA(expr1, expr2)` two-argument replacement; test NA with `expr = NA` | dictionary signature `expr1, expr2`; Misc/Math detail page; PR #4's own fix (Agent D) |
| PiotFScore vs PiotroskiF | `PiotFScore` | only `Piot*` code in dictionary (Agent C) |
| EstEPSCQ… vs CurFYEPSMean… | `CurFYEPSMean` family | `EstEPS*`/`EstSales*` count = 0 in dictionary (Agent C) |
| GetSeries vs DataSeries | `GetSeries` in formulas; `DataSeries`/`StockFactor` dropped as formula tokens | dictionary; api.md references the features by API method only (Agent A) |
| ##USR10YR / ##RBDI → RTWEXBGS | `##RBDI → RTWEXBGS` kept; `##USR10YR` mapping dropped (blank, with note) | FRED series name "Real Broad Dollar Index"; both rows shared numeric_id=1320 (Agent E) |
| Regional universe IDs (PR #6) | NOT shipped as verified (absent from dictionary); listed as PR-#6-reported only | Agents A + E independent checks |
| v1/v2 fabrications dropped | `AccrualsTTM`, `Streak`, `LatestRank`, `RegEst`, `DataSeries(...)` formula form; `SecCount` is VALID (`SectorCount` is not) | Agent D notes |
| AI Factor cost (R4.4) | Documented with both sources (spec `cost: 1` vs live-tested `20`); could NOT be resolved live — a predictor id from the owner's account is required and the API has no list-predictors operation. api.md advises budgeting 20 credits and confirming via the response's `cost`/`quotaRemaining`. Marker replaced 2026-06-09. | api.md → AI Factor |

## Gates 2–3 (2026-06-09)

- **Gate 2 PASS** (`build/gate2_checks.py`, report `build/data/gate2-report.md`): 0 wrong-name
  contradictions across all 15 files; slice coverage 100% on all 13 category files (the six Misc
  operator entries with symbol-list codes are rendered as operator tables — manually verified);
  0 bad relative links; all 13 header coverage lines match slice counts. Tooling note: the
  name-token regex was extended for mid-token `#` codes (`EPS#Positive`, `Inst#ShsOwn`...).
- **Gate 3 PASS:**
  - Compile: `py_compile` clean on all 10 script files.
  - Static sanity: 13 distinct `client.*` methods used by scripts, all present in the
    programmatic method list (`build/verify_scripts_static.py`); Agent A cross-checked every
    params key against api-docs.yml + client.py (no disagreements on keys actually used).
  - **Live smoke (read-only, owner credentials from v3/.env mapped to P123_API_ID/P123_API_KEY):**
    1. `01_auth_check.py` — PASS (authentication succeeded, Bearer token obtained). No cost.
    2. `07_price_history.py --start 2026-05-01 --end 2026-05-15` — PASS (IBM, 11 rows of EOD
       bars returned). Free-trial ticker; no cost surfaced by the wrapper's pandas path.
    3. `02_screen_run.py --universe SP500 --rule "Close(0) > 200" --max-holdings 10` — PASS
       (10 rows returned, payload shape per PR #6: no per-rule `type`).
    No mutating call was executed (script 09 not run beyond `--help`-level checks; Ground Rule 5).
  - R4.4 outcome recorded above; api.md and script 08 docstring consistent.

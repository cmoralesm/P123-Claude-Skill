# Build State Tracker

Claude Code: update this file after completing each phase/gate (see ../PLAN.md).

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

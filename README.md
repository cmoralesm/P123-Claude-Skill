# Portfolio123 Claude Skill

![Portfolio123 Claude Skill](https://raw.githubusercontent.com/cmoralesm/P123-Claude-Skill/main/docs/p123-skill.jpg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cmoralesm/P123-Claude-Skill/blob/main/LICENSE)

> **Built by a Verified Portfolio123 Coach and Consultant.** Carlos Morales runs
> [QuantSolvings](https://quantsolvings.com/), a boutique quantitative practice in factor investing
> for equities: [coaching](https://quantsolvings.com/coaching/),
> [consulting](https://quantsolvings.com/consulting/) and
> [team training](https://quantsolvings.com/training/) on Portfolio123.
> [Book a free 45-minute introductory call](https://quantsolvings.com/contact/).

A [Claude Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that turns
Claude into a reliable Portfolio123 (P123) assistant: writing screen rules and formulas,
building ranking-system XML, replicating published factors, and pulling data through the REST API
with the official `p123api` Python wrapper.

**v4.1.0** is the first public release since v3.0.0, and it carries two releases' worth of work.

**New in 4.1** - a factor-replication reference and an API refresh:

- **`references/factor-replication.md`** (new): 35 recipes across value, quality, earnings quality,
  momentum, low risk, size and investment/issuance, each with the P123 implementation, the ranking
  node's direction and scope, and the translation traps. No performance figures appear anywhere in
  it, by design: an unverifiable alpha is an invented fact. Seven constructions P123 genuinely
  cannot reproduce are listed as such, with the closest honest proxy instead of a fake.
- **The REST API surface is current again.** P123 added six operations on 2026-08-28 -
  `GET /dataSeries`, `GET /rank`, `POST /rank/create`, `GET /strategy`, `POST /strategy/{id}/copy`
  and `POST /strategy/{id}/copy-book` - plus the `preproc` machine-learning block on
  `POST /data/universe` and an extended currency enum. `references/api.md` now documents all
  **32 paths / 39 operations** of the 2026-09-03 spec capture.
- **The `GET /dataSeries` correction.** v4.0.0 stated that P123 had no Data Series read operation
  and used that absence to explain a reported `405`. That is no longer true, and the file says so
  in those words rather than quietly deleting the passage.
- **`p123api` 3.1.0**, verified method by method: all **44 public client methods**, the nine that
  now return typed objects instead of dicts, the four keyword-only lookups, and a 2.x-to-3.x
  migration table.

**From 4.0.0** (finished but never published) - four defects found by a P123 practitioner using the
skill on live research work: the `^` power operator is now the documented idiom for powers and
roots (P123 has no square-root and no exponential function), `SetVar`/`ShowVar` are documented as
always returning TRUE so assignments get inlined instead of wrapped in a dead `Eval` branch,
`Weight="0"` on a ranking-system node is documented as legal "equal weight" rather than an error to
fix, and the `p123api` upload methods are documented with their real snake_case kwargs. Full
details: [CHANGELOG.md](CHANGELOG.md).

The v3.0.0 foundation is unchanged - **full dictionary coverage**: every entry of P123's
official Factor Reference, extracted and verified programmatically on 2026-06-09, totalling
**4,463 factors and 465 functions** across the 13 official categories, plus 473
constants/series-IDs/operators.

> Independent community project. The **author** is a Verified Portfolio123 Coach and Consultant;
> **the skill itself** is not affiliated with, sponsored by, or endorsed by Portfolio123, Inc.
> All factor/function names and documentation excerpts belong to their respective owners.

## What's inside

```
portfolio123/
├── SKILL.md                      # Trigger description, routing table, anti-hallucination table
├── references/
│   ├── api.md                    # REST API + p123api wrapper (39 operations, 44 methods)
│   ├── ratios-statistics.md      # 60 functions / 1,206 factors
│   ├── financials.md             # 101 functions / 2,739 factors + vendor line-item mapping
│   ├── fundamentals.md           # 61 functions / 124 factors
│   ├── estimates.md              # 20 functions / 158 factors
│   ├── technical.md              # 95 functions / 55 factors
│   ├── advanced-functions.md     # 60 functions / 11 factors (FRank, FHist, Loops, ...)
│   ├── strategy.md               # 4 functions / 51 factors + buy/sell rule patterns
│   ├── universe-operations.md    # 8 functions
│   ├── universe-filters.md       # 3 functions
│   ├── benchmark-functions.md    # 1 function
│   ├── industry-sector.md        # 1 function / 91 factors (RBICS classification)
│   ├── taxonomy.md               # 8 functions / 8 factors (ETF vocabularies)
│   ├── misc.md                   # 43 functions / 20 factors + 473 constants, series IDs, operators
│   ├── factor-replication.md     # 35 published-factor recipes, node direction/scope, traps
│   └── ranking-system-xml.md     # Validated ranking XML schema; always read before XML work
├── scripts/                      # 9 runnable CLI examples + p123_helpers.py (see scripts/README.md)
├── docs/                         # repository assets (excluded from the .skill package)
├── BUILD-STATE.md                # build & verification log for this release
├── README.md · CHANGELOG.md · LICENSE · .gitignore
```

Every factor and function name in the 16 reference files was validated against the extracted
dictionary; "Common Mistakes" tables in each file list the names people (and language models)
invent that do **not** exist, next to the verified correct ones.

## Install

### Claude Code

```bash
# from this repo's root
mkdir -p ~/.claude/skills
cp -r . ~/.claude/skills/portfolio123
```

Or install the packaged `portfolio123.skill` (a zip): unzip it into `~/.claude/skills/`.
Project-scoped install: use `.claude/skills/portfolio123` inside your project instead.

### claude.ai (web/desktop)

Settings → Capabilities → Skills → **Upload skill** → select `portfolio123.skill`.
(A paid plan with code execution enabled is required for skills.)

### Cursor

Cursor reads agent instructions from `AGENTS.md`/rule files rather than Claude skills.
Two working options:

1. Copy the repo into your project (e.g. `docs/p123-skill/`) and add a Cursor rule
   (`.cursor/rules/p123.mdc`) that says: "For any Portfolio123/P123 task, read
   `docs/p123-skill/SKILL.md` first and follow its routing table to the reference files."
2. Or paste the contents of `SKILL.md` into your project rules and keep `references/`
   in the workspace so the agent can open them.

### Codex (OpenAI)

Same pattern as Cursor: place this folder in your workspace and add to `AGENTS.md`:
"For Portfolio123/P123 work, read `p123-skill/SKILL.md` and follow its routing table."

## Using the example scripts

```bash
pip install "p123api[pandas]"         # p123api 3.1.0 needs Python 3.10+; pandas is an extra
export P123_API_ID=your_api_id        # PowerShell: $env:P123_API_ID = "..."
export P123_API_KEY=your_api_key
python scripts/01_auth_check.py
python scripts/02_screen_run.py --universe SP500 --rule "Close(0) > 200" --max-holdings 10
python scripts/07_price_history.py    # IBM by default
```

The `[pandas]` extra matters: since `p123api` 3.0 pandas is optional and imported lazily, so
without it every `to_pandas=True` example fails at call time rather than at import.

API credentials: P123 Account Settings → API (paying subscription required; the spec's free
trial covers `/data` only, for IBM, MSFT and INTC with 5 years of history - `/data/universe`
carries no such clause and needs a data license).
All scripts are read-only except `09_strategy_rebalance_dryrun.py`, which changes nothing
unless run with `--execute` and a typed confirmation. See [scripts/README.md](scripts/README.md).

## Example prompts

- "Write a P123 screen for profitable small caps under 15x earnings with improving margins."
- "Build a 4-node value/quality ranking system as XML."
- "Why does my rule `Eval(IsNA(PEExclXorTTM), ...)` fail on P123?"
- "How do I take a square root in a P123 formula?"
- "Review this ranking system XML - my composite's children all have `Weight="0"`."
- "Implement Novy-Marx gross profitability as a ranking node - which denominator, which scope?"
- "Replicate 12-1 momentum and Sloan accruals on P123, and tell me where the translation breaks."
- "Download PE, ROE and 12-month momentum for the SP500 universe as a DataFrame."
- "Look up my P123 data series by name with `p123api` and read the id off the result."
- "What is the P123 factor for the Piotroski score, and how do I rank on it?"

## Accuracy & verification

- Source of truth: the official Factor Reference (`doc_factors.jsp`, 2026-06-09 extraction),
  the official `doc_detail.jsp` pages (850 full-detail pages parsed), the official OpenAPI
  spec (captured from `api.portfolio123.com` on 2026-09-03: 32 paths, 39 operations, 9 tags,
  111 component schemas), and the installed `p123api` 3.1.0 wrapper source.
- Category counts in every reference file header match the extraction report exactly.
- A name-validation pass gates every file and is green on all 19 shipped markdown files - the 16
  reference files plus `SKILL.md`, `scripts/README.md` and this README: backticked identifiers must
  exist in the extracted dictionary, except in the "Wrong (do not use)" column of a Common
  Mistakes table and for the non-P123 tokens each file declares in a `name-whitelist` comment
  (Python kwargs, API schema fields, XML attribute names). Prose that names an invented function
  as a trap says so without backticking it, so the gate keeps its teeth.
- `references/factor-replication.md` carries **no performance figures at all** - no alphas, no
  t-statistics, no return magnitudes. The skill exists to stop invented facts, and none of those
  numbers is verifiable from its sources. Where P123 cannot reproduce a published construction,
  the file says so and gives the proxy.
- Scripts compile and their happy paths were exercised live (read-only) before the 4.0.0 release.
  The 4.1 script changes are documentation, install guidance and one optional `print_quota`
  parameter; they were re-verified by compilation, not by new live calls.
- Known gaps are documented inline: 14 Industry & Sector classification detail pages are
  login-gated on P123's site (covered from dictionary data); the AI Factor per-call credit
  cost is documented with both conflicting official sources.
- The v4.0.0 corrections came from live production use. Formula semantics were re-verified
  against the 2026-06-09 detail-page extraction, and every wrapper signature against the
  installed `p123api` source plus the OpenAPI spec. Two items could not be: the
  ranking-node weight rule rests on the reporter's quotation of P123's `[0] - 100` weight range,
  and the `data_series_info` 405 on a single observation from their licensed account. The Factor
  Reference does not cover ranking-system XML and the spec has no node-weight schema, so
  this is the same provenance as the XML schema itself - disclosed in
  [BUILD-STATE.md](BUILD-STATE.md) (NEW-4) and [CHANGELOG.md](CHANGELOG.md) §Credits.
- `api.md` is verified against `p123api` 3.1.0, read from the installed source; where 2.x differs
  it says so in a migration table rather than assuming the reader has upgraded. Two spec-versus-
  wrapper disagreements are stated as unresolved rather than adjudicated, because settling each
  needs one live call: the return shape of `POST /rank/create` and the XML field name on
  `GET /rank`.

## Contributing

Issues and PRs welcome. Ground rule for content changes: every factor/function name must be
verifiable against the official Factor Reference - PRs that add unverified names will be
asked to include the verification evidence. Performance claims are not accepted at all.

## Work with me

If you or your team build systematic strategies on Portfolio123, this is what I do for a living:
[coaching](https://quantsolvings.com/coaching/) for individual quants,
[consulting](https://quantsolvings.com/consulting/) on ranking systems, screens and portfolio
construction, and [team training](https://quantsolvings.com/training/).
[Book a free 45-minute introductory call](https://quantsolvings.com/contact/).

The [QuantSolvings Factors page](https://quantsolvings.com/factors/) publishes daily simulated
equity curves for the classic factors (value, momentum, quality, earnings revisions, low beta,
size) on the 1,000 largest US stocks and the 2,000 below them since 2000, long-only and
long-short. Free, updated every weekday, and a useful sanity check before trusting any backtest.

## License

[MIT](LICENSE), copyright [QuantSolvings](https://quantsolvings.com).

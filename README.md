# Portfolio123 Claude Skill

A [Claude Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that turns
Claude into a reliable Portfolio123 (P123) assistant: writing screen rules and formulas,
building ranking-system XML, and pulling data through the REST API with the official
`p123api` Python wrapper.

**v3.0.0** is a ground-up rebuild with **full dictionary coverage**: every entry of P123's
official Factor Reference, extracted and verified programmatically on 2026-06-09 —
**4,463 factors and 465 functions** across the 13 official categories, plus 473
constants/series-IDs/operators, the complete REST API surface (28 paths, 33 operations), and
all 38 public `p123api` client methods.

> Independent community project. Not affiliated with, sponsored by, or endorsed by
> Portfolio123, Inc. All factor/function names and documentation excerpts belong to their
> respective owners.

## What's inside

```
portfolio123/
├── SKILL.md                      # Trigger description, routing table, anti-hallucination table
├── references/
│   ├── api.md                    # REST API + p123api wrapper (33 operations, 38 methods)
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
│   └── ranking-system-xml.md     # Validated ranking XML schema — always read before XML work
├── scripts/                      # 9 runnable CLI examples + p123_helpers.py (see scripts/README.md)
├── evals/evals.json              # 12 evaluation prompts (repo only; excluded from the .skill package)
├── BUILD-STATE.md                # build & verification log for this release
├── README.md · CHANGELOG.md · LICENSE · .gitignore
```

Every factor and function name in the reference files was validated against the extracted
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
pip install p123api pandas
export P123_API_ID=your_api_id        # PowerShell: $env:P123_API_ID = "..."
export P123_API_KEY=your_api_key
python scripts/01_auth_check.py
python scripts/02_screen_run.py --universe SP500 --rule "Close(0) > 200" --max-holdings 10
python scripts/07_price_history.py    # IBM by default — works on the API free trial
```

API credentials: P123 Account Settings → API (paying subscription required; the spec's free
trial covers `/data` and `/data/universe` for IBM, MSFT and INTC with 5 years of history).
All scripts are read-only except `09_strategy_rebalance_dryrun.py`, which changes nothing
unless run with `--execute` and a typed confirmation. See [scripts/README.md](scripts/README.md).

## Example prompts

- "Write a P123 screen for profitable small caps under 15x earnings with improving margins."
- "Build a 4-node value/quality ranking system as XML."
- "Why does my rule `Eval(IsNA(PEExclXorTTM), ...)` fail on P123?"
- "Download PE, ROE and 12-month momentum for the SP500 universe as a DataFrame."
- "What is the P123 factor for the Piotroski score, and how do I rank on it?"

## Accuracy & verification

- Source of truth: the official Factor Reference (`doc_factors.jsp`, 2026-06-09 extraction),
  the official `doc_detail.jsp` pages (850 full-detail pages parsed), the official OpenAPI
  spec (verified identical to `api-docs.yml` served live), and the `p123api` wrapper source.
- Category counts in every reference file header match the extraction report exactly.
- A name-validation pass gates every file: all backticked identifiers must exist in the
  extracted dictionary (wrong-side names are allowed only inside Common Mistakes tables).
- Scripts compile and their happy paths were exercised live (read-only) before release.
- Known gaps are documented inline: 14 Industry & Sector classification detail pages are
  login-gated on P123's site (covered from dictionary data); the AI Factor per-call credit
  cost is documented with both conflicting official sources.

## Contributing

Issues and PRs welcome. Ground rule for content changes: every factor/function name must be
verifiable against the official Factor Reference — PRs that add unverified names will be
asked to include the verification evidence.

## License

[MIT](LICENSE) — copyright QuantSolvings.

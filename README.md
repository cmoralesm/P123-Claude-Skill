# Portfolio123 Agent Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/)
[![Works with](https://img.shields.io/badge/Works_with-Claude_Code_%7C_Cursor_%7C_Codex-blue.svg)](#installation)
[![Functions](https://img.shields.io/badge/Functions-464+-brightgreen.svg)](#whats-covered)
[![Factors](https://img.shields.io/badge/Factors-4456+-orange.svg)](#whats-covered)

A comprehensive [Agent Skill](https://agentskills.io/) for **[Portfolio123](https://www.portfolio123.com/)** — the systematic/quantitative equity research platform. This skill gives your AI coding agent deep knowledge of the P123 formula language, ranking systems, screening rules, backtesting, and the `p123api` Python wrapper.

Built for quant researchers, factor investors, and anyone who uses P123 programmatically.

---

## Why Use This?

Portfolio123 has its own formula language with 464+ functions, 4456+ factors, and platform-specific conventions that differ from standard financial terminology (e.g., `DbtLT` not `LTDebt`, `Hi()` not `High()`, `OperCashFl` not `OpCashFl`). Without a dedicated skill, AI agents routinely hallucinate incorrect function names, wrong parameter orders, and non-existent syntax.

This skill was cross-referenced line-by-line against the official [P123 528-page syntax reference](https://www.portfolio123.com/doc/doc_factors.jsp) and the [REST API documentation](https://api.portfolio123.com/docs/index.html) to ensure every function name, parameter, and example is accurate.

---

## What's Covered

| Reference File | Lines | Content |
|---------------|-------|---------|
| `SKILL.md` | ~225 | Entry point, key concepts, naming gotchas, quick-start examples |
| `formula-quick-reference.md` | ~392 | Syntax, operators, SetVar, Eval, FRank, ZScore, FHist, NA handling, common patterns |
| `factors-and-functions/index.md` | ~398 | An index file with all categories and subcategories directly from the P123 Factor & Function Reference page. Links to specific reference files for each category |
| `factors-and-functions/*.md` | ~MANY | A reference file per top level category as seen in the [P123 Factor & Function Reference](https://www.portfolio123.com/doc/doc_factors.jsp). Should contain every factor in that reference page. |
| `api-reference.md` | ~773 | Full `p123api` Python wrapper: data, rank, screen, strategy & books, data series, stock factors, AI Factor |
| `ai-factor-reference.md` | ~441 | AI Factor ML predictions: parameters, response schema, feature extraction, operational gotchas |

**Total: ~3,625 lines of reference material.**

### Key areas:

- **Formula Language** — Every function signature verified: fundamentals (`Sales()`, `DbtLT()`, `OperCashFl()`), technical (`RSI()`, `MACDD()`, `BetaFunc()`), advanced (`FRank()`, `FHistAvg()`, `LoopAvg()`, `LinReg()`)
- **Pre-built Factors** — Naming patterns for 4,456+ auto-generated factors (growth, regression, per-share, ratios)
- **Ranking Systems** — XML text-editor format, `NodeRank()`, `Rating()`, bucket performance testing
- **Python API** — Complete `p123api` wrapper documentation with code examples for every endpoint
- **Common Pitfalls** — Mapping table of 30+ common financial terms to their actual P123 function names
- **Factor Strategy Patterns** — Value, momentum, quality, low-vol, BAB, Piotroski F-Score, earnings momentum

---

## Installation

### Claude Code (recommended)

```bash
git clone https://github.com/YOUR_USER/P123-Claude-Skill.git
cp -r P123-Claude-Skill ~/.claude/skills/portfolio123/
```

Or from the `.skill` package:

```bash
unzip portfolio123.skill -d ~/.claude/skills/portfolio123/
```

### Cursor

```bash
cp -r portfolio123-skill ~/.cursor/skills/portfolio123/
```

### Codex / Gemini CLI

```bash
cp -r portfolio123-skill ~/.codex/skills/portfolio123/
# or
cp -r portfolio123-skill ~/.gemini/skills/portfolio123/
```

### Project-level (scoped to a single repo)

```bash
cp -r portfolio123-skill .claude/skills/portfolio123/
```

Once installed, your AI agent will automatically use the skill when you mention P123 formulas, ranking systems, screens, backtests, or API calls.

---

## Skill Structure

```
portfolio123/
├── SKILL.md                              # Entry point (always loaded)
└── references/                           # Loaded on demand
    ├── formula-quick-reference.md        # Syntax, operators, patterns
    ├── api-reference.md                  # p123api Python wrapper
    ├── ai-factor-reference.md            # AI Factor ML predictions
    ├── factors-and-functions/index.md    # Factors and Functions Index by category/sub-category
    └── factors-and-functions/*.md        # Factors broken out by category
```

The skill follows the [Agent Skills](https://agentskills.io/) standard with progressive disclosure: `SKILL.md` is always in context (~225 lines), and reference files are loaded only when relevant to the task.

---

## Example Prompts

Once the skill is installed, you can ask your agent things like:

```
Write a P123 screen that finds cheap, high-quality stocks with positive momentum
in the Russell 3000, excluding financials and REITs.
```

```
Build a ranking system XML with 4 nodes: Value (30%), Momentum (25%),
Quality (25%), and Low Volatility (20%). Use the best P123 factors for each.
```

```
Write Python code using p123api to download weekly factor data for the S&P 500
including PE, ROE, 12-1 month momentum, and market cap, normalized with rank scaling.
```

```
Replicate the Betting Against Beta (BAB) factor from Frazzini-Pedersen
using P123 functions. Include beta calculation, ranking, and hedging logic.
```

```
Create a P123 strategy sell rule with a 20% trailing stop that only triggers
if the benchmark hasn't also dropped by the same amount.
```

---

## Accuracy Notes

Every function in this skill was verified against:

1. **P123 Syntax Reference PDF** (528 pages, v1.0 2026-02-25) — the complete formula/factor dictionary exported from Portfolio123
2. **[Factor & Function Browser](https://www.portfolio123.com/doc/doc_factors.jsp)** — the live online reference (4,456 factors, 464 functions)
3. **[p123api Help Center](https://portfolio123.customerly.help/en/dataminer-api/the-api-wrapper-p123api)** — official API wrapper documentation

Common errors corrected vs. typical AI hallucinations:

| AI Hallucination | Correct P123 Syntax |
|-----------------|-------------------|
| `High()`, `Volume()` | `Hi()`, `Vol()` |
| `COGS()`, `SGA()` | `CostG()`, `SGandA()` |
| `LTDebt()`, `TotDebt()` | `DbtLT()`, `DbtTot()` |
| `OpCashFl()` | `OperCashFl()` |
| `MACDHist()`, `MACDSig()` | `MACDD(short, long, period)` |
| `PlusDI()`, `MinusDI()` | `DMIPlus()`, `DMIMinus()` |
| `FHist()` returns average | `FHist()` = point-in-time; `FHistAvg()` = average |
| `Aggregate(..., #Median)` | `FMedian()` (Aggregate only supports `#Avg`/`#CapAvg`) |
| `FRank(..., #Asc, #NANeg)` | `FRank(..., #ASC, #InclNA)` |

---

## Contributing

Contributions are welcome. If you find an incorrect function name, missing parameter, or outdated API behavior:

1. Fork the repository
2. Create a branch (`git checkout -b fix/function-name`)
3. Verify your change against the [P123 Factor Browser](https://www.portfolio123.com/doc/doc_factors.jsp)
4. Submit a pull request with a reference to the official documentation

---

## Related Resources

- [Portfolio123](https://www.portfolio123.com/) — The platform itself
- [P123 API Swagger](https://api.portfolio123.com/docs/index.html) — REST API reference
- [P123 Help Center](https://portfolio123.customerly.help/en) — Official documentation
- [P123 Community Forum](https://community.portfolio123.com/) — Community discussions
- [p123api on PyPI](https://pypi.org/project/p123api/) — Python wrapper package
- [DataMiner Google Colab Examples](https://drive.google.com/drive/u/0/folders/1F3geOi2IYIbdb9obDj8U_o2aDTjw6Fpr) — Official notebook examples
- [Agent Skills Standard](https://agentskills.io/) — The open standard this skill follows

---

## Disclaimer

This skill is an independent community project and is **not officially affiliated with or endorsed by Portfolio123, Inc.** Portfolio123 is a trademark of Portfolio123, Inc. The skill provides documentation references to assist AI coding agents; always verify formulas against the official P123 documentation.

---

## License

[MIT](LICENSE)

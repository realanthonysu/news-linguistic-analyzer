# 🗞️ news-linguistic-analyzer

> English News Translation & Deep Linguistic Analysis

[CN](README.md) · EN

## Features

This Skill provides English-to-Chinese news translation and multi-dimensional linguistic analysis for AI coding assistants like **Qwen Code** and **Claude Code**. Given an English news article, it automatically executes the following **6-step standardized workflow**:

| Step | Module | Description |
|:--:|------|------|
| 📝 | Chinese Translation | Accurate, news-style segmented translation with heading hierarchy and built-in information-point verification |
| 🔍 | Lexical Analysis | Contextual interpretation of 5-8 key terms/phrases (table format) |
| 🧱 | Sentence Structure Breakdown | Component annotation of typical long sentences with CN-EN logic comparison |
| 📐 | Grammar Analysis | Tense, voice, participles, source attribution, and other features |
| 💡 | Translation Tips | 3-5 practical tips (original example + processing rationale) |
| 🌍 | Extended Reflection | Critical perspective on reporting ethics and media literacy |

Additionally, the Skill supports:
- 🎯 **Domain Adaptation**: Auto-supplements background notes for 10 domains: finance, sports, tech, geopolitics, healthcare, climate & environment, law & justice, education & research, military & defense, social & civic issues
- 🛡️ **Fact Checking**: Detects future dates, fictional content, AI-generated markers and auto-warns
- 🔄 **Multi-Mode Output**: Switch analysis depth with `translation only` / `brief` / `no reflection` commands
-  **Batch Processing**: Input multiple articles at once, auto-numbered and segmented analysis
- 📄 **Long-Text Processing**: For articles >2000 words, uses topic-aware segmentation with context bridging and full-text synthesis
- 🔐 **Input Security Validation**: Built-in input size limits and path validation

## Installation

Choose one of the following two methods:

### Method 1: Let Agent Install Directly (Recommended)

Send this repository link to AI assistants that support Agent Skills (Qwen Code, Claude Code, etc.):

```text
Please install this Skill: https://github.com/realanthonysu/news-linguistic-analyzer
```

The Agent will automatically clone it to `~/.qwen/skills/news-linguistic-analyzer/` and load it.

### Method 2: Install via npx skills Command

```bash
npx skills add https://github.com/realanthonysu/news-linguistic-analyzer --skill news-linguistic-analyzer
```

After installation, refresh the Agent (run `/skills` to confirm `news-linguistic-analyzer` appears in the list).

## Quick Start

Trigger by sending an English news text, for example:

- Explicit trigger (recommended)
```bash
/news-linguistic-analyzer Standoff and Peace Talks: Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports.
```

- Implicit trigger
```text
Iran Standoff and Peace Talks: Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports.
```

The Skill will automatically output: **Chinese Translation → Lexical Analysis → Sentence Breakdown → Grammar Analysis → Translation Tips → Extended Reflection**

## Directory Structure

```
news-linguistic-analyzer/
├── SKILL.md              # Core instruction file (YAML metadata + Markdown directives)
├── README.md             # Chinese documentation (中文文档)
├── README.en.md          # This file (English documentation)
├── LICENSE               # MIT License
├── scripts/
│   └── validate-input.py # Input pre-validation script (CLI tool)
├── references/
│   ├── domain-adaptation.md    # Domain adaptation (10 domains triggers & notes)
│   ├── edge-cases.md           # Edge cases & fallback strategies
│   ├── examples.md             # Input/output examples (5 scenarios)
│   ├── long-text-processing.md # Long-text processing rules
│   ├── news-sources.md         # 19 news sources identification table
│   ├── output-format.md        # Detailed output format specification
│   └── quality-checklist.md    # Quality assurance checklist
└── assets/               # (Reserved) Templates and resource files
```

## Documentation

- Full analysis workflow & specifications: [SKILL.md](SKILL.md)
- Output format template: [references/output-format.md](references/output-format.md)
- Quality checklist: [references/quality-checklist.md](references/quality-checklist.md)
- Input/output examples (5 scenarios): [references/examples.md](references/examples.md)

## Changelog

### v1.4.1 (2026-05-21)
- 🔧 Rewrote SKILL.md description: switched to third person, added natural language triggers (English + Chinese), added negative triggers to prevent false activation, aligned with Anthropic official skill spec

### v1.4.0 (2026-05-20)
- 🚨 Fact-check trigger logic refactored to **two tiers**: mandatory triggers (6 conditions) + model assessment fallback
- 🔍 Mandatory triggers expanded: any specific date (past/future), person+major event, casualty/loss data, ongoing major events, factual conflicts, fiction markers
- 🧠 Added second-tier "model self-assessment": when no clear trigger is met, evaluate if event exceeds knowledge cutoff or carries misinformation risk

### v1.3.3 (2026-05-20)
- 🏗️ Domain adaptation table (10 domains) moved to `references/domain-adaptation.md`, SKILL.md retains domain name list only
- 📝 Unified all output title emojis to 📝 (translation step), eliminating 📜 inconsistency

### v1.3.2 (2026-05-20)
- 📝 Fixed "ReDoS protection" claim in README to accurate description ("input size limits and path validation")
- 🔧 Expanded geo_event regex in validate-input.py to 14 event types (added election/summit/protest/deal/attack/crisis/conflict/agreement/sanctions/referendum)
- 🙈 Added `.claude/` to .gitignore to exclude local IDE configuration
- ✅ quality-checklist.md synced with new mode conflict priority check item
- 🔧 validate-input.py news sources now dynamically loaded from news-sources.md, eliminating dual maintenance

### v1.3.1 (2026-05-20)
- 🌐 Input validation temp file path switched to cross-platform solution (Python tempfile), compatible with Windows/Linux/macOS
- 🔧 validate-input.py news source matching now uses word-boundary regex (`\b`), preventing false matches like `AP` in `APPROACH`
- 🛡️ Added web search / web fetch unavailability fallback scenarios to edge-cases.md
- 🎨 Added missing emoji markers to README feature table, aligned with SKILL.md core workflow table

### v1.3.0 (2026-05-20)
- 📋 Clarified validate-input.py Agent invocation path, added temp file steps and inline judgment rules
- 📐 Eliminated content duplication between output-format.md and long-text-processing.md, replaced with cross-reference
- 📝 Added complete 6-step end-to-end output for Example 1, providing format anchor
- ⚖️ Added mode conflict priority rule: translation only > brief > no reflection > default full mode

### v1.2.3 (2026-05-20)
- 🔧 Added `web_fetch` to `tools_required` in YAML metadata, explicitly declaring tool dependencies
- 🛡️ Upgraded online verification fallback to **3-tier**: web search (primary) → web fetch (secondary) → offline annotation (fallback)

### v1.2.2 (2026-05-20)
- 🔧 Added `tools_required: [web_search]` to YAML metadata, explicitly declaring tool dependencies
- 🔍 Fact-check search queries now use **bilingual strategy**: English first, then Chinese cross-verification
- 🛡️ Added fallback strategy when web search is unavailable
- 📝 Fixed README directory structure, added 3 missing files under `references/`
- 📝 Fixed tree-drawing characters in README.en.md directory structure

### v1.2.1 (2026-05-20)
- 🚨 Fact checking elevated to **mandatory pre-step**, ensuring date validation and web search execute before translation
- 🎨 Fixed Keycap emoji (1️, etc.) rendering as boxes in Windows terminals, unified to standard emoji
- 📐 Added emoji marker for grammar analysis step (📐)
- Added emoji marker column to SKILL.md core workflow table, synced with output-format.md

### v1.2.0 (2026-05-19)
- SKILL.md streamlined from 237 to ~130 lines, compliant with <5000 tokens convention
- News source table (19 sources) moved to `references/news-sources.md`
- Long-text processing rules moved to `references/long-text-processing.md`
- Edge case handling + error fallback strategies moved to `references/edge-cases.md`
- Added translation information-point verification feature
- Domain adaptation expanded to 10 domains

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this Skill without any restrictions.

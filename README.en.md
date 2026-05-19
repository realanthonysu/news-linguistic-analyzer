# 🗞️ news-linguistic-analyzer

> English News Translation & Deep Linguistic Analysis

[🇨🇳 中文](README.md) · 🇬🇧 English

## Features

This Skill provides English-to-Chinese news translation and multi-dimensional linguistic analysis for AI coding assistants like **Qwen Code** and **Claude Code**. Given an English news article, it automatically executes the following **6-step standardized workflow**:

| Step | Module | Description |
|:--:|------|------|
| 1️⃣ | Chinese Translation | 📝 Accurate, news-style segmented translation with heading hierarchy preserved |
| 2️⃣ | Lexical Analysis | 🔍 Contextual interpretation of 5-8 key terms/phrases (table format) |
| 3️⃣ | Sentence Structure Breakdown | 🔨 Component annotation of typical long sentences with CN-EN logic comparison |
| 4️⃣ | Grammar Analysis | 📊 Tense, voice, participles, source attribution, and other features |
| 5️⃣ | Translation Tips | 💡 3-5 practical tips (original example + processing rationale) |
| 6️⃣ | Extended Reflection | 🌍 Critical perspective on reporting ethics and media literacy |

Additionally, the Skill supports:
- 🎯 **Domain Adaptation**: Auto-supplements background notes for finance, sports, tech, geopolitics keywords
- 🛡️ **Fact Checking**: Detects future dates, fictional content, AI-generated markers and auto-warns
- 🔄 **Multi-Mode Output**: Switch analysis depth with `translation only` / `brief` / `no reflection` commands
- 📦 **Batch Processing**: Input multiple articles at once, auto-numbered and segmented analysis

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
│   ├── output-format.md  # Detailed output format specification
│   ├── quality-checklist.md  # Quality assurance checklist
│   └── examples.md       # Input/output examples (5 scenarios)
└── assets/               # (Reserved) Templates and resource files
```

## Documentation

- Full analysis workflow & specifications: [SKILL.md](SKILL.md)
- Output format template: [references/output-format.md](references/output-format.md)
- Quality checklist: [references/quality-checklist.md](references/quality-checklist.md)
- Input/output examples (5 scenarios): [references/examples.md](references/examples.md)

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this Skill without any restrictions.

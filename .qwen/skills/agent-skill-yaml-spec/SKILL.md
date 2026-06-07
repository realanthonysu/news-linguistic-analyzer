---
name: agent-skill-yaml-spec
description: Agent Skill SKILL.md YAML frontmatter 规范速查 — 必需字段、可选字段、约束条件与合规模板
source: auto-skill
extracted_at: '2026-05-31T08:59:51.817Z'
---

# Agent Skill YAML Frontmatter 规范速查

> 来源：agentskills.io 开放标准（2026 年 3 月最新版）

## 字段总览

| 字段 | 状态 | 用途 | 约束 |
|------|------|------|------|
| `name` | **必需** | 技能唯一标识符 | 1-64 字符；仅小写字母 `a-z`、数字 `0-9`、连字符 `-`；不能以 `-` 开头/结尾；不能连续 `--`；必须与父目录名匹配 |
| `description` | **必需** | 描述功能与触发时机 | 1-1024 字符；非空；必须具体，禁止模糊误导 |
| `license` | 可选 | 开源许可证 | 建议保持简短（如 `MIT`、`Apache-2.0`） |
| `compatibility` | 可选 | 环境要求（工具依赖、系统包、网络访问等） | 1-500 字符；仅在特定环境要求时使用 |
| `metadata` | 可选 | 任意额外键值对 | 键和值均为字符串；建议键名唯一避免冲突 |
| `allowed-tools` | 可选（**实验性**） | 预批准可使用的工具列表 | 空格分隔的字符串（如 `"web_search web_fetch"`）；不同 Agent 支持情况可能不同 |

## 命名红线

- ❌ 禁止大写、空格、下划线、特殊字符
- ❌ 禁止以 `-` 开头或结尾
- ❌ 禁止连续 `--`

## 合规模板

### 最小合规版本

```yaml
---
name: my-skill-name
description: 描述功能与何时触发此技能
---
```

### 完整推荐版本

```yaml
---
name: my-skill-name
description: 描述功能与何时触发此技能，包含自然语言触发词
compatibility: "Requires web_search and web_fetch tools. Python 3.8+ for scripts."
allowed-tools: "web_search web_fetch"
metadata:
  author: your-name
  version: "1.0.0"
license: MIT
---
```

## 字段放置约定

| 字段 | 推荐位置 | 说明 |
|------|---------|------|
| `name` / `description` / `license` | 顶层 | 官方标准字段 |
| `compatibility` / `allowed-tools` | 顶层 | 官方标准字段（allowed-tools 为实验性） |
| `version` / `author` | `metadata` 下 | 非顶层标准字段，应嵌套在 metadata |

## `allowed-tools` 实验性说明

此字段为实验性，不同 Agent 实现支持情况不同：
- Qwen Code：支持
- Claude Code：支持情况待确认
- 其他 Agent：可能忽略此字段

如追求最大跨平台兼容性，可将其移至 `metadata.allowed-tools` 作为自定义字段。

## 验证清单

创建/修改 SKILL.md 时逐项确认：
- [ ] `name` 仅含小写字母、数字、连字符，且与文件夹名一致
- [ ] `description` 1-1024 字符，非空且具体
- [ ] `compatibility` 如有，不超过 500 字符
- [ ] `version` / `author` 嵌套在 `metadata` 下
- [ ] 无连续 `--`、无首尾 `-`
- [ ] YAML 分隔符 `---` 正确闭合

---
name: news-linguistic-analyzer
description: "Translates English news articles into Chinese with multi-dimensional linguistic analysis. Triggers on: English news text (Reuters, BBC, AP, CNN, Bloomberg), 英文新闻翻译, 新闻分析, translate and analyze news. Performs fact-checking, lexical/syntactic/grammatical analysis, and critical reflection. Do NOT use for non-news text, poetry, fiction, or general translation without analysis."
compatibility: "Requires web_search and web_fetch tools for the mandatory fact-checking step. If your Agent does not support the allowed-tools field, ensure web_search and web_fetch are available. Python 3.8+ for the optional scripts/validate-input.py."
allowed-tools: "web_search web_fetch"
metadata:
  author: anthonysu
  version: "1.8.0"
license: MIT
---

# 🗞️ 新闻英语翻译与深度分析器

当用户提供一段英文新闻文本时，**必须首先执行事实核查**，然后再进行后续 6 步分析。

## 当前日期

!`date +%Y-%m-%d`

> **动态命令注入**：此行在支持的 Agent（如 Claude Code）环境中会展开为当前日期，供事实核查步骤进行日期校验。在不支持此语法的环境中，该行显示为原始文本。

> **日期获取降级策略**：如上述命令注入未生效（即该行仍显示为 `` !`date ...` `` 原始文本），Agent 应通过以下方式获取当前日期：
> 1. 使用系统环境提供的当前日期信息（如 Agent 上下文中注入的日期）
> 2. 执行 `date` 命令获取系统日期
> 3. 若均不可用，在事实核查输出中标注「⚠️ 无法获取当前日期，跳过日期校验」，继续后续步骤

> **📋 多步骤任务提示**：本 skill 包含 **1 个强制前置步骤 + 6 个分析步骤**。如 Agent 支持任务追踪（todo list），建议开始前创建清单，逐步标记完成状态。

## 如何触发

本 skill 通过以下方式自动触发：

- **自然语言匹配**：提供英文新闻文本（尤其是 Reuters、BBC、AP、CNN、Bloomberg 等来源）
- **关键词匹配**：提及「英文新闻翻译」「新闻分析」「用词分析」「句法分析」「translate and analyze news」等
- **显式调用**：通过 skill 名称 `news-linguistic-analyzer` 直接调用

**不会触发**：非新闻类英文文本、诗歌、小说、无语言学分析的普通翻译请求。

## 🚨 事实核查（强制前置步骤）

**收到用户输入后，第一步必须执行以下检测**：

### 第一层：强制触发（满足任一即触发 web search）

| 触发条件 | 说明 |
|---------|------|
| 含具体日期 | 任何具体日期（过去/未来/当前均触发） |
| 人名+重大事件 | 具体人名与重大事件关键词同时出现 |
| 伤亡/损失数据 | 伤亡数字、经济损失、灾害规模等 |
| 正在进行的重大事件 | 当前持续发展的国际/国内重大事件 |
| 与已知事实冲突 | 与模型内置知识明显矛盾 |

**触发后执行**：
1. **调用 web search 工具**，执行双语查询：
   - 首次查询（英文）：`[事件人物英文名 + 日期/关键词]`
   - 交叉验证（中文）：`[人物/事件中文译名 + 日期/关键词 + 真实性]`
2. **输出核查结果**：在正式翻译开头添加以下格式提示：

```text
⚠️ 事实核查：经联网查询验证，[该事件为真实发生 / 该事件尚未发生 / 未找到相关权威报道]
   查询摘要：[1-2 句话概括搜索结果]
```

**低置信度情况**：当搜索结果存在单一信源、多源矛盾、关键细节不一致等问题时，使用低置信度标注：

```text
⚠️ 事实核查（低置信度）：经联网查询，[找到部分相关报道但无法完全验证 / 不同信源报道存在矛盾]
   查询摘要：[1-2 句话说明搜索信息及矛盾点]
   建议：[具体疑点及推荐权威信源]
```

> 完整事实核查输出格式规范见 [references/output-format.md](references/output-format.md)。

### 特殊路径：虚构标记词（不触发 web search，直接标注）

当检测到 `fiction`、`scenario`、`hypothetical`、`AI-generated` 等虚构标记词时，**跳过 web search**，直接标注：

```text
⚠️ 内容属性提示：本段文本包含虚构标记词（如 hypothetical、AI-generated 等），可能为情景推演、创作练习或 AI 生成内容。请结合权威信源交叉验证后再作引用。
```

> **区分**：「⚠️ 事实核查」= 已联网验证；「⚠️ 内容属性提示」= 检测到虚构标记词，无需联网。

### 第二层：模型评估（无明确触发条件时）

如上述强制触发条件均未满足，模型自行评估：
- 该事件是否可能超出模型内置知识的截止日期？
- 该事件是否涉及需要最新信息才能准确翻译的内容？
- 该事件是否存在被误传或捏造的风险？

**评估结果为"需要验证"时**，同样触发 web search 流程。

> **降级策略**：联网验证按以下优先级依次尝试：
> 1. **web search**（首选）：执行双语关键词查询
> 2. **web fetch**（次选）：当 web search 不可用时，访问已知权威新闻源页面（如 Reuters、AP、BBC 对应报道页）获取信息
> 3. **离线标注**（兜底）：当 web search 和 web fetch 均不可用时，在事实核查输出中标注「⚠️ 未能联网验证，以下分析基于模型内置知识」，并继续后续步骤

## 核心流程

事实核查完成后，依次执行以下 **6 步标准化分析流程**：

| 步骤 | 模块 | emoji 标记 | 输出形式 |
|------|------|----------|---------|
| 1 | 中文翻译 | 📝 | 分段译文 + 标题层级保留 + 信息点校验 |
| 2 | 用词分析 | 🔍 | Markdown 表格：`英文原词 | 中文对应 | 语境特点`（5-8 项） |
| 3 | 句子结构拆解 | 🧱 | 1-2 个典型长句的成分标注与中英文逻辑对比 |
| 4 | 语法结构分析 | 📐 | 时态、语态、分词、消息源位置等特征 |
| 5 | 翻译技巧提示 | 💡 | 3-5 项：技巧名 + 原文示例 + 处理原理 |
| 6 | 延伸思考 | 🌍 | 批判性视角 |

### 翻译信息点校验

步骤 1 翻译完成后，**必须自检**以下信息点是否在译文中完整呈现：

- 专有名词：人名、地名、机构名是否全部译出
- 数值数据：具体数字、百分比、金额是否准确对应
- 时间信息：日期、时段、频率是否无遗漏
- 核心动作：主要事件/决策是否已体现
- 条件/限定：范围、条件、因果等限定语是否保留

校验方式：在翻译输出末尾附加一行校验结果，格式为：
```text
✅ 翻译校验通过：原文 N 个关键信息点均已体现
```
或
```text
⚠️ 翻译校验：原文含 N 个关键信息点，以下未在译文中体现：[列举]
```

**注意**：此校验为内部自检步骤，校验结果对用户可见，但不作为独立章节输出。如发现遗漏，须在译文正文中补全后再输出。

## 输出格式

完整输出规范见 [references/output-format.md](references/output-format.md)。

**基础要求**：
- 全程使用**中文回复**
- 技术术语首次出现时保留英文原词，括号附简要解释
- 表格统一 Markdown 格式，关键术语用反引号标注
- 延伸思考部分标注「🌍」符号

## 使用模式

| 触发关键词 | 策略 |
|------|------|
| `仅需翻译` / `translation only` | 仅输出步骤 1 |
| `跳过延伸` / `no reflection` | 省略步骤 6 |
| `简洁模式` / `brief` | 用词分析限 3 项，技巧提示限 2 项 |

> **优先级**：仅需翻译 > 简洁模式 > 跳过延伸 > 默认完整。多个模式指令同时出现时，取最高级执行。

## 领域自适应

检测到特定领域关键词时，自动补充背景注释。

覆盖领域：金融、体育、科技、地缘政治、医疗健康、环境气候、法律司法、教育科研、军事防务、社会民生。

完整触发词示例与补充内容规范见 [references/domain-adaptation.md](references/domain-adaptation.md)。

## 消息源识别

完整消息源列表（19 个）见 [references/news-sources.md](references/news-sources.md)。

当新闻中出现消息源标识时，在语法分析中注明来源，翻译时使用标准中文译法。

## 批量处理与超长文本

> **判断依据**：用户用 `---` 或空行明确分隔多段 → **批量处理**；连续长文且 >2000 词 → **超长文本处理**。

### 批量处理

多段新闻按 `---` 或空行分割，每段独立执行 6 步分析，末尾添加批量小结。

完整规则（分割方式、输出结构、质量检查）见 [references/batch-processing.md](references/batch-processing.md)。

### 超长文本处理

单篇超过 2000 词时，采用主题感知分段策略，保留上下文衔接。

完整规则（分段原则、上下文衔接、输出结构模板）见 [references/long-text-processing.md](references/long-text-processing.md)。

## 输入校验（可选）

当不确定输入是否为新闻文本时，可运行 `scripts/validate-input.py` 辅助判断。根据退出码决定后续操作（`0`=正常执行，`1`=添加待确认提示，`2`=询问用户是否继续）。

完整调用方式、退出码说明和内联判断降级方案见 [references/input-validation.md](references/input-validation.md)。

## 边缘情况与错误处理

完整边缘情况处理表和降级策略见 [references/edge-cases.md](references/edge-cases.md)。

## 质量检查

完成全部分析步骤后，**必须**对照 [references/quality-checklist.md](references/quality-checklist.md) 逐项自检。如 [必检] 项未通过，修正后再输出最终结果。

## 示例

完整输入/输出对照示例见 [references/examples.md](references/examples.md)。

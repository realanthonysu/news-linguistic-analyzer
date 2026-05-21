---
name: news-linguistic-analyzer
description: "This skill translates English news articles into Chinese and performs multi-dimensional linguistic analysis (lexical, syntactic, grammatical, translation techniques, critical reflection). Use when the user provides English news text from sources like Reuters, BBC, AP, CNN, Bloomberg, or asks to translate and analyze news reports, breaking news, or news articles. Also triggers on: 英文新闻翻译, 新闻分析, 用词分析, 句法分析, translate and analyze news. Do NOT use for non-news English text, poetry, fiction, or general translation without linguistic analysis."
metadata:
  author: anthonysu
  version: "1.4.1"
tools_required:
  - web_search
  - web_fetch
license: MIT
compatibility: "Python 3.8+ required for optional scripts/validate-input.py"
---

# 🗞️ 新闻英语翻译与深度分析器

当用户提供一段英文新闻文本时，**必须首先执行事实核查**，然后再进行后续 6 步分析。

## 🚨 事实核查（强制前置步骤）

**收到用户输入后，第一步必须执行以下检测**：

### 第一层：强制触发（满足任一即触发 web search）

| 触发条件 | 说明 |
|---------|------|
| 含具体日期 | 识别到任何具体日期（如 `September 1`、`2026`、`last week` 等），无论过去/未来/当前 |
| 人名+重大事件组合 | 识别到具体人名与重大事件关键词同时出现（如 `President Trump + cancelled a trip`） |
| 伤亡/损失等敏感数据 | 含伤亡数字、经济损失金额、灾害规模等可能引发重大社会影响的数据 |
| 正在进行的重大事件 | 涉及当前正在发生或持续发展的国际/国内重大事件 |
| 与已知事实冲突 | 人物/事件与模型内置知识中的已知事实明显矛盾 |
| 虚构标记词 | 含 `fiction`, `scenario`, `hypothetical`, `AI-generated` 等标记 |

**触发后执行**：
1. **调用 web search 工具**，执行双语查询：
   - 首次查询（英文）：`[事件人物英文名 + 日期/关键词]`
   - 交叉验证（中文）：`[人物/事件中文译名 + 日期/关键词 + 真实性]`
2. **输出核查结果**：在正式翻译开头添加以下格式提示：

```text
⚠️ 事实核查：经联网查询验证，[该事件为真实发生 / 该事件尚未发生 / 未找到相关权威报道]
   查询摘要：[1-2 句话概括搜索结果]
```

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

| 用户指令关键词 | 策略 |
|------|------|
| 仅需翻译 / translation only | 仅输出步骤 1 |
| 跳过延伸 / no reflection | 省略步骤 6 |
| 简洁模式 / brief | 用词分析限 3 项，技巧提示限 2 项 |

> **模式冲突优先级**：仅需翻译 > 简洁模式 > 跳过延伸 > 默认完整模式。当用户同时发出多个模式指令时，按此优先级取最高级执行。

## 领域自适应

检测到特定领域关键词时，自动补充背景注释。

覆盖领域：金融、体育、科技、地缘政治、医疗健康、环境气候、法律司法、教育科研、军事防务、社会民生。

完整触发词示例与补充内容规范见 [references/domain-adaptation.md](references/domain-adaptation.md)。

## 消息源识别

完整消息源列表（19 个）见 [references/news-sources.md](references/news-sources.md)。

当新闻中出现消息源标识时，在语法分析中注明来源，翻译时使用标准中文译法。

## 批量处理

当用户一次性提供多段新闻时：
1. 按 `---` 或空行分割
2. 为每段添加序号标题：`## 【新闻 N】原标题`
3. 依次执行 6 步分析，段间用 `---` 分隔
4. 末尾添加「📊 批量分析小结」

## 超长文本处理

当单篇新闻超过 2000 词时，采用**主题感知分段策略**。

完整规则（分段原则、上下文衔接、输出结构模板、与批量处理对比）见 [references/long-text-processing.md](references/long-text-processing.md)。

## 输入校验（可选）

当不确定输入是否为新闻文本时，可运行预校验脚本辅助判断：

1. 将用户输入写入临时文件：`python -c "import tempfile,sys; f=tempfile.NamedTemporaryFile(mode='w',suffix='.txt',delete=False,encoding='utf-8'); f.write(sys.argv[1]); print(f.name); f.close()" "用户输入内容"`
2. 执行校验：`python scripts/validate-input.py <临时文件路径>`
3. 根据退出码决定后续操作：
   - 返回码 `0`：正常执行分析
   - 返回码 `1`：在输出开头添加「❓ 内容属性待确认」提示
   - 返回码 `2`：回复「该内容疑似非新闻文本，是否仍要执行语言分析？[是/否]」

> 如无法执行脚本，可按以下规则内联判断：检测消息源标识、新闻高频动词（reports/announced/stated）、时效性词汇；如含虚构标记词（fiction/scenario/hypothetical）则触发事实核查。

## 边缘情况与错误处理

完整边缘情况处理表和降级策略见 [references/edge-cases.md](references/edge-cases.md)。

## 质量检查

生成输出前，对照 [references/quality-checklist.md](references/quality-checklist.md) 自检。

## 示例

完整输入/输出对照示例见 [references/examples.md](references/examples.md)。

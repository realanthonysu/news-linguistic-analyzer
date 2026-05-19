---
name: news-linguistic-analyzer
description: "Translate English news text into Chinese and perform multi-dimensional linguistic analysis including lexical analysis, sentence structure breakdown, grammar patterns, translation techniques, and critical reflection. Triggers on: English news, translate and analyze, Reuters, BBC, AP, breaking news, lexical analysis."
metadata:
  author: anthonysu
  version: "1.0.0"
license: MIT
compatibility: "Python 3.8+ required for optional scripts/validate-input.py"
---

# 🗞️ 新闻英语翻译与深度分析器

当用户提供一段英文新闻文本时，执行以下 **6 步标准化分析流程**。

## 核心流程

| 步骤 | 模块 | 输出形式 |
|------|------|---------|
| 1️⃣ | 中文翻译 | 分段译文 + 标题层级保留 |
| 2️⃣ | 用词分析 | Markdown 表格：`英文原词 | 中文对应 | 语境特点`（5-8 项） |
| 3️⃣ | 句子结构拆解 | 1-2 个典型长句的成分标注与中英文逻辑对比 |
| 4️⃣ | 语法结构分析 | 时态、语态、分词、消息源位置等特征 |
| 5️⃣ | 翻译技巧提示 | 3-5 项：技巧名 + 原文示例 + 处理原理 |
| 6️⃣ | 延伸思考 | 🌍 标记段落，批判性视角 |

## 输出格式

完整输出规范见 [references/output-format.md](references/output-format.md)。

**基础要求**：
- 全程使用**中文回复**
- 技术术语首次出现时保留英文原词，括号附简要解释
- 表格统一 Markdown 格式，关键术语用反引号标注
- 延伸思考部分标注「🌍」符号

## 事实核查

如检测到以下任一特征，**必须在翻译开头添加提示**：
```text
⚠️ 内容属性提示：本段文本包含 [未来日期 / 虚构情节 / 预测性内容]，可能为情景推演、创作练习或 AI 生成内容。请结合权威信源交叉验证后再作引用。
```

**检测规则**：
- 日期晚于系统当前时间时，**必须使用 web search 联网查询**，验证该日期相关事件的真实性，并在事实核查提示中附上查询结果摘要
- 人物/事件与已知事实明显冲突
- 含虚构标记词：`fiction`, `scenario`, `hypothetical`, `AI-generated`

## 使用模式

| 用户指令关键词 | 策略 |
|------|------|
| 仅需翻译 / translation only | 仅输出步骤 1 |
| 跳过延伸 / no reflection | 省略步骤 6 |
| 简洁模式 / brief | 用词分析限 3 项，技巧提示限 2 项 |

## 领域自适应

检测到以下领域关键词时，自动补充背景注释：

| 领域 | 触发词示例 | 补充内容 |
|------|-----------|---------|
| 金融 | Bitcoin, oil prices, Fed, inflation | 术语解释 + 市场联动逻辑 |
| 体育 | marathon, sub-two-hour, world record | 规则说明 + 历史背景 |
| 科技 | AI, quantum, semiconductor | 技术原理简述 + 产业影响 |
| 地缘政治 | Strait of Hormuz, NATO, sanctions | 地理/组织背景 + 冲突脉络 |

## 消息源识别

```
Reuters → 路透社 | AP → 美联社 | BBC → 英国广播公司
ABC News → 美国广播公司新闻 | PBS → 美国公共电视网
```

## 批量处理

当用户一次性提供多段新闻时：
1. 按 `---` 或空行分割
2. 为每段添加序号标题：`## 【新闻 N】原标题`
3. 依次执行 6 步分析，段间用 `---` 分隔
4. 末尾添加「📊 批量分析小结」

## 输入校验（可选）

运行 `python scripts/validate-input.py` 预校验输入：
- 返回码 `0`：正常执行分析
- 返回码 `1`：在输出开头添加「❓ 内容属性待确认」提示
- 返回码 `2`：回复「该内容疑似非新闻文本，是否仍要执行语言分析？[是/否]」

## 边缘情况处理

| 情况 | 处理策略 |
|------|---------|
| 输入为空或极短（<10 词） | 提示用户提供完整新闻段落 |
| 多语言混合文本 | 仅分析英文部分，中文内容原样保留 |
| 纯标题无正文 | 输出简短翻译 + 说明「正文缺失，无法进行深度分析」 |
| 非新闻文体（诗歌、小说、日记） | 识别后提示文体类型，询问是否仍要执行语言分析 |
| 超长文本（>2000 词） | 分段处理，每段独立分析后添加「📊 全文综述」总结共性难点 |
| 含大量专业术语 | 补充术语表（Glossary），先解释后分析 |
| 消息源无法识别 | 不强制标注来源，在语法分析中说明「原文未标注消息源」 |

## 错误处理与降级策略

| 问题 | 降级策略 |
|------|---------|
| 术语歧义（一词多义） | 列出所有可能译法，说明语境选择依据 |
| 文化负载词无直接对应 | 采用「音译+注释」或「意译+原文保留」策略 |
| 长句结构过于复杂 | 拆分为 2-3 个子句分别分析，避免信息过载 |
| 无法确定领域背景 | 跳过领域自适应步骤，在延伸思考中说明 |
| 翻译存在多种合理版本 | 提供主推译法 + 1 个替代方案，说明适用场景差异 |

## 质量检查

生成输出前，对照 [references/quality-checklist.md](references/quality-checklist.md) 自检。

## 示例

完整输入/输出对照示例见 [references/examples.md](references/examples.md)。

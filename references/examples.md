# 📝 新闻英语分析 — 输入/输出示例

本文件提供完整的输入输出对照示例，供模型执行时参考。

---

## 示例 1：标准地缘政治新闻

### 输入

```text
Iran Standoff and Peace Talks: Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports. Meanwhile, oil prices have risen following Iran's threats to close the Strait of Hormuz.
```

### 期望输出

```markdown
### 📝 中文翻译
**伊朗对峙与和谈**：据路透社报道，在紧张局势升级、谈判陷入僵局之际，特朗普总统取消了美国特使前往巴基斯坦的原定行程，并表示"我们掌握着所有筹码"。与此同时，受伊朗威胁关闭霍尔木兹海峡的影响，油价出现上涨。
✅ 翻译校验通过：原文 6 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `escalating tensions` | 紧张局势升级 | `escalate` 原指自动扶梯上升，引申为事态恶化。新闻高频搭配，暗示动态加剧过程。 |
| `stalled negotiations` | 谈判陷入僵局 | `stall` 指引擎熄火或进程停滞。形容词化后修饰抽象名词，简洁表达"无进展"状态。 |
| `we have all the cards` | 我们掌握所有筹码 | 扑克隐喻。直译生硬，需转化为中文政经语境习惯用语，保留"掌控局势"的核心语义。 |
| `Strait of Hormuz` | 霍尔木兹海峡 | 专有名词，采用约定俗成译法。地缘政治高频地名，需准确对应。 |
| `cancelled a planned trip` | 取消了原定行程 | `planned` 作为前置定语修饰 `trip`，中文需补充"原定"以保留计划性含义。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports.
- 主干：President Trump cancelled a planned trip
    - 介词短语（背景）：Amid escalating tensions and stalled negotiations
    - 介词短语（目的）：for US envoys to Pakistan
    - 现在分词（伴随状语）：stating "we have all the cards"
    - 消息源附注：Reuters reports
- 中文切分逻辑：英文将背景状语前置、消息源后置；中文需将消息源前置（"据路透社报道"），背景状语可保留前置或转为"在……之际"中置。

### 📐 语法结构分析（Grammatical Analysis）
1. **现在分词作伴随状语**：`stating "we have all the cards"` 补充说明取消行程时的表态，新闻英语常用此结构压缩信息密度。翻译时拆为并列句更符合中文习惯。
2. **消息源位置**：`Reuters reports` 置于句末，是英文新闻的典型消息源归因方式。中文翻译时需前置为"据路透社报道"。
3. **并列名词短语**：`escalating tensions and stalled negotiations` 由两个分词修饰的抽象名词并列构成，中文需分别处理为动宾/主谓结构以保持流畅。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 消息源前置 | `Reuters reports` | 译为"据路透社报道"置于句首 | 中文新闻语体习惯将消息源前置，与英文后置归因形成语序差异 |
| 隐喻本土化 | `we have all the cards` | 译为"掌握所有筹码" | 扑克隐喻在中文政经语境中已有"筹码"对应，无需直译为"持有所有牌" |
| 分词转并列 | `stating "..."` | 译为"并表示'……'" | 英文现在分词表伴随，中文需转为并列谓语以避免欧化句式 |

### 🌍 延伸思考
🌍 本段报道的措辞选择值得关注。`escalating tensions` 与 `stalled negotiations` 构成对比张力——局势在升级而谈判在停滞，暗示外交空间的收窄。`we have all the cards` 作为直接引语保留，既传达了立场，也反映了特定修辞策略。翻译时需注意：直接引语在跨语言传播中可能失去原有的口语化冲击力，"筹码"比"牌"更符合中文政论语体，但也淡化了原话的口语色彩。这是新闻翻译中"准确还原"与"语体适配"之间的典型张力。
```

---

## 示例 2：财经/科技新闻

### 输入

```text
The IPO Strategy: SpaceX is reportedly preparing for a $1.75 trillion IPO. Adding a dominant software platform like Cursor allows Musk to pitch SpaceX not just as a rocket company, but as a diversified AI and Knowledge Work powerhouse to Wall Street.
```

### 期望输出要点

- 事实核查提示：`$1.75 trillion` 远超 SpaceX 已知估值，Cursor 与 SpaceX 无已知关联 → 添加 ⚠️ 警告
- 用词分析重点：`reportedly`（模糊消息源）、`pitch...to Wall Street`（商业隐喻）、`powerhouse`（能源隐喻）
- 句型拆解：动名词短语作主语（`Adding... allows...`）+ `not just as... but as...` 并列结构

---

## 示例 3：触发精简模式

### 用户指令

```text
仅需翻译：BBC reports that the UK Prime Minister has announced new economic measures aimed at reducing inflation, which has reached a 40-year high.
```

### 期望输出（仅步骤 1）

```markdown
### 📝 中文翻译
据英国广播公司报道，英国首相已宣布新的经济措施，旨在降低已触及 40 年高位的通胀率。
```

---

## 示例 4：事实核查触发

### 输入

```text
In 2030, Mars Colony One will celebrate its 5th anniversary. President Elon Musk stated that the population has exceeded 10,000 settlers, according to a hypothetical scenario released by SpaceX.
```

### 期望输出开头

```text
⚠️ 内容属性提示：本段文本包含未来日期（2030）、虚构情节（Mars Colony One）及虚构标记词（hypothetical scenario），可能为情景推演、创作练习或 AI 生成内容。请结合权威信源交叉验证后再作引用。

### 📝 中文翻译
...
```

---

## 示例 5：批量处理

### 用户输入

```text
Breaking News: A major earthquake struck Turkey.

---

Markets React: Oil prices surged following the announcement.
```

### 期望输出结构

```markdown
## 【新闻 1】Breaking News: A major earthquake struck Turkey.
### 📝 中文翻译
...

### 🔍 用词分析
...
（完整 6 步）

---

## 【新闻 2】Markets React: Oil prices surged following the announcement.
### 📝 中文翻译
...
### 🔍 用词分析
...
（完整 6 步）

---

## 📊 批量分析小结
- 总词数：XX
- 高频术语：...
- 共性翻译难点：...
```

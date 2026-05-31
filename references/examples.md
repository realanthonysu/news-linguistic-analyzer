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

### 期望输出

```markdown
⚠️ 事实核查：经联网查询验证，该内容存在多处疑点。
   查询摘要：SpaceX 当前估值约 3500 亿美元（2024 年数据），$1.75 trillion 远超合理范围；Cursor 为 AI 代码编辑器，与 SpaceX 无已知业务关联。该文本可能为假设性推演或 AI 生成内容。

### 📝 中文翻译
**IPO 策略**：据报道，SpaceX 正在筹备一项价值 1.75 万亿美元的 IPO。将 Cursor 这一主导性软件平台纳入旗下，使马斯克得以向华尔街推销 SpaceX——它不再仅仅是一家火箭公司，而是一个多元化的 AI 与知识工作巨头。
✅ 翻译校验通过：原文 5 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `reportedly` | 据报道 | 模糊消息源归因词，暗示信息未经官方确认。新闻英语中用以规避法律风险，翻译时保留同等模糊度。 |
| `pitch...to Wall Street` | 向华尔街推销 | `pitch` 本为投球/推销术语，商业语境中指向投资人展示项目价值。`Wall Street` 借代金融界，中文保留借代。 |
| `powerhouse` | 巨头 | 原义"发电站"，引申为"强大的实体"。能源隐喻在商业报道中高频出现，中文对应"巨头/强企"。 |
| `dominant` | 主导性的 | 市场份额语境下的高频形容词，暗示行业领导地位。中文"主导性"比"占统治地位的"更简洁。 |
| `diversified` | 多元化的 | 金融/商业术语，指业务线多元化以分散风险。中文已形成固定对应译法。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：Adding a dominant software platform like Cursor allows Musk to pitch SpaceX not just as a rocket company, but as a diversified AI and Knowledge Work powerhouse to Wall Street.
- 主干：Adding... allows Musk to pitch SpaceX
    - 动名词短语（主语）：Adding a dominant software platform like Cursor
    - 宾补结构：to pitch SpaceX not just as... but as...
        - 并列对比：not just as a rocket company / but as a diversified AI and Knowledge Work powerhouse
        - 介词短语（对象）：to Wall Street
- 中文切分逻辑：英文以动名词短语作主语，信息密度高；中文需拆为因果句式（"将...纳入旗下，使...得以..."），避免欧化长主语。

### 📐 语法结构分析（Grammatical Analysis）
1. **动名词短语作主语**：`Adding a dominant software platform like Cursor` 充当整句主语，是新闻英语压缩信息密度的典型手段。中文不常用动名词作主语，需转换为动宾短语或因果结构。
2. **`not just as... but as...` 并列结构**：对比两种定位，形成递进修辞。翻译时保留对比节奏（"不再仅仅是...而是..."）。
3. **不定式作宾补**：`to pitch SpaceX as...` 中 `as` 引导的介词短语充当补语，说明"推销成什么形象"。中文需补充动词（"得以推销为"）以保持流畅。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 动名词转因果 | `Adding... allows Musk to...` | 译为"将...纳入旗下，使...得以..." | 英文动名词作主语在中文中不自然，转为因果句式更符合中文逻辑链表达习惯 |
| 模糊消息源保留 | `reportedly` | 译为"据报道" | 中文新闻同样使用"据报道/据悉"等模糊归因词，保留同等法律规避功能 |
| 隐喻直译+意译结合 | `powerhouse` | 译为"巨头"而非"发电站" | 能源隐喻在中文商业语境中已有对应意译，直译反而费解 |

### 🌍 延伸思考
🌍 值得注意的是，`reportedly` 一词在原文中承担了重要的信息过滤功能——它暗示这些数据并非来自官方公告，而是基于传闻或推测。结合事实核查发现的疑点（$1.75 trillion 估值异常、Cursor 与 SpaceX 无已知关联），这段文本更接近投资推演或 AI 生成的假设性分析，而非真实新闻报道。翻译时保留 `reportedly` 的模糊性至关重要——若译为"据悉"可能暗示更高的可信度，"据报道"则更中性。此外，`pitch...to Wall Street` 的措辞本身带有推销色彩，暗示叙述者站在公司立场而非中立报道立场，这也是翻译和分析时需要注意的视角问题。
```

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
⚠️ 内容属性提示：本段文本包含虚构标记词（hypothetical scenario），可能为情景推演、创作练习或 AI 生成内容。请结合权威信源交叉验证后再作引用。

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

---

## 示例 6：事实核查触发（已联网验证）

### 输入

```text
Trade War Escalation: On May 15, 2026, President Trump announced new tariffs of 25% on Chinese imports, citing national security concerns under Section 301. The move drew swift condemnation from Beijing, with the Chinese Ministry of Commerce calling it "economic coercion."
```

### 期望输出开头

```text
⚠️ 事实核查：经联网查询验证，该事件为真实发生。
   查询摘要：2026年5月15日，特朗普政府确实在当日宣布了对中国进口商品加征25%关税的措施，援引301条款。中国商务部回应"经济胁迫"的报道已被路透社、美联社等多家权威媒体证实。

### 📝 中文翻译
**贸易战升级**：2026年5月15日，特朗普总统宣布对中国进口商品加征25%关税，援引《301条款》下的国家安全关切。此举迅速遭到北京强烈谴责，中国商务部称之为"经济胁迫"。
✅ 翻译校验通过：原文 6 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `escalation` | 升级 | 冲突/对抗语境高频词，指事态恶化。新闻标题中常用名词化形式压缩信息。 |
| `tariffs` | 关税 | 贸易政策核心术语，`25% tariffs on Chinese imports` 为固定搭配结构。 |
| `national security concerns` | 国家安全关切 | 外交/贸易政策中的委婉表达，实际指"以国家安全为由"。中文"关切"比"担忧"更中性。 |
| `swift condemnation` | 迅速谴责 | `swift` 强调反应速度，新闻中常见搭配。中文四字格"迅速谴责"节奏紧凑。 |
| `economic coercion` | 经济胁迫 | 国际关系高频术语，指通过经济手段施压。中文已有固定译法。 |

（后续完整 6 步分析略）
```

---

## 示例 7：垂直领域 — 医疗健康新闻

### 输入

```text
FDA Approves New Alzheimer's Drug: The FDA has granted accelerated approval to lecanemab, a monoclonal antibody targeting amyloid beta plaques. Clinical trials showed a 27% reduction in cognitive decline over 18 months, though the drug carries risks of brain swelling and microhemorrhages.
```

### 期望输出

```markdown
### 📝 中文翻译
**FDA 批准新型阿尔茨海默病药物**：美国食品药品监督管理局已加速批准 lecanemab（仑卡奈单抗），这是一种靶向 β-淀粉样蛋白斑块的单克隆抗体。临床试验显示，该药物在 18 个月内使认知衰退减少了 27%，但存在脑肿胀和微出血风险。
✅ 翻译校验通过：原文 7 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `accelerated approval` | 加速批准 | FDA 专有审批通道，用于严重疾病且现有疗法有限的情况。🏛️ [背景说明] 加速批准基于替代终点（如生物标志物），需后续确证性试验验证临床获益。 |
| `lecanemab` | 仑卡奈单抗 | 单克隆抗体药物名。🏛️ [背景说明] 由卫材和渤健联合开发，2023年首次获FDA批准，是阿尔茨海默病领域突破性疗法。 |
| `monoclonal antibody` | 单克隆抗体 | 生物制药术语，指由单一B细胞克隆产生的均一抗体。 |
| `amyloid beta plaques` | β-淀粉样蛋白斑块 | 阿尔茨海默病病理标志物。🏛️ [背景说明] Aβ沉积是AD"淀粉样蛋白级联假说"的核心，靶向清除Aβ是该领域主要研发方向。 |
| `cognitive decline` | 认知衰退 | 神经退行性疾病语境高频术语，比"dementia"更中性，涵盖轻度到重度范围。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：Clinical trials showed a 27% reduction in cognitive decline over 18 months, though the drug carries risks of brain swelling and microhemorrhages.
- 主干：Clinical trials showed a 27% reduction
    - 介词短语（范围）：in cognitive decline
    - 时间状语：over 18 months
    - 让步状语从句：though the drug carries risks of brain swelling and microhemorrhages
- 中文切分逻辑：英文将让步从句后置；中文需前置或用"但"转折处理为并列句。

### 📐 语法结构分析（Grammatical Analysis）
1. **现在完成时 + 被动语态**：`has granted accelerated approval` 表示已完成的动作及其对当前的影响，是医药新闻中报告监管决策的标准时态。
2. **though 引导让步状语从句**：平衡疗效与风险的信息，体现新闻报道的客观性原则。中文用"但"转折处理。
3. **动名词复合结构**：`brain swelling and microhemorrhages` 并列说明不良反应类型，医学术语需准确对应中文专业译法。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 机构名+简称展开 | `FDA` | 译为"美国食品药品监督管理局" | 中文新闻首次出现机构名需全称，后文可用简称 |
| 药名保留原文+附译名 | `lecanemab` | 译为"lecanemab（仑卡奈单抗）" | 药物通用名翻译需兼顾国际通用名和中文标准译名 |
| 数据精确还原 | `27% reduction` | 译为"减少了 27%" | 医疗新闻中数据准确性优先，不可模糊处理 |

### 🌍 延伸思考
🌍 本段报道中的 `accelerated approval` 是一个值得关注的监管术语。它不同于常规批准，而是基于替代终点（如影像学指标）的快速通道审批，意味着药物上市时其临床获益尚未得到充分确证。翻译时保留"加速"二字的精准性至关重要——若译为"快速批准"可能暗示速度而非监管路径差异。此外，`carries risks of brain swelling and microhemorrhages` 的措辞体现了医药新闻的伦理要求：在报告疗效的同时必须同等强调风险，这是医药报道与一般新闻的重要区别。
```

---

## 示例 8：「跳过延伸」模式

### 用户指令

```text
跳过延伸：The United Nations has called for an immediate ceasefire in Gaza, as humanitarian conditions continue to deteriorate. Secretary-General António Guterres described the situation as "untenable," urging all parties to prioritize civilian protection.
```

### 期望输出（省略步骤 6，含步骤 1-5）

```markdown
### 📝 中文翻译
联合国呼吁在加沙立即停火，因人道主义局势持续恶化。秘书长安东尼奥·古特雷斯将局势形容为"不可持续"，敦促各方优先保护平民。
✅ 翻译校验通过：原文 5 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `ceasefire` | 停火 | 冲突/外交语境核心术语，与 `truce`（休战）相比，`ceasefire` 更强调正式停止军事行动。 |
| `deteriorate` | 恶化 | 描述局势/条件下降的正式用词，新闻中高频搭配为 `continue to deteriorate`（持续恶化）。 |
| `untenable` | 不可持续的 | 原义为"无法防守的"（军事术语），引申为"无法维持的"。外交辞令中表达"局面已无法容忍"。 |
| `civilian protection` | 保护平民 | 国际法/人道主义高频术语。中文语序调整为动宾结构"保护平民"而非"平民保护"。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：Secretary-General António Guterres described the situation as "untenable," urging all parties to prioritize civilian protection.
- 主干：Secretary-General António Guterres described the situation
    - 介词补语：as "untenable"
    - 现在分词（伴随动作）：urging all parties to prioritize civilian protection
- 中文切分逻辑：英文用分词表伴随；中文拆为独立分句"并敦促……"，符合中文叙事节奏。

### 📐 语法结构分析（Grammatical Analysis）
1. **describe...as 结构**：引用 + 评价的经典新闻句式，将直接引语嵌入陈述中。中文用"形容为/称"对应。
2. **现在分词作伴随状语**：`urging all parties...` 补充说明表态的同时发出的呼吁。新闻英语中用于压缩信息密度。
3. **消息源位置**：联合国秘书长身份在句首标注，是新闻归因的标准方式。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 外交辞令降级 | `described as "untenable"` | 译为"形容为'不可持续'" | 外交语境中 `untenable` 是强烈但克制的措辞，中文"不可持续"保留同等语义强度 |
| 分词转并列句 | `urging all parties to...` | 译为"并敦促各方……" | 英文分词表伴随，中文需转为并列谓语避免欧化句式 |
```

> 注：因用户指令为「跳过延伸」，步骤 6（🌍 延伸思考）已省略。

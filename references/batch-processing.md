# 批量处理（Batch Processing）

SKILL.md 中「批量处理」章节的完整规则，供 Agent 按需加载。

## 触发条件

当用户一次性提供多段新闻时，按以下规则处理。

> **判断依据**：用户用 `---` 或空行明确分隔多段 → **批量处理**。

## 处理流程

1. 按 `---` 或空行分割输入
2. 为每段添加序号标题：`## 【新闻 N】原标题`
3. 依次执行 6 步分析，段间用 `---` 分隔
4. 末尾添加「📊 批量分析小结」

## 输出结构

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

## 完整示例

以下为两条短新闻的批量处理完整输出示例。

### 输入

```text
NATO Summit in Vilnius: NATO leaders convened in the Lithuanian capital for a two-day summit, where discussions centered on Ukraine's membership aspirations and the alliance's eastern flank defense posture. Secretary-General Jens Stoltenberg reaffirmed that "Ukraine's future is in NATO," though no specific timeline was announced.

---

Goldman Sachs Reports Record Q2 Earnings: Goldman Sachs posted second-quarter profits of $3.1 billion, driven by a surge in trading revenue. CEO David Solomon attributed the performance to "resilient client activity" amid volatile markets, while analysts cautioned that rising interest rates could dampen investment banking activity in the second half.
```

### 期望输出

```markdown
## 【新闻 1】NATO Summit in Vilnius: NATO leaders convened in the Lithuanian capital for a two-day summit, where discussions centered on Ukraine's membership aspirations and the alliance's eastern flank defense posture. Secretary-General Jens Stoltenberg reaffirmed that "Ukraine's future is in NATO," though no specific timeline was announced.

### 📝 中文翻译
**北约维尔纽斯峰会**：北约领导人在立陶宛首都举行为期两天的峰会，讨论议题聚焦于乌克兰的入约愿望以及联盟东翼防务态势。秘书长延斯·斯托尔滕贝格重申"乌克兰的未来在北约"，但未宣布具体时间表。
✅ 翻译校验通过：原文 5 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `convened` | 召集/举行 | 正式外交用语，比 `gathered` 更具官方色彩，暗示会议由组织发起而非自发。 |
| `membership aspirations` | 入约愿望 | `aspiration` 比 `desire` 更正式，外交语境中表示长期目标而非短期诉求。 |
| `eastern flank defense posture` | 东翼防务态势 | 军事术语，`flank` 指侧翼，`posture` 指军事部署姿态。🏛️ [背景说明] 北约东翼指波罗的海三国、波兰等与俄罗斯接壤的成员国，是联盟防务重心。 |
| `reaffirmed` | 重申 | 外交声明高频词，`re-` 前缀表示再次，暗示此前已有相同表态。 |
| `specific timeline` | 具体时间表 | 外交承诺语境中的关键限定词，`specific` 的加入暗示此前表态缺乏明确时间节点。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：Secretary-General Jens Stoltenberg reaffirmed that "Ukraine's future is in NATO," though no specific timeline was announced.
- 主干：Secretary-General Jens Stoltenberg reaffirmed that "Ukraine's future is in NATO"
    - 让步状语从句：though no specific timeline was announced
- 中文切分逻辑：英文将直接引语嵌入宾语从句，让步从句后置；中文保留引语，用"但"转折处理让步逻辑。

### 📐 语法结构分析（Grammatical Analysis）
1. **reaffirmed that 引导宾语从句**：外交新闻中用于引用官方立场，`that` 后为直接引语，强调表态的正式性。
2. **though 引导让步状语从句**：在肯定表态后补充限制条件，体现新闻报道的平衡性。被动语态 `was announced` 避免指明责任方。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 地名保留+身份补充 | `Vilnius` | 译为"维尔纽斯"并补充"立陶宛首都" | 非知名地名需附注地理身份，帮助中文读者定位 |
| 直接引语保留 | `"Ukraine's future is in NATO"` | 译为"乌克兰的未来在北约"并保留引号 | 外交表态引语需精确还原，引号标示为被引述内容 |

### 🌍 延伸思考
🌍 `reaffirmed` 一词的使用频率本身就是一个分析线索——它暗示北约在乌克兰入约问题上的立场并非新表态，而是对既有承诺的重申。`though no specific timeline was announced` 的让步结构则揭示了联盟内部的分歧：承诺存在，但执行路径模糊。翻译时需注意："重申"比"再次确认"更中性，后者可能暗示此前有过动摇。

---

## 【新闻 2】Goldman Sachs Reports Record Q2 Earnings: Goldman Sachs posted second-quarter profits of $3.1 billion, driven by a surge in trading revenue. CEO David Solomon attributed the performance to "resilient client activity" amid volatile markets, while analysts cautioned that rising interest rates could dampen investment banking activity in the second half.

### 📝 中文翻译
**高盛公布创纪录的第二季度收益**：高盛第二季度利润达 31 亿美元，受交易收入激增推动。首席执行官大卫·所罗门将此表现归因于"在市场波动中客户活动的韧性"，但分析师警告称，利率上升可能抑制下半年的投资银行业务。
✅ 翻译校验通过：原文 5 个关键信息点均已体现

### 🔍 用词分析（Lexical Analysis）
| 英文原词/短语 | 中文对应 | 语境与搭配特点 |
|--------------|---------|----------------|
| `posted...profits` | 公布利润 | 财报语境高频搭配，`post` 在金融语境中指公布/记录，非"发布"通用义。 |
| `trading revenue` | 交易收入 | 金融机构收入分类术语，指通过证券交易、做市等活动获得的收入。 |
| `resilient client activity` | 客户活动的韧性 | `resilient` 原为材料科学术语（弹性），引申为抗压能力。CEO 引语中用以正面描述业绩。 |
| `volatile markets` | 波动的市场 | 金融语境高频搭配，`volatile` 指价格剧烈波动，与 `stable`（稳定）相对。 |
| `dampen` | 抑制 | 比 `reduce` 更委婉，暗示"削弱活力"而非"减少数量"。财经报道中常用以描述负面影响。 |

### 🧱 句子结构拆解（Sentence Structure Breakdown）
#### 原句：CEO David Solomon attributed the performance to "resilient client activity" amid volatile markets, while analysts cautioned that rising interest rates could dampen investment banking activity in the second half.
- 主干：CEO attributed the performance to "resilient client activity"
    - 介词短语（背景）：amid volatile markets
    - while 并列对比：analysts cautioned that...
        - 宾语从句：rising interest rates could dampen investment banking activity
        - 时间状语：in the second half
- 中文切分逻辑：英文用 `while` 并列 CEO 正面表态与分析师警示，形成对比；中文用"但"衔接，拆为两个独立分句。

### 📐 语法结构分析（Grammatical Analysis）
1. **attributed...to 结构**：归因句式，CEO 用以正面解释业绩。翻译时保留"归因于"的因果框架。
2. **while 并列对比**：将乐观表态与谨慎预测并列，是财经新闻中常见的平衡叙事手法。
3. **could dampen 虚拟语气**：分析师使用 `could` 表达可能性，非确定性预测。翻译用"可能抑制"保留同等语气。

### 💡 翻译技巧提示（Translation Techniques）
| 技巧 | 原文示例 | 处理方式 | 原理 |
|------|---------|---------|------|
| 引语语气保留 | `resilient client activity` | 译为"客户活动的韧性"保留引号 | CEO 引语中刻意使用积极措辞，翻译需保留其修辞策略 |
| 时间范围转换 | `in the second half` | 译为"下半年" | 财经报道中 `second half` 指财年下半年，中文"下半年"为固定对应 |

### 🌍 延伸思考
🌍 CEO 引语中 `resilient` 的选择值得关注——在市场波动（`volatile`）的语境下，用"韧性"而非"强劲"来描述客户活动，暗示业绩虽好但并非毫无风险。分析师的 `cautioned` 则进一步平衡了叙事。翻译时需注意：中文"韧性"已逐渐成为商业报道的流行词，但其原文 `resilient` 的物理科学隐喻（材料受力后恢复原状）在中文中已弱化，读者可能仅理解为"抗压"而忽略"反弹"的含义。

---

## 📊 批量分析小结

- **总词数**：约 120 词（新闻 1 约 55 词，新闻 2 约 65 词）
- **高频术语**：无跨篇重复高频术语
- **共性翻译难点**：
  - 两篇均涉及直接引语处理：新闻 1 为外交表态引语（`"Ukraine's future is in NATO"`），新闻 2 为 CEO 业绩解释引语（`"resilient client activity"`），均需保留引号并精确还原语义
  - 被动语态处理：新闻 1 的 `was announced` 和新闻 2 的 `could dampen` 均涉及英文被动/虚拟语气向中文主动句式的转换
- **领域覆盖**：新闻 1 命中地缘政治（NATO, summit, defense posture），新闻 2 命中金融（Goldman Sachs, trading revenue, interest rates, investment banking）
```

## 质量检查

- [ ] 多段新闻已正确分割并编号
- [ ] 每段分析结构完整，无交叉混淆
- [ ] 末尾含「📊 批量分析小结」

## 与超长文本处理的区别

| 维度 | 批量处理 | 超长文本处理 |
|------|---------|------------|
| 输入性质 | 多篇独立新闻 | 一篇长文 |
| 分段依据 | `---` 或空行（用户已分隔） | 主题感知自动切分 |
| 段间关系 | 各篇独立，无衔接 | 上下文衔接 + 全文综述 |
| 术语处理 | 各篇独立分析 | 全文综述中汇总跨段术语一致性 |

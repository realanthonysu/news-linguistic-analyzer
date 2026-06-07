# 领域自适应（Domain Adaptation）

SKILL.md 中「领域自适应」章节的完整规则，供 Agent 按需加载。

## 领域触发词与补充内容

| 领域 | 触发词示例 | 补充内容 |
|------|-----------|---------|
| 金融 | Bitcoin, oil prices, Fed, inflation, GDP, interest rate, stock market, Wall Street, IPO, bond, forex, recession, unemployment, central bank, treasury, hedge fund | 术语解释 + 市场联动逻辑 |
| 体育 | marathon, sub-two-hour, world record, FIFA, World Cup, Premier League, Champions League, transfer, NBA, playoffs, championship, Olympic, medal, doping, tournament, league, referee, stadium, athlete, sprint, relay, podium | 规则说明 + 历史背景 |
| 科技 | AI, quantum, semiconductor | 技术原理简述 + 产业影响 |
| 地缘政治 | Strait of Hormuz, NATO, sanctions | 地理/组织背景 + 冲突脉络 |
| 医疗健康 | vaccine, clinical trial, WHO, pandemic, FDA, epidemic, outbreak, drug approval | 医学术语释义 + 监管机构职能说明 + 公共卫生背景 |
| 环境气候 | carbon emissions, Paris Agreement, COP, glacier, deforestation, renewable energy, sea level | 气候机制简述 + 国际协定背景 + 生态影响链 |
| 法律司法 | Supreme Court, ruling, indictment, lawsuit, conviction, appeal, constitutional, verdict | 法律体系差异说明 + 诉讼流程概要 + 关键法律概念对照 |
| 教育科研 | university ranking, tuition, research paper, peer review, STEM, scholarship, academic | 教育制度对比 + 学术术语解释 + 政策背景 |
| 军事防务 | Pentagon, missile, NATO forces, ceasefire, drone strike, troops, military exercise | 武器系统简述 + 军事编制对照 + 冲突时间线 |
| 社会民生 | minimum wage, housing crisis, immigration, gender pay gap, homelessness, poverty line | 社会政策背景 + 数据语境化 + 跨文化差异说明 |

**无领域匹配**：当输入文本未命中任何领域触发词时，跳过领域背景注释，不输出任何领域相关提示。正常执行 6 步分析流程。

## 使用说明

1. 扫描用户输入中的领域关键词
2. 如匹配到某一领域，在对应分析模块中补充背景注释。放置规则见 [output-format.md](output-format.md) 的「🏷️ 领域背景注释输出规范」章节
3. 如同时匹配多个领域，按下方优先级规则排序，优先补充排名最高的领域（最多补充 2 个领域，避免注释过载）

## 多领域重叠优先级规则

当触发词命中多个领域时，按以下启发式依次判定优先领域：

| 优先级 | 规则 | 说明 |
|:------:|------|------|
| 1 | **标题关键词** | 触发词出现在标题或首句中时，该领域为文章主题领域，优先级最高 |
| 2 | **触发词密度** | 统计各领域的触发词出现次数，词频最高的领域优先 |
| 3 | **谓语/动作归属** | 文章核心动作（主语+谓语）所属的领域优先。如"the Fed raised rates amid geopolitical tensions"——核心动作 `raised rates` 归属金融，`geopolitical tensions` 仅为背景 |
| 4 | **消息源身份** | 若消息源具有领域属性（如 Bloomberg → 金融、Defense Ministry → 军事），可辅助判定 |

> **上限**：单篇文章最多注入 2 个领域的背景注释。当 3 个及以上领域同时触发时，仅保留优先级最高的 2 个。

## 不应触发领域注释的情况

以下场景虽出现触发词，但**不应**注入领域背景注释：

| 场景 | 示例 | 原因 |
|------|------|------|
| **比喻/类比用法** | "He called it the Bitcoin of biology" | `Bitcoin` 在此为比喻而非金融讨论 |
| **否定/假设语境** | "There is no risk of pandemic" | 否定句中的触发词不代表文章主题 |
| **跨领域通用词** | "The company filed a lawsuit" | `lawsuit` 在商业新闻中为通用事件，不代表法律司法专题 |
| **历史回顾引用** | "Unlike the 2008 financial crisis, today's economy..." | 历史事件作为对比参照，非当前分析主题 |

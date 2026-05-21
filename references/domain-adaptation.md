# 领域自适应（Domain Adaptation）

SKILL.md 中「领域自适应」章节的完整规则，供 Agent 按需加载。

## 领域触发词与补充内容

| 领域 | 触发词示例 | 补充内容 |
|------|-----------|---------|
| 金融 | Bitcoin, oil prices, Fed, inflation | 术语解释 + 市场联动逻辑 |
| 体育 | marathon, sub-two-hour, world record | 规则说明 + 历史背景 |
| 科技 | AI, quantum, semiconductor | 技术原理简述 + 产业影响 |
| 地缘政治 | Strait of Hormuz, NATO, sanctions | 地理/组织背景 + 冲突脉络 |
| 医疗健康 | vaccine, clinical trial, WHO, pandemic, FDA, epidemic, outbreak, drug approval | 医学术语释义 + 监管机构职能说明 + 公共卫生背景 |
| 环境气候 | carbon emissions, Paris Agreement, COP, glacier, deforestation, renewable energy, sea level | 气候机制简述 + 国际协定背景 + 生态影响链 |
| 法律司法 | Supreme Court, ruling, indictment, lawsuit, conviction, appeal, constitutional, verdict | 法律体系差异说明 + 诉讼流程概要 + 关键法律概念对照 |
| 教育科研 | university ranking, tuition, research paper, peer review, STEM, scholarship, academic | 教育制度对比 + 学术术语解释 + 政策背景 |
| 军事防务 | Pentagon, missile, NATO forces, ceasefire, drone strike, troops, military exercise | 武器系统简述 + 军事编制对照 + 冲突时间线 |
| 社会民生 | minimum wage, housing crisis, immigration, gender pay gap, homelessness, poverty line | 社会政策背景 + 数据语境化 + 跨文化差异说明 |

## 使用说明

1. 扫描用户输入中的领域关键词
2. 如匹配到某一领域，在对应分析模块中补充背景注释
3. 如同时匹配多个领域，按相关性最高的领域优先补充

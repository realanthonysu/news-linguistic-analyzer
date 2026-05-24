# 🗞️ news-linguistic-analyzer

> 英文新闻翻译与深度分析

CN · [EN](README.en.md)

## 功能介绍

本 Skill 为 **Qwen Code / Claude Code** 等 AI 编程助手提供英文新闻翻译与多维度语言学分析能力。用户提供一段英文新闻，Skill 会自动执行以下 **6 步标准化流程**：

| 步骤 | 模块 | 说明 |
|:--:|------|------|
| 📝 | 中文翻译 | 准确、符合新闻语体的分段译文，保留标题层级，内置信息点校验 |
| 🔍 | 用词分析 | 5-8 个关键术语/短语的语境解读（表格形式） |
| 🧱 | 句子结构拆解 | 典型长句的成分标注与中英文逻辑对比 |
| 📐 | 语法结构分析 | 时态、语态、分词、消息源位置等特征 |
| 💡 | 翻译技巧提示 | 3-5 项实用技巧（原文示例 + 处理原理） |
| 🌍 | 延伸思考 | 结合报道伦理、媒介素养的批判性反思 |

此外，Skill 还支持：
- 🎯 **领域自适应**：覆盖金融、体育、科技、地缘政治、医疗健康、环境气候、法律司法、教育科研、军事防务、社会民生等 10 大领域，关键词自动补充背景注释
- ️ **事实核查**：检测未来日期、虚构内容、AI 生成标记并自动预警
- 🔄 **多模式输出**：`仅需翻译` / `简洁模式` / `跳过延伸` 等指令切换分析深度
- 📦 **批量处理**：一次输入多篇新闻，自动分段编号分析
- 📄 **超长文本处理**：>2000 词新闻采用主题感知分段策略，保留上下文衔接并生成全文综述
- 📋 **多步骤任务追踪提示**：内置对 Agent todo list 机制的协作提示，避免遗漏「事实核查」等强制前置步骤
-  **输入安全校验**：内置输入大小限制、路径校验

## 安装

以下两种方式任选其一：

### 方式一：让 Agent 直接安装（推荐）

把本仓库链接发给 Qwen Code / Claude Code 等支持 Agent Skills 的助手：

```text
请安装这个 Skill：https://github.com/realanthonysu/news-linguistic-analyzer
```

Agent 会自动将其克隆到 `~/.qwen/skills/news-linguistic-analyzer/` 并加载。

### 方式二：使用 npx skills 命令安装

```bash
npx skills add https://github.com/realanthonysu/news-linguistic-analyzer --skill news-linguistic-analyzer
```

安装完成后刷新 Agent（执行 `/skills` 确认列表中显示 `news-linguistic-analyzer`）。

## 快速使用

发送一段英文新闻文本即可触发，例如：

- 显式触发（推荐）
```bash
/news-linguistic-analyzer Standoff and Peace Talks: Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports.
```

- 隐式触发
```text
Iran Standoff and Peace Talks: Amid escalating tensions and stalled negotiations, President Trump cancelled a planned trip for US envoys to Pakistan, stating "we have all the cards," Reuters reports.
```



Skill 将自动输出：**中文翻译 → 用词分析 → 句法拆解 → 语法分析 → 翻译技巧 → 延伸思考**

## 目录结构

```
news-linguistic-analyzer/
├── SKILL.md              # 核心指令文件（YAML 元数据 + Markdown 指令）
├── README.md             # 本文件（中文文档）
├── README.en.md          # 英文文档
├── LICENSE               # MIT 许可证
├── scripts/
│   └── validate-input.py # 输入预校验脚本
├── references/
│   ├── domain-adaptation.md    # 领域自适应（10 大领域触发词与补充内容）
│   ├── edge-cases.md           # 边缘情况处理与降级策略
│   ├── examples.md             # 输入/输出对照示例（5 种场景）
│   ├── long-text-processing.md # 超长文本处理规则
│   ├── news-sources.md         # 19 个消息源识别表
│   ├── output-format.md        # 输出格式详细规范
│   └── quality-checklist.md    # 质量检查清单
└── assets/               # （预留）模板、资源文件
```

## 文档

- 完整分析流程与规范：[SKILL.md](SKILL.md)
- 输出格式模板：[references/output-format.md](references/output-format.md)
- 质量检查清单：[references/quality-checklist.md](references/quality-checklist.md)
- 输入/输出示例（5 种场景）：[references/examples.md](references/examples.md)

## 版本历史

### v1.4.6 (2026-05-24)
- 🔧 **元数据规范优化**：从 `description` 拆出工具依赖和环境要求
  - 新增 `compatibility` 字段，声明 `web_search`/`web_fetch` 工具依赖和 Python 3.8+ 要求
  - 新增 `allowed-tools` 字段（实验性），白名单 `web_search web_fetch`
  - `description` 聚焦触发语义，移除环境声明
- 📝 **批量/超长文本决策树**：合并为统一章节，顶部添加判断依据（`---` 分隔 → 批量处理；连续长文 >2000 词 → 超长文本处理）
- ✅ **质量检查措辞加强**：从"自检"改为"**必须**逐项自检，[必检]项未通过须修正"
- 📄 **示例 2 完整化**：从 3 行摘要扩展为完整 7 步端到端输出，与示例 1 结构对齐
- 🚀 **输入校验简化**：`scripts/validate-input.py` 调用方式从 3 步临时文件流程简化为 1 行 stdin 管道命令

### v1.4.5 (2026-05-21)
- 🧹 **逻辑去重**：建立单一信息源原则，避免多处定义不同步
  - 删除 `edge-cases.md` 中与 SKILL.md 主文件重复的「降级策略」条目，改为交叉引用
  - 删除 `edge-cases.md` 中冗余的「超长文本」条目（该规则已在 `long-text-processing.md` 单独覆盖）
- 📝 `scripts/validate-input.py` 在硬编码消息源 fallback 列表前补充 `NOTE` 注释，提醒维护者权威列表在 `references/news-sources.md`

### v1.4.4 (2026-05-21)
- 📋 **多步骤任务追踪提示**：在 SKILL.md 中新增对 Agent 内置 todo list 机制的协作提示（中英双语），明确标注「1 个强制前置步骤 + 6 个分析步骤 = 7 个不可省略环节」，降低「事实核查」前置步骤被跳过的风险
- 🧹 元数据规范化：
  - 移除非规范字段 `tools_required` 和 `compatibility`，将工具依赖与运行环境要求合并到 `description` 字段
  - 字段简化后完全符合 [agentskills.io](https://agentskills.io/specification) 开放标准

### v1.4.3 (2026-05-21)
- 🔧 SKILL.md 元数据字段精简，对齐官方 Agent Skill 规范，仅保留 `name`/`description`/`metadata`/`license` 四个规范认可字段

### v1.4.2 (2026-05-21)
- 🏷️ output-format.md 新增「领域背景注释输出规范」：5 类注释（术语释义/机构背景/逻辑机制/体系差异/历史脉络）与嵌入位置和格式的一一映射
- 🔗 domain-adaptation.md 补充 output-format.md 引用，形成完整引用链

### v1.4.1 (2026-05-21)
- 🔧 重写 SKILL.md description：改用第三人称，增加自然语言触发词（英文+中文），添加 negative triggers 防止误触发，对齐 Anthropic 官方 skill 规范

### v1.4.0 (2026-05-20)
- 🚨 事实核查触发逻辑重构为**两层**：强制触发（6 类条件）+ 模型评估兜底
- 🔍 强制触发条件扩展：含具体日期（无论过去/未来）、人名+重大事件、伤亡/损失敏感数据、正在进行的重大事件、与已知事实冲突、虚构标记词
- 🧠 新增第二层"模型自行评估"：当无明确触发条件时，评估事件是否超出知识截止日期或存在误传风险

### v1.3.3 (2026-05-20)
- 🏗️ 领域自适应表格（10 大领域）移至 `references/domain-adaptation.md`，SKILL.md 保留领域名称列表
- 📝 统一所有输出标题 emoji 为 📝（翻译步骤），消除 📜 混用

### v1.3.2 (2026-05-20)
- 📝 修正 README 中"ReDoS 防护"为准确描述（"输入大小限制、路径校验"）
- 🔧 validate-input.py 地名+事件正则扩展至 14 种事件类型（新增 election/summit/protest/deal/attack/crisis/conflict/agreement/sanctions/referendum）
- 🙈 .gitignore 新增 `.claude/` 目录，排除本地 IDE 配置
- ✅ quality-checklist.md 同步新增模式冲突优先级检查项
- 🔧 validate-input.py 消息源列表改为从 news-sources.md 动态加载，消除双处维护

### v1.3.1 (2026-05-20)
- 🌐 输入校验临时文件路径改为跨平台方案（Python tempfile），兼容 Windows/Linux/macOS
- 🔧 validate-input.py 消息源匹配改用词边界正则（`\b`），避免 `AP` 误匹配 `APPROACH` 等
- 🛡️ edge-cases.md 补充 web search / web fetch 不可用的降级场景
- 🎨 README 功能表补齐 emoji 标记，与 SKILL.md 核心流程表保持一致

### v1.3.0 (2026-05-20)
- 📋 明确 validate-input.py 的 Agent 调用路径，补充临时文件写入步骤和内联判断规则
- 📐 消除 output-format.md 与 long-text-processing.md 的超长文本格式内容重复，改为引用
- 📝 为示例 1 补充完整 6 步端到端输出，提供格式锚点
- ⚖️ 新增模式冲突优先级规则：仅需翻译 > 简洁模式 > 跳过延伸 > 默认完整模式

### v1.2.3 (2026-05-20)
- 🔧 YAML 元数据 `tools_required` 新增 `web_fetch`，显式标注工具依赖
- 🛡️ 联网验证降级策略升级为**三级**：web search（首选）→ web fetch（次选）→ 离线标注（兜底）

### v1.2.2 (2026-05-20)
- 🔧 YAML 元数据新增 `tools_required: [web_search]` 声明，显式标注工具依赖
- 🔍 事实核查搜索查询改为**双语策略**：先英文搜索原始事件，再中文交叉验证
- 🛡️ 新增 web search 不可用时的降级策略
- 📝 修正 README 目录结构，补全 `references/` 下缺失的 3 个文件
- 📝 修正 README.en.md 目录结构的树形字符错误

### v1.2.1 (2026-05-20)
- 🚨 事实核查提升为**强制前置步骤**，确保日期校验和 web search 在翻译前执行
- 🎨 修复 Keycap emoji（1️ 等）在 Windows 终端显示为方框的问题，统一改用标准 emoji
- 📐 为语法结构分析补充 emoji 标记（📐）
-  SKILL.md 核心流程表格新增 emoji 标记列，与 output-format.md 保持同步

### v1.2.0 (2026-05-19)
- SKILL.md 从 237 行精简至 ~130 行，符合 <5000 tokens 约定
- 消息源识别表（19 个）移至 `references/news-sources.md`
- 超长文本处理完整规则移至 `references/long-text-processing.md`
- 边缘情况处理 + 错误降级策略移至 `references/edge-cases.md`
- 翻译信息点校验功能
- 领域自适应扩展至 10 大领域

## 许可证

本项目采用 [MIT License](LICENSE)。你可以自由使用、修改、分发本 Skill，无需保留任何限制。

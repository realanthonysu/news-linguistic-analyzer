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
- 🚨 **事实核查**：强制前置步骤，检测具体日期、人名+重大事件、伤亡/损失数据等自动联网验证；检测虚构标记词直接标注内容属性
- 🔄 **多模式输出**：`仅需翻译` / `简洁模式` / `跳过延伸` 等指令切换分析深度
- 📦 **批量处理**：一次输入多篇新闻，自动分段编号分析
- 📄 **超长文本处理**：>2000 词新闻采用主题感知分段策略，保留上下文衔接并生成全文综述
- 📋 **多步骤任务追踪提示**：内置对 Agent todo list 机制的协作提示，避免遗漏「事实核查」等强制前置步骤
- 🔐 **输入安全校验**：内置输入大小限制、路径校验、边界条件守卫（非英文输入和零散单词/短语自动拦截）

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
│   └── validate-input.py # 输入预校验脚本（含 mypy 类型注解）
├── tests/
│   └── test_validate_input.py # 输入校验脚本单元测试（46 个用例）
├── pyproject.toml        # 项目元数据（PEP 621）+ mypy + ruff 配置
├── references/
│   ├── batch-processing.md     # 批量处理规则
│   ├── domain-adaptation.md    # 领域自适应（10 大领域触发词与补充内容）
│   ├── edge-cases.md           # 边缘情况处理与降级策略
│   ├── examples.md             # 输入/输出对照示例（9 种场景）
│   ├── input-validation.md     # 输入校验调用方式与降级方案
│   ├── long-text-processing.md # 超长文本处理规则
│   ├── news-sources.md         # 27 个消息源识别表
│   ├── output-format.md        # 输出格式详细规范
│   └── quality-checklist.md    # 质量检查清单
```

## 文档

- 完整分析流程与规范：[SKILL.md](SKILL.md)
- 输出格式模板：[references/output-format.md](references/output-format.md)
- 质量检查清单：[references/quality-checklist.md](references/quality-checklist.md)
- 输入/输出示例（9 种场景）：[references/examples.md](references/examples.md)
- 批量处理规则：[references/batch-processing.md](references/batch-processing.md)
- 超长文本处理规则：[references/long-text-processing.md](references/long-text-processing.md)
- 输入校验说明：[references/input-validation.md](references/input-validation.md)

## 版本历史

### v1.9.0 (2026-06-06)
- 🛑 **边界条件守卫**：新增强制前置拦截机制，在事实核查和分析流程之前执行两项边界检测
  - 守卫 1 — 非英文输入检测：字符级 + 词级双重判定，拦截中文、日文、韩文、俄文、阿拉伯文等非英文输入
  - 守卫 2 — 英文单词/短语检测：通过句末标点和主谓结构识别，拦截零散单词或短语，提示用户提供完整句子
  - 新闻标题格式的短文本不受守卫 2 拦截
- 📋 **SKILL.md 结构更新**：新增「🛑 边界条件守卫」章节，输入校验和边缘情况引用同步更新
- 📝 **edge-cases.md 重构**：新增边界条件守卫完整章节，非英文输入策略从"可继续"收紧为"拒绝分析"
- 🔧 **validate-input.py 扩展**：新增语言检测、句子完整性检测、新闻标题识别等功能，`ValidationResult` 新增 `boundary_reject` 字段
- 🧪 **单元测试**：新增 17 个边界条件测试用例（覆盖 6 种非英文语言 + 多种英文输入场景），总计 46 个用例全部通过

### v1.8.0 (2026-06-05)
- 🚨 **事实核查置信度标注**：新增「⚠️ 事实核查（低置信度）」中间态，覆盖单一信源、多源矛盾、细节不一致等场景
- 📦 **超长文本完整示例**：examples.md 新增示例 9（气候变化峰会），展示分段、衔接、全文综述完整结构
- 🎯 **领域重叠优先级启发式**：新增四级优先级规则和四种不应触发场景
- 🌐 **消息源扩展**：从 19 个增至 27 个（新增 AFP、共同社、韩联社、财新、南华早报、塔斯社、安莎社）
- 🔧 **脚本修复**：修复 IndexError、时间词缺失工作日、AI-generated 大小写不匹配、⚠️ emoji 重复等 bug
- 🏗️ **工程规范**：完善 .gitignore、pyproject.toml 新增 PEP 621 元数据、日期注入增加三级降级策略
- 🧪 **单元测试**：新增 `tests/test_validate_input.py`，29 个用例覆盖全部核心功能

### v1.7.0 (2026-06-01)
- 📋 **Skill 规范性优化**：SKILL.md 新增「如何触发」章节，明确触发方式；`!`date`` 命令注入补充跨平台兼容性说明；description 核心触发语义前置；compatibility 补充 allowed-tools fallback 说明
- 🔧 **类型检查配置**：`scripts/validate-input.py` 添加 TypedDict 类型注解；新增 `pyproject.toml` 配置 mypy 静态类型检查

### v1.6.0 (2026-05-31)
- 🗜️ **Token 效率优化**：多步骤任务提示去重、事实核查触发条件表精简、使用模式表压缩
- 🔧 **动态上下文注入**：SKILL.md 新增 `` !`date +%Y-%m-%d` `` 命令注入，事实核查步骤可自动获取当前日期（Claude Code 专有，其他平台自动降级）

### v1.5.1 (2026-05-31)
- 🚨 **事实核查提示格式统一**：将「虚构标记词」从强制触发条件中移出为特殊路径，检测到虚构标记词时跳过 web search 直接标注
- 📝 **统一两种提示格式**：「⚠️ 事实核查」= 已联网验证；「⚠️ 内容属性提示」= 检测到虚构标记词，无需联网
- 📦 **新增 3 个示例**（examples.md 从 5 个扩增至 8 个）：事实核查触发（已联网验证）、垂直领域医疗健康、「跳过延伸」模式
- 🔗 **quality-checklist.md 交叉引用补全**：批量处理和超长文本附加检查处补充快速对照清单，形成双向引用链

### v1.5.0 (2026-05-31)
- 📦 **SKILL.md 精简**：将「批量处理」「输入校验」的完整规则移至 references/，主文件仅保留简要说明和链接
  - 新增 `references/batch-processing.md`：批量处理的分割方式、输出结构、质量检查
  - 新增 `references/input-validation.md`：脚本调用方式、退出码说明、内联判断降级方案
  - 「超长文本处理」已有独立文件，SKILL.md 同步精简为一句话 + 链接
- 🎯 SKILL.md 从 ~180 行精简至 ~160 行，进一步降低 token 开销

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

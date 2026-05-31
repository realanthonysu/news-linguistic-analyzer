# Changelog

All notable changes to this project will be documented in this file.

## v1.6.0 (2026-05-31)

- **Token 效率优化**：
  - 多步骤任务提示删除英文版本，保留中文，从 ~4 行压缩至 ~2 行
  - 事实核查触发条件表精简说明列，去掉冗余示例
  - 使用模式表压缩措辞，模式冲突优先级说明更简洁
- **动态上下文注入（Claude Code 专有）**：
  - SKILL.md 新增 `!`date +%Y-%m-%d`` 命令注入，事实核查步骤可自动获取当前日期
  - 跨平台降级：Qwen Code 等不支持 `` !`command` `` 语法的平台，该行作为普通文本保留，不影响功能

## v1.5.1 (2026-05-31)

- **事实核查提示格式统一**：
  - SKILL.md 将「虚构标记词」从强制触发条件中移出为特殊路径，检测到虚构标记词时跳过 web search 直接标注
  - 统一两种提示格式的使用场景：「⚠️ 事实核查」= 已联网验证；「⚠️ 内容属性提示」= 检测到虚构标记词，无需联网
  - `output-format.md` 新增「🚨 事实核查输出格式」章节，含格式 A/B 对照表和区分规则
  - 修正 `examples.md` 示例 4，统一使用「⚠️ 内容属性提示」格式
- **新增 3 个示例**（examples.md 从 5 个扩增至 8 个）：
  - 示例 6：事实核查触发（已联网验证，含 web search 查询摘要输出格式锚点）
  - 示例 7：垂直领域 — 医疗健康（展示 🏛️ 领域背景注释嵌入用词分析表格的完整效果）
  - 示例 8：「跳过延伸」模式（展示省略步骤 6 的输出结构）
- **quality-checklist.md 交叉引用补全**：批量处理和超长文本附加检查处补充快速对照清单，形成双向引用链

## v1.5.0 (2026-05-31)

- **SKILL.md 精简**：将「批量处理」「输入校验」的完整规则移至 references/，主文件仅保留简要说明和链接
  - 新增 `references/batch-processing.md`：批量处理的分割方式、输出结构、质量检查
  - 新增 `references/input-validation.md`：脚本调用方式、退出码说明、内联判断降级方案
  - 「超长文本处理」已有独立文件，SKILL.md 同步精简为一句话 + 链接
- quality-checklist.md 中批量处理和超长文本的重复检查项改为交叉引用，遵循单一信息源原则
- SKILL.md 从 ~180 行精简至 ~160 行，进一步降低 token 开销

## v1.4.6 (2026-05-24)

- **元数据规范优化**：从 `description` 拆出工具依赖和环境要求
  - 新增 `compatibility` 字段，声明 `web_search`/`web_fetch` 工具依赖和 Python 3.8+ 要求
  - 新增 `allowed-tools` 字段（实验性），白名单 `web_search web_fetch`
  - `description` 聚焦触发语义，移除环境声明
- **批量/超长文本决策树**：合并为统一章节，顶部添加判断依据（`---` 分隔 → 批量处理；连续长文 >2000 词 → 超长文本处理）
- **质量检查措辞加强**：从"自检"改为"**必须**逐项自检，[必检]项未通过须修正"
- **示例 2 完整化**：从 3 行摘要扩展为完整 7 步端到端输出，与示例 1 结构对齐
- **输入校验简化**：`scripts/validate-input.py` 调用方式从 3 步临时文件流程简化为 1 行 stdin 管道命令

## v1.4.5 (2026-05-21)

- **逻辑去重**：建立单一信息源原则，避免多处定义不同步
  - 删除 `edge-cases.md` 中与 SKILL.md 主文件重复的「降级策略」条目，改为交叉引用
  - 删除 `edge-cases.md` 中冗余的「超长文本」条目（该规则已在 `long-text-processing.md` 单独覆盖）
- `scripts/validate-input.py` 在硬编码消息源 fallback 列表前补充 `NOTE` 注释，提醒维护者权威列表在 `references/news-sources.md`

## v1.4.4 (2026-05-21)

- **多步骤任务追踪提示**：在 SKILL.md 中新增对 Agent 内置 todo list 机制的协作提示（中英双语），明确标注「1 个强制前置步骤 + 6 个分析步骤 = 7 个不可省略环节」，降低「事实核查」前置步骤被跳过的风险
- 元数据规范化：
  - 移除非规范字段 `tools_required` 和 `compatibility`，将工具依赖与运行环境要求合并到 `description` 字段
  - 字段简化后完全符合 [agentskills.io](https://agentskills.io/specification) 开放标准

## v1.4.3 (2026-05-21)

- SKILL.md 元数据字段精简，对齐官方 Agent Skill 规范，仅保留 `name`/`description`/`metadata`/`license` 四个规范认可字段

## v1.4.2 (2026-05-21)

- `output-format.md` 新增「领域背景注释输出规范」：5 类注释（术语释义/机构背景/逻辑机制/体系差异/历史脉络）与嵌入位置和格式的一一映射
- `domain-adaptation.md` 补充 `output-format.md` 引用，形成完整引用链

## v1.4.1 (2026-05-21)

- 重写 SKILL.md description：改用第三人称，增加自然语言触发词（英文+中文），添加 negative triggers 防止误触发，对齐 Anthropic 官方 skill 规范
- 新增 README.en.md 中英双语支持

## v1.4.0 (2026-05-20)

- 事实核查触发逻辑重构为**两层**：强制触发（6 类条件）+ 模型评估兜底
- 强制触发条件扩展：含具体日期（无论过去/未来）、人名+重大事件、伤亡/损失敏感数据、正在进行的重大事件、与已知事实冲突、虚构标记词
- 新增第二层"模型自行评估"：当无明确触发条件时，评估事件是否超出知识截止日期或存在误传风险

## v1.3.3 (2026-05-20)

- 领域自适应表格（10 大领域）移至 `references/domain-adaptation.md`，SKILL.md 保留领域名称列表
- 统一所有输出标题 emoji 为 📝（翻译步骤），消除 📜 混用

## v1.3.2 (2026-05-20)

- 修正 README 中"ReDoS 防护"为准确描述（"输入大小限制、路径校验"）
- `validate-input.py` 地名+事件正则扩展至 14 种事件类型（新增 election/summit/protest/deal/attack/crisis/conflict/agreement/sanctions/referendum）
- `.gitignore` 新增 `.claude/` 目录，排除本地 IDE 配置
- `quality-checklist.md` 同步新增模式冲突优先级检查项
- `validate-input.py` 消息源列表改为从 `news-sources.md` 动态加载，消除双处维护

## v1.3.1 (2026-05-20)

- 输入校验临时文件路径改为跨平台方案（Python tempfile），兼容 Windows/Linux/macOS
- `validate-input.py` 消息源匹配改用词边界正则（`\b`），避免 `AP` 误匹配 `APPROACH` 等
- `edge-cases.md` 补充 web search / web fetch 不可用的降级场景
- README 功能表补齐 emoji 标记，与 SKILL.md 核心流程表保持一致

## v1.3.0 (2026-05-20)

- 明确 `validate-input.py` 的 Agent 调用路径，补充临时文件写入步骤和内联判断规则
- 消除 `output-format.md` 与 `long-text-processing.md` 的超长文本格式内容重复，改为引用
- 为示例 1 补充完整 6 步端到端输出，提供格式锚点
- 新增模式冲突优先级规则：仅需翻译 > 简洁模式 > 跳过延伸 > 默认完整模式

## v1.2.3 (2026-05-20)

- YAML 元数据 `tools_required` 新增 `web_fetch`，显式标注工具依赖
- 联网验证降级策略升级为**三级**：web search（首选）→ web fetch（次选）→ 离线标注（兜底）

## v1.2.2 (2026-05-20)

- YAML 元数据新增 `tools_required: [web_search]` 声明，显式标注工具依赖
- 事实核查搜索查询改为**双语策略**：先英文搜索原始事件，再中文交叉验证
- 新增 web search 不可用时的降级策略
- 修正 README 目录结构，补全 `references/` 下缺失的 3 个文件
- 修正 README.en.md 目录结构的树形字符错误

## v1.2.1 (2026-05-20)

- 事实核查提升为**强制前置步骤**，确保日期校验和 web search 在翻译前执行
- 修复 Keycap emoji（1️ 等）在 Windows 终端显示为方框的问题，统一改用标准 emoji
- 为语法结构分析补充 emoji 标记（📐）
- SKILL.md 核心流程表格新增 emoji 标记列，与 output-format.md 保持同步

## v1.2.0 (2026-05-19)

- SKILL.md 从 237 行精简至 ~130 行，符合 <5000 tokens 约定
- 消息源识别表（19 个）移至 `references/news-sources.md`
- 超长文本处理完整规则移至 `references/long-text-processing.md`
- 边缘情况处理 + 错误降级策略移至 `references/edge-cases.md`
- 翻译信息点校验功能
- 领域自适应扩展至 10 大领域

# 🗞️ news-linguistic-analyzer

> 英文新闻翻译与深度分析

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

## 功能介绍

本 Skill 为 **Qwen Code / Claude Code** 等 AI 编程助手提供英文新闻翻译与多维度语言学分析能力。用户提供一段英文新闻，Skill 会自动执行以下 **6 步标准化流程**：

| 步骤 | 模块 | 说明 |
|:--:|------|------|
| 1️⃣ | 中文翻译 | 准确、符合新闻语体的分段译文，保留标题层级 |
| 2️⃣ | 用词分析 | 5-8 个关键术语/短语的语境解读（表格形式） |
| 3️⃣ | 句子结构拆解 | 典型长句的成分标注与中英文逻辑对比 |
| 4️⃣ | 语法结构分析 | 时态、语态、分词、消息源位置等特征 |
| 5️⃣ | 翻译技巧提示 | 3-5 项实用技巧（原文示例 + 处理原理） |
| 6️⃣ | 延伸思考 | 🌍 结合报道伦理、媒介素养的批判性反思 |

此外，Skill 还支持：
- **领域自适应**：金融、体育、科技、地缘政治等关键词自动补充背景注释
- **事实核查**：检测未来日期、虚构内容、AI 生成标记并自动预警
- **多模式输出**：`仅需翻译` / `简洁模式` / `跳过延伸` 等指令切换分析深度
- **批量处理**：一次输入多篇新闻，自动分段编号分析

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
├── README.md             # 本文件
├── LICENSE               # MIT 许可证
├── scripts/
│   └── validate-input.py # 输入预校验脚本
├── references/
│   ├── output-format.md  # 输出格式详细规范
│   ├── quality-checklist.md  # 质量检查清单
│   └── examples.md       # 输入/输出对照示例（5 种场景）
└── assets/               # （预留）模板、资源文件
```

## 文档

- 完整分析流程与规范：[SKILL.md](SKILL.md)
- 输出格式模板：[references/output-format.md](references/output-format.md)
- 质量检查清单：[references/quality-checklist.md](references/quality-checklist.md)
- 输入/输出示例（5 种场景）：[references/examples.md](references/examples.md)

## 许可证

本项目采用 [MIT License](LICENSE)。你可以自由使用、修改、分发本 Skill，无需保留任何限制。

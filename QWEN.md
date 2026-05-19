# 🗞️ news-linguistic-analyzer

英文新闻翻译与深度分析 Qwen Code Skill。

## 项目概述

这是一个为 **Qwen Code** 编写的 Skill，用于对英文新闻文本进行专业翻译与多维度语言学分析。用户提供一段英文新闻，Skill 会输出：

1. **中文翻译** — 准确、符合新闻语体的译文
2. **用词分析** — 5-8 个关键术语/短语的语境解读（表格形式）
3. **句子结构拆解** — 典型长句的成分标注与中英文逻辑对比
4. **语法结构分析** — 时态、语态、分词、消息源位置等特征
5. **翻译技巧提示** — 3-5 项实用技巧（示例 + 原理）
6. **延伸思考** — 结合报道伦理、媒介素养等维度的批判性反思

## 目录结构

```
news-linguistic-analyzer/
├── README.md                          # 安装与快速入门指南
├── SKILL.md                           # Skill 定义文件（核心配置）
├── QWEN.md                            # 本文件
└── templates/
    ├── output-format.md               # 输出格式模板（模型内部参考）
    ├── analysis-checklist.md          # 质量检查清单（输出前自检）
    └── validate-input.py              # 输入预校验脚本（CLI 工具）
```

## 安装方式

```bash
# 1. 创建 Skill 目录
mkdir -p ~/.qwen/skills/news-linguistic-analyzer

# 2. 复制本套件所有文件（保持 templates/ 子目录结构）
cp -r * ~/.qwen/skills/news-linguistic-analyzer/

# 3. 赋予脚本执行权限
chmod +x ~/.qwen/skills/news-linguistic-analyzer/templates/validate-input.py

# 4. 重启 Qwen Code 或执行 /skills 刷新
/skills  # 确认列表中显示 news-linguistic-analyzer
```

## 触发方式

当用户输入包含以下特征时，Skill 自动触发：
- 明显英文新闻特征（标题 + 正文 + 消息源）
- 触发词：`英文新闻`、`翻译分析`、`news analysis`、`lexical analysis`、`Reuters`、`BBC`、`AP`、`breaking news`、`translate and analyze`

也可显式调用：`/skills news-linguistic-analyzer + 你的文本`

## 使用模式

| 模式 | 触发关键词 | 行为 |
|------|-----------|------|
| **标准模式** | 无特殊关键词 | 执行完整 6 步分析 |
| **仅翻译** | `仅需翻译` / `translation only` | 仅输出中文翻译 |
| **跳过延伸** | `跳过延伸` / `no reflection` | 省略步骤 6（延伸思考） |
| **简洁模式** | `简洁模式` / `brief` | 用词分析限 3 项，技巧提示限 2 项 |

## 输入校验脚本

`templates/validate-input.py` 可独立运行，用于预判断输入是否为新闻文本：

```bash
# 从 stdin 读取
echo "Your news text here" | python templates/validate-input.py

# 从文件读取
python templates/validate-input.py input.txt
```

**退出码含义**：
| 退出码 | 含义 | 处理方式 |
|--------|------|---------|
| `0` | 疑似新闻文本 | 正常执行分析 |
| `1` | 不确定 | 开头添加「❓ 内容属性待确认」提示 |
| `2` | 非新闻文本 | 回复询问是否仍要执行分析 |

## 事实核查机制

如检测到以下特征，**必须在输出开头添加警告**：
- 日期晚于系统当前时间
- 人物/事件与已知事实明显冲突
- 含虚构标记词：`fiction`、`scenario`、`hypothetical`、`AI-generated`

## 领域自适应

检测到特定领域关键词时自动补充背景注释：

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

## 输出语言

全程使用 **中文** 回复（参见 `.qwen/output-language.md` 全局配置）。

## 质量保障

生成输出前需对照 `templates/analysis-checklist.md` 自检，覆盖：
- **基础完整性** — 翻译覆盖、术语数量、句型典型性
- **专业准确性** — 专有名词、时态逻辑、被动语态处理
- **事实核查** — 日期/人物/事件验证
- **用户体验** — 表格格式、术语解释、视觉层次
- **伦理与边界** — 情绪化渲染规避、主观评论限制

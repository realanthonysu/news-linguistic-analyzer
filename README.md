# 🗞️ news-linguistic-analyzer

> 英文新闻翻译与深度分析

## 安装

```bash
# 1. 创建目录
mkdir -p ~/.qwen/skills/news-linguistic-analyzer

# 2. 复制本套件（保持子目录结构）
cp -r * ~/.qwen/skills/news-linguistic-analyzer/

# 3. 赋予脚本执行权限
chmod +x ~/.qwen/skills/news-linguistic-analyzer/scripts/validate-input.py

# 4. 刷新
/skills  # 确认显示 news-linguistic-analyzer
```

## 快速使用

发送一段英文新闻文本即可触发，例如：

```text
Iran Standoff and Peace Talks: Amid escalating tensions and stalled negotiations,
President Trump cancelled a planned trip for US envoys to Pakistan,
stating "we have all the cards," Reuters reports.
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

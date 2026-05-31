# 输入校验（Input Validation）

SKILL.md 中「输入校验」章节的完整规则，供 Agent 按需加载。

## 概述

当不确定输入是否为新闻文本时，可运行预校验脚本辅助判断。此步骤为**可选**，不影响核心分析流程。

## 调用方式

### 方式一（推荐）：stdin 管道输入

```bash
echo "<用户输入内容>" | python scripts/validate-input.py
```

### 方式二：文件路径参数

```bash
python scripts/validate-input.py <文件路径>
```

## 退出码与后续操作

| 退出码 | 含义 | Agent 处理方式 |
|--------|------|---------------|
| `0` | 疑似新闻文本 | 正常执行分析 |
| `1` | 不确定 | 在输出开头添加「❓ 内容属性待确认」提示 |
| `2` | 非新闻文本 | 回复「该内容疑似非新闻文本，是否仍要执行语言分析？[是/否]」 |

## 内联判断规则（脚本不可用时的降级方案）

如无法执行脚本，可按以下规则内联判断：

1. **消息源标识**：检测是否包含已知新闻源（Reuters、BBC、AP 等），完整列表见 [news-sources.md](news-sources.md)
2. **新闻高频动词**：`reports`、`announced`、`stated`、`confirmed`、`according to`
3. **时效性词汇**：`today`、`yesterday`、`this week`、具体星期几
4. **虚构标记词**：`fiction`、`scenario`、`hypothetical`、`AI-generated` — 检测到则触发事实核查

## 脚本说明

`scripts/validate-input.py` 是一个独立的 CLI 工具，基于正则匹配和置信度评分判断输入是否为新闻文本。它会：

- 动态加载 `references/news-sources.md` 中的消息源列表
- 检测正向特征（消息源、新闻动词、时效性词汇、标题格式、地名+事件组合）
- 检测负向特征（未来日期、虚构标记词、非新闻文体）
- 返回置信度评分和建议操作

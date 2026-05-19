#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
news-linguistic-analyzer 输入预校验脚本
功能：判断用户输入是否为典型英文新闻文本，辅助模型决策是否调用本 Skill
"""

import re
from datetime import datetime

def is_likely_news(text: str) -> dict:
    """
    预校验输入文本
    返回: {
        'is_news': bool,
        'confidence': float (0-1),
        'flags': list[str]  # 检测到的特征/疑点
    }
    """
    flags = []
    score = 0.0
    
    # === 正向特征（加分项）===
    
    # 1. 消息源标识
    news_sources = ['Reuters', 'AP', 'BBC', 'ABC News', 'PBS', 'CNN', 'Al Jazeera']
    if any(src in text for src in news_sources):
        score += 0.3
        flags.append(f"detected_source:{[s for s in news_sources if s in text][0]}")
    
    # 2. 新闻高频动词
    news_verbs = ['reports', 'says', 'announced', 'confirmed', 'stated', 'according to']
    if any(v in text.lower() for v in news_verbs):
        score += 0.2
        flags.append("detected_news_verb")
    
    # 3. 时效性词汇
    time_words = ['today', 'yesterday', 'Saturday', 'Sunday', 'this week', 'as of']
    if any(t in text.lower() for t in time_words):
        score += 0.15
        flags.append("detected_time_marker")
    
    # 4. 标题特征（首行大写+冒号/短横线）
    lines = text.strip().split('\n')
    if lines and re.match(r'^[A-Z][^\.]{20,}[:\-]', lines[0]):
        score += 0.2
        flags.append("likely_headline")
    
    # 5. 地名+事件组合
    geo_event = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s*[:\-,]?\s*(?:shooting|bombing|tornado|talks|strike)'
    if re.search(geo_event, text, re.I):
        score += 0.15
        flags.append("detected_geo_event")
    
    # === 负向特征（减分项/警示）===
    
    # 1. 未来日期检测
    current_year = datetime.now().year
    future_years = [str(y) for y in range(current_year + 1, current_year + 10)]
    if any(y in text for y in future_years):
        flags.append(f"⚠️ future_date_detected:{[y for y in future_years if y in text][0]}")
        # 不扣分，但标记供后续事实核查使用
    
    # 2. 虚构标记词
    fiction_markers = ['fiction', 'scenario', 'hypothetical', 'AI-generated', 'creative writing']
    if any(m in text.lower() for m in fiction_markers):
        flags.append("⚠️ fiction_marker_detected")
        score -= 0.3
    
    # 3. 非新闻文体特征
    if re.search(r'(once upon a time|dear diary|poem|verse)', text, re.I):
        flags.append("⚠️ non_news_genre_detected")
        score -= 0.4
    
    # === 结果判定 ===
    confidence = max(0.0, min(1.0, score))
    is_news = confidence >= 0.5
    
    return {
        'is_news': is_news,
        'confidence': round(confidence, 2),
        'flags': flags,
        'suggestion': 'proceed' if is_news else 'ask_user' if confidence > 0.3 else 'decline'
    }


def format_validation_report(result: dict) -> str:
    """生成人类可读的校验报告"""
    report = [f"🔍 输入校验结果：{'✅ 疑似新闻文本' if result['is_news'] else '❓ 不确定 / ❌ 非新闻'}"]
    report.append(f"置信度：{result['confidence']:.0%}")
    if result['flags']:
        report.append("检测特征：")
        for flag in result['flags']:
            prefix = "⚠️ " if flag.startswith("⚠️") else "• "
            report.append(f"  {prefix}{flag}")
    return '\n'.join(report)


# === CLI 测试入口 ===
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # 从文件读取
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        # 从 stdin 读取
        text = sys.stdin.read()
    
    result = is_likely_news(text)
    print(format_validation_report(result))
    # 退出码：0=建议处理，1=建议询问，2=建议拒绝
    sys.exit(0 if result['suggestion'] == 'proceed' else (1 if result['suggestion'] == 'ask_user' else 2))
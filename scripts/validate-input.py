#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
news-linguistic-analyzer 输入预校验脚本
功能：判断用户输入是否为典型英文新闻文本，辅助模型决策是否调用本 Skill
"""

from __future__ import annotations

import logging
import os
import re
import sys
import unicodedata
from datetime import datetime
from typing import TypedDict


class ValidationResult(TypedDict):
    """预校验结果数据结构"""
    is_news: bool
    confidence: float
    flags: list[str]
    suggestion: str
    boundary_reject: str | None  # 'non_english' | 'words_only' | None


MAX_INPUT_SIZE = 1_000_000


def _is_latin_char(char: str) -> bool:
    """判断字符是否为拉丁字母（含扩展）"""
    name = unicodedata.name(char, '')
    return 'LATIN' in name


def _detect_english_ratio(text: str) -> float:
    """计算文本中英文（拉丁）字母占总字母的比例"""
    alpha_chars = [c for c in text if c.isalpha()]
    if not alpha_chars:
        return 0.0
    latin_chars = sum(1 for c in alpha_chars if _is_latin_char(c))
    return latin_chars / len(alpha_chars)


def _has_complete_sentence(text: str) -> bool:
    """检测文本是否包含至少一个完整的英文句子（主语+谓语动词）"""
    # 检查是否存在句末标点
    has_end_punct = bool(re.search(r'[.!?]', text))
    if not has_end_punct:
        return False
    # 简单的主谓结构检测：找到一个句子中存在 主语（名词/代词）+ 动词 的搭配
    # 按句末标点分割，检查每个子句
    sentences = re.split(r'[.!?]+', text)
    common_verbs = {
        # auxiliary / modal
        'is', 'are', 'was', 'were', 'has', 'have', 'had', 'do', 'does', 'did',
        'will', 'would', 'could', 'should', 'may', 'might', 'shall', 'can',
        # general high-frequency verbs
        'said', 'says', 'reported', 'announced', 'confirmed', 'stated',
        'told', 'asked', 'called', 'made', 'took', 'went', 'came', 'gave',
        'found', 'knew', 'thought', 'saw', 'looked', 'used', 'worked',
        'became', 'left', 'began', 'showed', 'wanted', 'seemed', 'kept',
        'killed', 'died', 'hit', 'reached', 'fell', 'rose', 'won', 'lost',
        # news verbs — attribution & reporting
        'added', 'admitted', 'alleged', 'argued', 'claimed', 'concluded',
        'continued', 'denied', 'disclosed', 'indicated', 'noted', 'revealed',
        'suggested', 'tells',
        # news verbs — action & decision
        'adjourned', 'approved', 'authorised', 'authorized', 'converged',
        'cut', 'declined', 'deliberated', 'dropped', 'expected', 'increased',
        'launched', 'mandated', 'ordered', 'passed', 'petitioned', 'pledged',
        'proposed', 'raised', 'ratified', 'rejected', 'signed', 'scrapped',
        'unveiled', 'voted', 'vowed', 'warned',
        # news verbs — investigation
        'investigated', 'launched', 'probed', 'testified', 'threatened',
        'uncovers',
    }
    pronouns = {
        'i', 'you', 'he', 'she', 'it', 'we', 'they',
        'this', 'that', 'these', 'those', 'who', 'which', 'what',
    }
    for sent in sentences:
        words = sent.lower().split()
        if len(words) < 2:
            continue
        has_verb = any(w.strip('.,;:!?\'"()') in common_verbs for w in words)
        has_subject = any(w.strip('.,;:!?\'"()') in pronouns for w in words)
        # 或者检查大写开头的词（专有名词）作为主语
        has_proper_noun = any(re.match(r'^[A-Z][a-z]+', w) for w in sent.split())
        if has_verb and (has_subject or has_proper_noun):
            return True
    return False


def _is_headline(text: str) -> bool:
    """检测是否为新闻标题格式（短文本、首字母大写、含动词、无句末标点）"""
    text = text.strip()
    if len(text.split()) < 3 or len(text.split()) > 15:
        return False
    if re.search(r'[.!?]', text):
        return False
    if not text[0].isupper():
        return False
    news_verbs = ['reports', 'says', 'announced', 'announces', 'confirmed', 'confirms',
                  'stated', 'states', 'hit', 'hits',
                  'kills', 'dies', 'wins', 'loses', 'rises', 'falls', 'calls',
                  'warns', 'urges', 'seeks', 'faces', 'signs', 'passes',
                  'surge', 'soar', 'slam', 'vow', 'pledge', 'launch', 'probe']
    lower_text = text.lower()
    return any(re.search(r'\b' + re.escape(v) + r'\b', lower_text) for v in news_verbs)


def _load_news_sources() -> list[str]:
    """从 references/news-sources.md 动态加载消息源列表"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sources_path = os.path.join(script_dir, '..', 'references', 'news-sources.md')
    sources = []
    try:
        with open(sources_path, 'r', encoding='utf-8') as f:
            in_table = False
            for line in f:
                line = line.strip()
                if line.startswith('| 缩写/原名'):
                    in_table = True
                    continue
                if in_table and line.startswith('|') and not line.startswith('|---'):
                    parts = [p.strip() for p in line.split('|')]
                    if len(parts) >= 2:
                        name = parts[1]
                        if name and name != '缩写/原名':
                            sources.append(name)
    except (FileNotFoundError, IOError) as e:
        logging.debug("Failed to load news sources from %s: %s", sources_path, e)
    return sources

def is_likely_news(text: str) -> ValidationResult:
    """
    预校验输入文本
    返回: ValidationResult 字典，包含 is_news, confidence, flags, suggestion, boundary_reject
    """
    flags = []
    score = 0.0

    if len(text) > MAX_INPUT_SIZE:
        return {
            'is_news': False,
            'confidence': 0.0,
            'flags': [f"⚠️ input_too_large:{len(text)} bytes (max {MAX_INPUT_SIZE})"],
            'suggestion': 'decline',
            'boundary_reject': None
        }

    # === 边界条件守卫（优先于一切检测）===

    # 守卫 1：非英文输入检测
    english_ratio = _detect_english_ratio(text)
    # 字符级检测：拉丁字母占比低于 30%
    # 词级补充检测：含非拉丁字符且纯英文单词 ≤5 个（防止少量英文关键词拉高字符占比）
    has_non_latin = any(
        c.isalpha() and not _is_latin_char(c)
        for c in text
    )
    english_word_count = len(re.findall(r'\b[a-zA-Z]+\b', text))
    is_non_english = (
        english_ratio < 0.3
        or (has_non_latin and english_word_count <= 5)
    )
    if is_non_english:
        return {
            'is_news': False,
            'confidence': 0.0,
            'flags': [f"⚠️ non_english_input (english_ratio={english_ratio:.0%})"],
            'suggestion': 'decline',
            'boundary_reject': 'non_english'
        }

    # 守卫 2：英文单词/短语而非完整句子检测
    word_count = len(text.split())
    if word_count >= 1 and not _is_headline(text):
        has_sentence = _has_complete_sentence(text)
        has_end_punct = bool(re.search(r'[.!?]', text))
        if not has_sentence and not has_end_punct:
            return {
                'is_news': False,
                'confidence': 0.0,
                'flags': [f"⚠️ words_only_input (word_count={word_count}, no_complete_sentence)"],
                'suggestion': 'decline',
                'boundary_reject': 'words_only'
            }
    
    # === 正向特征（加分项）===
    
    # 1. 消息源标识
    news_sources = _load_news_sources()
    if not news_sources:
        # NOTE: 以下硬编码列表仅作为动态加载失败时的最小 fallback。
        # 权威消息源列表请维护在 references/news-sources.md，避免双源不同步。
        news_sources = [
            'Reuters', 'AP', 'BBC', 'ABC News', 'PBS', 'CNN', 'Al Jazeera',
            'The New York Times', 'The Guardian', 'The Washington Post',
            'Bloomberg', 'The Wall Street Journal', 'The Economist',
            'NHK', 'DW', 'France 24', 'Xinhua', 'CNBC', 'NPR',
            'Associated Press', 'AFP', 'Kyodo News', 'Yonhap',
            'Caixin', 'South China Morning Post', 'TASS', 'ANSA',
        ]
    matched = next(
        (s for s in news_sources if re.search(r'\b' + re.escape(s) + r'\b', text)),
        None
    )
    if matched is not None:
        score += 0.3
        flags.append(f"detected_source:{matched}")
    
    # 2. 新闻高频动词
    news_verbs = ['reports', 'says', 'announced', 'confirmed', 'stated', 'according to']
    if any(v in text.lower() for v in news_verbs):
        score += 0.2
        flags.append("detected_news_verb")
    
    # 3. 时效性词汇
    time_words = [
        'today', 'yesterday', 'tomorrow',
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
        'this week', 'last week', 'as of',
    ]
    if any(t in text.lower() for t in time_words):
        score += 0.15
        flags.append("detected_time_marker")
    
    # 4. 标题特征（首行大写+冒号/短横线）
    lines = text.strip().split('\n')
    if lines and re.match(r'^[A-Z][^\.]{20,80}[:\-]', lines[0]):
        score += 0.2
        flags.append("likely_headline")
    
    # 5. 地名+事件组合
    geo_event = r'\b(?:[A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,3})\s*[:\-,]?\s*(?:shooting|bombing|tornado|talks|strike|election|summit|protest|deal|attack|crisis|conflict|agreement|sanctions|referendum)'
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
    fiction_markers = ['fiction', 'scenario', 'hypothetical', 'ai-generated', 'creative writing']
    if any(m in text.lower() for m in fiction_markers):
        flags.append("⚠️ fiction_marker_detected")
        score -= 0.3
    
    # 3. 非新闻文体特征
    non_news_patterns = ['once upon a time', 'dear diary', 'poem', 'verse']
    if any(p in text.lower() for p in non_news_patterns):
        flags.append("⚠️ non_news_genre_detected")
        score -= 0.4
    
    # === 结果判定 ===
    confidence = max(0.0, min(1.0, score))
    is_news = confidence >= 0.5
    
    return {
        'is_news': is_news,
        'confidence': round(confidence, 2),
        'flags': flags,
        'suggestion': 'proceed' if is_news else 'ask_user' if confidence > 0.3 else 'decline',
        'boundary_reject': None
    }


def format_validation_report(result: ValidationResult) -> str:
    """生成人类可读的校验报告"""
    # 边界条件拦截优先展示
    if result.get('boundary_reject') == 'non_english':
        report = ["🚫 边界条件拦截：输入为非英文文本"]
        report.append("本 skill 专为英文新闻精读设计，请提供一段英文新闻文本后再使用。")
        if result['flags']:
            for flag in result['flags']:
                report.append(f"  {flag}")
        return '\n'.join(report)
    if result.get('boundary_reject') == 'words_only':
        report = ["🚫 边界条件拦截：输入为英文单词/短语，而非完整句子"]
        report.append("请提供至少一句完整的英文句子，最好是一段英文新闻正文（推荐 50-500 词）。")
        if result['flags']:
            for flag in result['flags']:
                report.append(f"  {flag}")
        return '\n'.join(report)

    report = [f"🔍 输入校验结果：{'✅ 疑似新闻文本' if result['is_news'] else '❓ 不确定 / ❌ 非新闻'}"]
    report.append(f"置信度：{result['confidence']:.0%}")
    if result['flags']:
        report.append("检测特征：")
        for flag in result['flags']:
            if flag.startswith("⚠️"):
                report.append(f"  {flag}")
            else:
                report.append(f"  • {flag}")
    return '\n'.join(report)


# === CLI 测试入口 ===
if __name__ == '__main__':
    if sys.platform == 'win32':
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
        if hasattr(sys.stderr, 'reconfigure'):
            sys.stderr.reconfigure(encoding='utf-8')

    text = ''
    if len(sys.argv) > 1:
        file_path = os.path.realpath(sys.argv[1])
        if not os.path.isfile(file_path):
            print(f"❌ 文件不存在：{sys.argv[1]}", file=sys.stderr)
            sys.exit(2)
        file_size = os.path.getsize(file_path)
        if file_size > MAX_INPUT_SIZE:
            print(f"❌ 文件过大：{file_size} bytes (上限 {MAX_INPUT_SIZE} bytes)", file=sys.stderr)
            sys.exit(2)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
        except UnicodeDecodeError:
            result: ValidationResult = {
                'is_news': False, 'confidence': 0.0, 'flags': ["文件编码错误"],
                'suggestion': 'decline', 'boundary_reject': 'words_only'
            }
            print(format_validation_report(result))
            sys.exit(2)
    else:
        raw = sys.stdin.read()
        if len(raw) > MAX_INPUT_SIZE:
            result = {
                'is_news': False, 'confidence': 0.0,
                'flags': [f"input_too_large:{len(raw)} bytes (max {MAX_INPUT_SIZE})"],
                'suggestion': 'decline', 'boundary_reject': None
            }
            print(format_validation_report(result))
            sys.exit(2)
        text = raw
    
    result = is_likely_news(text)
    print(format_validation_report(result))
    # 退出码：0=建议处理，1=建议询问，2=建议拒绝（含边界条件拦截）
    if result.get('boundary_reject'):
        sys.exit(2)
    sys.exit(0 if result['suggestion'] == 'proceed' else (1 if result['suggestion'] == 'ask_user' else 2))
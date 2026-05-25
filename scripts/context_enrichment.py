#!/usr/bin/env python3
"""
P0: 上下文增强模块 (Context Enrichment)
在 Tier 1 文章发布前，自动搜索关键实体的背景信息并附加到正文。

使用方法:
    python3 scripts/context_enrichment.py <article_path>
    
或者作为模块导入:
    from scripts.context_enrichment import enrich_article
    enriched_content = enrich_article(article_content, max_entities=3)
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
from typing import List, Dict, Optional

# ==========================================
# 配置
# ==========================================
MAX_ENTITIES_TO_SEARCH = 3  # 每篇文章最多搜索几个实体
SEARCH_TIMEOUT = 10  # 搜索超时 (秒)
MAX_CONTEXT_LENGTH = 300  # 每个实体的背景信息最大长度

# ==========================================
# 实体提取
# ==========================================

def extract_entities_from_article(article_content: str) -> List[str]:
    """
    从文章中提取关键实体（公司名、技术术语、人名等）
    返回去重后的实体列表
    """
    # 提取 frontmatter 后的正文
    parts = article_content.split('---', 2)
    if len(parts) >= 3:
        body = parts[2]
    else:
        body = article_content
    
    # 提取可能的实体模式
    entities = set()
    
    # 1. 提取大写缩写 (如 AI, GPU, TSMC, NVIDIA, SEC 等)
    acronyms = re.findall(r'\b[A-Z]{2,6}\b', body)
    entities.update(acronyms)
    
    # 2. 提取首字母大写的词组 (如 "Large Language Model", "Federal Reserve" 等)
    # 排除以动词/形容词开头的无意义短语
    title_phrases = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}\b', body)
    
    # 过滤掉常见的非实体开头词
    phrase_stop_prefixes = {
        'The', 'This', 'That', 'These', 'Those', 'What', 'When', 'Where',
        'Who', 'Why', 'How', 'With', 'From', 'Have', 'Has', 'Had',
        'More', 'Most', 'Some', 'Such', 'Than', 'They', 'Them', 'Their',
        'Also', 'Very', 'Just', 'Only', 'Even', 'Still', 'Already',
        'Reports', 'Report', 'Driven', 'Based', 'Made', 'Used', 'Used',
        'New', 'High', 'Low', 'Good', 'Bad', 'Great', 'Large', 'Small',
        'Record', 'Major', 'Key', 'First', 'Last', 'Next', 'Previous'
    }
    
    filtered_phrases = [
        p for p in title_phrases 
        if not any(p.startswith(prefix + ' ') for prefix in phrase_stop_prefixes)
        and not p.split()[0] in phrase_stop_prefixes
    ]
    entities.update(filtered_phrases)
    
    # 3. 提取带引号的术语
    quoted_terms = re.findall(r'["\"]([^"\"]{3,50})["\"]', body)
    entities.update(quoted_terms)
    
    # 过滤掉常见非实体词
    stop_words = {
        'The', 'This', 'That', 'These', 'Those', 'What', 'When', 'Where',
        'Who', 'Why', 'How', 'With', 'From', 'Have', 'Has', 'Had',
        'More', 'Most', 'Some', 'Such', 'Than', 'They', 'Them', 'Their',
        'About', 'After', 'Before', 'Between', 'During', 'Through',
        'Would', 'Could', 'Should', 'Will', 'Shall', 'Can', 'May',
        'Also', 'Very', 'Just', 'Only', 'Even', 'Still', 'Already',
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday',
        'January', 'February', 'March', 'April', 'June', 'July', 'August', 'September', 'October', 'November', 'December',
        'AI', 'IT', 'US', 'UK', 'EU', 'UN', 'TV', 'PC', 'App', 'Web',
        'I', 'A', 'An'
    }
    
    filtered_entities = [
        e for e in entities 
        if e not in stop_words 
        and len(e) > 2 
        and not e.isdigit()
    ]
    
    return filtered_entities[:MAX_ENTITIES_TO_SEARCH * 2]  # 返回多一些供筛选


# ==========================================
# 背景搜索
# ==========================================

def search_entity_background(entity: str) -> Optional[str]:
    """
    搜索实体的背景信息
    返回简短的背景描述
    """
    try:
        # 使用 Wikipedia API 获取摘要
        search_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(entity.replace(' ', '_'))}"
        req = urllib.request.Request(
            search_url,
            headers={'User-Agent': 'GoodInfo/1.0 (News Context Enrichment)'}
        )
        
        with urllib.request.urlopen(req, timeout=SEARCH_TIMEOUT) as resp:
            data = json.loads(resp.read())
            
            if 'extract' in data and data['extract']:
                extract = data['extract'][:MAX_CONTEXT_LENGTH]
                if len(data['extract']) > MAX_CONTEXT_LENGTH:
                    extract += '...'
                return extract
            return None
            
    except Exception as e:
        # 搜索失败时静默返回
        return None


def search_entity_background_cn(entity: str) -> Optional[str]:
    """
    搜索中文实体的背景信息
    """
    try:
        # 尝试中文 Wikipedia
        search_url = f"https://zh.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(entity.replace(' ', '_'))}"
        req = urllib.request.Request(
            search_url,
            headers={'User-Agent': 'GoodInfo/1.0 (News Context Enrichment)'}
        )
        
        with urllib.request.urlopen(req, timeout=SEARCH_TIMEOUT) as resp:
            data = json.loads(resp.read())
            
            if 'extract' in data and data['extract']:
                extract = data['extract'][:MAX_CONTEXT_LENGTH]
                if len(data['extract']) > MAX_CONTEXT_LENGTH:
                    extract += '...'
                return extract
            return None
            
    except Exception as e:
        return None


# ==========================================
# 文章增强
# ==========================================

def generate_context_section(entities_with_context: Dict[str, str], language: str = 'en') -> str:
    """
    生成背景信息区块
    """
    if not entities_with_context:
        return ""
    
    if language == 'zh':
        section = "\n\n---\n\n## 📚 背景知识\n\n"
        for entity, context in entities_with_context.items():
            section += f"**{entity}**: {context}\n\n"
    else:
        section = "\n\n---\n\n## 📚 Background\n\n"
        for entity, context in entities_with_context.items():
            section += f"**{entity}**: {context}\n\n"
    
    return section


def enrich_article(article_content: str, max_entities: int = MAX_ENTITIES_TO_SEARCH) -> str:
    """
    增强文章：提取实体 → 搜索背景 → 附加到正文
    
    Args:
        article_content: 原始文章内容
        max_entities: 最多搜索几个实体
        
    Returns:
        增强后的文章内容
    """
    # 提取实体
    entities = extract_entities_from_article(article_content)
    
    if not entities:
        return article_content
    
    # 搜索背景信息
    entities_with_context = {}
    has_cjk = bool(re.search(r'[\u4e00-\u9fff]', article_content))
    
    for entity in entities[:max_entities]:
        if has_cjk:
            # 尝试中文搜索
            context = search_entity_background_cn(entity)
            if not context:
                context = search_entity_background(entity)
        else:
            context = search_entity_background(entity)
        
        if context:
            entities_with_context[entity] = context
    
    if not entities_with_context:
        return article_content
    
    # 检测文章格式
    parts = article_content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[0] + '---' + parts[1] + '---'
        body = parts[2]
        
        # 检测是否有英文部分（格式 A）
        if '\n---\n' in body:
            # 格式 A：中英双语单文件
            cn_en_split = body.split('\n---\n', 1)
            cn_body = cn_en_split[0]
            en_body = cn_en_split[1] if len(cn_en_split) > 1 else ""
            
            # 在中文部分后添加中文背景
            cn_context = generate_context_section(entities_with_context, 'zh')
            cn_body += cn_context
            
            # 在英文部分后添加英文背景
            en_context = generate_context_section(entities_with_context, 'en')
            en_body += en_context
            
            return frontmatter + cn_body + '\n---\n' + en_body
        else:
            # 格式 B/C：单语言
            # 判断是中文还是英文
            if has_cjk:
                lang = 'zh'
            else:
                lang = 'en'
            
            context_section = generate_context_section(entities_with_context, lang)
            return frontmatter + body + context_section
    else:
        # 无 frontmatter 的简单格式
        lang = 'zh' if re.search(r'[\u4e00-\u9fff]', article_content) else 'en'
        context_section = generate_context_section(entities_with_context, lang)
        return article_content + context_section


# ==========================================
# 命令行入口
# ==========================================

def main():
    if len(sys.argv) < 2:
        print("用法: python3 context_enrichment.py <article_path>")
        print("  或: python3 context_enrichment.py --stdin  # 从标准输入读取")
        sys.exit(1)
    
    if sys.argv[1] == '--stdin':
        content = sys.stdin.read()
        enriched = enrich_article(content)
        print(enriched)
    else:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print(f"错误：文件不存在 - {filepath}")
            sys.exit(1)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        enriched = enrich_article(content)
        
        # 输出到标准输出
        print(enriched)
        
        # 如果指定了输出文件
        if len(sys.argv) >= 3:
            output_path = sys.argv[2]
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(enriched)
            print(f"\n✅ 已保存到: {output_path}")


if __name__ == '__main__':
    main()

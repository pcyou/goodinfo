#!/usr/bin/env python3
"""
P1: 跨平台去重模块 (Cross-Platform Deduplication)
在现有去重逻辑基础上增加 URL 归一化和跨平台故事合并。

功能:
1. URL 归一化：去除跟踪参数、统一格式
2. 跨平台故事合并：同一故事在不同平台的重复识别
3. 标题语义相似度匹配

使用方法:
    from scripts.cross_platform_dedup import normalize_url, is_duplicate_story
    
    # URL 归一化
    clean_url = normalize_url("https://example.com/article?utm_source=twitter&ref=xyz")
    
    # 故事去重
    if is_duplicate_story(new_title, new_url, existing_articles):
        print("跳过重复文章")
"""

import re
import os
import json
from typing import List, Dict, Set, Tuple, Optional
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# ==========================================
# URL 归一化
# ==========================================

# 常见的跟踪参数（应被移除）
TRACKING_PARAMS = {
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'ref', 'referrer', 'fbclid', 'gclid', 'yclid',
    'source', 'share', 'shared', 'from',
    'trk', 'mc_cid', 'mc_eid',
    '_ga', '_gl',
}

# URL 规范化规则
URL_NORMALIZATION_RULES = [
    # 移除末尾斜杠
    (r'/$', ''),
    # 统一 http/https
    # (由 urlparse 处理)
    # 移除 www 前缀
    (r'^www\.', ''),
]


def normalize_url(url: str) -> str:
    """
    归一化 URL：去除跟踪参数、统一格式
    
    Args:
        url: 原始 URL
        
    Returns:
        归一化后的 URL
    """
    if not url:
        return url
    
    try:
        parsed = urlparse(url)
        
        # 规范化主机名（小写，移除 www）
        hostname = parsed.hostname.lower() if parsed.hostname else ''
        hostname = re.sub(r'^www\.', '', hostname)
        
        # 规范化路径
        path = parsed.path.rstrip('/')
        
        # 过滤查询参数（移除跟踪参数）
        if parsed.query:
            params = parse_qs(parsed.query)
            clean_params = {
                k: v for k, v in params.items()
                if k.lower() not in TRACKING_PARAMS
            }
            query = urlencode(clean_params, doseq=True) if clean_params else ''
        else:
            query = ''
        
        # 重新构建 URL
        normalized = urlunparse((
            parsed.scheme.lower(),
            hostname,
            path,
            parsed.params,
            query,
            ''  # 移除 fragment
        ))
        
        return normalized
        
    except Exception:
        # 如果解析失败，返回原始 URL 的基本清理版本
        return url.strip().rstrip('/')


def extract_story_id(url: str) -> Optional[str]:
    """
    从 URL 中提取故事 ID（用于识别同一文章的不同 URL）
    
    例如:
    - https://example.com/article/12345 -> 12345
    - https://example.com/posts/abc-def-ghi -> abc-def-ghi
    """
    try:
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # 提取最后一段路径
        segments = path.split('/')
        if segments:
            last_segment = segments[-1]
            
            # 如果是数字 ID
            if last_segment.isdigit():
                return last_segment
            
            # 如果是 slug (字母数字和连字符)
            if re.match(r'^[a-z0-9-]+$', last_segment.lower()):
                return last_segment.lower()
        
        return None
        
    except Exception:
        return None


# ==========================================
# 标题相似度匹配
# ==========================================

def clean_title_for_comparison(title: str) -> str:
    """
    清理标题用于比较：去除标点、转小写、移除停用词
    """
    # 转小写
    title = title.lower()
    
    # 移除标点
    title = re.sub(r'[^\w\s]', '', title)
    
    # 移除常见停用词
    stop_words = {
        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'in', 'on', 'at',
        'to', 'for', 'of', 'and', 'or', 'but', 'with', 'by', 'as',
        'this', 'that', 'these', 'those', 'it', 'its',
        'from', 'up', 'about', 'into', 'through', 'during',
        'before', 'after', 'above', 'below', 'between',
        'new', 'just', 'now', 'today', 'says', 'said'
    }
    
    words = title.split()
    filtered = [w for w in words if w not in stop_words and len(w) > 2]
    
    return ' '.join(filtered)


def calculate_title_similarity(title1: str, title2: str) -> float:
    """
    计算两个标题的相似度 (0.0 - 1.0)
    
    使用改进的 Jaccard 相似度 + 词序匹配
    """
    clean1 = clean_title_for_comparison(title1)
    clean2 = clean_title_for_comparison(title2)
    
    if not clean1 or not clean2:
        return 0.0
    
    # 词集相似度 (Jaccard)
    words1 = set(clean1.split())
    words2 = set(clean2.split())
    
    intersection = words1 & words2
    union = words1 | words2
    
    if not union:
        return 0.0
    
    jaccard = len(intersection) / len(union)
    
    # 词序相似度 (考虑位置)
    words1_list = clean1.split()
    words2_list = clean2.split()
    
    common_in_order = 0
    i = j = 0
    while i < len(words1_list) and j < len(words2_list):
        if words1_list[i] == words2_list[j]:
            common_in_order += 1
            i += 1
            j += 1
        elif words1_list[i] in words2_list[j:]:
            j += 1
        else:
            i += 1
    
    order_similarity = common_in_order / max(len(words1_list), len(words2_list))
    
    # 综合相似度 (Jaccard 60% + 词序 40%)
    return 0.6 * jaccard + 0.4 * order_similarity


# ==========================================
# 跨平台故事去重
# ==========================================

# 存储已有文章的信息
_existing_articles_cache = None


def load_existing_articles(goodinfo_dir: str = '/root/goodinfo-site') -> List[Dict]:
    """
    加载已有文章的信息（标题、URL、slug）
    """
    global _existing_articles_cache
    
    if _existing_articles_cache is not None:
        return _existing_articles_cache
    
    articles = []
    
    # 扫描 content/posts 和 content.en/posts
    for base in ['content/posts', 'content.en/posts']:
        base_path = os.path.join(goodinfo_dir, base)
        if not os.path.exists(base_path):
            continue
        
        for root, dirs, files in os.walk(base_path):
            for fname in files:
                if not fname.endswith('.md') or 'daily-briefing' in fname:
                    continue
                
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 提取 frontmatter
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        fm_text = parts[1]
                        
                        # 提取标题
                        title_match = re.search(r"title:\s*['\"]?([^'\"]+)['\"]?", fm_text)
                        title = title_match.group(1) if title_match else fname.replace('.md', '')
                        
                        # 提取源 URL (如果有)
                        url_match = re.search(r"source_url:\s*['\"]?([^'\"]+)['\"]?", fm_text)
                        url = url_match.group(1) if url_match else ''
                        
                        articles.append({
                            'slug': fname.replace('.md', '').lower(),
                            'title': title,
                            'url': url,
                            'path': fpath
                        })
                        
                except Exception:
                    continue
    
    _existing_articles_cache = articles
    return articles


def is_duplicate_story(
    new_title: str,
    new_url: str,
    existing_articles: Optional[List[Dict]] = None,
    similarity_threshold: float = 0.70,
    goodinfo_dir: str = '/root/goodinfo-site'
) -> Tuple[bool, Optional[Dict]]:
    """
    检查新文章是否与已有文章重复
    
    Args:
        new_title: 新文章标题
        new_url: 新文章 URL
        existing_articles: 已有文章列表（如果为 None 则自动加载）
        similarity_threshold: 相似度阈值
        goodinfo_dir: GoodInfo 目录路径
        
    Returns:
        (is_duplicate, matched_article)
    """
    if existing_articles is None:
        existing_articles = load_existing_articles(goodinfo_dir)
    
    # 1. URL 归一化匹配
    if new_url:
        normalized_new = normalize_url(new_url)
        new_story_id = extract_story_id(normalized_new)
        
        for article in existing_articles:
            if article['url']:
                normalized_existing = normalize_url(article['url'])
                
                # 完全匹配
                if normalized_new == normalized_existing:
                    return True, article
                
                # 故事 ID 匹配
                existing_story_id = extract_story_id(normalized_existing)
                if new_story_id and existing_story_id and new_story_id == existing_story_id:
                    return True, article
    
    # 2. 标题相似度匹配
    for article in existing_articles:
        similarity = calculate_title_similarity(new_title, article['title'])
        if similarity >= similarity_threshold:
            return True, article
    
    return False, None


def find_related_stories(
    new_title: str,
    existing_articles: Optional[List[Dict]] = None,
    min_similarity: float = 0.50,
    goodinfo_dir: str = '/root/goodinfo-site'
) -> List[Tuple[float, Dict]]:
    """
    查找与新文章相关的已有故事（用于补充背景）
    
    Returns:
        [(similarity, article), ...] 按相似度降序排列
    """
    if existing_articles is None:
        existing_articles = load_existing_articles(goodinfo_dir)
    
    related = []
    for article in existing_articles:
        similarity = calculate_title_similarity(new_title, article['title'])
        if similarity >= min_similarity:
            related.append((similarity, article))
    
    # 按相似度降序
    related.sort(key=lambda x: x[0], reverse=True)
    return related[:5]  # 返回最相关的 5 个


# ==========================================
# 批量去重
# ==========================================

def dedup_article_candidates(
    candidates: List[Dict],
    existing_articles: Optional[List[Dict]] = None,
    goodinfo_dir: str = '/root/goodinfo-site'
) -> Tuple[List[Dict], List[Dict]]:
    """
    对候选文章列表进行去重
    
    Args:
        candidates: 候选文章列表，每项包含 {'title', 'url', 'source', ...}
        existing_articles: 已有文章列表
        goodinfo_dir: GoodInfo 目录路径
        
    Returns:
        (unique_articles, duplicates)
    """
    unique = []
    duplicates = []
    
    for candidate in candidates:
        is_dup, matched = is_duplicate_story(
            candidate.get('title', ''),
            candidate.get('url', ''),
            existing_articles,
            goodinfo_dir=goodinfo_dir
        )
        
        if is_dup:
            duplicates.append({**candidate, 'matched': matched})
        else:
            unique.append(candidate)
    
    return unique, duplicates


# ==========================================
# 命令行入口
# ==========================================

def main():
    import sys
    
    print("P1: 跨平台去重模块")
    print("=" * 50)
    
    # 加载已有文章
    articles = load_existing_articles()
    print(f"已加载 {len(articles)} 篇已有文章")
    
    # 测试 URL 归一化
    test_urls = [
        "https://example.com/article?utm_source=twitter&ref=xyz",
        "https://www.example.com/article/",
        "HTTPS://Example.Com/Article/12345?foo=bar&utm_campaign=test",
    ]
    
    print("\nURL 归一化测试:")
    for url in test_urls:
        normalized = normalize_url(url)
        print(f"  原始: {url}")
        print(f"  归一化: {normalized}")
        print()
    
    # 测试标题相似度
    test_titles = [
        ("NVIDIA Reports Record Q3 Revenue", "Nvidia Announces Record Third Quarter Revenue"),
        ("Apple Launches New iPhone", "Google Releases Pixel Phone"),
        ("Federal Reserve Raises Interest Rates", "Fed Hikes Rates by 25 Basis Points"),
    ]
    
    print("标题相似度测试:")
    for t1, t2 in test_titles:
        sim = calculate_title_similarity(t1, t2)
        print(f"  '{t1}'")
        print(f"  vs '{t2}'")
        print(f"  相似度: {sim:.2f}")
        print()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
P2: 中国热点采集模块 (China Hotspot Collector)
从国内平台 RSS 源采集热点，发布到 goodinfo.net/categories/china-hotspot/

数据源:
- 知乎日报
- 36 氪
- 少数派
- 澎湃新闻
- 界面新闻

使用方法:
    python3 scripts/china_hotspot_collector.py [--hours 12] [--max-articles 10]
"""

import os
import sys
import re
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta, timedelta
from email.utils import parsedate_to_datetime
from typing import List, Dict, Optional

# ==========================================
# 配置
# ==========================================

GOODINFO_DIR = '/root/goodinfo-site'
OUTPUT_DIR = os.path.join(GOODINFO_DIR, 'content/posts/china-hotspot')
HOURS_WINDOW = 12  # 默认时间窗口 (小时)
MAX_ARTICLES = 10  # 每次最多发布文章数

# 国内 RSS 源列表
# 注意：国内 RSS 源可能需要 -L 跟随重定向
CHINA_RSS_SOURCES = [
    {
        'name': '钛媒体',
        'url': 'https://www.tmtpost.com/rss',
        'priority': 5,
        'follow_redirect': True,
    },
    {
        'name': '36 氪',
        'url': 'https://36kr.com/feed',
        'priority': 4,
        'follow_redirect': True,
    },
    {
        'name': '少数派',
        'url': 'https://sspai.com/feed',
        'priority': 3,
        'follow_redirect': True,
    },
    {
        'name': '澎湃新闻',
        'url': 'https://www.thepaper.cn/rss_hotNews',
        'priority': 4,
        'follow_redirect': True,
    },
    {
        'name': '品玩',
        'url': 'https://www.pingwest.com/feed',
        'priority': 3,
        'follow_redirect': True,
    },
]

# 过滤类别 (不发布的文章类型)
FILTER_CATEGORIES = {
    '广告', '推广', '赞助', '广告', '营销',
    'ad', 'promotion', 'sponsored', 'marketing'
}


# ==========================================
# RSS 采集
# ==========================================

def fetch_rss(source: Dict, timeout: int = 15) -> Optional[str]:
    """
    获取 RSS 内容
    """
    try:
        req = urllib.request.Request(
            source['url'],
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) GoodInfo/1.0',
                'Accept': 'application/rss+xml, application/xml, text/xml',
            }
        )
        
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
            
    except Exception as e:
        print(f"  ⚠️ 获取 {source['name']} RSS 失败: {e}")
        return None


def parse_rss_articles(rss_content: str, source_name: str) -> List[Dict]:
    """
    解析 RSS 内容为文章列表
    """
    articles = []
    
    try:
        # 处理 BOM
        if rss_content.startswith('\ufeff'):
            rss_content = rss_content[1:]
        
        # 移除 CDATA
        rss_content = re.sub(r'<!\[CDATA\[', '', rss_content)
        rss_content = re.sub(r'\]\]>', '', rss_content)
        
        root = ET.fromstring(rss_content)
        
        for item in root.iter('item'):
            title_elem = item.find('title')
            link_elem = item.find('link')
            desc_elem = item.find('description')
            pubdate_elem = item.find('pubDate')
            
            if title_elem is None or link_elem is None:
                continue
            
            title = (title_elem.text or '').strip()
            link = (link_elem.text or '').strip()
            desc = (desc_elem.text or '').strip() if desc_elem is not None else ''
            
            # 清理 HTML 标签
            desc = re.sub(r'<[^>]+>', '', desc).strip()
            
            # 解析发布时间
            pub_dt = None
            if pubdate_elem is not None and pubdate_elem.text:
                try:
                    pub_dt = parsedate_to_datetime(pubdate_elem.text)
                except:
                    pass
            
            articles.append({
                'title': title,
                'url': link,
                'description': desc[:200],
                'source': source_name,
                'pub_timestamp': pub_dt.timestamp() if pub_dt else 0,
                'pub_datetime': pub_dt,
            })
            
    except ET.ParseError as e:
        print(f"  ⚠️ 解析 {source_name} RSS 失败: XML 解析错误")
    except Exception as e:
        print(f"  ⚠️ 解析 {source_name} RSS 失败: {e}")
    
    return articles


# ==========================================
# 去重
# ==========================================

def get_existing_slugs() -> set:
    """获取已有文章的 slug 集合"""
    existing_slugs = set()
    
    for root, dirs, files in os.walk(OUTPUT_DIR):
        for fname in files:
            if fname.endswith('.md'):
                existing_slugs.add(fname.replace('.md', '').lower())
    
    return existing_slugs


def generate_slug(title: str, source: str) -> str:
    """生成文章 slug"""
    # 清理标题
    slug = title.lower()
    slug = re.sub(r'[^\w\s\u4e00-\u9fff-]', '', slug)  # 保留中文、字母、数字、连字符
    slug = re.sub(r'\s+', '-', slug)
    slug = slug[:80]  # 限制长度
    
    # 添加日期后缀
    date_str = datetime.now(timezone.utc).strftime('%Y%m%d')
    return f"{slug}-{date_str}"


def is_filtered(title: str) -> bool:
    """检查文章是否应被过滤"""
    title_lower = title.lower()
    return any(kw in title_lower for kw in FILTER_CATEGORIES)


# ==========================================
# 文章生成
# ==========================================

def generate_article_content(article: Dict) -> tuple:
    """
    生成 Hugo Markdown 文章内容 (格式 C: 中文-only)
    
    Returns:
        (content, slug)
    """
    now_beijing = datetime.now(timezone.utc) + timedelta(hours=8)
    date_str = now_beijing.strftime('%Y-%m-%dT%H:%M:%S+08:00')
    slug = generate_slug(article['title'], article['source'])
    
    # 提取关键词作为 tags
    tags = [article['source']]
    if 'AI' in article['title'] or 'AI' in article['description']:
        tags.append('AI')
    if '科技' in article['title'] or 'tech' in article['title'].lower():
        tags.append('科技')
    
    tags_yaml = '[' + ', '.join(f'"{t}"' for t in tags) + ']'
    
    # 生成内容
    content = f"""---
title: '{article['title']}'
date: {date_str}
categories: [china-hotspot]
tags: {tags_yaml}
source_url: '{article['url']}'
---

## {article['title']}

{article['description']}

> 来源：[{article['source']}]({article['url']})

---

> 📰 本文自动采集自 {article['source']}，仅供资讯参考。
"""
    
    return content, slug


# ==========================================
# 主流程
# ==========================================

def collect_china_hotspot(hours: int = HOURS_WINDOW, max_articles: int = MAX_ARTICLES) -> Dict:
    """
    采集中国热点文章并发布
    
    Args:
        hours: 时间窗口 (小时)
        max_articles: 最多发布文章数
        
    Returns:
        采集结果统计
    """
    print(f"🇨🇳 开始采集中国热点 (时间窗口: {hours}h, 最多: {max_articles} 篇)")
    print("=" * 60)
    
    # 计算截止时间
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=hours)).timestamp()
    
    # 获取已有 slug
    existing_slugs = get_existing_slugs()
    
    # 采集所有 RSS 源
    all_articles = []
    for source in CHINA_RSS_SOURCES:
        print(f"\n📡 采集: {source['name']}")
        rss_content = fetch_rss(source)
        
        if rss_content:
            articles = parse_rss_articles(rss_content, source['name'])
            print(f"  ✅ 获取到 {len(articles)} 篇文章")
            all_articles.extend(articles)
        else:
            print(f"  ❌ 获取失败")
    
    print(f"\n📊 共获取到 {len(all_articles)} 篇原始文章")
    
    # 按时间过滤
    recent_articles = [a for a in all_articles if a['pub_timestamp'] >= cutoff]
    print(f"📅 时间窗口内: {len(recent_articles)} 篇")
    
    # 按优先级排序
    source_priority = {s['name']: s['priority'] for s in CHINA_RSS_SOURCES}
    recent_articles.sort(key=lambda x: (-source_priority.get(x['source'], 0), -x['pub_timestamp']))
    
    # 去重 + 过滤 + 发布
    published = 0
    skipped_dup = 0
    skipped_filter = 0
    published_articles = []
    
    for article in recent_articles:
        # 过滤
        if is_filtered(article['title']):
            skipped_filter += 1
            continue
        
        # 生成 slug
        slug = generate_slug(article['title'], article['source'])
        
        # 去重
        if slug in existing_slugs:
            skipped_dup += 1
            continue
        
        # 生成文章
        content, slug = generate_article_content(article)
        
        # 写入文件
        output_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        published_articles.append({'title': article['title'], 'slug': slug, 'source': article['source']})
        published += 1
        existing_slugs.add(slug)
        
        if published >= max_articles:
            break
    
    # 统计结果
    result = {
        'fetched': len(all_articles),
        'recent': len(recent_articles),
        'published': published,
        'skipped_dup': skipped_dup,
        'skipped_filter': skipped_filter,
        'articles': published_articles,
    }
    
    print(f"\n{'=' * 60}")
    print(f"📊 采集结果:")
    print(f"  获取: {result['fetched']} 篇")
    print(f"  时间窗口内: {result['recent']} 篇")
    print(f"  已发布: {result['published']} 篇")
    print(f"  跳过 (重复): {result['skipped_dup']} 篇")
    print(f"  跳过 (过滤): {result['skipped_filter']} 篇")
    
    if published_articles:
        print(f"\n📰 已发布文章:")
        for a in published_articles:
            print(f"  - [{a['source']}] {a['title'][:50]}...")
    
    return result


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='中国热点采集模块')
    parser.add_argument('--hours', type=int, default=HOURS_WINDOW, help='时间窗口 (小时)')
    parser.add_argument('--max-articles', type=int, default=MAX_ARTICLES, help='最多发布文章数')
    
    args = parser.parse_args()
    
    result = collect_china_hotspot(hours=args.hours, max_articles=args.max_articles)
    
    # 输出 JSON 结果供 cron 使用
    print(f"\n📄 JSON 结果:")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

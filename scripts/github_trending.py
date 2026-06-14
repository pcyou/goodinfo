#!/usr/bin/env python3
"""
GitHub Trending 爬虫脚本
抓取 GitHub 每日/每周热门项目，生成 Hugo 文章

使用方法:
    python3 scripts/github_trending.py [daily|weekly]
    
输出:
    content/posts/github-trending-YYYY-MM-DD.md
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
from datetime import datetime, timedelta, timezone

# ==========================================
# 配置
# ==========================================
CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'content', 'posts')
GITHUB_API = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GoodInfo-GitHub-Trending"
}

# 添加 GitHub Token (可选，提高速率限制)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


def fetch_trending_repos(since="daily", language="", per_page=20):
    """
    获取 GitHub 热门仓库
    
    Args:
        since: daily/weekly/monthly
        language: 编程语言过滤 (如 python, javascript)
        per_page: 返回数量
    
    Returns:
        list: 仓库列表
    """
    # 计算时间范围
    now = datetime.now(timezone.utc)
    if since == "daily":
        date_from = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    elif since == "weekly":
        date_from = (now - timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        date_from = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    
    # 构建搜索查询 (放宽条件: stars:>10 以确保有结果)
    query = f"created:>{date_from} stars:>10"
    if language:
        query += f" language:{language}"
    
    # API 请求
    url = f"{GITHUB_API}/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }
    
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(full_url, headers=HEADERS)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
            return data.get("items", [])
    except Exception as e:
        print(f"Error fetching GitHub API: {e}")
        return []


def fetch_trending_from_page(since="daily"):
    """
    从 GitHub Trending 页面抓取 (备用方案)
    
    Args:
        since: daily/weekly/monthly
    
    Returns:
        list: 仓库列表
    """
    url = f"https://github.com/trending?since={since}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml"
    })
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode()
        
        # 解析每个 article 块
        repos = []
        articles = re.findall(r'<article[^>]*class="Box-row"[^>]*>(.*?)</article>', html, re.DOTALL)
        
        for art in articles[:25]:
            # 仓库路径
            h2_match = re.search(r'<h2[^>]*>.*?<a[^>]*href="(/[^"]+)"', art, re.DOTALL)
            if not h2_match:
                continue
            repo_path = h2_match.group(1).strip()
            # 必须是 /owner/repo 格式 (恰好2个斜杠)
            if repo_path.count('/') != 2:
                continue
            
            full_name = repo_path.lstrip('/')
            
            # 描述
            desc = ""
            desc_match = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', art, re.DOTALL)
            if desc_match:
                desc = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip()
            
            # 语言
            lang = "Unknown"
            lang_match = re.search(r'<span[^>]*itemprop="programmingLanguage"[^>]*>(.*?)</span>', art)
            if lang_match:
                lang = lang_match.group(1).strip()
            
            # 总 Star 数
            stars = 0
            star_match = re.search(r'<a[^>]*href="[^"]*/stargazers"[^>]*>.*?([\d,]+)\s*</a>', art, re.DOTALL)
            if star_match:
                stars = int(star_match.group(1).replace(',', ''))
            
            # 今日/本周新增 Star
            today_stars = 0
            today_match = re.search(r'([\d,]+)\s*stars?\s*(?:today|this week)', art)
            if today_match:
                today_stars = int(today_match.group(1).replace(',', ''))
            
            repos.append({
                "full_name": full_name,
                "html_url": f"https://github.com{repo_path}",
                "description": desc,
                "stargazers_count": stars,
                "language": lang,
                "topics": [],
                "trending_stars": today_stars
            })
        
        return repos
    except Exception as e:
        print(f"Error fetching trending page: {e}")
        return []


def format_repo_item(repo, index):
    """
    格式化单个仓库为 Markdown
    
    Args:
        repo: 仓库数据
        index: 序号
    
    Returns:
        str: Markdown 格式
    """
    name = repo.get("full_name", "Unknown")
    url = repo.get("html_url", "#")
    desc = repo.get("description", "") or "暂无描述"
    stars = repo.get("stargazers_count", 0)
    lang = repo.get("language", "") or "Unknown"
    topics = repo.get("topics", [])
    
    # 构建标签
    tags_str = ""
    if topics:
        tags_str = " ".join([f"`{t}`" for t in topics[:5]])
    
    trending = repo.get("trending_stars", 0)
    trending_line = f"- 🔥 **Trending**: +{trending:,} stars\n" if trending else ""
    
    return f"""### {index}. [{name}]({url})

{desc}

- ⭐ **Stars**: {stars:,}
{trending_line}- 💻 **Language**: {lang}
- 🏷️ **Topics**: {tags_str or "无"}

"""


def generate_article(repos, since="daily"):
    """
    生成 Hugo 文章
    
    Args:
        repos: 仓库列表
        since: daily/weekly
    
    Returns:
        str: Markdown 文章内容
    """
    now = datetime.utcnow() + timedelta(hours=8)  # 北京时间 UTC+8
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    period = "每日" if since == "daily" else "每周"
    title = f"🔥 GitHub {period}热门项目 ({date_str})"
    
    # 构建内容
    content = f"""---
title: "{title}"
date: {time_str}
tags: ["GitHub", "开源", "热门项目", "Trending"]
categories: ["github"]
---

# 🔥 GitHub {period}热门项目

> 更新时间：{now.strftime("%Y年%m月%d日 %H:%M")} (北京时间)
> 数据来源：GitHub Trending & Search API

---

以下是过去{period}内最受欢迎的开源项目，按新增 Star 数排序。

"""
    
    # 添加仓库列表
    for i, repo in enumerate(repos[:15], 1):
        content += format_repo_item(repo, i)
    
    # 添加尾部
    content += f"""
---

## 📊 统计

- **收录项目数**: {len(repos)}
- **时间范围**: {period}
- **排序依据**: 新增 Star 数

---

*本文由 GoodInfo GitHub Trending 自动生成，每小时更新。*
"""
    
    return title, content


def save_article(title, content):
    """
    保存文章到 Hugo content 目录
    
    Args:
        title: 文章标题
        content: Markdown 内容
    
    Returns:
        str: 保存的文件路径
    """
    os.makedirs(CONTENT_DIR, exist_ok=True)
    
    now = datetime.now()
    filename = f"github-trending-{now.strftime('%Y-%m-%d-%H')}.md"
    filepath = os.path.join(CONTENT_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    """主函数"""
    # 解析参数
    since = "daily"
    if len(sys.argv) > 1:
        since = sys.argv[1] if sys.argv[1] in ["daily", "weekly", "monthly"] else "daily"
    
    print(f"🚀 开始抓取 GitHub Trending ({since})...")
    
    # 方案1: 使用 API
    print("📡 尝试 GitHub Search API...")
    repos = fetch_trending_repos(since=since, per_page=20)
    
    # 方案2: 如果 API 失败，使用页面抓取
    if not repos:
        print("⚠️ API 失败，尝试页面抓取...")
        repos = fetch_trending_from_page(since=since)
    
    if not repos:
        print("❌ 无法获取数据")
        sys.exit(1)
    
    print(f"✅ 获取到 {len(repos)} 个项目")
    
    # 生成文章
    print("📝 生成文章...")
    title, content = generate_article(repos, since)
    
    # 保存
    filepath = save_article(title, content)
    print(f"✅ 文章已保存: {filepath}")
    
    # 输出摘要
    print("\n📊 前5个项目:")
    for i, repo in enumerate(repos[:5], 1):
        name = repo.get("full_name", "Unknown")
        stars = repo.get("stargazers_count", 0)
        print(f"  {i}. {name} ⭐ {stars:,}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

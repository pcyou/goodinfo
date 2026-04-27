#!/usr/bin/env python3
"""
xiaohu.ai 开源项目采集脚本
采集 https://www.xiaohu.ai/c/a066c4/ 的所有文章，转为 Hugo Markdown 格式
"""

import json
import re
import os
import sys
import time
import hashlib
import urllib.request
import urllib.parse

SPACE_ID = "1677027"
SITE_URL = "https://www.xiaohu.ai"
POSTS_API = f"{SITE_URL}/internal_api/spaces/{SPACE_ID}/posts"
POST_DETAILS_API = f"{SITE_URL}/internal_api/post_details"

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}


def fetch_json(url):
    """Fetch JSON from URL with retries."""
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            if attempt < 2:
                time.sleep(2)
            else:
                print(f"  Failed to fetch {url}: {e}", file=sys.stderr)
                return None


def tip_to_text(node):
    """Convert Tiptap JSON to plain text."""
    if not node:
        return ""
    texts = []

    def extract(n):
        if isinstance(n, dict):
            if n.get("type") == "text":
                texts.append(n.get("text", ""))
            elif n.get("type") == "hardBreak":
                texts.append("\n")
            elif n.get("type") == "paragraph":
                texts.append("\n\n")
                for c in n.get("content", []):
                    extract(c)
                texts.append("\n")
            elif n.get("type") == "heading":
                level = n.get("attrs", {}).get("level", 2)
                texts.append("\n\n")
                for c in n.get("content", []):
                    extract(c)
                texts.append("\n\n")
            elif n.get("type") == "bulletList":
                texts.append("\n")
                for c in n.get("content", []):
                    texts.append("- ")
                    extract(c)
                    texts.append("\n")
            elif n.get("type") == "orderedList":
                for i, c in enumerate(n.get("content", []), 1):
                    texts.append(f"{i}. ")
                    extract(c)
                    texts.append("\n")
            elif n.get("type") == "listItem":
                for c in n.get("content", []):
                    extract(c)
            elif n.get("type") == "blockquote":
                texts.append("\n> ")
                for c in n.get("content", []):
                    extract(c)
                texts.append("\n")
            elif n.get("type") == "codeBlock":
                lang = n.get("attrs", {}).get("language", "")
                texts.append(f"\n\n```{lang}\n")
                for c in n.get("content", []):
                    extract(c)
                texts.append("\n```\n\n")
            elif n.get("type") == "image":
                src = n.get("attrs", {}).get("src", "")
                texts.append(f"\n![image]({src})\n")
            elif n.get("type") == "horizontalRule":
                texts.append("\n\n---\n\n")
            else:
                for c in n.get("content", []):
                    extract(c)
        elif isinstance(n, list):
            for item in n:
                extract(item)

    extract(node)
    return "".join(texts).strip()


def sanitize_filename(title):
    """Create a safe filename from title."""
    name = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", title)
    name = name.replace(" ", "-")
    name = re.sub(r"-+", "-", name)
    return name[:100]


def make_slug(title):
    """Create a URL-friendly slug."""
    slug = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", title)
    slug = slug.lower()
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug[:80]


def clean_yaml_value(val):
    """Remove quotes from YAML values."""
    return val.replace('"', '').replace("'", '').replace('\n', ' ').strip()


def fetch_all_posts():
    """Fetch all posts from the space."""
    all_posts = []
    page = 1
    while True:
        url = f"{POSTS_API}?page={page}&per_page=20&include_top_pinned_post=true&used_on=cards"
        print(f"  Fetching page {page}...")
        data = fetch_json(url)
        if not data:
            break

        records = data.get("records", [])
        if not records:
            break

        for post in records:
            post_id = post.get("id")
            title = post.get("name", "")
            published = post.get("published_at", "")
            slug = post.get("slug", "")
            post_url = f"{SITE_URL}/p/{slug}/{post_id}"

            # Extract body content
            body = ""
            tiptap_body = post.get("tiptap_body", {})
            if tiptap_body and "body" in tiptap_body:
                body = tip_to_text(tiptap_body["body"])

            # Extract topics
            topics = []
            for topic in post.get("topics", []):
                if isinstance(topic, dict):
                    topics.append(topic.get("name", ""))
                elif isinstance(topic, str):
                    topics.append(topic)

            all_posts.append({
                "id": post_id,
                "title": title,
                "slug": slug,
                "url": post_url,
                "published_at": published,
                "body": body,
                "topics": topics,
            })

        if not data.get("has_next_page", False):
            break
        page += 1
        time.sleep(0.5)

    return all_posts


def generate_hugo_md(post, output_dir):
    """Generate Hugo markdown file for a post."""
    title = post["title"]
    slug = make_slug(title)
    pub_date = post["published_at"][:10] if post["published_at"] else "2026-01-01"
    post_url = post["url"]
    body = post["body"]

    # Topics to tags
    tags = post.get("topics", [])
    tags_str = ", ".join(f'"{t}"' for t in tags if t) if tags else ""

    # Summary: first 150 chars of body
    summary = body[:150].replace("\n", " ").replace('"', '').replace("'", '').strip() if body else ""

    content = f"""---
title: "{clean_yaml_value(title)}"
date: {pub_date}T08:00:00+08:00
tags: [{tags_str}]
categories: ["opensource"]
summary: "{clean_yaml_value(summary)}"
source_url: "{post_url}"
xiahuid: "{post['id']}"
---

## 📰 正文

{body}

---

*来源：[{title}]({post_url})*
"""

    filepath = os.path.join(output_dir, f"{slug}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    output_dir = "/root/goodinfo-site/content/posts/opensource"
    os.makedirs(output_dir, exist_ok=True)

    # Load existing posts for dedup
    existing_ids = set()
    for fname in os.listdir(output_dir):
        if fname.endswith(".md"):
            fpath = os.path.join(output_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            m = re.search(r'xiahuid:\s*"(\d+)"', content)
            if m:
                existing_ids.add(m.group(1))

    print(f"Existing posts: {len(existing_ids)}")
    print("Fetching posts from xiaohu.ai...")

    posts = fetch_all_posts()
    print(f"Total posts found: {len(posts)}")

    new_count = 0
    for post in posts:
        pid = str(post["id"])
        if pid in existing_ids:
            continue
        new_count += 1
        filepath = generate_hugo_md(post, output_dir)
        print(f"  + {post['title'][:60]}")
        existing_ids.add(pid)

    print(f"\nDone! New posts: {new_count}, Total: {len(posts)}")
    return new_count


if __name__ == "__main__":
    count = main()
    sys.exit(0)

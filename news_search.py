#!/usr/bin/env python3
import subprocess
import re

def search_ddg(query):
    """Search DuckDuckGo HTML and extract results"""
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    result = subprocess.run(
        ['curl', '-s', url, '-H', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'],
        capture_output=True, text=True, timeout=30
    )
    html = result.stdout
    results = re.findall(r'<a[^>]+class="result__"[^>]*href="([^"]+)"[^>]*>(.+?)</a>', html)
    items = []
    for link, title in results[:10]:
        title = re.sub(r'<[^>]+>', '', title)
        # Extract uddg URL
        m = re.search(r'uddg=([^&]+)', link)
        real_url = m.group(1) if m else link
        items.append({'title': title, 'url': real_url})
    return items

def search_google_news(query):
    """Search Google News RSS"""
    url = f"https://news.google.com/rss?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    result = subprocess.run(
        ['curl', '-s', url],
        capture_output=True, text=True, timeout=30
    )
    html = result.stdout
    titles = re.findall(r'<title>([^<]+)</title>', html)[1:11]  # skip channel title
    dates = re.findall(r'<pubDate>([^<]+)</pubDate>', html)[:10]
    return list(zip(titles, dates))

# Search Google News for specific topics
queries = [
    ("AI news", "AI+technology+news"),
    ("Stock market", "stock+market+news"),
    ("World news", "world+news+breaking"),
    ("Science news", "science+news+discovery"),
]

for label, ddg_q in queries:
    print(f"\n{'='*60}")
    print(f"=== {label} (DuckDuckGo) ===")
    items = search_ddg(ddg_q)
    for i, item in enumerate(items):
        print(f"  {i+1}. {item['title']}")
        print(f"     {item['url']}")

print(f"\n{'='*60}")
print("=== RECENT HEADLINES (Google News general) ===")
# Get general top stories
result = subprocess.run(
    ['curl', '-s', 'https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en'],
    capture_output=True, text=True, timeout=30
)
html = result.stdout
titles = re.findall(r'<title>([^<]+)</title>', html)[1:21]
dates = re.findall(r'<pubDate>([^<]+)</pubDate>', html)[:20]
for t, d in zip(titles, dates):
    print(f"  [{d}] {t}")

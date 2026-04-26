#!/usr/bin/env python3
import subprocess
import re
import json

def fetch(url):
    r = subprocess.run(['curl', '-s', '-L', url, '-H', 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'], capture_output=True, text=True, timeout=30)
    return r.stdout

def extract_text(html, min_len=30, max_items=20):
    paras = re.findall(r'<p[^>]*>(.+?)</p>', html)
    results = []
    for p in paras:
        clean = re.sub(r'<[^>]+>', '', p).strip()
        if clean and len(clean) > min_len:
            results.append(clean)
            if len(results) >= max_items:
                break
    return results

# 1. BBC main page for latest
print("=== BBC NEWS HEADLINES ===")
html = fetch("https://www.bbc.com/news")
headings = re.findall(r'<h[23][^>]*>(.+?)</h[23]>', html)
for h in headings[:20]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean and len(clean) > 15:
        print(f"  - {clean}")

# 2. Try to find the WH dinner shooting article
print("\n=== BBC SEARCH: Washington shooting ===")
html = fetch("https://www.bbc.com/search?q=Washington+shooting+press+dinner")
headings = re.findall(r'<h[23][^>]*>(.+?)</h[23]>', html)
for h in headings[:10]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean and len(clean) > 15:
        print(f"  - {clean}")

# Get article text
paras = re.findall(r'<p[^>]*>(.+?)</p>', html)
print("\nArticle excerpts:")
for p in paras[:15]:
    clean = re.sub(r'<[^>]+>', '', p).strip()
    if clean and len(clean) > 30:
        print(f"  {clean}")

# 3. Reuters articles  
print("\n=== REUTERS ===")
html = fetch("https://www.reuters.com/")
json_data = re.findall(r'"headline"\s*:\s*"([^"]+)"', html)
for j in json_data[:10]:
    print(f"  - {j}")

# 4. BBC Science 
print("\n=== BBC SCIENCE ===")
html = fetch("https://www.bbc.com/news/science_and_environment")
headings = re.findall(r'<h[23][^>]*>(.+?)</h[23]>', html)
for h in headings[:10]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean and len(clean) > 15:
        print(f"  - {clean}")

# 5. BBC Chernobyl
print("\n=== BBC CHERNOBYL ===")
html = fetch("https://www.bbc.com/news/topics/c407n03905vt")
headings = re.findall(r'<h[23][^>]*>(.+?)</h[23]>', html)
for h in headings[:10]:
    clean = re.sub(r'<[^>]+>', '', h).strip()
    if clean and len(clean) > 15:
        print(f"  - {clean}")

paras = re.findall(r'<p[^>]*>(.+?)</p>', html)
for p in paras[:10]:
    clean = re.sub(r'<[^>]+>', '', p).strip()
    if clean and len(clean) > 30:
        print(f"  {clean}")

# 6. Find actual BBC article URLs
print("\n=== BBC ARTICLE LINKS ===")
html = fetch("https://www.bbc.com/news")
links = re.findall(r'<a[^>]+href="(/news/articles/[^"]+)"[^>]*>(.+?)</a>', html)
seen = set()
for href, text in links:
    text = re.sub(r'<[^>]+>', '', text).strip()
    if text and len(text) > 20 and text not in seen:
        seen.add(text)
        print(f"  {text} → https://www.bbc.com{href}")
        if len(seen) >= 15:
            break

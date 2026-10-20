#!/usr/bin/env python3
"""Targeted Google News RSS search for topic detail."""
import sys, re, html, urllib.parse, subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

QUERIES = sys.argv[1:]
for q in QUERIES:
    url = ("https://news.google.com/rss/search?q=" + urllib.parse.quote(q)
           + "&hl=en-US&gl=US&ceid=US:en")
    try:
        out = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", "Mozilla/5.0", url],
                             capture_output=True, timeout=40).stdout
    except Exception as e:
        print(f"!! {q}: {e}")
        continue
    print(f"\n{'#'*70}\n### QUERY: {q}")
    try:
        root = ET.fromstring(out)
    except Exception as e:
        print(f"  !! parse fail: {e}")
        continue
    n = 0
    for it in root.iter("item"):
        t = it.find("title")
        d = it.find("description")
        p = it.find("pubDate")
        title = strip_tags(t.text if t is not None else "")
        desc = strip_tags(d.text if d is not None else "")[:300]
        pd = p.text if p is not None else ""
        src = it.find("source")
        sname = src.text if src is not None and src.text else ""
        n += 1
        if n > 8:
            break
        print(f"\n - {title}\n   [{sname} | {pd}]\n   {desc}")
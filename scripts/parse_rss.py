#!/usr/bin/env python3
"""Parse RSS feeds, filter to last N hours, print candidates."""
import sys, glob, re, html
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

HOURS = int(sys.argv[1]) if len(sys.argv) > 1 else 4
CUTOFF = datetime.now(timezone.utc) - timedelta(hours=HOURS)

FEEDS = [
    ("GoogleNews-Top", "/tmp/news_top.xml"),
    ("GoogleNews-World", "/tmp/gw2.xml"),
    ("GoogleNews-Business", "/tmp/gb.xml"),
    ("GoogleNews-Technology", "/tmp/gt2.xml"),
    ("TheVerge", "/tmp/vg.xml"),
    ("TechCrunch", "/tmp/tc2.xml"),
    ("CNBC", "/tmp/cnbc.xml"),
    ("WSJ-World", "/tmp/wsj.xml"),
    ("Cointelegraph", "/tmp/ct2.xml"),
    ("TheBlock", "/tmp/crypto2.xml"),
]

def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()

def parse_date(txt):
    if not txt:
        return None
    txt = txt.strip()
    try:
        d = parsedate_to_datetime(txt)
        if d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return d.astimezone(timezone.utc)
    except Exception:
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ"):
        try:
            d = datetime.strptime(txt, fmt)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
            return d.astimezone(timezone.utc)
        except Exception:
            continue
    return None

seen = set()
rows = []
for name, path in FEEDS:
    try:
        data = open(path, "rb").read()
    except Exception:
        continue
    if not data.strip():
        continue
    try:
        root = ET.fromstring(data)
    except Exception as e:
        print(f"!! parse fail {name}: {e}", file=sys.stderr)
        continue
    items = root.iter("item")
    for it in items:
        def g(tag):
            el = it.find(tag)
            return (el.text or "").strip() if el is not None and el.text else ""
        title = strip_tags(g("title"))
        desc = strip_tags(g("description"))
        link = g("link")
        date = parse_date(g("pubDate")) or parse_date(g("{http://purl.org/dc/elements/1.1/}date"))
        src = name
        srcel = it.find("source")
        if srcel is not None and srcel.text:
            src = f"{name}/{srcel.text.strip()}"
        if not date or date < CUTOFF:
            continue
        key = re.sub(r"[^a-z0-9 ]", "", title.lower())[:80]
        if key in seen:
            continue
        seen.add(key)
        rows.append((date, src, title, desc[:280], link))

rows.sort(reverse=True)
print(f"### {len(rows)} items in last {HOURS}h (cutoff {CUTOFF.strftime('%Y-%m-%d %H:%M UTC')})")
for d, src, t, desc, link in rows:
    age = (datetime.now(timezone.utc) - d).total_seconds() / 3600
    print(f"\n[{d.strftime('%H:%M')}Z | {age:.1f}h] {src}\n  T: {t}\n  D: {desc}\n  L: {link[:150]}")
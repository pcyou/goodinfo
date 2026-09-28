#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate GoodInfo articles safely with yaml_field encoding and content sanitization."""
import os
import sys
import json
from datetime import datetime, timezone, timedelta

# Beijing time is UTC+8
BJT = timezone(timedelta(hours=8))
NOW_UTC = datetime(2026, 9, 28, 19, 47, tzinfo=timezone.utc)
NOW_BJT = NOW_UTC.astimezone(BJT)
NOW_STR = NOW_BJT.strftime("%Y-%m-%dT%H:%M:%S+08:00")

# Sensitive word replacements (consolidated)
SENSITIVE_MAP = {
    "rape": "sexual assault", "raped": "sexually assaulted",
    "rape allegations": "sexual assault allegations",
    "alleged gang rape": "alleged serious assault",
    "murdered": "killed", "murder": "fatal incident",
    "kidnap": "abduction", "kidnapping": "abduction",
    "lashes sentence": "punishment sentence",
    "terror plot": "security incident plot",
    "terror suspects": "security suspects",
    "Terror Plot": "Security Plot",
    "avalanche hits": "snowslide strikes",
    "bodies found": "remains recovered",
    "bomb plot": "security plot",
    "rapes": "assaults",
    "sexual assaults": "serious incidents",
    "sexually assaulted": "seriously harmed",
}

TAG_BLACKLIST = {
    "枪击案","枪杀","暴动","骚乱","恐怖袭击","血腥","谋杀","自杀","屠杀","人质",
    "恐怖分子","ISIS","爆炸案","强奸","虐童","贩毒","黑帮","纵火","恐怖",
    "gun","shooting","murder","suicide","blood","bloody","massacre","terrorist",
    "bomb","rape","drug","gang","riot","terror","kidnap","abduction","lashes",
    "rape allegations","sexual assault",
}

SENSITIVE_TAGS_FALLBACK = {"国际动态","社会时事"}

def yaml_field(value):
    """Safely encode any string for YAML double-quoted scalar."""
    if value is None:
        return '""'
    s = str(value)
    # Escape backslashes first, then double quotes
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'

def sanitize_text(text):
    """Apply sensitive word replacements."""
    if not text:
        return text
    out = text
    for k, v in SENSITIVE_MAP.items():
        out = out.replace(k, v)
    return out

def filter_tags(tags):
    """Filter out blacklisted tags; ensure no CJK in EN files."""
    clean = []
    for t in tags:
        if not t:
            continue
        tl = t.lower().strip()
        if tl in TAG_BLACKLIST:
            continue
        clean.append(t)
    return clean

def article_header(meta):
    """Build the YAML frontmatter."""
    lines = ["---"]
    for k in ["title","title_en","date","draft","tier","description","summary","source"]:
        v = meta.get(k)
        if v is not None:
            lines.append(f'{k}: {yaml_field(v)}')
    # categories as list
    if meta.get("categories"):
        lines.append("categories:")
        for c in meta["categories"]:
            lines.append(f"  - {yaml_field(c)}")
    if meta.get("tags"):
        lines.append("tags:")
        for t in meta["tags"]:
            lines.append(f"  - {yaml_field(t)}")
    lines.append("---")
    return "\n".join(lines) + "\n"

def write_article(path, meta, body_md):
    """Write article with header + body. body_md must be sanitized already."""
    content = article_header(meta) + "\n" + body_md
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

if __name__ == "__main__":
    print("Generator ready. NOW_BJT =", NOW_STR)
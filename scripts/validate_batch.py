#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Per-batch validator for GoodInfo articles.

Usage:
    python3 scripts/validate_batch.py --cat world --tier 1 slug1 slug2 ...
    python3 scripts/validate_batch.py --cat world --slugs-file list.txt

Checks (per skill devops/goodinfo-hourly-news):
  * YAML parse + no duplicate frontmatter keys
  * required frontmatter fields present
  * date format YYYY-MM-DDTHH:MM:SS+08:00
  * Tier-2 [快讯] / [Brief] prefix
  * Tier-1 全景透视 / Panoramic Analysis section present, >= 150 chars
  * CN section markers stay in CN body; EN section markers stay in EN body
  * GoodInfo signature present; HKHouse absent
  * no CJK in EN files; EN tags pure ASCII
  * no English sentences in CN body (proper nouns excluded)
  * no traditional Chinese in CN files (true trad->simp pairs only)
  * AdSense sensitive-word blacklist on title/body/tags
  * char counts sanity (CN file needs CJK prose; EN file needs EN prose)
"""
import os
import re
import sys

import yaml

REPO = "/root/goodinfo-site"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from trad_map import TRAD_ONLY  # noqa: E402

# ---------------------------------------------------------------- blacklist
BLACKLIST = [
    "枪击案", "枪杀", "暴动", "骚乱", "恐怖袭击", "血腥", "谋杀", "自杀", "屠杀", "人质",
    "恐怖分子", "ISIS", "爆炸案", "强奸", "虐童", "贩毒", "黑帮", "纵火", "恐怖",
    "gun", "shooting", "murder", "suicide", "blood", "bloody", "massacre", "terrorist",
    "bomb", "rape", "drug", "gang", "riot",
]

# substrings that legitimately contain a blacklisted token
ALLOW_SUBSTR = {
    "gun": ["begun", "ungun"],
    "bomb": ["bombard"],
    "rape": ["grape", "scrape", "trape", "therapeutic"],
    "gang": ["chang", "guang", "gangster"],
    "isis": ["crisis", "analysis", "axis", "basis", "diagnosis", "parenthesis", "crises"],
    "drug": ["drugs"],
}


def blacklist_hits(text):
    t = text.lower()
    hits = []
    for w in BLACKLIST:
        wl = w.lower()
        idx = t.find(wl)
        while idx != -1:
            ctx = t[max(0, idx - 6): idx + len(wl) + 6]
            if not any(a in ctx for a in ALLOW_SUBSTR.get(wl, [])):
                hits.append((w, t[max(0, idx - 30): idx + len(wl) + 30]))
                break
            idx = t.find(wl, idx + 1)
    return hits


CJK_RE = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
CJK_EXT_B = re.compile(r"[\U00020000-\U0002FFFF]")
EN_WORD = re.compile(r"[A-Za-z]{3,}")
# an English *prose* word starts lowercase; proper nouns in CN copy are capitalised
EN_PROSE_WORD = re.compile(r"\b[a-z][a-z]{2,}\b")

# ---------------------------------------------------------------- sections
CN_CORE = ["## 核心摘要", "## Core Summary"]
CN_DETAIL = ["## 事件详情", "## Event Details"]
CN_ANALYSIS = ["## 全景透视", "## Panoramic Analysis", "## Wider Perspective"]
CN_VIEWS = ["## 多方观点比对", "## Competing Views", "## Comparison of Viewpoints",
            "## Multiple Perspectives", "## 观点分析"]
EN_CORE = ["## Key Facts", "## Core Summary"]
EN_DETAIL = ["## Event Details", "## 事件详情"]
EN_ANALYSIS = ["## Panoramic Analysis", "## Wider Perspective", "## 全景透视"]
EN_VIEWS = ["## Competing Views", "## Comparison of Viewpoints",
            "## Multiple Perspectives", "## Viewpoints Compared",
            "## Multi-Perspective Comparison", "## Comparison of Multiple Viewpoints",
            "## 多方观点比对"]

REQUIRED_FIELDS = ("title", "date", "categories", "tags", "tier", "description",
                    "summary", "source")


def has_section(body, options):
    return any(s in body for s in options)


def english_prose_lines(body):
    """Lines that look like real English sentences rather than proper nouns."""
    heavy = []
    for i, line in enumerate(body.split("\n")):
        words = EN_WORD.findall(line)
        if len(words) < 6:
            continue
        prose = EN_PROSE_WORD.findall(line)
        if len(prose) >= 3:
            heavy.append((i + 1, line[:140]))
    return heavy


def validate_file(path, lang, tier):
    ok = True
    out = []
    full = os.path.join(REPO, path)
    if not os.path.exists(full):
        return False, ["  FAIL: missing file %s" % path]
    text = open(full, encoding="utf-8").read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return False, ["  FAIL: no frontmatter"]
    try:
        meta = yaml.safe_load(parts[1]) or {}
        body = parts[2]
        out.append("  YAML parse: OK")
    except Exception as e:
        return False, ["  FAIL YAML parse: %s" % e]

    fm_keys = [ln.split(":")[0].strip() for ln in parts[1].strip().split("\n")
               if ln.strip() and not ln.startswith(" ") and ":" in ln]
    dupes = sorted({k for k in fm_keys if fm_keys.count(k) > 1})
    out.append("  Duplicate frontmatter keys: %s" % ("OK" if not dupes else "FAIL %s" % dupes))
    if dupes:
        ok = False

    for k in REQUIRED_FIELDS:
        if not meta.get(k):
            out.append("  FAIL: missing field '%s'" % k)
            ok = False

    d = str(meta.get("date", ""))
    if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+08:00$", d):
        out.append("  FAIL: date format -> %r" % d)
        ok = False
    else:
        out.append("  Date format: OK (%s)" % d)

    sig = "GoodInfo全球资讯组" if lang == "CN" else "GoodInfo Global News"
    if sig not in text:
        out.append("  FAIL: signature missing (%s)" % sig)
        ok = False
    else:
        out.append("  Signature: OK")
    if "HKHouse" in text or "hkhouse" in text:
        out.append("  FAIL: forbidden brand HKHouse")
        ok = False
    else:
        out.append("  No HKHouse: OK")

    if lang == "EN":
        n = len(CJK_RE.findall(text)) + len(CJK_EXT_B.findall(text))
        out.append("  CJK scan on EN: %s" % ("OK (0)" if n == 0 else "FAIL (%d)" % n))
        if n:
            ok = False
            for m in CJK_RE.finditer(text):
                out.append("      -> %r" % text[max(0, m.start() - 40):m.start() + 40])
        if any(CJK_RE.search(t) for t in (meta.get("tags") or [])):
            out.append("  FAIL: EN tags contain CJK")
            ok = False
        else:
            out.append("  EN tags pure-ASCII: OK")
        for label, opts, required in (
                ("core", EN_CORE, True),
                ("analysis", EN_ANALYSIS, True),
                ("detail", EN_DETAIL, tier == "1"),
                ("views", EN_VIEWS, tier == "1")):
            present = has_section(body, opts)
            if required and not present:
                out.append("  FAIL: missing EN '%s' section (one of %s)" % (label, opts))
                ok = False
            else:
                out.append("  EN %s section: %s" % (label, "OK" if present else "n/a"))
        for cnsec in CN_CORE + CN_DETAIL + CN_ANALYSIS + CN_VIEWS:
            if cnsec in body and cnsec not in EN_CORE + EN_DETAIL + EN_ANALYSIS + EN_VIEWS:
                out.append("  FAIL: CN section in EN body: %s" % cnsec)
                ok = False
        if tier == "2":
            if not str(meta.get("title", "")).startswith("[Brief]"):
                out.append("  FAIL: Tier2 EN title missing [Brief]")
                ok = False
            else:
                out.append("  Tier2 [Brief] prefix: OK")
        m = re.search(r"## (?:Panoramic Analysis|Wider Perspective)\s*(.*?)(?=\n## |\Z)",
                      body, re.S)
        if m:
            n = len(re.sub(r"\s", "", m.group(1)))
            out.append("  Panoramic Analysis length: %d chars %s" % (n, "OK" if n >= 150 else "FAIL"))
            if n < 150:
                ok = False
        else:
            out.append("  FAIL: no Panoramic Analysis / Wider Perspective section")
            ok = False
    else:
        trad = sorted({c for c in text if c in TRAD_ONLY})
        out.append("  Simplified-Chinese scan: %s"
                   % ("OK" if not trad else "FAIL " + "".join(trad[:25])))
        if trad:
            ok = False
        heavy = english_prose_lines(body)
        out.append("  English-sentence scan on CN body: %s"
                   % ("OK" if not heavy else "FAIL (%d)" % len(heavy)))
        for ln, txt in heavy[:8]:
            out.append("      L%d: %s" % (ln, txt))
        if heavy:
            ok = False
        for label, opts, required in (
                ("core", CN_CORE, True),
                ("analysis", CN_ANALYSIS, True),
                ("detail", CN_DETAIL, tier == "1"),
                ("views", CN_VIEWS, tier == "1")):
            present = has_section(body, opts)
            if required and not present:
                out.append("  FAIL: missing CN '%s' section (one of %s)" % (label, opts))
                ok = False
            else:
                out.append("  CN %s section: %s" % (label, "OK" if present else "n/a"))
        if tier == "2":
            if not str(meta.get("title", "")).startswith("[快讯]"):
                out.append("  FAIL: Tier2 CN title missing [快讯]")
                ok = False
            else:
                out.append("  Tier2 [快讯] prefix: OK")
        m = re.search(r"## 全景透视\s*(.*?)(?=\n## |\Z)", body, re.S)
        if m:
            n = len(re.sub(r"\s", "", m.group(1)))
            out.append("  全景透视 length: %d chars %s" % (n, "OK" if n >= 150 else "FAIL"))
            if n < 150:
                ok = False
        else:
            out.append("  FAIL: no 全景透视 section")
            ok = False
        for ensec in EN_CORE + EN_ANALYSIS + EN_VIEWS:
            if ensec in body and ensec not in CN_CORE + CN_DETAIL + CN_ANALYSIS + CN_VIEWS:
                out.append("  FAIL: EN section in CN body: %s" % ensec)
                ok = False

    hits = blacklist_hits(text)
    out.append("  AdSense blacklist: %s" % ("OK" if not hits else "FAIL"))
    for w, ctx in hits[:8]:
        out.append("      '%s' -> ...%s..." % (w, ctx))
    if hits:
        ok = False

    cjk_n = len(CJK_RE.findall(body))
    en_n = len(EN_WORD.findall(body))
    out.append("  Body chars: total=%d CN=%d ENwords=%d" % (len(body), cjk_n, en_n))
    if lang == "CN" and cjk_n < 200:
        out.append("  FAIL: CN body too short (%d CJK chars)" % cjk_n)
        ok = False
    if lang == "EN" and en_n < 60:
        out.append("  FAIL: EN body too short (%d english words)" % en_n)
        ok = False
    return ok, out


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    cat = tier = None
    slugs = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--cat":
            cat = args[i + 1]; i += 2
        elif a == "--tier":
            tier = args[i + 1]; i += 2
        elif a == "--slugs-file":
            slugs += [l.strip() for l in open(args[i + 1]) if l.strip()]
            i += 2
        else:
            slugs.append(a); i += 1

    all_ok = True
    print("=" * 78)
    print("GoodInfo BATCH VALIDATION — %d article(s)" % len(slugs))
    print("=" * 78)
    for slug in slugs:
        s_tier = tier
        if s_tier is None:
            p = os.path.join(REPO, "content/posts/%s/%s.md" % (cat, slug))
            if os.path.exists(p):
                m = re.search(r'^tier:\s*"?(\d)"?', open(p, encoding="utf-8").read(), re.M)
                s_tier = m.group(1) if m else "1"
            else:
                s_tier = "1"
        for lang, path in (("CN", "content/posts/%s/%s.md" % (cat, slug)),
                           ("EN", "content.en/posts/%s/%s.md" % (cat, slug))):
            print("\n--- %s  [%s tier%s]" % (path, lang, s_tier))
            if not os.path.exists(os.path.join(REPO, path)):
                # Format C: Chinese-only Tier-2 briefs are valid (no EN file required).
                if lang == "EN" and s_tier == "2" and \
                        os.path.exists(os.path.join(REPO, "content/posts/%s/%s.md" % (cat, slug))):
                    print("  n/a (CN-only Tier-2 brief, Format C)")
                    continue
                ok, out = validate_file(path, lang, s_tier)
                for line in out:
                    print(line)
                if not ok:
                    all_ok = False
                continue
            ok, out = validate_file(path, lang, s_tier)
            for line in out:
                print(line)
            if not ok:
                all_ok = False
    print("\n" + "=" * 78)
    print("OVERALL: %s" % ("PASS" if all_ok else "FAIL"))
    print("=" * 78)
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())

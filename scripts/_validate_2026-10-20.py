#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run validation on newly generated articles."""
import os
import re
import sys
import yaml

sys.path.insert(0, '/root/goodinfo-site')
from scripts.generate import sanitize_text

ARTICLES = [
    ("CN", "1", "/root/goodinfo-site/content/posts/finance/china-q3-gdp-ai-exports-boom-2026-10-20.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/finance/china-q3-gdp-ai-exports-boom-2026-10-20.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/finance/musk-spacex-share-every-kid-america-2026-10-20.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/finance/musk-spacex-share-every-kid-america-2026-10-20.md"),
    ("CN", "2", "/root/goodinfo-site/content/posts/world/egypt-saudi-yemen-conflict-military-involvement-2026-10-20.md"),
    ("EN", "2", "/root/goodinfo-site/content.en/posts/world/egypt-saudi-yemen-conflict-military-involvement-2026-10-20.md"),
    ("CN", "2", "/root/goodinfo-site/content/posts/crypto/mastercard-stablecoin-security-fraud-sanctions-2026-10-20.md"),
    ("EN", "2", "/root/goodinfo-site/content.en/posts/crypto/mastercard-stablecoin-security-fraud-sanctions-2026-10-20.md"),
]

FORBIDDEN_TAGS = {"枪击案","枪杀","暴动","骚乱","恐怖袭击","血腥","谋杀","自杀","屠杀","人质","恐怖分子","isis","爆炸案","强奸","虐童","贩毒","黑帮","纵火","恐怖","gun","shooting","murder","suicide","blood","bloody","massacre","terrorist","bomb","rape","drug","gang","riot","terror","kidnap","abduction","lashes"}
FORBIDDEN_CONTENT = ["rape allegations", "alleged gang rape", "raped", "kidnap victims", "lashes sentence", "Terror Plot", "terror plot", "terror suspects"]
CN_CHAR_RE = re.compile(r'[一-鿿]')
CJK_RE = re.compile(r'[㐀-鿿]')
TRAD_PAIRS = [("員","员"),("數","数"),("採","采"),("允許","允许"),("暫停","暂停"),("分鐘","分钟"),("個","个"),("們","们"),("這","这"),("來","会"),("為","为"),("從","从"),("時","时"),("會","会"),("說","说"),("對","对"),("長","长"),("學","学"),("術","术"),("觀","观"),("點","点"),("議","议"),("題","题"),("產","产"),("業","业"),("發","发"),("記","记"),("應","应"),("聲","声"),("體","体"),("關","关"),("開","开"),("選","选"),("戰","战"),("頭","头"),("顯","显"),("條","条"),("處","处"),("歷","历"),("畫","画"),("種","种"),("價","价"),("營","营"),("專","专"),("檢","检"),("標","标"),("權","权"),("熱","热"),("練","练"),("縣","县"),("櫃","柜"),("轉","转"),("黨","党"),("齡","龄"),("興","兴"),("辦","办"),("語","语"),("訊","讯"),("計","计"),("認","认"),("讓","让"),("測","测"),("兒","儿"),("鄉","乡"),("證","证"),("貝","贝"),("賓","宾"),("贏","赢"),("報","报"),("寫","写")]

def is_trad(line):
    for t, s in TRAD_PAIRS:
        if t in line:
            # Replace the trad char with simp, see if rest looks like the same context
            new_line = line.replace(t, s)
            # If replacing this one trad char with simp makes more sense, mark as trad
            return True
    return False

errors = 0
warnings = 0
for lang, tier, path in ARTICLES:
    print(f"\n{'='*70}")
    print(f"[{lang} tier-{tier}] {os.path.basename(path)}")
    if not os.path.exists(path):
        print(f"  ❌ MISSING")
        errors += 1
        continue
    with open(path, encoding="utf-8") as f:
        text = f.read()
    # YAML parse
    try:
        m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
        assert m, "no frontmatter"
        meta = yaml.safe_load(m.group(1))
        body = m.group(2)
        print(f"  ✓ YAML parsed. Title: {meta.get('title','')[:60]}")
    except Exception as e:
        print(f"  ❌ YAML parse error: {e}")
        errors += 1
        continue
    # Tier 2 prefix
    if tier == "2":
        title = meta.get("title", "")
        title_en = meta.get("title_en", "")
        if lang == "CN":
            if not title.startswith("[快讯]"):
                print(f"  ❌ CN title missing [快讯]: {title[:60]}")
                errors += 1
            if not title_en.startswith("[Brief]"):
                print(f"  ❌ EN title_en missing [Brief]: {title_en[:60]}")
                errors += 1
        else:
            if not title.startswith("[Brief]"):
                print(f"  ❌ EN title missing [Brief]: {title[:60]}")
                errors += 1
            if not title_en.startswith("[Brief]"):
                print(f"  ❌ EN title_en missing [Brief]: {title_en[:60]}")
                errors += 1
        if title.startswith("[快讯]") or title.startswith("[Brief]"):
            print(f"  ✓ Tier 2 prefix present")
    # Panoramic
    if tier == "1":
        if "全景透视" not in body:
            print(f"  ❌ Missing 全景透视 section")
            errors += 1
        else:
            print(f"  ✓ 全景透视 present")
    # Footer / signature
    if lang == "CN":
        if "编辑：GoodInfo全球资讯组" not in body:
            print(f"  ❌ Missing CN signature")
            errors += 1
        else:
            print(f"  ✓ CN signature present")
    else:
        if "Editor: GoodInfo Global News Team" not in body:
            print(f"  ❌ Missing EN signature")
            errors += 1
        else:
            print(f"  ✓ EN signature present")
    if "HKHouse" in text:
        print(f"  ❌ HKHouse in text!")
        errors += 1
    # CJK in EN
    if lang == "EN":
        cjk_lines = []
        for ln, line in enumerate(text.split("\n")):
            c = CJK_RE.findall(line)
            if c:
                cjk_lines.append((ln+1, line[:80], c[:5]))
        if cjk_lines:
            print(f"  ❌ CJK in EN: {len(cjk_lines)} lines")
            for ln, l, c in cjk_lines[:3]:
                print(f"     L{ln}: {c} | {l}")
            errors += 1
        else:
            print(f"  ✓ No CJK in EN")
    # English sentences in CN body
    if lang == "CN":
        eng_lines = []
        for ln, line in enumerate(body.split("\n")):
            if not line.strip() or len(line) < 30:
                continue
            if CN_CHAR_RE.search(line):
                continue
            words = re.findall(r'[A-Za-z]+', line)
            if len(words) >= 5:
                eng_lines.append((ln+1, line[:120]))
        if eng_lines:
            print(f"  ❌ English sentences in CN: {len(eng_lines)}")
            for ln, l in eng_lines[:3]:
                print(f"     L{ln}: {l}")
            errors += 1
        else:
            print(f"  ✓ No English sentences in CN")
    # Traditional
    trad = []
    for ln, line in enumerate(text.split("\n")):
        if is_trad(line):
            trad.append((ln+1, line[:80]))
    if trad:
        print(f"  ❌ Traditional Chinese: {len(trad)} lines")
        for ln, l in trad[:3]:
            print(f"     L{ln}: {l}")
        errors += 1
    else:
        print(f"  ✓ Simplified only")
    # Sensitive tags
    tags = meta.get("tags", []) or []
    bad_tags = [t for t in tags if t.lower() in FORBIDDEN_TAGS]
    if bad_tags:
        print(f"  ❌ Sensitive tags: {bad_tags}")
        errors += 1
    else:
        print(f"  ✓ Tags clean ({len(tags)} tags)")
    # Sensitive content
    body_l = body.lower()
    bad_content = [t for t in FORBIDDEN_CONTENT if t.lower() in body_l]
    if bad_content:
        print(f"  ❌ Sensitive content: {bad_content}")
        errors += 1
    else:
        print(f"  ✓ Content clean")
    # Word count
    body_clean = re.sub(r'[#*`>|\-\[\]]', ' ', body)
    wc = len([w for w in re.split(r'\s+', body_clean) if w.strip()])
    print(f"  ℹ Word count (rough): {wc}")

print(f"\n{'='*70}")
print(f"ERRORS: {errors}  WARNINGS: {warnings}")
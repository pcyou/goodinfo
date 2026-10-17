#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate new GoodInfo articles."""
import yaml, sys, re, os

NEW_FILES = [
    ("content/posts/finance/wall-street-q3-2026-bank-earnings-beat-oct-2026.md", "CN", "t1"),
    ("content.en/posts/finance/wall-street-q3-2026-bank-earnings-beat-oct-2026.md", "EN", "t1"),
    ("content/posts/world/uk-mi5-state-threat-cold-war-levels-2026-10-14.md", "CN", "t1"),
    ("content.en/posts/world/uk-mi5-state-threat-cold-war-levels-2026-10-14.md", "EN", "t1"),
    ("content/posts/world/brief-argentina-falklands-maritime-tribunal-2026-10-14.md", "CN", "t2"),
    ("content/posts/world/brief-bulgaria-black-sea-merchant-ship-sunk-2026-10-14.md", "CN", "t2"),
    ("content/posts/world/brief-six-flags-rollercoaster-fatal-closure-2026-10-14.md", "CN", "t2"),
]

CJK_RE = re.compile(r'[㐀-鿿]')
# CJK extension B
CJK_RE2 = re.compile(r'[𠀀-𯿿]')

# Traditional Chinese chars (commonly used)
TRADITIONAL = {
    '員':'员','數':'数','據':'据','採':'采','集':'集','允':'允','許':'许','暫':'暂','停':'停',
    '分':'分','鐘':'钟','個':'个','會':'会','議':'议','時':'时','間':'间','從':'从','業':'业',
    '務':'务','對':'对','話':'话','證':'证','書':'书','檢':'检','驗':'验','發':'发','現':'现',
    '進':'进','過':'过','程':'程','點':'点','線':'线','機':'机','構':'构','應':'应','該':'该',
    '為':'为','麼':'么','麼':'么','長':'长','氣':'气','隻':'只','兒':'儿','車':'车','東':'东',
    '視':'视','覺':'觉','經':'经','營':'营','銷':'销','價':'价','銀':'银','門':'门','關':'关',
    '問':'问','題':'题','頭':'头','頁':'页','寫':'写','類':'类','條':'条','畫':'画','報':'报',
    '師':'师','導':'导','歷':'历','史':'史','醫':'医','療':'疗','藥':'药','術':'术','練':'练',
    '習':'习','蘭':'兰','萬':'万','萬':'万','創':'创','衛':'卫','歐':'欧','亞':'亚','國':'国',
    '際':'际','聯':'联','響':'响','顯':'显','觀':'观','眾':'众','預':'预','測':'测','準':'准',
    '確':'确','實':'实','質':'质','績':'绩','績':'绩','績':'绩','績':'绩','績':'绩','績':'绩',
}

# AdSense blacklist
BLACKLIST_WORDS = [
    '枪击案','枪杀','暴动','骚乱','恐怖袭击','血腥','谋杀','自杀','屠杀','人质',
    '恐怖分子','ISIS','爆炸案','强奸','虐童','贩毒','黑帮','纵火','恐怖',
    'gun','shooting','murder','suicide','blood','bloody','massacre','terrorist',
    'bomb','rape','drug','gang','riot','terror',
]
# Tier 2 required prefix
TIER2_PREFIX = "[快讯]"

print("=" * 70)
print("VALIDATION REPORT")
print("=" * 70)

all_pass = True

for path, lang, tier in NEW_FILES:
    print(f"\n--- {path} ({lang} {tier}) ---")
    if not os.path.exists(path):
        print("  FAIL: file missing")
        all_pass = False
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    # YAML parse
    try:
        parts = text.split('---', 2)
        meta = yaml.safe_load(parts[1])
        body = parts[2] if len(parts) > 2 else ''
    except Exception as e:
        print(f"  FAIL: YAML parse error: {e}")
        all_pass = False
        continue
    print(f"  YAML: OK title={meta.get('title','')[:40]}")

    # Required fields
    for k in ['title','date','categories','tags']:
        if not meta.get(k):
            print(f"  FAIL: missing field {k}")
            all_pass = False

    # CJK on EN
    if lang == 'EN':
        cjk_count = len(CJK_RE.findall(text))
        cjk_count2 = len(CJK_RE2.findall(text))
        if cjk_count or cjk_count2:
            print(f"  FAIL: CJK chars in EN: {cjk_count+cjk_count2}")
            all_pass = False
        else:
            print(f"  CJK scan: OK (0 chars)")

    # English scan on CN body (skip frontmatter title_en)
    if lang == 'CN':
        # Strip frontmatter
        body_only = body
        # Find lines with >= 5 English words (excluding lists, code)
        en_heavy = 0
        for line in body_only.split('\n'):
            # Skip pure proper nouns by allowing common english brand names
            words = re.findall(r'[a-zA-Z]{3,}', line)
            if len(words) >= 6:
                en_heavy += 1
                if en_heavy <= 3:
                    print(f"  EN-heavy body line: {line[:120]}")
        if en_heavy > 0:
            print(f"  WARN: {en_heavy} English-heavy body lines")
        else:
            print(f"  English scan: OK (no English-heavy lines in body)")

    # Traditional Chinese check
    trad_found = []
    for c in TRADITIONAL:
        if c in text:
            trad_found.append(c)
    if trad_found:
        print(f"  WARN: Traditional chars found: {trad_found[:5]}")
    else:
        print(f"  Simplified check: OK")

    # AdSense blacklist
    bl_found = []
    text_lower = text.lower()
    for w in BLACKLIST_WORDS:
        if w.lower() in text_lower:
            bl_found.append(w)
    if bl_found:
        print(f"  FAIL: AdSense blacklist: {bl_found}")
        all_pass = False
    else:
        print(f"  AdSense blacklist: OK")

    # Tier 2 prefix check
    if tier == 't2':
        title = meta.get('title','')
        if not title.startswith(TIER2_PREFIX):
            print(f"  FAIL: Tier 2 missing [快讯] prefix: {title[:40]}")
            all_pass = False
        else:
            print(f"  Tier 2 [快讯] prefix: OK")

    # 全景透视 section check (only for tier 1)
    if tier == 't1':
        if '全景透视' not in body and 'Panorama' not in body:
            print(f"  FAIL: missing 全景透视 / Panorama section")
            all_pass = False
        else:
            print(f"  全景透视 / Panorama section: OK")

    # Multiple perspectives check (only for tier 1)
    if tier == 't1':
        if '多方观点' not in body and 'Multiple Perspectives' not in body:
            print(f"  FAIL: missing 多方观点 / Multiple Perspectives section")
            all_pass = False
        else:
            print(f"  多方观点 / Multiple Perspectives section: OK")

    # 核心摘要 check
    if '核心摘要' not in body and 'Core Summary' not in body:
        print(f"  FAIL: missing 核心摘要 / Core Summary")
        all_pass = False
    else:
        print(f"  核心摘要 / Core Summary: OK")

    # Editor signature check
    if 'GoodInfo全球资讯组' not in text and 'GoodInfo Global News Desk' not in text:
        print(f"  FAIL: missing editor signature")
        all_pass = False
    else:
        print(f"  Editor signature: OK")

print("\n" + "=" * 70)
print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
print("=" * 70)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate GoodInfo articles for Oct 15 21:38 BJT update."""
import yaml, sys, re, os

NEW_FILES = [
    ("content/posts/world/pakistan-school-roof-collapse-casualties-2026-10-15.md", "CN", "t1"),
    ("content.en/posts/world/pakistan-school-roof-collapse-casualties-2026-10-15.md", "EN", "t1"),
    ("content/posts/crypto/eu-eba-designates-usdc-significant-emoney-token-2026-10-15.md", "CN", "t1"),
    ("content.en/posts/crypto/eu-eba-designates-usdc-significant-emoney-token-2026-10-15.md", "EN", "t1"),
    ("content/posts/finance/brief-us-september-ppi-largest-gain-four-years-2026-10-15.md", "CN", "t2"),
    ("content/posts/crypto/brief-q3-crypto-hacks-12-billion-supply-chain-2026-10-15.md", "CN", "t2"),
    ("content/posts/crypto/brief-ledger-atom-solana-mobile-tamper-protection-2026-10-15.md", "CN", "t2"),
]

CJK_RE = re.compile(r'[㐀-鿿]')
CJK_RE2 = re.compile(r'[𠀀-𯿿]')

TRADITIONAL = {
    '員':'员','數':'数','據':'据','採':'采','允':'允','許':'许','暫':'暂','鐘':'钟','個':'个',
    '會':'会','議':'议','時':'时','間':'间','從':'从','業':'业','務':'务','對':'对','話':'话',
    '證':'证','書':'书','檢':'检','驗':'验','發':'发','現':'现','進':'进','過':'过','程':'程',
    '點':'点','線':'线','機':'机','構':'构','應':'应','該':'该','為':'为','長':'长','氣':'气',
    '隻':'只','兒':'儿','車':'车','東':'东','視':'视','覺':'觉','經':'经','營':'营','銷':'销',
    '價':'价','銀':'银','門':'门','關':'关','問':'问','題':'题','頭':'头','頁':'页','寫':'写',
    '類':'类','條':'条','畫':'画','報':'报','師':'师','歷':'历','醫':'医','療':'疗','藥':'药',
    '術':'术','練':'练','習':'习','蘭':'兰','萬':'万','創':'创','衛':'卫','歐':'欧','亞':'亚',
    '國':'国','際':'际','聯':'联','響':'响','顯':'显','觀':'观','眾':'众','預':'预','測':'测',
    '準':'准','確':'确','實':'实','質':'质','績':'绩','學':'学','產':'产','報':'报','權':'权',
    '產':'产','幣':'币','關':'关','顏':'颜','飯':'饭','館':'馆','電':'电','腦':'脑','傳':'传',
}

BLACKLIST_WORDS = [
    '枪击案','枪杀','暴动','骚乱','恐怖袭击','血腥','谋杀','自杀','屠杀','人质',
    '恐怖分子','ISIS','爆炸案','强奸','虐童','贩毒','黑帮','纵火','恐怖',
    'gun','shooting','murder','suicide','blood','bloody','massacre','terrorist',
    'bomb','rape','drug','gang','riot','terror',
]
TIER2_PREFIX = "[快讯]"

print("=" * 70)
print("VALIDATION REPORT — Oct 15 21:38 BJT")
print("=" * 70)

all_pass = True
for path, lang, tier in NEW_FILES:
    print(f"\n--- {path} ({lang} {tier}) ---")
    if not os.path.exists(path):
        print(f"  FAIL: file missing")
        all_pass = False
        continue
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    try:
        parts = text.split('---', 2)
        meta = yaml.safe_load(parts[1])
        body = parts[2] if len(parts) > 2 else ''
    except Exception as e:
        print(f"  FAIL: YAML parse error: {e}")
        all_pass = False
        continue
    print(f"  YAML: OK title={meta.get('title','')[:50]}")

    for k in ['title','date','categories','tags']:
        if not meta.get(k):
            print(f"  FAIL: missing field {k}")
            all_pass = False

    if lang == 'EN':
        cjk_count = len(CJK_RE.findall(text))
        cjk_count2 = len(CJK_RE2.findall(text))
        if cjk_count or cjk_count2:
            print(f"  FAIL: CJK chars in EN: {cjk_count+cjk_count2}")
            all_pass = False
        else:
            print(f"  CJK scan: OK (0 chars)")

    if lang == 'CN':
        body_only = body
        en_heavy = 0
        for line in body_only.split('\n'):
            words = re.findall(r'[a-zA-Z]{3,}', line)
            if len(words) >= 6:
                en_heavy += 1
                if en_heavy <= 3:
                    print(f"  EN-heavy body line: {line[:120]}")
        if en_heavy > 0:
            print(f"  WARN: {en_heavy} English-heavy body lines")
        else:
            print(f"  English scan: OK (no English-heavy lines in body)")

    trad_found = []
    for c in TRADITIONAL:
        if c in text:
            trad_found.append(c)
    if trad_found:
        print(f"  WARN: Traditional chars found: {trad_found[:8]}")
    else:
        print(f"  Simplified check: OK")

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

    if tier == 't2':
        title = meta.get('title','')
        if not title.startswith(TIER2_PREFIX):
            print(f"  FAIL: Tier 2 missing [快讯] prefix: {title[:40]}")
            all_pass = False
        else:
            print(f"  Tier 2 [快讯] prefix: OK")

    if tier == 't1':
        if '全景透视' not in body and 'Panorama' not in body:
            print(f"  FAIL: missing 全景透视 / Panorama section")
            all_pass = False
        else:
            print(f"  全景透视 / Panorama section: OK")

    if tier == 't1':
        if '多方观点' not in body and 'Multiple Perspectives' not in body:
            print(f"  FAIL: missing 多方观点 / Multiple Perspectives section")
            all_pass = False
        else:
            print(f"  多方观点 / Multiple Perspectives section: OK")

    if '核心摘要' not in body and 'Core Summary' not in body:
        print(f"  FAIL: missing 核心摘要 / Core Summary")
        all_pass = False
    else:
        print(f"  核心摘要 / Core Summary: OK")

    if 'GoodInfo全球资讯组' not in text and 'GoodInfo Global News Desk' not in text:
        print(f"  FAIL: missing editor signature")
        all_pass = False
    else:
        print(f"  Editor signature: OK")

print("\n" + "=" * 70)
print(f"OVERALL: {'PASS' if all_pass else 'FAIL'}")
print("=" * 70)
sys.exit(0 if all_pass else 1)
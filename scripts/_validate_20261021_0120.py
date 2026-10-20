#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit the 2026-10-21 01:20 BJT GoodInfo batch."""
import os
import re
import sys

import yaml

CJK = re.compile(r'[㐀-鿿豈-﫿]')
CJK_B = re.compile(r'[\U00020000-\U0002FFFF]')
EN_WORD = re.compile(r'\b[A-Za-z]{2,}\b')
DATE_OK = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+08:00$')
CN_CHAR = re.compile(r'[一-鿿]')

BLACKLIST = [
    '枪击案', '枪杀', '暴动', '骚乱', '恐怖袭击', '血腥', '谋杀', '自杀',
    '屠杀', '人质', '恐怖分子', 'ISIS', '爆炸案', '强奸', '虐童', '贩毒',
    '黑帮', '纵火', '恐怖',
    'gun', 'shooting', 'murder', 'suicide', 'blood', 'bloody', 'massacre',
    'terrorist', 'bomb', 'rape', 'drug', 'gang', 'riot', 'terror',
]
_ASCII_PAT = {w: re.compile(r'(?<![a-z])' + w + r'(?![a-z])') for w in BLACKLIST if w.isascii()}
_CJK_PAT = {w: re.compile(re.escape(w)) for w in BLACKLIST if not w.isascii()}

TRAD = set('員數據採允許暫鐘個會議時間從業務對話證書檢驗發現過程點線機構應該為麼長氣隻兒車東視覺經營銷價銀門關問題頭頁寫類條畫報師導歷醫療藥術練習習蘭萬創衛歐亞國國際聯響顯觀眾預準確實質績勝隨擊貴慮濟動狀權標識週歲極簡約單雙親愛壓懷憶區營轉變豐')
SIMPLIFIED_ONLY = set('员数据采允许钟个会议时间从业务对话证书检验发现过程点线机构应该为么长气只儿车东视觉营销价银门关问题头页写类条画报师导历史医疗药术练习习兰万创卫欧亚国际联响显观众预测准确实质绩胜随击贵虑济动状权标识周岁极简约单双亲爱压怀忆区营转变丰')

ALLOWED_EN = {w.lower() for w in """
AI ETF GDP API IT CEO CFO CTO US UK EU UN NASA JAXA IBM PC EV IPO L2 L3 MMX H3
Phobos Mars DeepSeek BlackRock HSBC Elice GM Walmart Revolut Alberta Canada Britain
China Chinese Cu LME McKinsey IBIT iShares DHS Apple Tesla Microsoft Google OpenAI
Nasdaq S&P Reuters BBC CNN AP AFP The In On At It As For Not If But So We Its His
Her She He They This That These Those With From About After Before During While
When Where Which Whose What How Why Is Are Was Were Be Been Has Had Do Did Can
Could Will Would Should May Might Must More Most Less Least Such Both Each Any All
One Two New Old Good Bad Best Worst Right Left Up Down Out Over Under Again Still
Yet Now Then Here There Also Only Very Oct Sep Nov Dec Sun Mon Tue Wed Thu Fri Sat
Jan Feb Mar Apr Jun Jul Aug Q3 Al Jazeera FT WSJ Nikkei SCMP Braze Coinbase
Trump Salesforce Section Tariff Act Britain Yemen Houthi Houthis Typhoon
Royal Air Force Defence Ministry Defence Saudi Yemeni China ByteDance Alibaba
Tencent Nvidia Reuters Tom Hardware Barron Blackwell Crypto Finma Swiss Switzerland
Bitcoin ETF Retail Investors Spot General Motors Q3 Novo Nordisk CagriSema
Stablecoin Stablecoins Payments Settlement Transfer Volume Digital Assets Saudi
""".split()}

ROOT = "/root/goodinfo-site"
BATCH = [
    ("world", "uk-fighter-jets-saudi-defence-houthi-2026-10-21", "1"),
    ("ai-tech", "nvidia-china-tech-giants-35-billion-chip-orders-2026-10-21", "1"),
    ("finance", "us-importer-lawsuit-section-338-canada-tariffs-2026-10-21", "1"),
    ("ai-tech", "brief-salesforce-braze-acquisition-2026-10-21", "2"),
    ("finance", "brief-gm-q3-profit-buyback-2026-10-21", "2"),
    ("crypto", "brief-finma-swiss-retail-bitcoin-etf-2026-10-21", "2"),
    ("health", "brief-novo-cagrisema-weight-loss-women-2026-10-21", "2"),
    ("crypto", "brief-stablecoin-transfer-volume-off-hours-2026-10-21", "2"),
]


def audit(name, text, lang, tier):
    fails, warns = [], []
    parts = text.split('---', 2)
    try:
        meta = yaml.safe_load(parts[1])
        body = parts[2] if len(parts) > 2 else ''
    except Exception as e:
        return [f"{name}: YAML FAIL {e}"], []
    if not isinstance(meta, dict):
        return [f"{name}: frontmatter is not a mapping"], []

    for k in ('title', 'date', 'categories', 'tags'):
        if not meta.get(k):
            fails.append(f"{name}: missing field {k}")

    if not DATE_OK.match(str(meta.get('date', ''))):
        fails.append(f"{name}: bad date {meta.get('date')!r}")

    if 'GoodInfo' not in text:
        fails.append(f"{name}: missing GoodInfo signature")
    if re.search(r'hkhouse', text, re.I):
        fails.append(f"{name}: HKHouse BRAND LEAK")

    low = text.lower()
    hits = [w for w in BLACKLIST if (_ASCII_PAT.get(w) or _CJK_PAT[w]).search(low)]
    fails += [f"{name}: BLACKLIST {w!r}" for w in hits]

    if lang == 'EN':
        cjk = CJK.findall(text) + CJK_B.findall(text)
        if cjk:
            fails.append(f"{name}: CJK in EN ({len(cjk)}): {''.join(sorted(set(cjk))[:25])}")
    else:
        trad = sorted({c for c in text if c in TRAD and c not in SIMPLIFIED_ONLY})
        if trad:
            fails.append(f"{name}: traditional chars {trad[:12]}")

    if tier == '2':
        if lang == 'CN':
            if not str(meta.get('title', '')).startswith('[快讯]'):
                fails.append(f"{name}: T2 CN missing [快讯]")
            if not str(meta.get('title_en', '')).startswith('[Brief]'):
                fails.append(f"{name}: T2 title_en missing [Brief]")
        elif not str(meta.get('title', '')).startswith('[Brief]'):
            fails.append(f"{name}: T2 EN missing [Brief]")

    if lang == 'CN':
        for sec in ('核心摘要', '全景透视'):
            if sec not in body:
                fails.append(f"{name}: CN missing [{sec}]")
        if tier == '1' and '多方观点' not in body:
            fails.append(f"{name}: CN missing 多方观点")

        en_lines = [
            ln for ln in body.split('\n')
            if len(EN_WORD.findall(ln)) >= 6
            and len([w for w in EN_WORD.findall(ln)
                     if w.lower() in ALLOWED_EN or w.isupper()]) < len(EN_WORD.findall(ln)) - 2
        ]
        if en_lines:
            fails.append(f"{name}: {len(en_lines)} English-heavy CN lines e.g. {en_lines[0][:90]!r}")

        m = re.search(r'\*\*\[全景透视\]\*\*(.+?)(?=\n\*\*\[|\Z)', body, re.S)
        if m and len(re.sub(r'\s', '', m.group(1))) < 150:
            fails.append(f"{name}: 全景透视 too short ({len(re.sub(chr(92)+'s', '', m.group(1)))})")
    else:
        req_en = ('Key Facts', 'Wider Perspective', 'Viewpoints Compared') if tier == '1' \
            else ('Key Facts', 'Wider Perspective')
        for sec in req_en:
            if sec not in body:
                fails.append(f"{name}: EN missing [{sec}]")
        m = re.search(r'\*\*\[Wider Perspective\]\*\*(.+?)(?=\n\*\*\[|\Z)', body, re.S)
        if m and len(re.sub(r'\s', '', m.group(1))) < 150 * 3:
            warns.append(f"{name}: EN Wider Perspective short ({len(re.sub(chr(92)+'s', '', m.group(1)))})")

    # description/summary language check
    for f in ('description', 'summary', 'source'):
        v = str(meta.get(f, '') or '')
        if lang == 'EN' and CJK.search(v):
            fails.append(f"{name}: EN frontmatter {f} contains CJK")
        if lang == 'CN' and not CN_CHAR.search(v) and len(v) > 20:
            fails.append(f"{name}: CN frontmatter {f} has no Chinese ({v[:50]!r})")

    return fails, warns


def main():
    fails, warns = [], []
    nfiles = 0
    for cat, slug, tier in BATCH:
        for base, lang in (("content/posts", "CN"), ("content.en/posts", "EN")):
            path = os.path.join(ROOT, base, cat, f"{slug}.md")
            name = f"{lang}:{slug[:34]}"
            if not os.path.exists(path):
                fails.append(f"{name}: MISSING {path}")
                continue
            nfiles += 1
            f, w = audit(name, open(path, encoding='utf-8').read(), lang, tier)
            fails += f
            warns += w
            print(f"  {'FAIL' if f else ' ok '} {name} ({lang} T{tier})")
    print(f"\nfiles checked: {nfiles}")
    if fails:
        print(f"\nFAILURES ({len(fails)}):")
        for x in fails:
            print("  X", x)
    else:
        print("\nALL CHECKS PASSED")
    for x in warns:
        print("  !", x)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
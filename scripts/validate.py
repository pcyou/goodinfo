#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate GoodInfo articles before commit."""
import os
import re
import sys
import yaml
import unicodedata

ARTICLES = [
    # CN Tier 1
    ("CN", "1", "/root/goodinfo-site/content/posts/crypto/tether-usdt-iran-shadown-banking-senate-report-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/world/trump-scales-back-fuel-economy-rules-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/ai-tech/ai-tech-executives-white-house-ai-policy-meeting-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/finance/us-bond-selloff-trump-spurns-iran-offer-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/crypto/citi-coinbase-stablecoin-payment-partnership-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/world/fbi-deputy-director-andrew-bailey-resigns-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/world/russian-drone-hits-kyiv-national-academy-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/world/pope-leo-urges-ukraine-peace-concessions-2026-09-28.md"),
    ("CN", "1", "/root/goodinfo-site/content/posts/world/alito-recuses-climate-case-2026-09-28.md"),
    # CN Tier 2
    ("CN", "2", "/root/goodinfo-site/content/posts/world/brief-white-house-taxpayer-trump-promotion-2026-09-28.md"),
    ("CN", "2", "/root/goodinfo-site/content/posts/world/brief-senate-republicans-midterm-push-2026-09-28.md"),
    # EN Tier 1
    ("EN", "1", "/root/goodinfo-site/content.en/posts/crypto/tether-usdt-iran-shadown-banking-senate-report-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/world/trump-scales-back-fuel-economy-rules-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/ai-tech/ai-tech-executives-white-house-ai-policy-meeting-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/finance/us-bond-selloff-trump-spurns-iran-offer-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/crypto/citi-coinbase-stablecoin-payment-partnership-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/world/fbi-deputy-director-andrew-bailey-resigns-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/world/russian-drone-hits-kyiv-national-academy-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/world/pope-leo-urges-ukraine-peace-concessions-2026-09-28.md"),
    ("EN", "1", "/root/goodinfo-site/content.en/posts/world/alito-recuses-climate-case-2026-09-28.md"),
    # EN Tier 2
    ("EN", "2", "/root/goodinfo-site/content.en/posts/world/brief-white-house-taxpayer-trump-promotion-2026-09-28.md"),
    ("EN", "2", "/root/goodinfo-site/content.en/posts/world/brief-senate-republicans-midterm-push-2026-09-28.md"),
]

# Forbidden patterns
FORBIDDEN_TAGS = ["枪击案","枪杀","暴动","骚乱","恐怖袭击","血腥","谋杀","自杀","屠杀","人质","恐怖分子","ISIS","爆炸案","强奸","虐童","贩毒","黑帮","纵火","恐怖","gun","shooting","murder","suicide","blood","bloody","massacre","terrorist","bomb","rape","drug","gang","riot","terror","kidnap","abduction","lashes"]

FORBIDDEN_CONTENT_TERMS = [
    "rape allegations", "alleged gang rape", "raped", "kidnap victims", "lashes sentence",
    "Terror Plot", "terror plot", "terror suspects",
]

# Proper nouns allowed in CN
CN_PROPER_NOUNS = set("""AI ETF NASA FBI CIA DOJ IRS CEO CFO NATO EU G7 G20 GDP CPI IPO SEC ESG FBI DOD
OpenAI Anthropic Google Meta Coinbase Tether Citi Bloomberg Reuters NBC CBS CNN BBC 
HTTPS HTTPS IRC ICO IEO DeFi DAO L1 L2 DEX CEX NFT ETF CBDC ZK USDC USDT BTC ETH SOL 
Trump Biden Putin Zelensky Zelensky Macron Erdogan Xi Jinping Ramaphosa Alito Bailey 
Ukraine Russia USA China Israel Iran Vatican Pope Leo Trumpflation BRICS""".split())

# English sentence detection (per line) - rejects English sentences in CN files
EN_SENT_RE = re.compile(r'[A-Za-z]{4,}(?:\s+[A-Za-z]{3,}){3,}')  # 4 words with 4+ char each
CN_CHAR_RE = re.compile(r'[\u4e00-\u9fff]')
CJK_RE = re.compile(r'[\u3000-\u303f\u4e00-\u9fff]')

# Traditional Chinese detection - common simplified/traditional pairs
TRAD_PAIRS = [
    ("員","员"), ("數","数"), ("採","采"), ("允許","允许"), ("暫停","暂停"), ("分鐘","分钟"),
    ("個","个"), ("們","们"), ("這","这"), ("個","个"), ("來","来"), ("為","为"), ("從","从"),
    ("時","时"), ("會","会"), ("說","说"), ("對","对"), ("長","长"), ("學","学"), ("術","术"),
    ("觀","观"), ("點","点"), ("議","议"), ("題","题"), ("產","产"), ("業","业"), ("發","发"),
    ("記","记"), ("應","应"), ("聲","声"), ("體","体"), ("關","关"), ("開","开"), ("選","选"),
    ("戰","战"), ("頭","头"), ("顯","显"), ("條","条"), ("處","处"), ("歷","历"), ("畫","画"),
    ("畫","画"), ("種","种"), ("價","价"), ("營","营"), ("專","专"), ("節","节"), ("檢","检"),
    ("標","标"), ("權","权"), ("熱","热"), ("練","练"), ("縣","县"), ("櫃","柜"), ("轉","转"),
    ("黨","党"), ("齡","龄"), ("興","兴"), ("興","兴"), ("紅","红"), ("辦","办"), ("語","语"),
    ("訊","讯"), ("計","计"), ("認","认"), ("讓","让"), ("測","测"), ("兒","儿"), ("鄉","乡"),
    ("術","术"), ("證","证"), ("貝","贝"), ("賓","宾"), ("贏","赢"), ("報","报"), ("寫","写"),
]

def is_traditional_line(line):
    for trad, simp in TRAD_PAIRS:
        if trad in line and simp not in line.replace(trad, ""):
            return True
    return False

def detect_english_sentences_cn(text):
    """Find English sentences in CN text (lines with 4+ EN words and no CN chars)."""
    issues = []
    for ln, line in enumerate(text.split("\n")):
        # Skip code blocks and short lines
        if not line.strip() or len(line) < 30:
            continue
        if CN_CHAR_RE.search(line):
            continue  # has Chinese - skip
        # Count English words
        words = re.findall(r'[A-Za-z]+', line)
        if len(words) >= 5:
            issues.append((ln+1, line[:120]))
    return issues

def detect_cjk_en(text):
    """Find CJK chars in EN text."""
    issues = []
    for ln, line in enumerate(text.split("\n")):
        # Skip frontmatter lines? No - frontmatter must be English too
        cjk = CJK_RE.findall(line)
        if cjk:
            issues.append((ln+1, line[:120], cjk[:5]))
    return issues

def check_footer(text):
    if "GoodInfo" not in text:
        return "Footer missing GoodInfo"
    if "HKHouse" in text:
        return "Footer has HKHouse - FORBIDDEN"
    return None

def check_signature_cn(text):
    return "编辑：GoodInfo全球资讯组" in text

def check_signature_en(text):
    return "Editor: GoodInfo Global News Team" in text

def check_tier2_prefix(meta, tier, lang):
    if tier != "2":
        return None
    title = meta.get("title", "")
    title_en = meta.get("title_en", "")
    if lang == "CN":
        if not title.startswith("[快讯]"):
            return f"CN title missing [快讯] prefix: {title[:60]}"
        if not title_en.startswith("[Brief]"):
            return f"EN title_en missing [Brief] prefix: {title_en[:60]}"
    else:  # EN
        # In EN files, `title` is the English title (with [Brief])
        if not title.startswith("[Brief]"):
            return f"EN title missing [Brief] prefix: {title[:60]}"
        if not title_en.startswith("[Brief]"):
            return f"EN title_en missing [Brief] prefix: {title_en[:60]}"
    return None

def check_panoramic(text, tier):
    if tier != "1":
        return None
    if "全景透视" not in text and "Panoramic Analysis" not in text:
        return "Missing 全景透视/Panoramic Analysis section"
    return None

def check_sensitive_tags(meta):
    issues = []
    tags = meta.get("tags", []) or []
    for t in tags:
        if t.lower() in [x.lower() for x in FORBIDDEN_TAGS]:
            issues.append(t)
    return issues

def check_sensitive_content(text, lang):
    issues = []
    text_lower = text.lower()
    for term in FORBIDDEN_CONTENT_TERMS:
        if term.lower() in text_lower:
            issues.append(term)
    return issues

def main():
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
        # Parse frontmatter
        try:
            m = re.match(r'^---\n(.*?)\n---\n(.*)$', text, re.DOTALL)
            assert m, "no frontmatter"
            fm_text = m.group(1)
            body = m.group(2)
            meta = yaml.safe_load(fm_text)
        except Exception as e:
            print(f"  ❌ YAML parse error: {e}")
            errors += 1
            continue
        print(f"  ✓ YAML parsed. Title: {meta.get('title','')[:60]}")
        # Tier 2 prefix
        e = check_tier2_prefix(meta, tier, lang)
        if e:
            print(f"  ❌ {e}")
            errors += 1
        # Panoramic section
        e = check_panoramic(body, tier)
        if e:
            print(f"  ❌ {e}")
            errors += 1
        # Footer
        e = check_footer(text)
        if e:
            print(f"  ❌ {e}")
            errors += 1
        else:
            print(f"  ✓ Footer: GoodInfo present, no HKHouse")
        # Signature
        if lang == "CN":
            if not check_signature_cn(body):
                print(f"  ❌ Missing '编辑：GoodInfo全球资讯组'")
                errors += 1
            else:
                print(f"  ✓ CN signature present")
        else:
            if not check_signature_en(body):
                print(f"  ❌ Missing 'Editor: GoodInfo Global News Team'")
                errors += 1
            else:
                print(f"  ✓ EN signature present")
        # CJK in EN
        if lang == "EN":
            cjk = detect_cjk_en(text)
            if cjk:
                print(f"  ❌ CJK chars found in EN file: {len(cjk)} lines")
                for ln, line, c in cjk[:3]:
                    print(f"     L{ln}: {c} | {line[:90]}")
                errors += 1
            else:
                print(f"  ✓ No CJK in EN file")
        # English sentences in CN
        if lang == "CN":
            ens = detect_english_sentences_cn(body)
            if ens:
                print(f"  ❌ English sentences in CN file: {len(ens)}")
                for ln, line in ens[:3]:
                    print(f"     L{ln}: {line[:100]}")
                errors += 1
            else:
                print(f"  ✓ No English sentences in CN body")
        # Traditional Chinese
        trad_lines = []
        for ln, line in enumerate(text.split("\n")):
            if is_traditional_line(line):
                trad_lines.append((ln+1, line[:80]))
        if trad_lines:
            print(f"  ❌ Traditional Chinese detected: {len(trad_lines)} lines")
            for ln, l in trad_lines[:3]:
                print(f"     L{ln}: {l}")
            errors += 1
        else:
            print(f"  ✓ Simplified Chinese only")
        # Sensitive tags
        st = check_sensitive_tags(meta)
        if st:
            print(f"  ❌ Sensitive tags: {st}")
            errors += 1
        else:
            print(f"  ✓ Tags clean")
        # Sensitive content terms
        sc = check_sensitive_content(body, lang)
        if sc:
            print(f"  ❌ Sensitive content: {sc}")
            errors += 1
        else:
            print(f"  ✓ Content clean")
        # Word count
        body_only = re.sub(r'[#*`>|\-\[\]]', ' ', body)
        wc = len([w for w in re.split(r'\s+', body_only) if w.strip()])
        print(f"  ℹ Word count (rough): {wc}")
    print(f"\n{'='*70}")
    print(f"ERRORS: {errors}")

if __name__ == "__main__":
    main()
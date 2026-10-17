#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Wall Street Q3 2026 earnings article (Tier 1 bilingual)."""
import sys, os
sys.path.insert(0, '/root/goodinfo-site')
from scripts.generate import yaml_field, write_article, sanitize_text, filter_tags

NOW_BJT_STR = "2026-10-14T02:21:00+08:00"

title_cn = "华尔街三大行Q3财报超预期 高利率驱动贷款收入创纪录"
title_en = "Wall Street Banks Beat Q3 Expectations as High Rates Turbocharge Lending Income"

description_cn = "摩根大通、高盛与富国银行10月中旬相继公布2026年第三季度财报，营收与利润双双超预期，主要受益于高利率环境下贷款利息收入大幅增长以及投行业务回暖。"

summary_cn = "摩根大通、高盛、富国银行与花旗银行本周陆续公布2026年第三季度财报，营收与利润均超出市场预期。高利率环境下贷款与利息收入大幅上升、投行业务回暖以及交易部门稳健表现共同推动业绩，但分析师警告高利率对零售与中小企业贷款带来的潜在违约风险亦不可忽视。"

source = "WSJ / Reuters / Bloomberg / CNBC"

body_cn = """**[核心摘要]**

美国四大银行摩根大通、高盛集团、富国银行与花旗银行10月14日前后集中公布2026年第三季度业绩，主要受高利率环境下贷款利息收入跃升和投行业务回暖推动，营收与净利润均超出华尔街分析师预期。

**[事件详情]**

- **业绩概况**：摩根大通第三季度净利润同比增长约9%，营收达到447亿美元，超出分析师预期；高盛集团净利润同比增长约12%，投行业务收入同比增长约25%，交易部门营收稳健。
- **富国银行与花旗**：富国银行第三季度净利润同比增长约8%，主要来自净利息收入的增长；花旗银行净利润同比增长约7%，得益于全球银行业务的强劲表现。
- **市场反应**：财报公布后四大银行股价普遍上涨2%至4%，市场对银行业盈利前景持乐观态度。
- **分析师观点**：分析师指出，尽管业绩超预期，但高利率环境对零售贷款和中小企业贷款的潜在违约风险仍需密切关注。

**[全景透视]**

华尔街四大行第三季度财报集体超预期，反映出高利率环境下美国银行业盈利模式的结构性变化。在美联储维持较高政策利率的背景下，银行净息差扩大，贷款利息收入成为推动业绩增长的核心引擎。同时，2026年第三季度资本市场活动回暖，IPO与并购重组数量回升，为投行业务带来强劲收入。这一趋势若持续，可能进一步推动银行业资本充足率提升，为后续信贷扩张和股东回报创造空间。然而，零售贷款和中小企业贷款违约率上行的潜在风险亦不容忽视，若经济动能进一步放缓，银行业绩增长可能面临挑战。

**[多方观点对比]**

- **银行管理层乐观**：摩根大通首席执行官杰米·戴蒙表示，业绩反映出美国经济韧性以及消费者支出的稳健增长。
- **分析师谨慎**：部分分析师认为，银行业绩增长高度依赖利率环境，若美联储转向降息周期，净息差可能收窄。
- **市场分歧**：部分投资者对银行业绩可持续性持怀疑态度，认为当前估值已充分反映乐观预期，回调风险上升。

*编辑：GoodInfo全球资讯组*
"""

meta = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_cn,
    "summary": summary_cn,
    "source": source,
    "categories": ["finance"],
    "tags": ["财报", "华尔街", "摩根大通", "高盛", "富国银行", "花旗银行", "银行业", "美国经济"],
}

path_cn = "/root/goodinfo-site/content/posts/finance/wall-street-q3-2026-bank-earnings-beat-oct-2026.md"
write_article(path_cn, meta, body_cn)
print(f"CN written: {path_cn}")

# English version
title_en_full = title_en
summary_en = "JPMorgan, Goldman Sachs, Wells Fargo, and Citi reported Q3 2026 earnings that beat Wall Street expectations, driven by higher net interest income from the high-rate environment and a rebound in investment banking. Revenue and net profit all exceeded analyst forecasts."
description_en = "JPMorgan, Goldman Sachs, Wells Fargo, and Citi reported Q3 2026 earnings that beat expectations, driven by higher net interest income and a rebound in investment banking."

body_en = """**[Core Summary]**

JPMorgan, Goldman Sachs, Wells Fargo, and Citi reported Q3 2026 earnings that beat Wall Street expectations, driven primarily by higher net interest income in the high-rate environment and a rebound in investment banking activity.

**[Event Details]**

- **Earnings Overview**: JPMorgan reported Q3 net profit up roughly 9% year-over-year with revenue of $44.7 billion, exceeding analyst forecasts. Goldman Sachs posted net profit growth of around 12%, with investment banking revenue up about 25% and a solid trading performance.
- **Wells Fargo and Citi**: Wells Fargo's Q3 net profit rose roughly 8%, driven by net interest income growth. Citi's net profit increased about 7%, supported by strong performance in global banking.
- **Market Reaction**: Shares of the four major banks rose 2% to 4% after the earnings releases, with the market showing optimism about the sector's earnings outlook.
- **Analyst View**: Analysts noted that while the results beat expectations, potential default risks in retail and small-business lending under the high-rate environment warrant close attention.

**[Panorama]**

The collective earnings beat by Wall Street's four major banks reflects a structural shift in the U.S. banking profit model under a high-rate environment. With the Federal Reserve maintaining a relatively elevated policy rate, net interest margins have expanded and loan interest income has become the core engine driving earnings growth. Meanwhile, the recovery in capital market activity during Q3 2026, with rising IPO and M&A deal volumes, has delivered strong revenue for the investment banking divisions. If this trend continues, it could further strengthen bank capital adequacy ratios, creating room for credit expansion and shareholder returns. However, the potential upside risks in retail and small-business loan default rates cannot be ignored; if economic momentum slows further, bank earnings growth may face headwinds.

**[Multiple Perspectives]**

- **Bank Management Optimistic**: JPMorgan CEO Jamie Dimon stated that the results reflect U.S. economic resilience and robust consumer spending.
- **Analysts Cautious**: Some analysts noted that bank earnings growth is highly dependent on the rate environment, and net interest margins could compress if the Fed shifts to a cutting cycle.
- **Market Divided**: Some investors are skeptical about the sustainability of bank earnings, arguing that current valuations already fully reflect optimistic expectations and that pullback risks are rising.

*Editor: GoodInfo Global News Desk*
"""

meta_en = {
    "title": title_en_full,
    "title_en": title_en_full,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_en,
    "summary": summary_en,
    "source": source,
    "categories": ["finance"],
    "tags": ["Earnings", "Wall Street", "JPMorgan", "Goldman Sachs", "Wells Fargo", "Citi", "Banking", "US Economy"],
}

path_en = "/root/goodinfo-site/content.en/posts/finance/wall-street-q3-2026-bank-earnings-beat-oct-2026.md"
write_article(path_en, meta_en, body_en)
print(f"EN written: {path_en}")

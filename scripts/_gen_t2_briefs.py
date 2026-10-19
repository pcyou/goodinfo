#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tier 2 briefs for 2026-10-19 17:00 BJT:
  A. Australian MP Helen Haines critically injured in vehicle ramming
  B. West Bank settler attacks, Israel arrests 10 suspects
  C. China Q3 GDP expanded 4.5%
"""
import sys
sys.path.insert(0, '/root/goodinfo-site')
from scripts.adsense_sanitize import sanitize_title, sanitize_content, sanitize_tags
from scripts.generate import yaml_field, article_header, write_article

NOW_BJT_STR = "2026-10-19T17:00:00+08:00"


# ======================================================================
# AUSTRALIA MP HELEN HAINES — TIER 2 BRIEF
# ======================================================================
title_A_cn_raw = "[快讯] 澳大利亚独立议员海伦・黑恩斯在选区办公室附近遭车辆撞击 伤情危重"
title_A_en_raw = "[Brief] Australian Independent MP Helen Haines Critically Injured in Vehicle Ramming Near Electorate Office"

description_A_cn_raw = "澳大利亚独立议员海伦・黑恩斯在维多利亚州选区办公室附近遭一名男子驾驶的车辆撞击，伤情危重，警方已逮捕涉案驾驶员。"
summary_A_cn_raw = "澳大利亚独立议员海伦・黑恩斯10月19日在维多利亚州选区办公室附近遭车辆撞击，目前伤情危重，警方已逮捕涉案驾驶员并定性为蓄意行为，总理阿尔巴尼斯予以强烈谴责。"

source_AB = "Politico / BBC / Reuters / The Guardian"

body_A_cn_raw = """**[核心摘要]**

澳大利亚独立议员海伦・黑恩斯10月19日在维多利亚州选区办公室附近遭一名男子驾驶的车辆撞击，目前伤情危重。警方已逮捕涉案驾驶员，初步调查将其定性为蓄意行为，总理阿尔巴尼斯予以强烈谴责，并下令加强全国民选代表的安全保障。

**[事件详情]**

- **事件经过**：黑恩斯当天在选区办公室外与选民会面时，遭一名男子驾驶的车辆撞击，事发地点在维多利亚州东北部。
- **伤情通报**：院方表示黑恩斯伤情危重，已接受紧急手术并转入重症监护，警方形容伤势严重但生命体征暂时稳定。
- **嫌疑人处理**：现场一名涉案男子已被逮捕，警方初步调查显示事件系蓄意所为，动机仍在调查之中。
- **政治反应**：阿尔巴尼斯总理在记者会上称这是一次"令人震惊的蓄意行为"，并下令对全体议员安全安排进行紧急评估。
- **后续影响**：黑恩斯所属选区的部分公开活动已经取消，议会办公室将与警方协作评估安全形势。

**[全景透视]**

此次针对议员的暴力事件再次凸显出民选代表在公共接触与个人安全之间日益复杂的平衡难题。澳大利亚近年已多次发生针对议员办公室的骚扰与破坏事件，从涂鸦、纵火到人身威胁，逐步升级至今日的人身撞击。各国政界人士面对日益两极化的舆论环境，其在公共场所的工作模式正在被迫调整，包括增加出行随员、限制选民面对面接触以及加强办公室物理防护。这一趋势如果加剧，可能进一步拉远民众与政治人物之间的物理距离，削弱代议制民主赖以运行的互动基础。

*编辑：GoodInfo全球资讯组*
"""

body_A_en_raw = """**[Key Facts]**

Australian independent MP Helen Haines was critically injured on October 19 when a vehicle struck her near her electorate office in regional Victoria. A man has been taken into custody, with police treating the incident as a deliberate act. Prime Minister Anthony Albanese condemned the incident and ordered an urgent review of safety arrangements for federal parliamentarians.

**[What We Know]**

- **Sequence**: Haines was meeting constituents outside her electorate office in northeast Victoria when she was struck by a vehicle driven by a male suspect.
- **Condition**: Hospital officials described her condition as critical; she underwent emergency surgery and remains in intensive care, with police describing the injuries as serious but her vital signs currently stable.
- **Suspect**: A man has been taken into custody at the scene; investigators say early evidence indicates the act was deliberate, with motive still under examination.
- **Political reaction**: PM Albanese called the event a "shocking deliberate act" and ordered an immediate safety review for all federal parliamentarians.
- **Aftermath**: Public events in Haines' electorate have been cancelled while Parliament House security and Victoria Police coordinate the next operational steps.

**[Wider Perspective]**

The incident is the latest in a string of escalating incidents targeting Australian elected officials, ranging from vandalism and arson of electorate offices to direct personal threats. As political polarisation intensifies across many democracies, the working model of elected representatives — open office hours, street canvassing and unscripted constituent meetings — is becoming harder to sustain without significant security overheads. If events of this kind recur, parliaments may be forced to insulate their members more aggressively from the public, eroding the everyday accessibility that underpins representative democracy.

*Editor: GoodInfo Global News Team*
"""

title_A_cn = sanitize_title(title_A_cn_raw)
title_A_en = sanitize_title(title_A_en_raw)
description_A_cn = sanitize_title(description_A_cn_raw)
summary_A_cn = sanitize_title(summary_A_cn_raw)
description_A_en = sanitize_title("Australian independent MP Helen Haines was critically injured when a vehicle struck her near her electorate office in Victoria on October 19; a man is in custody.")
summary_A_en = sanitize_title("Australian independent MP Helen Haines was critically injured on October 19 in a vehicle-ramming near her electorate office in Victoria. A man is in custody; PM Albanese condemned the incident and ordered a nationwide review of MP safety arrangements.")

body_A_cn = sanitize_content(body_A_cn_raw)
body_A_en = sanitize_content(body_A_en_raw)

tags_A_cn_raw = ["澳大利亚", "黑恩斯", "议员安全", "国际动态", "社会时事"]
tags_A_en_raw = ["Australia", "Helen Haines", "Parliament Security", "Electoral Violence"]

tags_A_cn = sanitize_tags(tags_A_cn_raw)
tags_A_en = sanitize_tags(tags_A_en_raw)

meta_A_cn = {
    "title": title_A_cn, "title_en": title_A_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_A_cn, "summary": summary_A_cn,
    "source": source_AB, "categories": ["world"], "tags": tags_A_cn,
}
path_A_cn = "/root/goodinfo-site/content/posts/world/brief-australia-mp-helen-haines-vehicle-strike-2026-10-19.md"
write_article(path_A_cn, meta_A_cn, body_A_cn)
print(f"A CN: {path_A_cn}")

meta_A_en = {
    "title": title_A_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_A_en, "summary": summary_A_en,
    "source": source_AB, "categories": ["world"], "tags": tags_A_en,
}
path_A_en = "/root/goodinfo-site/content.en/posts/world/brief-australia-mp-helen-haines-vehicle-strike-2026-10-19.md"
write_article(path_A_en, meta_A_en, body_A_en)
print(f"A EN: {path_A_en}")


# ======================================================================
# WEST BANK SETTLER ATTACKS — TIER 2 BRIEF
# ======================================================================
title_B_cn_raw = "[快讯] 以色列逮捕十名涉嫌约旦河西岸袭击事件的嫌疑人 美国持续施压"
title_B_en_raw = "[Brief] Israel Arrests Ten Suspects over West Bank Attacks on Journalists and EU Diplomats as US Pressure Mounts"

description_B_cn_raw = "以色列警方10月18日宣布逮捕十名涉嫌参与约旦河西岸袭击外国记者与欧盟外交官事件的嫌疑人，行动背景为美国持续施压以遏制定居者暴力。"
summary_B_cn_raw = "以色列警方10月18日宣布逮捕十名涉嫌参与近期约旦河西岸袭击外国记者与欧盟外交官事件的嫌疑人，此举发生在美国总统特使持续施压要求遏制定居者暴力的背景下，多家媒体披露袭击事件细节。"

source_WB = "The Times of Israel / CNN / NPR / The New York Times / AP"

body_B_cn_raw = """**[核心摘要]**

以色列警方与辛贝特10月18日宣布逮捕十名涉嫌参与约旦河西岸袭击外国记者与欧盟外交官事件的嫌疑人。此次行动发生在美国总统特使持续施压要求遏制定居者暴力的背景下，多家媒体披露袭击事件细节并引发国际社会高度关注。

**[事件详情]**

- **行动规模**：以色列警方与安全部门在约旦河西岸多地开展同步行动，逮捕十名涉案嫌疑人，并对相关定居点展开搜查取证。
- **事件背景**：被捕嫌疑人涉嫌参与此前针对一名外国摄影记者与一组欧盟外交人员车辆的袭击，相关袭击发生在约旦河西岸北部地区。
- **国际压力**：美国总统特使近期与以色列高层多次会晤，要求对方采取切实措施遏制定居者暴力事件，否则将影响双边关系与中东援助安排。
- **各方反应**：欧盟外交事务发言人重申对驻外人员安全的关切，并要求以方提供调查进展通报，多家国际媒体记者在现场记录袭击事件。
- **后续程序**：被捕嫌疑人已移送司法部门处理，以方表示将在适当时候公布更多调查细节，相关指控若成立将面临多年监禁。

**[全景透视]**

此次逮捕行动既是以色列对国际压力的具体回应，也反映出定居者暴力问题已对其国际形象与外交关系构成实质性挑战。在欧洲多国因定居者暴力升级而考虑对以方采取限制措施、美国国会议员推动有条件援助法案的背景下，以色列政府在国内政治压力与国际责任之间的博弈空间正不断收窄。如果后续调查与司法程序能够产生有说服力的判决结果，可能有助于缓解部分国际质疑；反之，案件若以从轻处理收场，将进一步削弱以方在该议题上的国际公信力，并加剧欧美在对以政策上的内部分歧。国际舆论的关注焦点也将从单一袭击事件转向以色列司法体系对定居者暴力案件的处置能力与公正性。

*编辑：GoodInfo全球资讯组*
"""

body_B_en_raw = """**[Key Facts]**

Israeli police and the Shin Bet security service announced on October 18 that ten suspects had been arrested in connection with recent West Bank attacks on a foreign photojournalist and EU diplomatic personnel. The operation comes amid sustained US pressure on Israel to curb settler violence, with multiple international outlets reporting on the incidents in detail.

**[What We Know]**

- **Operation scope**: Coordinated raids across several West Bank locations led to ten arrests, with searches carried out at linked settlement addresses.
- **Incident background**: The suspects are alleged to have taken part in attacks on a foreign photographer and a group of EU diplomats in the northern West Bank in recent days.
- **International pressure**: The US presidential envoy has held repeated meetings with senior Israeli officials demanding concrete steps to curb settler violence, warning of consequences for bilateral ties and Middle East aid arrangements.
- **Reactions**: The EU's foreign affairs spokesperson reiterated concern for the safety of EU personnel and demanded updates on the investigation; international media crews documented the incidents in the field.
- **Legal process**: Suspects have been remanded; Israel says further investigative details will be released in due course. Convictions on the alleged charges carry multi-year prison terms.

**[Wider Perspective]**

The arrests reflect an Israeli calculation that unchecked settler violence is now exacting a real cost on the country's international standing and diplomatic relationships. European governments have been weighing countermeasures and senior US lawmakers continue to push conditional-aid legislation, narrowing the political space Israeli leaders have to navigate between domestic coalition pressures and international responsibilities. If the legal process produces robust convictions, the international criticism may partially subside; if cases are resolved lightly, however, expect more vocal demands from Brussels and Washington for systemic accountability, deepening transatlantic divides over how to handle the settler question.

*Editor: GoodInfo Global News Team*
"""

title_B_cn = sanitize_title(title_B_cn_raw)
title_B_en = sanitize_title(title_B_en_raw)
description_B_cn = sanitize_title(description_B_cn_raw)
summary_B_cn = sanitize_title(summary_B_cn_raw)
description_B_en = sanitize_title("Israeli police arrested ten suspects in connection with recent West Bank attacks on a foreign photojournalist and EU diplomats, amid sustained US pressure to curb settler violence.")
summary_B_en = sanitize_title("Israeli police and the Shin Bet announced on October 18 the arrest of ten suspects in recent West Bank attacks on a foreign photojournalist and EU diplomatic personnel. The operation follows sustained US envoy pressure on Israel to curb settler violence.")

body_B_cn = sanitize_content(body_B_cn_raw)
body_B_en = sanitize_content(body_B_en_raw)

tags_B_cn_raw = ["以色列", "约旦河西岸", "定居者", "美国", "欧盟", "国际动态", "社会时事"]
tags_B_en_raw = ["Israel", "West Bank", "Settler Violence", "United States", "European Union", "Diplomacy"]

tags_B_cn = sanitize_tags(tags_B_cn_raw)
tags_B_en = sanitize_tags(tags_B_en_raw)

meta_B_cn = {
    "title": title_B_cn, "title_en": title_B_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_B_cn, "summary": summary_B_cn,
    "source": source_WB, "categories": ["world"], "tags": tags_B_cn,
}
path_B_cn = "/root/goodinfo-site/content/posts/world/brief-israel-arrests-west-bank-settler-attack-suspects-2026-10-19.md"
write_article(path_B_cn, meta_B_cn, body_B_cn)
print(f"B CN: {path_B_cn}")

meta_B_en = {
    "title": title_B_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_B_en, "summary": summary_B_en,
    "source": source_WB, "categories": ["world"], "tags": tags_B_en,
}
path_B_en = "/root/goodinfo-site/content.en/posts/world/brief-israel-arrests-west-bank-settler-attack-suspects-2026-10-19.md"
write_article(path_B_en, meta_B_en, body_B_en)
print(f"B EN: {path_B_en}")


# ======================================================================
# CHINA Q3 GDP — TIER 2 BRIEF
# ======================================================================
title_C_cn_raw = "[快讯] 中国第三季度 GDP 同比增长百分之四点五 出口与工业生产为主要支撑"
title_C_en_raw = "[Brief] China's Q3 GDP Expands 4.5 Percent Year-on-Year, Powered by Exports and Industrial Output"

description_C_cn_raw = "中国国家统计局公布第三季度 GDP 同比增长百分之四点五，出口与工业生产为主要支撑，零售与房地产投资仍承压。"
summary_C_cn_raw = "中国国家统计局10月19日公布的数据显示，第三季度 GDP 同比增长百分之四点五，与第二季度持平，出口与工业生产为主要支撑，但零售消费与房地产投资仍延续低迷态势。"

source_GDP = "Wall Street Journal / Bloomberg / Reuters / Xinhua"

body_C_cn_raw = """**[核心摘要]**

中国国家统计局10月19日公布的数据显示，第三季度国内生产总值同比增长百分之四点五，与第二季度增速持平。出口与工业生产继续为主要支撑，但零售消费与房地产投资仍延续低迷态势，凸显经济内生动能修复的不平衡格局。

**[事件详情]**

- **整体增速**：第三季度 GDP 同比增速为百分之四点五，与上一季度持平，符合市场预期，前三季度累计同比增长百分之五点一。
- **工业表现**：规模以上工业增加值同比增长超过百分之六，其中装备制造业与高技术制造业增速显著高于整体水平。
- **出口拉动**：以美元计价的出口同比增长接近百分之九，对东盟与"一带一路"沿线市场表现尤其突出。
- **消费偏弱**：社会消费品零售总额增速放缓至约百分之三，汽车与家电等大宗消费表现低于历史同期。
- **房地产延续调整**：全国房地产开发投资同比下降约百分之十五，商品房销售面积与销售额同比降幅虽有所收窄但仍处低位。

**[全景透视]**

第三季度经济数据呈现出中国经济增长引擎切换过程中的典型特征：外需与制造业投资成为稳定器，而内需特别是房地产相关链条仍是主要拖累。这一结构背后既反映了海外市场需求改善与全球补库存周期的外部红利，也暴露出国内消费信心与企业资本支出意愿仍待修复的深层问题。在出口端持续承压与房地产调整周期延长的背景下，宏观政策预计将继续保持适度宽松，但具体路径将在稳增长、防风险与调结构之间寻求精细平衡。

*编辑：GoodInfo全球资讯组*
"""

body_C_en_raw = """**[Key Facts]**

China's National Bureau of Statistics released GDP data on October 19 showing third-quarter economic growth at 4.5 percent year-on-year, unchanged from the second quarter. Exports and industrial output remained the main supports, while retail consumption and property investment continued to weigh on the headline figure.

**[What We Know]**

- **Headline growth**: Q3 GDP grew 4.5 percent year-on-year, in line with market expectations and unchanged from Q2; cumulative growth for the first three quarters stood at 5.1 percent.
- **Industry**: Value-added industrial output from major enterprises rose more than 6 percent year-on-year, with equipment manufacturing and high-tech manufacturing noticeably outperforming the overall figure.
- **Exports**: Dollar-denominated exports rose close to 9 percent year-on-year, with particularly strong growth into ASEAN and Belt-and-Road markets.
- **Consumption**: Retail sales growth slowed to around 3 percent, with auto and home-appliance spending below the same period in recent years.
- **Property**: National property development investment fell about 15 percent year-on-year; although declines in sales area and value narrowed, both remained in negative territory.

**[Wider Perspective]**

The Q3 data illustrates the typical pattern of China's growth-engine transition: external demand and manufacturing investment are stabilisers, while domestic demand — especially property-linked activity — continues to drag. Strong export growth reflects both restocking cycles abroad and improved competitiveness in selected sectors; weak consumer sentiment and corporate capex caution underline the deeper structural challenges of rebalancing the economy toward consumption. With property adjustments likely to extend further and external demand facing renewed uncertainty, policymakers are expected to keep policy settings moderately accommodative, carefully calibrating the trade-off between growth stabilisation, risk control and structural rebalancing.

*Editor: GoodInfo Global News Team*
"""

title_C_cn = sanitize_title(title_C_cn_raw)
title_C_en = sanitize_title(title_C_en_raw)
description_C_cn = sanitize_title(description_C_cn_raw)
summary_C_cn = sanitize_title(summary_C_cn_raw)
description_C_en = sanitize_title("China's Q3 GDP grew 4.5 percent year-on-year, unchanged from Q2; exports and industrial output were the main supports, while retail and property investment remained soft.")
summary_C_en = sanitize_title("China's National Bureau of Statistics released Q3 GDP data on October 19 showing 4.5 percent year-on-year growth, unchanged from Q2. Exports and industrial output supported the figure, while retail consumption and property investment continued to weigh on the headline number.")

body_C_cn = sanitize_content(body_C_cn_raw)
body_C_en = sanitize_content(body_C_en_raw)

tags_C_cn_raw = ["中国", "经济数据", "GDP", "第三季度", "出口", "房地产", "国际动态", "财经"]
tags_C_en_raw = ["China", "GDP", "Economic Data", "Q3", "Exports", "Property Market", "Macroeconomy"]

tags_C_cn = sanitize_tags(tags_C_cn_raw)
tags_C_en = sanitize_tags(tags_C_en_raw)

meta_C_cn = {
    "title": title_C_cn, "title_en": title_C_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_C_cn, "summary": summary_C_cn,
    "source": source_GDP, "categories": ["finance"], "tags": tags_C_cn,
}
path_C_cn = "/root/goodinfo-site/content/posts/finance/brief-china-q3-gdp-4-5-percent-2026-10-19.md"
write_article(path_C_cn, meta_C_cn, body_C_cn)
print(f"C CN: {path_C_cn}")

meta_C_en = {
    "title": title_C_en, "date": NOW_BJT_STR,
    "draft": "false", "tier": "2",
    "description": description_C_en, "summary": summary_C_en,
    "source": source_GDP, "categories": ["finance"], "tags": tags_C_en,
}
path_C_en = "/root/goodinfo-site/content.en/posts/finance/brief-china-q3-gdp-4-5-percent-2026-10-19.md"
write_article(path_C_en, meta_C_en, body_C_en)
print(f"C EN: {path_C_en}")

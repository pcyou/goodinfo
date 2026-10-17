#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Tier 2 briefs for Oct 14 4h window."""
import sys, os
sys.path.insert(0, '/root/goodinfo-site')
from scripts.generate import yaml_field, write_article

NOW_BJT_STR = "2026-10-14T02:21:00+08:00"

# --- BRIEF 1: Argentina Falklands maritime tribunal ---
title_cn = "[快讯] 阿根廷就福克兰群岛石油勘探向国际海洋法庭提起申诉"
title_en = "[Brief] Argentina Files Legal Claim with International Maritime Tribunal over UK Falklands Oil Exploration"

description_cn = "阿根廷就英国在福克兰群岛海域的石油勘探活动向国际海洋法庭提起法律申诉。"
summary_cn = "阿根廷就英国在福克兰群岛海域的石油勘探活动向国际海洋法庭提起法律申诉，标志两国围绕该群岛主权与资源开发的争议再度升级。"

source = "BBC News"
body_cn = """**[核心摘要]**

阿根廷政府10月14日就英国在福克兰群岛海域的石油勘探活动向国际海洋法庭提起法律申诉，标志两国围绕该群岛主权与资源开发争议再度升级。

**[事件详情]**

- **法律行动**：阿根廷已就英国在福克兰群岛海域的石油勘探活动向国际海洋法庭提交法律申诉。
- **背景**：阿根廷总统米莱近期持续升级对福克兰群岛的主权声索，指责英国在该海域的勘探活动侵犯阿根廷主权。
- **英方立场**：英国政府多次明确表示对福克兰群岛拥有主权，拒绝就主权问题与阿根廷进行任何谈判或航线安排。
- **能源意义**：福克兰群岛周边海域被认为蕴藏丰富的石油与天然气资源，是双方争议的经济核心。

**[全景透视]**

阿根廷此次法律行动标志着福克兰群岛争议在能源利益驱动下持续升温。在南大西洋海域被认为蕴藏可观油气资源的背景下，阿根廷与英国围绕勘探许可、海洋管辖权与环境保护标准的分歧日益尖锐。国际海洋法庭的受理将开启漫长的法律程序，短期内难以对实际勘探活动产生影响，但可能加剧双边外交紧张局势，并引发周边国家对南极与南大西洋资源开发规则的高度关注。

*编辑：GoodInfo全球资讯组*
"""

meta = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_cn,
    "summary": summary_cn,
    "source": source,
    "categories": ["world"],
    "tags": ["阿根廷", "英国", "福克兰群岛", "国际动态", "南美政治", "能源", "外交"],
}

path = "/root/goodinfo-site/content/posts/world/brief-argentina-falklands-maritime-tribunal-2026-10-14.md"
write_article(path, meta, body_cn)
print(f"Brief 1: {path}")

# --- BRIEF 2: Bulgaria Black Sea ship sunk ---
title_cn = "[快讯] 保加利亚传召俄大使 一艘商船在黑海无人机袭击中沉没10人失踪"
title_en = "[Brief] Bulgaria Summons Russian Ambassador after Merchant Ship Sunk in Black Sea Drone Attack"

description_cn = "保加利亚就黑海商船遭无人机袭击沉没事件传召俄罗斯大使，六名船员获救但仍有十人失踪。"
summary_cn = "保加利亚政府10月14日就一艘商船在黑海遭无人机袭击沉没事件传召俄罗斯大使，六名船员获救但仍有十人失踪。"

source = "BBC News"
body_cn = """**[核心摘要]**

保加利亚政府10月14日就一艘商船在黑海遭无人机袭击沉没事件传召俄罗斯大使，六名船员获救但仍有十人失踪。

**[事件详情]**

- **事件经过**：一艘商船在黑海海域遭无人机袭击后沉没，六名船员获救，十人仍处于失踪状态。
- **外交行动**：保加利亚已传召俄罗斯大使，要求就袭击事件作出解释，并保留采取进一步措施的权利。
- **航运影响**：事件发生在黑海航运安全持续承压的背景下，多国船东已对黑海航线提高保险费率，部分船公司考虑暂停相关航线运营。
- **北约协调**：保加利亚作为北约与欧盟成员国，正与盟国协调评估黑海区域安全形势，并考虑加强对民用航运的护航行动。

**[全景透视]**

此次商船沉没事件再次暴露黑海航运面临的非传统安全威胁。在俄乌冲突延宕背景下，黑海港口与航线频繁成为无人机与导弹袭击的目标，对全球粮食与能源供应链构成持续冲击。保加利亚的传召行动既是外交抗议，也可能推动北约与欧盟加强对黑海民用航运的保护与监测。短期内，相关航线保险成本可能进一步上行，并对黑海地区贸易流量产生连锁影响。

*编辑：GoodInfo全球资讯组*
"""

meta = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_cn,
    "summary": summary_cn,
    "source": source,
    "categories": ["world"],
    "tags": ["保加利亚", "俄罗斯", "黑海", "国际动态", "航运", "北约"],
}

path = "/root/goodinfo-site/content/posts/world/brief-bulgaria-black-sea-merchant-ship-sunk-2026-10-14.md"
write_article(path, meta, body_cn)
print(f"Brief 2: {path}")

# --- BRIEF 3: Six Flags rollercoaster fatal + closures ---
title_cn = "[快讯] 美国六旗游乐园过山车事故致一人身亡 全国九台同类设施紧急停运"
title_en = "[Brief] Six Flags Rollercoaster Fatal Incident Prompts Closure of Nine Similar Rides Nationwide"

description_cn = "美国六旗游乐园旗下位于佐治亚州的一台过山车发生坠落事故致一人身亡，公司已紧急关闭全美其他九台同类设施配合调查。"
summary_cn = "美国六旗游乐园位于佐治亚州的一台过山车发生坠落事故致一人身亡，公司已紧急关闭全美其他九台同类过山车配合调查，警方初步调查显示事故可能涉及安全带失效。"

source = "BBC / CNN / AP News"
body_cn = """**[核心摘要]**

美国六旗游乐园位于佐治亚州的一台过山车发生坠落事故致一人身亡，公司已紧急关闭全美其他九台同类过山车配合安全调查，警方初步调查显示事故可能涉及安全约束装置失效。

**[事件详情]**

- **事故经过**：一名42岁男子在六旗旗下位于佐治亚州的主题公园乘坐过山车时从座椅坠落，送医后不治身亡。
- **目击者陈述**：现场目击者描述事故发生瞬间极为骇人，附近游客立即报警并协助救援。
- **公司响应**：六旗集团宣布暂时关闭全美其他九台同型号过山车接受安全审查，相关设施在调查结束前不会重新开放。
- **官方调查**：州政府监管机构已对事故启动正式调查，重点审查安全约束装置、维护记录与操作流程。

**[全景透视]**

此次致命事故折射出大型主题公园在客流压力与设备老化之间的安全管理挑战。在主题公园行业普遍追求更高、更快、更刺激的过山车设计的背景下，机械结构的复杂性与安全冗余之间的平衡日益受到关注。六旗集团的大规模停运决定虽然会对营收产生影响，但有助于防止类似事故再次发生，并恢复公众对游乐设施安全的信心。监管机构也可能借此事件推动全行业设备审查标准的升级。

*编辑：GoodInfo全球资讯组*
"""

meta = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_cn,
    "summary": summary_cn,
    "source": source,
    "categories": ["world"],
    "tags": ["美国", "六旗", "过山车", "安全事故", "国际动态", "社会时事"],
}

path = "/root/goodinfo-site/content/posts/world/brief-six-flags-rollercoaster-fatal-closure-2026-10-14.md"
write_article(path, meta, body_cn)
print(f"Brief 3: {path}")

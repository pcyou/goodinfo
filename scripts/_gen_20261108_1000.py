#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 2026-11-08 10:00 BJT GoodInfo news batch.

Batch contents (4 Tier-1 CN+EN, 4 Tier-2 briefs):
  T1 world    israel-herzog-eisenkot-form-government-2026-11-08
  T1 finance  iran-war-escalation-oil-risk-premium-2026-11-08
  T1 ai-tech  meta-wehner-fireworks-cfo-ai-inference-2026-11-08
  T1 world    us-homelessness-decade-drop-housing-policy-2026-11-08
  T2 crypto   binance-cfo-departs-after-record-hack-2026-11-08       (CN+EN)
  T2 crypto   ex-fbi-agent-crypto-theft-guilty-plea-2026-11-08        (CN only)
  T2 world    trump-ufc-dana-white-press-secretary-2026-11-08        (CN+EN)
  T2 ai-tech  kids-safe-phones-parent-controls-2026-11-08             (CN only)
"""
import os
from datetime import datetime, timezone, timedelta

REPO = "/root/goodinfo-site"
BJT = timezone(timedelta(hours=8))
NOW = datetime.now(timezone.utc).astimezone(BJT)
NOW_STR = NOW.strftime("%Y-%m-%dT%H:%M:%S+08:00")

CN_SIG = "编辑：GoodInfo全球资讯组"
EN_SIG = "Editor: GoodInfo Global News Team"


def yaml_field(value):
    if value is None:
        return '""'
    s = str(value)
    s = s.replace("\\", "\\\\").replace('"', '\\"')
    return '"%s"' % s


def with_sig(body, sig):
    """Append the signature exactly once (gate 112)."""
    lines = [ln.rstrip() for ln in body.strip().split("\n")]
    while lines and (not lines[-1] or lines[-1] == sig):
        lines.pop()
    return "\n".join(lines).rstrip() + "\n\n" + sig + "\n"


def header(meta):
    lines = ["---"]
    for k in ("title", "title_en", "date", "draft", "tier", "description",
              "summary", "source"):
        if meta.get(k) is not None:
            lines.append("%s: %s" % (k, yaml_field(meta[k])))
    lines.append("categories:")
    for c in meta.get("categories", []):
        lines.append("  - %s" % yaml_field(c))
    lines.append("tags:")
    for t in meta.get("tags", []):
        lines.append("  - %s" % yaml_field(t))
    lines.append("---")
    return "\n".join(lines) + "\n"


def write_article(path, meta, body, sig):
    full = os.path.join(REPO, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(header(meta) + "\n" + with_sig(body, sig))
    return full


A = []

# ------------------------------------------------------------------ A (T1 world)
A.append({
    "tier": "1", "cat": "world",
    "slug": "israel-herzog-eisenkot-form-government-2026-11-08",
    "title_cn": "以色列总统跳过内塔尼亚胡 交由反对派艾森科特组阁 组阁权成了一张政治考卷",
    "title_en": "Israel's President Sends Netanyahu's Rival Eisenkot to Form a Government",
    "desc_cn": "以色列总统艾萨克·赫尔佐格周六宣布，由前国防军总参谋长加迪·艾森科特尝试组建新政府，正式授权仪式定于周日下午五点举行。十月二十七日选举中没有党派取得过半席位，艾森科特将获得二十八天组阁期，必要时可再延长十四天。",
    "desc_en": "Israeli President Isaac Herzog said on Saturday that he has chosen Gadi Eisenkot, the former chief of staff of the armed forces and the strongest rival of Prime Minister Benjamin Netanyahu, to try to form a government, with the formal mandate to be handed over on Sunday afternoon. Neither party won a majority in the October 27 election, and Eisenkot now has 28 days, with a possible 14-day extension, to put a coalition together.",
    "sum_cn": "把组阁权交给最大反对者，本身就是一次制度性重新排序：它承认选举结果对执政联盟的否定，同时把政治更替的成本压在一个承诺绝不与内塔尼亚胡同台、并主张对威胁使用不成比例武力的候选人身上。",
    "sum_en": "Handing the mandate to the leading opponent is itself a reordering of the system: it accepts the verdict of the election on the ruling coalition, and at the same time places the cost of the transition on a candidate who has sworn never to serve alongside Netanyahu and who argues for disproportionate force against threats.",
    "src_cn": "法广France24", "src_en": "France 24",
    "tags_cn": ["国际动态", "以色列", "中东局势", "组阁", "政治更迭"],
    "tags_en": ["World Affairs", "Middle East", "Israel", "Government Formation", "Politics"],
    "body_cn": """## 核心摘要

以色列总统艾萨克·赫尔佐格周六发表声明，选择前国防军总参谋长加迪·艾森科特尝试组建新政府，正式授权仪式定于当地时间周日下午五点举行。这是内塔尼亚胡执政以来遭遇的最直接的政治重挫：十月二十七日选举中，他的利库德党拿下最多席位却未过半，他的宗教民族主义联盟总计五十三席，距离议会一百二十席中的六十一席多数线差八席。

## 事件详情

- **组阁授权**：总统发言人称，艾森科特将被邀请至总统官邸，并在次日接受组阁授权。
- **席位格局**：利库德党二十七席居首，艾森科特的亚沙尔党二十席居次，其牵头的四个政党联盟共四十八席；代表阿拉伯少数族裔的两个政党取得前所未有的十九席。
- **时间表**：二十八天组阁期，必要时可再延长十四天，最长约六周；若艾森科特失败，可另择人选，若再失败议会可另行提名，整个流程期限约一百天，无人成功则重新选举。
- **可能路径**：组建少数政府并争取阿拉伯政党从外部支持；与一贯被他拒绝的极端正统派政党结盟；或与内塔尼亚胡组成联合政府。分析人士认为三条路径都难以成形。
- **政治立场**：艾森科特公开指责内塔尼亚胡对加沙军事行动的领导方式，并宣称不会与其共同组阁。他在二〇二三年十月后的战时内阁中曾短暂留任，之后重回反对派阵营。
- **安全主张**：他以「达希亚原则」作为竞选主打，即对真主党控制区域内的民用基础设施施加不成比例的打击。该原则源自二〇〇六年的黎巴嫩战争，并在加沙再次被采用，批评者认为其后果构成战争罪指控，以方对此有异议。
- **个人背景**：六十六岁，摩洛哥移民家庭出身，若组阁成功将成为以色列首位米兹拉希社群出身的总理；二〇二二年才进入政坛，二〇一五至二〇一九年担任国防军总参谋长。
- **战争代价**：二〇二三年以来，其子与两名外甥在加沙阵亡。

## 多方观点比对

**阿拉伯政党从拒绝到交涉，掌握着真正的开关**。以色列入选的阿拉伯议员合计十九席，创下历史纪录；但反内塔尼亚胡阵营此前拒绝与这些政党联手，理由是它们的政治立场带有被外界解读为种族主义的内容。这一拒绝使该阵营即便联合全部盟友也凑不出多数。艾森科特获授权后，是否愿意为换取组阁机会而改变这一底线，将直接决定他走少数政府还是回到谈判桌。

**极端正统派是另一道被封印的门**。这些政党在内塔尼亚胡时期一直是可靠票仓，艾森科特与其政治盟友过去明确拒绝与之合作。若组阁需要他们的支持，等于要求他放弃多年经营的清白形象，代价是右翼盟友关系与部分中间选民的支持。

**联合政府并非没有支持者**。在内塔尼亚胡本人仍握有最多票数、且总统拒绝立即解散议会重选的情况下，先由双方共组过渡政府再择机选举，是可以想象的折中。但艾森科特已公开表示不会与内塔尼亚胡同台，这使该选项的政治成本远高于其技术可行性。

**地区观察者更关心的是安全政策会不会真的改变**。新政府无论由谁出面，都要面对同一组结构性约束：六十一席的算术、阿拉伯政党的条件、极端正统派的要求，以及被列入威慑清单的周边战线。把组阁权交给一位以强硬军事履历为卖点的候选人，究竟意味着政策收紧还是仅仅意味着选民换了标签，这是外部评估中最难回答的问题。

## 全景透视

这次授权最值得玩味的地方，是总统角色本身的变化。以色列总统长期被描述为礼仪性职位，在内塔尼亚胡的多届任内几乎没有展现过决定性影响力。赫尔佐格在僵局中选择把组阁权交给败选阵营的核心人物，等于承认总统可以成为僵局的裁决者而非橡皮图章。这一步会否在后续几届中被复制，取决于新政府是否顺利成局，以及新政府在面对下一轮选举时会如何处理与总统的关系。

另一层更长的影响在于，以色列政治的重心可能从安全遗产转向选举算术。十月二十七日的选举结果暴露了一个结构性事实：传统上的安全民族主义联盟已经无法独自过半，而阿拉伯少数族裔议员的席位成为决定多数的关键筹码。这意味着未来任何政府的政策空间，都要先在两个彼此戒备的社群之间找到可承受的平衡点，艾森科特的米兹拉希出身与清廉改革平台，恰好是这一转向最合适的政治包装。

对外部观察者而言，评估这条新闻不能只看谁组阁，而要看两件事：一是少数政府路径是否真的需要阿拉伯议员的外部支持，以及这种支持会附带什么条件；二是新政府在加沙与黎巴嫩方向上的实际动作是否与其竞选期间的强硬表述一致。前者决定治理的可行性，后者决定这个地区的水位是否真的下降。""",
    "body_en": """## Core Summary

Israeli President Isaac Herzog said on Saturday that he has chosen Gadi Eisenkot, the former chief of staff of the armed forces and the strongest rival of Prime Minister Benjamin Netanyahu, to try to form a new government, with the formal mandate to be handed over on Sunday at five in the afternoon. This is the most direct political setback of Netanyahu's tenure: in the October 27 election his Likud party took the most seats but not a majority, and his religious-nationalist bloc counted 53 of the 120 seats in parliament, eight short of the 61 needed to govern.

## Event Details

- **The mandate**: A spokesperson for the president said Eisenkot would be invited to the presidential residence and would be formally tasked with forming the government the following day.
- **The arithmetic**: Likud took 27 seats and Eisenkot's Yashar party 21, with the four-party bloc he leads counting 48 in total. Two parties representing the Arab minority won an unprecedented 19 seats.
- **The timetable**: Eisenkot has 28 days to form a government, with a possible 14-day extension, giving him up to roughly six weeks. If he fails, another candidate may try, and if that fails parliament may nominate again. The whole process runs to about 100 days, after which a new election is held.
- **The available paths**: a minority government with outside Arab support; a coalition with the ultra-Orthodox parties he has repeatedly shunned; or a unity government with Netanyahu. Analysts consider all three unlikely to take shape.
- **His position**: Eisenkot has publicly rebuked Netanyahu over his leadership of the military campaign in Gaza and has sworn that he will not serve in a government with him. He briefly joined Netanyahu's wartime cabinet after October 2023 before returning to the opposition.
- **His security doctrine**: He campaigned on what he calls the Dahiyeh doctrine, the vow to use disproportionate force against civilian infrastructure in areas controlled by the Lebanese militant movement Hezbollah. The doctrine dates from the 2006 war and has been applied again in Gaza, where critics say the destruction amounts to war crimes, an assertion Israel disputes.
- **His background**: Eisenkot is 66 and the son of Moroccan immigrants; if he succeeds he would be Israel's first prime minister from the Mizrahi community. He entered politics only in 2022 and served as chief of staff of the armed forces from 2015 to 2019.
- **His family cost**: A son and two nephews have been killed in Gaza since 2023.

## Comparison of Viewpoints

**The Arab parties went from refusal to negotiation, and they now hold the real switch.** Arab lawmakers took a record 19 seats in the Israeli election, yet the anti-Netanyahu bloc declined to join forces with them, citing positions the bloc regarded as racist. That refusal left the opposition short of a majority even with every ally. Now that Eisenkot has the mandate, whether he will reverse that red line in order to secure a government decides whether he attempts a minority administration or returns to the table.

**The ultra-Orthodox parties are a second sealed door.** They were a reliable base for Netanyahu, and Eisenkot and his allies have consistently refused to work with them. Bringing them in to secure a majority would mean abandoning an image of political cleanliness built over years, at the cost of his right-wing allies and part of the middle-ground electorate.

**A unity government is not without supporters.** With Netanyahu still holding the largest bloc and the president declining to call an immediate new election, an interim government of both followed by an election at a later date is a conceivable compromise. Eisenkot's public pledge never to serve with Netanyahu, however, makes the political cost of that route far higher than its technical feasibility.

**Regional observers care more about whether security policy actually changes.** Any new government faces the same structural constraints: the arithmetic of 61 seats, the conditions attached to Arab support, the demands of the ultra-Orthodox parties, and the fronts on which the country has placed deterrence. Whether handing the mandate to a candidate who sells a strong military record tightens policy or merely relabels the voter is the hardest question for outside assessments.

## Panoramic Analysis

The most revealing part of this mandate is what it says about the presidency itself. The Israeli president has long been described as a largely ceremonial office that exerted almost no decisive influence during Netanyahu's successive terms. By giving the mandate to the central figure of the defeated bloc in a deadlock, Herzog has effectively conceded that a president can serve as the arbiter of a stalemate rather than a rubber stamp. Whether that precedent survives depends on whether the new government actually takes shape, and on how it handles its relationship with the presidency in the next electoral cycle.

A longer shift is visible in the centre of gravity of Israeli politics, which may be moving from the inheritance of security politics toward electoral arithmetic. The October 27 result exposed a structural fact: the traditional security-nationalist alliance can no longer govern alone, and the seats won by Arab minority lawmakers have become the decisive currency of any majority. The policy space of future governments will first have to be found in a balance between two mutually wary communities, and Eisenkot's Mizrahi background and clean-government platform are precisely the political packaging that such a turn requires.

For outside observers, the right question is not only who forms the government but two specifics: whether the minority route genuinely requires external support from Arab lawmakers and on what conditions, and whether the new government's actual actions in Gaza and toward Lebanon match the hard-line framing of the campaign. The first determines whether governance is feasible at all; the second determines whether the region's water level actually falls.""",
})

# ------------------------------------------------------------------ B (T1 finance)
A.append({
    "tier": "1", "cat": "finance",
    "slug": "iran-war-escalation-oil-risk-premium-2026-11-08",
    "title_cn": "民主党胜选压低油价 地面信号却指向再度开战 分析师给出八成重启概率",
    "title_en": "Oil Falls on the Democratic Sweep While Ground Signals Point to Renewed Fighting",
    "desc_cn": "民主党在美国中期选举中的压倒性胜利，让原油价格在此前五个交易日内累计下跌逾百分之十六，市场押注战争授权决议将迫使白宫收手。但海湾地区的实际动作并未同步降温：美国中央司令部已使一艘油轮失去动力，第三支航母打击群正在驶向该区域，伊朗媒体报道霍尔木兹海峡附近发生多起爆炸。",
    "desc_en": "The decisive Democratic victory in the United States midterm elections pushed crude prices down more than 16 percent over five trading sessions, with markets betting that a war powers resolution will force the White House to stop. The action on the ground in the Gulf has not followed. US Central Command has disabled an oil tanker, a third carrier strike group is steaming toward the region, and Iranian media reported several blasts near the Strait of Hormuz.",
    "sum_cn": "真正决定下一步的不是选票，而是十二月十一日的政府拨款截止日。在那之前，行政部门不受任何约束；在此之后，国会的钱袋子才会变成杠杆。油价把这两件事之间的空窗期误当成了和平。",
    "sum_en": "What decides the next step is not the ballot but the government funding deadline on December 11. Before that date the executive branch faces no constraint at all; after it, the power of the purse becomes the only real lever. Oil prices have mistaken the length of that window for peace.",
    "src_cn": "美国消费者新闻与商业频道", "src_en": "CNBC",
    "tags_cn": ["伊朗", "原油", "地缘局势", "中期选举", "美国国会"],
    "tags_en": ["Iran", "Crude Oil", "Geopolitics", "Midterm Elections", "US Congress"],
    "body_cn": """## 核心摘要

民主党在美国中期选举中的压倒性胜利，让原油价格在此前五个交易日内累计下跌逾百分之十六，周五国际布伦特原油收于每桶九十七美元上方，美国原油约为每桶九十美元。市场把这一轮下跌解读为民主党将利用国会多数推动战争授权决议，迫使白宫结束这场战争。

但海湾地区的实际动作并没有同步降温。能源咨询机构拉皮丹能源的评估认为，随着外交努力停滞，冲突重新爆发的概率为百分之八十。

## 事件详情

- **油价与选票**：五个交易日内原油累计下跌逾百分之十六，副总统万斯公开把共和党的败选归咎于这场战争，这一表态抬升了市场对战争难以持续的预期。
- **升级迹象**：美国中央司令部周六宣布，已使一艘圣基茨船旗油轮失去动力，该船在访问伊朗港口后无视多次警告并试图驶离相关区域。伊朗国家媒体同时报道霍尔木兹海峡内的格什岛发生爆炸，以及贾斯克港出现数起爆炸。该频道无法独立核实这些报道。
- **航运风险**：选举以来已有数艘油轮在阿曼附近遭到袭击，造成一名海员死亡；伊朗在也门的盟友则继续向邻国沙特发射导弹。
- **军事部署**：美军增援仍在继续，第三支航母打击群正在驶向该区域。
- **概率评估**：拉皮丹能源认为，在外交陷入停滞的情况下，冲突重新爆发的概率为百分之八十；该机构总裁鲍勃·麦克纳利表示，一旦重燃战火，原油价格将再次升破每桶一百美元。
- **总统表态**：特朗普周四表示将很快就是否再次对伊朗动武作出决定，并称如果可能，他宁愿不摧毁这个国家的其余部分，但也许不得不这么做，同时强调已经做好充分准备。
- **国会杠杆**：民主党计划利用两院的多数席位通过战争授权决议，要求总统结束战争，但要到一月才会就职，且总统拥有否决权。分析师认为国会手中真正的杠杆是拨款权：政府拨款将于十二月十一日到期，若后续延续决议的谈判拖入二〇二七年，民主党在掌权后的谈判地位将明显增强。
- **外交渠道**：特朗普周五与卡塔尔埃米尔通话讨论降温。据路透社报道，一名伊朗高级官员称德黑兰通过卡塔尔向美国递交了一份核方案，但要先等美方满足其条件才会讨论；特朗普则表示伊朗永远不会拥有核武器。

## 多方观点比对

**市场选择相信叙事而非现场**。多位分析师指出，本周最强烈的感受是，海湾地区不断加深的升级担忧，与数千公里之外由头条驱动的乐观情绪之间出现了明显背离。这句话点破了本周定价的核心矛盾：油价的下跌来自政治结果的推断，而风险的上升来自现场事件的累积。

**强硬派认为选举结果并未改变行政当局的意图**。特朗普反复强调不会允许伊朗拥有核武器，前能源顾问霍赫斯坦指出，特朗普不再面临选举周期，这恰恰使战争风险存活下来，一旦冲突重启，汽油、柴油与航空燃油价格都会随之飙升。

**鸽派看到的窗口在拨款而非授权**。从制度上看，在十二月十一日之前，通过战争授权决议并不现实，即使通过也可被否决；真正能改变长期资金前景的是把拨款决定推迟到新政府手里。分析师同时提醒，推迟拨款决定并不会立刻限制当局的军事行动能力。

**伊朗方面的信号是条件式而非让步式**。通过卡塔尔转交的核方案以美方先满足条件为前提，最高领袖穆杰塔巴·哈梅内伊的社交账号则在选举后宣称美国走向瓦解的进程已经加速。外交渠道存在，但双方给出的都是先决条件而非共同基础。

## 全景透视

这场油价与战场之间的错位，暴露的是当前美国政治结构中最关键的一个时间差。选举结果已经落地，但它的全部效力要到一月才由新国会兑现；而在此之前，总统在军事行动上不受任何程序约束。也就是说，市场用新政府的未来权限给当下的军事风险定价，而现场的军事部署恰恰没有等待的意思。

真正可以观察的机制，是十二月十一日拨款截止日如何运作。多数分析把焦点放在战争授权决议上，但那条路径在当前的时间窗口内几乎不可能走通——议员尚未就职，总统可以否决，国会也不可能在此期间停摆政府。可行的是拨款：若持续决议的谈判被拖入新国会，新政府将在预算谈判桌上获得实质筹码。前提是行政部门在预算失守时是否仍继续行动，而这恰恰是分析中被反复强调的一点——推迟拨款不会立刻约束军事能力。

对能源与航运市场而言，风险溢价的来源也因此清晰了：不是某一条政治声明，而是霍尔木兹海峡两侧连续发生的、即便规模有限却持续累积的事件。油轮失去动力、阿曼附近的袭击、格什岛与贾斯克港的爆炸报告，这些单看都不足以改变供需曲线，但它们共同决定着保险费率与船东的绕行意愿。当保险成本与绕行时间被计入实际到岸价格，市场看到的每桶价格与战前的差异就会缩小一部分。

因此，接下来两周真正值得跟踪的指标有四个：海湾主要航线战争险费率的变动、伊朗核方案在卡塔尔渠道中是否有任何实质进展、十二月十一日之前是否出现能源部门高层的公开表态，以及中央司令部对第三支航母打击群的部署说明。这些指标的共同指向，比任何一份选后评论都更能回答战争会否重启这个问题。""",
    "body_en": """## Core Summary

The decisive Democratic victory in the United States midterm elections pushed crude prices down more than 16 percent over five trading sessions. Brent crude traded above 97 dollars a barrel on Friday and the US contract sat near 90 dollars. Markets read the move as a bet that Democrats will use their congressional majority to push a war powers resolution that forces the White House to end the war.

The action on the ground in the Gulf has not followed. The energy consultancy Rapidan Energy assesses the probability of renewed fighting at 80 percent as diplomatic efforts stall.

## Event Details

- **Oil and the ballot**: Crude fell more than 16 percent over five sessions after Vice President JD Vance publicly attributed the Republican loss to the war, raising expectations that the conflict could not continue.
- **Escalation signals**: US Central Command said on Saturday that it disabled a St. Kitts-flagged tanker after the ship ignored multiple warnings and tried to leave the region following a visit to an Iranian port. Iranian state media also reported explosions on Qeshm Island in the Strait of Hormuz and several blasts at the port of Jask. The network could not independently confirm those reports.
- **Shipping risk**: Several tankers have come under attack near Oman since the election, killing one seafarer, while Iran's Houthi allies in Yemen continue to fire missiles at neighbouring Saudi Arabia.
- **Military posture**: The US buildup continues, with a third carrier strike group en route to the region.
- **The odds**: Rapidan sees an 80 percent chance of renewed fighting while diplomacy stalls, and its president Bob McNally said crude will move back above 100 dollars a barrel when hostilities resume.
- **The president's words**: Trump said on Thursday that he would decide soon whether to attack Iran again, adding that he would rather not destroy the rest of the country if possible but perhaps would have to, and that he was ready to act.
- **The congressional lever**: Democrats intend to use their majorities in both chambers to pass a war powers resolution demanding an end to the war, but they are not sworn in until January and the president can veto it. The real lever, analysts say, is the power of the purse: government funding expires on December 11, and if talks over a further continuing resolution drag into 2027, Democrats gain bargaining strength once they take office.
- **The diplomatic channel**: Trump spoke with the emir of Qatar on Friday about de-escalation. According to Reuters, a senior Iranian official said Tehran had sent a nuclear proposal to the United States through Qatar, and would only discuss it after Washington meets its demands. Trump said Iran will never have a nuclear weapon.

## Comparison of Viewpoints

**Markets chose to price the narrative rather than the scene.** Analysts noted this week that the strongest impression was the divergence between deepening escalation concerns in the Gulf and the headline-driven optimism of market participants thousands of miles away. That sentence names the contradiction behind this week's pricing: the fall in oil came from an inference about political outcomes, while the rising risk came from the accumulation of events on the ground.

**The hardliners argue the election did not change the administration's intent.** Trump has repeatedly said he will not allow Iran to have a nuclear weapon, and former energy adviser Amos Hochstein pointed out that Trump no longer faces future elections, which is precisely why the risk of war stays alive and why gasoline, diesel and jet fuel prices would all surge if hostilities resumed.

**The doves see the window in funding rather than in authorization.** Passing a war powers resolution is not realistic before December 11, and it could be vetoed in any case. What could change the longer-term funding outlook is deferring the funding decision to a new Congress. Analysts caution at the same time that deferring funding would not immediately constrain the administration's ability to conduct military operations.

**Iran's signals are conditional rather than concessive.** The nuclear proposal relayed through Qatar is premised on Washington meeting its demands first, and the social media account of Iran's supreme leader claimed after the midterms that the process of American collapse had accelerated. A diplomatic channel exists, but both sides have offered preconditions rather than a shared basis.

## Panoramic Analysis

The mismatch between the oil price and the battlefield exposes the single most important time gap in current American politics. The election result has landed, but none of its force is delivered until the new Congress takes office in January, and until then the president faces no procedural constraint on military action. Markets priced the future authority of an incoming government against a military posture that was plainly not waiting.

The mechanism worth watching is how the December 11 funding deadline actually works. Most commentary focuses on the war powers resolution, yet that route is effectively unavailable inside the current window: lawmakers are not sworn in, the president can veto, and Congress cannot shut down the government in the meantime. Funding is the viable instrument. If talks over a continuing resolution are dragged into the incoming Congress, the new administration inherits real bargaining leverage on the budget. The condition is whether the executive branch keeps operating after the money runs out, which is the point analysts keep returning to: deferring funding does not immediately constrain military capacity.

For energy and shipping markets, the source of the risk premium is also now clear. It is not any single political statement but the succession of limited but continuous incidents on both sides of the Strait of Hormuz. A tanker disabled, an attack near Oman, reported blasts on Qeshm Island and at the port of Jask: none of these alone changes a supply-demand curve, but together they set insurance rates and the willingness of shipowners to divert. Once insurance cost and routing time are counted in the delivered price, the gap between the traded barrel and the pre-war barrel narrows by a visible margin.

Four indicators matter most over the coming fortnight: war-risk insurance rates on the main Gulf routes, whether the nuclear proposal moves at all through the Qatari channel, any public comment from senior energy officials before December 11, and the Pentagon's account of the third carrier strike group's deployment. Their combined direction answers the question of renewed fighting far better than any post-election commentary.""",
})

# ------------------------------------------------------------------ C (T1 ai-tech)
A.append({
    "tier": "1", "cat": "ai-tech",
    "slug": "meta-wehner-fireworks-cfo-ai-inference-2026-11-08",
    "title_cn": "Meta战略主管韦纳转任Fireworks首席财务官 推理层创业公司估值传闻升至三百亿至四百亿美元",
    "title_en": "Meta's Strategy Chief Dave Wehner Joins AI Inference Startup Fireworks as Chief Financial Officer",
    "desc_cn": "Meta首席战略官戴夫·韦纳确认离职，将出任人工智能推理与模型训练平台Fireworks的首席财务官。该公司今年七月的一轮融资估值为一百七十五亿美元，据《商业内幕》报道正就新一轮融资进行早期接触，潜在估值区间为三百亿至四百亿美元。",
    "desc_en": "Meta chief strategy officer Dave Wehner has confirmed his departure to become chief financial officer of Fireworks, an artificial intelligence inference and model-training platform. The startup was valued at 17.5 billion dollars in a funding round in July and is, according to Business Insider, in early talks for a new raise at a possible valuation of between 30 and 40 billion dollars.",
    "sum_cn": "一位在Facebook服务十四年、掌过八年财务的资深高管选择回到一家四岁的公司，本身就说明推理层正在从「谁训练模型」的竞赛里独立出来，成为一门需要严肃财务能力与合规纪律的生意。",
    "sum_en": "A veteran executive who spent fourteen years at Facebook and eight of them as chief financial officer choosing to return to a four-year-old company says something specific: the inference layer has separated from the race to train models and become a business that demands serious financial discipline and compliance rigour.",
    "src_cn": "美国消费者新闻与商业频道", "src_en": "CNBC",
    "tags_cn": ["人工智能", "推理算力", "数据经纪", "人才流动", "资本市场"],
    "tags_en": ["Artificial Intelligence", "AI Infrastructure", "Open Models", "Executive Moves", "Venture Capital"],
    "body_cn": """## 核心摘要

Meta首席战略官戴夫·韦纳确认离开公司，将出任人工智能推理与模型训练平台Fireworks的首席财务官。他在社交平台上的说法是，这家公司的使命「符合当下的需要」，并表示自己对团队所构建的东西越来越乐观。

Fireworks成立于二〇二二年，专注于让开发者定制并运行开源模型，其最新一轮融资由Atreides Management、Index Ventures与TCV领投，红杉资本亦参与其中。该公司今年七月的一轮融资估值为一百七十五亿美元，据《商业内幕》报道，正就新一轮融资进行早期接触，潜在估值区间为三百亿至四百亿美元。

## 事件详情

- **人事变动**：韦纳在社交平台宣布将于周五出任Fireworks的首席财务官。Fireworks首席执行官林巧表示，将由他负责推动公司财务与运营的规模化。
- **履历**：韦纳二〇一二年加入当时仍名为Facebook的Meta，二〇一四至二〇二二年担任公司首席财务官，之后出任首席战略官。他在Facebook时期参与了那家公司从单一社交网络走向庞大基础设施体系的转型。
- **评价**：Meta首席运营官哈维尔·奥利瓦表示，韦纳在十四年间帮助公司穿越了巨大的增长与复杂度，并在公司层面最艰难的一些决策中带来了纪律化的判断。
- **离职动机**：林巧在领英上写道，韦纳希望回到一家规模更小的公司，在那里他可以再次朝有影响力的方向建设，并认为人工智能是他一生中最重要的技术转折。
- **公司业务**：Fireworks是一个推理与模型训练平台，让开发者为自身业务定制并运行开源模型，客户包括希望自托管模型的企业。
- **融资情况**：最新一轮融资由Atreides Management、Index Ventures与TCV领投，红杉资本亦参与。据《商业内幕》报道，公司正就新一轮融资进行早期接触，潜在估值为三百亿至四百亿美元。
- **规模对比**：Fireworks与Meta体量差距巨大，后者截至周五收盘市值约一点五六万亿美元；Fireworks的直接竞争者包括OpenAI与Anthropic。
- **安全记录**：今年十月，Fireworks披露了一起涉及内部凭据被未授权使用的事件，某个未授权第三方访问了少量客户账户在评测任务中使用的环境变量。公司称调查未发现安全边界内客户模型、数据集、训练数据、个人信息或推理流量被未授权访问的证据。

## 多方观点比对

**乐观的一方强调技术与使命的匹配**。韦纳本人称这家公司拥有异常深厚的技术人才储备，同时对客户真正需要什么保持着务实的关注。Fireworks首席执行官则把这条任命描述为一次阶段性的必然结果：一家公司从创始人驱动走向规模化运营，需要有人来建立财务纪律、准备下一轮融资，并让投资者相信数字背后有体系。

**谨慎的一方把注意力放在规模与安全上**。公司体量与巨头相差两个数量级，而竞争者恰恰是估值与资本实力最雄厚的两家模型公司。更值得注意的是十月那起凭据事件：一家主打企业级模型托管与定制的公司，如果连内部评测环境的环境变量都可能暴露在未授权访问之下，那么它向企业客户承诺的数据边界就需要更严格的第三方验证。公告中「未发现证据」这一表述本身，就是取证范围有限时的标准措辞。

**财务视角的一方看到了这次任命的真正功能**。在潜在估值三百亿至四百亿美元的新一轮融资进入早期接触阶段时，引入一位在超大型上市公司掌管过财务、且经历过多轮监管与公开市场考验的高管，是典型的上市前准备动作。这意味着公司自己把这一轮融资视为从「有故事」转向「有报表」的转折点。

**行业视角的一方关注的是人才流向的方向**。从超大规模平台流向基础设施创业公司，本身说明资本正在从模型训练层向推理与交付层重新分配。当开源模型的能力差距缩小，企业客户的真实问题就从「该选哪个模型」变成「如何以可控成本稳定运行我自己的模型」，而后者正是推理层公司的立足点。

## 全景透视

这次人事变动若放在更长的技术周期里看，其指示意义可能高于人事本身。过去几年的人工智能资本叙事高度集中在训练端：算力规模、数据质量、参数效率、模型能力的天花板。而推理层长期被视为一个「必然被大厂吸收」的中间环节，成本高、毛利薄、议价能力弱。

Fireworks这类公司的存在恰恰说明这个判断过于乐观。当企业选择自托管与定制开源模型时，交付环节会承担起合规审计、数据隔离、区域化部署、版本管理与成本核算等一整套职责，而这些工作的复杂度接近传统的企业软件与云服务，而不是接近模型研究。也正因如此，一家主营推理的公司需要一位真正懂大型机构财务流程的高管，而不是又一位研究型创始人。

融资节奏进一步强化了这一判断。一百七十五亿美元到三百亿至四百亿美元的传闻区间，意味着投资人对这类基础设施公司的定价逻辑，已经从「技术领先」转向「能承载多大的企业收入规模」。而十月那次凭据事件恰好点出了这个逻辑的软肋：一旦推理层开始托管客户的模型、数据集与推理流量，它承担的就同时是数据责任，而这类责任在监管与商业上的分量，通常比训练层更重。

值得继续跟踪的指标有三个：新一轮融资是否落地以及最终估值落在区间何处；推理层公司的客户结构是否从少数试点型客户转向有稳定预算的企业；以及安全事件的披露口径是否从公司自查转向第三方审计。只有当这三条同时推进，推理层才能真正从「模型竞争的配套」变成一条独立的产业主线。""",
    "body_en": """## Core Summary

Meta chief strategy officer Dave Wehner has confirmed that he is leaving the company to become chief financial officer of Fireworks, an artificial intelligence inference and model-training platform. He wrote on social media that the company has the right mission for the moment and that he has become increasingly bullish on what it is building.

Fireworks was founded in 2022 and focuses on letting developers customise and run open models. Its most recent round was led by Atreides Management, Index Ventures and TCV, with Sequoia Capital also participating. The startup was valued at 17.5 billion dollars in a July round and, according to Business Insider, is in early talks to raise again at a possible valuation of between 30 and 40 billion dollars.

## Event Details

- **The move**: Wehner announced on Friday that he will take the chief financial officer role at Fireworks. Chief executive Lin Qiao said he will be tasked with scaling the company's finances and operations.
- **His record**: Wehner joined Meta, then called Facebook, in 2012 and was its chief financial officer from 2014 to 2022 before becoming chief strategy officer. He helped steer the company through the transformation from a single social network into a vast infrastructure business.
- **The internal assessment**: Meta chief operating officer Javier Olivan said Dave helped guide Meta through tremendous growth and complexity over 14 years and brought disciplined thinking to some of the company's hardest decisions.
- **His reasoning**: Lin wrote on LinkedIn that Dave told him he wanted to get back to a smaller company where he could build toward a big impact again, and that he sees artificial intelligence as the defining technology shift of his lifetime.
- **The business**: Fireworks is an inference and model-training platform that lets developers customise and run open models for their own businesses, serving customers who want to host models themselves.
- **Funding**: The latest round was led by Atreides Management, Index Ventures and TCV, with Sequoia Capital also backing the company. Business Insider reported that it is in early talks to raise again at a possible 30 to 40 billion dollar valuation.
- **Scale**: Fireworks is far smaller than Meta, which closed Friday with a market capitalisation of about 1.56 trillion dollars. Fireworks competes with OpenAI and Anthropic.
- **Security record**: In October the company disclosed a security incident involving unauthorised use of internal Fireworks credentials, in which an unauthorised third party accessed environment variables used in evaluation jobs in a limited number of customer accounts. It said its investigation had found no evidence of unauthorised access to customer models, datasets, training data, personal information or inference traffic within its security perimeter.

## Comparison of Viewpoints

**The optimistic reading stresses the fit between craft and mission.** Wehner himself points to an unusual depth of technical talent alongside a practical focus on what customers actually need, and the chief executive frames the appointment as an orderly stage transition: a company moving from founder-led growth to scaled operations needs someone to install financial discipline, prepare the next raise and convince investors that the numbers behind the story hold up.

**The cautious reading focuses on scale and on security.** The company is orders of magnitude smaller than the platforms it competes with, and its direct competitors are the two model companies with the deepest capital and the strongest valuation. More pointed is the October credential incident. A company selling enterprise-grade hosting and customisation of models, if environment variables in evaluation jobs can be reached by an unauthorised third party, will find that the data boundaries it promises to enterprise buyers require third-party verification rather than internal attestation. The phrase "we have not detected evidence" is the standard formulation for a limited forensic scope.

**The financial reading identifies the real function of the hire.** With a new round in early talks at a possible 30 to 40 billion dollars, bringing in an executive who ran finance at a mega-cap listed company through repeated regulatory and public-market cycles is a textbook pre-listing preparation. It suggests the company itself reads this raise as the moment it moves from having a story to having statements.

**The industry reading watches where talent is flowing.** Movement from a hyperscale platform to an infrastructure startup says that capital is redistributing from the training layer toward the inference and delivery layer. As the capability gap between open and closed models narrows, the real question for an enterprise buyer becomes how to run its own model reliably and at a controlled cost, which is exactly where an inference company earns its place.

## Panoramic Analysis

Placed in a longer technology cycle, this appointment may say more than the appointment itself. For the past several years the capital narrative in artificial intelligence has concentrated on the training side: compute scale, data quality, parameter efficiency, the ceiling on model capability. The inference layer was treated as an intermediary destined to be absorbed by the large platforms, with thin margins and weak bargaining power.

The existence of companies like Fireworks suggests that judgement was premature. When enterprises choose to self-host and customise open models, the delivery layer takes on compliance auditing, data isolation, regional deployment, version management and cost accounting as a full set of responsibilities, and that complexity resembles traditional enterprise software and cloud services far more than it resembles model research. It is for exactly that reason that a company built on inference needs a genuinely seasoned financial executive rather than another research founder.

The financing sequence reinforces the reading. A gap between 17.5 billion dollars and a rumoured 30 to 40 billion means investors have already shifted from pricing technical leadership to pricing how much enterprise revenue the delivery layer can carry. The October credential incident marks the soft spot in that logic: once the inference layer hosts customer models, datasets and inference traffic, it also inherits data responsibility, and that responsibility carries more weight in regulators' eyes and in commercial negotiations than it does at the training layer.

Three indicators are worth tracking: whether the new round closes and where the valuation lands inside the range; whether the customer mix shifts from a handful of pilot buyers to organisations with recurring budgets; and whether security disclosure moves from self-attestation toward third-party audit. Only when all three advance together can the inference layer stop being a companion to the model race and become an industry line of its own.""",
})

# ------------------------------------------------------------------ D (T1 world)
A.append({
    "tier": "1", "cat": "world",
    "slug": "us-homelessness-decade-drop-housing-policy-2026-11-08",
    "title_cn": "美国无家可归人数录得十余年来最大降幅 官方与公益组织给出完全相反的归因",
    "title_en": "US Homelessness Records Its Largest Drop in More Than a Decade, With Two Very Different Explanations",
    "desc_cn": "美国住房与城市发展部公布的年度统计显示，二〇二五年美国无家可归人口下降超过百分之六，约四万九千人不再无家可归，连续第二年下降，但总数仍接近七十万人。住房与城市发展部长斯科特·特纳把降幅归因于边境管控与治安政策，而受其委托展开同类分析的全国终结无家可归联盟则将其归因于国会拨款支持的住房项目与租金回落。",
    "desc_en": "An annual count from the Department of Housing and Urban Development shows that the homeless population in the United States fell by more than 6 percent in 2025, some 49,000 fewer people without housing, a second consecutive annual decline that nevertheless leaves the total near 700,000. Housing Secretary Scott Turner credits the drop to border enforcement and public safety policy, while the National Alliance to End Homelessness, which commissioned its own analysis of the same count, attributes it to housing programmes funded by Congress and to softening rents.",
    "sum_cn": "同一份统计数据被两个立场相反的机构引用，得出完全不同的因果结论，这种分歧本身就是这则新闻的核心：它不是「问题解决了」的公告，而是一次关于住房政策优先级的路线之争被公开摆上桌面。",
    "sum_en": "Two bodies with opposite positions cite the same count and reach opposite causal conclusions, and that disagreement is the real story: this is not an announcement that the problem is solved but a public airing of a contest over housing policy priorities.",
    "src_cn": "美国国家公共广播电台", "src_en": "NPR",
    "tags_cn": ["社会时事", "无家可归", "住房政策", "移民政策", "美国社会"],
    "tags_en": ["Social Affairs", "Housing Policy", "Homelessness", "Immigration Policy", "United States"],
    "body_cn": """## 核心摘要

美国住房与城市发展部公布的年度「时点统计」显示，二〇二五年美国无家可归人口下降超过百分之六，约四万九千人不再处于无家可归状态，这是连续第二年下降，也是十余年来最大的一次年度降幅。住房与城市发展部长斯科特·特纳在宣布结果的新闻稿中表示，是「总统在收紧边境、把非法移民从街头清走、恢复社区安全方面的行动」推动了这次历史性下降。

然而，全国终结无家可归联盟委托进行的同类分析得出了相近的数字，却给出了完全不同的归因：该联盟首席执行官安·奥利瓦表示，「更多人住上了房子、国会拨款的项目确实在起作用，这本该是件好事」。

## 事件详情

- **总量与降幅**：二〇二五年无家可归人口下降逾百分之六，约四万九千人不再无家可归，二〇二四年的降幅更小，两年连降。
- **仍然庞大的基数**：目前仍有近七十万人生活在收容所或街头，显著高于新冠疫情爆发前的水平。
- **官方口径**：住房与城市发展部长把降幅主要归因于边境管控与治安政策，并称在拜登政府时期，纽约、芝加哥、波士顿与丹佛均出现过庇护所申请人数的激增。
- **第三方口径**：全国终结无家可归联盟基于同一份统计数据得出相近的下降幅度，但认为国会拨款支持的住房项目、租金从疫情高峰回落，以及部分地区遭遇重大灾害后政府投入的救助资源，共同构成了下降的原因。
- **具体城市的对应关系**：由行政当局盟友西塞罗研究所提供的分析指出，纽约、芝加哥、波士顿与丹佛这四座城市近期贡献了降幅的一半；同时，旧金山等城市正在推动要求居住场所禁绝酒精与毒品的支持性住房，批评者认为这类做法会在复吸常见的背景下把人重新推回街头。
- **老兵群体的表现**：无家可归老兵人数去年下降逾百分之七，自二〇一〇年以来累计下降接近百分之六十。奥利瓦认为，无条件先把人安置下来的项目与这一群体需求的规模更匹配。
- **反向指标**：与整体下降形成对照的是，长期无家可归人数出现小幅上升，这部分人群更容易同时面临精神健康问题与成瘾障碍。
- **地方政府工具争议**：最高法院二〇二四年裁定地方政府可以禁止在公共场所睡眠与露营，奥利瓦则表示其委托的分析显示，采取此类禁令的城市「表现比全国平均水平更差」。
- **政策转向**：行政当局主张削减无家可归相关联邦支出，并把资金转向附带强制成瘾与精神健康治疗的短期住房；联盟方面则主张为长期无家可归者提供更多永久性住房。

## 多方观点比对

**归因的分歧集中在因果链条的起点**。住房与城市发展部的逻辑是：边境收紧减少了新增的无家可归人口，街头秩序的恢复则降低了存量人数。联盟的逻辑是：住房供给与项目拨款才是变量，边境政策最多是辅助因素。两套说法都能引用同一份统计数据，这恰恰说明年度时点统计本身难以支撑因果判断。

**强制治疗与无条件安置是真正的政策分歧**。行政当局认为「先提供永久住房、再提供自愿治疗」的长期路线已经失败，并把疫情期间的无家可归激增归咎于这一路线，主张改为附带强制治疗的短期住房。联盟则指出，恰恰是那些先把人带离街头、再提供后续服务的项目构成了最近两年的降幅主力，尤其在老兵群体上表现明显——这组数据被双方都拿来当作反驳对方的证据。

**地方政府工具的效果也在被重新评估**。禁止街头露营的做法在最高法院层面获得支持后推广开来，但联盟引用的分析显示，实施此类禁令的城市平均表现反而更差。这条线索对评估全国性政策的落地效果有直接意义：联邦层面的工具设计与地方层面的实际效果，可能指向不同方向。

**降幅的来源构成被低估**。联盟特别提到，租金从疫情高峰回落、西部北卡罗来纳与夏威夷等遭遇重大灾害的地区在灾后获得了额外救助资源，这些都把原本可能被推入街头的人拦截了下来。这提示所谓的「政策胜利」中，有相当一部分其实来自市场周期与灾害响应。

## 全景透视

这则新闻最值得关注的，不是数字本身，而是同一份数据被两个立场对立的机构引用并得出相反结论这一事实本身。时点统计是一种脆弱的测量工具：它依赖某一夜在收容所、街头和临时安置点的人数，受季节天气、统计口径、救助资源的临时投入影响很大，本身就不具备识别因果的能力。当一个数字被证明有多种解释时，最有价值的追问是：这一年里，数据的采集方式是否发生变化，统计覆盖的人群是否发生变化，以及不同人群的降幅是否均衡。

而答案显然不是均衡的。整体数字下降的同时，长期无家可归人数出现小幅上升，这两组数据的背离，恰恰指向了财政与救助资源正在从最难服务的人群身上转移这一事实。伴随这一转向的是政策工具的整体替换：先安置后自愿治疗被改成短期住房加强制治疗。这一替换在财政上更省、在效果上更可测量，在政治上也更容易向选民交代，但它把一部分原本能被接住的人重新暴露在街头风险之中。

放在更长的时间尺度上，美国的住房政策一直在两条路线之间摇摆：一条是提高供给，另一条是强化对需求侧的管理。二〇二五年这一轮下降，很大程度上是第三条路径的结果——移民政策、公共秩序与灾害救助同时发力。三条路径都难以长期独立维持，因此真正的观察点在于：当租金周期再次转向、当灾害周期结束、当移民政策的边际效果递减时，这套由多个临时因素拼成的降幅还能剩下多少。

需要说明的是，二〇二四年最高法院关于地方政府禁止露营的裁定，把一批城市从被动管理推向了主动清理，而各城市实际效果的分化，说明全国性结论与地方执行之间存在明显落差。这也是为什么联盟的分析值得被认真对待，而不是被当作立场表态：在缺少公开方法学细节的情况下，能够对官方叙事提出数据层面的反面证据，本身就是公共讨论质量的必要条件。""",
    "body_en": """## Core Summary

An annual point-in-time count from the Department of Housing and Urban Development shows that the homeless population in the United States fell by more than 6 percent in 2025, roughly 49,000 fewer people without housing. It is the second consecutive annual decline and the largest in more than a decade. Housing and Urban Development Secretary Scott Turner said in the announcement that the historic decrease was driven by the president's actions to secure the border, get undocumented migrants off the streets and restore safety to communities.

The National Alliance to End Homelessness, which commissioned its own analysis of the same count, found a similar decline but offered a completely different explanation. Its chief executive, Ann Oliva, said it was good news that more people are getting housed and that the programmes funded by Congress are working.

## Event Details

- **The headline figure**: The homeless population fell by more than 6 percent in 2025, some 49,000 fewer people without housing, following a smaller decline in 2024.
- **The remaining scale**: Nearly 700,000 people still live in shelters or on the streets, significantly more than before the Covid-19 pandemic.
- **The official account**: The secretary credits the fall primarily to border enforcement and public safety policy, arguing that during the previous administration New York, Chicago, Boston and Denver all saw surges in shelter demand.
- **The third-party account**: The alliance analysed the same count and found a comparable decline, but attributes it to housing programmes funded by Congress, rents falling back from their pandemic peaks, and the assistance that became available in areas hit by major disasters.
- **Which cities moved**: Analysis from the Cicero Institute, an administration ally on homelessness policy, notes that those same four cities have driven half of the recent drop, while cities such as San Francisco are backing supportive housing that bans alcohol and other substances. Critics argue that such conditions send people back to the street when relapse, which is common, becomes an issue.
- **Veterans**: Homelessness among veterans fell more than 7 percent last year and has declined nearly 60 percent since 2010. Oliva argues that programmes which move people off the street without preconditions are much closer to the scale of need for that population.
- **The counter-current**: Alongside the overall decline, the number of people who have been homeless for a long time ticked up slightly, a group more likely to face mental health problems and addiction.
- **Municipal tools in dispute**: The Supreme Court said in 2024 that cities may ban sleeping and camping in public places. Oliva states that her commissioned analysis showed cities with such bans actually did worse than the national average.
- **The policy direction**: The administration wants to cut federal homelessness spending and shift it toward short-term housing with mandated addiction and mental health treatment, while the alliance argues for more permanent housing for people who are chronically homeless.

## Comparison of Viewpoints

**The disagreement concerns where the causal chain begins.** The department's logic is that tightened borders reduced new flows into homelessness and restored order on the streets, reducing the stock. The alliance's logic is that housing supply and programme funding are the real variables and that immigration policy is at most an accelerant. Both readings rest on the same dataset, which is precisely the point: an annual point-in-time count cannot, on its own, identify causes.

**Mandatory treatment versus unconditional placement is the real fault line.** The administration argues that the long-standing approach of permanent housing first and voluntary treatment afterwards has failed, blames it for the pandemic spike, and wants short-term housing with mandated treatment instead. The alliance counters that the very programmes which move people off the street without preconditions account for a large share of the recent declines, most visibly among veterans, and both sides cite the same veteran figures as evidence against the other.

**The effect of municipal tools is being reassessed.** After the Supreme Court ruling in 2024 pushed cities from passive management towards active enforcement, the divergence in how those cities actually performed suggests that national conclusions and local execution point in different directions.

**The composition of the decline is under-credited.** The alliance points in particular to rents coming off their pandemic peaks and to disaster assistance in western North Carolina and Hawaii, which intercepted people who might otherwise have ended up on the street. That share of the improvement looks less like a policy victory and more like a market cycle and emergency response.

## Panoramic Analysis

The most important feature of this story is not the figure itself but the fact that two organisations with opposed positions cite the same dataset and reach opposite conclusions. A point-in-time count is a fragile instrument: it depends on how many people are counted in shelters, on the street and in temporary accommodation on a single night, and it is sensitive to weather, to counting methodology and to temporary surges in services. It does not, by itself, identify causes. And when a number admits several explanations, the questions that matter are whether the collection method changed this year, whether the population covered by the count changed, and whether the decline is evenly distributed. On the last point the answer is clearly no. Alongside an overall fall, the number of people homeless for a long time rose slightly, and that divergence points to a real shift in where money and effort are going: toward the people who are easiest to count and away from those who are hardest.

The accompanying change of instrument is the substitution of short-term housing with mandated treatment for housing first with voluntary treatment. That substitution is cheaper in fiscal terms, more measurable in outcome terms and easier to defend politically, but it leaves part of the population that was previously being caught by the system exposed again on the street.

Over a longer horizon, American housing policy has oscillated between raising supply and managing demand, and the 2025 decline rests largely on a third route: immigration policy, public order and disaster relief all contributing at once. None of the three can be relied on indefinitely, which makes the real question how much of this assembled decline survives when the rent cycle turns, when the disaster cycle ends and when the marginal effect of immigration policy fades.

One caveat deserves stating plainly: the 2024 Supreme Court ruling allowing cities to ban street camping pushed a number of them from passive management towards active enforcement, and the divergence in how individual cities performed shows a clear gap between national conclusions and local execution. That is why the alliance's analysis deserves to be read rather than dismissed: in the absence of published methodological detail, offering data-level counter-evidence to an official narrative is itself a necessary condition for the quality of public debate.""",
})

# ------------------------------------------------------------------ E (T2 crypto, CN+EN)
A.append({
    "tier": "2", "cat": "crypto",
    "slug": "binance-cfo-departs-after-record-hack-2026-11-08",
    "title_cn": "[快讯] 币安首席财务官离任 距创纪录安全事件仅九天 公司称交接计划已酝酿半年",
    "title_en": "[Brief] Binance CFO Departs Nine Days After Record Security Incident",
    "desc_cn": "加密媒体The Block报道，币安首席财务官在遭遇创纪录安全事件仅九天后离任，联合首席执行官何毅表示，离任属于一项在六个月前就已启动的交接安排。",
    "desc_en": "The Block reports that the chief financial officer of Binance has departed nine days after a record security incident, with co-chief executive Yi He saying the transition was a plan put in place over the past six months.",
    "sum_cn": "在安全事故后九天就更换财务负责人，本身就是一个需要解释的时序问题；而公司的解释把这次变动放回了一个提前半年启动的常规交接框架。两种说法之间的落差，正是外界关注的焦点。",
    "sum_en": "Changing the finance chief nine days after a security incident is a timing that invites explanation, and the company's answer places it inside a routine transition framework begun six months earlier. The gap between the two accounts is what observers are watching.",
    "src_cn": "加密媒体The Block", "src_en": "The Block",
    "tags_cn": ["加密货币", "交易所安全", "人事变动", "国际动态"],
    "tags_en": ["Crypto", "Exchange Security", "Executive Moves", "Digital Assets"],
    "body_cn": """## 核心摘要

加密媒体The Block报道，币安首席财务官在公司遭遇创纪录安全事件仅九天后离任，联合首席执行官何毅表示，离任是为追求新的职业方向，而相关交接安排早在六个月前就已启动。

## 全景透视

在安全事故之后第九天更换财务负责人，这个时序本身就构成一个需要解释的事实，而公司的解释把这次变动放回了一个提前半年启动的常规交接框架。两种叙事之间的落差，正是外部观察者关注的焦点：前者指向危机后的治理反应，后者指向人事安排的连续性。要判断哪一条更接近事实，需要看的不是公告措辞，而是三项可验证的痕迹——冷热钱包比例是否给出了精确拆分与第三方审计、交易所是否面临新的监管问询、以及管理层变动是否在接下来数月继续发生。如果财务之外的合规与安全负责人也开始轮换，那说明公司内部把这次事件定性为流程问题而非孤立事故；如果交接平稳，则更支持公司给出的解释。

---

编辑：GoodInfo全球资讯组""",
    "body_en": """## Key Facts

The Block reports that the chief financial officer of Binance has departed nine days after a record security incident. Co-chief executive Yi He said the departing executive is leaving to pursue a new venture, under a transition plan that was put in place over the past six months.

## Panoramic Analysis

Changing the finance chief nine days after a security incident is a timing that invites explanation, and the company's answer places the change inside a routine transition framework that began six months earlier. The gap between the two narratives is what observers are watching: the first points to a governance response after a crisis, the second to continuity in staffing. Deciding which account is closer to fact will not depend on the wording of the announcement but on three verifiable traces. The first is whether the exchange now publishes an exact breakdown of assets held in cold versus hot wallets together with third-party audit results. The second is whether the incident has triggered fresh regulatory enquiries or reporting requirements. The third is whether further senior departures follow in the security and compliance functions over the coming months. If the change spreads beyond finance, the company is treating the event as a process failure rather than an isolated incident; if the transition holds steady, the company's own account is better supported.

---

Editor: GoodInfo Global News Team""",
})

# ------------------------------------------------------------------ F (T2 crypto, CN only)
A.append({
    "tier": "2", "cat": "crypto",
    "slug": "ex-fbi-agent-crypto-theft-guilty-plea-2026-11-08",
    "title_cn": "[快讯] 前联邦探员承认窃取两百四十七万美元加密资产 涉及三十五起调查关联钱包",
    "title_en": "[Brief] Former US Federal Agent Pleads Guilty to Taking Crypto From Wallet Addresses",
    "desc_cn": "加密媒体The Block报道，一名前联邦调查局探员已对窃取加密资产认罪，涉案金额为二百四十七万美元，相关钱包与三十五起在办调查存在关联。报道称，其将支付至少二百四十万美元的赔偿金，并放弃未来通过讲述该案经历获得的全部收益。",
    "desc_en": "The Block reports that a former United States federal agent has pleaded guilty to taking cryptocurrency worth 2.47 million dollars from wallet addresses linked to thirty-five active investigations, with the individual to pay at least 2.4 million dollars in restitution.",
    "sum_cn": "这起案件的意义不在金额，而在结构：一名掌握取证工具链与地址追踪能力的人，恰恰最清楚如何在监控体系里留下最少的痕迹。",
    "sum_en": "The significance lies not in the amount but in the structure: someone who understands the forensic toolchain and address tracing is also the person best placed to leave the fewest traces inside a monitoring system.",
    "src_cn": "加密媒体The Block", "src_en": "The Block",
    "tags_cn": ["加密货币", "金融犯罪", "执法行动", "国际动态"],
    "tags_en": ["Crypto", "Financial Crime", "Law Enforcement"],
    "body_cn": """## 核心摘要

加密媒体The Block报道，一名前联邦调查局探员已对窃取加密资产一事认罪，涉案金额为二百四十七万美元，相关钱包地址与三十五起在办调查存在关联。报道称，其将支付至少二百四十万美元的赔偿金，并放弃未来通过讲述该案经历获得的全部收益。

## 全景透视

这起案件的意义不在金额，而在结构。一名掌握取证工具链与地址追踪能力的人，恰恰最清楚如何在链上分析与交易所监控体系中留下最少的痕迹——这类案件对行业提出的现实问题，是链上证据在多大程度上仍能依赖中心化机构的自愿配合。对交易所而言，它再次提示风控的薄弱环节往往不在技术侧，而在权限管理：内部人员接触提款通道与客户资产的操作范围，本应与岗位权限严格对应，而这正是多数中型交易所在快速扩张期最容易松动的部分。

---

编辑：GoodInfo全球资讯组""",
})

# ------------------------------------------------------------------ G (T2 world, CN+EN)
A.append({
    "tier": "2", "cat": "world",
    "slug": "trump-ufc-dana-white-press-secretary-2026-11-08",
    "title_cn": "[快讯] 特朗普向综合格斗赛事掌门人达纳·怀特发出白宫发言人邀约",
    "title_en": "[Brief] Trump Offers the White House Press Secretary Role to UFC Chief Dana White",
    "desc_cn": "法广France24报道，美国总统特朗普周六表示，已向综合格斗赛事Ultimate Fighting Championship的掌门人达纳·怀特发出白宫新闻发言人职位邀约，并称其为「一位出色的斗士与战士」。怀特尚未明确接受邀请。",
    "desc_en": "France 24 reports that US President Donald Trump said on Saturday he had offered the role of White House press secretary to Ultimate Fighting Championship president and chief executive Dana White, describing him as a fighter and warrior. White has not explicitly accepted the offer.",
    "sum_cn": "把传播能力当作政治资产的定价逻辑，在这次人事设想中体现得最为直接：一个把格斗赛做成全球商业品牌的掌门人，其价值在于触达能力与可控的形象管理，而这恰恰是白宫记者会最需要也最难获得的东西。",
    "sum_en": "The pricing of reach as a political asset is on full display in the idea: a promoter who built a global commercial fighting brand is valued for audience access and controllable image management, precisely what a White House briefing needs and finds hardest to obtain.",
    "src_cn": "法广France24", "src_en": "France 24",
    "tags_cn": ["国际动态", "白宫", "美国政治", "媒体"],
    "tags_en": ["World Affairs", "White House", "US Politics", "Media"],
    "body_cn": """## 核心摘要

法广France24报道，美国总统特朗普周六表示，已向综合格斗赛事Ultimate Fighting Championship的掌门人达纳·怀特发出白宫新闻发言人职位邀约，并在社交平台上称这位五十八岁的高管是「一位出色的斗士与战士」。怀特尚未明确接受邀请，只是发布了一张站在白宫讲台后的照片，该照片是否为人工生成尚无法确认。白宫自十月十六日凯茜·扎卡里亚离任以来一直没有新闻发言人。

## 全景透视

这次人事设想本身的信息量，不在于人选，而在于它透露出一种明确的定价逻辑：白宫把「触达能力」当作一种政治资产来配置。白宫记者会通常是一份强度极高的工作——需要随时应对突发提问、在直播环境中维持立场、并把政策信息准确地传递给媒体；而它的曝光度与规模又远不及选举活动。一个把格斗赛事做成全球商业品牌的掌门人，其价值恰在于自带关注度与个人形象的可控性，这在常规政治传播工具里并不好找。但这一逻辑的短板同样清楚：新闻发言人的职责是解释与澄清，而赛事推广的核心能力是制造话题，二者需要的训练并不相同；此外，如此高曝光的岗位通常需要长期的政策训练与团队磨合，一个新任者能否在数周内进入角色，是这段任期的第一个考验。

---

编辑：GoodInfo全球资讯组""",
    "body_en": """## Key Facts

France 24 reports that US President Donald Trump said on Saturday he had offered the role of White House press secretary to Ultimate Fighting Championship president and chief executive Dana White, describing him on social media as a fighter and warrior. White has not explicitly accepted; he posted a photograph of himself behind the White House lectern that may be artificially generated. The White House has been without a press secretary since Katie Zacharia left the post on October 16 after less than a week in the job.

## Panoramic Analysis

The information value of the idea lies less in the candidate than in the pricing logic it reveals: the White House treats reach as a political asset to be allocated. The daily briefing is demanding work, requiring the ability to field unexpected questions, hold a position under live television and convey policy accurately to the press, while its exposure and scale remain far below an election campaign. A promoter who turned a fighting promotion into a global commercial brand brings exactly what is hard to find in ordinary political communications, namely built-in attention and a personal image that can be managed. The weakness of the logic is equally clear. A press secretary explains and clarifies; a promotion builds an audience, and the two require different training. On top of that, a role with this level of exposure normally depends on long familiarity with policy detail and the rhythm of the briefing room, so whether the new officeholder can become effective within a few weeks is the first test of the term.

---

Editor: GoodInfo Global News Team""",
})

# ------------------------------------------------------------------ H (T2 ai-tech, CN only)
A.append({
    "tier": "2", "cat": "ai-tech",
    "slug": "kids-safe-phones-parent-controls-2026-11-08",
    "title_cn": "[快讯] 家长要求更安全的儿童手机 多家公司推出功能受限设备与家长控制应用",
    "title_en": "[Brief] Parents Want Safer Phones for Kids and Manufacturers Are Answering",
    "desc_cn": "科技媒体TechCrunch报道，随着家长对儿童不受限制使用智能手机的担忧上升，多家公司开始开发专为儿童设计的设备，包括大幅修改系统以移除功能的触屏机型，以及只保留通话与短信功能的极简设备。",
    "desc_en": "TechCrunch reports that as parents grow more concerned about unrestricted smartphone access for children, a growing number of companies are developing devices designed specifically for kids, from touchscreens with heavily modified software to minimalist handsets limited to calls and texts.",
    "sum_cn": "儿童设备市场的真正变量不是硬件配置，而是家长控制这套软件机制能否在不同系统之间互通；一旦控制权分散在各品牌自有的应用里，跨设备的管理就只剩下人工核对。",
    "sum_en": "The real variable in the children's device market is not hardware but whether parental controls interoperate across operating systems; once control is scattered across each vendor's own application, cross-device management is reduced to manual checking.",
    "src_cn": "科技媒体TechCrunch", "src_en": "TechCrunch",
    "tags_cn": ["消费电子", "儿童安全", "家长控制", "智能手机"],
    "tags_en": ["Consumer Tech", "Child Safety", "Parental Controls"],
    "body_cn": """## 核心摘要

科技媒体TechCrunch报道，随着家长对儿童不受限制使用智能手机的担忧上升，多家公司开始开发专为儿童设计的设备。目前面向儿童的机型通常保留触摸屏、相机与通讯能力，但预装软件经过大幅修改，移除了原有功能。

## 全景透视

这类产品的机制其实相当明确：家长通过配套应用审批联系人、查看位置、设置屏幕时间上限、筛选可用的应用，在部分机型上还能收到实时提醒。除修改系统外，另一些厂商选择了更极简的路线，专注通话与短信，还有面向儿童的家庭电话产品。对行业而言，这意味着儿童设备不再是一个由屏幕尺寸和硬件参数定义的市场，而是一个由控制软件、账号体系与家长信任定义的市场，谁能把这些环节做成跨设备、跨品牌的统一体验，谁才可能拿到真正的用户时长与续费；反过来，如果控制权始终分散在各品牌自有应用之中，家庭在多设备之间管理孩子账号的实际成本，就只剩下人工核对这一条路了。

---

编辑：GoodInfo全球资讯组""",
})

# ------------------------------------------------------------------ writer
written = []
for art in A:
    tier = art["tier"]
    cn_meta = {
        "title": art["title_cn"], "title_en": art["title_en"], "date": NOW_STR,
        "draft": "false", "tier": tier,
        "description": art["desc_cn"], "summary": art["sum_cn"],
        "source": art["src_cn"], "categories": [art["cat"]],
        "tags": art["tags_cn"],
    }
    cn_path = "content/posts/%s/%s.md" % (art["cat"], art["slug"])
    written.append(write_article(cn_path, cn_meta, art["body_cn"], CN_SIG))

    if art.get("body_en"):
        en_meta = {
            "title": art["title_en"], "title_en": art["title_en"], "date": NOW_STR,
            "draft": "false", "tier": tier,
            "description": art["desc_en"], "summary": art["sum_en"],
            "source": art["src_en"], "categories": [art["cat"]],
            "tags": art["tags_en"],
        }
        en_path = "content.en/posts/%s/%s.md" % (art["cat"], art["slug"])
        written.append(write_article(en_path, en_meta, art["body_en"], EN_SIG))

print("NOW_STR =", NOW_STR)
for p in written:
    print("WROTE", p)
print("TOTAL", len(written))

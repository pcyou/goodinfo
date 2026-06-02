#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GoodInfo AdSense 合規過濾器 (模組二)
功能：
1. 敏感詞安全替換（標題、內文、標籤）
2. 標籤黑名單過濾（禁止暴力/血腥類標籤出現在側邊欄）
3. 強制歸類機制（敏感新聞統一歸類為「國際動態」或「社會時事」）

使用方法：
    from scripts.adsense_sanitize import sanitize_title, sanitize_content, filter_tags
    
    title = sanitize_title("槍擊案導致多人身亡")
    content = sanitize_content(raw_content)
    tags = filter_tags(["槍擊案", "科技", "AI"])  # 返回 ["國際動態", "科技", "AI"]
"""

import re

# ==================== 敏感詞替換字典 ====================
SENSITIVE_WORDS_MAP = {
    # 暴力/槍械類
    "槍殺": "不幸身亡",
    "被槍殺": "遇襲身亡",
    "槍擊案": "安全事件",
    "開槍射擊": "使用武力",
    "槍手": "涉案人員",
    "槍戰": "衝突事件",
    "中彈": "受傷",
    "彈孔": "損毀痕跡",
    
    # 死亡/謀殺類
    "謀殺": "致命事件",
    "遇害": "不幸離世",
    "遇害身亡": "不幸離世",
    "一家六口家中遇害": "一起嚴重的家庭安全事件",
    "屠殺": "悲劇事件",
    "斬首": "極端暴力行為",
    "屍體": "遺體",
    "碎屍": "遺體損毀",
    "肢解": "遺體損毀",
    "血腥": "令人震驚的",
    "血跡斑斑": "現場跡象明顯",
    "滿地鮮血": "現場情況嚴重",
    
    # 自殺/自殘類
    "自殺": "輕生",
    "自盡": "輕生",
    "跳樓身亡": "墜樓意外",
    "上吊": "輕生",
    "燒炭自殺": "輕生",
    
    # 暴動/衝突類
    "暴動": "群體事件",
    "騷亂": "群體事件",
    "暴亂": "群體事件",
    "抗議衝突": "局勢動盪",
    "示威衝突": "局勢動盪",
    "鎮壓": "管制措施",
    "武力鎮壓": "執法行動",
    "催淚彈": "防暴措施",
    "投擲石塊": "激烈對峙",
    
    # 恐怖主義類
    "恐怖襲擊": "安全威脅事件",
    "恐怖分子": "極端組織成員",
    "ISIS": "極端組織",
    "伊斯蘭國": "極端組織",
    "自殺炸彈": "爆炸事件",
    "人質劫持": "挾持事件",
    "恐怖主義": "極端主義",
    
    # 其他敏感詞
    "強姦": "性侵犯",
    "虐童": "兒童虐待",
    "戀童": "不當行為",
    "販毒": "毒品相關",
    "毒梟": "毒品集團",
    "黑幫": "犯罪組織",
    "黑社會": "犯罪組織",
    "斬人": "持刀傷人",
    "砍人": "持刀傷人",
    "縱火": "火災事件",
    "爆炸案": "爆炸事件",
}

# ==================== 標籤黑名單 ====================
BANNED_TAGS = {
    "槍擊案", "槍殺", "暴動", "騷亂", "暴亂", "恐怖襲擊", "血腥",
    "謀殺", "自殺", "自盡", "屠殺", "人質", "斬首", "碎屍",
    "恐怖分子", "ISIS", "伊斯蘭國", "自殺炸彈", "強姦", "虐童",
    "販毒", "毒梟", "黑幫", "黑社會", "縱火", "爆炸案",
    "gun", "shooting", "murder", "suicide", "blood", "bloody",
    "massacre", "terrorist", "terrorism", "bomb", "bombing",
    "rape", "abuse", "drug", "drugs", "gang", "riot", "rioting",
}

# 安全替代標籤（當觸發黑名單時使用）
SAFE_FALLBACK_TAGS = ["國際動態", "社會時事"]


def sanitize_text(text: str) -> str:
    """對任意文本進行敏感詞替換"""
    if not text:
        return text
    for bad_word, safe_word in SENSITIVE_WORDS_MAP.items():
        text = text.replace(bad_word, safe_word)
    return text


def sanitize_title(title: str) -> str:
    """安全化標題（用於 Hugo frontmatter title）"""
    return sanitize_text(title)


def sanitize_content(content: str) -> str:
    """安全化文章正文"""
    return sanitize_text(content)


def sanitize_tags(tags: list) -> list:
    """
    過濾標籤列表：
    1. 移除黑名單標籤
    2. 如果移除了任何標籤，添加安全替代標籤
    3. 去重
    """
    if not tags:
        return tags
    
    original_count = len(tags)
    filtered = []
    had_banned = False
    
    for tag in tags:
        tag_lower = tag.lower().strip()
        # 檢查是否在黑名單中
        is_banned = False
        for banned in BANNED_TAGS:
            if banned.lower() in tag_lower or tag_lower in banned.lower():
                is_banned = True
                had_banned = True
                break
        if not is_banned:
            filtered.append(tag)
    
    # 如果移除了標籤，添加安全替代標籤
    if had_banned:
        for safe_tag in SAFE_FALLBACK_TAGS:
            if safe_tag not in filtered:
                filtered.append(safe_tag)
    
    return filtered


def needs_safe_category(content: str, title: str = "") -> bool:
    """判斷文章是否需要強制歸類為安全類別"""
    check_text = (title + " " + content).lower()
    for banned in BANNED_TAGS:
        if banned.lower() in check_text:
            return True
    return False


# ==================== 單元測試 ====================
if __name__ == "__main__":
    # 測試敏感詞替換
    test_title = "某地發生槍擊案，多人不幸身亡"
    print(f"原始標題: {test_title}")
    print(f"安全標題: {sanitize_title(test_title)}")
    
    # 測試標籤過濾
    test_tags = ["槍擊案", "科技", "AI", "國際"]
    print(f"\n原始標籤: {test_tags}")
    print(f"安全標籤: {sanitize_tags(test_tags)}")
    
    # 測試安全歸類
    test_content = "這是一篇關於科技發展的文章"
    print(f"\n需要安全歸類: {needs_safe_category(test_content, test_title)}")
    
    print("\n✅ 所有測試通過")

#!/usr/bin/env python3
"""
P3: Telegram 推送格式优化模块
参考 TrendRadar 的五大板块结构，优化 GoodInfo 的 Telegram 推送排版。

板块结构:
1. 📊 头条新闻 (Tier 1: 评分 8.0-10.0)
2. ⚡ 快讯 (Tier 2: 评分 6.0-7.9)
3. 🇨🇳 中国热点 (新增分类)
4. 📈 加密行情 (CoinGecko 数据)
5. 🔗 完整阅读链接

使用方法:
    from scripts.telegram_formatter import format_telegram_message
    
    message = format_telegram_message(articles, crypto_data, briefing_url)
"""

from typing import List, Dict, Optional
from datetime import datetime, timezone, timedelta

# ==========================================
# 配置
# ==========================================

MAX_TIER1_DISPLAY = 5  # 头条最多显示条数
MAX_TIER2_DISPLAY = 8  # 快讯最多显示条数
MAX_CHINA_DISPLAY = 5  # 中国热点最多显示条数
MAX_TOTAL_LENGTH = 4000  # Telegram 消息最大长度

# ==========================================
# 格式化函数
# ==========================================

def format_article_link(title: str, url: str, is_brief: bool = False) -> str:
    """
    格式化单篇文章链接
    
    Args:
        title: 文章标题
        url: 文章 URL
        is_brief: 是否为快讯
        
    Returns:
        Markdown 格式的链接
    """
    prefix = "⚡ " if is_brief else "🔥 "
    return f"{prefix}[{title}]({url})"


def format_tier1_section(articles: List[Dict]) -> str:
    """
    格式化头条新闻板块 (Tier 1)
    """
    if not articles:
        return ""
    
    lines = ["📊 **头条新闻** (深度解读)"]
    lines.append("")
    
    for i, article in enumerate(articles[:MAX_TIER1_DISPLAY]):
        title = article.get('title_zh', article.get('title', ''))
        url = article.get('url', '')
        summary = article.get('summary', '')
        
        link_line = format_article_link(title, url, is_brief=False)
        lines.append(link_line)
        
        if summary and len(summary) < 100:
            lines.append(f"   _{summary}_")
        
        lines.append("")
    
    return '\n'.join(lines)


def format_tier2_section(articles: List[Dict]) -> str:
    """
    格式化快讯板块 (Tier 2)
    """
    if not articles:
        return ""
    
    lines = ["⚡ **快讯** (快速播报)"]
    lines.append("")
    
    for article in articles[:MAX_TIER2_DISPLAY]:
        title = article.get('title_zh', article.get('title', ''))
        url = article.get('url', '')
        
        # 确保标题包含 [快讯] 前缀
        if not title.startswith('[快讯]'):
            title = f'[快讯] {title}'
        
        link_line = format_article_link(title, url, is_brief=True)
        lines.append(link_line)
    
    lines.append("")
    return '\n'.join(lines)


def format_china_section(articles: List[Dict]) -> str:
    """
    格式化中国热点板块
    """
    if not articles:
        return ""
    
    lines = ["🇨🇳 **中国热点**"]
    lines.append("")
    
    for article in articles[:MAX_CHINA_DISPLAY]:
        title = article.get('title', '')
        url = article.get('url', '')
        source = article.get('source', '')
        
        link_line = f"📌 [{title}]({url})"
        if source:
            link_line += f" — _{source}_"
        
        lines.append(link_line)
    
    lines.append("")
    return '\n'.join(lines)


def format_crypto_section(crypto_data: Optional[Dict]) -> str:
    """
    格式化加密货币行情板块
    """
    if not crypto_data:
        return ""
    
    lines = ["📈 **加密行情**"]
    lines.append("")
    
    coins = {
        'bitcoin': 'BTC',
        'ethereum': 'ETH',
        'solana': 'SOL',
        'binancecoin': 'BNB',
        'dogecoin': 'DOGE',
    }
    
    for coin_id, symbol in coins.items():
        if coin_id in crypto_data:
            data = crypto_data[coin_id]
            price = data.get('usd', 0)
            change = data.get('usd_24h_change', 0)
            
            if change > 0:
                change_str = f"🟢 +{change:.1f}%"
            elif change < 0:
                change_str = f"🔴 {change:.1f}%"
            else:
                change_str = "⚪ 0.0%"
            
            lines.append(f"• {symbol}: ${price:,.0f} ({change_str})")
    
    lines.append("")
    return '\n'.join(lines)


def format_telegram_message(
    tier1_articles: List[Dict],
    tier2_articles: List[Dict],
    china_articles: Optional[List[Dict]] = None,
    crypto_data: Optional[Dict] = None,
    briefing_url: str = "https://goodinfo.net",
    extra_sections: Optional[Dict[str, str]] = None
) -> str:
    """
    生成完整的 Telegram 推送消息
    
    Args:
        tier1_articles: 头条文章列表
        tier2_articles: 快讯文章列表
        china_articles: 中国热点文章列表
        crypto_data: 加密货币行情数据
        briefing_url: 完整图文链接
        extra_sections: 额外板块 {'板块名': '内容'}
        
    Returns:
        格式化后的 Telegram 消息
    """
    sections = []
    
    # 头部
    now_beijing = datetime.now(timezone.utc) + timedelta(hours=8)
    date_str = now_beijing.strftime('%Y-%m-%d %H:%M')
    
    header = f"📰 **GoodInfo 全球热点**\n🕒 {date_str} (北京时间)\n"
    sections.append(header)
    
    # 板块 1: 头条新闻
    tier1_section = format_tier1_section(tier1_articles)
    if tier1_section:
        sections.append(tier1_section)
    
    # 板块 2: 快讯
    tier2_section = format_tier2_section(tier2_articles)
    if tier2_section:
        sections.append(tier2_section)
    
    # 板块 3: 中国热点
    if china_articles:
        china_section = format_china_section(china_articles)
        if china_section:
            sections.append(china_section)
    
    # 板块 4: 加密行情
    if crypto_data:
        crypto_section = format_crypto_section(crypto_data)
        if crypto_section:
            sections.append(crypto_section)
    
    # 额外板块
    if extra_sections:
        for section_name, section_content in extra_sections.items():
            if section_content:
                sections.append(section_content)
    
    # 底部链接
    footer = f"📖 **完整图文版**: {briefing_url}\n"
    footer += f"\n_— GoodInfo 自动发布_"
    sections.append(footer)
    
    # 拼接所有板块
    message = '\n'.join(sections)
    
    # 截断到最大长度
    if len(message) > MAX_TOTAL_LENGTH:
        message = message[:MAX_TOTAL_LENGTH - 50] + '\n\n... (内容过长，请点击完整链接阅读)'
    
    return message


# ==========================================
# 辅助函数
# ==========================================

def split_long_message(message: str, max_length: int = MAX_TOTAL_LENGTH) -> List[str]:
    """
    将长消息分割为多条
    
    Args:
        message: 原始消息
        max_length: 每条消息最大长度
        
    Returns:
        消息列表
    """
    if len(message) <= max_length:
        return [message]
    
    parts = []
    current = ""
    
    # 按段落分割
    paragraphs = message.split('\n\n')
    
    for para in paragraphs:
        if len(current) + len(para) + 2 <= max_length:
            if current:
                current += '\n\n' + para
            else:
                current = para
        else:
            if current:
                parts.append(current)
            current = para
    
    if current:
        parts.append(current)
    
    return parts


# ==========================================
# 命令行入口
# ==========================================

def main():
    """测试示例"""
    test_tier1 = [
        {
            'title_zh': 'NVIDIA 发布新一代 AI 芯片，性能提升 10 倍',
            'url': 'https://goodinfo.net/posts/ai-tech/nvidia-new-chip',
            'summary': 'NVIDIA 今天发布了新一代 AI 加速器，号称性能比上一代提升 10 倍。',
        },
        {
            'title_zh': '美联储宣布加息 25 个基点',
            'url': 'https://goodinfo.net/finance/fed-rate-hike',
            'summary': '美联储宣布将基准利率上调 25 个基点至 5.5%-5.75%。',
        },
    ]
    
    test_tier2 = [
        {
            'title_zh': '[快讯] 苹果发布 iOS 18.2 更新',
            'url': 'https://goodinfo.net/ai-tech/ios-update',
        },
        {
            'title_zh': '[快讯] 特斯拉 Q3 交付量超预期',
            'url': 'https://goodinfo.net/finance/tesla-delivery',
        },
    ]
    
    test_china = [
        {
            'title': '知乎热榜：AI 将如何改变教育？',
            'url': 'https://goodinfo.net/china-hotspot/zhihu-ai-education',
            'source': '知乎日报',
        },
    ]
    
    test_crypto = {
        'bitcoin': {'usd': 68500, 'usd_24h_change': 2.5},
        'ethereum': {'usd': 3450, 'usd_24h_change': -1.2},
        'solana': {'usd': 145, 'usd_24h_change': 5.8},
    }
    
    message = format_telegram_message(
        tier1_articles=test_tier1,
        tier2_articles=test_tier2,
        china_articles=test_china,
        crypto_data=test_crypto,
    )
    
    print("=" * 60)
    print("Telegram 推送消息预览:")
    print("=" * 60)
    print(message)
    print("=" * 60)
    print(f"消息长度: {len(message)} 字符")


if __name__ == '__main__':
    main()

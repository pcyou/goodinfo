import subprocess, re, json

urls = [
    ("OpenAI Phone", "https://techcrunch.com/2026/04/27/openai-could-be-making-a-phone-with-ai-agents-replacing-apps/"),
    ("Itron Hack", "https://techcrunch.com/2026/04/27/critical-infrastructure-giant-itron-says-it-was-hacked/"),
    ("Meta Space Solar", "https://techcrunch.com/2026/04/27/meta-inks-deal-for-solar-power-at-night-beamed-from-space/"),
    ("SWE-bench OpenAI", "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"),
    ("BBC Mandelson", "https://www.bbc.com/news/articles/c3r3r2vzjp1o"),
    ("BBC Northern Ireland", "https://www.bbc.com/news/articles/c80m0mgvm05o"),
]

for name, url in urls:
    try:
        r = subprocess.run(["curl", "-s", "-L", url, 
            "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"],
            capture_output=True, text=True, timeout=15)
        html = r.stdout
        
        title_m = re.search(r'<title[^>]*>(.*?)</title>', html, re.DOTALL)
        title = title_m.group(1).strip().replace('| TechCrunch', '').replace('| BBC News', '').replace('| OpenAI', '') if title_m else "N/A"
        
        desc_m = re.search(r'meta name="description" content="(.*?)"', html)
        desc = desc_m.group(1) if desc_m else "N/A"
        
        body = re.sub(r'<[^>]+>', ' ', html)
        body = re.sub(r'\s+', ' ', body).strip()
        
        print(f"\n{'='*60}")
        print(f"NAME: {name}")
        print(f"URL: {url}")
        print(f"TITLE: {title}")
        print(f"DESC: {desc}")
        print(f"BODY_PREVIEW: {body[:1500]}")
    except Exception as e:
        print(f"\n{'='*60}")
        print(f"NAME: {name}")
        print(f"ERROR: {str(e)}")

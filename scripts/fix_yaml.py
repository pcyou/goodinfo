import os, re

output_dir = "/root/goodinfo-site/content/posts/opensource"
fixed = 0

for fname in os.listdir(output_dir):
    if not fname.endswith(".md"):
        continue
    
    fpath = os.path.join(output_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract frontmatter block
    m = re.match(r'(---\n)(.*?)(\n---)', content, re.DOTALL)
    if not m:
        continue
    
    header = m.group(1)
    fm_text = m.group(2)
    footer = m.group(3)
    
    # Clean up: remove stray quote-only lines, merge multi-line values
    lines = fm_text.split('\n')
    clean_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip empty/quote-only lines
        if line.strip() in ('"', "'", '""', "''"):
            i += 1
            continue
        # If line starts with a known key, take it
        if any(line.startswith(k) for k in ['title:', 'date:', 'tags:', 'categories:', 'summary:', 'source_url:', 'xiahuid:']):
            clean_lines.append(line)
            i += 1
            continue
        # Otherwise it's a continuation of previous value - append to previous
        if clean_lines:
            clean_lines[-1] += ' ' + line.strip()
        i += 1
    
    # Now fix title and summary
    final_lines = []
    for line in clean_lines:
        stripped = line.strip()
        if stripped.startswith("title:") or stripped.startswith("summary:"):
            key, _, val = stripped.partition(":")
            val = val.strip().strip("'\"").strip()
            val = val.replace('"', '').replace("'", '').strip()
            if len(val) > 200:
                val = val[:200]
            final_lines.append(f'{key}: "{val}"')
        else:
            final_lines.append(stripped)
    
    new_fm = '\n'.join(final_lines)
    new_content = header + new_fm + footer + content[m.end():]
    
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixed += 1

print(f"Fixed {fixed} files")

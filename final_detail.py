import os
import re
import html

post_dir = "_posts"

# Barnacles to scrape off
tags_to_strip = [
    r'<div.*?>', r'</div>', 
    r'<span.*?>', r'</span>', 
    r'<br\s*/?>',
    r'imageanchor="1"', r'border="0"'
]

print("Starting deep cleanup of HTML entities...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Fix the Header (Turn 5 dashes into 3)
        content = re.sub(r'^-----', '---', content)

        # 2. Convert &lt; and &gt; back into < and >
        content = html.unescape(content)

        # 3. Strip the junk tags
        for tag in tags_to_strip:
            content = re.sub(tag, '', content, flags=re.IGNORECASE)

        # 4. Clean up spacing and curly quotes
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = content.replace('”', '"').replace('“', '"')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Repaired: {filename}")

print("\nAll 52 files deep-cleaned. Run 'pushit' to update the site.")
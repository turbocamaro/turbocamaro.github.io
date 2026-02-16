import os
import re

post_dir = "_posts"

# These are the "barnacles" we want to scrape off
tags_to_strip = [
    r'<div.*?>', r'</div>', 
    r'<span.*?>', r'</span>', 
    r'<br\s*/>', r'<br>',
    r'imageanchor="1"', r'border="0"'
]

print("Starting final text detailing...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Clean up the messy HTML tags
        clean_content = content
        for tag in tags_to_strip:
            clean_content = re.sub(tag, '', clean_content, flags=re.IGNORECASE)

        # 2. Fix the specific "Separator" blocks but keep the image/iframe inside
        # This replaces multiple newlines with a clean double break
        clean_content = re.sub(r'\n\s*\n', '\n\n', clean_content)

        # 3. Smart replacement for common HTML entities
        clean_content = clean_content.replace('&nbsp;', ' ')
        clean_content = clean_content.replace('”', '"').replace('“', '"') # Fix curly quotes

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(clean_content)
        print(f"Detailed: {filename}")

print("\nCleanup complete! Your posts are now clean Markdown.")
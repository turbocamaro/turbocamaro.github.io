import os
import re
import html

post_dir = "_posts"

print("Stripping HTML tags and reverting to clean Markdown alignment...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Standardize text and quotes
        content = html.unescape(content)
        content = content.replace('“', '"').replace('”', '"').replace('’', "'")

        # 2. THE CLEANUP: Convert <figure> blocks back to simple centered blocks
        # This regex catches the image and the caption text inside our previous mess
        figure_repair_regex = r'<figure.*?>\s*(<a.*?>.*?</a>)\s*<figcaption.*?>(.*?)</figcaption>\s*</figure>'
        
        def simple_layout(match):
            img_part = match.group(1)
            caption_text = match.group(2)
            # We use a simple <div> for centering and <em> for italics
            return f'\n\n<div align="center">\n  {img_part}\n  <br/>\n  <em>{caption_text}</em>\n</div>\n\n'

        content = re.sub(figure_repair_regex, simple_layout, content, flags=re.DOTALL)

        # 3. Final spacing check
        content = re.sub(r'\n{3,}', '\n\n', content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Simplified: {filename}")

print("\nDone. All fancy tags removed. Run 'pushit'.")
import os
import re
import html

post_dir = "_posts"

print("Simplifying HTML blocks for Jekyll compatibility...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Standardize text
        content = html.unescape(content)
        content = content.replace('“', '"').replace('”', '"').replace('’', "'")

        # 2. The "Clean Figure" Logic
        # We use markdown="1" to tell Jekyll to keep processing inside the tags
        # And we use a simpler class-free figcaption
        def fix_figure(match):
            img_part = match.group(1)
            caption_text = match.group(2)
            return f'\n\n<figure markdown="1" style="text-align:center;">\n  {img_part}\n  <figcaption><i>{caption_text}</i></figcaption>\n</figure>\n\n'

        # This regex finds the existing figure/figcaption mess and rewrites it clean
        figure_regex = r'<figure.*?>\s*(<a.*?>.*?</a>)\s*<figcaption.*?>(.*?)</figcaption>\s*</figure>'
        content = re.sub(figure_regex, fix_figure, content, flags=re.DOTALL)

        # 3. Final flush-left and spacing check
        content = re.sub(r'\n{3,}', '\n\n', content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Refined: {filename}")

print("\nDone. Run 'pushit' and check the site.")
import os
import re
import html

post_dir = "_posts"

# Added table, tbody, tr, and td to the hit list
tags_to_strip = [
    r'<table.*?>', r'</table>', 
    r'<tbody.*?>', r'</tbody>',
    r'<tr.*?>', r'</tr>',
    r'<td.*?>', r'</td>',
    r'<div.*?>', r'</div>', 
    r'<span.*?>', r'</span>', 
    r'<br\s*/?>',
    r'imageanchor="1"', r'border="0"'
]

print("Stripping tables and detailing captions...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Fix the Header (Ensure 3 dashes)
        content = re.sub(r'^-----', '---', content)

        # 2. Convert &lt; to <
        content = html.unescape(content)

        # 3. Specifically handle the "tr-caption" class to keep descriptions readable
        # This replaces the caption tag with a simple bold label
        content = content.replace('class="tr-caption"', '')

        # 4. Strip the junk tags (including tables)
        for tag in tags_to_strip:
            content = re.sub(tag, '', content, flags=re.IGNORECASE)

        # 5. Clean up spacing and curly quotes
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = content.replace('”', '"').replace('“', '"')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Table Busted: {filename}")

print("\nCleanup complete! Run 'pushit' to update the site.")
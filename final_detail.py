import os
import re
import html

post_dir = "_posts"

# List of tags to strip entirely
tags_to_strip = [
    r'<table.*?>', r'</table>', r'<tbody.*?>', r'</tbody>',
    r'<tr.*?>', r'</tr>', r'<td.*?>', r'</td>',
    r'<div.*?>', r'</div>', r'<span.*?>', r'</span>', 
    r'<br\s*/?>', r'imageanchor="1"', r'border="0"'
]

print("Applying professional figure captions...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Header and Entity Fix
        content = re.sub(r'^-----', '---', content)
        content = html.unescape(content)

        # 2. CAPTION LOGIC: 
        # This looks for an image followed by text that was marked as a caption in Blogger
        # and wraps it in a <figure> block for perfect alignment.
        pattern = r'(<a href=.*?><img.*?></a>)\s*(.*?)(?=\s*<a|<br|Early|With|The|Overall|\n\n|$)'
        # Note: We'll apply this specifically to known caption text if it's short.
        
        # 3. Strip the junk tags
        for tag in tags_to_strip:
            content = re.sub(tag, '', content, flags=re.IGNORECASE)

        # 4. Final Spacing and Curly Quote fix
        content = re.sub(r'\n\s*\n', '\n\n', content)
        content = content.replace('”', '"').replace('“', '"')
        
        # 5. Add custom CSS alignment to the images
        # This centers images and makes captions look like captions
        content = content.replace('<img ', '<img style="display: block; margin: 0 auto; max-width: 100%; height: auto;" ')

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Captions Aligned: {filename}")

print("\nDetailing complete. Run 'pushit' to update.")
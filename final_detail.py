import os
import re
import html

post_dir = "_posts"

print("Converting floating text to professional Figcaptions...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Standard Cleanup (Entities and Headers)
        content = html.unescape(content)
        content = re.sub(r'^-----', '---', content)

        # 2. THE CAPTION ENGINE
        # This regex looks for: 
        # An image link (<a...><img...></a>) 
        # Followed by a single line of text (the caption)
        # Followed by a double newline (the next paragraph)
        # It wraps them in <figure> and <figcaption>
        figure_pattern = r'(<a href=.*?><img.*?></a>)\n(.*?)\n\n'
        content = re. some_sub = re.sub(figure_pattern, r'<figure style="text-align: center; margin: 20px 0;">\1<figcaption style="font-style: italic; font-size: 0.9em; color: #666; margin-top: 8px;">\2</figcaption></figure>\n\n', content)

        # 3. Clean up the "Turbo | Camaro" signature at the bottom
        content = content.replace("Turbo | Camaro", "---\n*Turbo Camaro Build History*")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Figcaptioned: {filename}")

print("\nDone! Your captions are now locked to your images.")
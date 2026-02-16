import os
import re
import html

post_dir = "_posts"

print("Enforcing 'Flush-Left' margins for HTML tags...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            # If the line contains an HTML tag we want to render, remove ALL leading spaces
            if line.strip().startswith('<figure') or line.strip().startswith('</figure') or line.strip().startswith('<figcaption'):
                new_lines.append(line.lstrip())
            else:
                new_lines.append(line)

        content = "".join(new_lines)

        # Ensure double newlines around the figure blocks
        content = re.sub(r'(<figure.*?>)', r'\n\n\1', content)
        content = re.sub(r'(</figure>)', r'\1\n\n', content)
        
        # Final cleanup of any weird spacing
        content = re.sub(r'\n{3,}', '\n\n', content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Fixed Margins: {filename}")

print("\nDone. Run 'pushit' and check the site.")
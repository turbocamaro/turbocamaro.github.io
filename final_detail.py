import os
import re
import html

post_dir = "_posts"

print("Fixing Figure spacing for Jekyll...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Standard Cleanup
        content = html.unescape(content)
        content = re.sub(r'^-----', '---', content)

        # THE REPAIR: Ensure <figure> has blank lines around it and NO leading spaces
        # We wrap the existing figure logic to include double newlines
        figure_pattern = r'(<figure.*?>)(.*?)(</figure>)'
        content = re.sub(figure_pattern, r'\n\n\1\2\3\n\n', content, flags=re.DOTALL)
        
        # Clean up any accidental triple-newlines created by the fix
        content = re.sub(r'\n{3,}', '\n\n', content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Spaced & Repaired: {filename}")

print("\nDone. Run 'pushit' now.")
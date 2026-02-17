import os
import re

post_dir = "_posts"

# Regex to find: {% post_url 2016-02-06-some-slug %}
# It captures the date and the slug separately
liquid_pattern = r'\{%\s*post_url\s+(\d{4}-\d{2}-\d{2})-(.*?)\s*%\}'

print("Neutralizing all Liquid post_url tags...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Replacement logic:
        # Turns {% post_url 2016-02-06-paint %} into /posts/paint/
        def replace_with_standard(match):
            slug = match.group(2)
            return f"/posts/{slug}/"

        new_content = re.sub(liquid_pattern, replace_with_standard, content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Bypassed links in: {filename}")

print("\nAll Liquid tags neutralized. Jekyll will no longer crash on build.")
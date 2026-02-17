import os
import re

post_dir = "_posts"

# 1. First, we build a map of all your posts so we know what to link to
post_map = {}
for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        # Extract the date and slug: 2016-02-07-crank-and-rods
        # The filename (minus .md) is exactly what 'post_url' needs
        base_name = filename.replace(".md", "")
        # The "slug" part is usually the end: crank-and-rods
        slug = "-".join(base_name.split("-")[3:])
        post_map[slug] = base_name

print(f"Mapped {len(post_map)} posts for internal linking.")

# 2. Now we scan and replace the old URLs
print("Updating internal links...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find old Blogger/Custom domain links
        # Matches: http://www.turbocamaro.ca/2016/02/something.html
        link_pattern = r'https?://(?:www\.)?turbocamaro\.ca/\d{4}/\d{2}/([^/\s\>]+)\.html'

        def replace_link(match):
            old_slug = match.group(1).replace("_", "-") # Blogger uses underscores sometimes
            if old_slug in post_map:
                new_link = f"{{% post_url {post_map[old_slug]} %}}"
                return new_link
            return match.group(0) # Keep original if no match found

        new_content = re.sub(link_pattern, replace_link, content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated links in: {filename}")

print("\nInternal links fixed! Run 'pushit' to sync.")
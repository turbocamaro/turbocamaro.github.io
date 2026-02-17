import os
import re

post_dir = "_posts"

# 1. Build a strict map of what actually exists in your folder
valid_posts = [f.replace(".md", "") for f in os.listdir(post_dir) if f.endswith(".md")]
print(f"Verified {len(valid_posts)} valid files in _posts.")

# 2. Re-run the repair with a safety check
print("Updating internal links with safety checks...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex for your old Blogger links
        link_pattern = r'https?://(?:www\.)?turbocamaro\.ca/\d{4}/\d{2}/([^/\s\>]+)\.html'

        def safe_replace(match):
            old_slug = match.group(1).replace("_", "-")
            # We look for a file that ENDS with this slug
            # e.g., if slug is 'scat-seats', it matches '2016-01-25-scat-seats'
            match_found = next((p for p in valid_posts if p.endswith(old_slug)), None)
            
            if match_found:
                return f"{{% post_url {match_found} %}}"
            else:
                # If no match, revert to a standard relative link so the build doesn't crash
                print(f"Warning: No file found for slug '{old_slug}'. Using raw path.")
                return f"/posts/{old_slug}/"

        new_content = re.sub(link_pattern, safe_replace, content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

print("\nSafety check complete. Try 'pushit' now.")
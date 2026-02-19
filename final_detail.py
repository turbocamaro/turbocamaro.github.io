import os
import re

# Path to your posts
posts_dir = '_posts'

# Regex to find: {% post_url YYYY-MM-DD-slug %}
# It captures the date and the slug separately
link_pattern = re.compile(r'\{%\s+post_url\s+(?:\d{4}-\d{2}-\d{2}-)?([\w-]+)\s+%\}')

def fix_links():
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            path = os.path.join(posts_dir, filename)
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Replace the liquid tag with a standard relative link
            # Example: {% post_url 2016-02-07-alcohol-injection %} -> /posts/alcohol-injection/
            new_content = link_pattern.sub(r'/posts/\1/', content)

            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed links in: {filename}")

if __name__ == "__main__":
    fix_links()
    print("Link overhaul complete. Try building the site now.")
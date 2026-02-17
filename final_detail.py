import os
import re

post_dir = "_posts"
# This is the path Jekyll uses to find the images on the live site
new_img_path = "/assets/img/posts/"

print("Re-linking posts to local Takeout images...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find any Blogger image URL
        # e.g., https://blogger.googleusercontent.com/.../s1600/20161119_143625.jpg
        img_pattern = r'https://blogger\.googleusercontent\.com/img/b/[^"\)\s\>]+'
        
        def link_to_local(match):
            url = match.group(0)
            # Grab just the filename at the end (e.g., 20161119_143625.jpg)
            img_filename = url.split('/')[-1]
            # Return the new local path
            return f"{new_img_path}{img_filename}"

        new_content = re.sub(img_pattern, link_to_local, content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated images in: {filename}")

print("\nAll links updated to local assets. Use 'pushit' to upload.")
import os
import re

# Since you are running this in VSC inside your repo, "." is the current folder
repo_path = "." 
posts_path = os.path.join(repo_path, "_posts")
images_dir = os.path.join(repo_path, "assets", "img", "posts")

# Tightened Regex: Specifically looks for .jpg, .png, .gif, .jpeg
img_regex = r'src="([^"]+\.(?:jpg|png|gif|jpeg))"|!\[.*?\]\((.*?\.(?:jpg|png|gif|jpeg))\)'

def check_images():
    if not os.path.exists(posts_path):
        print(f"ERROR: Cannot find _posts folder at {os.path.abspath(posts_path)}")
        return

    print(f"--- Scanning: {os.path.abspath(posts_path)} ---")
    broken_count = 0
    verified_count = 0
    
    for filename in os.listdir(posts_path):
        if filename.endswith(".md") or filename.endswith(".markdown"):
            file_path = os.path.join(posts_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(img_regex, content, re.IGNORECASE)
                
                for match in matches:
                    raw_path = match[0] if match[0] else match[1]
                    
                    # IGNORE YouTube or external http links
                    if "youtube.com" in raw_path or "youtu.be" in raw_path or raw_path.startswith("http"):
                        continue
                    
                    img_filename = os.path.basename(raw_path)
                    full_img_path = os.path.join(images_dir, img_filename)
                    
                    if os.path.exists(full_img_path):
                        verified_count += 1
                    else:
                        print(f"\n[BROKEN] Post: {filename}")
                        print(f"        Missing Image: {img_filename}")
                        print(f"        Expected at:   {full_img_path}")
                        broken_count += 1

    print("\n--- Summary ---")
    print(f"Images Verified (Found): {verified_count}")
    print(f"Broken Images (Missing): {broken_count}")

if __name__ == "__main__":
    check_images()
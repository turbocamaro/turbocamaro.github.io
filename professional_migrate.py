import os
import re

output_dir = "_posts"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Starting heading-focused migration...")

with open("feed.atom", "r", encoding="utf-8") as f:
    data = f.read()

entries = data.split("<entry>")
entries.pop(0)

used_filenames = {}
count = 0

for entry in entries:
    if "<blogger:type>POST</blogger:type>" not in entry:
        continue

    # 1. EXTRACT TITLE - Improved regex to catch all title types
    title_match = re.search(r'<title.*?type=["\']text["\']>(.*?)</title>', entry)
    if not title_match:
        # Fallback for older or differently formatted titles
        title_match = re.search(r'<title.*?>(.*?)</title>', entry)
    
    title = title_match.group(1).strip() if title_match else "Untitled Post"
    
    # 2. EXTRACT DATE
    date_match = re.search(r'<published>(.*?)T', entry)
    date = date_match.group(1) if date_match else "2026-01-01"

    # 3. EXTRACT CONTENT
    content_match = re.search(r"<content type='html'>(.*?)</content>", entry, re.DOTALL)
    content = content_match.group(1) if content_match else ""

    # 4. CREATE CLEAN FILENAME FROM HEADING
    # Remove special characters, keep only letters, numbers, and spaces
    clean_heading = re.sub(r'[^a-zA-Z0-9\s]', '', title).strip().lower()
    # Swap spaces for single hyphens
    clean_heading = re.sub(r'\s+', '-', clean_heading)
    
    if not clean_heading or clean_heading == "untitled-post":
        clean_heading = f"post-{count}"

    # 5. JEKLL FORMAT: YYYY-MM-DD-heading.md
    base_name = f"{date}-{clean_heading}"
    final_name = base_name

    if final_name in used_filenames:
        used_filenames[base_name] += 1
        final_name = f"{base_name}-{used_filenames[base_name]}"
    else:
        used_filenames[base_name] = 0

    filename = f"{output_dir}/{final_name}.md"

    # 6. WRITE FILE
    with open(filename, "w", encoding="utf-8") as post:
        post.write("-----") # Standard Jekyll delimiter
        post.write(f'\ntitle: "{title}"\n')
        post.write(f"date: {date} 12:00:00 +0000\n")
        post.write("categories: [Build]\n")
        post.write("tags: [blogger]\n")
        post.write("---\n\n")
        post.write(content)

    count += 1
    print(f"Success: {final_name}.md")

print(f"\nMigration complete. {count} posts successfully named by heading.")
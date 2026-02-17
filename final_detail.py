import os
import re
import html

post_dir = "_posts"

print("Automating responsive YouTube containers...")

for filename in os.listdir(post_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(post_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Standardize text and quotes
        content = html.unescape(content)

        # 2. THE VIDEO FIX: Wrap iframes in a responsive div
        # We remove the fixed width/height and use a 16:9 aspect ratio container
        video_pattern = r'<iframe.*?src="(https://www.youtube.com/embed/.*?)".*?></iframe>'
        
        def responsive_video(match):
            video_url = match.group(1)
            return (
                f'\n\n<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">'
                f'\n  <iframe src="{video_url}" '
                f'style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" '
                f'allowfullscreen></iframe>'
                f'\n</div>\n\n'
            )

        content = re.sub(video_pattern, responsive_video, content, flags=re.DOTALL)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip())
        print(f"Video Resized: {filename}")

print("\nAll videos are now responsive. Run 'pushit' to update.")
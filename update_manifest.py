import os
import json
import re

slides_dir = os.path.join(os.path.dirname(__file__), 'slides')
valid_exts = ('.jpg', '.jpeg', '.png', '.webp', '.gif')

files = []
if os.path.exists(slides_dir):
    for f in os.listdir(slides_dir):
        if f.lower().endswith(valid_exts):
            files.append(f)

# Sort by leading number if present
def sort_key(name):
    m = re.match(r'^(\d+)', name)
    return int(m.group(1)) if m else 999

files.sort(key=sort_key)

manifest_path = os.path.join(slides_dir, 'manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as mf:
    json.dump(files, mf, indent=2)

print(f"Updated slides/manifest.json with {len(files)} files: {files}")

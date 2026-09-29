import json
import re

with open('links_data.json', 'r', encoding='utf-8') as f:
    links = json.load(f)

links_dict = {item['id']: item for item in links}

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = content
for id_val, data in links_dict.items():
    lat, lon = data['lat'], data['lon']
    img = data['img']
    url = data['url']
    
    # regex to find coords
    pattern = r'(id:\s*["\']' + re.escape(id_val) + r'["\']\s*,[\s\S]*?coords:\s*\[)[^\]]+(\])'
    replacement = rf'\g<1>{lat}, {lon}\g<2>'
    new_content = re.sub(pattern, replacement, new_content)
    
    # insert yandexUrl right after title
    pattern_url = r'(id:\s*["\']' + re.escape(id_val) + r'["\']\s*,[\s\S]*?title:\s*["\'][^"\']+["\'],)'
    replacement_url = rf'\g<1>\n        yandexUrl: "{url}",'
    if f'yandexUrl: "{url}"' not in new_content:
        new_content = re.sub(pattern_url, replacement_url, new_content)
    
    # replace img if valid
    if img and 'static-maps' not in img:
        pattern_img = r'(id:\s*["\']' + re.escape(id_val) + r'["\']\s*,[\s\S]*?img:\s*["\']).*?(["\'])'
        replacement_img = rf'\g<1>{img}\g<2>'
        new_content = re.sub(pattern_img, replacement_img, new_content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Updated script.js')

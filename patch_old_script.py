import re
import json

with open('old_script.js', 'r', encoding='utf-16') as f:
    js = f.read()

# 1. Shift numbers FIRST
def shift_id(match):
    full_str = match.group(0)
    id_str = match.group(1)
    if '.' in id_str:
        major, minor = id_str.split('.')
        new_major = int(major) + 1
        new_id = f"{new_major}.{minor}"
    else:
        new_id = str(int(id_str) + 1)
    
    # We only shift if major >= 6
    if ('.' in id_str and int(major) >= 6) or ('.' not in id_str and int(id_str) >= 6):
        return full_str.replace(f'"{id_str}"', f'"{new_id}"')
    return full_str

# Shift IDs in the object definitions
js = re.sub(r'id:\s*"(\d+(?:\.\d+)?)"', shift_id, js)

# Shift titles
def shift_title(match):
    full_str = match.group(0)
    num_str = match.group(1)
    rest = match.group(2)
    if '.' in num_str:
        major, minor = num_str.split('.')
        if int(major) >= 6:
            return f'title: "{int(major)+1}.{minor} {rest}"'
    else:
        if int(num_str) >= 6:
            return f'title: "{int(num_str)+1}. {rest}"'
    return full_str

js = re.sub(r'title:\s*"(\d+(?:\.\d+)?)\.?\s*(.*?)"', shift_title, js)

# 2. Insert Park Yuzhnie Kultury AS 6
park_obj = '''    {
        id: "6",
        coords: [43.419568, 39.931381],
        title: "6. Парк Южные культуры",
        yandexUrl: "https://yandex.ru/maps/-/CXUcQTJe",
        category: "Природа/Парк",
        brief: "Дендрологический парк с экзотическими растениями.",
        desc: "Исторический парк в Адлере, основанный более 100 лет назад. Собраны растения со всего мира.",
        importance: "Ценный ботанический объект региона, оазис зелени рядом с морем.",
        fact: "Здесь растут секвойи, бамбук и цветут лотосы.",
        img: "https://avatars.mds.yandex.net/get-altay/239474/2a0000015d059ec428668e23acb2be76bb46/L_height"
    },
'''

# Find the insertion point: after id: "5"
js = re.sub(r'(id:\s*"5",.*?\},)', r'\1\n' + park_obj, js, flags=re.DOTALL)

# 3. Add scroll animation
js = re.sub(r'(document\.querySelector\(\'.info-content\'\)\.style\.display = \'block\';)', r'\1\n    setTimeout(() => { document.querySelector(\'.info-panel\').scrollIntoView({behavior: \'smooth\', block: \'center\'}); }, 100);', js)

# 4. Insert precise polygons
# Get precise polygons from current script.js
with open('script.js', 'r', encoding='utf-8') as f:
    curr_js = f.read()

oly_poly = re.search(r'var olympicPolygon = new ymaps\.Polygon\(\[\s*(\[\[.*?\]\])\s*\]', curr_js, flags=re.DOTALL).group(1)
tiso_poly = re.search(r'var tisoPolygon = new ymaps\.Polygon\(\[\s*(\[\[.*?\]\])\s*\]', curr_js, flags=re.DOTALL).group(1)

js = re.sub(r'var olympicPolygon = new ymaps\.Polygon\(\[\s*\[\[.*?\]\]\s*\]', f'var olympicPolygon = new ymaps.Polygon([\n        {oly_poly}\n    ]', js, flags=re.DOTALL)
js = re.sub(r'var tisoPolygon = new ymaps\.Polygon\(\[\s*\[\[.*?\]\]\s*\]', f'var tisoPolygon = new ymaps.Polygon([\n        {tiso_poly}\n    ]', js, flags=re.DOTALL)

# 5. Fix mainRouteCoords
# The old one had:
#     var mainRouteCoords = [
#        [43.413337, 39.93146], ...
#     ];
# We need to insert park_coords [43.419568, 39.931381] after [43.414441, 39.949121] (which is point 5 in old coords, wait, old coords had [43.413, 39.93] for point 1, what was point 5?)
# Let's check old_script.js for point 5 coords!
# 5 is Учебный центр Сириус. Its coords: [43.402484, 39.97237]
js = js.replace('[43.402484, 39.97237], [43.529718, 39.875345]', '[43.402484, 39.97237], [43.419568, 39.931381], [43.529718, 39.875345]')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

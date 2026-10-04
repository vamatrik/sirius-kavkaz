import re
import json

# Read the pristine script.js (utf-8)
with open('script.js', 'r', encoding='utf-8') as f:
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
# Ensure we only replace what needs to be replaced, avoiding backslash hell.
scroll_js = r"document.querySelector('.info-content').style.display = 'block';\n    setTimeout(() => { document.querySelector('.info-panel').scrollIntoView({behavior: 'smooth', block: 'center'}); }, 100);"
js = js.replace("document.querySelector('.info-content').style.display = 'block';", scroll_js)

# 4. Insert precise polygons
# I will use the PRECISE coordinates I fetched from links_data_fixed previously, which I'll inject manually here to avoid needing to parse the broken script.js again.
oly_poly = "[[43.40541400000001, 39.95288036943176], [43.40200599999999, 39.95409336943176], [43.401353324962514, 39.95433407228669], [43.40087552921666, 39.95499168471588], [43.40070064289388, 39.95589], [43.40087552921666, 39.956788315284115], [43.40337557586592, 39.96883731528412], [43.40385335189549, 39.969494927713306], [43.40773639373023, 39.97359592771331], [43.408389000000014, 39.973836630568236], [43.409041599238506, 39.97359592771331], [43.411214575825646, 39.97114792771331], [43.411692290028135, 39.970490315284124], [43.41186714462, 39.969592000000006], [43.411692290028135, 39.96869368471588], [43.40854834870058, 39.957417684715885], [43.40654438609684, 39.95377868471588], [43.40606663129091, 39.95312107228669]]"
tiso_poly = "[[43.529717999999995, 39.8730992117897], [43.528903876920864, 39.873400090358366], [43.52830789049668, 39.874222105894845], [43.52808974285286, 39.875344999999996], [43.52830789049668, 39.87646789410515], [43.52891990480467, 39.87772989410515], [43.5295158851816, 39.87855190964163], [43.53033, 39.8788527882103], [43.54005600000001, 39.8822607882103], [43.54086997253583, 39.88195990964164], [43.54146583482121, 39.88113789410515], [43.54168393408258, 39.880015], [43.54146583482121, 39.878892105894856], [43.53998286949843, 39.87655310589486], [43.53938699255669, 39.87573109035837], [43.53857299999999, 39.875430211789705]]"

js = re.sub(r'var olympicPolygon = new ymaps\.Polygon\(\[\s*\[\[.*?\]\]\s*\]', f'var olympicPolygon = new ymaps.Polygon([\n        {oly_poly}\n    ]', js, flags=re.DOTALL)
js = re.sub(r'var tisoPolygon = new ymaps\.Polygon\(\[\s*\[\[.*?\]\]\s*\]', f'var tisoPolygon = new ymaps.Polygon([\n        {tiso_poly}\n    ]', js, flags=re.DOTALL)

# 5. Fix mainRouteCoords
# The old one had: [43.402484, 39.97237] for Point 5.
# We append Park coords [43.419568, 39.931381] after it!
js = js.replace('[43.402484, 39.97237], [43.529718, 39.875345]', '[43.402484, 39.97237], [43.419568, 39.931381], [43.529718, 39.875345]')

# Make sure guide backgrounds don't have !important in js either, but this is script.js, guide backgrounds are in style.css which I already fixed in previous commits!
# Wait! In the pristine script.js from ca67836, showPage() and switchGuide() were STILL set up for SPA (Single Page Application)!
# Ah! I need to apply the "One-page scroll layout" changes to `switchGuide`!
# Because the pristine script.js has `showPage` and `switchGuide(targetId)`!

# Fix switchGuide for event
js = js.replace('function switchGuide(targetId) {', 'function switchGuide(event, targetId) {')
js = js.replace('event.target.classList.add(\'active\');', 'if(event && event.currentTarget) event.currentTarget.classList.add(\'active\');')
# Remove showPage
js = re.sub(r'function showPage\(pageId\) \{.*?\}\s*ymaps\.ready\(initMap\);', 'ymaps.ready(initMap);', js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

import requests
import re
url = 'https://yandex.ru/maps/org/prirodniy_ornitologicheskiy_park_v_imeretinskoy_nizmennosti/115591322258/'
html = requests.get(url).text
m = re.search(r'"coordinates":\[([\d\.]+),([\d\.]+)\]', html)
print(f'Lat: {m.group(2) if m else None}, Lon: {m.group(1) if m else None}')
m2 = re.search(r'<meta property="og:image" content="([^"]+)"', html)
print(f'Image: {m2.group(1) if m2 else None}')

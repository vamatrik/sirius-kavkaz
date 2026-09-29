import requests
import re
url = 'https://yandex.ru/maps/-/CXUcQTJe'
r = requests.get(url, allow_redirects=True)
html = r.text
lat, lon = None, None
m = re.search(r'poi%5Bpoint%5D=([\d\.]+)%2C([\d\.]+)', r.url)
if m:
    lon = float(m.group(1))
    lat = float(m.group(2))
else:
    m = re.search(r'"coordinates":\[([\d\.]+),([\d\.]+)\]', html)
    if m:
        lon = float(m.group(1))
        lat = float(m.group(2))
print(f'Lat: {lat}, Lon: {lon}')
m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
print(f'Image: {m.group(1) if m else None}')

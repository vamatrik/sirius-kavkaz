import json
import urllib.parse
import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('links_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    final_url = item['final_url']
    parsed = urllib.parse.urlparse(final_url)
    query = urllib.parse.parse_qs(parsed.query)
    
    found_exact = False
    
    if 'poi[point]' in query:
        lon, lat = query['poi[point]'][0].split(',')
        item['lon'] = float(lon)
        item['lat'] = float(lat)
        found_exact = True
    elif 'org' in final_url or 'geo' in final_url:
        # fetch HTML and find coordinates
        try:
            req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0'})
            res = urllib.request.urlopen(req, context=ctx)
            html = res.read().decode('utf-8', errors='ignore')
            # Yandex state has "coordinates":[lon,lat] or "coordinates":[lat,lon]? 
            # Usually it's lon, lat in geojson, but let's check exact match.
            # actually let's look for "coordinates":[lon, lat]
            # or in meta: <meta property="og:url" content="...ll=lon,lat...">
            match_ll = re.search(r'll=([0-9\.]+)(?:%2C|,)([0-9\.]+)', html)
            # Actually, yandex maps json state has the exact coordinates of the organization.
            # "coordinates":[39.939615,43.410295]
            match_coords = re.search(r'\"coordinates\":\[([0-9\.]+),([0-9\.]+)\]', html)
            if match_coords:
                # yandex json state usually has lon, lat
                item['lon'] = float(match_coords.group(1))
                item['lat'] = float(match_coords.group(2))
                found_exact = True
            else:
                # fallback to ll if not found exactly
                pass
        except Exception as e:
            print(f"Error {item['id']}: {e}")

    print(f"{item['id']}: lat={item['lat']} lon={item['lon']} exact={found_exact}")

with open('links_data_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

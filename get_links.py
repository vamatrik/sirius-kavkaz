import urllib.request, re, ssl, json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

links = [
    ('1', 'https://yandex.ru/maps/-/CXU8mL7w'),
    ('2', 'https://yandex.ru/maps/-/CXU8uU4D'),
    ('3.1', 'https://yandex.ru/maps/-/CXU8uRMW'),
    ('3.2', 'https://yandex.ru/maps/-/CXU8uZKO'),
    ('3.3', 'https://yandex.ru/maps/-/CXU8uKYZ'),
    ('3.4', 'https://yandex.ru/maps/-/CXU8uSP0'),
    ('3.5', 'https://yandex.ru/maps/-/CXU8u8iV'),
    ('3.6', 'https://yandex.ru/maps/-/CXU8uL1U'),
    ('3.7', 'https://yandex.ru/maps/-/CXU8yR5o'),
    ('3.7_2', 'https://yandex.ru/maps/-/CXU8y6kB'),
    ('3.8', 'https://yandex.ru/maps/-/CXU8yS8c'),
    ('4', 'https://yandex.ru/maps/-/CXU8y-MR'),
    ('5', 'https://yandex.ru/maps/-/CXU85QOt'),
    ('6.1', 'https://yandex.com/maps/-/CXU8yN8j'),
    ('6.2', 'https://yandex.com/maps/-/CXU85Fif'),
    ('6.3', 'https://yandex.com/maps/org/ruiny_vizantiyskoy_kreposti_viii_x_vv_/205246609730'),
    ('6.4', 'https://yandex.ru/maps/-/CXU8BS-Z'),
    ('7', 'https://yandex.ru/maps/org/kanyon_chyortovy_vorota/149726264059/'),
    ('8', 'https://yandex.ru/maps/org/ao_plemennoy_forelevodcheskiy_zavod_adler/1069639997/'),
    ('9', 'https://yandex.ru/maps/org/akhshtyrskaya_peshchera/145496035348/'),
    ('10', 'https://yandex.ru/maps/org/skaypark/1210593378/'),
    ('11', 'https://yandex.ru/maps/org/kurort_krasnaya_polyana/1214311519/'),
    ('12', 'https://yandex.ru/maps/-/CXU8u84K'),
    ('13.1', 'https://yandex.ru/maps/org/roza_pik/158962977869/'),
    ('13.2', 'https://yandex.ru/maps/-/CXU850zZ'),
    ('14', 'https://yandex.ru/maps/org/gorno_turisticheskiy_tsentr_gazprom/43313807333/')
]

results = []
for id, url in links:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        res = urllib.request.urlopen(req, context=ctx)
        final_url = res.geturl()
        html = res.read().decode('utf-8', errors='ignore')
        
        # parse coordinates
        lat, lon = None, None
        
        # try to parse from coordinates config or og:image
        match_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
        img = match_img.group(1) if match_img else ''
        
        # In Yandex maps URL ll=lon,lat
        match_ll = re.search(r'll=([0-9\.]+)(?:%2C|,)([0-9\.]+)', final_url)
        if match_ll:
            lon, lat = match_ll.group(1), match_ll.group(2)
        else:
            # try to parse from html state
            match_coords = re.search(r'\"coordinates\":\[([0-9\.]+),([0-9\.]+)\]', html)
            if match_coords:
                lon, lat = match_coords.group(1), match_coords.group(2)
        
        results.append({
            'id': id,
            'lat': float(lat) if lat else 0.0,
            'lon': float(lon) if lon else 0.0,
            'img': img,
            'url': url,
            'final_url': final_url
        })
        print(f"Done {id}")
    except Exception as e:
        print(f"Error {id}: {e}")

with open('links_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

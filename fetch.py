import urllib.request, re, ssl
ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
url = 'https://yandex.ru/maps/org/krugozor_yefremova/122559507832/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8', errors='ignore')
match = re.search(r'"coordinates":\[([0-9\.]+),([0-9\.]+)\]', html)
if match:
    print(f"coords: {match.group(1)}, {match.group(2)}")
match_img = re.search(r'<meta property="og:image" content="([^"]+)"', html)
if match_img:
    print(f"img: {match_img.group(1)}")

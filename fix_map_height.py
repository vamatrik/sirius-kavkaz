with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div id="map"></div>', '<div id="map" style="width: 100%; height: 600px; min-height: 600px; background-color: #e0e0e0; border: 2px solid red;"></div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

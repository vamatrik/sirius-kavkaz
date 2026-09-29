import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<section id="guide" class="page">', '<section id="guide" class="page" style="min-height: calc(100vh - 74px); background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url(https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height); background-size: cover; background-position: center; padding: 20px;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

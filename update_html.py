import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add new tabs to Guide
old_tabs = '''                <ul id="guide-nav">
                    <li class="active" onclick="switchGuide(event, 'guide-intro')">Введение</li>
                    <li onclick="switchGuide(event, 'guide-geo')">География и природа</li>
                    <li onclick="switchGuide(event, 'guide-eco')">Экология</li>
                    <li onclick="switchGuide(event, 'guide-pop')">Популяризация науки</li>
                </ul>'''

new_tabs = '''                <ul id="guide-nav">
                    <li class="active" onclick="switchGuide(event, 'guide-brief')">Вкратце о маршруте</li>
                    <li onclick="switchGuide(event, 'guide-intro')">Введение</li>
                    <li onclick="switchGuide(event, 'guide-geo')">География и природа</li>
                    <li onclick="switchGuide(event, 'guide-eco')">Экология</li>
                    <li onclick="switchGuide(event, 'guide-flora')">Флора и фауна</li>
                    <li onclick="switchGuide(event, 'guide-pop')">Популяризация науки</li>
                </ul>'''
html = html.replace(old_tabs, new_tabs)

# Add new panes
new_panes = '''                <!-- Pane: Brief -->
                <div id="guide-brief" class="guide-pane active">
                    <h3>Вкратце о маршруте</h3>
                    <p>Наш маршрут пролегает от теплого побережья Имеретинской низменности, где современные архитектурные шедевры соседствуют с яхтенными маринами и пляжами, до заснеженных вершин Красной Поляны. Вы проедете через уникальные реликтовые леса, увидите древние пещеры, насладитесь видами горных каньонов и прикоснетесь к передовым технологиям в Олимпийском парке.</p>
                </div>
                <!-- Pane: Intro -->'''
html = html.replace('<!-- Pane: Intro -->', new_panes).replace('<div id="guide-intro" class="guide-pane active">', '<div id="guide-intro" class="guide-pane">')

flora_pane = '''                <!-- Pane: Flora -->
                <div id="guide-flora" class="guide-pane">
                    <h3>Флора и фауна</h3>
                    <p>Кавказский биосферный заповедник и национальный парк Сочи берегут уникальное биоразнообразие. Здесь встречаются реликтовые леса колхидского типа, самшит, тис ягодный. В горах обитают кавказские серны, бурые медведи, а в небе парят беркуты и белоголовые сипы. Орнитологический парк в Имеретинской низменности стал домом для сотен видов перелетных птиц.</p>
                </div>
                <!-- Pane: Pop -->'''
html = html.replace('<!-- Pane: Pop -->', flora_pane)

# Change info panel structure to support masonry
old_info_content = '''                    <div class="info-media">
                        <img id="p-img" src="" alt="">
                        <div id="p-video" style="display: none;"></div>
                    </div>
                    <div class="info-text">'''

new_info_content = '''                    <div id="p-gallery-top" class="masonry-gallery"></div>
                    <div id="p-video-container" style="display: none; margin-bottom: 20px;"></div>
                    <div class="info-text">'''
html = html.replace(old_info_content, new_info_content)

html = html.replace('                        </div>\n                    </div>\n                </div>', '                        </div>\n                    </div>\n                    <div id="p-gallery-bottom" class="masonry-gallery"></div>\n                </div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

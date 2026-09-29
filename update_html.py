import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

home_replacement = '''
<div class="hero-content">
    <div class="hero-card">
        <h2>От моря к Кавказу</h2>
        <p>Добро пожаловать в интерактивный путеводитель по уникальному маршруту, соединяющему побережье Черного моря и заснеженные вершины Кавказских гор.</p>
        <button onclick="showPage('guide')" class="btn">Читать путеводитель</button>
        <button onclick="showPage('route')" class="btn btn-primary">Смотреть маршрут</button>
    </div>
</div>'''
html = re.sub(r'(<section id="home"[^>]*>).*?(</section>)', r'\1' + home_replacement + r'\2', html, flags=re.DOTALL)

guide_replacement = '''
<h2>Путеводитель по региону</h2>
<div class="guide-container">
    <div class="guide-sidebar">
        <ul id="guide-nav">
            <li class="active" onclick="switchGuide('guide-intro')">Введение</li>
            <li onclick="switchGuide('guide-geo')">География и природа</li>
            <li onclick="switchGuide('guide-eco')">Экономика и ресурсы</li>
            <li onclick="switchGuide('guide-pop')">Население и культура</li>
        </ul>
    </div>
    <div class="guide-content">
        <div id="guide-intro" class="guide-pane active">
            <h3>Обзор региона</h3>
            <p>Наш маршрут проходит по уникальной территории — от федеральной территории «Сириус» (Имеретинская низменность) через Хостинский район Сочи к горному кластеру Красной Поляны. Это место, где субтропики встречаются с ледниками.</p>
        </div>
        <div id="guide-geo" class="guide-pane">
            <h3>География и природа</h3>
            <p>Регион отличается уникальным климатом: у моря царят влажные субтропики, а в горах — альпийский пояс. Здесь расположены реликтовые леса (например, Тисо-самшитовая роща, пережившая ледниковый период) и глубокие ущелья рек (Мзымта, Хоста).</p>
        </div>
        <div id="guide-eco" class="guide-pane">
            <h3>Экономика и ресурсы</h3>
            <p>Основа экономики — туризм (пляжный и горнолыжный), а также наука и образование (центр «Сириус»). Также развито сельское хозяйство — здесь выращивают чай, цитрусовые, а в реках разводят ценные породы рыб (форелевое хозяйство).</p>
        </div>
        <div id="guide-pop" class="guide-pane">
            <h3>Население и культура</h3>
            <p>Сочи — многонациональный город. Здесь переплелись культуры русских, армян, греков, грузин и адыгов. Олимпийское наследие сильно повлияло на современный облик города, превратив его в курорт мирового уровня.</p>
        </div>
    </div>
</div>
'''
html = re.sub(r'(<section id="guide"[^>]*>).*?(</section>)', r'\1' + guide_replacement + r'\2', html, flags=re.DOTALL)

# Let's fix route-container in HTML: just wrap info-panel contents in a div for layout if needed
route_replacement = '''
<div class="route-container">
    <div class="map-container">
        <div id="map"></div>
    </div>
    <div class="info-panel">
        <div class="empty-state">
            <h3>Выберите точку на карте</h3>
            <p>Нажмите на любой маркер, чтобы узнать подробности.</p>
        </div>
        <div class="info-content" style="display: none;">
            <div class="info-media">
                <img id="p-img" src="" alt="">
                <div id="p-video" style="display: none;"></div>
            </div>
            <div class="info-text">
                <div class="p-tags">
                    <span class="tag" id="p-category">Категория</span>
                </div>
                <h3 id="p-title"><a href="#" target="_blank" id="p-title-link" style="color: inherit; text-decoration: none;">Название точки</a></h3>
                
                <div class="info-block">
                    <h4>Вкратце:</h4>
                    <p id="p-brief"></p>
                </div>
                
                <div class="info-block">
                    <h4>Описание:</h4>
                    <p id="p-desc"></p>
                </div>
                
                <div class="info-block">
                    <h4>Значение:</h4>
                    <p id="p-importance"></p>
                </div>
                
                <div class="info-block">
                    <h4>Интересный факт:</h4>
                    <p id="p-fact"></p>
                </div>
            </div>
        </div>
    </div>
</div>
'''
html = re.sub(r'<div class="route-container">.*?</div>\s*</section>', route_replacement + '</section>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

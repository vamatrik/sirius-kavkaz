import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Home height
html = html.replace('<section id="home" class="page active">', '<section id="home" class="page active" style="min-height: calc(100vh - 74px);">')
html = html.replace('<section id="home" class="page active hero">', '<section id="home" class="page active" style="min-height: calc(100vh - 74px);">')

# Fix Route
route_replacement = '''
    <section id="route" class="page">
        <div class="route-container" style="padding: 20px;">
            <h2 style="text-align: center; color: #333; margin-bottom: 20px;">Интерактивный маршрут</h2>
            <div class="map-container">
                <div id="map"></div>
            </div>
            <div class="info-panel">
                <div class="empty-state" id="empty-state">
                    <h3>Выберите точку на карте</h3>
                    <p>Нажмите на любой маркер, чтобы узнать подробности.</p>
                </div>
                <div class="info-content" id="info-content" style="display: none;">
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
    </section>
'''
html = re.sub(r'<section id="route"[^>]*>.*?</section>', route_replacement, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

import json
import math
import re

def convex_hull(points):
    # points: list of (lon, lat)
    points = sorted(set(points))
    if len(points) <= 1: return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def get_buffered_polygon(latlon_points, padding_m):
    # Generate circle around each point
    all_points = []
    for lat, lon in latlon_points:
        lat_scale = 111320.0
        lon_scale = 111320.0 * math.cos(math.radians(lat))
        
        for angle_deg in range(0, 360, 15):
            angle = math.radians(angle_deg)
            dy = padding_m * math.sin(angle)
            dx = padding_m * math.cos(angle)
            
            p_lat = lat + dy / lat_scale
            p_lon = lon + dx / lon_scale
            all_points.append((p_lon, p_lat))
            
    hull = convex_hull(all_points)
    # yandex expects [lat, lon]
    return [[p[1], p[0]] for p in hull]

with open('links_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Rebuild coords dict
coords = {item['id']: [item['lat'], item['lon']] for item in data}

# User overrides:
# 3.7 is Museum Panulli and Sochi Autodrom (merge 3.7 and 3.7_2)
# We will create two points, both with ID "3.7"
# 6.3 is Bukovaya polyana (was 6.4), 6.4 is Fortress (was 6.3)
# 12 is Krugozor Efremova (43.673304, 40.182899)
# 13.1 is Ratusha, 13.2 is Roza Pik

coords['12'] = [43.673304, 40.182899]
img_12 = "https://avatars.mds.yandex.net/get-altay/14090612/2a00000195f2ba324855abb9bbb440361a3c/L_height"

points_js = f'''const routePoints = [
    {{
        id: "1",
        coords: {coords['1']},
        title: "1. Имеретинский морской вокзал",
        yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w",
        category: "Транспорт и Архитектура",
        brief: "Главные морские ворота Адлерского района.",
        desc: "Отправная точка нашего маршрута. Морской вокзал не только обслуживает пассажиров, но и является интересным архитектурным объектом на побережье, символизируя связь города с морем.",
        importance: "Морское сообщение исторически играло ключевую роль в развитии региона.",
        fact: "Здание вокзала часто становится местом для городских фотосессий благодаря красивому виду на закаты.",
        img: "https://avatars.mds.yandex.net/get-altay/1005628/2a000001892c348aa71914d331716792e2ab/L_height"
    }},
    {{
        id: "2",
        coords: {coords['2']},
        title: "2. Олимпийский пляж",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D",
        category: "Отдых",
        brief: "Крутой современный пляж в Имеретинской низменности.",
        desc: "Несмотря на название, этот пляж находится у моря. Это современная зона отдыха.",
        importance: "Демонстрирует, как горные курорты Сочи развивают комплексный отдых: от снежных вершин до теплого моря.",
        fact: "Пляж регулярно получает международную награду «Голубой флаг» за чистоту воды и инфраструктуру.",
        img: "https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height"
    }},
    {{
        id: "3.1",
        coords: {coords['3.1']},
        title: "3.1 Стадион Фишт",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uRMW",
        category: "Олимпийский парк",
        brief: "Легендарный стадион, принимавший открытие и закрытие Олимпиады.",
        desc: "Сейчас используется для проведения футбольных матчей.",
        importance: "Главный символ Олимпиады-2014.",
        fact: "Футбольные матчи здесь иногда отменяют или ставят на паузу из-за угроз с воздуха.",
        img: "https://avatars.mds.yandex.net/get-altay/1246719/2a00000163996b11cf8fa6eb65efad6ba738/L_height"
    }},
    {{
        id: "3.2",
        coords: {coords['3.2']},
        title: "3.2 Поющие фонтаны",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uZKO",
        category: "Олимпийский парк",
        brief: "Грандиозное вечернее шоу воды, света и музыки.",
        desc: "Фонтан в виде жар-птицы. Вечером (если нет угрозы) здесь проходит потрясающе красивое шоу под классическую и современную музыку.",
        importance: "Центр притяжения всех туристов в Сириусе.",
        fact: "Фонтан может выбрасывать струи воды на высоту до 70 метров.",
        videoUrl: "https://www.youtube.com/embed/dQw4w9WgXcQ"
    }},
    {{
        id: "3.3",
        coords: {coords['3.3']},
        title: "3.3 ЛД Айсберг",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uKYZ",
        category: "Олимпийский парк",
        brief: "Ледовый дворец спорта с уникальной архитектурой.",
        desc: "Здесь проходят самые красивые ледовые шоу знаменитых фигуристов.",
        importance: "Сохранение ледовых традиций России после Олимпиады.",
        fact: "Форма здания повторяет траекторию полёта фигуриста во время прыжка.",
        img: "https://avatars.mds.yandex.net/get-altay/813485/2a000001603403bc8148cf35a37122b90fdb/L_height"
    }},
    {{
        id: "3.4",
        coords: {coords['3.4']},
        title: "3.4 Музей Леонардо да Винчи",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uSP0",
        category: "Олимпийский парк",
        brief: "Механические изобретения гения.",
        desc: "В экспозиции представлены реконструкции механизмов по чертежам Леонардо.",
        importance: "Популяризация инженерной мысли.",
        fact: "Многие экспонаты можно трогать и приводить в движение.",
        img: "https://avatars.mds.yandex.net/get-altay/11421964/2a0000018cf241332914b3272b98bdf28da0/L_height"
    }},
    {{
        id: "3.5",
        coords: {coords['3.5']},
        title: "3.5 Музей Теслы",
        yandexUrl: "https://yandex.ru/maps/-/CXU8u8iV",
        category: "Олимпийский парк",
        brief: "Музей электричества.",
        desc: "Рядом с музеем Да Винчи. Здесь рассказывают об электричестве и проводят электрическое шоу (с музыкой и молниями).",
        importance: "Обучение физике через развлечение.",
        fact: "Генераторы Теслы создают настоящие молнии длиной в несколько метров.",
        img: "https://avatars.mds.yandex.net/get-altay/5548986/2a0000018400c3d368869bb8c1bfe2998c7d/L_height"
    }},
    {{
        id: "3.6",
        coords: {coords['3.6']},
        title: "3.6 Концертный центр Сириус",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uL1U",
        category: "Олимпийский парк",
        brief: "Крутой концертный зал с потрясающей акустикой.",
        desc: "Новый центр, включающий Главную сцену на 1200 мест.",
        importance: "Территория получила новое научно-культурное содержание.",
        fact: "Акустика зала разрабатывалась ведущими мировыми специалистами.",
        img: "https://avatars.mds.yandex.net/get-altay/18708590/2a0000019d952cd5db8c59c726b844e77494/L_height"
    }},
    {{
        id: "3.7",
        coords: {coords['3.7']},
        title: "3.7 Сочи Автодром",
        yandexUrl: "https://yandex.ru/maps/-/CXU8yR5o",
        category: "Олимпийский парк",
        brief: "Гоночная трасса.",
        desc: "Единственная в России трасса, принимавшая Гран-при Формулы 1.",
        importance: "Интеграция автоспорта мирового уровня в олимпийскую инфраструктуру.",
        fact: "Трасса проложена прямо между олимпийскими стадионами.",
        img: "https://avatars.mds.yandex.net/get-altay/1532977/2a00000168d3053a97089db3ae8c03f187b2/L_height"
    }},
    {{
        id: "3.7",
        coords: {coords['3.7_2']},
        title: "3.7 Музей Панулли",
        yandexUrl: "https://yandex.ru/maps/-/CXU8y6kB",
        category: "Олимпийский парк",
        brief: "Музей спортивных авто.",
        desc: "Коллекция уникальных спортивных и гоночных автомобилей.",
        importance: "Автоспорт и история.",
        fact: "Здесь собраны уникальные модели болидов со всего мира.",
        img: "https://avatars.mds.yandex.net/get-altay/15426074/2a00000196c05ad6562107939f6e5c6327cb/L_height"
    }},
    {{
        id: "3.8",
        coords: {coords['3.8']},
        title: "3.8 Сочи Парк",
        yandexUrl: "https://yandex.ru/maps/-/CXU8yS8c",
        category: "Олимпийский парк",
        brief: "Первый тематический парк развлечений в России.",
        desc: "Аттракционы мирового уровня, оформленные в стиле русских сказок.",
        importance: "Главный семейный развлекательный центр юга России.",
        fact: "Аттракцион «Квантовый скачок» — самая быстрая и высокая горка в России.",
        img: "https://avatars.mds.yandex.net/get-altay/11368589/2a0000018bc478cc293ceb2e61b8dd97abd9/L_height"
    }},
    {{
        id: "4",
        coords: {coords['4']},
        title: "4. Орнитологический парк",
        yandexUrl: "https://yandex.ru/maps/-/CXU8y-MR",
        category: "Природа",
        brief: "Парк, где можно покормить почти ручных птиц.",
        desc: "Особо охраняемая природная территория. Создана для сохранения мест отдыха перелетных птиц во время миграции.",
        importance: "Сохранение экосистемы Имеретинской низменности.",
        fact: "Здесь останавливается более 200 видов птиц, многие из которых занесены в Красную книгу.",
        img: "https://avatars.mds.yandex.net/get-altay/813485/2a0000015ea829aadbed291bb1461e00fe06/L_height"
    }},
    {{
        id: "5",
        coords: {coords['5']},
        title: "5. Учебный центр Сириус",
        yandexUrl: "https://yandex.ru/maps/-/CXU85QOt",
        category: "Наука и образование",
        brief: "Образовательный центр для одаренных детей.",
        desc: "Здесь круглый год проходят учебные мероприятия для талантливых школьников со всей России по науке, искусству и спорту.",
        importance: "Главный образовательный проект страны, созданный на базе олимпийской инфраструктуры.",
        fact: "Рядом находится макет легендарного Бурана, куда водят экскурсии.",
        img: "https://avatars.mds.yandex.net/get-altay/1439437/2a0000018c69b53c549d34564a36c867eff9/L_height"
    }},
    {{
        id: "6.1",
        coords: {coords['6.1']},
        title: "6.1 Тис-великан",
        yandexUrl: "https://yandex.com/maps/-/CXU8yN8j",
        category: "Тисо-самшитовая роща",
        brief: "Древнейшее дерево Кавказа.",
        desc: "Огромное дерево, возраст которого исчисляется тысячелетиями.",
        importance: "Живой памятник доледниковой эпохи.",
        fact: "Тис ягодный растет очень медленно — всего на 1 мм в год в толщину.",
        img: "https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height"
    }},
    {{
        id: "6.2",
        coords: {coords['6.2']},
        title: "6.2 Каменный лабиринт",
        yandexUrl: "https://yandex.com/maps/-/CXU85Fif",
        category: "Тисо-самшитовая роща",
        brief: "Природный тектонический разлом.",
        desc: "Глубокие трещины в известняковых скалах, поросшие мхом и папоротниками.",
        importance: "Демонстрирует геологическую историю формирования Кавказских гор.",
        fact: "Здесь сохраняется свой микроклимат, более влажный и прохладный.",
        img: "https://avatars.mds.yandex.net/get-altay/15417312/2a00000197a090ac71ece0503eae945aa454/L_height"
    }},
    {{
        id: "6.3",
        coords: {coords['6.4']},
        title: "6.3 Буковая поляна",
        yandexUrl: "https://yandex.ru/maps/-/CXU8BS-Z",
        category: "Тисо-самшитовая роща",
        brief: "Красивая поляна в лесу.",
        desc: "Участок древнего леса.",
        importance: "Формирует уникальный микроклимат.",
        fact: "Деревья здесь имеют огромный возраст.",
        img: "https://avatars.mds.yandex.net/get-altay/13461681/2a00000190f9040a9bc57bc0c0059d1e38c4/L_height"
    }},
    {{
        id: "6.4",
        coords: {coords['6.3']},
        title: "6.4 Хостинская крепость",
        yandexUrl: "https://yandex.com/maps/org/ruiny_vizantiyskoy_kreposti_viii_x_vv_/205246609730",
        category: "Тисо-самшитовая роща",
        brief: "Развалины древней генуэзской крепости.",
        desc: "Остатки оборонительных сооружений VIII-X веков.",
        importance: "Свидетельство того, что эти территории активно осваивались в эпоху Средневековья.",
        fact: "Стены крепости так плотно поросли растениями, что почти сливаются с лесом.",
        img: "https://avatars.mds.yandex.net/get-altay/10812438/2a0000018c3f84bfb686579f37e3ad5380f0/L_height"
    }},
    {{
        id: "7",
        coords: {coords['7']},
        title: "7. Каньон Чёртовы ворота",
        yandexUrl: "https://yandex.ru/maps/org/kanyon_chyortovy_vorota/149726264059/",
        category: "Природа / Гастрономия",
        brief: "Глубокий каньон и отличный ресторанчик.",
        desc: "Ущелье с отвесными скалами высотой до 50 метров.",
        importance: "Популярное место для эко-туризма и сплавов на сапах.",
        fact: "В самом узком месте ширина каньона составляет всего около 3 метров.",
        img: "https://avatars.mds.yandex.net/get-altay/6310045/2a000001902b6cd5dd108acfa347bda76539/L_height"
    }},
    {{
        id: "8",
        coords: {coords['8']},
        title: "8. Форелевое хозяйство",
        yandexUrl: "https://yandex.ru/maps/org/ao_plemennoy_forelevodcheskiy_zavod_adler/1069639997/",
        category: "Экономика",
        brief: "Племенной форелеводческий завод «Адлер».",
        desc: "Крупнейшее в России хозяйство по выращиванию форели.",
        importance: "Успешное использование горных водных ресурсов для сельского хозяйства.",
        fact: "Хозяйство вывело уникальную породу форели — «Адлерскую янтарную».",
        img: "https://avatars.mds.yandex.net/get-altay/374295/2a0000015b2171316393e398f4c7f73309ad/L_height"
    }},
    {{
        id: "9",
        coords: {coords['9']},
        title: "9. Ахштырская пещера",
        yandexUrl: "https://yandex.ru/maps/org/akhshtyrskaya_peshchera/145496035348/",
        category: "Археология",
        brief: "Пещера, где жили древние люди.",
        desc: "Находится высоко над рекой Мзымта. Первые люди поселились здесь около 70 тысяч лет назад.",
        importance: "Важнейший археологический памятник эпохи палеолита на Кавказе.",
        fact: "В пещере обнаружены орудия труда неандертальцев и кроманьонцев.",
        img: "https://avatars.mds.yandex.net/get-altay/4716261/2a00000182277979173ca801adde160bdb7d/L_height"
    }},
    {{
        id: "10",
        coords: {coords['10']},
        title: "10. Скай Парк (Skypark)",
        yandexUrl: "https://yandex.ru/maps/org/skaypark/1210593378/",
        category: "Экстрим",
        brief: "Парк высотных приключений над Ахштырским ущельем.",
        desc: "Один из самых длинных подвесных пешеходных мостов в мире.",
        importance: "Центр экстремального туризма, привлекающий гостей со всего мира.",
        fact: "Длина подвесного моста Скайбридж составляет 439 метров.",
        img: "https://avatars.mds.yandex.net/get-altay/15112342/2a00000194ef20b6759a5c781dda7d098022/L_height"
    }},
    {{
        id: "11",
        coords: {coords['11']},
        title: "11. Курорт Красная Поляна",
        yandexUrl: "https://yandex.ru/maps/org/kurort_krasnaya_polyana/1214311519/",
        category: "Горный туризм",
        brief: "Бывший Горки Город, мощный туристический кластер.",
        desc: "Современный курорт, расположившийся на нескольких высотных уровнях.",
        importance: "Один из локомотивов горного туризма в России.",
        fact: "В Нижнем городе (Поляна 540) архитектура стилизована под европейские города.",
        img: "https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height"
    }},
    {{
        id: "12",
        coords: {coords['12']},
        title: "12. Кругозор Ефремова",
        yandexUrl: "https://yandex.ru/maps/-/CXU8fXK5",
        category: "География",
        brief: "Смотровая площадка на горе Монашка.",
        desc: "Находится как раз у Эсто-Садка. Отсюда открываются панорамные виды на долину Мзымты.",
        importance: "Точка названа в честь географа и исследователя Юрия Ефремова.",
        fact: "С площадки можно одновременно увидеть и поселок, и вершины Главного Кавказского хребта.",
        img: "{img_12}"
    }},
    {{
        id: "13.1",
        coords: {coords['13.2']},
        title: "13.1 Ратуша Роза Хутор",
        yandexUrl: "https://yandex.ru/maps/-/CXU850zZ",
        category: "Архитектура",
        brief: "Главная площадь и символ курорта.",
        desc: "Центральная площадь с часовой башней.",
        importance: "Архитектурная доминанта, задающая стиль всему курорту.",
        fact: "Башня Ратуши стилизована под башню железнодорожного вокзала Сочи.",
        img: "https://avatars.mds.yandex.net/get-altay/13970739/2a0000019199a98ce17675787a1c6a1c1404/L_height"
    }},
    {{
        id: "13.2",
        coords: {coords['13.1']},
        title: "13.2 Роза Пик",
        yandexUrl: "https://yandex.ru/maps/org/roza_pik/158962977869/",
        category: "Высокогорье",
        brief: "Вершина хребта Аибга, 2320 м.",
        desc: "Высшая точка нашего маршрута. Подъем сюда осуществляется по трем канатным дорогам.",
        importance: "Кульминация идеи маршрута: мы поднялись от уровня моря высоко в горы.",
        fact: "Даже в разгар лета на северных склонах здесь может лежать снег.",
        img: "https://avatars.mds.yandex.net/get-altay/11622009/2a0000019073c9497e964506f53f0614a419/L_height"
    }},
    {{
        id: "14",
        coords: {coords['14']},
        title: "14. Газпром Поляна",
        yandexUrl: "https://yandex.ru/maps/org/gorno_turisticheskiy_tsentr_gazprom/43313807333/",
        category: "Горный туризм",
        brief: "Уютный и престижный курорт (зоны Лаура и Альпика).",
        desc: "Здесь проводились соревнования по биатлону и лыжным гонкам.",
        importance: "Дополняет картину горного кластера, предлагая круглогодичный отдых.",
        fact: "Канатная дорога типа 3S на Газпроме — одна из самых длинных в мире.",
        img: "https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height"
    }}
];
'''
# JS code
js_bottom = '''
// Навигация
function showPage(pageId) {
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.classList.remove('active');
    });
    
    document.getElementById(pageId).classList.add('active');
    document.getElementById('link-' + pageId).classList.add('active');

    if(pageId === 'route' && window.mapObj) {
        window.mapObj.container.fitToViewport();
    }
}

ymaps.ready(initMap);

function initMap() {
    window.mapObj = new ymaps.Map("map", {
        center: [43.5500, 40.0500],
        zoom: 10,
        controls: ['zoomControl', 'typeSelector', 'fullscreenControl']
    });

    // Олимпийский парк
    var olympicPolygon = new ymaps.Polygon([
        POLY_OLYMPIC
    ], {
        hintContent: 'Олимпийский парк'
    }, {
        fillColor: "#007bff33",
        strokeColor: "#007bff",
        strokeOpacity: 0.8,
        strokeWidth: 2
    });
    window.mapObj.geoObjects.add(olympicPolygon);

    // Тисо-самшитовая роща
    var tisoPolygon = new ymaps.Polygon([
        POLY_TISO
    ], {
        hintContent: 'Тисо-самшитовая роща'
    }, {
        fillColor: "#28a74533",
        strokeColor: "#28a745",
        strokeOpacity: 0.8,
        strokeWidth: 2
    });
    window.mapObj.geoObjects.add(tisoPolygon);

    var mainRouteCoords = [
        ROUTE_LINE
    ];

    var mainPolyline = new ymaps.Polyline(mainRouteCoords, {}, {
        strokeColor: "#17a2b8",
        strokeWidth: 4,
        strokeOpacity: 0.7,
        strokeStyle: 'shortdash'
    });
    window.mapObj.geoObjects.add(mainPolyline);

    routePoints.forEach((point) => {
        let presetStyle = 'islands#blueIcon';
        if(point.id.includes('.')) {
            presetStyle = 'islands#lightBlueIcon';
        }

        var placemark = new ymaps.Placemark(point.coords, {
            hintContent: point.title,
            iconContent: point.id 
        }, {
            preset: presetStyle
        });
        
        placemark.events.add('click', function () {
            showPointInfo(point);
        });

        window.mapObj.geoObjects.add(placemark);
    });

    window.mapObj.setBounds(window.mapObj.geoObjects.getBounds(), {
        checkZoomRange: true,
        zoomMargin: 30
    });
}

function showPointInfo(point) {
    document.querySelector('.empty-state').style.display = 'none';
    document.querySelector('.info-content').style.display = 'block';
    
    const imgEl = document.getElementById('p-img');
    const videoEl = document.getElementById('p-video');

    if (point.videoUrl) {
        imgEl.style.display = 'none';
        videoEl.style.display = 'block';
        videoEl.innerHTML = \`<iframe width="100%" height="100%" src="${point.videoUrl}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\`;
    } else {
        videoEl.style.display = 'none';
        videoEl.innerHTML = '';
        imgEl.style.display = 'block';
        imgEl.src = point.img;
    }

    document.getElementById('p-category').innerText = point.category;
    document.getElementById('p-title-link').innerText = point.title;
    if (point.yandexUrl) {
        document.getElementById('p-title-link').href = point.yandexUrl;
        document.getElementById('p-title-link').style.pointerEvents = "auto";
        document.getElementById('p-title-link').style.textDecoration = "underline";
    } else {
        document.getElementById('p-title-link').removeAttribute('href');
        document.getElementById('p-title-link').style.pointerEvents = "none";
        document.getElementById('p-title-link').style.textDecoration = "none";
    }
    document.getElementById('p-brief').innerText = point.brief;
    document.getElementById('p-desc').innerText = point.desc;
    document.getElementById('p-importance').innerText = point.importance;
    document.getElementById('p-fact').innerText = point.fact;
}
'''

olympic_pts = [coords[k] for k in ["3.1","3.2","3.3","3.4","3.5","3.6","3.7","3.7_2","3.8"]]
tiso_pts = [coords[k] for k in ["6.1","6.2","6.3","6.4"]]

# Generate buffered polygons (150m for olympic, 250m for tiso to encompass well)
poly_olympic = get_buffered_polygon(olympic_pts, 200)
poly_tiso = get_buffered_polygon(tiso_pts, 250)

js_bottom = js_bottom.replace('POLY_OLYMPIC', json.dumps(poly_olympic))
js_bottom = js_bottom.replace('POLY_TISO', json.dumps(poly_tiso))

# Line
line_coords = [
    coords['1'], coords['2'],
    coords['3.2'], coords['3.7'], # Olympic enter/exit
    coords['4'], coords['5'],
    coords['6.1'], coords['6.3'], # Tiso enter/exit
    coords['7'], coords['8'], coords['9'], coords['10'],
    coords['11'], coords['12'], coords['13.2'], coords['13.1'], coords['14']
]
js_bottom = js_bottom.replace('ROUTE_LINE', json.dumps(line_coords)[1:-1])

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(points_js + js_bottom)
print("done")

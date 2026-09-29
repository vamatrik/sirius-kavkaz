import json
import math

with open('links_data_fixed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

coords = {item['id']: [item['lat'], item['lon']] for item in data}

# Add Park as point 6
park_coords = [43.419568, 39.931381]
park_img = "https://avatars.mds.yandex.net/get-altay/239474/2a0000015d059ec428668e23acb2be76bb46/L_height"
park_url = "https://yandex.ru/maps/-/CXUcQTJe"

# We need to shift numbers in the JS array!
# Tiso 6.1..6.4 -> 7.1..7.4
# 7 (Vorota) -> 8
# 8 (Adler) -> 9
# 9 (Ahshtir) -> 10
# 10 (Skypark) -> 11
# 11 (Krasnaya polyana) -> 12
# 12 (Krugozor efremova) -> 13
# 13.1, 13.2 (Roza ratusha/pik) -> 14.1, 14.2
# 14 (Gazprom) -> 15

points_js = f'''
const routePoints = [
    {{ id: "1", coords: {coords['2']}, title: "1. Имеретинский морской вокзал", yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w", category: "Транспорт/Отдых", brief: "Яхтенная марина и порт.", desc: "Порт, построенный для приема грузовых судов во время олимпийской стройки, теперь превращен в яхтенную марину.", importance: "Морские ворота курорта Сириус, популярное место для прогулок.", fact: "Волны здесь могут достигать нескольких метров во время зимних штормов.", img: "{data[1]['img']}" }},
    {{ id: "2", coords: {coords['4']}, title: "2. Олимпийский пляж", yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D", category: "Отдых", brief: "Широкий галечный пляж Сириуса.", desc: "Один из самых чистых пляжей побережья без волнорезов.", importance: "Главная рекреационная зона у моря.", fact: "Часто дельфины подплывают близко к берегу.", img: "{data[10]['img']}" }},
    {{ id: "3.1", coords: {coords['3.1']}, title: "3.1 Стадион Фишт", yandexUrl: "https://yandex.ru/maps/-/CXU8uRMW", category: "Спорт", brief: "Главный Олимпийский стадион.", desc: "Место проведения церемоний открытия и закрытия Олимпиады 2014, а также матчей ЧМ по футболу 2018.", importance: "Символ Олимпиады в Сочи, архитектура напоминает снежную вершину и ракушку.", fact: "Назван в честь горной вершины Главного Кавказского хребта.", img: "{data[2]['img']}" }},
    {{ id: "3.2", coords: {coords['3.2']}, title: "3.2 Поющие фонтаны", yandexUrl: "https://yandex.ru/maps/-/CXU8uZKO", category: "Достопримечательность", brief: "Грандиозное вечернее шоу воды и света.", desc: "Фонтан в центре Олимпийского парка, стилизованный под Жар-птицу.", importance: "Главная точка притяжения вечернего парка.", fact: "Высота струй достигает 50 метров.", img: "{data[3]['img']}", videoUrl: "https://www.youtube.com/embed/V6XN4F8eR3w" }},
    {{ id: "3.3", coords: {coords['3.3']}, title: "3.3 Ледовый дворец Айсберг", yandexUrl: "https://yandex.ru/maps/-/CXU8uKYZ", category: "Спорт", brief: "Дворец зимнего спорта.", desc: "Арена для фигурного катания и шорт-трека. Сейчас принимает ледовые шоу.", importance: "Уникальная архитектура, напоминающая глыбу льда.", fact: "Здание спроектировано как сборно-разборное.", img: "{data[4]['img']}" }},
    {{ id: "3.4", coords: {coords['3.4']}, title: "3.4 Музей Леонардо да Винчи", yandexUrl: "https://yandex.ru/maps/-/CXU8uSP0", category: "Музей", brief: "Интерактивный музей механизмов.", desc: "Экспозиция, воссоздающая механизмы по чертежам великого итальянского изобретателя Леонардо да Винчи.", importance: "Популяризация науки и инженерной мысли.", fact: "Все экспонаты можно трогать и приводить в движение.", img: "{data[5]['img']}" }},
    {{ id: "3.5", coords: {coords['3.5']}, title: "3.5 Музей Николы Теслы", yandexUrl: "https://yandex.ru/maps/-/CXU8uSiN", category: "Музей", brief: "Шоу молний и электричества.", desc: "Научно-развлекательный центр, посвященный Николе Тесле.", importance: "Интерактивное изучение законов физики.", fact: "В музее регулярно проходят шоу с огромными трансформаторами Теслы.", img: "{data[6]['img']}" }},
    {{ id: "3.6", coords: {coords['3.6']}, title: "3.6 Планетарий Сириус", yandexUrl: "https://yandex.ru/maps/-/CXU8uK-y", category: "Наука/Космос", brief: "Современный планетарий с купольным экраном.", desc: "Один из крупнейших планетариев в Европе с современной проекционной системой.", importance: "Астрономическое образование и просвещение.", fact: "Диаметр купола составляет 26 метров.", img: "{data[7]['img']}" }},
    {{ id: "3.7", coords: {coords['3.7']}, title: "3.7 Сочи Автодром", yandexUrl: "https://yandex.ru/maps/-/CXU8yR5o", category: "Спорт", brief: "Гоночная трасса.", desc: "Трасса, принимавшая Гран-при России Формулы 1.", importance: "Единственная в России трасса, проложенная вокруг Олимпийских объектов.", fact: "Длина круга — 5,8 км.", img: "{data[8]['img']}" }},
    {{ id: "3.7", coords: {coords['3.7_2']}, title: "3.7 Музей Панулли", yandexUrl: "https://yandex.ru/maps/-/CXU8y6kB", category: "Музей", brief: "Музей спортивных и ретро-автомобилей.", desc: "Уникальная коллекция автомобилей на территории Автодрома.", importance: "Сохранение автомобильной истории.", fact: "В коллекции есть болиды Формулы 1.", img: "{data[9]['img']}" }},
    {{ id: "4", coords: [43.398014, 39.972986], title: "4. Орнитологический парк", yandexUrl: "https://yandex.ru/maps/org/prirodniy_ornitologicheskiy_park_v_imeretinskoy_nizmennosti/115591322258/", category: "Природа/Парк", brief: "Природный оазис для птиц.", desc: "Природный орнитологический парк в Имеретинской низменности. Здесь останавливаются перелетные птицы.", importance: "Важный экологический объект для сохранения биоразнообразия региона.", fact: "В парке зарегистрировано более 200 видов птиц.", img: "https://avatars.mds.yandex.net/get-altay/223006/2a0000015cb7ed258dc71f84d0b13cfcc7a1/L_height" }},
    {{ id: "5", coords: {coords['5']}, title: "5. Буран", yandexUrl: "https://yandex.ru/maps/-/CXU85QOt", category: "Достопримечательность", brief: "Макет космического корабля.", desc: "Полноразмерный макет орбитального корабля «Буран», расположенный в Сириусе.", importance: "Памятник советской космической программе.", fact: "Это один из испытательных макетов, перевезенных сюда для выставки.", img: "{data[12]['img']}" }},
    {{ id: "6", coords: {park_coords}, title: "6. Парк Южные культуры", yandexUrl: "{park_url}", category: "Природа/Парк", brief: "Дендрологический парк с экзотическими растениями.", desc: "Исторический парк в Адлере, основанный более 100 лет назад. Собраны растения со всего мира.", importance: "Ценный ботанический объект региона, оазис зелени рядом с морем.", fact: "Здесь растут секвойи, бамбук и цветут лотосы.", img: "{park_img}" }},
    
    {{ id: "7.1", coords: {coords['6.1']}, title: "7.1 Тисо-самшитовая роща", yandexUrl: "https://yandex.com/maps/org/tis_velikan/130928037188", category: "Природа", brief: "Реликтовый лес древних эпох.", desc: "Уникальный лес на склоне горы Ахун, часть Кавказского заповедника. Здесь сохранились деревья, росшие миллионы лет назад.", importance: "Памятник природы, находящийся под охраной ЮНЕСКО.", fact: "Некоторые деревья здесь старше 2000 лет.", img: "{data[13]['img']}" }},
    {{ id: "7.2", coords: {coords['6.2']}, title: "7.2 Лабиринт (Тис-самшитовая)", yandexUrl: "https://yandex.com/maps/org/labirint/175931569938", category: "Природа", brief: "Участок древнего леса.", desc: "Часть маршрута по Тисо-самшитовой роще с причудливыми скалами и корнями деревьев.", importance: "Позволяет погрузиться в атмосферу первобытного леса.", fact: "В 2014 году самшит сильно пострадал от завезенной бабочки-огневки.", img: "{data[14]['img']}" }},
    {{ id: "7.3", coords: {coords['6.3']}, title: "7.3 Буковая поляна", yandexUrl: "https://yandex.com/maps/org/ruiny_vizantiyskoy_kreposti_viii_x_vv_/205246609730", category: "Природа", brief: "Живописная поляна в реликтовом лесу.", desc: "Место отдыха на Большом кольце Тисо-самшитовой рощи.", importance: "Переходная зона между разными типами леса.", fact: "Здесь часто встречаются редкие виды папоротников.", img: "{data[15]['img']}" }},
    {{ id: "7.4", coords: {coords['6.4']}, title: "7.4 Руины крепости", yandexUrl: "https://yandex.ru/maps/-/CXU8BS-Z", category: "История", brief: "Развалины древней византийской крепости.", desc: "Остатки оборонительного сооружения VIII-X веков на территории Тисо-самшитовой рощи.", importance: "Свидетельство присутствия византийцев на Черноморском побережье Кавказа.", fact: "Крепость защищала торговые пути, идущие по реке Хоста.", img: "{data[16]['img']}" }},
    
    {{ id: "8", coords: {coords['7']}, title: "8. Каньон Чертовы ворота", yandexUrl: "https://yandex.ru/maps/org/kanyon_chyortovy_vorota/149726264059/", category: "Природа", brief: "Живописный каньон реки Хоста.", desc: "Узкое ущелье со скалами высотой до 50 метров. Популярное место для купания в кристально чистой воде.", importance: "Уникальный геологический объект.", fact: "Вода в реке даже в жару редко прогревается выше 17 градусов.", img: "{data[17]['img']}" }},
    {{ id: "9", coords: {coords['8']}, title: "9. Форелевое хозяйство", yandexUrl: "https://yandex.ru/maps/org/ao_plemennoy_forelevodcheskiy_zavod_adler/1069639997/", category: "Производство", brief: "Племенной завод по разведению форели.", desc: "Крупнейшее в России предприятие по выращиванию ценных пород рыб.", importance: "Важный объект экономики региона и поставщик рыбы.", fact: "Здесь вывели уникальную породу форели «Адлерская янтарная» (золотого цвета).", img: "{data[18]['img']}" }},
    {{ id: "10", coords: {coords['9']}, title: "10. Ахштырская пещера", yandexUrl: "https://yandex.ru/maps/org/akhshtyrskaya_peshchera/145496035348/", category: "История/Природа", brief: "Пещера со следами древних людей.", desc: "Карстовая пещера в ущелье реки Мзымта, где были найдены стоянки неандертальцев и кроманьонцев.", importance: "Один из важнейших археологических памятников Кавказа.", fact: "Пещера была обитаема на протяжении многих тысячелетий.", img: "{data[19]['img']}" }},
    {{ id: "11", coords: {coords['10']}, title: "11. Скайпарк (Скайбридж)", yandexUrl: "https://yandex.ru/maps/org/skaypark/1210593378/", category: "Экстрим/Развлечения", brief: "Подвесной мост и парк экстремальных развлечений.", desc: "Один из самых длинных подвесных пешеходных мостов в мире, перекинутый через Ахштырское ущелье.", importance: "Знаковый туристический объект современного Сочи.", fact: "Здесь находится самая высокая в России точка для банджи-джампинга (207 м).", img: "{data[20]['img']}" }},
    {{ id: "12", coords: {coords['11']}, title: "12. Курорт Красная Поляна", yandexUrl: "https://yandex.ru/maps/org/kurort_krasnaya_polyana/1214311519/", category: "Горный курорт", brief: "Крупнейший горнолыжный курорт региона.", desc: "Всесезонный курорт, предлагающий горнолыжные трассы зимой и пешие маршруты летом.", importance: "Ключевой объект горного кластера, развивающий туризм круглый год.", fact: "Курорт расположен на нескольких уровнях (Поляна 540, Поляна 960 и выше).", img: "{data[21]['img']}" }},
    {{ id: "13", coords: {coords['12']}, title: "13. Кругозор Ефремова", yandexUrl: "https://yandex.ru/maps/-/CXU8u84K", category: "Природа/Вид", brief: "Смотровая площадка с видом на Красную Поляну.", desc: "Панорамная точка на горе Монашка, названная в честь Ю.К. Ефремова — поэта и географа, исследователя Кавказа.", importance: "Одно из лучших мест для обзора поселка Красная Поляна и окружающих вершин.", fact: "Дорога к смотровой проходит по живописному реликтовому лесу.", img: "{data[22]['img']}" }},
    {{ id: "14.1", coords: {coords['13.2']}, title: "14.1 Ратуша Роза Хутор", yandexUrl: "https://yandex.ru/maps/-/CXU850zZ", category: "Архитектура", brief: "Символ курорта Роза Хутор.", desc: "Здание ратуши с башней с часами на площади Роза, стилизованное под европейскую архитектуру.", importance: "Центральное место встреч и проведения мероприятий на курорте.", fact: "Часы на ратуше вдохновлены вокзалом в Сочи.", img: "{data[24]['img']}" }},
    {{ id: "14.2", coords: {coords['13.1']}, title: "14.2 Роза Пик", yandexUrl: "https://yandex.ru/maps/org/roza_pik/158962977869/", category: "Горы/Панорама", brief: "Высшая точка курорта, доступная на канатке.", desc: "Вершина хребта Аибга высотой 2320 метров, откуда открывается вид на горы и море.", importance: "Самая популярная видовая площадка Розы Хутор.", fact: "Здесь находятся качели над пропастью.", img: "{data[23]['img']}" }},
    {{ id: "15", coords: {coords['14']}, title: "15. Газпром Поляна", yandexUrl: "https://yandex.ru/maps/org/gorno_turisticheskiy_tsentr_gazprom/43313807333/", category: "Горный курорт", brief: "Курорт на склонах плато Псехако.", desc: "Включает в себя лыжно-биатлонный комплекс «Лаура» и склоны на горе Альпика.", importance: "Место проведения олимпийских соревнований по биатлону и лыжным гонкам.", fact: "Канатная дорога типа 3S — одна из самых длинных в мире.", img: "{data[25]['img']}" }}
];
'''

js_bottom = '''
function switchGuide(event, targetId) {
    document.querySelectorAll('#guide-nav li').forEach(li => {
        li.classList.remove('active');
    });
    if(event && event.currentTarget) event.currentTarget.classList.add('active');
    
    document.querySelectorAll('.guide-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    document.getElementById(targetId).classList.add('active');

    const guideBg = {
        'guide-intro': 'https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height',
        'guide-geo': 'https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height',
        'guide-eco': 'https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height',
        'guide-pop': 'https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height'
    };
    
    document.getElementById('guide').style.backgroundImage = `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url(${guideBg[targetId]})`;
}

ymaps.ready(initMap);

function initMap() {
    window.mapObj = new ymaps.Map("map", {
        center: [43.5500, 40.0500],
        zoom: 10,
        controls: ['zoomControl', 'typeSelector', 'fullscreenControl']
    });

    // Олимпик (с 1 по 3.7_2)
    var olympicPolygon = new ymaps.Polygon([
        POLY_OLYMPIC
    ], { hintContent: 'Олимпийский парк' }, { fillColor: "#007bff33", strokeColor: "#007bff", strokeOpacity: 0.8, strokeWidth: 2 });
    window.mapObj.geoObjects.add(olympicPolygon);

    // Тисо-Самшитовая (7.1 .. 7.4)
    var tisoPolygon = new ymaps.Polygon([
        POLY_TISO
    ], { hintContent: 'Тисо-самшитовая роща' }, { fillColor: "#28a74533", strokeColor: "#28a745", strokeOpacity: 0.8, strokeWidth: 2 });
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
        videoEl.innerHTML = `<iframe width="100%" height="100%" src="${point.videoUrl}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>`;
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

def get_buffered_polygon(points, buffer_radius_m=200, points_per_circle=12):
    def project(lat, lon):
        r_earth = 6378137
        x = math.radians(lon) * r_earth
        y = math.log(math.tan(math.pi/4 + math.radians(lat)/2)) * r_earth
        return x, y
    def unproject(x, y):
        r_earth = 6378137
        lon = math.degrees(x / r_earth)
        lat = math.degrees(2 * math.atan(math.exp(y / r_earth)) - math.pi/2)
        return lat, lon

    circle_pts = []
    for (lat, lon) in points:
        px, py = project(lat, lon)
        for i in range(points_per_circle):
            angle = 2 * math.pi * i / points_per_circle
            cx = px + buffer_radius_m * math.cos(angle)
            cy = py + buffer_radius_m * math.sin(angle)
            circle_pts.append((cx, cy))
    
    def convex_hull(pts):
        pts = sorted(pts)
        if len(pts) <= 1: return pts
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]

    hull_proj = convex_hull(circle_pts)
    hull_latlon = [list(unproject(x, y)) for x, y in hull_proj]
    return hull_latlon

olympic_pts = [coords[k] for k in ["3.1","3.2","3.3","3.4","3.5","3.6","3.7","3.7_2","3.8"]]
tiso_pts = [coords[k] for k in ["6.1","6.2","6.3","6.4"]]

poly_olympic = get_buffered_polygon(olympic_pts, 200)
poly_tiso = get_buffered_polygon(tiso_pts, 250)

js_bottom = js_bottom.replace('POLY_OLYMPIC', json.dumps(poly_olympic))
js_bottom = js_bottom.replace('POLY_TISO', json.dumps(poly_tiso))

# Line
line_coords = [
    coords['2'], coords['4'],
    coords['3.2'], coords['3.7'],
    [43.398014, 39.972986], coords['5'],
    park_coords,
    coords['6.1'], coords['6.3'],
    coords['7'], coords['8'], coords['9'], coords['10'],
    coords['11'], coords['12'], coords['13.2'], coords['13.1'], coords['14']
]
js_bottom = js_bottom.replace('ROUTE_LINE', json.dumps(line_coords))

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(points_js + js_bottom)
print("done script.js")

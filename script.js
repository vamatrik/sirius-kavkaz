
const routePoints = [
    { id: "1", coords: [43.413337, 39.93146], title: "1. Сириус", yandexUrl: "https://yandex.ru/maps/-/CXU8mH74", category: "Город/Курорт", brief: "Современный курорт и образовательный центр.", desc: "Стартовая точка маршрута. Имеретинская низменность, преображенная к Олимпиаде 2014.", importance: "Федеральная территория с особым статусом, центр науки и спорта.", fact: "До Олимпиады здесь располагался поселок староверов Марлинский.", img: "https://avatars.mds.yandex.net/get-altay/1005628/2a000001892c348aa71914d331716792e2ab/L_height" },
    { id: "2", coords: [43.399239, 39.958595], title: "2. Имеретинский морской вокзал", yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w", category: "Транспорт/Отдых", brief: "Яхтенная марина и порт.", desc: "Порт, построенный для приема грузовых судов во время олимпийской стройки, теперь превращен в яхтенную марину.", importance: "Морские ворота курорта Сириус, популярное место для прогулок.", fact: "Волны здесь могут достигать нескольких метров во время зимних штормов.", img: "https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height" },
    { id: "3.1", coords: [43.402006, 39.95589], title: "3.1 Стадион Фишт", yandexUrl: "https://yandex.ru/maps/-/CXU8uRMW", category: "Спорт", brief: "Главный Олимпийский стадион.", desc: "Место проведения церемоний открытия и закрытия Олимпиады 2014, а также матчей ЧМ по футболу 2018.", importance: "Символ Олимпиады в Сочи, архитектура напоминает снежную вершину и ракушку.", fact: "Назван в честь горной вершины Главного Кавказского хребта.", img: "https://avatars.mds.yandex.net/get-altay/1246719/2a00000163996b11cf8fa6eb65efad6ba738/L_height" },
    { id: "3.2", coords: [43.405414, 39.954677], title: "3.2 Поющие фонтаны", yandexUrl: "https://yandex.ru/maps/-/CXU8uZKO", category: "Достопримечательность", brief: "Грандиозное вечернее шоу воды и света.", desc: "Фонтан в центре Олимпийского парка, стилизованный под Жар-птицу.", importance: "Главная точка притяжения вечернего парка.", fact: "Высота струй достигает 50 метров.", img: "https://avatars.mds.yandex.net/get-altay/14337779/2a00000195ce583e32c5eea4884d772f4a95/L_height", videoUrl: "https://www.youtube.com/embed/V6XN4F8eR3w" },
    { id: "3.3", coords: [43.407418, 39.958316], title: "3.3 Ледовый дворец Айсберг", yandexUrl: "https://yandex.ru/maps/-/CXU8uKYZ", category: "Спорт", brief: "Дворец зимнего спорта.", desc: "Арена для фигурного катания и шорт-трека. Сейчас принимает ледовые шоу.", importance: "Уникальная архитектура, напоминающая глыбу льда.", fact: "Здание спроектировано как сборно-разборное.", img: "https://avatars.mds.yandex.net/get-altay/813485/2a000001603403bc8148cf35a37122b90fdb/L_height" },
    { id: "3.4", coords: [43.406147, 39.967654], title: "3.4 Музей Леонардо да Винчи", yandexUrl: "https://yandex.ru/maps/-/CXU8uSP0", category: "Музей", brief: "Интерактивный музей механизмов.", desc: "Экспозиция, воссоздающая механизмы по чертежам великого итальянского изобретателя Леонардо да Винчи.", importance: "Популяризация науки и инженерной мысли.", fact: "Все экспонаты можно трогать и приводить в движение.", img: "https://avatars.mds.yandex.net/get-altay/11421964/2a0000018cf241332914b3272b98bdf28da0/L_height" },
    { id: "3.5", coords: [43.406072, 39.968277], title: "3.5 Музей Николы Теслы", yandexUrl: "https://yandex.ru/maps/-/CXU8uSiN", category: "Музей", brief: "Шоу молний и электричества.", desc: "Научно-развлекательный центр, посвященный Николе Тесле.", importance: "Интерактивное изучение законов физики.", fact: "В музее регулярно проходят шоу с огромными трансформаторами Теслы.", img: "https://avatars.mds.yandex.net/get-altay/5548986/2a0000018400c3d368869bb8c1bfe2998c7d/L_height" },
    { id: "3.6", coords: [43.408389, 39.97204], title: "3.6 Планетарий Сириус", yandexUrl: "https://yandex.ru/maps/-/CXU8uK-y", category: "Наука/Космос", brief: "Современный планетарий с купольным экраном.", desc: "Один из крупнейших планетариев в Европе с современной проекционной системой.", importance: "Астрономическое образование и просвещение.", fact: "Диаметр купола составляет 26 метров.", img: "https://avatars.mds.yandex.net/get-altay/18708590/2a0000019d952cd5db8c59c726b844e77494/L_height" },
    { id: "3.7", coords: [43.410149, 39.96911], title: "3.7 Сочи Автодром", yandexUrl: "https://yandex.ru/maps/-/CXU8yR5o", category: "Спорт", brief: "Гоночная трасса.", desc: "Трасса, принимавшая Гран-при России Формулы 1.", importance: "Единственная в России трасса, проложенная вокруг Олимпийских объектов.", fact: "Длина круга — 5,8 км.", img: "https://avatars.mds.yandex.net/get-altay/1532977/2a00000168d3053a97089db3ae8c03f187b2/L_height" },
    { id: "3.7", coords: [43.410562, 39.969592], title: "3.7 Музей Панулли", yandexUrl: "https://yandex.ru/maps/-/CXU8y6kB", category: "Музей", brief: "Музей спортивных и ретро-автомобилей.", desc: "Уникальная коллекция автомобилей на территории Автодрома.", importance: "Сохранение автомобильной истории.", fact: "В коллекции есть болиды Формулы 1.", img: "https://avatars.mds.yandex.net/get-altay/15426074/2a00000196c05ad6562107939f6e5c6327cb/L_height" },
    { id: "4", coords: [43.394531, 39.991941], title: "4. Олимпийский пляж", yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D", category: "Отдых", brief: "Широкий галечный пляж Сириуса.", desc: "Один из самых чистых пляжей побережья без волнорезов.", importance: "Главная рекреационная зона у моря.", fact: "Часто дельфины подплывают близко к берегу.", img: "https://avatars.mds.yandex.net/get-altay/813485/2a0000015ea829aadbed291bb1461e00fe06/L_height" },
    { id: "5", coords: [43.414441, 39.949121], title: "5. Буран", yandexUrl: "https://yandex.ru/maps/-/CXU85QOt", category: "Достопримечательность", brief: "Макет космического корабля.", desc: "Полноразмерный макет орбитального корабля «Буран», расположенный в Сириусе.", importance: "Памятник советской космической программе.", fact: "Это один из испытательных макетов, перевезенных сюда для выставки.", img: "https://avatars.mds.yandex.net/get-altay/1439437/2a0000018c69b53c549d34564a36c867eff9/L_height" },
    { id: "6", coords: [43.419568, 39.931381], title: "6. Парк Южные культуры", yandexUrl: "https://yandex.ru/maps/-/CXUcQTJe", category: "Природа/Парк", brief: "Дендрологический парк с экзотическими растениями.", desc: "Исторический парк в Адлере, основанный более 100 лет назад. Собраны растения со всего мира.", importance: "Ценный ботанический объект региона, оазис зелени рядом с морем.", fact: "Здесь растут секвойи, бамбук и цветут лотосы.", img: "https://avatars.mds.yandex.net/get-altay/239474/2a0000015d059ec428668e23acb2be76bb46/L_height" },
    
    { id: "7.1", coords: [43.529718, 39.875345], title: "7.1 Тисо-самшитовая роща", yandexUrl: "https://yandex.com/maps/org/tis_velikan/130928037188", category: "Природа", brief: "Реликтовый лес древних эпох.", desc: "Уникальный лес на склоне горы Ахун, часть Кавказского заповедника. Здесь сохранились деревья, росшие миллионы лет назад.", importance: "Памятник природы, находящийся под охраной ЮНЕСКО.", fact: "Некоторые деревья здесь старше 2000 лет.", img: "https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height" },
    { id: "7.2", coords: [43.53033, 39.876607], title: "7.2 Лабиринт (Тис-самшитовая)", yandexUrl: "https://yandex.com/maps/org/labirint/175931569938", category: "Природа", brief: "Участок древнего леса.", desc: "Часть маршрута по Тисо-самшитовой роще с причудливыми скалами и корнями деревьев.", importance: "Позволяет погрузиться в атмосферу первобытного леса.", fact: "В 2014 году самшит сильно пострадал от завезенной бабочки-огневки.", img: "https://avatars.mds.yandex.net/get-altay/15417312/2a00000197a090ac71ece0503eae945aa454/L_height" },
    { id: "7.3", coords: [43.540056, 39.880015], title: "7.3 Буковая поляна", yandexUrl: "https://yandex.com/maps/org/ruiny_vizantiyskoy_kreposti_viii_x_vv_/205246609730", category: "Природа", brief: "Живописная поляна в реликтовом лесу.", desc: "Место отдыха на Большом кольце Тисо-самшитовой рощи.", importance: "Переходная зона между разными типами леса.", fact: "Здесь часто встречаются редкие виды папоротников.", img: "https://avatars.mds.yandex.net/get-altay/10812438/2a0000018c3f84bfb686579f37e3ad5380f0/L_height" },
    { id: "7.4", coords: [43.538573, 39.877676], title: "7.4 Руины крепости", yandexUrl: "https://yandex.ru/maps/-/CXU8BS-Z", category: "История", brief: "Развалины древней византийской крепости.", desc: "Остатки оборонительного сооружения VIII-X веков на территории Тисо-самшитовой рощи.", importance: "Свидетельство присутствия византийцев на Черноморском побережье Кавказа.", fact: "Крепость защищала торговые пути, идущие по реке Хоста.", img: "https://avatars.mds.yandex.net/get-altay/13461681/2a00000190f9040a9bc57bc0c0059d1e38c4/L_height" },
    
    { id: "8", coords: [43.544621, 39.87877], title: "8. Каньон Чертовы ворота", yandexUrl: "https://yandex.ru/maps/org/kanyon_chyortovy_vorota/149726264059/", category: "Природа", brief: "Живописный каньон реки Хоста.", desc: "Узкое ущелье со скалами высотой до 50 метров. Популярное место для купания в кристально чистой воде.", importance: "Уникальный геологический объект.", fact: "Вода в реке даже в жару редко прогревается выше 17 градусов.", img: "https://avatars.mds.yandex.net/get-altay/6310045/2a000001902b6cd5dd108acfa347bda76539/L_height" },
    { id: "9", coords: [43.517264, 39.993583], title: "9. Форелевое хозяйство", yandexUrl: "https://yandex.ru/maps/org/ao_plemennoy_forelevodcheskiy_zavod_adler/1069639997/", category: "Производство", brief: "Племенной завод по разведению форели.", desc: "Крупнейшее в России предприятие по выращиванию ценных пород рыб.", importance: "Важный объект экономики региона и поставщик рыбы.", fact: "Здесь вывели уникальную породу форели «Адлерская янтарная» (золотого цвета).", img: "https://avatars.mds.yandex.net/get-altay/374295/2a0000015b2171316393e398f4c7f73309ad/L_height" },
    { id: "10", coords: [43.520777, 39.996083], title: "10. Ахштырская пещера", yandexUrl: "https://yandex.ru/maps/org/akhshtyrskaya_peshchera/145496035348/", category: "История/Природа", brief: "Пещера со следами древних людей.", desc: "Карстовая пещера в ущелье реки Мзымта, где были найдены стоянки неандертальцев и кроманьонцев.", importance: "Один из важнейших археологических памятников Кавказа.", fact: "Пещера была обитаема на протяжении многих тысячелетий.", img: "https://avatars.mds.yandex.net/get-altay/4716261/2a00000182277979173ca801adde160bdb7d/L_height" },
    { id: "11", coords: [43.524942, 39.997254], title: "11. Скайпарк (Скайбридж)", yandexUrl: "https://yandex.ru/maps/org/skaypark/1210593378/", category: "Экстрим/Развлечения", brief: "Подвесной мост и парк экстремальных развлечений.", desc: "Один из самых длинных подвесных пешеходных мостов в мире, перекинутый через Ахштырское ущелье.", importance: "Знаковый туристический объект современного Сочи.", fact: "Здесь находится самая высокая в России точка для банджи-джампинга (207 м).", img: "https://avatars.mds.yandex.net/get-altay/15112342/2a00000194ef20b6759a5c781dda7d098022/L_height" },
    { id: "12", coords: [43.66848, 40.257731], title: "12. Курорт Красная Поляна", yandexUrl: "https://yandex.ru/maps/org/kurort_krasnaya_polyana/1214311519/", category: "Горный курорт", brief: "Крупнейший горнолыжный курорт региона.", desc: "Всесезонный курорт, предлагающий горнолыжные трассы зимой и пешие маршруты летом.", importance: "Ключевой объект горного кластера, развивающий туризм круглый год.", fact: "Курорт расположен на нескольких уровнях (Поляна 540, Поляна 960 и выше).", img: "https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height" },
    { id: "13", coords: [43.685056, 40.256059], title: "13. Кругозор Ефремова", yandexUrl: "https://yandex.ru/maps/-/CXU8u84K", category: "Природа/Вид", brief: "Смотровая площадка с видом на Красную Поляну.", desc: "Панорамная точка на горе Монашка, названная в честь Ю.К. Ефремова — поэта и географа, исследователя Кавказа.", importance: "Одно из лучших мест для обзора поселка Красная Поляна и окружающих вершин.", fact: "Дорога к смотровой проходит по живописному реликтовому лесу.", img: "https://static-maps.yandex.ru/1.x/?api_key=01931952-3aef-4eba-951a-8afd26933ad6&amp;theme=light&amp;lang=ru_RU&amp;size=520%2C440&amp;l=map&amp;z=14&amp;ll=40.258399%2C43.678217&amp;lg=0&amp;cr=0&amp;pt=40.256059%2C43.685056%2Cplacemark&amp;signature=CcQImaj24I0kEVVdi5-hrUuqfSK0I1SnFjUc0YJ4NoU=" },
    { id: "14.1", coords: [43.672435, 40.296279], title: "14.1 Ратуша Роза Хутор", yandexUrl: "https://yandex.ru/maps/-/CXU850zZ", category: "Архитектура", brief: "Символ курорта Роза Хутор.", desc: "Здание ратуши с башней с часами на площади Роза, стилизованное под европейскую архитектуру.", importance: "Центральное место встреч и проведения мероприятий на курорте.", fact: "Часы на ратуше вдохновлены вокзалом в Сочи.", img: "https://avatars.mds.yandex.net/get-altay/13970739/2a0000019199a98ce17675787a1c6a1c1404/L_height" },
    { id: "14.2", coords: [43.624629, 40.310452], title: "14.2 Роза Пик", yandexUrl: "https://yandex.ru/maps/org/roza_pik/158962977869/", category: "Горы/Панорама", brief: "Высшая точка курорта, доступная на канатке.", desc: "Вершина хребта Аибга высотой 2320 метров, откуда открывается вид на горы и море.", importance: "Самая популярная видовая площадка Розы Хутор.", fact: "Здесь находятся качели над пропастью.", img: "https://avatars.mds.yandex.net/get-altay/11622009/2a0000019073c9497e964506f53f0614a419/L_height" },
    { id: "15", coords: [43.694211, 40.314328], title: "15. Газпром Поляна", yandexUrl: "https://yandex.ru/maps/org/gorno_turisticheskiy_tsentr_gazprom/43313807333/", category: "Горный курорт", brief: "Курорт на склонах плато Псехако.", desc: "Включает в себя лыжно-биатлонный комплекс «Лаура» и склоны на горе Альпика.", importance: "Место проведения олимпийских соревнований по биатлону и лыжным гонкам.", fact: "Канатная дорога типа 3S — одна из самых длинных в мире.", img: "https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height" }
];

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
        [[43.40541400000001, 39.95288036943176], [43.40200599999999, 39.95409336943176], [43.401353324962514, 39.95433407228669], [43.40087552921666, 39.95499168471588], [43.40070064289388, 39.95589], [43.40087552921666, 39.956788315284115], [43.40337557586592, 39.96883731528412], [43.40385335189549, 39.969494927713306], [43.40773639373023, 39.97359592771331], [43.408389000000014, 39.973836630568236], [43.409041599238506, 39.97359592771331], [43.411214575825646, 39.97114792771331], [43.411692290028135, 39.970490315284124], [43.41186714462, 39.969592000000006], [43.411692290028135, 39.96869368471588], [43.40854834870058, 39.957417684715885], [43.40654438609684, 39.95377868471588], [43.40606663129091, 39.95312107228669]]
    ], { hintContent: 'Олимпийский парк' }, { fillColor: "#007bff33", strokeColor: "#007bff", strokeOpacity: 0.8, strokeWidth: 2 });
    window.mapObj.geoObjects.add(olympicPolygon);

    // Тисо-Самшитовая (7.1 .. 7.4)
    var tisoPolygon = new ymaps.Polygon([
        [[43.529717999999995, 39.8730992117897], [43.528903876920864, 39.873400090358366], [43.52830789049668, 39.874222105894845], [43.52808974285286, 39.875344999999996], [43.52830789049668, 39.87646789410515], [43.52891990480467, 39.87772989410515], [43.5295158851816, 39.87855190964163], [43.53033, 39.8788527882103], [43.54005600000001, 39.8822607882103], [43.54086997253583, 39.88195990964164], [43.54146583482121, 39.88113789410515], [43.54168393408258, 39.880015], [43.54146583482121, 39.878892105894856], [43.53998286949843, 39.87655310589486], [43.53938699255669, 39.87573109035837], [43.53857299999999, 39.875430211789705]]
    ], { hintContent: 'Тисо-самшитовая роща' }, { fillColor: "#28a74533", strokeColor: "#28a745", strokeOpacity: 0.8, strokeWidth: 2 });
    window.mapObj.geoObjects.add(tisoPolygon);

    var mainRouteCoords = [[43.413337, 39.93146], [43.399239, 39.958595], [43.405414, 39.954677], [43.410149, 39.96911], [43.394531, 39.991941], [43.414441, 39.949121], [43.419568, 39.931381], [43.529718, 39.875345], [43.540056, 39.880015], [43.544621, 39.87877], [43.517264, 39.993583], [43.520777, 39.996083], [43.524942, 39.997254], [43.66848, 40.257731], [43.685056, 40.256059], [43.672435, 40.296279], [43.624629, 40.310452], [43.694211, 40.314328]];

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
    setTimeout(() => { document.querySelector(\'.info-panel\').scrollIntoView({behavior: \'smooth\', block: \'center\'}); }, 100);
    
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

const routePoints = [
    {
        id: "1",
        coords: [43.413337, 39.93146],
        title: "1. Имеретинский морской вокзал",
        yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w",
        category: "Транспорт и Архитектура",
        brief: "Главные морские ворота Адлерского района.",
        desc: "Отправная точка нашего маршрута. Морской вокзал не только обслуживает пассажиров, но и является интересным архитектурным объектом на побережье, символизируя связь города с морем.",
        importance: "Морское сообщение исторически играло ключевую роль в развитии региона.",
        fact: "Здание вокзала часто становится местом для городских фотосессий благодаря красивому виду на закаты.",
        img: "https://avatars.mds.yandex.net/get-altay/1005628/2a000001892c348aa71914d331716792e2ab/L_height"
    },
    {
        id: "2",
        coords: [43.399239, 39.958595],
        title: "2. Олимпийский пляж",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D",
        category: "Отдых",
        brief: "Крутой современный пляж в Имеретинской низменности.",
        desc: "Несмотря на название, этот пляж находится у моря. Это современная зона отдыха.",
        importance: "Демонстрирует, как горные курорты Сочи развивают комплексный отдых: от снежных вершин до теплого моря.",
        fact: "Пляж регулярно получает международную награду «Голубой флаг» за чистоту воды и инфраструктуру.",
        img: "https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height"
    },
    {
        id: "3.1",
        coords: [43.402006, 39.95589],
        title: "3.1 Стадион Фишт",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uRMW",
        category: "Олимпийский парк",
        brief: "Легендарный стадион, принимавший открытие и закрытие Олимпиады.",
        desc: "Сейчас используется для проведения футбольных матчей.",
        importance: "Главный символ Олимпиады-2014.",
        fact: "Футбольные матчи здесь иногда отменяют или ставят на паузу из-за угроз с воздуха.",
        img: "https://avatars.mds.yandex.net/get-altay/1246719/2a00000163996b11cf8fa6eb65efad6ba738/L_height"
    },
    {
        id: "3.2",
        coords: [43.405414, 39.954677],
        title: "3.2 Поющие фонтаны",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uZKO",
        category: "Олимпийский парк",
        brief: "Грандиозное вечернее шоу воды, света и музыки.",
        desc: "Фонтан в виде жар-птицы. Вечером (если нет угрозы) здесь проходит потрясающе красивое шоу под классическую и современную музыку.",
        importance: "Центр притяжения всех туристов в Сириусе.",
        fact: "Фонтан может выбрасывать струи воды на высоту до 70 метров.",
        videoUrl: "https://www.youtube.com/embed/dQw4w9WgXcQ"
    },
    {
        id: "3.3",
        coords: [43.407418, 39.958316],
        title: "3.3 ЛД Айсберг",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uKYZ",
        category: "Олимпийский парк",
        brief: "Ледовый дворец спорта с уникальной архитектурой.",
        desc: "Здесь проходят самые красивые ледовые шоу знаменитых фигуристов.",
        importance: "Сохранение ледовых традиций России после Олимпиады.",
        fact: "Форма здания повторяет траекторию полёта фигуриста во время прыжка.",
        img: "https://avatars.mds.yandex.net/get-altay/813485/2a000001603403bc8148cf35a37122b90fdb/L_height"
    },
    {
        id: "3.4",
        coords: [43.406147, 39.967654],
        title: "3.4 Музей Леонардо да Винчи",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uSP0",
        category: "Олимпийский парк",
        brief: "Механические изобретения гения.",
        desc: "В экспозиции представлены реконструкции механизмов по чертежам Леонардо.",
        importance: "Популяризация инженерной мысли.",
        fact: "Многие экспонаты можно трогать и приводить в движение.",
        img: "https://avatars.mds.yandex.net/get-altay/11421964/2a0000018cf241332914b3272b98bdf28da0/L_height"
    },
    {
        id: "3.5",
        coords: [43.406072, 39.968277],
        title: "3.5 Музей Теслы",
        yandexUrl: "https://yandex.ru/maps/-/CXU8u8iV",
        category: "Олимпийский парк",
        brief: "Музей электричества.",
        desc: "Рядом с музеем Да Винчи. Здесь рассказывают об электричестве и проводят электрическое шоу (с музыкой и молниями).",
        importance: "Обучение физике через развлечение.",
        fact: "Генераторы Теслы создают настоящие молнии длиной в несколько метров.",
        img: "https://avatars.mds.yandex.net/get-altay/5548986/2a0000018400c3d368869bb8c1bfe2998c7d/L_height"
    },
    {
        id: "3.6",
        coords: [43.408389, 39.97204],
        title: "3.6 Концертный центр Сириус",
        yandexUrl: "https://yandex.ru/maps/-/CXU8uL1U",
        category: "Олимпийский парк",
        brief: "Крутой концертный зал с потрясающей акустикой.",
        desc: "Новый центр, включающий Главную сцену на 1200 мест.",
        importance: "Территория получила новое научно-культурное содержание.",
        fact: "Акустика зала разрабатывалась ведущими мировыми специалистами.",
        img: "https://avatars.mds.yandex.net/get-altay/18708590/2a0000019d952cd5db8c59c726b844e77494/L_height"
    },
    {
        id: "3.7",
        coords: [43.410149, 39.96911],
        title: "3.7 Сочи Автодром",
        yandexUrl: "https://yandex.ru/maps/-/CXU8yR5o",
        category: "Олимпийский парк",
        brief: "Гоночная трасса.",
        desc: "Единственная в России трасса, принимавшая Гран-при Формулы 1.",
        importance: "Интеграция автоспорта мирового уровня в олимпийскую инфраструктуру.",
        fact: "Трасса проложена прямо между олимпийскими стадионами.",
        img: "https://avatars.mds.yandex.net/get-altay/1532977/2a00000168d3053a97089db3ae8c03f187b2/L_height"
    },
    {
        id: "3.7",
        coords: [43.410562, 39.969592],
        title: "3.7 Музей Панулли",
        yandexUrl: "https://yandex.ru/maps/-/CXU8y6kB",
        category: "Олимпийский парк",
        brief: "Музей спортивных авто.",
        desc: "Коллекция уникальных спортивных и гоночных автомобилей.",
        importance: "Автоспорт и история.",
        fact: "Здесь собраны уникальные модели болидов со всего мира.",
        img: "https://avatars.mds.yandex.net/get-altay/15426074/2a00000196c05ad6562107939f6e5c6327cb/L_height"
    },
    {
        id: "3.8",
        coords: [43.404506, 39.967939],
        title: "3.8 Сочи Парк",
        yandexUrl: "https://yandex.ru/maps/-/CXU8yS8c",
        category: "Олимпийский парк",
        brief: "Первый тематический парк развлечений в России.",
        desc: "Аттракционы мирового уровня, оформленные в стиле русских сказок.",
        importance: "Главный семейный развлекательный центр юга России.",
        fact: "Аттракцион «Квантовый скачок» — самая быстрая и высокая горка в России.",
        img: "https://avatars.mds.yandex.net/get-altay/11368589/2a0000018bc478cc293ceb2e61b8dd97abd9/L_height"
    },
    {
        id: "4",
        coords: [43.394531, 39.991941],
        title: "4. Орнитологический парк",
        yandexUrl: "https://yandex.ru/maps/-/CXU8y-MR",
        category: "Природа",
        brief: "Парк, где можно покормить почти ручных птиц.",
        desc: "Особо охраняемая природная территория. Создана для сохранения мест отдыха перелетных птиц во время миграции.",
        importance: "Сохранение экосистемы Имеретинской низменности.",
        fact: "Здесь останавливается более 200 видов птиц, многие из которых занесены в Красную книгу.",
        img: "https://avatars.mds.yandex.net/get-altay/813485/2a0000015ea829aadbed291bb1461e00fe06/L_height"
    },
    {
        id: "5",
        coords: [43.414441, 39.949121],
        title: "5. Учебный центр Сириус",
        yandexUrl: "https://yandex.ru/maps/-/CXU85QOt",
        category: "Наука и образование",
        brief: "Образовательный центр для одаренных детей.",
        desc: "Здесь круглый год проходят учебные мероприятия для талантливых школьников со всей России по науке, искусству и спорту.",
        importance: "Главный образовательный проект страны, созданный на базе олимпийской инфраструктуры.",
        fact: "Рядом находится макет легендарного Бурана, куда водят экскурсии.",
        img: "https://avatars.mds.yandex.net/get-altay/1439437/2a0000018c69b53c549d34564a36c867eff9/L_height"
    },
    {
        id: "6",
        coords: [43.419568, 39.931381],
        title: "6. Парк Южные культуры",
        yandexUrl: "https://yandex.ru/maps/-/CXUcQTJe",
        category: "Природа/Парк",
        brief: "Дендрологический парк с экзотическими растениями.",
        desc: "Исторический парк в Адлере, основанный более 100 лет назад. Собраны растения со всего мира.",
        importance: "Ценный ботанический объект региона, оазис зелени рядом с морем.",
        fact: "Здесь растут секвойи, бамбук и цветут лотосы.",
        img: "https://avatars.mds.yandex.net/get-altay/239474/2a0000015d059ec428668e23acb2be76bb46/L_height"
    },

    {
        id: "7.1",
        coords: [43.529718, 39.875345],
        title: "7.1 Тис-великан",
        yandexUrl: "https://yandex.com/maps/-/CXU8yN8j",
        category: "Тисо-самшитовая роща",
        brief: "Древнейшее дерево Кавказа.",
        desc: "Огромное дерево, возраст которого исчисляется тысячелетиями.",
        importance: "Живой памятник доледниковой эпохи.",
        fact: "Тис ягодный растет очень медленно — всего на 1 мм в год в толщину.",
        img: "https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height"
    },
    {
        id: "7.2",
        coords: [43.53033, 39.876607],
        title: "7.2 Каменный лабиринт",
        yandexUrl: "https://yandex.com/maps/-/CXU85Fif",
        category: "Тисо-самшитовая роща",
        brief: "Природный тектонический разлом.",
        desc: "Глубокие трещины в известняковых скалах, поросшие мхом и папоротниками.",
        importance: "Демонстрирует геологическую историю формирования Кавказских гор.",
        fact: "Здесь сохраняется свой микроклимат, более влажный и прохладный.",
        img: "https://avatars.mds.yandex.net/get-altay/15417312/2a00000197a090ac71ece0503eae945aa454/L_height"
    },
    {
        id: "7.3",
        coords: [43.538573, 39.877676],
        title: "7.3 Буковая поляна",
        yandexUrl: "https://yandex.ru/maps/-/CXU8BS-Z",
        category: "Тисо-самшитовая роща",
        brief: "Красивая поляна в лесу.",
        desc: "Участок древнего леса.",
        importance: "Формирует уникальный микроклимат.",
        fact: "Деревья здесь имеют огромный возраст.",
        img: "https://avatars.mds.yandex.net/get-altay/13461681/2a00000190f9040a9bc57bc0c0059d1e38c4/L_height"
    },
    {
        id: "7.4",
        coords: [43.540056, 39.880015],
        title: "7.4 Хостинская крепость",
        yandexUrl: "https://yandex.com/maps/org/ruiny_vizantiyskoy_kreposti_viii_x_vv_/205246609730",
        category: "Тисо-самшитовая роща",
        brief: "Развалины древней генуэзской крепости.",
        desc: "Остатки оборонительных сооружений VIII-X веков.",
        importance: "Свидетельство того, что эти территории активно осваивались в эпоху Средневековья.",
        fact: "Стены крепости так плотно поросли растениями, что почти сливаются с лесом.",
        img: "https://avatars.mds.yandex.net/get-altay/10812438/2a0000018c3f84bfb686579f37e3ad5380f0/L_height"
    },
    {
        id: "8",
        coords: [43.544621, 39.87877],
        title: "8. Каньон Чёртовы ворота",
        yandexUrl: "https://yandex.ru/maps/org/kanyon_chyortovy_vorota/149726264059/",
        category: "Природа / Гастрономия",
        brief: "Глубокий каньон и отличный ресторанчик.",
        desc: "Ущелье с отвесными скалами высотой до 50 метров.",
        importance: "Популярное место для эко-туризма и сплавов на сапах.",
        fact: "В самом узком месте ширина каньона составляет всего около 3 метров.",
        img: "https://avatars.mds.yandex.net/get-altay/6310045/2a000001902b6cd5dd108acfa347bda76539/L_height"
    },
    {
        id: "9",
        coords: [43.517264, 39.993583],
        title: "9. Форелевое хозяйство",
        yandexUrl: "https://yandex.ru/maps/org/ao_plemennoy_forelevodcheskiy_zavod_adler/1069639997/",
        category: "Экономика",
        brief: "Племенной форелеводческий завод «Адлер».",
        desc: "Крупнейшее в России хозяйство по выращиванию форели.",
        importance: "Успешное использование горных водных ресурсов для сельского хозяйства.",
        fact: "Хозяйство вывело уникальную породу форели — «Адлерскую янтарную».",
        img: "https://avatars.mds.yandex.net/get-altay/374295/2a0000015b2171316393e398f4c7f73309ad/L_height"
    },
    {
        id: "10",
        coords: [43.520777, 39.996083],
        title: "10. Ахштырская пещера",
        yandexUrl: "https://yandex.ru/maps/org/akhshtyrskaya_peshchera/145496035348/",
        category: "Археология",
        brief: "Пещера, где жили древние люди.",
        desc: "Находится высоко над рекой Мзымта. Первые люди поселились здесь около 70 тысяч лет назад.",
        importance: "Важнейший археологический памятник эпохи палеолита на Кавказе.",
        fact: "В пещере обнаружены орудия труда неандертальцев и кроманьонцев.",
        img: "https://avatars.mds.yandex.net/get-altay/4716261/2a00000182277979173ca801adde160bdb7d/L_height"
    },
    {
        id: "11",
        coords: [43.524942, 39.997254],
        title: "11. Скай Парк (Skypark)",
        yandexUrl: "https://yandex.ru/maps/org/skaypark/1210593378/",
        category: "Экстрим",
        brief: "Парк высотных приключений над Ахштырским ущельем.",
        desc: "Один из самых длинных подвесных пешеходных мостов в мире.",
        importance: "Центр экстремального туризма, привлекающий гостей со всего мира.",
        fact: "Длина подвесного моста Скайбридж составляет 439 метров.",
        img: "https://avatars.mds.yandex.net/get-altay/15112342/2a00000194ef20b6759a5c781dda7d098022/L_height"
    },
    {
        id: "12",
        coords: [43.66848, 40.257731],
        title: "12. Курорт Красная Поляна",
        yandexUrl: "https://yandex.ru/maps/org/kurort_krasnaya_polyana/1214311519/",
        category: "Горный туризм",
        brief: "Бывший Горки Город, мощный туристический кластер.",
        desc: "Современный курорт, расположившийся на нескольких высотных уровнях.",
        importance: "Один из локомотивов горного туризма в России.",
        fact: "В Нижнем городе (Поляна 540) архитектура стилизована под европейские города.",
        img: "https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height"
    },
    {
        id: "13",
        coords: [43.673304, 40.182899],
        title: "13. Кругозор Ефремова",
        yandexUrl: "https://yandex.ru/maps/-/CXU8fXK5",
        category: "География",
        brief: "Смотровая площадка на горе Монашка.",
        desc: "Находится как раз у Эсто-Садка. Отсюда открываются панорамные виды на долину Мзымты.",
        importance: "Точка названа в честь географа и исследователя Юрия Ефремова.",
        fact: "С площадки можно одновременно увидеть и поселок, и вершины Главного Кавказского хребта.",
        img: "https://avatars.mds.yandex.net/get-altay/14090612/2a00000195f2ba324855abb9bbb440361a3c/L_height"
    },
    {
        id: "14.1",
        coords: [43.672435, 40.296279],
        title: "14.1 Ратуша Роза Хутор",
        yandexUrl: "https://yandex.ru/maps/-/CXU850zZ",
        category: "Архитектура",
        brief: "Главная площадь и символ курорта.",
        desc: "Центральная площадь с часовой башней.",
        importance: "Архитектурная доминанта, задающая стиль всему курорту.",
        fact: "Башня Ратуши стилизована под башню железнодорожного вокзала Сочи.",
        img: "https://avatars.mds.yandex.net/get-altay/13970739/2a0000019199a98ce17675787a1c6a1c1404/L_height"
    },
    {
        id: "14.2",
        coords: [43.624629, 40.310452],
        title: "14.2 Роза Пик",
        yandexUrl: "https://yandex.ru/maps/org/roza_pik/158962977869/",
        category: "Высокогорье",
        brief: "Вершина хребта Аибга, 2320 м.",
        desc: "Высшая точка нашего маршрута. Подъем сюда осуществляется по трем канатным дорогам.",
        importance: "Кульминация идеи маршрута: мы поднялись от уровня моря высоко в горы.",
        fact: "Даже в разгар лета на северных склонах здесь может лежать снег.",
        img: "https://avatars.mds.yandex.net/get-altay/11622009/2a0000019073c9497e964506f53f0614a419/L_height"
    },
    {
        id: "15",
        coords: [43.694211, 40.314328],
        title: "15. Газпром Поляна",
        yandexUrl: "https://yandex.ru/maps/org/gorno_turisticheskiy_tsentr_gazprom/43313807333/",
        category: "Горный туризм",
        brief: "Уютный и престижный курорт (зоны Лаура и Альпика).",
        desc: "Здесь проводились соревнования по биатлону и лыжным гонкам.",
        importance: "Дополняет картину горного кластера, предлагая круглогодичный отдых.",
        fact: "Канатная дорога типа 3S на Газпроме — одна из самых длинных в мире.",
        img: "https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height"
    }
];

// Навигация
ymaps.ready(initMap);

function initMap() {
    window.mapObj = new ymaps.Map("map", {
        center: [43.5500, 40.0500],
        zoom: 10,
        controls: ['zoomControl', 'typeSelector', 'fullscreenControl']
    });

    // Олимпийский парк
    var olympicPolygon = new ymaps.Polygon([
        [[43.40541400000001, 39.95288036943176], [43.40200599999999, 39.95409336943176], [43.401353324962514, 39.95433407228669], [43.40087552921666, 39.95499168471588], [43.40070064289388, 39.95589], [43.40087552921666, 39.956788315284115], [43.40337557586592, 39.96883731528412], [43.40385335189549, 39.969494927713306], [43.40773639373023, 39.97359592771331], [43.408389000000014, 39.973836630568236], [43.409041599238506, 39.97359592771331], [43.411214575825646, 39.97114792771331], [43.411692290028135, 39.970490315284124], [43.41186714462, 39.969592000000006], [43.411692290028135, 39.96869368471588], [43.40854834870058, 39.957417684715885], [43.40654438609684, 39.95377868471588], [43.40606663129091, 39.95312107228669]]
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
        [[43.529717999999995, 39.8730992117897], [43.528903876920864, 39.873400090358366], [43.52830789049668, 39.874222105894845], [43.52808974285286, 39.875344999999996], [43.52830789049668, 39.87646789410515], [43.52891990480467, 39.87772989410515], [43.5295158851816, 39.87855190964163], [43.53033, 39.8788527882103], [43.54005600000001, 39.8822607882103], [43.54086997253583, 39.88195990964164], [43.54146583482121, 39.88113789410515], [43.54168393408258, 39.880015], [43.54146583482121, 39.878892105894856], [43.53998286949843, 39.87655310589486], [43.53938699255669, 39.87573109035837], [43.53857299999999, 39.875430211789705]]
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
        [43.413337, 39.93146], [43.399239, 39.958595], [43.405414, 39.954677], [43.410149, 39.96911], [43.394531, 39.991941], [43.414441, 39.949121], [43.419568, 39.931381], [43.529718, 39.875345], [43.540056, 39.880015], [43.544621, 39.87877], [43.517264, 39.993583], [43.520777, 39.996083], [43.524942, 39.997254], [43.66848, 40.257731], [43.673304, 40.182899], [43.672435, 40.296279], [43.624629, 40.310452], [43.694211, 40.314328]
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
    setTimeout(() => { document.querySelector('.info-panel').scrollIntoView({behavior: 'smooth', block: 'center'}); }, 100);
    
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
    
    document.getElementById('guide').style.backgroundImage = linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url();
}

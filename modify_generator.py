with open('final_js_generator.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re

# Swap 1 and 2, and add Ornithological Park as 4
# Currently in final_js_generator:
# 1 is coords['1'] (Sirius)
# 2 is coords['2'] (Port)
# 4 is coords['4'] (Olympic Beach)
# 5 is coords['5'] (Buran)

code = code.replace(
    '{ id: "1", coords: {coords[\'1\']}',
    '{ id: "1", coords: {coords[\'2\']}'
).replace(
    'title: "1. Сириус", yandexUrl: "https://yandex.ru/maps/-/CXU8mH74", category: "Город/Курорт", brief: "Современный курорт и образовательный центр.", desc: "Стартовая точка маршрута. Имеретинская низменность, преображенная к Олимпиаде 2014.", importance: "Федеральная территория с особым статусом, центр науки и спорта.", fact: "До Олимпиады здесь располагался поселок староверов Марлинский.", img: "{data[0][\'img\']}"',
    'title: "1. Имеретинский морской вокзал", yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w", category: "Транспорт/Отдых", brief: "Яхтенная марина и порт.", desc: "Порт, построенный для приема грузовых судов во время олимпийской стройки, теперь превращен в яхтенную марину.", importance: "Морские ворота курорта Сириус, популярное место для прогулок.", fact: "Волны здесь могут достигать нескольких метров во время зимних штормов.", img: "{data[1][\'img\']}"'
)

code = code.replace(
    '{ id: "2", coords: {coords[\'2\']}',
    '{ id: "2", coords: {coords[\'4\']}'
).replace(
    'title: "2. Имеретинский морской вокзал", yandexUrl: "https://yandex.ru/maps/-/CXU8mL7w", category: "Транспорт/Отдых", brief: "Яхтенная марина и порт.", desc: "Порт, построенный для приема грузовых судов во время олимпийской стройки, теперь превращен в яхтенную марину.", importance: "Морские ворота курорта Сириус, популярное место для прогулок.", fact: "Волны здесь могут достигать нескольких метров во время зимних штормов.", img: "{data[1][\'img\']}"',
    'title: "2. Олимпийский пляж", yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D", category: "Отдых", brief: "Широкий галечный пляж Сириуса.", desc: "Один из самых чистых пляжей побережья без волнорезов.", importance: "Главная рекреационная зона у моря.", fact: "Часто дельфины подплывают близко к берегу.", img: "{data[10][\'img\']}"'
)

# Replace old 4 (which was beach) with ornithological park
# coords for orn park: 43.398014, 39.972986
code = code.replace(
    '{ id: "4", coords: {coords[\'4\']}',
    '{ id: "4", coords: [43.398014, 39.972986]'
).replace(
    'title: "4. Олимпийский пляж", yandexUrl: "https://yandex.ru/maps/-/CXU8uU4D", category: "Отдых", brief: "Широкий галечный пляж Сириуса.", desc: "Один из самых чистых пляжей побережья без волнорезов.", importance: "Главная рекреационная зона у моря.", fact: "Часто дельфины подплывают близко к берегу.", img: "{data[11][\'img\']}"',
    'title: "4. Орнитологический парк", yandexUrl: "https://yandex.ru/maps/org/prirodniy_ornitologicheskiy_park_v_imeretinskoy_nizmennosti/115591322258/", category: "Природа/Парк", brief: "Природный оазис для птиц.", desc: "Природный орнитологический парк в Имеретинской низменности. Здесь останавливаются перелетные птицы.", importance: "Важный экологический объект для сохранения биоразнообразия региона.", fact: "В парке зарегистрировано более 200 видов птиц.", img: "https://avatars.mds.yandex.net/get-altay/223006/2a0000015cb7ed258dc71f84d0b13cfcc7a1/L_height"'
)

# Route line adjustment
code = code.replace(
    'coords[\'1\'], coords[\'2\'],',
    'coords[\'2\'], coords[\'4\'],'
).replace(
    'coords[\'4\'], coords[\'5\'],',
    '[43.398014, 39.972986], coords[\'5\'],'
)

with open('final_js_generator.py', 'w', encoding='utf-8') as f:
    f.write(code)

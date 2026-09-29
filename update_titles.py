import re

with open('script.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Update Titles
c = re.sub(r'title:\s*\"1\.\s*[^\"]+\"', 'title: \"1. Имеретинский морской вокзал\"', c)
c = re.sub(r'title:\s*\"2\.\s*[^\"]+\"', 'title: \"2. Олимпийский пляж\"', c)
c = re.sub(r'title:\s*\"6\.4\s*[^\"]+\"', 'title: \"6.4 Буковая поляна\"', c)

# Use Regex to replace circles with polygons
pattern_circles = r'// Олимпийский парк \(круг\)[\s\S]*?// 2\. Линия основного маршрута'
polygons_code = '''// Олимпийский парк (многоугольник по крайним точкам)
    var olympicPolygon = new ymaps.Polygon([[
        [43.400351, 39.958225], // Фишт
        [43.403427, 39.957647], // Фонтаны
        [43.406159, 39.958155], // Айсберг
        [43.410152, 39.969803], // Автодром / Музей
        [43.407913, 39.971830], // Центр Сириус
        [43.403977, 39.972947], // Сочи Парк
        [43.400351, 39.958225]
    ]], {
        hintContent: 'Олимпийский парк'
    }, {
        fillColor: "#007bff33",
        strokeColor: "#007bff",
        strokeOpacity: 0.8,
        strokeWidth: 2
    });
    window.mapObj.geoObjects.add(olympicPolygon);

    // Тисо-самшитовая роща (многоугольник)
    var tisoPolygon = new ymaps.Polygon([[
        [43.529718, 39.875345], // Тис-великан
        [43.530330, 39.876607], // Лабиринт
        [43.537020, 39.878943], // Буковая поляна
        [43.540056, 39.880015], // Крепость
        [43.529718, 39.875345]
    ]], {
        hintContent: 'Тисо-самшитовая роща'
    }, {
        fillColor: "#28a74533",
        strokeColor: "#28a745",
        strokeOpacity: 0.8,
        strokeWidth: 2
    });
    window.mapObj.geoObjects.add(tisoPolygon);

    // 2. Линия основного маршрута'''

c = re.sub(pattern_circles, polygons_code, c)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated script.js titles and polygons')

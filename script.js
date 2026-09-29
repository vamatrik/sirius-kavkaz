

const guideBg = {
    'guide-intro': 'https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height',
    'guide-geo': 'https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height',
    'guide-eco': 'https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height',
    'guide-pop': 'https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height'
};

function switchGuide(event, targetId) {
    document.querySelectorAll('#guide-nav li').forEach(li => {
        li.classList.remove('active');
    });
    if(event && event.currentTarget) event.currentTarget.classList.add('active');
    
    document.querySelectorAll('.guide-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    document.getElementById(targetId).classList.add('active');

    // Change background of guide section
    document.getElementById('guide').style.backgroundImage = `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url(${guideBg[targetId]})`;
    document.getElementById('guide').style.backgroundSize = 'cover';
    document.getElementById('guide').style.backgroundPosition = 'center';
}

// Навигация
);
    
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.classList.remove('active');
    });
    
    document.getElementById(pageId).classList.add('active');
    document.getElementById('link-' + pageId).classList.add('active');

    if(pageId === 'route' && window.mapObj) {
        window.mapObj.container.fitToViewport();
        window.mapObj.setBounds(window.mapObj.geoObjects.getBounds(), {
            checkZoomRange: true,
            zoomMargin: 30
        });
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
        [[43.405414, 39.952204049889716], [43.40494899991897, 39.95228831362135], [43.40154099991897, 39.95350144799435], [43.40110768882501, 39.95374848285773], [43.4007355961531, 39.95414145857534], [43.40045007940391, 39.95465359450144], [43.40027059607206, 39.955249989419], [43.400209377650015, 39.95589], [43.40027059607206, 39.95653001058099], [43.40277059607206, 39.968579036992594], [43.40295007940391, 39.96917545652185], [43.403235596153095, 39.969687613582494], [43.40749068882501, 39.97418174280371], [43.40792399991897, 39.97442880369829], [43.408389, 39.97451307156851], [43.40885400008103, 39.97442880369829], [43.40928731117499, 39.97418174280371], [43.4096594038469, 39.97378872567646], [43.4118324038469, 39.97134078841612], [43.41211792059609, 39.9708285801479], [43.41229740392794, 39.970232100986145], [43.412358622349984, 39.969592], [43.41229740392794, 39.96895189901385], [43.40915340392794, 39.95767593223889], [43.40897392059609, 39.95707948403793], [43.40696992059609, 39.95344052494486], [43.4066844038469, 39.95292836020748], [43.40631231117499, 39.9525353623822], [43.40587900008103, 39.95228831362135]]
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
        [[43.529718, 39.87224744891545], [43.52913674989871, 39.87235299540919], [43.528595111031265, 39.87266244207127], [43.52812999519137, 39.87315470062305], [43.52777309925489, 39.87379622445773], [43.52754874509008, 39.87454329478614], [43.52747222206253, 39.875345], [43.52754874509008, 39.87614670521386], [43.52777309925489, 39.87689377554228], [43.52838509925488, 39.87815579125767], [43.52874199519137, 39.87879732160188], [43.52920711103126, 39.8792895851486], [43.52974874989871, 39.87959903495062], [43.53947474989871, 39.88300751756199], [43.540056, 39.88311308215139], [43.54063725010129, 39.88300751756199], [43.54117888896874, 39.88269801784612], [43.54164400480863, 39.88220567489792], [43.542000900745116, 39.88156404107569], [43.54222525490992, 39.880816842664075], [43.542301777937475, 39.880015], [43.54222525490992, 39.879213157335926], [43.542000900745116, 39.87846595892431], [43.54164400480863, 39.87782432510208], [43.54016100480863, 39.87548537898336], [43.53969588896874, 39.87499304814471], [43.53915425010129, 39.874683556041205], [43.530299250101294, 39.87235299540919]]
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
        [43.413337, 39.93146], [43.399239, 39.958595], [43.405414, 39.954677], [43.410149, 39.96911], [43.394531, 39.991941], [43.414441, 39.949121], [43.529718, 39.875345], [43.540056, 39.880015], [43.544621, 39.87877], [43.517264, 39.993583], [43.520777, 39.996083], [43.524942, 39.997254], [43.66848, 40.257731], [43.673304, 40.182899], [43.672435, 40.296279], [43.624629, 40.310452], [43.694211, 40.314328]
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

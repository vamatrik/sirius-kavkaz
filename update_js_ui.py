import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace switchGuide
old_sg = r"function switchGuide\(event, targetId\) \{.*?\}"
new_sg = '''function switchGuide(event, targetId) {
    document.querySelectorAll('#guide-nav li').forEach(li => {
        li.classList.remove('active');
    });
    if(event && event.currentTarget) event.currentTarget.classList.add('active');
    
    document.querySelectorAll('.guide-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    document.getElementById(targetId).classList.add('active');

    const guideBg = {
        'guide-brief': 'https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height',
        'guide-intro': 'https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height',
        'guide-geo': 'https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height',
        'guide-eco': 'https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height',
        'guide-flora': 'https://avatars.mds.yandex.net/get-altay/239474/2a0000015d059ec428668e23acb2be76bb46/L_height',
        'guide-pop': 'user_photos/Буран снаружи.jpg'
    };
    
    if(guideBg[targetId]) {
        document.getElementById('guide').style.backgroundImage = `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url("${guideBg[targetId]}")`;
    }
}'''

js = re.sub(old_sg, new_sg, js, flags=re.DOTALL)

# Replace showPointInfo
old_spi = r"function showPointInfo\(point\) \{.*?\}(?=\n\n)"
new_spi = '''function showPointInfo(point) {
    document.getElementById('p-category').innerText = point.category;
    
    if(point.yandexUrl) {
        document.getElementById('p-title-link').innerText = point.title;
        document.getElementById('p-title-link').href = point.yandexUrl;
        document.getElementById('p-title-link').style.pointerEvents = "auto";
        document.getElementById('p-title-link').style.textDecoration = "underline";
    } else {
        document.getElementById('p-title-link').innerText = point.title;
        document.getElementById('p-title-link').removeAttribute('href');
        document.getElementById('p-title-link').style.pointerEvents = "none";
        document.getElementById('p-title-link').style.textDecoration = "none";
    }
    
    document.getElementById('p-brief').innerText = point.brief;
    document.getElementById('p-desc').innerText = point.desc;
    document.getElementById('p-importance').innerText = point.importance;
    document.getElementById('p-fact').innerText = point.fact;
    
    const topGallery = document.getElementById('p-gallery-top');
    const bottomGallery = document.getElementById('p-gallery-bottom');
    if(topGallery) topGallery.innerHTML = '';
    if(bottomGallery) bottomGallery.innerHTML = '';
    
    let allImages = [];
    if(point.images && point.images.length > 0) {
        allImages = point.images;
    } else if (point.img) {
        allImages.push({url: point.img, caption: ''});
    }

    const midPoint = Math.ceil(allImages.length / 2);
    
    allImages.forEach((imgObj, index) => {
        let capHTML = imgObj.caption ? `<div class="masonry-caption">${imgObj.caption}</div>` : '';
        let itemHTML = `<div class="masonry-item"><img src="${imgObj.url}" alt="">${capHTML}</div>`;
        if(index < midPoint) {
            if(topGallery) topGallery.innerHTML += itemHTML;
        } else {
            if(bottomGallery) bottomGallery.innerHTML += itemHTML;
        }
    });

    const videoContainer = document.getElementById('p-video-container');
    if(videoContainer) {
        if(point.videoUrl) {
            videoContainer.innerHTML = `<iframe width="100%" height="315" src="${point.videoUrl}" frameborder="0" allowfullscreen></iframe>`;
            videoContainer.style.display = 'block';
        } else {
            videoContainer.innerHTML = '';
            videoContainer.style.display = 'none';
        }
    }

    document.querySelector('.info-content').style.display = 'block';
    setTimeout(() => { document.querySelector('.info-panel').scrollIntoView({behavior: 'smooth', block: 'center'}); }, 100);
}'''

js = re.sub(old_spi, new_spi, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

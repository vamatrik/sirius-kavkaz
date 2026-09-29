import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update switchGuide
switch_guide_new = '''
const guideBg = {
    'guide-intro': 'https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height',
    'guide-geo': 'https://avatars.mds.yandex.net/get-altay/19816667/2a0000019ecafbf514f5e2c7a7a6f9617b62/L_height',
    'guide-eco': 'https://avatars.mds.yandex.net/get-altay/2094876/2a0000016d3f3bc2b1494e4c1a89184a9420/L_height',
    'guide-pop': 'https://avatars.mds.yandex.net/get-altay/18748727/2a0000019db9f02b67007d4c6c3cebce75cf/L_height'
};

function switchGuide(targetId) {
    document.querySelectorAll('#guide-nav li').forEach(li => {
        li.classList.remove('active');
    });
    event.target.classList.add('active');
    
    document.querySelectorAll('.guide-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    document.getElementById(targetId).classList.add('active');

    // Change background of guide section
    document.getElementById('guide').style.backgroundImage = `linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url(${guideBg[targetId]})`;
    document.getElementById('guide').style.backgroundSize = 'cover';
    document.getElementById('guide').style.backgroundPosition = 'center';
}
'''
js = re.sub(r'function switchGuide\(targetId\) \{.*?(?=\n// Навигация|\nfunction showPage)', switch_guide_new, js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

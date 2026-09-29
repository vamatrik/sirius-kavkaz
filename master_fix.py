import re

# --- INDEX.HTML FIXES ---
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix navigation links for scrolling
html = re.sub(r'href="#" onclick="showPage\(\'home\'\)"[^>]*', 'href="#home"', html)
html = re.sub(r'href="#" onclick="showPage\(\'guide\'\)"[^>]*', 'href="#guide"', html)
html = re.sub(r'href="#" onclick="showPage\(\'route\'\)"[^>]*', 'href="#route"', html)

# Home buttons
html = html.replace('onclick="showPage(\'guide\')"', 'onclick="document.getElementById(\'guide\').scrollIntoView({behavior: \'smooth\'})"')
html = html.replace('onclick="showPage(\'route\')"', 'onclick="document.getElementById(\'route\').scrollIntoView({behavior: \'smooth\'})"')

# Fix switchGuide calls
html = html.replace("onclick=\"switchGuide('guide-intro')\"", "onclick=\"switchGuide(event, 'guide-intro')\"")
html = html.replace("onclick=\"switchGuide('guide-geo')\"", "onclick=\"switchGuide(event, 'guide-geo')\"")
html = html.replace("onclick=\"switchGuide('guide-eco')\"", "onclick=\"switchGuide(event, 'guide-eco')\"")
html = html.replace("onclick=\"switchGuide('guide-pop')\"", "onclick=\"switchGuide(event, 'guide-pop')\"")

# Remove "page" classes
html = re.sub(r'<section id="home"[^>]*>', '<section id="home" class="scroll-section">', html)
html = re.sub(r'<section id="guide"[^>]*>', '<section id="guide" class="scroll-section">', html)
html = re.sub(r'<section id="route"[^>]*>', '<section id="route" class="scroll-section">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# --- STYLE.CSS FIXES ---
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_overrides = '''
/* ENABLE SMOOTH SCROLLING */
html {
    scroll-behavior: smooth;
}

/* FIX NAVBAR */
.navbar {
    position: fixed !important;
    width: 100% !important;
    top: 0 !important;
    left: 0 !important;
    background: rgba(255, 255, 255, 0.4) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.3) !important;
    z-index: 1000 !important;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1) !important;
}

/* OVERRIDE SPA BEHAVIOR */
.page { display: block !important; }

/* SECTIONS */
.scroll-section {
    min-height: 100vh;
    padding-top: 80px; /* Offset for absolute navbar */
    box-sizing: border-box;
}

/* HOME SECTION */
#home {
    background-image: url('home.jpg') !important;
    background-size: contain !important;
    background-position: top center !important;
    background-repeat: no-repeat !important;
    background-color: #f0f4f8 !important; 
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}

/* APPLE GLASS CARD */
.hero-card {
    background: rgba(255, 255, 255, 0.3) !important;
    backdrop-filter: blur(20px) saturate(180%) !important;
    -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
    border-radius: 30px !important;
    padding: 3rem !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15) !important;
    color: #222 !important;
}
.hero-card h2 { color: #111 !important; text-shadow: none !important; font-weight: 700; }
.hero-card p { color: #222 !important; text-shadow: none !important; font-weight: 500 !important; }

/* GUIDE SECTION */
#guide {
    background-image: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.9)), url('https://avatars.mds.yandex.net/get-altay/18769949/2a0000019c4c1a35d071a4cdfc8c23fd89fc/L_height') !important;
    background-size: cover !important;
    background-position: center !important;
    transition: background-image 0.5s ease;
}

/* ROUTE CONTAINER */
#route {
    background: #f8f9fa !important;
}
.route-container {
    padding: 20px !important;
    max-width: 1200px;
    margin: 0 auto;
}
'''
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_overrides)

# --- SCRIPT.JS FIXES ---
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix switchGuide
js = js.replace('function switchGuide(targetId) {', 'function switchGuide(event, targetId) {')
js = js.replace('event.target.classList.add(\'active\');', 'if(event && event.currentTarget) event.currentTarget.classList.add(\'active\');')

# Remove showPage logic completely, just make it smooth scroll
js = re.sub(r'function showPage\(pageId\) \{.*?\}', '', js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

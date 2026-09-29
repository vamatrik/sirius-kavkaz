import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will append the new CSS and override old classes, or completely replace.
# It's better to replace specific blocks.
# Replace #home block
css = re.sub(r'#home\s*{[^}]*}', '''#home {
    background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.4)), url('https://images.unsplash.com/photo-1549488344-c7ab275ccb98?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}''', css)

# Add home hero card CSS
css += '''
.hero-content {
    max-width: 800px;
    text-align: center;
}
.hero-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    padding: 3rem;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}
.hero-card h2 { font-size: 3.5rem; margin-bottom: 1.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
.hero-card p { font-size: 1.2rem; margin-bottom: 2rem; line-height: 1.6; text-shadow: 0 1px 2px rgba(0,0,0,0.5); }
.hero-card .btn { margin: 0 10px; }

/* Guide Sidebar Layout */
.guide-container {
    display: flex;
    gap: 30px;
    margin-top: 30px;
    align-items: flex-start;
}
.guide-sidebar {
    flex: 0 0 250px;
}
#guide-nav {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 10px;
}
#guide-nav li {
    padding: 15px 20px;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(5px);
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    font-weight: 500;
    border-left: 4px solid transparent;
}
#guide-nav li:hover { background: #e9ecef; }
#guide-nav li.active {
    background: #e0f2f1;
    border-left: 4px solid #009688;
    color: #00796b;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.guide-content {
    flex: 1;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 40px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.05);
    border: 1px solid rgba(255,255,255,0.4);
}
.guide-pane { display: none; animation: fadeIn 0.4s ease; }
.guide-pane.active { display: block; }
.guide-pane h3 { margin-bottom: 20px; color: #333; font-size: 1.8rem; }
.guide-pane p { font-size: 1.1rem; line-height: 1.6; }

/* Route Vertical Layout */
.route-container {
    display: flex;
    flex-direction: column;
    height: auto;
    gap: 20px;
}
.map-container {
    height: 65vh;
    width: 100%;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}
#map {
    width: 100%;
    height: 100%;
}
.info-panel {
    width: 100%;
    height: auto;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.4);
    overflow: hidden;
}
.empty-state { padding: 40px; text-align: center; }
.info-content {
    display: flex;
    flex-direction: row;
    gap: 30px;
    padding: 30px;
}
.info-media {
    flex: 0 0 40%;
}
.info-media img, .info-media #p-video iframe {
    width: 100%;
    height: 350px;
    object-fit: cover;
    border-radius: 15px;
}
.info-text {
    flex: 1;
    display: flex;
    flex-direction: column;
}

@media (max-width: 900px) {
    .info-content { flex-direction: column; }
    .info-media { flex: 0 0 auto; }
    .guide-container { flex-direction: column; }
    .guide-sidebar { flex: 1; }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Glassmorphism background for body */
body {
    background: #f0f4f8 url('https://www.transparenttextures.com/patterns/cubes.png');
}
'''
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update script.js for guide navigation and zoom fix
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add switchGuide function
switch_guide_js = '''
function switchGuide(targetId) {
    document.querySelectorAll('#guide-nav li').forEach(li => {
        li.classList.remove('active');
    });
    event.target.classList.add('active');
    
    document.querySelectorAll('.guide-pane').forEach(pane => {
        pane.classList.remove('active');
    });
    document.getElementById(targetId).classList.add('active');
}
'''
js = switch_guide_js + js

# Fix zoom on route load
js = js.replace('''    if(pageId === 'route' && window.mapObj) {
        window.mapObj.container.fitToViewport();
    }''', '''    if(pageId === 'route' && window.mapObj) {
        window.mapObj.container.fitToViewport();
        window.mapObj.setBounds(window.mapObj.geoObjects.getBounds(), {
            checkZoomRange: true,
            zoomMargin: 30
        });
    }''')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

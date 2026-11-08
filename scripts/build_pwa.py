import os
import json
import re

PWA_DIR = "/Users/macbookpro/sound-play/pwa"
DRAWABLE_DIR = "/Users/macbookpro/sound-play/app/src/main/res/drawable"

categories = [
    {
        "id": "animal",
        "title": "Hewan",
        "icon": "🐾",
        "color": "#FF9800",
        "items": [
            {"name": "KUCING", "audio": "sounds/animal_cat.wav", "xml": "ic_animal_cat.xml", "bg": "#FFE0B2"},
            {"name": "ANJING", "audio": "sounds/animal_dog.wav", "xml": "ic_animal_dog.xml", "bg": "#FFF9C4"},
            {"name": "SAPI", "audio": "sounds/animal_cow.wav", "xml": "ic_animal_cow.xml", "bg": "#B2EBF2"},
            {"name": "AYAM", "audio": "sounds/animal_rooster.wav", "xml": "ic_animal_rooster.xml", "bg": "#FFCDD2"},
            {"name": "BEBEK", "audio": "sounds/animal_duck.wav", "xml": "ic_animal_duck.xml", "bg": "#FFF9C4"},
            {"name": "SINGA", "audio": "sounds/animal_lion.wav", "xml": "ic_animal_lion.xml", "bg": "#FFE0B2"},
            {"name": "GAJAH", "audio": "sounds/animal_elephant.wav", "xml": "ic_animal_elephant.xml", "bg": "#BBDEFB"},
            {"name": "KUDA", "audio": "sounds/animal_horse.wav", "xml": "ic_animal_horse.xml", "bg": "#F8BBD0"},
            {"name": "DOMBA", "audio": "sounds/animal_sheep.wav", "xml": "ic_animal_sheep.xml", "bg": "#C8E6C9"},
            {"name": "BURUNG", "audio": "sounds/animal_bird.wav", "xml": "ic_animal_bird.xml", "bg": "#B2EBF2"}
        ]
    },
    {
        "id": "vehicle",
        "title": "Kendaraan",
        "icon": "🚗",
        "color": "#03A9F4",
        "items": [
            {"name": "MOBIL", "audio": "sounds/vehicle_car.wav", "xml": "ic_vehicle_car.xml", "bg": "#FFCDD2"},
            {"name": "MOTOR", "audio": "sounds/vehicle_motorcycle.wav", "xml": "ic_vehicle_motorcycle.xml", "bg": "#B2EBF2"},
            {"name": "BUS", "audio": "sounds/vehicle_bus.wav", "xml": "ic_vehicle_bus.xml", "bg": "#FFF9C4"},
            {"name": "KERETA API", "audio": "sounds/vehicle_train.wav", "xml": "ic_vehicle_train.xml", "bg": "#C8E6C9"},
            {"name": "PESAWAT", "audio": "sounds/vehicle_airplane.wav", "xml": "ic_vehicle_airplane.xml", "bg": "#BBDEFB"},
            {"name": "HELIKOPTER", "audio": "sounds/vehicle_helicopter.wav", "xml": "ic_vehicle_helicopter.xml", "bg": "#FFE0B2"},
            {"name": "KAPAL LAUT", "audio": "sounds/vehicle_ship.wav", "xml": "ic_vehicle_ship.xml", "bg": "#B2EBF2"},
            {"name": "SEPEDA", "audio": "sounds/vehicle_bicycle.wav", "xml": "ic_vehicle_bicycle.xml", "bg": "#E1BEE7"},
            {"name": "AMBULANS", "audio": "sounds/vehicle_ambulance.wav", "xml": "ic_vehicle_ambulance.xml", "bg": "#F8BBD0"},
            {"name": "PEMADAM", "audio": "sounds/vehicle_fire_truck.wav", "xml": "ic_vehicle_fire_truck.xml", "bg": "#FFCDD2"}
        ]
    },
    {
        "id": "music",
        "title": "Alat Musik",
        "icon": "🎵",
        "color": "#9C27B0",
        "items": [
            {"name": "GITAR", "audio": "sounds/music_guitar.wav", "xml": "ic_music_guitar.xml", "bg": "#FFE0B2"},
            {"name": "PIANO", "audio": "sounds/music_piano.wav", "xml": "ic_music_piano.xml", "bg": "#BBDEFB"},
            {"name": "DRUM", "audio": "sounds/music_drum.wav", "xml": "ic_music_drum.xml", "bg": "#FFCDD2"},
            {"name": "TEROMPET", "audio": "sounds/music_trumpet.wav", "xml": "ic_music_trumpet.xml", "bg": "#FFF9C4"},
            {"name": "BIOLA", "audio": "sounds/music_violin.wav", "xml": "ic_music_violin.xml", "bg": "#E1BEE7"},
            {"name": "XYLOPHONE", "audio": "sounds/music_xylophone.wav", "xml": "ic_music_xylophone.xml", "bg": "#B2EBF2"},
            {"name": "SERULING", "audio": "sounds/music_flute.wav", "xml": "ic_music_flute.xml", "bg": "#C8E6C9"},
            {"name": "HARMONIKA", "audio": "sounds/music_harmonica.wav", "xml": "ic_music_harmonica.xml", "bg": "#BBDEFB"},
            {"name": "MARAKAS", "audio": "sounds/music_maracas.wav", "xml": "ic_music_maracas.xml", "bg": "#F8BBD0"},
            {"name": "SAKSOFON", "audio": "sounds/music_saxophone.wav", "xml": "ic_music_saxophone.xml", "bg": "#FFF9C4"}
        ]
    }
]

def xml_to_svg(xml_content):
    paths = []
    path_matches = re.findall(r'<path\s+([^>]+)/>', xml_content)
    for p in path_matches:
        d_match = re.search(r'android:pathData="([^"]+)"', p)
        fill_match = re.search(r'android:fillColor="([^"]+)"', p)
        stroke_match = re.search(r'android:strokeColor="([^"]+)"', p)
        stroke_w_match = re.search(r'android:strokeWidth="([^"]+)"', p)
        cap_match = re.search(r'android:strokeLineCap="([^"]+)"', p)
        join_match = re.search(r'android:strokeLineJoin="([^"]+)"', p)

        attrs = []
        if d_match:
            attrs.append(f'd="{d_match.group(1)}"')
        fill = fill_match.group(1) if fill_match else 'none'
        if fill == '#00000000':
            fill = 'none'
        attrs.append(f'fill="{fill}"')
        if stroke_match:
            attrs.append(f'stroke="{stroke_match.group(1)}"')
        if stroke_w_match:
            attrs.append(f'stroke-width="{stroke_w_match.group(1)}"')
        if cap_match:
            attrs.append(f'stroke-linecap="{cap_match.group(1)}"')
        if join_match:
            attrs.append(f'stroke-linejoin="{join_match.group(1)}"')
        paths.append(f'<path {" ".join(attrs)} />')
    return f'<svg viewBox="0 0 100 100" width="105" height="105" xmlns="http://www.w3.org/2000/svg">{" ".join(paths)}</svg>'

# Convert all drawables to SVG
for cat in categories:
    for item in cat['items']:
        xml_file = os.path.join(DRAWABLE_DIR, item['xml'])
        if os.path.exists(xml_file):
            with open(xml_file) as f:
                item['svg'] = xml_to_svg(f.read())
        else:
            item['svg'] = '<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="#FFB74D"/></svg>'

# Build Manifest
manifest = {
    "name": "Sound Play",
    "short_name": "SoundPlay",
    "description": "Aplikasi Belajar Suara untuk Balita - 100% Offline",
    "start_url": "./index.html",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#FFFDF6",
    "theme_color": "#FF6B6B",
    "icons": [
        {
            "src": "icons/icon-192.svg",
            "sizes": "192x192 512x512",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        }
    ]
}

with open(os.path.join(PWA_DIR, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=2)

# Build App Icon SVG
icon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108" width="192" height="192">
    <circle cx="54" cy="54" r="50" fill="#FF6B6B"/>
    <path fill="#FFFFFF" d="M40,43 L32,43 C30.9,43 30,43.9 30,45 L30,63 C30,64.1 30.9,65 32,65 L40,65 L52,77 L52,31 L40,43 Z M62,40 C67.5,43.2 71,48.2 71,54 C71,59.8 67.5,64.8 62,68 L62,63.5 C65.3,61 67.5,57.8 67.5,54 C67.5,50.2 65.3,47 62,44.5 L62,40 Z M62,29 C72,32.7 78,42.5 78,54 C78,65.5 72,75.3 62,79 L62,74.5 C70,71 74.5,63.2 74.5,54 C74.5,44.8 70,37 62,33.5 L62,29 Z"/>
</svg>"""

with open(os.path.join(PWA_DIR, "icons", "icon-192.svg"), "w") as f:
    f.write(icon_svg)

# List of assets to precache in Service Worker
cached_assets = [
    "./",
    "./index.html",
    "./manifest.json",
    "./icons/icon-192.svg"
]
for cat in categories:
    for item in cat['items']:
        cached_assets.append(f"./{item['audio']}")

sw_js = f"""// Sound Play Service Worker for 100% Offline Capability
const CACHE_NAME = 'sound-play-v1';
const ASSETS_TO_CACHE = {json.dumps(cached_assets, indent=2)};

self.addEventListener('install', (event) => {{
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {{
            console.log('[SW] Pre-caching offline assets...');
            return cache.addAll(ASSETS_TO_CACHE);
        }}).then(() => self.skipWaiting())
    );
}});

self.addEventListener('activate', (event) => {{
    event.waitUntil(
        caches.keys().then((keys) => {{
            return Promise.all(
                keys.map((key) => {{
                    if (key !== CACHE_NAME) {{
                        console.log('[SW] Removing old cache', key);
                        return caches.delete(key);
                    }}
                }})
            );
        }}).then(() => self.clients.claim())
    );
}});

self.addEventListener('fetch', (event) => {{
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {{
            if (cachedResponse) {{
                return cachedResponse;
            }}
            return fetch(event.request);
        }})
    );
}});
"""

with open(os.path.join(PWA_DIR, "sw.js"), "w") as f:
    f.write(sw_js)

# Build index.html
html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#FF6B6B">
    <title>Sound Play - Belajar Bunyi untuk Balita</title>
    <link rel="manifest" href="manifest.json">
    <link rel="icon" href="icons/icon-192.svg">
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
            -webkit-user-select: none;
            -webkit-tap-highlight-color: transparent;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: #FFFDF6;
            color: #2D3436;
            min-height: 100vh;
            display: flex;
            justify-content: center;
        }}
        .app {{
            width: 100%;
            max-width: 460px;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background: #FFFDF6;
            box-shadow: 0 0 25px rgba(0,0,0,0.06);
        }}
        /* Header */
        .header {{
            padding: 16px 18px 12px;
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .logo-circle {{
            width: 46px;
            height: 46px;
            background: #FF6B6B;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            box-shadow: 0 4px 10px rgba(255, 107, 107, 0.35);
        }}
        .header-title {{
            font-size: 24px;
            font-weight: 900;
            color: #FF6B6B;
            line-height: 1.1;
        }}
        .header-subtitle {{
            font-size: 13px;
            color: #636E72;
            font-weight: 500;
            margin-top: 2px;
        }}
        /* 3 Posisi Tabs */
        .tabs {{
            display: flex;
            gap: 8px;
            padding: 4px 14px 12px;
        }}
        .tab-btn {{
            flex: 1;
            padding: 12px 6px;
            border-radius: 24px;
            background: #DFE6E9;
            color: #747D8C;
            font-size: 14px;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            cursor: pointer;
            border: none;
            outline: none;
            transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}
        .tab-btn.active-animal {{
            background: #FF9800;
            color: #FFFFFF;
            box-shadow: 0 4px 12px rgba(255, 152, 0, 0.35);
        }}
        .tab-btn.active-vehicle {{
            background: #03A9F4;
            color: #FFFFFF;
            box-shadow: 0 4px 12px rgba(3, 169, 244, 0.35);
        }}
        .tab-btn.active-music {{
            background: #9C27B0;
            color: #FFFFFF;
            box-shadow: 0 4px 12px rgba(156, 39, 176, 0.35);
        }}
        /* Grid Kartu */
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
            padding: 6px 14px 30px;
            overflow-y: auto;
        }}
        .card {{
            border-radius: 22px;
            padding: 16px 12px 14px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            border: 1px solid rgba(0,0,0,0.06);
            cursor: pointer;
            transition: transform 0.15s cubic-bezier(0.175, 0.885, 0.32, 1.4);
        }}
        .card:active, .card.bounce {{
            transform: scale(0.92);
        }}
        .card-img {{
            width: 105px;
            height: 105px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 8px;
        }}
        .card-name {{
            font-size: 19px;
            font-weight: 900;
            color: #2D3436;
            margin-bottom: 10px;
            letter-spacing: 0.5px;
        }}
        .play-btn {{
            width: 52px;
            height: 52px;
            background: #2ED573;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(46, 213, 115, 0.38);
        }}
        .play-btn svg {{
            width: 26px;
            height: 26px;
            fill: #FFFFFF;
            margin-left: 3px;
        }}
        /* Offline Pill Badge */
        .badge-offline {{
            margin-left: auto;
            background: #E8F5E9;
            color: #2E7D32;
            font-size: 11px;
            font-weight: 800;
            padding: 4px 8px;
            border-radius: 12px;
        }}
    </style>
</head>
<body>
    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="logo-circle">🎈</div>
            <div>
                <div class="header-title">Sound Play</div>
                <div class="header-subtitle">Sentuh untuk mendengar suara!</div>
            </div>
            <div class="badge-offline">100% OFFLINE</div>
        </div>

        <!-- 3 Posisi Tab Kategori -->
        <div class="tabs">
            <button class="tab-btn active-animal" onclick="switchCategory('animal')">
                <span>🐾</span> <span>Hewan</span>
            </button>
            <button class="tab-btn" onclick="switchCategory('vehicle')">
                <span>🚗</span> <span>Kendaraan</span>
            </button>
            <button class="tab-btn" onclick="switchCategory('music')">
                <span>🎵</span> <span>Musik</span>
            </button>
        </div>

        <!-- Grid 10 Item per Kategori -->
        <div class="cards-grid" id="cardsGrid"></div>
    </div>

    <script>
        const categoryData = {json.dumps(categories)};
        let activeAudio = null;

        function playSound(audioPath, cardEl) {{
            // Animasi membal
            cardEl.classList.add('bounce');
            setTimeout(() => cardEl.classList.remove('bounce'), 220);

            // Putar audio
            if (activeAudio) {{
                activeAudio.pause();
                activeAudio.currentTime = 0;
            }}
            activeAudio = new Audio(audioPath);
            activeAudio.play().catch(err => console.log('Playback error:', err));
        }}

        function switchCategory(catId) {{
            const buttons = document.querySelectorAll('.tab-btn');
            buttons[0].className = 'tab-btn ' + (catId === 'animal' ? 'active-animal' : '');
            buttons[1].className = 'tab-btn ' + (catId === 'vehicle' ? 'active-vehicle' : '');
            buttons[2].className = 'tab-btn ' + (catId === 'music' ? 'active-music' : '');

            const cat = categoryData.find(c => c.id === catId);
            const grid = document.getElementById('cardsGrid');
            grid.innerHTML = '';

            cat.items.forEach(item => {{
                const card = document.createElement('div');
                card.className = 'card';
                card.style.background = item.bg;
                card.innerHTML = `
                    <div class="card-img">${{item.svg}}</div>
                    <div class="card-name">${{item.name}}</div>
                    <div class="play-btn">
                        <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                    </div>
                `;
                card.onclick = () => playSound(item.audio, card);
                grid.appendChild(card);
            }});
        }}

        // Inisialisasi awal pada kategori Hewan
        switchCategory('animal');

        // Daftarkan Service Worker untuk fitur 100% Offline
        if ('serviceWorker' in navigator) {{
            window.addEventListener('load', () => {{
                navigator.serviceWorker.register('sw.js')
                    .then(reg => console.log('ServiceWorker registered:', reg.scope))
                    .catch(err => console.log('ServiceWorker registration failed:', err));
            }});
        }}
    </script>
</body>
</html>"""

with open(os.path.join(PWA_DIR, "index.html"), "w") as f:
    f.write(html)

print("PWA generated successfully with 30 items, Service Worker, and Manifest!")

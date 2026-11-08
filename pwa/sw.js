// Sound Play Service Worker for 100% Offline Capability
const CACHE_NAME = 'sound-play-v1';
const ASSETS_TO_CACHE = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icons/icon-192.svg",
  "./sounds/animal_cat.wav",
  "./sounds/animal_dog.wav",
  "./sounds/animal_cow.wav",
  "./sounds/animal_rooster.wav",
  "./sounds/animal_duck.wav",
  "./sounds/animal_lion.wav",
  "./sounds/animal_elephant.wav",
  "./sounds/animal_horse.wav",
  "./sounds/animal_sheep.wav",
  "./sounds/animal_bird.wav",
  "./sounds/vehicle_car.wav",
  "./sounds/vehicle_motorcycle.wav",
  "./sounds/vehicle_bus.wav",
  "./sounds/vehicle_train.wav",
  "./sounds/vehicle_airplane.wav",
  "./sounds/vehicle_helicopter.wav",
  "./sounds/vehicle_ship.wav",
  "./sounds/vehicle_bicycle.wav",
  "./sounds/vehicle_ambulance.wav",
  "./sounds/vehicle_fire_truck.wav",
  "./sounds/music_guitar.wav",
  "./sounds/music_piano.wav",
  "./sounds/music_drum.wav",
  "./sounds/music_trumpet.wav",
  "./sounds/music_violin.wav",
  "./sounds/music_xylophone.wav",
  "./sounds/music_flute.wav",
  "./sounds/music_harmonica.wav",
  "./sounds/music_maracas.wav",
  "./sounds/music_saxophone.wav"
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            console.log('[SW] Pre-caching offline assets...');
            return cache.addAll(ASSETS_TO_CACHE);
        }).then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        console.log('[SW] Removing old cache', key);
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request).then((cachedResponse) => {
            if (cachedResponse) {
                return cachedResponse;
            }
            return fetch(event.request);
        })
    );
});

# Sound Play (Aplikasi Suara Edukasi Balita) 🎈

Aplikasi Android edukasi suara untuk anak-anak di bawah 3 tahun (balita) yang **100% Offline**, ramah anak (*kids-friendly*), dan dibangun menggunakan **Java Native**.

---

## 🌟 Fitur Utama

1. **3 Kategori Bunyi (3 Posisi Tab)**:
   - 🐶 **Hewan (10 Item)**: Kucing, Anjing, Sapi, Ayam, Bebek, Singa, Gajah, Kuda, Domba, Burung.
   - 🚗 **Kendaraan (10 Item)**: Mobil, Motor, Bus, Kereta Api, Pesawat, Helikopter, Kapal Laut, Sepeda, Ambulans, Pemadam Kebakaran.
   - 🎵 **Alat Musik (10 Item)**: Gitar, Piano, Drum, Terompet, Biola, Xylophone, Flute/Seruling, Harmonika, Marakas, Saksofon.
2. **100% Offline Tanpa Internet**:
   - Seluruh 30 file audio (`res/raw`) dan 30 gambar vektor (`res/drawable`) sudah tertanam (*embedded*) di dalam aplikasi.
   - Tidak memerlukan kuota data, Wi-Fi, akun/login, ataupun koneksi internet setelah diinstall di perangkat Android.
3. **Desain Ramah Balita (*Kids-Friendly*)**:
   - Warna-warni pastel yang cerah dan ceria.
   - Tombol dan kartu berukuran besar, mudah disentuh jemari balita.
   - Efek animasi sentuh membal (*tactile bounce animation*) saat gambar atau tombol Play ditekan.
   - Audio Engine menggunakan **SoundPool** (instan berbunyi tanpa jeda/lag meski ditekan berkali-kali).
   - Orientasi layar dikunci (*Portrait*) agar tampilan tetap rapi saat ponsel diputar-putar anak.

---

## 📁 Struktur Project

```
sound-play/
├── app/
│   ├── build.gradle
│   ├── proguard-rules.pro
│   └── src/
│       └── main/
│           ├── AndroidManifest.xml
│           ├── java/com/kids/soundplay/
│           │   ├── MainActivity.java       # Activity utama & navigasi 3 tab
│           │   ├── SoundAdapter.java       # Grid adapter kartu gambar + animasi bounce
│           │   ├── SoundCategory.java      # Enum 3 kategori suara
│           │   ├── SoundItem.java          # Model data item suara
│           │   └── SoundManager.java       # Audio engine SoundPool berkecepatan tinggi
│           └── res/
│               ├── drawable/               # 30 Vektor gambar kartun + ikon UI
│               ├── layout/
│               │   ├── activity_main.xml   # Header, 3 tab, & grid 2 kolom
│               │   └── item_sound_card.xml # Kartu gambar besar + tombol Play
│               ├── raw/                    # 30 File audio (WAV 16-bit)
│               └── values/
│                   ├── colors.xml          # Palet warna pastel ceria
│                   ├── strings.xml         # Nama-nama objek (Bahasa Indonesia)
│                   └── themes.xml          # Tema aplikasi tanpa ActionBar
├── scripts/
│   ├── generate_drawables.py               # Generator aset vektor XML
│   └── generate_sounds.py                  # Generator aset audio non-komersial
├── build.gradle
├── gradle.properties
├── settings.gradle
└── README.md
```

---

## 🚀 Cara Menjalankan & Build APK

### Opsi 1: Menggunakan Android Studio (Paling Mudah)
1. Buka aplikasi **Android Studio**.
2. Pilih **File > Open**, lalu arahkan ke folder `/Users/macbookpro/sound-play`.
3. Tunggu hingga proses *Gradle Sync* selesai otomatis.
4. Hubungkan HP Android Anda via kabel USB (atau gunakan Emulator), lalu klik tombol hijau **Run ▶**.
5. Untuk membuat file installer `.apk`:
   - Klik menu **Build > Build Bundle(s) / APK(s) > Build APK(s)**.
   - Setelah selesai, klik **locate** untuk mendapatkan file `app-debug.apk`.

### Opsi 2: Build lewat Terminal (Command Line)
Jika sudah terpasang JDK dan Android SDK:
```bash
./gradlew assembleDebug
```
File APK akan berada di folder:
`app/build/outputs/apk/debug/app-debug.apk`

---

## 📲 Cara Pasang (*Install*) di HP Android Tanpa Internet

1. Kirim file `app-debug.apk` ke HP Android (bisa lewat kabel data USB, Bluetooth, flashdisk OTG, atau kirim via WhatsApp).
2. Di HP Android, buka file `.apk` tersebut.
3. Jika muncul peringatan keamanan, pilih **Izinkan instalasi dari sumber tidak dikenal** (*Install from Unknown Sources*).
4. Klik **Install** dan buka aplikasinya. Aplikasi langsung siap dimainkan 100% tanpa internet!


import os
import math
import struct
import wave

RAW_DIR = "/Users/macbookpro/sound-play/app/src/main/res/raw"
os.makedirs(RAW_DIR, exist_ok=True)

SAMPLE_RATE = 22050

def save_wav(filename, samples):
    filepath = os.path.join(RAW_DIR, filename)
    with wave.open(filepath, 'w') as wav:
        wav.setnchannels(1)  # Mono
        wav.setsampwidth(2)  # 16-bit
        wav.setframerate(SAMPLE_RATE)
        # Clamp & pack to 16-bit signed integer
        packed = bytearray()
        for s in samples:
            val = max(-1.0, min(1.0, s))
            int_val = int(val * 32767.0)
            packed.extend(struct.pack('<h', int_val))
        wav.writeframes(packed)
    print(f"Generated {filename}: {len(samples)} samples ({len(samples)/SAMPLE_RATE:.2f}s)")

# Helper synthesis primitives
def sine_wave(freq, duration, amp=0.5):
    n = int(SAMPLE_RATE * duration)
    return [amp * math.sin(2.0 * math.pi * freq * i / SAMPLE_RATE) for i in range(n)]

def apply_envelope(samples, attack=0.05, decay=0.1, sustain=0.7, release=0.1):
    total = len(samples)
    att_samples = int(attack * SAMPLE_RATE)
    dec_samples = int(decay * SAMPLE_RATE)
    rel_samples = int(release * SAMPLE_RATE)
    sus_samples = max(0, total - (att_samples + dec_samples + rel_samples))
    
    out = []
    for i in range(total):
        if i < att_samples:
            env = i / max(1, att_samples)
        elif i < att_samples + dec_samples:
            progress = (i - att_samples) / max(1, dec_samples)
            env = 1.0 - progress * (1.0 - sustain)
        elif i < total - rel_samples:
            env = sustain
        else:
            progress = (i - (total - rel_samples)) / max(1, rel_samples)
            env = sustain * (1.0 - progress)
        out.append(samples[i] * env)
    return out

# Synthesizers for each of the 30 items
def gen_cat():
    # "Meee-oww": glide 420Hz -> 680Hz -> 380Hz
    dur = 1.2
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        if t < 0.4:
            f = 420.0 + (680.0 - 420.0) * (t / 0.4)
        else:
            f = 680.0 - (680.0 - 360.0) * ((t - 0.4) / 0.6)
        # Harmonics for nasal "meow"
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        vibrato = 0.05 * math.sin(2.0 * math.pi * 6.0 * i / SAMPLE_RATE)
        s = 0.5 * math.sin(phase + vibrato) + 0.3 * math.sin(2 * phase) + 0.15 * math.sin(3 * phase)
        # Amplitude envelope
        amp = math.sin(math.pi * t)
        samples.append(s * amp * 0.8)
    return samples

def gen_dog():
    # Two sharp barks "Woof! Woof!"
    samples = []
    for bark in range(2):
        dur = 0.28
        n = int(SAMPLE_RATE * dur)
        phase = 0.0
        for i in range(n):
            t = i / n
            f = 350.0 * (1.0 - 0.6 * t)
            phase += 2.0 * math.pi * f / SAMPLE_RATE
            env = math.exp(-6.0 * t)
            # Add gravel/noise
            noise = ((i * 1103515245 + 12345) % 32768) / 16384.0 - 1.0
            s = 0.6 * math.sin(phase) + 0.3 * math.sin(2 * phase) + 0.25 * noise * env
            samples.append(s * env * 0.85)
        # Gap between barks
        samples.extend([0.0] * int(SAMPLE_RATE * 0.15))
    return samples

def gen_cow():
    # "Moooo": 130Hz with rich harmonics and vibrato
    dur = 1.6
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 135.0 - 15.0 * t
        vib = 1.5 * math.sin(2.0 * math.pi * 4.5 * t)
        phase += 2.0 * math.pi * (f + vib) / SAMPLE_RATE
        s = 0.5 * math.sin(phase) + 0.35 * math.sin(2 * phase) + 0.2 * math.sin(3 * phase) + 0.1 * math.sin(4 * phase)
        env = math.sin(math.pi * t) ** 0.8
        samples.append(s * env * 0.85)
    return samples

def gen_rooster():
    # "Ku-ku-ru-yuuuk!"
    notes = [(450, 0.12), (550, 0.12), (680, 0.15), (600, 0.9)]
    samples = []
    for freq, d in notes:
        n = int(SAMPLE_RATE * d)
        phase = 0.0
        for i in range(n):
            t = i / n
            phase += 2.0 * math.pi * freq / SAMPLE_RATE
            # Piercing rooster harmonics
            s = 0.5 * math.sin(phase) + 0.35 * math.sin(2*phase) + 0.25 * math.sin(3*phase) + 0.15 * math.sin(4*phase)
            env = (1.0 - t * 0.3) if d > 0.5 else math.sin(math.pi * t)
            samples.append(s * env * 0.75)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.04))
    return samples

def gen_duck():
    # "Kwek! Kwek! Kwek!"
    samples = []
    for k in range(3):
        dur = 0.22
        n = int(SAMPLE_RATE * dur)
        phase = 0.0
        for i in range(n):
            t = i / n
            f = 320.0 - 60.0 * t
            phase += 2.0 * math.pi * f / SAMPLE_RATE
            # Nasal harmonics
            s = 0.4 * math.sin(phase) + 0.4 * math.sin(3*phase) + 0.3 * math.sin(5*phase)
            env = (math.sin(math.pi * t)) ** 0.6
            samples.append(s * env * 0.8)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.1))
    return samples

def gen_lion():
    # Deep throaty roar
    dur = 1.5
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 90.0 + 30.0 * math.sin(math.pi * t)
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        noise = (((i * 48271) % 65536) / 32768.0 - 1.0)
        s = 0.5 * math.sin(phase) + 0.3 * math.sin(2*phase) + 0.45 * noise
        env = math.sin(math.pi * t) ** 0.5
        samples.append(s * env * 0.8)
    return samples

def gen_elephant():
    # High brassy trumpet
    dur = 1.3
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 500.0 + 600.0 * (t ** 1.5)
        vib = 25.0 * math.sin(2.0 * math.pi * 12.0 * t)
        phase += 2.0 * math.pi * (f + vib) / SAMPLE_RATE
        s = 0.45 * math.sin(phase) + 0.35 * math.sin(2*phase) + 0.25 * math.sin(3*phase) + 0.2 * math.sin(4*phase)
        env = math.sin(math.pi * t) ** 0.6
        samples.append(s * env * 0.8)
    return samples

def gen_horse():
    # Whinny / Neigh
    dur = 1.4
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 900.0 - 350.0 * t
        flutter = 80.0 * math.sin(2.0 * math.pi * 14.0 * t)
        phase += 2.0 * math.pi * (f + flutter) / SAMPLE_RATE
        s = 0.5 * math.sin(phase) + 0.3 * math.sin(2*phase)
        env = (1.0 - t) * (math.sin(math.pi * t) ** 0.3)
        samples.append(s * env * 0.75)
    return samples

def gen_sheep():
    # "Baa-aa-aa" with 11Hz tremolo
    dur = 1.3
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 260.0 - 30.0 * t
        trem = 0.6 + 0.4 * math.sin(2.0 * math.pi * 11.0 * t)
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        s = 0.5 * math.sin(phase) + 0.35 * math.sin(2*phase) + 0.2 * math.sin(3*phase)
        env = math.sin(math.pi * t) ** 0.7
        samples.append(s * env * trem * 0.8)
    return samples

def gen_bird():
    # Sweet cheerful chirps
    samples = []
    for _ in range(4):
        dur = 0.16
        n = int(SAMPLE_RATE * dur)
        phase = 0.0
        for i in range(n):
            t = i / n
            f = 2400.0 + 1400.0 * math.sin(math.pi * t)
            phase += 2.0 * math.pi * f / SAMPLE_RATE
            s = math.sin(phase)
            env = math.sin(math.pi * t)
            samples.append(s * env * 0.6)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.08))
    return samples

# Kendaraan (Vehicles)
def gen_car():
    # Brum brum + Beep-Beep horn
    samples = []
    # Engine rev
    n_rev = int(SAMPLE_RATE * 0.7)
    phase = 0.0
    for i in range(n_rev):
        t = i / n_rev
        f = 80.0 + 80.0 * math.sin(math.pi * t)
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        noise = (((i * 12345) % 32768) / 16384.0 - 1.0)
        s = 0.5 * math.sin(phase) + 0.3 * math.sin(2*phase) + 0.25 * noise
        samples.append(s * 0.6 * math.sin(math.pi * t))
    samples.extend([0.0] * int(SAMPLE_RATE * 0.08))
    # Beep beep
    for _ in range(2):
        n_beep = int(SAMPLE_RATE * 0.18)
        for i in range(n_beep):
            t = i / n_beep
            s = 0.45 * math.sin(2.0 * math.pi * 440.0 * i / SAMPLE_RATE) + 0.45 * math.sin(2.0 * math.pi * 554.0 * i / SAMPLE_RATE)
            samples.append(s * math.sin(math.pi * t) * 0.85)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.08))
    return samples

def gen_motorcycle():
    # 2-stroke motorcycle rev: Ngeeeng!
    dur = 1.3
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 110.0 + 260.0 * (t ** 1.8) if t < 0.7 else 370.0 - 180.0 * ((t - 0.7) / 0.3)
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        # Sawtooth wave approximation for raspy motor
        s = 0.5 * math.sin(phase) + 0.3 * math.sin(2*phase) + 0.2 * math.sin(3*phase) + 0.15 * math.sin(4*phase)
        env = math.sin(math.pi * t) ** 0.5
        samples.append(s * env * 0.8)
    return samples

def gen_bus():
    # Bus deep air horn: "Honnnk-honk!"
    samples = []
    durations = [0.4, 0.5]
    for d in durations:
        n = int(SAMPLE_RATE * d)
        for i in range(n):
            t = i / n
            s = 0.5 * math.sin(2.0 * math.pi * 311.0 * i / SAMPLE_RATE) + 0.45 * math.sin(2.0 * math.pi * 370.0 * i / SAMPLE_RATE) + 0.25 * math.sin(2.0 * math.pi * 466.0 * i / SAMPLE_RATE)
            samples.append(s * math.sin(math.pi * t) * 0.85)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.1))
    return samples

def gen_train():
    # Train whistle "Choo Choo!"
    samples = []
    for _ in range(2):
        dur = 0.5
        n = int(SAMPLE_RATE * dur)
        for i in range(n):
            t = i / n
            s = 0.4 * math.sin(2.0 * math.pi * 494.0 * i / SAMPLE_RATE) + 0.4 * math.sin(2.0 * math.pi * 622.0 * i / SAMPLE_RATE) + 0.3 * math.sin(2.0 * math.pi * 740.0 * i / SAMPLE_RATE)
            samples.append(s * (math.sin(math.pi * t) ** 0.5) * 0.8)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.12))
    return samples

def gen_airplane():
    # Jet engine whoosh crescendo
    dur = 1.4
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / n
        noise = (((i * 214013 + 2531011) >> 16) & 0x7fff) / 16384.0 - 1.0
        pitch = 300.0 + 500.0 * t
        tone = math.sin(2.0 * math.pi * pitch * i / SAMPLE_RATE)
        s = 0.3 * tone + 0.5 * noise
        env = math.sin(math.pi * t) ** 0.8
        samples.append(s * env * 0.8)
    return samples

def gen_helicopter():
    # Rotor chop: "Chop chop chop chop chop"
    dur = 1.5
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / n
        pulse = (math.sin(2.0 * math.pi * 13.0 * t) ** 4)
        noise = (((i * 16807) % 2147483647) / 1073741824.0) - 1.0
        bass = math.sin(2.0 * math.pi * 55.0 * i / SAMPLE_RATE)
        s = (0.5 * bass + 0.4 * noise) * pulse
        samples.append(s * 0.85)
    return samples

def gen_ship():
    # Deep foghorn (80Hz + 120Hz)
    dur = 1.6
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / n
        s = 0.6 * math.sin(2.0 * math.pi * 82.0 * i / SAMPLE_RATE) + 0.35 * math.sin(2.0 * math.pi * 164.0 * i / SAMPLE_RATE) + 0.2 * math.sin(2.0 * math.pi * 246.0 * i / SAMPLE_RATE)
        env = math.sin(math.pi * t) ** 0.4
        samples.append(s * env * 0.9)
    return samples

def gen_bicycle():
    # "Kring-kring! Kring-kring!"
    samples = []
    for burst in range(2):
        for ring in range(3):
            dur = 0.08
            n = int(SAMPLE_RATE * dur)
            for i in range(n):
                t = i / n
                s = 0.5 * math.sin(2.0 * math.pi * 2200.0 * i / SAMPLE_RATE) + 0.45 * math.sin(2.0 * math.pi * 2800.0 * i / SAMPLE_RATE)
                decay = math.exp(-12.0 * t)
                samples.append(s * decay * 0.75)
            samples.extend([0.0] * int(SAMPLE_RATE * 0.03))
        samples.extend([0.0] * int(SAMPLE_RATE * 0.15))
    return samples

def gen_ambulance():
    # European/ID two-tone siren: Nee-naw-nee-naw
    samples = []
    tones = [750.0, 950.0, 750.0, 950.0]
    for freq in tones:
        n = int(SAMPLE_RATE * 0.28)
        for i in range(n):
            s = math.sin(2.0 * math.pi * freq * i / SAMPLE_RATE)
            samples.append(s * 0.75)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.02))
    return samples

def gen_fire_truck():
    # Siren pitch wail (500Hz -> 1100Hz -> 500Hz)
    dur = 1.4
    n = int(SAMPLE_RATE * dur)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        f = 500.0 + 600.0 * math.sin(math.pi * t)
        phase += 2.0 * math.pi * f / SAMPLE_RATE
        s = 0.6 * math.sin(phase) + 0.3 * math.sin(3 * phase)
        samples.append(s * 0.8)
    return samples

# Alat Musik (Musical Instruments)
def gen_guitar():
    # Acoustic strum chord (C major: C3, E3, G3, C4, E4)
    freqs = [130.81, 164.81, 196.0, 261.63, 329.63]
    dur = 1.6
    n = int(SAMPLE_RATE * dur)
    samples = [0.0] * n
    for idx, f in enumerate(freqs):
        offset = int(SAMPLE_RATE * idx * 0.04) # strumming delay
        for i in range(offset, n):
            t = (i - offset) / SAMPLE_RATE
            decay = math.exp(-2.5 * t)
            # Karplus-like harmonics
            harm = math.sin(2 * math.pi * f * t) + 0.5 * math.sin(4 * math.pi * f * t) + 0.25 * math.sin(6 * math.pi * f * t)
            samples[i] += 0.2 * harm * decay
    return samples

def gen_piano():
    # Piano arpeggio: C4, E4, G4, C5 (Do-Mi-Sol-Do)
    notes = [261.63, 329.63, 392.0, 523.25]
    dur_note = 0.35
    samples = []
    for f in notes:
        n = int(SAMPLE_RATE * dur_note)
        for i in range(n):
            t = i / SAMPLE_RATE
            decay = math.exp(-3.5 * t)
            s = math.sin(2 * math.pi * f * t) + 0.4 * math.sin(4 * math.pi * f * t) + 0.2 * math.sin(6 * math.pi * f * t)
            samples.append(s * decay * 0.7)
    return samples

def gen_drum():
    # Kick -> Hihat -> Snare -> Hihat
    samples = []
    # Kick
    n = int(SAMPLE_RATE * 0.25)
    for i in range(n):
        t = i / n
        f = 120.0 * (1.0 - t * 0.7)
        s = math.sin(2 * math.pi * f * i / SAMPLE_RATE) * math.exp(-6.0 * t)
        samples.append(s * 0.9)
    # Snare
    n = int(SAMPLE_RATE * 0.3)
    for i in range(n):
        t = i / n
        noise = (((i * 48271) % 65536) / 32768.0 - 1.0)
        tone = math.sin(2 * math.pi * 180.0 * i / SAMPLE_RATE)
        s = (0.3 * tone + 0.6 * noise) * math.exp(-8.0 * t)
        samples.append(s * 0.85)
    # Second Kick
    for i in range(int(SAMPLE_RATE * 0.2)):
        t = i / (SAMPLE_RATE * 0.2)
        f = 130.0 * (1.0 - t * 0.7)
        s = math.sin(2 * math.pi * f * i / SAMPLE_RATE) * math.exp(-6.0 * t)
        samples.append(s * 0.9)
    # Second Snare Crash
    for i in range(int(SAMPLE_RATE * 0.35)):
        t = i / (SAMPLE_RATE * 0.35)
        noise = (((i * 16807) % 65536) / 32768.0 - 1.0)
        s = noise * math.exp(-5.0 * t)
        samples.append(s * 0.8)
    return samples

def gen_trumpet():
    # Brass fanfare (G4 -> C5 -> E5 -> G5)
    fanfare = [(392.0, 0.15), (523.25, 0.15), (659.25, 0.15), (783.99, 0.5)]
    samples = []
    for f, d in fanfare:
        n = int(SAMPLE_RATE * d)
        for i in range(n):
            t = i / n
            phase = 2 * math.pi * f * i / SAMPLE_RATE
            # Rich brass sawtooth-ish
            s = 0.5 * math.sin(phase) + 0.35 * math.sin(2*phase) + 0.2 * math.sin(3*phase) + 0.15 * math.sin(4*phase)
            env = math.sin(math.pi * t) ** 0.3
            samples.append(s * env * 0.8)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.03))
    return samples

def gen_violin():
    # Smooth bowed melody with warm vibrato
    notes = [440.0, 493.88, 554.37, 659.25]
    samples = []
    for f in notes:
        n = int(SAMPLE_RATE * 0.3)
        for i in range(n):
            t = i / n
            vib = 8.0 * math.sin(2 * math.pi * 6.0 * (i / SAMPLE_RATE))
            phase = 2 * math.pi * (f + vib) * i / SAMPLE_RATE
            s = 0.5 * math.sin(phase) + 0.3 * math.sin(2*phase) + 0.2 * math.sin(3*phase)
            env = math.sin(math.pi * t) ** 0.5
            samples.append(s * env * 0.75)
    return samples

def gen_xylophone():
    # Bright sparkling tinkles (C6, E6, G6, C7)
    notes = [1046.50, 1318.51, 1567.98, 2093.00]
    samples = []
    for f in notes:
        n = int(SAMPLE_RATE * 0.25)
        for i in range(n):
            t = i / SAMPLE_RATE
            decay = math.exp(-14.0 * t)
            s = math.sin(2 * math.pi * f * t) + 0.2 * math.sin(6 * math.pi * f * t)
            samples.append(s * decay * 0.8)
    return samples

def gen_flute():
    # Peaceful serene seruling tones
    notes = [523.25, 587.33, 659.25, 783.99]
    samples = []
    for f in notes:
        n = int(SAMPLE_RATE * 0.3)
        for i in range(n):
            t = i / n
            vib = 5.0 * math.sin(2 * math.pi * 5.0 * (i / SAMPLE_RATE))
            s = math.sin(2 * math.pi * (f + vib) * i / SAMPLE_RATE)
            env = math.sin(math.pi * t)
            samples.append(s * env * 0.75)
    return samples

def gen_harmonica():
    # Folk chord reed melody
    dur = 1.3
    n = int(SAMPLE_RATE * dur)
    samples = []
    for i in range(n):
        t = i / n
        trem = 0.7 + 0.3 * math.sin(2 * math.pi * 8.0 * t)
        s = 0.4 * math.sin(2*math.pi*440.0*i/SAMPLE_RATE) + 0.35 * math.sin(2*math.pi*554.37*i/SAMPLE_RATE) + 0.35 * math.sin(2*math.pi*659.25*i/SAMPLE_RATE)
        env = math.sin(math.pi * t) ** 0.5
        samples.append(s * env * trem * 0.75)
    return samples

def gen_maracas():
    # Rhythmic shaker: cha-cha-cha
    samples = []
    for _ in range(4):
        n = int(SAMPLE_RATE * 0.15)
        for i in range(n):
            t = i / n
            noise = (((i * 214013 + 2531011) >> 16) & 0x7fff) / 16384.0 - 1.0
            decay = math.exp(-12.0 * t)
            samples.append(noise * decay * 0.8)
        samples.extend([0.0] * int(SAMPLE_RATE * 0.1))
    return samples

def gen_saxophone():
    # Smooth jazzy saxophone phrase
    notes = [349.23, 392.0, 440.0, 523.25]
    samples = []
    for f in notes:
        n = int(SAMPLE_RATE * 0.32)
        for i in range(n):
            t = i / n
            vib = 6.0 * math.sin(2 * math.pi * 5.5 * (i / SAMPLE_RATE))
            phase = 2 * math.pi * (f + vib) * i / SAMPLE_RATE
            s = 0.5 * math.sin(phase) + 0.35 * math.sin(2*phase) + 0.25 * math.sin(3*phase) + 0.1 * math.sin(4*phase)
            env = math.sin(math.pi * t) ** 0.4
            samples.append(s * env * 0.8)
    return samples

sound_map = {
    # 10 Animals
    "animal_cat.wav": gen_cat,
    "animal_dog.wav": gen_dog,
    "animal_cow.wav": gen_cow,
    "animal_rooster.wav": gen_rooster,
    "animal_duck.wav": gen_duck,
    "animal_lion.wav": gen_lion,
    "animal_elephant.wav": gen_elephant,
    "animal_horse.wav": gen_horse,
    "animal_sheep.wav": gen_sheep,
    "animal_bird.wav": gen_bird,

    # 10 Vehicles
    "vehicle_car.wav": gen_car,
    "vehicle_motorcycle.wav": gen_motorcycle,
    "vehicle_bus.wav": gen_bus,
    "vehicle_train.wav": gen_train,
    "vehicle_airplane.wav": gen_airplane,
    "vehicle_helicopter.wav": gen_helicopter,
    "vehicle_ship.wav": gen_ship,
    "vehicle_bicycle.wav": gen_bicycle,
    "vehicle_ambulance.wav": gen_ambulance,
    "vehicle_fire_truck.wav": gen_fire_truck,

    # 10 Music Instruments
    "music_guitar.wav": gen_guitar,
    "music_piano.wav": gen_piano,
    "music_drum.wav": gen_drum,
    "music_trumpet.wav": gen_trumpet,
    "music_violin.wav": gen_violin,
    "music_xylophone.wav": gen_xylophone,
    "music_flute.wav": gen_flute,
    "music_harmonica.wav": gen_harmonica,
    "music_maracas.wav": gen_maracas,
    "music_saxophone.wav": gen_saxophone
}

if __name__ == "__main__":
    for fname, func in sound_map.items():
        save_wav(fname, func())
    print("All 30 audio files generated successfully!")


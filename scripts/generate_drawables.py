import os

DRAWABLE_DIR = "/Users/macbookpro/sound-play/app/src/main/res/drawable"
os.makedirs(DRAWABLE_DIR, exist_ok=True)

def wrap_vector(paths, w=120, h=120, vw=100, vh=100):
    return f"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="{w}dp"
    android:height="{h}dp"
    android:viewportWidth="{vw}"
    android:viewportHeight="{vh}">
{paths}
</vector>
"""

drawables = {}

# 1. Cat
drawables["ic_animal_cat.xml"] = wrap_vector("""
    <!-- Head -->
    <path android:fillColor="#FFA726" android:pathData="M50,22 C30,22 18,36 18,56 C18,74 32,88 50,88 C68,88 82,74 82,56 C82,36 70,22 50,22 Z" />
    <!-- Left Ear -->
    <path android:fillColor="#FB8C00" android:pathData="M24,40 L12,14 L38,26 Z" />
    <path android:fillColor="#FFCC80" android:pathData="M24,36 L16,18 L34,26 Z" />
    <!-- Right Ear -->
    <path android:fillColor="#FB8C00" android:pathData="M76,40 L88,14 L62,26 Z" />
    <path android:fillColor="#FFCC80" android:pathData="M76,36 L84,18 L66,26 Z" />
    <!-- Eyes -->
    <path android:fillColor="#2D3436" android:pathData="M36,52 A5,6 0 1,0 36,40 A5,6 0 1,0 36,52 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M38,44 A2,2 0 1,0 38,40 A2,2 0 1,0 38,44 Z" />
    <path android:fillColor="#2D3436" android:pathData="M64,52 A5,6 0 1,0 64,40 A5,6 0 1,0 64,52 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M66,44 A2,2 0 1,0 66,40 A2,2 0 1,0 66,44 Z" />
    <!-- Pink Nose -->
    <path android:fillColor="#E91E63" android:pathData="M46,58 L54,58 L50,63 Z" />
    <!-- Smiling Mouth -->
    <path android:fillColor="#00000000" android:strokeColor="#5D4037" android:strokeWidth="2.5" android:strokeLineCap="round"
          android:pathData="M44,65 Q50,71 50,63 Q50,71 56,65" />
    <!-- Whiskers -->
    <path android:fillColor="#00000000" android:strokeColor="#FFE0B2" android:strokeWidth="2.5" android:strokeLineCap="round"
          android:pathData="M16,56 L30,58 M16,64 L30,62 M84,56 L70,58 M84,64 L70,62" />
""")

# 2. Dog
drawables["ic_animal_dog.xml"] = wrap_vector("""
    <!-- Head -->
    <path android:fillColor="#8D6E63" android:pathData="M50,22 C32,22 22,36 22,55 C22,74 34,88 50,88 C66,88 78,74 78,55 C78,36 68,22 50,22 Z" />
    <!-- Left Floppy Ear -->
    <path android:fillColor="#5D4037" android:pathData="M24,32 C14,32 10,48 12,64 C14,72 20,74 24,68 C28,62 26,44 26,32 Z" />
    <!-- Right Floppy Ear -->
    <path android:fillColor="#5D4037" android:pathData="M76,32 C86,32 90,48 88,64 C86,72 80,74 76,68 C72,62 74,44 74,32 Z" />
    <!-- Snout background -->
    <path android:fillColor="#D7CCC8" android:pathData="M50,52 C40,52 34,60 34,68 C34,78 42,82 50,82 C58,82 66,78 66,68 C66,60 60,52 50,52 Z" />
    <!-- Eyes -->
    <path android:fillColor="#2D3436" android:pathData="M38,44 A4.5,5 0 1,0 38,34 A4.5,5 0 1,0 38,44 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M39.5,38 A1.5,1.5 0 1,0 39.5,35 A1.5,1.5 0 1,0 39.5,38 Z" />
    <path android:fillColor="#2D3436" android:pathData="M62,44 A4.5,5 0 1,0 62,34 A4.5,5 0 1,0 62,44 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M63.5,38 A1.5,1.5 0 1,0 63.5,35 A1.5,1.5 0 1,0 63.5,38 Z" />
    <!-- Nose -->
    <path android:fillColor="#2D3436" android:pathData="M44,60 C44,56 56,56 56,60 C56,64 50,67 50,67 C50,67 44,64 44,60 Z" />
    <!-- Tongue -->
    <path android:fillColor="#FF5252" android:pathData="M47,72 C47,78 53,78 53,72 Z" />
""")

# 3. Cow
drawables["ic_animal_cow.xml"] = wrap_vector("""
    <!-- Head -->
    <path android:fillColor="#ECEFF1" android:pathData="M50,18 C32,18 24,30 24,52 C24,72 34,84 50,84 C66,84 76,72 76,52 C76,30 68,18 50,18 Z" />
    <!-- Black Spots -->
    <path android:fillColor="#37474F" android:pathData="M24,36 C24,46 36,42 34,30 C32,24 24,28 24,36 Z" />
    <path android:fillColor="#37474F" android:pathData="M70,48 C64,48 62,58 72,62 C76,58 76,52 70,48 Z" />
    <!-- Horns -->
    <path android:fillColor="#FFE082" android:pathData="M28,24 Q18,12 26,10 Q32,16 34,22 Z" />
    <path android:fillColor="#FFE082" android:pathData="M72,24 Q82,12 74,10 Q68,16 66,22 Z" />
    <!-- Big Pink Snout -->
    <path android:fillColor="#F8BBD0" android:pathData="M50,54 C34,54 30,64 30,72 C30,82 40,86 50,86 C60,86 70,82 70,72 C70,64 66,54 50,54 Z" />
    <path android:fillColor="#880E4F" android:pathData="M42,72 A3,3 0 1,0 42,66 A3,3 0 1,0 42,72 Z" />
    <path android:fillColor="#880E4F" android:pathData="M58,72 A3,3 0 1,0 58,66 A3,3 0 1,0 58,72 Z" />
    <!-- Eyes -->
    <path android:fillColor="#263238" android:pathData="M38,42 A4,4 0 1,0 38,34 A4,4 0 1,0 38,42 Z" />
    <path android:fillColor="#263238" android:pathData="M62,42 A4,4 0 1,0 62,34 A4,4 0 1,0 62,42 Z" />
""")

# 4. Rooster
drawables["ic_animal_rooster.xml"] = wrap_vector("""
    <!-- Body -->
    <path android:fillColor="#FFF9C4" android:pathData="M50,30 C30,30 22,46 22,66 C22,82 34,92 50,92 C66,92 78,82 78,66 C78,46 70,30 50,30 Z" />
    <!-- Red Comb -->
    <path android:fillColor="#F44336" android:pathData="M40,24 C36,14 44,12 46,20 C50,10 56,12 56,20 C60,14 66,16 64,24 Z" />
    <!-- Red Wattle -->
    <path android:fillColor="#F44336" android:pathData="M46,68 C42,76 50,80 52,72 Z" />
    <!-- Orange Beak -->
    <path android:fillColor="#FF9800" android:pathData="M42,54 L58,54 L50,66 Z" />
    <!-- Eyes -->
    <path android:fillColor="#212121" android:pathData="M36,46 A4,4 0 1,0 36,38 A4,4 0 1,0 36,46 Z" />
    <path android:fillColor="#212121" android:pathData="M64,46 A4,4 0 1,0 64,38 A4,4 0 1,0 64,46 Z" />
    <!-- Wings -->
    <path android:fillColor="#FFF176" android:pathData="M18,60 C14,70 20,80 26,76 C24,68 20,62 18,60 Z" />
    <path android:fillColor="#FFF176" android:pathData="M82,60 C86,70 80,80 74,76 C76,68 80,62 82,60 Z" />
""")

# 5. Duck
drawables["ic_animal_duck.xml"] = wrap_vector("""
    <!-- Body and Head -->
    <path android:fillColor="#FFEE58" android:pathData="M50,20 C34,20 28,32 28,46 C28,58 34,64 34,70 C34,84 42,90 58,90 C74,90 82,82 82,70 C82,54 72,46 72,38 C72,26 64,20 50,20 Z" />
    <!-- Big Orange Bill -->
    <path android:fillColor="#FB8C00" android:pathData="M24,44 C12,44 14,54 26,56 C34,58 40,54 38,46 Z" />
    <!-- Eye -->
    <path android:fillColor="#263238" android:pathData="M44,36 A4,4 0 1,0 44,28 A4,4 0 1,0 44,36 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M45,31 A1.5,1.5 0 1,0 45,28 A1.5,1.5 0 1,0 45,31 Z" />
    <!-- Wing -->
    <path android:fillColor="#FDD835" android:pathData="M50,62 C42,62 40,74 52,78 C64,82 72,74 68,66 C64,62 56,62 50,62 Z" />
""")

# 6. Lion
drawables["ic_animal_lion.xml"] = wrap_vector("""
    <!-- Big Fluffy Mane -->
    <path android:fillColor="#E65100" android:pathData="M50,8 C24,8 10,24 10,50 C10,76 24,92 50,92 C76,92 90,76 90,50 C90,24 76,8 50,8 Z" />
    <!-- Lion Face -->
    <path android:fillColor="#FFB74D" android:pathData="M50,22 C34,22 26,34 26,52 C26,70 34,80 50,80 C66,80 74,70 74,52 C74,34 66,22 50,22 Z" />
    <!-- Ears -->
    <path android:fillColor="#FF9800" android:pathData="M26,26 A8,8 0 1,0 26,10 A8,8 0 1,0 26,26 Z" />
    <path android:fillColor="#FF9800" android:pathData="M74,26 A8,8 0 1,0 74,10 A8,8 0 1,0 74,26 Z" />
    <!-- Snout & Nose -->
    <path android:fillColor="#FFE0B2" android:pathData="M50,56 C42,56 38,62 38,68 C38,76 44,78 50,78 C56,78 62,76 62,68 C62,62 58,56 50,56 Z" />
    <path android:fillColor="#4E342E" android:pathData="M46,58 L54,58 L50,64 Z" />
    <!-- Eyes -->
    <path android:fillColor="#212121" android:pathData="M38,44 A4,4 0 1,0 38,36 A4,4 0 1,0 38,44 Z" />
    <path android:fillColor="#212121" android:pathData="M62,44 A4,4 0 1,0 62,36 A4,4 0 1,0 62,44 Z" />
""")

# 7. Elephant
drawables["ic_animal_elephant.xml"] = wrap_vector("""
    <!-- Left Big Ear -->
    <path android:fillColor="#90A4AE" android:pathData="M28,24 C10,24 8,56 22,66 C28,70 34,60 34,48 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M26,30 C16,30 14,52 24,60 C26,54 28,44 28,30 Z" />
    <!-- Right Big Ear -->
    <path android:fillColor="#90A4AE" android:pathData="M72,24 C90,24 92,56 78,66 C72,70 66,60 66,48 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M74,30 C84,30 86,52 76,60 C74,54 72,44 72,30 Z" />
    <!-- Head & Trunk -->
    <path android:fillColor="#B0BEC5" android:pathData="M50,22 C36,22 30,34 30,52 C30,68 38,74 44,74 C44,82 46,90 54,90 C60,90 60,82 56,76 C54,72 54,64 58,60 C64,60 70,54 70,52 C70,34 64,22 50,22 Z" />
    <!-- Eyes -->
    <path android:fillColor="#263238" android:pathData="M40,44 A3.5,4 0 1,0 40,36 A3.5,4 0 1,0 40,44 Z" />
    <path android:fillColor="#263238" android:pathData="M60,44 A3.5,4 0 1,0 60,36 A3.5,4 0 1,0 60,44 Z" />
""")

# 8. Horse
drawables["ic_animal_horse.xml"] = wrap_vector("""
    <!-- Head & Neck -->
    <path android:fillColor="#A1887F" android:pathData="M40,16 L32,32 L26,56 C24,68 30,76 42,76 L62,76 C64,64 68,52 72,40 L62,16 Z" />
    <!-- Snout -->
    <path android:fillColor="#8D6E63" android:pathData="M26,58 C24,68 30,78 44,78 L54,78 C52,66 48,58 40,58 Z" />
    <!-- Ears -->
    <path android:fillColor="#8D6E63" android:pathData="M38,18 L34,6 L44,14 Z" />
    <path android:fillColor="#8D6E63" android:pathData="M60,18 L66,6 L56,14 Z" />
    <!-- Mane -->
    <path android:fillColor="#4E342E" android:pathData="M62,14 C66,24 74,32 76,50 L68,52 C64,36 58,26 56,14 Z" />
    <!-- Eye -->
    <path android:fillColor="#212121" android:pathData="M44,40 A4,4 0 1,0 44,32 A4,4 0 1,0 44,40 Z" />
""")

# 9. Sheep
drawables["ic_animal_sheep.xml"] = wrap_vector("""
    <!-- Fluffy Wool Cloud Body -->
    <path android:fillColor="#ECEFF1" android:pathData="M50,14 C36,14 26,22 22,34 C12,38 10,54 18,66 C14,78 28,90 40,86 C48,92 62,90 68,84 C80,84 88,72 84,60 C92,48 86,34 76,30 C72,18 60,14 50,14 Z" />
    <!-- Dark Cute Face -->
    <path android:fillColor="#455A64" android:pathData="M50,38 C38,38 32,46 32,58 C32,70 40,78 50,78 C60,78 68,70 68,58 C68,46 62,38 50,38 Z" />
    <!-- Ears -->
    <path android:fillColor="#37474F" android:pathData="M32,44 C22,44 18,52 24,56 C28,58 32,54 32,44 Z" />
    <path android:fillColor="#37474F" android:pathData="M68,44 C78,44 82,52 76,56 C72,58 68,54 68,44 Z" />
    <!-- Eyes -->
    <path android:fillColor="#FFFFFF" android:pathData="M42,54 A3,3 0 1,0 42,48 A3,3 0 1,0 42,54 Z" />
    <path android:fillColor="#212121" android:pathData="M42,52 A1.5,1.5 0 1,0 42,49 A1.5,1.5 0 1,0 42,52 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M58,54 A3,3 0 1,0 58,48 A3,3 0 1,0 58,54 Z" />
    <path android:fillColor="#212121" android:pathData="M58,52 A1.5,1.5 0 1,0 58,49 A1.5,1.5 0 1,0 58,52 Z" />
""")

# 10. Bird
drawables["ic_animal_bird.xml"] = wrap_vector("""
    <!-- Body -->
    <path android:fillColor="#42A5F5" android:pathData="M46,26 C30,26 22,40 22,56 C22,74 34,86 50,86 C64,86 74,78 86,88 L82,68 C86,60 84,48 76,38 C68,28 58,26 46,26 Z" />
    <!-- Belly -->
    <path android:fillColor="#90CAF9" android:pathData="M36,54 C36,70 44,82 56,82 C44,82 36,72 36,54 Z" />
    <!-- Beak -->
    <path android:fillColor="#FFA726" android:pathData="M24,46 L10,50 L24,56 Z" />
    <!-- Eye -->
    <path android:fillColor="#212121" android:pathData="M38,42 A4,4 0 1,0 38,34 A4,4 0 1,0 38,42 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M39,37 A1.5,1.5 0 1,0 39,34 A1.5,1.5 0 1,0 39,37 Z" />
    <!-- Wing -->
    <path android:fillColor="#1E88E5" android:pathData="M52,50 C44,50 42,66 58,70 C68,72 72,60 68,54 C64,50 58,50 52,50 Z" />
""")

# 11. Car
drawables["ic_vehicle_car.xml"] = wrap_vector("""
    <!-- Car Body -->
    <path android:fillColor="#E53935" android:pathData="M14,56 L24,36 C26,32 30,30 36,30 L64,30 C70,30 74,32 76,36 L86,56 L90,62 C92,66 88,72 82,72 L18,72 C12,72 8,66 10,62 Z" />
    <!-- Roof Windows -->
    <path android:fillColor="#B3E5FC" android:pathData="M36,34 L48,34 L48,52 L26,52 L34,36 C34.5,35 35,34 36,34 Z" />
    <path android:fillColor="#B3E5FC" android:pathData="M52,34 L64,34 C65,34 65.5,35 66,36 L74,52 L52,52 Z" />
    <!-- Headlight -->
    <path android:fillColor="#FFEE58" android:pathData="M12,58 A4,4 0 1,0 12,50 A4,4 0 1,0 12,58 Z" />
    <path android:fillColor="#FFCA28" android:pathData="M88,58 A4,4 0 1,0 88,50 A4,4 0 1,0 88,58 Z" />
    <!-- Wheels -->
    <path android:fillColor="#37474F" android:pathData="M28,82 A10,10 0 1,0 28,62 A10,10 0 1,0 28,82 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M28,76 A4,4 0 1,0 28,68 A4,4 0 1,0 28,76 Z" />
    <path android:fillColor="#37474F" android:pathData="M72,82 A10,10 0 1,0 72,62 A10,10 0 1,0 72,82 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M72,76 A4,4 0 1,0 72,68 A4,4 0 1,0 72,76 Z" />
""")

# 12. Motorcycle
drawables["ic_vehicle_motorcycle.xml"] = wrap_vector("""
    <!-- Frame & Body -->
    <path android:fillColor="#00ACC1" android:pathData="M32,46 L48,36 L66,36 L74,52 L56,58 L42,54 Z" />
    <!-- Handlebar & Headlight -->
    <path android:fillColor="#00000000" android:strokeColor="#37474F" android:strokeWidth="4" android:strokeLineCap="round"
          android:pathData="M66,36 L72,24 L64,22" />
    <path android:fillColor="#FFEE58" android:pathData="M76,32 A4,4 0 1,0 76,24 A4,4 0 1,0 76,32 Z" />
    <!-- Seat -->
    <path android:fillColor="#212121" android:pathData="M44,36 C42,34 54,34 56,36 L54,42 L42,42 Z" />
    <!-- Front Wheel -->
    <path android:fillColor="#37474F" android:pathData="M76,78 A12,12 0 1,0 76,54 A12,12 0 1,0 76,78 Z" />
    <path android:fillColor="#ECEFF1" android:pathData="M76,71 A5,5 0 1,0 76,61 A5,5 0 1,0 76,71 Z" />
    <!-- Rear Wheel -->
    <path android:fillColor="#37474F" android:pathData="M26,78 A12,12 0 1,0 26,54 A12,12 0 1,0 26,78 Z" />
    <path android:fillColor="#ECEFF1" android:pathData="M26,71 A5,5 0 1,0 26,61 A5,5 0 1,0 26,71 Z" />
""")

# 13. Bus
drawables["ic_vehicle_bus.xml"] = wrap_vector("""
    <!-- Bus Body -->
    <path android:fillColor="#FDD835" android:pathData="M16,30 C16,24 22,20 28,20 L72,20 C78,20 84,24 84,30 L84,68 C84,72 80,74 76,74 L24,74 C20,74 16,72 16,68 Z" />
    <!-- Windows -->
    <path android:fillColor="#81D4FA" android:pathData="M22,28 L38,28 L38,44 L22,44 Z" />
    <path android:fillColor="#81D4FA" android:pathData="M42,28 L58,28 L58,44 L42,44 Z" />
    <path android:fillColor="#81D4FA" android:pathData="M62,28 L78,28 L78,44 L62,44 Z" />
    <!-- Stripe -->
    <path android:fillColor="#FB8C00" android:pathData="M16,50 L84,50 L84,56 L16,56 Z" />
    <!-- Wheels -->
    <path android:fillColor="#37474F" android:pathData="M30,84 A9,9 0 1,0 30,66 A9,9 0 1,0 30,84 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M30,78 A3,3 0 1,0 30,72 A3,3 0 1,0 30,78 Z" />
    <path android:fillColor="#37474F" android:pathData="M70,84 A9,9 0 1,0 70,66 A9,9 0 1,0 70,84 Z" />
    <path android:fillColor="#CFD8DC" android:pathData="M70,78 A3,3 0 1,0 70,72 A3,3 0 1,0 70,78 Z" />
""")

# 14. Train
drawables["ic_vehicle_train.xml"] = wrap_vector("""
    <!-- Cabin -->
    <path android:fillColor="#1E88E5" android:pathData="M18,34 L40,34 L40,70 L18,70 Z" />
    <!-- Roof -->
    <path android:fillColor="#D32F2F" android:pathData="M14,30 C14,28 20,26 28,26 L42,26 L40,34 L16,34 Z" />
    <!-- Boiler -->
    <path android:fillColor="#43A047" android:pathData="M40,42 L80,42 L80,70 L40,70 Z" />
    <!-- Chimney & Steam -->
    <path android:fillColor="#FB8C00" android:pathData="M66,28 L76,28 L74,42 L68,42 Z" />
    <path android:fillColor="#ECEFF1" android:pathData="M70,18 A5,5 0 1,0 70,8 A5,5 0 1,0 70,18 Z" />
    <!-- Window -->
    <path android:fillColor="#B3E5FC" android:pathData="M24,40 L34,40 L34,54 L24,54 Z" />
    <!-- Wheels -->
    <path android:fillColor="#37474F" android:pathData="M28,82 A8,8 0 1,0 28,66 A8,8 0 1,0 28,82 Z" />
    <path android:fillColor="#37474F" android:pathData="M50,82 A8,8 0 1,0 50,66 A8,8 0 1,0 50,82 Z" />
    <path android:fillColor="#37474F" android:pathData="M72,82 A8,8 0 1,0 72,66 A8,8 0 1,0 72,82 Z" />
""")

# 15. Airplane
drawables["ic_vehicle_airplane.xml"] = wrap_vector("""
    <!-- Airplane Body -->
    <path android:fillColor="#ECEFF1" android:pathData="M88,48 C88,44 82,42 74,42 L34,44 L16,30 L10,34 L20,48 L14,50 L10,46 L6,48 L10,54 L26,54 L36,54 L74,54 C82,54 88,52 88,48 Z" />
    <!-- Wings -->
    <path android:fillColor="#1E88E5" android:pathData="M44,48 L32,20 L44,20 L62,48 Z" />
    <path android:fillColor="#1976D2" android:pathData="M44,52 L36,78 L46,78 L60,52 Z" />
    <!-- Cockpit -->
    <path android:fillColor="#0288D1" android:pathData="M74,44 L82,46 L82,48 L74,48 Z" />
    <!-- Red engines/details -->
    <path android:fillColor="#E53935" android:pathData="M10,30 L16,30 L18,36 L12,36 Z" />
""")

# 16. Helicopter
drawables["ic_vehicle_helicopter.xml"] = wrap_vector("""
    <!-- Rotor Blade -->
    <path android:fillColor="#37474F" android:pathData="M16,18 L84,18 L84,22 L16,22 Z" />
    <path android:fillColor="#78909C" android:pathData="M48,22 L52,22 L52,32 L48,32 Z" />
    <!-- Main Body Cabin -->
    <path android:fillColor="#FF7043" android:pathData="M30,32 C48,32 68,32 72,44 C76,56 68,68 48,68 C34,68 24,56 24,46 C24,38 28,32 30,32 Z" />
    <!-- Windshield -->
    <path android:fillColor="#B3E5FC" android:pathData="M56,36 C64,38 68,44 68,50 L50,50 L50,36 Z" />
    <!-- Tail Boom -->
    <path android:fillColor="#FF7043" android:pathData="M30,46 L10,40 L10,44 L30,52 Z" />
    <!-- Skids -->
    <path android:fillColor="#00000000" android:strokeColor="#37474F" android:strokeWidth="3" android:strokeLineCap="round"
          android:pathData="M34,68 L34,76 M58,68 L58,76 M24,76 L68,76" />
""")

# 17. Ship
drawables["ic_vehicle_ship.xml"] = wrap_vector("""
    <!-- Hull Boat -->
    <path android:fillColor="#C62828" android:pathData="M14,54 L86,54 L76,74 L24,74 Z" />
    <!-- Cabin Deck -->
    <path android:fillColor="#ECEFF1" android:pathData="M30,38 L68,38 L68,54 L30,54 Z" />
    <!-- Portholes Windows -->
    <path android:fillColor="#0288D1" android:pathData="M38,46 A3,3 0 1,0 38,40 A3,3 0 1,0 38,46 Z" />
    <path android:fillColor="#0288D1" android:pathData="M50,46 A3,3 0 1,0 50,40 A3,3 0 1,0 50,46 Z" />
    <path android:fillColor="#0288D1" android:pathData="M62,46 A3,3 0 1,0 62,40 A3,3 0 1,0 62,46 Z" />
    <!-- Chimney & Smoke -->
    <path android:fillColor="#FBC02D" android:pathData="M44,26 L54,26 L54,38 L44,38 Z" />
    <!-- Blue Ocean Waves -->
    <path android:fillColor="#29B6F6" android:pathData="M10,74 Q25,68 40,74 Q55,80 70,74 Q85,68 95,74 L95,84 L10,84 Z" />
""")

# 18. Bicycle
drawables["ic_vehicle_bicycle.xml"] = wrap_vector("""
    <!-- Left Wheel -->
    <path android:fillColor="#00000000" android:strokeColor="#37474F" android:strokeWidth="4"
          android:pathData="M24,76 A14,14 0 1,0 24,48 A14,14 0 1,0 24,76 Z" />
    <!-- Right Wheel -->
    <path android:fillColor="#00000000" android:strokeColor="#37474F" android:strokeWidth="4"
          android:pathData="M76,76 A14,14 0 1,0 76,48 A14,14 0 1,0 76,76 Z" />
    <!-- Colorful Bike Frame -->
    <path android:fillColor="#00000000" android:strokeColor="#8E24AA" android:strokeWidth="4" android:strokeLineJoin="round"
          android:pathData="M24,62 L46,62 L64,40 L76,62 M46,62 L54,40 L38,40 M54,40 L70,30 L66,24" />
    <!-- Seat -->
    <path android:fillColor="#212121" android:pathData="M34,38 L46,38 L42,42 L34,40 Z" />
""")

# 19. Ambulance
drawables["ic_vehicle_ambulance.xml"] = wrap_vector("""
    <!-- Ambulance White Body -->
    <path android:fillColor="#ECEFF1" android:pathData="M14,64 L14,36 C14,32 18,28 22,28 L66,28 L82,44 L86,64 Z" />
    <!-- Windshield -->
    <path android:fillColor="#81D4FA" android:pathData="M64,34 L76,46 L64,46 Z" />
    <!-- Red Cross -->
    <path android:fillColor="#E53935" android:pathData="M34,42 L42,42 L42,34 L48,34 L48,42 L56,42 L56,48 L48,48 L48,56 L42,56 L42,48 L34,48 Z" />
    <!-- Siren Light -->
    <path android:fillColor="#1E88E5" android:pathData="M40,24 L48,24 L48,28 L40,28 Z" />
    <!-- Wheels -->
    <path android:fillColor="#37474F" android:pathData="M28,78 A9,9 0 1,0 28,60 A9,9 0 1,0 28,78 Z" />
    <path android:fillColor="#37474F" android:pathData="M72,78 A9,9 0 1,0 72,60 A9,9 0 1,0 72,78 Z" />
""")

# 20. Fire Truck
drawables["ic_vehicle_fire_truck.xml"] = wrap_vector("""
    <!-- Red Body -->
    <path android:fillColor="#D32F2F" android:pathData="M14,66 L14,38 L64,38 L78,48 L86,52 L86,66 Z" />
    <!-- Ladder -->
    <path android:fillColor="#00000000" android:strokeColor="#B0BEC5" android:strokeWidth="2.5"
          android:pathData="M20,28 L60,28 M20,34 L60,34 M28,28 L28,34 M38,28 L38,34 M48,28 L48,34 M58,28 L58,34" />
    <!-- Windshield -->
    <path android:fillColor="#81D4FA" android:pathData="M64,42 L76,50 L64,50 Z" />
    <!-- Siren Light -->
    <path android:fillColor="#00E5FF" android:pathData="M66,32 L72,32 L72,38 L66,38 Z" />
    <!-- Wheels -->
    <path android:fillColor="#212121" android:pathData="M28,80 A9,9 0 1,0 28,62 A9,9 0 1,0 28,80 Z" />
    <path android:fillColor="#212121" android:pathData="M72,80 A9,9 0 1,0 72,62 A9,9 0 1,0 72,80 Z" />
""")

# 21. Guitar
drawables["ic_music_guitar.xml"] = wrap_vector("""
    <!-- Guitar Body -->
    <path android:fillColor="#D84315" android:pathData="M32,54 C24,58 24,74 34,82 C44,90 58,88 64,78 C70,70 66,60 56,58 C52,56 50,50 56,44 C62,38 58,30 50,30 C40,30 38,42 42,46 C46,50 40,52 32,54 Z" />
    <!-- Sound hole -->
    <path android:fillColor="#212121" android:pathData="M48,64 A6,6 0 1,0 48,52 A6,6 0 1,0 48,64 Z" />
    <!-- Neck -->
    <path android:fillColor="#FFB74D" android:pathData="M48,34 L56,34 L78,12 L70,12 Z" />
    <!-- Headstock -->
    <path android:fillColor="#8D6E63" android:pathData="M76,14 L86,4 L80,2 L70,12 Z" />
""")

# 22. Piano
drawables["ic_music_piano.xml"] = wrap_vector("""
    <!-- Base frame -->
    <path android:fillColor="#37474F" android:pathData="M14,24 L86,24 L86,76 L14,76 Z" />
    <!-- White Keys -->
    <path android:fillColor="#FFFFFF" android:pathData="M18,34 L26,34 L26,72 L18,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M28,34 L36,34 L36,72 L28,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M38,34 L46,34 L46,72 L38,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M48,34 L56,34 L56,72 L48,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M58,34 L66,34 L66,72 L58,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M68,34 L76,34 L76,72 L68,72 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M78,34 L82,34 L82,72 L78,72 Z" />
    <!-- Black Keys -->
    <path android:fillColor="#212121" android:pathData="M24,34 L29,34 L29,56 L24,56 Z" />
    <path android:fillColor="#212121" android:pathData="M34,34 L39,34 L39,56 L34,56 Z" />
    <path android:fillColor="#212121" android:pathData="M54,34 L59,34 L59,56 L54,56 Z" />
    <path android:fillColor="#212121" android:pathData="M64,34 L69,34 L69,56 L64,56 Z" />
    <path android:fillColor="#212121" android:pathData="M74,34 L79,34 L79,56 L74,56 Z" />
""")

# 23. Drum
drawables["ic_music_drum.xml"] = wrap_vector("""
    <!-- Drum Shell -->
    <path android:fillColor="#E53935" android:pathData="M20,40 L80,40 L80,72 C80,82 20,82 20,72 Z" />
    <!-- Drum Top -->
    <path android:fillColor="#ECEFF1" android:pathData="M50,28 C70,28 80,34 80,40 C80,46 70,52 50,52 C30,52 20,46 20,40 C20,34 30,28 50,28 Z" />
    <!-- Drumsticks -->
    <path android:fillColor="#00000000" android:strokeColor="#FFA726" android:strokeWidth="3.5" android:strokeLineCap="round"
          android:pathData="M16,16 L44,36 M84,16 L56,36" />
    <!-- Shell Pattern -->
    <path android:fillColor="#00000000" android:strokeColor="#FFFFFF" android:strokeWidth="2.5"
          android:pathData="M24,46 L36,74 L48,46 L60,74 L72,46" />
""")

# 24. Trumpet
drawables["ic_music_trumpet.xml"] = wrap_vector("""
    <!-- Golden Bell & Tubing -->
    <path android:fillColor="#FFD54F" android:pathData="M84,26 C86,22 88,38 88,50 C88,62 86,78 84,74 L68,54 L14,54 L14,46 L68,46 Z" />
    <!-- Loop Tubing -->
    <path android:fillColor="#00000000" android:strokeColor="#FFC107" android:strokeWidth="3"
          android:pathData="M30,46 L30,36 L54,36 L54,46" />
    <!-- Valves -->
    <path android:fillColor="#FFA000" android:pathData="M38,30 L42,30 L42,46 L38,46 Z" />
    <path android:fillColor="#FFA000" android:pathData="M46,30 L50,30 L50,46 L46,46 Z" />
""")

# 25. Violin
drawables["ic_music_violin.xml"] = wrap_vector("""
    <!-- Violin Body -->
    <path android:fillColor="#8D6E63" android:pathData="M38,36 C34,42 42,48 40,54 C38,60 30,64 34,74 C38,82 54,84 60,74 C64,66 56,60 54,54 C52,48 60,42 56,36 C52,30 42,30 38,36 Z" />
    <!-- Neck & Scroll -->
    <path android:fillColor="#5D4037" android:pathData="M45,32 L49,32 L49,12 L45,12 Z" />
    <path android:fillColor="#3E2723" android:pathData="M44,12 A3,3 0 1,0 44,6 A3,3 0 1,0 44,12 Z" />
    <!-- Bow -->
    <path android:fillColor="#00000000" android:strokeColor="#FFA726" android:strokeWidth="2.5" android:strokeLineCap="round"
          android:pathData="M24,24 L74,78" />
""")

# 26. Xylophone
drawables["ic_music_xylophone.xml"] = wrap_vector("""
    <!-- Colorful Rainbow Bars -->
    <path android:fillColor="#E53935" android:pathData="M16,24 L24,24 L24,76 L16,76 Z" />
    <path android:fillColor="#FB8C00" android:pathData="M26,27 L34,27 L34,73 L26,73 Z" />
    <path android:fillColor="#FDD835" android:pathData="M36,30 L44,30 L44,70 L36,70 Z" />
    <path android:fillColor="#43A047" android:pathData="M46,33 L54,33 L54,67 L46,67 Z" />
    <path android:fillColor="#00ACC1" android:pathData="M56,36 L64,36 L64,64 L56,64 Z" />
    <path android:fillColor="#1E88E5" android:pathData="M66,39 L74,39 L74,61 L66,61 Z" />
    <path android:fillColor="#8E24AA" android:pathData="M76,42 L84,42 L84,58 L76,58 Z" />
    <!-- Mallet -->
    <path android:fillColor="#00000000" android:strokeColor="#795548" android:strokeWidth="2.5"
          android:pathData="M24,84 L52,50" />
    <path android:fillColor="#FF5722" android:pathData="M54,52 A4,4 0 1,0 54,44 A4,4 0 1,0 54,52 Z" />
""")

# 27. Flute
drawables["ic_music_flute.xml"] = wrap_vector("""
    <!-- Silver Tube -->
    <path android:fillColor="#CFD8DC" android:pathData="M14,46 L86,46 L86,54 L14,54 Z" />
    <path android:fillColor="#B0BEC5" android:pathData="M84,44 L88,44 L88,56 L84,56 Z" />
    <!-- Tone Holes -->
    <path android:fillColor="#37474F" android:pathData="M26,50 A2,2 0 1,0 26,46 A2,2 0 1,0 26,50 Z" />
    <path android:fillColor="#37474F" android:pathData="M36,50 A2,2 0 1,0 36,46 A2,2 0 1,0 36,50 Z" />
    <path android:fillColor="#37474F" android:pathData="M46,50 A2,2 0 1,0 46,46 A2,2 0 1,0 46,50 Z" />
    <path android:fillColor="#37474F" android:pathData="M56,50 A2,2 0 1,0 56,46 A2,2 0 1,0 56,50 Z" />
    <path android:fillColor="#37474F" android:pathData="M66,50 A2,2 0 1,0 66,46 A2,2 0 1,0 66,50 Z" />
""")

# 28. Harmonica
drawables["ic_music_harmonica.xml"] = wrap_vector("""
    <!-- Silver Body -->
    <path android:fillColor="#90A4AE" android:pathData="M16,36 C16,32 20,30 26,30 L74,30 C80,30 84,32 84,36 L84,64 C84,68 80,70 74,70 L26,70 C20,70 16,68 16,64 Z" />
    <!-- Inset Plate -->
    <path android:fillColor="#ECEFF1" android:pathData="M22,36 L78,36 L78,64 L22,64 Z" />
    <!-- Holes -->
    <path android:fillColor="#263238" android:pathData="M26,44 L32,44 L32,56 L26,56 Z" />
    <path android:fillColor="#263238" android:pathData="M36,44 L42,44 L42,56 L36,56 Z" />
    <path android:fillColor="#263238" android:pathData="M46,44 L52,44 L52,56 L46,56 Z" />
    <path android:fillColor="#263238" android:pathData="M56,44 L62,44 L62,56 L56,56 Z" />
    <path android:fillColor="#263238" android:pathData="M66,44 L72,44 L72,56 L66,56 Z" />
""")

# 29. Maracas
drawables["ic_music_maracas.xml"] = wrap_vector("""
    <!-- Left Maraca -->
    <path android:fillColor="#FF7043" android:pathData="M36,18 C26,18 20,30 28,42 C32,48 38,54 36,64 L30,82 L38,84 L44,66 C48,58 54,46 50,34 C48,22 42,18 36,18 Z" />
    <path android:fillColor="#FFEE58" android:pathData="M26,34 L48,34 L46,40 L28,40 Z" />
    <!-- Right Maraca -->
    <path android:fillColor="#42A5F5" android:pathData="M64,18 C54,18 48,30 56,42 C60,48 66,54 64,64 L58,82 L66,84 L72,66 C76,58 82,46 78,34 C76,22 70,18 64,18 Z" />
    <path android:fillColor="#FFCA28" android:pathData="M54,34 L76,34 L74,40 L56,40 Z" />
""")

# 30. Saxophone
drawables["ic_music_saxophone.xml"] = wrap_vector("""
    <!-- Saxophone Body Tube & Bell -->
    <path android:fillColor="#FFB300" android:pathData="M36,20 L44,20 L44,64 C44,78 68,82 74,70 C78,62 76,46 84,40 L68,36 C64,46 64,60 58,62 C52,64 52,56 52,48 L52,20 Z" />
    <!-- Neck -->
    <path android:fillColor="#FFA000" android:pathData="M36,20 C32,18 24,20 22,14 L18,16 C20,24 28,26 36,24 Z" />
    <!-- Keys -->
    <path android:fillColor="#FFFFFF" android:pathData="M48,32 A2,2 0 1,0 48,28 A2,2 0 1,0 48,32 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M48,40 A2,2 0 1,0 48,36 A2,2 0 1,0 48,40 Z" />
    <path android:fillColor="#FFFFFF" android:pathData="M48,48 A2,2 0 1,0 48,44 A2,2 0 1,0 48,48 Z" />
""")

if __name__ == "__main__":
    for fname, content in drawables.items():
        with open(os.path.join(DRAWABLE_DIR, fname), 'w') as f:
            f.write(content.strip() + "\n")
        print(f"Created {fname}")
    print(f"Successfully generated {len(drawables)} vector drawables!")


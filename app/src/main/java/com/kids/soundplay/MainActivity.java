package com.kids.soundplay;

import android.graphics.drawable.GradientDrawable;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    private LinearLayout tabAnimal;
    private LinearLayout tabVehicle;
    private LinearLayout tabMusic;

    private ImageView iconTabAnimal;
    private ImageView iconTabVehicle;
    private ImageView iconTabMusic;

    private TextView textTabAnimal;
    private TextView textTabVehicle;
    private TextView textTabMusic;

    private RecyclerView rvSoundItems;
    private SoundAdapter soundAdapter;
    private SoundManager soundManager;

    private SoundCategory currentCategory = SoundCategory.ANIMAL;
    private final Map<SoundCategory, List<SoundItem>> categoryData = new HashMap<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        initViews();
        initData();
        setupAudio();
        setupRecyclerView();
        setupTabs();

        selectCategory(SoundCategory.ANIMAL);
    }

    private void initViews() {
        tabAnimal = findViewById(R.id.tabAnimal);
        tabVehicle = findViewById(R.id.tabVehicle);
        tabMusic = findViewById(R.id.tabMusic);

        iconTabAnimal = findViewById(R.id.iconTabAnimal);
        iconTabVehicle = findViewById(R.id.iconTabVehicle);
        iconTabMusic = findViewById(R.id.iconTabMusic);

        textTabAnimal = findViewById(R.id.textTabAnimal);
        textTabVehicle = findViewById(R.id.textTabVehicle);
        textTabMusic = findViewById(R.id.textTabMusic);

        rvSoundItems = findViewById(R.id.rvSoundItems);
    }

    private void initData() {
        // 1. Kategori Hewan (10 Item)
        List<SoundItem> animals = new ArrayList<>();
        animals.add(new SoundItem("cat", R.string.animal_cat, R.drawable.ic_animal_cat, R.raw.animal_cat, R.color.card_bg_orange, SoundCategory.ANIMAL));
        animals.add(new SoundItem("dog", R.string.animal_dog, R.drawable.ic_animal_dog, R.raw.animal_dog, R.color.card_bg_yellow, SoundCategory.ANIMAL));
        animals.add(new SoundItem("cow", R.string.animal_cow, R.drawable.ic_animal_cow, R.raw.animal_cow, R.color.card_bg_cyan, SoundCategory.ANIMAL));
        animals.add(new SoundItem("rooster", R.string.animal_rooster, R.drawable.ic_animal_rooster, R.raw.animal_rooster, R.color.card_bg_red, SoundCategory.ANIMAL));
        animals.add(new SoundItem("duck", R.string.animal_duck, R.drawable.ic_animal_duck, R.raw.animal_duck, R.color.card_bg_yellow, SoundCategory.ANIMAL));
        animals.add(new SoundItem("lion", R.string.animal_lion, R.drawable.ic_animal_lion, R.raw.animal_lion, R.color.card_bg_orange, SoundCategory.ANIMAL));
        animals.add(new SoundItem("elephant", R.string.animal_elephant, R.drawable.ic_animal_elephant, R.raw.animal_elephant, R.color.card_bg_blue, SoundCategory.ANIMAL));
        animals.add(new SoundItem("horse", R.string.animal_horse, R.drawable.ic_animal_horse, R.raw.animal_horse, R.color.card_bg_pink, SoundCategory.ANIMAL));
        animals.add(new SoundItem("sheep", R.string.animal_sheep, R.drawable.ic_animal_sheep, R.raw.animal_sheep, R.color.card_bg_green, SoundCategory.ANIMAL));
        animals.add(new SoundItem("bird", R.string.animal_bird, R.drawable.ic_animal_bird, R.raw.animal_bird, R.color.card_bg_cyan, SoundCategory.ANIMAL));
        categoryData.put(SoundCategory.ANIMAL, animals);

        // 2. Kategori Kendaraan (10 Item)
        List<SoundItem> vehicles = new ArrayList<>();
        vehicles.add(new SoundItem("car", R.string.vehicle_car, R.drawable.ic_vehicle_car, R.raw.vehicle_car, R.color.card_bg_red, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("motorcycle", R.string.vehicle_motorcycle, R.drawable.ic_vehicle_motorcycle, R.raw.vehicle_motorcycle, R.color.card_bg_cyan, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("bus", R.string.vehicle_bus, R.drawable.ic_vehicle_bus, R.raw.vehicle_bus, R.color.card_bg_yellow, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("train", R.string.vehicle_train, R.drawable.ic_vehicle_train, R.raw.vehicle_train, R.color.card_bg_green, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("airplane", R.string.vehicle_airplane, R.drawable.ic_vehicle_airplane, R.raw.vehicle_airplane, R.color.card_bg_blue, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("helicopter", R.string.vehicle_helicopter, R.drawable.ic_vehicle_helicopter, R.raw.vehicle_helicopter, R.color.card_bg_orange, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("ship", R.string.vehicle_ship, R.drawable.ic_vehicle_ship, R.raw.vehicle_ship, R.color.card_bg_cyan, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("bicycle", R.string.vehicle_bicycle, R.drawable.ic_vehicle_bicycle, R.raw.vehicle_bicycle, R.color.card_bg_purple, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("ambulance", R.string.vehicle_ambulance, R.drawable.ic_vehicle_ambulance, R.raw.vehicle_ambulance, R.color.card_bg_pink, SoundCategory.VEHICLE));
        vehicles.add(new SoundItem("fire_truck", R.string.vehicle_fire_truck, R.drawable.ic_vehicle_fire_truck, R.raw.vehicle_fire_truck, R.color.card_bg_red, SoundCategory.VEHICLE));
        categoryData.put(SoundCategory.VEHICLE, vehicles);

        // 3. Kategori Alat Musik (10 Item)
        List<SoundItem> music = new ArrayList<>();
        music.add(new SoundItem("guitar", R.string.music_guitar, R.drawable.ic_music_guitar, R.raw.music_guitar, R.color.card_bg_orange, SoundCategory.MUSIC));
        music.add(new SoundItem("piano", R.string.music_piano, R.drawable.ic_music_piano, R.raw.music_piano, R.color.card_bg_blue, SoundCategory.MUSIC));
        music.add(new SoundItem("drum", R.string.music_drum, R.drawable.ic_music_drum, R.raw.music_drum, R.color.card_bg_red, SoundCategory.MUSIC));
        music.add(new SoundItem("trumpet", R.string.music_trumpet, R.drawable.ic_music_trumpet, R.raw.music_trumpet, R.color.card_bg_yellow, SoundCategory.MUSIC));
        music.add(new SoundItem("violin", R.string.music_violin, R.drawable.ic_music_violin, R.raw.music_violin, R.color.card_bg_purple, SoundCategory.MUSIC));
        music.add(new SoundItem("xylophone", R.string.music_xylophone, R.drawable.ic_music_xylophone, R.raw.music_xylophone, R.color.card_bg_cyan, SoundCategory.MUSIC));
        music.add(new SoundItem("flute", R.string.music_flute, R.drawable.ic_music_flute, R.raw.music_flute, R.color.card_bg_green, SoundCategory.MUSIC));
        music.add(new SoundItem("harmonica", R.string.music_harmonica, R.drawable.ic_music_harmonica, R.raw.music_harmonica, R.color.card_bg_blue, SoundCategory.MUSIC));
        music.add(new SoundItem("maracas", R.string.music_maracas, R.drawable.ic_music_maracas, R.raw.music_maracas, R.color.card_bg_pink, SoundCategory.MUSIC));
        music.add(new SoundItem("saxophone", R.string.music_saxophone, R.drawable.ic_music_saxophone, R.raw.music_saxophone, R.color.card_bg_yellow, SoundCategory.MUSIC));
        categoryData.put(SoundCategory.MUSIC, music);
    }

    private void setupAudio() {
        soundManager = new SoundManager(this);
        for (List<SoundItem> list : categoryData.values()) {
            soundManager.preloadSounds(list);
        }
    }

    private void setupRecyclerView() {
        GridLayoutManager layoutManager = new GridLayoutManager(this, 2);
        rvSoundItems.setLayoutManager(layoutManager);

        soundAdapter = new SoundAdapter((item, view) -> {
            soundManager.playSound(item.getSoundResId());
        });
        rvSoundItems.setAdapter(soundAdapter);
    }

    private void setupTabs() {
        tabAnimal.setOnClickListener(v -> selectCategory(SoundCategory.ANIMAL));
        tabVehicle.setOnClickListener(v -> selectCategory(SoundCategory.VEHICLE));
        tabMusic.setOnClickListener(v -> selectCategory(SoundCategory.MUSIC));
    }

    private void selectCategory(SoundCategory category) {
        this.currentCategory = category;

        updateTabStyle(tabAnimal, iconTabAnimal, textTabAnimal, category == SoundCategory.ANIMAL, SoundCategory.ANIMAL);
        updateTabStyle(tabVehicle, iconTabVehicle, textTabVehicle, category == SoundCategory.VEHICLE, SoundCategory.VEHICLE);
        updateTabStyle(tabMusic, iconTabMusic, textTabMusic, category == SoundCategory.MUSIC, SoundCategory.MUSIC);

        List<SoundItem> items = categoryData.get(category);
        if (items != null) {
            soundAdapter.setItems(items);
            rvSoundItems.scrollToPosition(0);
        }
    }

    private void updateTabStyle(LinearLayout tab, ImageView icon, TextView text, boolean isActive, SoundCategory category) {
        GradientDrawable background = new GradientDrawable();
        background.setShape(GradientDrawable.RECTANGLE);
        background.setCornerRadius(dpToPx(24));

        if (isActive) {
            int activeColor = ContextCompat.getColor(this, category.getActiveColorResId());
            background.setColor(activeColor);
            icon.setColorFilter(ContextCompat.getColor(this, R.color.white));
            text.setTextColor(ContextCompat.getColor(this, R.color.white));
        } else {
            int inactiveColor = ContextCompat.getColor(this, R.color.tab_inactive);
            background.setColor(inactiveColor);
            int inactiveTextColor = ContextCompat.getColor(this, R.color.tab_inactive_text);
            icon.setColorFilter(inactiveTextColor);
            text.setTextColor(inactiveTextColor);
        }

        tab.setBackground(background);
    }

    private int dpToPx(int dp) {
        float density = getResources().getDisplayMetrics().density;
        return Math.round(dp * density);
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (soundManager != null) {
            soundManager.stopActiveSound();
        }
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (soundManager != null) {
            soundManager.release();
        }
    }
}


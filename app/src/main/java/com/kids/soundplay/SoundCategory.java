package com.kids.soundplay;

public enum SoundCategory {
    ANIMAL(R.string.category_animal, R.drawable.ic_tab_animal, R.color.tab_animal_active, R.color.tab_animal_light),
    VEHICLE(R.string.category_vehicle, R.drawable.ic_tab_vehicle, R.color.tab_vehicle_active, R.color.tab_vehicle_light),
    MUSIC(R.string.category_music, R.drawable.ic_tab_music, R.color.tab_music_active, R.color.tab_music_light);

    private final int titleResId;
    private final int iconResId;
    private final int activeColorResId;
    private final int lightColorResId;

    SoundCategory(int titleResId, int iconResId, int activeColorResId, int lightColorResId) {
        this.titleResId = titleResId;
        this.iconResId = iconResId;
        this.activeColorResId = activeColorResId;
        this.lightColorResId = lightColorResId;
    }

    public int getTitleResId() {
        return titleResId;
    }

    public int getIconResId() {
        return iconResId;
    }

    public int getActiveColorResId() {
        return activeColorResId;
    }

    public int getLightColorResId() {
        return lightColorResId;
    }
}


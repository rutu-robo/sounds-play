package com.kids.soundplay;

public class SoundItem {
    private final String id;
    private final int nameResId;
    private final int iconResId;
    private final int soundResId;
    private final int bgColorResId;
    private final SoundCategory category;

    public SoundItem(String id, int nameResId, int iconResId, int soundResId, int bgColorResId, SoundCategory category) {
        this.id = id;
        this.nameResId = nameResId;
        this.iconResId = iconResId;
        this.soundResId = soundResId;
        this.bgColorResId = bgColorResId;
        this.category = category;
    }

    public String getId() {
        return id;
    }

    public int getNameResId() {
        return nameResId;
    }

    public int getIconResId() {
        return iconResId;
    }

    public int getSoundResId() {
        return soundResId;
    }

    public int getBgColorResId() {
        return bgColorResId;
    }

    public SoundCategory getCategory() {
        return category;
    }
}


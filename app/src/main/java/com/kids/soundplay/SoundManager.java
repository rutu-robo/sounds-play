package com.kids.soundplay;

import android.content.Context;
import android.media.AudioAttributes;
import android.media.SoundPool;
import android.util.Log;

import java.util.HashMap;
import java.util.Map;

public class SoundManager {
    private static final String TAG = "SoundManager";
    private static final int MAX_STREAMS = 5;

    private final Context context;
    private SoundPool soundPool;
    private final Map<Integer, Integer> soundMap; // rawResId -> soundPoolId
    private final Map<Integer, Boolean> loadedMap; // soundPoolId -> isLoaded
    private int activeStreamId = 0;

    public SoundManager(Context context) {
        this.context = context.getApplicationContext();
        this.soundMap = new HashMap<>();
        this.loadedMap = new HashMap<>();

        AudioAttributes audioAttributes = new AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_ASSISTANCE_SONIFICATION)
                .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
                .build();

        this.soundPool = new SoundPool.Builder()
                .setMaxStreams(MAX_STREAMS)
                .setAudioAttributes(audioAttributes)
                .build();

        this.soundPool.setOnLoadCompleteListener((pool, sampleId, status) -> {
            if (status == 0) {
                loadedMap.put(sampleId, true);
            } else {
                Log.e(TAG, "Error loading sound sample ID: " + sampleId);
            }
        });
    }

    /**
     * Preload a sound resource into SoundPool
     */
    public void preloadSound(int rawResId) {
        if (!soundMap.containsKey(rawResId)) {
            try {
                int soundId = soundPool.load(context, rawResId, 1);
                soundMap.put(rawResId, soundId);
            } catch (Exception e) {
                Log.e(TAG, "Failed to load sound resource: " + rawResId, e);
            }
        }
    }

    /**
     * Preload all sound items in the category
     */
    public void preloadSounds(Iterable<SoundItem> items) {
        for (SoundItem item : items) {
            preloadSound(item.getSoundResId());
        }
    }

    /**
     * Play a sound resource immediately. If not loaded, loads it and attempts playback.
     */
    public void playSound(int rawResId) {
        if (soundPool == null) return;

        Integer soundId = soundMap.get(rawResId);
        if (soundId == null) {
            soundId = soundPool.load(context, rawResId, 1);
            soundMap.put(rawResId, soundId);
            // It will be ready shortly via OnLoadCompleteListener
            return;
        }

        Boolean isLoaded = loadedMap.get(soundId);
        if (isLoaded != null && isLoaded) {
            activeStreamId = soundPool.play(soundId, 1.0f, 1.0f, 1, 0, 1.0f);
        } else {
            // In case listener didn't trigger yet, attempt play
            activeStreamId = soundPool.play(soundId, 1.0f, 1.0f, 1, 0, 1.0f);
        }
    }

    /**
     * Stop active playing sound
     */
    public void stopActiveSound() {
        if (soundPool != null && activeStreamId != 0) {
            soundPool.stop(activeStreamId);
            activeStreamId = 0;
        }
    }

    /**
     * Release all native sound resources
     */
    public void release() {
        if (soundPool != null) {
            soundPool.release();
            soundPool = null;
        }
        soundMap.clear();
        loadedMap.clear();
    }
}


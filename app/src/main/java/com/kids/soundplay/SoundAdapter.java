package com.kids.soundplay;

import android.animation.AnimatorSet;
import android.animation.ObjectAnimator;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.animation.OvershootInterpolator;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.core.content.ContextCompat;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.card.MaterialCardView;

import java.util.ArrayList;
import java.util.List;

public class SoundAdapter extends RecyclerView.Adapter<SoundAdapter.ViewHolder> {

    public interface OnItemClickListener {
        void onItemClick(SoundItem item, View view);
    }

    private final List<SoundItem> items = new ArrayList<>();
    private final OnItemClickListener listener;

    public SoundAdapter(OnItemClickListener listener) {
        this.listener = listener;
    }

    public void setItems(List<SoundItem> newItems) {
        items.clear();
        if (newItems != null) {
            items.addAll(newItems);
        }
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_sound_card, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        SoundItem item = items.get(position);
        Context context = holder.itemView.getContext();

        holder.tvSoundName.setText(item.getNameResId());
        holder.imgSound.setImageResource(item.getIconResId());
        
        int bgColor = ContextCompat.getColor(context, item.getBgColorResId());
        holder.cardContainer.setCardBackgroundColor(bgColor);

        View.OnClickListener clickHandler = v -> {
            animateBounce(holder.cardContainer);
            if (listener != null) {
                listener.onItemClick(item, v);
            }
        };

        holder.cardContainer.setOnClickListener(clickHandler);
        holder.btnPlay.setOnClickListener(clickHandler);
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    /**
     * Tactile bounce animation for kids tactile delight
     */
    private void animateBounce(View view) {
        ObjectAnimator scaleDownX = ObjectAnimator.ofFloat(view, "scaleX", 1f, 0.92f);
        ObjectAnimator scaleDownY = ObjectAnimator.ofFloat(view, "scaleY", 1f, 0.92f);
        scaleDownX.setDuration(100);
        scaleDownY.setDuration(100);

        ObjectAnimator scaleUpX = ObjectAnimator.ofFloat(view, "scaleX", 0.92f, 1f);
        ObjectAnimator scaleUpY = ObjectAnimator.ofFloat(view, "scaleY", 0.92f, 1f);
        scaleUpX.setDuration(220);
        scaleUpY.setDuration(220);
        scaleUpX.setInterpolator(new OvershootInterpolator(2.5f));
        scaleUpY.setInterpolator(new OvershootInterpolator(2.5f));

        AnimatorSet set = new AnimatorSet();
        set.play(scaleDownX).with(scaleDownY);
        set.play(scaleUpX).with(scaleUpY).after(scaleDownX);
        set.start();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        public final MaterialCardView cardContainer;
        public final LinearLayout layoutCardContent;
        public final ImageView imgSound;
        public final TextView tvSoundName;
        public final View btnPlay;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            cardContainer = itemView.findViewById(R.id.cardContainer);
            layoutCardContent = itemView.findViewById(R.id.layoutCardContent);
            imgSound = itemView.findViewById(R.id.imgSound);
            tvSoundName = itemView.findViewById(R.id.tvSoundName);
            btnPlay = itemView.findViewById(R.id.btnPlay);
        }
    }
}


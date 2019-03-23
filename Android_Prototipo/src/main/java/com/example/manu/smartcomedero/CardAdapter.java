package com.example.manu.smartcomedero;

import android.content.Context;
import android.graphics.Color;
import android.support.annotation.NonNull;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.util.List;

class CardAdapter extends ArrayAdapter<Card>{

    public CardAdapter(@NonNull Context context, List<Card> cards) {
        super(context, 0, cards);
    }

    public View getView(int position, View convertView, ViewGroup parent){
        View listItemView = convertView;
        if (listItemView == null) {
            listItemView = LayoutInflater.from(getContext()).inflate(
                    R.layout.item_animal, parent, false);
        }

        Card currentCard = getItem(position);


        /*
        ImageView imageView = listItemView.findViewById(R.id.image);
        if(currentCard.hasImage()){
            imageView.setVisibility(View.VISIBLE);
            imageView.setImageResource(currentCard.getImage());
        }else{
            imageView.setVisibility(View.GONE);
        }
        */

        TextView headerView = listItemView.findViewById(R.id.tx_tipo_pienso);
        String header = currentCard.getPienso();
        headerView.setText(header);

        TextView subtitleView = listItemView.findViewById(R.id.tx_tiempo_ultima);
        String subtitle = currentCard.getTiempo();
        subtitleView.setText(subtitle);

        TextView tx3View = listItemView.findViewById(R.id.tx3);
        String tx3 = currentCard.getOp();
        LinearLayout card =  listItemView.findViewById(R.id.card);
        LinearLayout extraData =  listItemView.findViewById(R.id.extra_data);

        if (tx3 != null && !tx3.isEmpty()){
            card.setBackgroundColor(getContext().getResources().getColor(R.color.alerta));
        }else{
            extraData.setVisibility(View.INVISIBLE);
        }
        tx3View.setText(tx3);


        // Return the list item view that is now showing the appropriate data
        return listItemView;
    }
}

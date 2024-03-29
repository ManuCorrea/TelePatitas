package com.example.manu.smartcomedero;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ListView;

import java.util.ArrayList;

public class Pienso extends android.support.v4.app.Fragment{

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.menu_principal, container, false);

        ArrayList<Card> cards = new ArrayList<>();
        cards.add(new Card(getString(R.string.pienso_1), getString(R.string.tiempo_1)));


        CardAdapter adapter = new CardAdapter(getActivity(), cards);

        ListView listView = rootView.findViewById(R.id.list);

        listView.setAdapter(adapter);

        return rootView;
    }
}


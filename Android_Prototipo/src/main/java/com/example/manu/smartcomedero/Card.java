package com.example.manu.smartcomedero;

class Card {
    private String mPienso;
    private String mTiempo;
    private String mOp;

    public Card(String pienso, String tiempo){
        mPienso = pienso;
        mTiempo = tiempo;
    }

    public Card(String pienso, String tiempo, String tx3){
        mPienso = pienso;
        mTiempo = tiempo;
        mOp = tx3;
    }


    public String getPienso() {
        return mPienso;
    }

    public String getTiempo() { return mTiempo; }

    public String getOp() {
        return mOp;
    }
}

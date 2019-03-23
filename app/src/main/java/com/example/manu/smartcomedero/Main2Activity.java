package com.example.manu.smartcomedero;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;


public class Main2Activity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }

    public void local(View target) {

    }

    public void cloud(View target) {
        setContentView(R.layout.login);
    }

    public void entrar(View target) {
        Intent numbersIntent = new Intent(Main2Activity.this, ActividadPrincipal.class);
        startActivity(numbersIntent);
    }

}

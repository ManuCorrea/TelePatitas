package com.example.manu.smartcomedero;

import android.content.Context;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

/**
 * Provides the appropriate {@link Fragment} for a view pager.
 */
public class FragmentAdapter extends FragmentPagerAdapter {

    private Context mContext;

    public FragmentAdapter(Context context,FragmentManager fm) {
        super(fm);
        mContext = context;
    }

    @Override
    public Fragment getItem(int position) {
        if (position == 0) {
            return new Animales();
        } else if (position == 1){
            return new Pienso();
        } else {
            return new Estadisticas();
        }
    }

    @Override
    public CharSequence getPageTitle(int position) {
        if (position == 0) {
            return mContext.getString(R.string.tab_1);
        } else if (position == 1) {
            return mContext.getString(R.string.tab_2);
        } else{
            return mContext.getString(R.string.tab_3);
        }
    }

    @Override
    public int getCount() {
        return 3;
    }
}

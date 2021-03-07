package com.ima.perfectlynormalapp;

import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.EditText;
import android.widget.TextView;
import androidx.fragment.app.Fragment;
import androidx.navigation.fragment.NavHostFragment;
import b.a.a.a.a;
import java.util.Arrays;

public class FirstFragment extends Fragment {
    @Override  // androidx.fragment.app.Fragment
    public View L(LayoutInflater arg2, ViewGroup arg3, Bundle arg4) {
        return arg2.inflate(0x7F0B002E, arg3, false);  // layout:fragment_first
    }

    @Override  // androidx.fragment.app.Fragment
    public void Z(View arg3, Bundle arg4) {
        TextView v4 = (TextView)arg3.findViewById(0x7F08010D);  // id:result
        EditText v0 = (EditText)arg3.findViewById(0x7F0800A5);  // id:flagchecker1
        arg3.findViewById(0x7F08005D).setOnClickListener(new FirstFragment.a(this, v0, v4));  // id:button_first
        v0.setOnKeyListener(new FirstFragment.b(this, v0, v4));
    }

    public void o0(EditText arg12, TextView arg13) {
        String v12_4;
        byte[] v12_3;
        String v12 = arg12.getText().toString();
        int v1 = 1;
        int v0 = v12.length() - 1;
        if(v12.length() >= 8) {
            if(v12.substring(0, 7).compareTo("WH2021{") != 0 || v12.substring(v0).compareTo("}") != 0) {
                arg13.setVisibility(0);
                arg13.setText(0x7F100024);  // string:ctf "This CTF flags starts with WH2021{ and ends with }"
                return;
            }

            String v12_1 = v12.substring(7, v0);
            String[] v2 = new String[]{"VGhpc0lzTm90VGhlRmxhZw==", "U01VV2hpdGVIYXRDaGFsbGVuZ2U=", "gjhU9MzCkbTNF54MXwReLkE=", "yeLGMCaRA8p8xA==", "azMtkQ//3JA=", "zMq9wKxBrbpj1PQ9WLADXJaGRq1gnwyWdUj+2A=="};
            byte[] v3 = new byte[]{0x8A, 107, 97, 0x7B, 26, 43, 0x91, -20};
            try {
                v12_3 = Base64.decode(v12_1, 0);
            }
            catch(Exception v12_2) {
                StringBuilder v1_1 = a.f("False, ");
                v1_1.append(v12_2.toString());
                v12_4 = v1_1.toString();
                goto label_66;
            }

            byte[] v5 = Arrays.copyOf(v12_3, v12_3.length);
            int v6;
            for(v6 = 0; v6 < v12_3.length; ++v6) {
                v5[v12_3.length - 1 - v6] = (byte)(v12_3[v6] ^ v3[v6 % 8]);
            }

            if(Base64.encodeToString(v5, 0).trim().compareTo(v2[2]) == 0) {
                Log.d("RESULT", "True");
            }
            else {
                v12_4 = "False";
            label_66:
                Log.d("RESULT", v12_4);
                v1 = 0;
            }

            if(v1 != 0) {
                arg13.setVisibility(4);
                NavHostFragment.o0(this).c(0x7F080032);  // id:action_FirstFragment_to_SecondFragment
                return;
                arg13.setVisibility(0);
                arg13.setText(0x7F100024);  // string:ctf "This CTF flags starts with WH2021{ and ends with }"
                return;
            }
        }

        arg13.setVisibility(0);
        arg13.setText(MainActivity.stringFromJNI());
    }
}
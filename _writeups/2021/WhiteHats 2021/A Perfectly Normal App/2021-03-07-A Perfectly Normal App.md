---
layout: writeup
ctf: WhiteHats CTF 2021
chal: A Perfectly Normal App (A)
category: CSIT
flag: WH2021{y0U/f0UnD/tH3/C51t/F1Ag} 
points: 495
solves: 8
---

>Two flags have been hidden in this Android Application.

>The first flag is hidden somewhere in the Java code, and requires the reversal of a simple ciphering function.

>The second flag requires an understanding of the JNI calls involved and the native code called in order to decrypt the hidden flag.

Files given:
 - [com.ima.perfectlynormalapp.apk](com.ima.perfectlynormalapp.apk)

```sh
> strings com.ima.perfectlynormalapp.apk | grep flag
The second flag is encrypted and hidden in a database somewhere, can you find it?
The creators of this app have hidden two secret flags for the CTF challenge. You can verify the flags in the textbox below if you can find them!
22This CTF flags starts with WH2021{ and ends with }
''Verify your first flag by entering here
((Verify your second flag by entering here
h1ntS/f0R/tHe/f!r5t/Cha1LeNg3 : The flags are hidden among the strings! Reverse engineer the apk by decompiling the apk using JEB / JADX to see which one is the flag and how it can be readable!
flagchecker1
flagchecker2
fake_flag_1
```

We see the hint suggests JADX or JEB and the apk name tells us the directory to look in. However, JADX seems to fail to decompile the file. For some reason, we only realized that we could try JEB 24 minutes before the CTF ended. Realizing that we could actually solve this challenge, everyone started rusing to download JEB pro as JEB _without pro_ has no disassembly. After 11 minutes of hoping for fast wifi connection, we obtain the file [FirstFragment.java](FirstFragment.java) which contains some simple cipher (code cleaned up):

```java
for(i = 0; i < input.length; ++i) {
    cipher[input.length - 1 - i] = (byte)(input[i] ^ key[i % 8]);
}

if(Base64.encodeToString(cipher, 0).trim().compareTo(result) == 0) {
    Log.d("RESULT", "True");
}
```

This essentially XORs a fixed key with our input, reverses it and then base64 encodes it. These are all extremely easy to undo hence we can easily get the flag, 6 minutes before the CTF ended, securing first place.

The script to get the flag can be found at [solve.py](solve.py)

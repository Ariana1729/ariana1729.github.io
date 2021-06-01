---
layout: writeup
ctf: CTFSG CTF 2021
chal: Haachama Cooking
category: re
flag: CTFSG{t0d@y_1_1E@rnT_hum@ns_c@nt_multit@sk_BUT_c0mput3rs_c@n_d0}
points: 989
solves: 5
---

> Welcome to Haachama cooking! Today's I'm going to make my very own blend of AES! A little sprinkle of concurrency... Or was it parallism? Whatever, either one will work, this should still taste better than the tarantula ramen I had last time anyway.

Files given:
 - [haachama-cooking](haachama-cooking)

We see that this is a golang binary. Typically the main functions for such binary is located at `main.main` and appears at the bottom few functions in for instance IDA.

Using IDA to disassemble the main function, we see some encryption:

```c
for ( i = 0; i < 4; i = v4 )
  {
    ...
    runtime_stringtoslicebyte(0, *v2 + (((signed int)(v7 - v5) >> 31) & v7), v5 - v7, v29, v31, v32);
    main_encryptPart(
      v35,
      v8,
      v9,
      v10,
      main_key,     //mysupersecurekey
      dword_81856B4,
      dword_81856B8,
      main_iv,      //mysupersecureiv\x00
      dword_81856A4,
      dword_81856A8,
      v34);
    ...
  }
```

seeing at AES is included in the massive list of functions, one easily guess that this performs AES encryption with the same key and iv for each chunk.

We soon see a hexencode function and a comparison between some variables and some constant:

```c
runtime_slicebytetostring(0, v16, v14, v18, v19);
...
if ( v22 == 128 && (runtime_memequal(&unk_80FFFE8, v36, 128, v30), v26) )
```

hence we can try running AES decrypt on each block of `unk_80FFFE8`, trying out different modes. This immediately gives us the flag.

The solution script can be found at [solve.py](solve.py)

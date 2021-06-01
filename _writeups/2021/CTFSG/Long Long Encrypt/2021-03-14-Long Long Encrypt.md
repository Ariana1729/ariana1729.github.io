---
layout: writeup
ctf: CTFSG CTF 2021
chal: Long Long Encrypt
category: crypto
flag: CTFSG{mY_fEll0W_s1Ngap0r3aNs}
points: 980
solves: 10
---

> My encryption algorithm can encrypt paragraphs of text!

Files given:
 - [encrypt.py](encrypt.py)
 - [txt.enc](txt.enc)

This is a normal RSA implementation. Although \\(n\\) looks big, we can easily factor it as \\(p^e\\). With \\(\phi\left(p^e\right)=(p-1)p^{e-1}\\), we can easily decrypt the message.

The solution script can be found at [solve.sage](solve.sage)

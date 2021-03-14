---
layout: writeup
ctf: CTFSG CTF 2021
chal: Live From Serangoon Road
category: crypto
flag: CTFSG{C0rRel4t10N_AtT4cK$_0n_LsFR_101}
points: 989
solves: 5
---

> Damnit, this telco is down again. It's fine, we know exactly how they encrypted the message, maybe you might be able to help us decode it?

Files given:
 - [decrypted.txt](decrypted.txt)
 - [encrypt.py](encrypt.py)
 - [encrypted.enc](encrypted.enc)

The challenge here is that we have 4 lfsr, and a very funny way to combine them. As we are given the first 9 characters, we have the first 72 outputs of the combined stream cipher.

Initially I thought of running [correlation attacks](https://en.wikipedia.org/wiki/Correlation_attack), but this would be extremely troublesome. Eventually I recalled that there was a similar challenge - [zer0lfsr](https://ctftime.org/task/7894), so I used the lfsr implementation as that worked with z3 and modified a little, and got z3 to work and it immeidately gave the solution (after remembering to remove newline in the plaintext).

The solution script can be found at [solve.py](solve.py)

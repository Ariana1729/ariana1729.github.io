---
layout: writeup
ctf: Crypto CTF 2019
chal: Time Capsule
flag: CCTF{_______________________________________________Happy_Birthday_LCS______________________________________________}
points: 122
category: crypto
---

> You neither need 35 years nor even 20 years to solve this problem!

## Challenge

The goal is basically to compute \\(l=2^{2^t}\pmod n\\).

Note that \\(2^x\equiv2^{x\pmod{\phi(n)}}\pmod n\\)

\\(n\\) is easily factored with yafu, and the calculation is trivial from there


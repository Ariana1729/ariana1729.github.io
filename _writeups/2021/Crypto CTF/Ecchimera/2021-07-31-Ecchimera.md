---
layout: writeup
ctf: Crypto CTF 2021
chal: Ecchimera
category: crypto
flag: CCTF{m1X3d_VeR5!0n_oF_3Cc!}
points: 271
solves: 11
---

> The mixed version is a hard version!

Files given:
 - [ecchimera.sage](ecchimera.sage)
 - [output.txt](output.txt)

```python
n = 43216667049953267964807040003094883441902922285265979216983383601881964164181
U = 18230294945466842193029464818176109628473414458693455272527849780121431872221
V = 13100009444194791894141652184719316024656527520759416974806280188465496030062
W = 5543957019331266247602346710470760261172306141315670694208966786894467019982

flag = flag.lstrip(b'CCTF{').rstrip(b'}')
s = int(flag.hex(), 16)
assert s < n

E = EllipticCurve(Zmod(n), [0, U, 0, V, W])
G = E(6907136022576092896571634972837671088049787669883537619895520267229978111036, 35183770197918519490131925119869132666355991678945374923783026655753112300226)

print(f'G = {G}')
print(f's * G = {s * G}')
```


This challenge is simply discrete log over an elliptic curve over \\(\mb Z/n\mb Z\\) where \\(n=pq\\). Since \\(\mb Z/n\mb Z=\mb F_p\times\mb F_q\\\), we can just consider the curves over \\(\mb F_p,\mb F_q\\) separately then CRT the result together. Let \\(s_\cdot=s\pmod\cdot,\cdot\in\{p,q\}\\)

Reducing mod \\(q\\), we get a trace one elliptic curve, so we can easily obtain \\(s_q\\) via the Smart attack. 

Reducing mod \\(p\\), we get a trace zero elliptic curve, meaing it is supersingular and has embedding degree \\(2\\). This allows us to use the MOV attack, which uses the tate pairing to map our points to elements in \\(\mb F_{p^2}\\). However, the order of the points, \\(p+1\\), has a very large factor:

```python
sage: factor(p+1)
2^4 * 3 * 13 * 233 * 4253 * 49555349 * 7418313402470596923151
```

However, if the flag length is not too long, it may be possible to ignore that factor completely. We know that

\\[[x\cdot q+s_q]G=sG\\]
\\[\[x\]([q]G)=sG-[s_q]G\\]

and we run pohlig hellman to solve for \\(x\\), ignoring the last prime factor. This actually does give our flag!

Solution at [solve.sage](solve.sage)

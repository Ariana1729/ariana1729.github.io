---
layout: writeup
ctf: Crypto CTF 2021
chal: Elegant Curve
category: crypto
flag: CCTF{Pl4yIn9_Wi7H_ECC_1Z_liK3_pLAiNg_wiTh_Fir3!!}
points: 217
solves: 16
---

> Playing with Fire!

Files given:
 - [elegant_curve.py](elegant_curve.py)

This challenge asks us to supply curves 
\\[C_1:y^2=x^3+ax+b\pmod p\\]
\\[C_2:y^2=x^3+cx+d\pmod q\\]
under the condition that \\(0<q-p\leq2022,0<a,b<p,0<c,d<q\\) then it asks us to solve the discrete log problem over these curves. 

As there isn't any requirement that the curve msut be nonsingular, we can simply supply a curve like \\(y^2=(x-3)^2(x-3+9)\\) where over any field \\(K\\), the group of nonsingular points has a canonical map to \\(K^*\\) given by

\\[(x,y)\mapsto\frac{y+3(x-3)}{y-3(x-3)}\\]

Hence all we need to do is choose some \\(p,q\\) such that \\(p-1,q-1\\) has small factors and the discrete log can be solved extremely quickly. Do note that we shouldn't choose the factors to be too small otherwise the order of the generator may not be the full \\(p-1,q-1\\) as well as run the solution a few times as the generators occasionally will lose a factor of \\(2\\) or \\(3\\) from the maximal order.

Solution at [solve.sage](solve.sage)

---
layout: writeup
ctf: Crypto CTF 2021
chal: Double Miff
category: crypto
flag: CCTF{D39enEr47E_ECC_4TtaCk!_iN_Huffs?}
points: 217
solves: 16
---

> A new approach, a new attack. Can you attack this curve?

Files given:
 - [output.txt](output.txt)
 - [double_miff.py](double_miff.py)

```python
def onmiff(a, b, p, G):
	x, y = G
	return (a*x*(y**2 - 1) - b*y*(x**2 - 1)) % p == 0

l = len(flag) // 2
m1, m2 = bytes_to_long(flag[:l]), bytes_to_long(flag[l:])

assert m1 < (p // 2) and m2 < (p // 2)
assert onmiff(a, b, p, P) and onmiff(a, b, p, Q)
assert P[0] == m1 and Q[0] == m2

print(f'P + Q = {addmiff(P, Q)}')
print(f'Q + Q = {addmiff(Q, Q)}')
print(f'P + P = {addmiff(P, P)}')
```

The python file uses the flag to generate points \\(P,Q\\) on the curve \\(ax(y^2-1)-by(x^2-1)=0\\) over \\(\mb F_p\\) where \\(a,b,p\\) are unknown. It then outputs the points \\(P+P,P+Q,Q+Q\\).

To compute \\(p\\), we rewrite the equations as 

\\[\begin{pmatrix}x_1\left(y_1^2-1\right)&-y_1\left(x_1^2-1\right)\\\\x_2\left(y_2^2-1\right)&-y_2\left(x_2^2-1\right)\end{pmatrix}\begin{pmatrix}a\\\\b\end{pmatrix}=0\\]

then we know that the matrix must have determinant \\(0\\) mod \\(p\\). This gives us three values that must be \\(0\\) mod \\(p\\), hence we can get a multiple of \\(p\\). By taking the largest prime factor of all the determinants, we obtain a likely value of \\(p\\).

From this value of \\(p\\), we can easily compute the values of \\(a,b\\) as well.

Since this curve is an elliptic curve, we can use sage's vast library of functions to obtain \\(P,Q\\) from \\(2P,2Q\\):

```python
QQp.<x,y,z>=PolynomialRing(QQ)
r_pol = QQ(a)*x*(y**2 - 1) - QQ(b)*y*(x**2 - 1)
h_pol = r_pol.homogenize(var=z)
phi = EllipticCurve_from_cubic(h_pol)
E = phi.codomain().change_ring(FF)
tocurve = lambda a,b:E([i.change_ring(FF).subs(x=a,y=b,z=1) for i in phi.defining_polynomials()])
fromcurve = lambda a,b: (lambda P:[i/P[-1] for i in P[:-1]])\
    ([i.change_ring(FF).subs(x=a,y=b,z=1) for i in phi.inverse().defining_polynomials()])

PQ = tocurve(*PQ)
P2 = tocurve(*P2)
Q2 = tocurve(*Q2)

print([bytes.fromhex(hex(fromcurve(*i.xy())[0])[2:]) for i in P2.division_points(2)])
print([bytes.fromhex(hex(fromcurve(*i.xy())[0])[2:]) for i in Q2.division_points(2)])
```

and this gives us the flag

Solution at [solve.sage](solve.sage)

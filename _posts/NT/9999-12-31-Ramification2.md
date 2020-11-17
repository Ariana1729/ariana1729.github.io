---
layout: blog
title: Ramification 2
---

The proofs for statements can be found in Neukirch Section 1.9.

Let \\(L/K\\) be a finite extension of number fields and \\(M\\) be the Galois closure of \\(L/K\\) and \\(G\\) be its Galois group.

Let \\(\mf p\in K\\) be a prime, \\(\mf P_L\in L\\) be a prime above \\(\mf p\\) and \\(\mf P_M\in M\\) be a prime above \\(\mf P_L\\)

```python
K.<a> = NumberField(x^3 - 3)
L.<b> = K.galois_closure()
M,phi,_ = L.subfields()[1]
for p,_ in factor(L.discriminant()):
    print(p)
    for I,_ in M.ideal(p).factor():
        print(I)
        print(phi(I).factor())
print(factor(K.disc()))
print(factor(L.disc()))
print(factor(M.disc()))
```

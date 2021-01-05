---
layout: blog
title: Unit group of quotients
---

Let \\(K\\) be a number field and \\(I\\) be an integral ideal in \\(K\\), then can we find the structure of \\(\left(\frac{\mc O_K}{I\mc O_K}\right)^\*\\) in terms of cyclic groups? 

By the chinese remainder theorem, if we have \\(I=\prod_i\mf P_i^{n_i}\\), we can decompose the quotient as
\\[\frac{\mc O_K}{I\mc O_K}\cong\bigoplus_i\frac{\mc O_K}{\mf P_i^{n_i}}\\]
Which reduces the problem of finding the structure of the unit group into when \\(I=\mf P^n\\).

A useful way to understand what \\(\frac{\mc O_K}{\mf P^n}\\) is to study the completion of \\(K\\) at \\(\mf P_i\\), given by \\(L=\hat K_{\mf P}\\). 

Suppose the residue field \\(k\\) of \\(L\\) has order \\(q=p^f\\) and let \\(e\\) be the ramification index of \\(L/\mb Q_p\\). Let \\(U^{(n)}=1+\mf P^n\\) be the \\(n\\)th unit groups and let \\(\mc O=\mc O_L\\) be the ring of integers.

As the map \\(\mc O^\*\to\left(\frac{\mc O}{\mf P^n}\right)^\*\\) has kernel \\(U^{(n)}\\), we have the isomorphism 
\\[\frac{\mc O^\*}{U^{(n)}}\cong\left(\frac{\mc O}{\mf P^n}\right)^\*\\]

By Hensel's lemma, \\(\mc O^\*\\) contains the \\(q-1\\) roots of unity, hence it contains \\(\mu_{q-1}\\). Since the map from \\(\frac{\mc O^\*}{U^{(n)}}\to k^\*\cong\mu_{q-1}\\) has kernel \\(\frac{U^{(1)}}{U^{(n)}}\\), we have the isomorphism

\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong\mu_{q-1}\oplus\frac{U^{(1)}}{U^{(n)}}\\]

Since \\(\mu_{q-1}\cong C_{q-1}\\), we only need to figure out the structure of \\(\frac{U^{(1)}}{U^{(n)}}\\).

When \\(n>\frac e{p-1}\\), we have the isomorphisms between the multiplicative group \\(U^{(n)}\\) and the additive group \\(\mf P^n\\)(Neukirch Proposition II.5.5)
\\[\log:U^{(n)}\to\mf P^n\\]
\\[\exp:\mf P^n\to U^{(n)}\\]
Note that we have \\(\mf P^n=\pi^n\mc O\\) and we have, as additive groups, \\(\mc O\cong\mb Z_p^d\\) where \\(d=ef=\left[L:\mb Q_p\right]\\), and since we have \\(\frac{\mb Z_p}{p^n\mb Z_p}\cong C_{p^n}\\) as additive groups, when \\(1>\frac e{p-1}\\), we have
\\[\frac{U^{(1)}}{U^{(n)}}\cong C_{p^{n-1}}^d\\]
giving us
\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong C_{q-1}\oplus C_{p^{n-1}}^d\\]

## Example

Specializing in the case of the Gaussian integers, we either have:

\\(p=2,e=2,f=1\\) but since \\(\frac 2{2-1}=2>1\\), the conclusion cannot be used.

\\(p\equiv1\pmod 4\\), we have \\(e=f=1\\) and the unit group is isomorphic to \\(C_{p-1}\oplus C_{p^{n-1}}=C_{p^n-p^{n-1}}\\)

\\(p\equiv3\pmod 4\\), we have \\(e=1,f=2\\) and the unit group is isomorphic to \\(C_{p^2-1}\oplus C_{p^{n-1}}\oplus C_{p^{n-1}}\\)

## Some code

```py
K.<a> = NumberField(x^3-x^2-2*x-8)
R = K.ring_of_integers()
p = 503
n = 3
P,e = K.factor(p)[1]
f = P.residue_class_degree()
d = e*f
RqI = R.quo(P^n,'b')
od = p^(n-1)*(p^e-1)  # order
k = a # some element
assert p > e+1
assert K.ideal(a) + P == K.ideal(1) # coprime
assert RqI(a)^od == RqI(1)
```



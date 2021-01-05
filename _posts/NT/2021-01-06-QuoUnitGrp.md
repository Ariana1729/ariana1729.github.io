---
layout: blog
title: Unit group of quotients [WIP]
---

Let \\(K\\) be a number field and \\(I\\) be an integral ideal in \\(K\\), then can we find the structure of \\(\left(\frac{\mc O_K}{I\mc O_K}\right)^\*\\) in terms of cyclic groups? 

By the chinese remainder theorem, if we have \\(I=\prod_i\mf P_i^{n_i}\\), we can decompose the quotient as
\\[\frac{\mc O_K}{I\mc O_K}\cong\bigoplus_i\frac{\mc O_K}{\mf P_i^{n_i}}\\]
Which reduces the problem of finding the structure of the unit group into when \\(I=\mf P^n\\).

A useful way to understand what \\(\frac{\mc O_K}{\mf P^n}\\) is to study the completion of \\(K\\) at \\(\mf P_i\\), given by \\(L=\hat K_{\mf P}\\). 

Suppose the residue field \\(k\\) of \\(L\\) has order \\(q=p^f\\) and let \\(e\\) be the ramification index of \\(L/\mb Q_p\\). Let \\(U^{(n)}=1+\mf P^n\\) be the \\(n\\)th unit groups and let \\(\mc O=\mc O_L\\) be the ring of integers and let \\(\pi\\) be a uniformizing element.

As the map \\(\mc O^\*\to\left(\frac{\mc O}{\mf P^n}\right)^\*\\) has kernel \\(U^{(n)}\\), we have the isomorphism 
\\[\frac{\mc O^\*}{U^{(n)}}\cong\left(\frac{\mc O}{\mf P^n}\right)^\*\\]

By Hensel's lemma, \\(\mc O^\*\\) contains the \\(q-1\\) roots of unity, hence it contains \\(\mu_{q-1}\\). Since the map from \\(\frac{\mc O^\*}{U^{(n)}}\to k^\*\cong\mu_{q-1}\\) has kernel \\(\frac{U^{(1)}}{U^{(n)}}\\), we have the isomorphism

\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong\mu_{q-1}\oplus\frac{U^{(1)}}{U^{(n)}}\\]

Since \\(\mu_{q-1}\cong C_{q-1}\\), we only need to figure out the structure of \\(\frac{U^{(1)}}{U^{(n)}}\\).

To work out the structure of this group, we first determine the structure of \\(U^{(1)}\\).

When \\(n>\frac e{p-1}\\), we have the isomorphisms between the multiplicative group \\(U^{(n)}\\) and the additive group \\(\mf P^n\\)(Neukirch Proposition II.5.5)
\\[\log:U^{(n)}\to\mf P^n\\]
\\[\exp:\mf P^n\to U^{(n)}\\]

Note that we have \\(\mf P^n=\pi^n\mc O\\) and we have, as additive groups, \\(\mc O\cong\mb Z_p^d\\). The only other elements that are missing comes from the \\(p^a\\)th roots of unity, thus giving us
\\[U^{(1)}=\mu_{p^a}\oplus\mb Z_p^d\\]
for some \\(a\leq\frac e{p-1}\\). Finally, this shows that we have \\(d+1\\) generators for \\(U^{(1)}\\), with one of them having order \\(p^a\\) for \\(n\geq a\\) in \\(\frac{U^{(1)}}{U^{(n)}}\\).

First we study the non-ramified case, we have \\(a=0\\) and \\((p)=(\pi)\\), hence the generators form cyclic groups of order \\(p^{n-1}\\) and the structure of the unit group is given by 

\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong C_{q-1}\oplus C_{p^{n-1}}^d\\]

In the ramified case, we have \\((p)=(\pi^e)\\). For now, lets assume that \\(a=0\\). The maximum order of each generator is \\(p^{\left\lceil\frac{n-1}e\right\rceil}\\). I claim that there must exist a generator with order \\(p^{\left\lceil\frac{n-1}e\right\rceil}\\) by counting arguments:

The local ring \\(\frac{\mc O}{\mf P^n}\\) has \\(p^{fn}\\) elements in it, and \\(p^{f(n-1)}\\) elements in the maximal ideal \\(\frac{\mf P\mc O}{\mf P^n}\\), hence it has a total of \\(p^{f(n-1)}\left(p^f-1\right)\\) elements in its unit group.

Let \\(r=e\left\lceil\frac{n-1}e\right\rceil-(n-1)\<e\\). Suppose that every generator has order \\(p^{\left\lceil\frac{n-1}e\right\rceil-1}\\), which will produce the largest unit group, then this largest group has order
\\[\left(p^f-1\right)\left(p^{\left\lceil\frac{n-1}e\right\rceil-1}\right)^d=\left(p^f-1\right)p^{f(n-1+r)-d}=p^{f(n-1)}\left(p^f-1\right)p^{rf-d}\\]

Since \\(r\<e\\), we have \\(rf-d\\) is negative, so we have less elements in this group than in the unit group of \\(\frac{\mc O}{\mf P^n}\\), which cannot be possible, hence we need at least \\(d-rf\\) of the generators to have maximal order \\(p^{\left\lceil\frac{n-1}e\right\rceil}\\). Hence we can deduce that

\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong C_{q-1}\oplus C_{p^{\left\lceil\frac{n-1}e\right\rceil}}^{d-rf}\oplus G\\]

where \\(G\\) is a group with \\(rf\\) generators of order a power of \\(p\\) but at most \\(p^{n-1}\\). Let \\(g_i\\) be the generators, by the same counting argument, we also need
\\[\prod\text{ord}\left(g_i\right)=p^{\left(\left\lceil\frac{n-1}e-1\right\rceil\right)rf}\\]

Notice that when \\(e=1\\), we have \\(r=0\\), rederiving the unramified case.

If \\(a\neq0\\), we could possibly modify the result slightly by having \\(p^{rf-d+a}\\) and as long as \\(rf-d+a<0\\), the result holds except we have 
\\[\left(\frac{\mc O}{\mf P^n}\right)^\*\cong\frac{\mc O^\*}{U^{(n)}}\cong C_{q-1}\oplus C_{p^{\left\lceil\frac{n-1}e\right\rceil}}^{d-rf+a}\oplus G\\]
where \\(G\\) has \\(rf-a\\) generators satisfying 
\\[\prod\text{ord}\left(g_i\right)=p^{\left(\left\lceil\frac{n-1}e-1\right\rceil\right)(rf-a)}\\]

## Example

Specializing in the case of the Gaussian integers, we have

 - \\(p\equiv1\pmod 4\\), we have \\(e=f=1\\) and the unit group is isomorphic to \\(C_{p-1}\oplus C_{p^{n-1}}=C_{p^n-p^{n-1}}\\)

 - \\(p\equiv3\pmod 4\\), we have \\(e=1,f=2\\) and the unit group is isomorphic to \\(C_{p^2-1}\oplus C_{p^{n-1}}\oplus C_{p^{n-1}}\\)

 - \\(p=2,e=2,f=1\\), since \\(\frac e{p-1}=2\geq1\\), \\(a\\) could be non-zero and we are not able to apply the results directly.. (turns out \\(a=2\\)?)

## Some code

```py
K.<a> = NumberField(x^4-x^3-x^2-2*x+4)
R = K.ring_of_integers()
p = 7
n = 3
for P,e in K.factor(p):
    f = P.residue_class_degree()
    d = e*f
    a = e//(p-1)
    r = (1-n)%e
    if r*f-d+a>=0:
        print("a could be non-zero, skipping this case")
        continue
    print(f"Checking the prime {P} with ramification index {e} and inertia degree {f}")
    RqI = R.quo(P^n,'b')
    od = p^(1+(n-2)//e)*(p^f-1)  # order
    for p_fac in [i for i,j in list(factor(p^f-1))]+[p]:
        not_od = ZZ(od/p_fac)
        print(f"Checkng {p_fac}")
        while True:
            k = R.random_element()
            if K.ideal(k) + P == K.ideal(1): # coprime
                assert RqI(k)^od == RqI(1):
                if RqI(k)^not_od != RqI(1):
                    print(f"{k} does not have order {not_od}")
                    break
    print(f"{od} is minimal order for R/IR")
```



---
layout: blog
title: Ramification Part 1
---

Let \\(\mc A\\) be an arbitrary Dedekind domain with field of fractions \\(K\\) and let \\(L/K\\) be a finite extension of fields. Let \\(\mc B\\) be the integral closure of \\(\mc A\\) in \\(L\\).

For any prime \\(\mf p\in\mc A\\), we let its factorization in \\(\mc B\\) be given by \\(\prod_i\mf P_i^{e_i}\\). We define \\(e_i\\) as the **ramification index** of \\(\mf P_i\\) and the degree of the field extension \\(f_i=\left[\mc B/\mf P_i:\mc A/\mf p\right]\\).

We have the following special cases for splitting behavior of primes:

| **totally split** | \\(e_i=f_i=1\\) |
| **nonsplit** | \\(r=1\\) |
| **unramified** | \\(e_i=1\\)  |
| **ramified** | \\(e_i\neq1\\) for some \\(i\\)  |
| **totally ramified** | \\(f_i=1\\) |

**Theorem 1:** If \\(L/K\\) is separable, we have the following theorem relating \\(e_i,f_i\\) and the degree of the field extension \\(n=[L:K]\\):

\\[\sum_{i=1}^re_if_i=n\\]

We can check this identity with sage:

```python
K.<a> = NumberField(x^3-x+1)
L.<b> = K.extension(x^3+x+1)
for p in flatten([[j[0] for j in K.factor(i)] for i in [2,23,31]]):
    t = p.residue_class_degree()
    P = L.ideal(p).factor()
    P = [(i.residue_class_degree()/t,j) for i,j in P]
    print(sum(i*j for i,j in P),P)
```

As the proof of the theorem only requires \\(\mc B\\) to be finitely generated over \\(\mc A\\), any counterexamples when relaxing the separable condition to Theorem 1 would require \\(\mc B\\) to not be finitely generated. Such a example can be found [here](https://math.stackexchange.com/a/24612/258870):

Let \\(k\\) be a field of characteristic \\(p>0\\) and let \\(y\in k[[x]]\\) be transcendental over \\(k[x]\\). Let \\(K=k\left(x,y^p\right), L=k\left(x,y\right), \mc A=k[[x]]\cap k\left(x,y^p\right), \mc B=k[[x]]\cap k\left(x,y\right)\\). \\(\mc A,\mc B\\) are DVRs with maximal ideal \\((x)\\) (hence Dedekind domains) with field of fractions \\(K,L\\) respectively and the extension \\(L/K\\) has degree \\(p\\). However, the residue field of \\(\mc A,\mc B\\) are both \\(k\\), hence the inertia degree and the ramification index of the prime \\((x)\\) is \\(1\\), in contrary to Theorem 1.

We can investigate the splitting behavior of primes by considering how certain polynomials factor mod \\(\mf p\\):

**Theorem 2:** Suppse \\(L|K\\) is a separable extension and \\(\theta\in\mc B\\) is a primitive element with minimal polynomial \\(p(x)\\). We define the **conductor** \\(\mf F\\) of the ring \\(\mc A[\theta]\\) as the ideal
\\[\mc F=\left\\{\beta\in\mc B|\beta\mc B\subseteq\mc A[\theta]\right\\}\\]
Then if \\(\mf p\subset\mc A\\) is relatively prime to \\(\mc F\\), let \\(p(x)=\prod_ip_i(x)^{e_i}\pmod{\mf p}\\) be the factorization of \\(p(x)\\) in \\(\frac{\mc A}{\mf p}[x]\\). The factorization of \\(\mf p\\) in \\(\mc B\\) is given by \\(\prod_i\mf P_i^{e_i}\\) where \\(\mf P_i=\mf p\mc B+p_i(\theta)\mc B\\). The inertia degree of \\(\mc P_i\\) is given as the degree of \\(p_i(x)\\).

This allows us to determine the splitting behavior of primes purely by looking at how polynomials split as we can vary the choice of primitive element to obtain a conductor coprime to a prime of choice.

We can also try this out in sage with a number field without a power basis for its ring of integers. Sage doesn't seem to have a way to compute the conductor, however we can compute the norm with `O.discriminant()/K.disc()` for number fields:

```python
K.<a> = NumberField(x^3+x^2-2*x+8)
th = 5*a+7*a^2
O = K.order(th)
f = O.discriminant()/K.disc()
for p in Primes()[:20]+[i for i,_ in factor(K.disc())]:
    if gcd(p,f) == 1:
        print(f"Factoring {p}")
    else:
        print(f"Factoring {p} (Note: not coprime to conductor)")
    pi = GF(p)[x](th.minpoly()).factor()
    Pi = [(K.ideal(ZZ[x](i).subs(x=th))+K.ideal(p),j) for i,j in pi]
    print(pi)
    print(prod(i^j for i,j in Pi))
```

The same counterexample for Theorem 1 when the separability condition is relaxed applies here as well. Using the notation from the counterexample, we have \\(\mc B=\mc A[y]\\), hence using \\(y\\) as our primitive element, \\(\mathfrak F=(1)\\) and all ideals are coprime to it. The minimal polynomial of \\(y\\) is given by \\(p(z)=z^p-\left(y^p\right)\in\mc A[z]\\) and when taken modulo \\((x)\\), the polynomial remains unchanged and still can't be factored, which is in direct contradiction to the factorization of \\((x)\in\mc A\\) in \\(\mc B\\), which remains as \\((x)\\).

## References
 - Jürgen Neukirch - Algebraic number theory


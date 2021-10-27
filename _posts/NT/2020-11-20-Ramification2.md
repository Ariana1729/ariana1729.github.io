---
layout: blog
title: Ramification Part 2
---

## Definitions

Let \\(\mc A\\) be a Dedekind domain with field of fractions \\(K\\), and let \\(M/L/K\\) be a tower of field extensions and \\(\mc B\\) and \\(\mc C\\) be the integral closure of \\(\mc A\\) in \\(L\\) and \\(K\\) respectively. By a prime \\(K,L,M\\), we mean a prime ideal in the Dedekind domains \\(\mc A,\mc B,\mc C\\) respectively.

Let \\(\mf p_M\\) be a prime in \\(M\\) above \\(\mf p_L\\) in \\(L\\) above \\(\mf p_K\\) in \\(K\\). Let \\(e_{\mf q\|\mf p},f_{\mf q\|\mf p}\\) be the ramification index and inertia degree of the prime \\(\mf q\\) above \\(\mf p\\). Then we have \\(e_{\mf p_M\|\mf p_L}e_{\mf p_L\|\mf p_K}=e_{\mf p_M\|\mf p_K}\\) and \\(f_{\mf p_M\|\mf p_L}f_{\mf p_L\|\mf p_K}=f_{\mf p_M\|\mf p_K}\\) directly from definition. 

From now, suppose \\(L/K\\) is a separable extension and let \\(M/K\\) be the normal closure of \\(L/K\\). Let \\(G=\Gal{M/K}\\) and \\(H=\Gal{M/L}\\).

Fix some prime \\(\mf p\\) in \\(K\\) and let its factorization in \\(M\\) be \\(\prod\mf P_i^{e_i}\\). Because \\(M\\) is Galois, we have the following properties:

 - \\(G\\) acts transitively on \\(\mf P_i\\)
 - The inertia degrees and ramification indices are all equal

The first property can be proven by contradiction as the norm of any element in \\(P_i\\) is in \\(\mf p\\) while the second is because any \\(\sigma\in G\\) is an automorphism of \\(\mc C\\). Hence, there is no ambiguity when we say the inertia degree and ramification index of \\(\mf p\\) in \\(M\\). From now, let \\(e,f\\) be the ramification index and the inertia degree of \\(\mf p\\) in \\(M\\) and \\(r\\) be the number of primes above \\(\mf p\\). 

Let \\(\mf P\\) be any prime in \\(M\\) above \\(\mf p\\) in \\(K\\). We define the **decomposition group** \\(G_{\mf P}\\) as the the stabalizer subgroup of \\(\mf P\\) under the action of \\(G\\) and the **decomposition field** \\(Z_{\mf P}\\) as the fixed field of \\(G_{\mf P}\\).

Before continuing, we need a short proposition:

**Proposition 1:** The extension \\(\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}\\) is normal and the morphism \\(G_{\mf P}\to\Aut{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}\\) is surjective.

As every \\(\sigma\in G_{\mf P}\\) is an automorphism of \\(\mc C/\mf P\\) that fixes \\(\mf A/\mf p\\), the morphism \\(G_{\mf P}\to\Aut{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}\\) is well defined. The proof can be found in Neukirch Chapter 1 Proposition 9.6. In the case of number fields, \\(\mc A/\mf p\\) is finite so this extension is Galois in the case of number fields.

We define the **inertia group** \\(I_{\mf P}\\) as the kernel of the morphism above and the **inertia field** \\(T_{\mf P}\\) as the fixed field of \\(I_{\mf P}\\).

With all of these definitions, we have the following and chain of fields and groups related by \\(\Gal{\cdot/M}\\):

\\[M\supseteq T_{\mf P}\supseteq Z_{\mf P} \supseteq K\\]
\\[\{e\}\subseteq I_{\mf P}\subseteq G_{\mf P}\subseteq G\\]

We note that \\(I_{\sigma\mf P},G_{\sigma\mf P}\\) are conjugates to \\(I_{\mf P},G_{\mf P}\\) respectively for \\(\sigma\in G\\).

## Properties

Now lets investigate the properties of these groups and fields.

Let \\(\mf P_T=\mf P\cap T_{\mf P},\mf P_Z=\mf P\cap Z_{\mf P}\\) be primes above \\(\mf p\\) in the fields \\(T_{\mf P},Z_{\mf P}\\) respectively.

As \\(G_{\mf P}\\) is the stabalizer of \\(\mf P\\), the only prime in \\(Z_{\mf P}\\) above \\(\mf p\\) is \\(\mf P_Z\\), implying the only prime in \\(T_{\mf P},M\\) above \\(\mf P_Z\\) is \\(\mf P_T\\) and \\(\mf P\\). Intuitively, one can imagine the fields \\(Z_{\sigma\mf P}\\) as 'isolating' the primes above \\(\mf p\\) in \\(M\\).

By orbit-stabalizer theorem, we have \\(\left\|G_{\mf P}\right\|=\frac{\|G\|}{r}=\frac{ref}r=ef\\). Hence we must have \\(e_{\mf P_Z\|\mf p}=f_{\mf P_Z\|\mf p}=1\\). Intuitively, the fields \\(Z_{\sigma\mf P}\\) isolate the different primes that \\(\mf p\\) split into in \\(M\\).

Now lets assume that \\(\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}\\) is separable, then \\(\Aut{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}=\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}\\), hence \\(\left\|\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}\right\|=f\\) and \\(\left\|I_{\mf P}\right\|=e\\).

Using proposition \\(1\\) on the Galois extension \\(M\|T_{\mf P}\\), we see that the morphism \\(\Gal{M/T_{\mf P}}=I_{\mf P}\to\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc T}{\mf P_T}}\\) is surjective where \\(\mc T\\) is the integral closure of \\(\mc A\\) in \\(T\\). 
By definition, \\(I_{\mf P}\\) must act trivially on \\(\mc C/\mf P\\), hence \\(\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc T}{\mf P_T}}\\) must be trivial, implying that \\(\frac{\mc C}{\mf P}\cong\frac{\mc T}{\mf P_T}\\) and \\(f_{\mf P\|\mf P_T}=1\\).

Finally, we can give the following identities:

\\[
\begin{aligned}
    e_{\mf P_Z|\mf p}&=1&f_{\mf P_Z|\mf p}&=1\\\\\\\\
    e_{\mf P_T|\mf P_Z}&=1&f_{\mf P_T|\mf P_Z}&=f\\\\\\\\
    e_{\mf P|\mf P_T}&=e&f_{\mf P|\mf P_T}&=1\\\\\\\\
\end{aligned}
\\]

## Non-Galois case

Now let's consider how the prime splits in \\(L\\). 

We have the bijection from the double cosets \\(H\setminus G/G_{\mf P}\\) to the primes above \\(\mf p\\) in \\(L\\) given by \\(H\sigma G_{\mf P}\to\sigma\mf P\cap L\\). Let \\(\mf P_B=\mf P\cap\mc B\\), we shall now compute \\(f_{\mf P_B\|\mf p}\\) purely with the groups that we have.

We have \\(\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc A}{\mf p}}\cong\frac{G_{\mf P}}{I_{\mf P}}\\) and the tower of field extensions \\(\left.\left.\frac{\mc C}{\mf P}\right/\frac{\mc B}{\mf P_B}\right/\frac{\mc A}{\mf p}\\). As \\(H=\Gal{M/L}\\), we have the surjection from \\(H\cap G_{\mf P}\to\Gal{\left.\frac{\mc C}{\mf P}\right/\frac{\mc B}{\mf P_B}}\\) with kernel \\(H\cap I_{\mf P}\\), hence we have
\\[\left[\frac{G_{\mf P}}{I_{\mf P}}:\frac{G_{\mf P}\cap H}{I_{\mf P}\cap H}\right]=\left[\frac{\mc C}{\mf P}:\frac{\mc B}{\mf P_B}\right]=f_{\mf P_B\|\mf p}\\]

We can also write some sage code to test this! Note that the following sage code does take some time to run.

```python
K.<a> = NumberField(x^4 + x^3 + 3*x^2 + 4*x + 18)
L.<b> = K.galois_closure()
q = 17
print("Computed Galois closure")
f = K.embeddings(L)[0]
G = list(L.galois_group())
print("Computed Gal(L/Q)")
aL = f(a)
H = [g for g in G if g(aL)==aL]
print("Computed Gal(L/K)")
for p,eK in K.factor(q):
    fK = p.residue_class_degree()
    print(f"Prime above {q}: {p}")
    print(f"Ramification index: {eK}")
    print(f"Inertia degree: {fK}")
    for P,eL in L.factor([f(i) for i in p.gens()]):
        fL = P.residue_class_degree()/fK
        GP = P.decomposition_group()
        IP = P.inertia_group()
        GPH = [g for g in GP if g in H]
        IPH = [g for g in IP if g in H]
        t = len(GP)*len(IPH)/QQ(len(GPH)*len(IP))
        print(f"\tComputed inertia degree with groups: {t}")
```

The behavior of other primes can be found easily as well as the decomposition and inertia groups are conjugates to each other for the conjugate primes.

With the decomposition and inertia fields, we can easily show that
 - \\(\mf p\\) is unramified in \\(L\iff\mf p\\) is unramified in \\(M\\)
 - \\(\mf p\\) is totally split in \\(L\iff\mf p\\) is totally split in \\(M\\)

The reverse inclusion is immediate as \\(L\subseteq T_{\mf P}=M\\) and \\(L\subseteq Z_{\mf P}=M\\) respectively. For the forward inclusion, note that we have \\(\sigma L\subseteq T_{\mf P}\\) and \\(\sigma L\subseteq Z_{\mf P}\\) respectively for all \\(\sigma\in\Gal{M/K}\\). As \\(M\\) is the Galois closure if \\(L\\), this implies that \\(T_{\mf P}=M\\) and \\(Z_{\mf P}=M\\) respectively, showing the forward inclusion.

Similarly, we can also write some sage code to check this:

```python
K.<a> = NumberField(x^4 + x^3 + 3*x^2 + 4*x + 18)
L.<b> = K.galois_closure()
dK = K.degree()
dL = L.degree()
print("Computed Galois closure")
for p in Primes()[:100]:
    fac = K.factor(p)
    if len(fac) == dK:
        print(f"{p} is totally split in K")
    elif all(e==1 for e,f in fac):
        print(f"{p} is unramified in K")
    else:
        print(f"{p} has some ramification/inertia")
    fac = L.factor(p)
    if len(fac) == dL:
        print(f"{p} is totally split in L")
    elif all(e==1 for e,f in fac):
        print(f"{p} is unramified in L")
    else:
        print(f"{p} has some ramification/inertia")
```

## References
 - Jürgen Neukirch - Algebraic number theory

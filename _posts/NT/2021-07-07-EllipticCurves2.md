---
layout: blog
title: Elliptic Curves Part 2 - Lattices
---

## Classifying all curves

Recall that we defined \\(\wp_\Lambda(z)\\) in terms of some lattice \\(\Lambda=\mb Z\omega_1+\mb Z\omega_2\\) and an elliptic curve as \\(\mb C/\Lambda\\). The next obvious thing to do would be to define a morphism between curves, and the most obvious way is as a holomorphic map. More specifically, given elliptic curves \\(E=\mb C/\Lambda,E'=\mb C/\Lambda'\\), a map between them is a holomorphic map \\(\phi:E\to E'\\). As elliptic curves are compact, all maps must either be constant or surjective due to the open mapping theorem. We typically ignore the constant curve and call the surjective maps isogenies. If an inverse isogeny \\(\psi:E'\to E\\) exists such that \\(\psi\circ\phi=\id_E,\phi\circ\psi=\id_{E'}\\), then \\(E,E'\\) are isomorphic.

Now we aim to 'classify all elliptic curves'. First fact to notice is that by multiplying a lattice by an element in \\(\SL{2,\mb Z}\\), meaning 
\\[\begin{pmatrix}a&b\\\\c&d\end{pmatrix}:\begin{pmatrix}\omega_1\\\\\omega_2\end{pmatrix}\mapsto\begin{pmatrix}a&b\\\\c&d\end{pmatrix}\begin{pmatrix}\omega_1\\\\\omega_2\end{pmatrix}\\]
we actually get the same lattice back since every element in \\(\SL{2,\mb Z}\\) is invertible. Now using the holomorphic map \\(z\mapsto\frac z{\omega_1}\\), we see all elliptic curves are isomorphic to some lattice \\(\mb Z+\mb Z\tau\\). While its tempting to say that \\(\mb C/\SL{2,\mb Z}\\) is all elliptic curves, we actually should be using the upper half plane since \\(\mb Z+\mb Z\tau=\mb Z-\mb Z\tau\\) and if \\(\tau\in\mb R\\), we dont actually get an elliptic curve. Hence we have an isomorphism between elliptic curves and \\(\mc H/\SL{2,\mb Z}\\) where \\(\mc H=\\{z\in \mb C|\Im(z)>0\\}\\). Hence we typically use \\(\tau\in\mc H\\) to refer to the elliptic curve \\(\mb Z+\mb Z\tau\\).

It turns out theres a natural way to biject \\(\mc H/\SL{2,\mb Z}\\) to \\(\mb C\\) via the \\(j\\)-invariant. For an elliptic curve \\(y^2=4x^3-g_2(\tau)x-g_3(\tau)\\), we define
\\[j(\tau)=1728\frac{g_2(\tau)^2}{g_2(\tau)^3-27g_3(\tau)^2}\\]
Through a nontrivial application of the residue theorem, one can show this is a surjective function from \\(\mc H\to\mb C\\). Furthermore, since \\(\frac{g_3(\tau)^2}{g_2(\tau)^3}=\frac{j(\tau)-1728}{27j(\tau)}\\)
and recalling that \\(g_k\propto\sum_{\lambda\in\Lambda-\{0\}}\lambda^{-k}\\), the only elliptic curves with the same \\(j\\)-invariant must be the ones obtained through scaling! Hence the \\(j\\) invariant is yet another way to classify elliptic curves.

## Endomorphisms

Another natural question to ask is what is the endomorphism group of an elliptic curves. It turns out holomorphic maps are quite restrictive and by using the fact that \\(\mb C\\) is the universal cover of elliptic curves, one obtains the fact that maps between curves are simply linear functions over \\(\mb C\\) (consider the derivative of the lifted function, it must be doubly periodic!). This tells us that the only endomorphisms that we need to consider is \\(z\mapsto kz\\). As we require \\(k\mb Z+k\tau\mb Z\subset\mb Z+\tau\mb Z\\), we need \\(k,k\tau\in\mb Z[\tau]\\). Hence if \\(k=a+b\tau\\), we have \\(k\tau=a\tau+b\tau^2\in\mb Z[\tau]\\), implying that either \\(k\in\mb Z\\), or \\(\tau\in\mb Q(\sqrt{-d})\\) for some \\(d\\)! In the case where the endomorphism group is larger than \\(\mb Z\\), the curve is said to have complex multiplication. 

Suppose further that \\(\tau\\) is an algebraic integer, meaning \\(\tau^2+a\tau+b=0\\) for some \\(a,b\in\mb Z\\). Let \\(K=\mb Q(\tau)\\), then it turns out that
\\[\End{\mb Z+\mb Z\tau}=\mb Z+\mb Z\tau\subseteq\mc O_K\\]
One easy way to get an endomorphism group of \\(\mc O_K\\) is to use ideals in \\(\mc O_K\\) since they are lattices as well. This immediately implies that there is a bijective correspondence between \\(Cl(K)\\) and elliptic curves with endomorphism group \\(\mc O_K\\)!

## \\(N\\)-torsion

For any elliptic curve \\(\Lambda=\mb Z\omega_1+\mb Z\omega_2,\frac{\omega_1}{\omega_2}\in\mc H\\), it is immediate that the points with \\(N\\)-torsion is precisely the lattice \\(\frac1n\Lambda\\). This tells us that the group structure of the \\(N\\)-torsion points on an elliptic curve \\(E\\) is simply \\(C_N\times C_N\\) and is denoted by \\(E[N]\\). It turns out that there's a natural 'inner product' that maps pairs to roots of unity. Let \\(P,Q\in E[N]\\), then we have
\\[\begin{pmatrix}P\\\\Q\end{pmatrix}=\frac1N\begin{pmatrix}a&b\\\\c&d\end{pmatrix}\begin{pmatrix}\omega_1\\\\\omega_2\end{pmatrix}\\]
and we define the Weil pairing to be
\\[e_N(P,Q)=e^{\frac1N2\pi i(ad-bc)}\\]
This paring satisfies many properties that we like - it's bilinear, alternating/antisymmetric and nondegenerate and many other nice properties. For instance if we have an isomorphism of elliptic curves \\(f:E\to E'\\), \\(e_{N,E}(P,Q)=e_{N,E'}(f(P),f(Q))\\) and nore interestingly the following diagram commutes:

{::nomarkdown}
<p align="center">
    <img src = "/static/posts_image/EllipticCurves2_1.svg" alt="some commutative diagram" width="25%"/>
</p>
{:/}


Furthermore if \\(P,Q\\) generates \\(E[N]\\), then \\(e_N(P,Q)\\) is a primitive root of unity. While this definition seems somewhat opaque, it's easier to see it in a more algebraic perspective where it can be defined as some quotients of some divisors or as some antisymemtric bilinear map on the Tate module.

## References 
 - Neal Koblitz - Introduction to Elliptic Curves and Modular Forms
 - Fred Diamond and Jerry Shurman - A First Course in Modular Forms

---
layout: blog
title: Elliptic Curves Part 1 - Doubly periodic functions
---

This exposition introduces how one can naturally come across elliptic curves by exploring rather natural questions in complex analysis.

## Doubly periodic functions

One recalls that in real analysis, given a square intergrable function \\(f:\mb R\to\mb C\\) with period \\(T\\), i.e. \\(f(x+T)=f(x)\\), one can write express \\(f(x)\\) as a sum of \\(e^{\frac{2\pi ix}{T}}\\), in particular,

\\[\hat f(n)=\frac1T\int_0^Tf(x)e^{\frac{-2\pi inx}T}dx\quad f(x)\sim\sum_{n=-\infty}^\infty\hat f(n)e^{\frac{2\pi inx}T}\\]

with some appropriate notion of convergence. One could ask a similar question over the complex numbers, but in this case since \\(\mb C\\) is `two dimensional', we can ask for double periodicity, i.e. \\(f(z)=f(z+\omega_1)+f(z+\omega_2)\\). If the function is simply \\(L^2\\) integrable, one can perform a similar fourier transform so it doesn't get much more interesting. However what if we require that the function is complex differentiable, or perhaps meromorphic? The answer turns out to be rather elegant and leads us naturally to considering elliptic curves!

Let \\(\Lambda=\mb Z\omega_1+\mb Z\omega_2\\) be the lattice generated by \\(\omega_1,\omega_2\\) and \\(\Pi=[0,1)\omega_1+[0,1)\omega_2\\) be the fundamental domain. One viewpoint we can take is that \\(f\\) is a function from \\(\mb C/\Lambda\to\mb C\cup\{\infty\}\\) where the map is a map of Riemann surfaces. We will go back to this viewpoint eventually.

First, let's search for nontrivial examples of such functions. The simplest example one can come up with is
\\[\sum_{\lambda\in\Lambda}(z-\lambda)^{-3}\\]
where this sum converges absolutely so the order of the summation doesn't matter. (note as long as the exponent is smaller than $-2$ it works). It turns out that this is not quite the correct function to consider, instead we integrate this function and throw in some constant terms to obtain the weiestrass elliptic functions:

\\[\wp_\Lambda(z)=z^{-2}+\sum_{\lambda\in\Lambda-\\{0\\}}(z-\lambda)^{-2}-\lambda^{-2}\\]
\\[\wp_\Lambda'(z)=-2\sum_{\lambda\in\Lambda}(z-\lambda)^{-3}\\]

Similarly one can verify both sum converges absolutely, in the first case since the term in the sum grows like \\(\lambda^{-3}\\) eventually, hence order of summation is not a concern here either. To verify double periodicity, notice that \\(\wp_L'(z)\\) is doubly periodic and \\(\wp(z)=\wp(-z)\\), hence it follows that \\(\wp_L(z)\\) is doubly periodic.

It turns out that if \\(f(z)\\) is doubly periodic, it can be written as a rational fucntion of \\(\wp(z)\\) and \\(\wp'(z)\\)! More specifically, if \\(f(z)\\) is even and doubly periodic, we can write it as a rational function in terms of \\(\wp(z)\\). The general case follows using the fact \\(\wp'(z)\\) is odd.

First, we show that \\(f(z)\\) has finitely many zeros/poles in \\(\overline{\Pi}\\). Suppose it has infinitely many, then since \\(\overline{\Pi}\\) is compact, the set of all zeros/poles cannot be isolated but that contradicts the memomorpic assumption.

Since we know \\(f(z)\\) has finitely many zeros/poles, we can construct some rational function \\(P(x)\\) such that \\(P(\wp(z))\\) has the same zeros/poles as \\(f(z)\\) counting multiplicity since we can't have essential singularities (again the meromorphic condition). Since \\(\frac{f(z)}{P(\wp(z))}\\) has no poles or zeros, it is bounded on \\(\Pi\\), hence on the entire complex plane, but this implies it is constant!

## Elliptic curves

Since the proof above is constructive, and we can apply it to the even function \\(\wp'(z)^2\\) to obtain

\\[\wp'(z)^2=4\left(\wp(z)-\underbrace{\wp\left(\frac{\omega\_1}2\right)}\_{e\_1}\right)\left(\wp(z)-\underbrace{\wp\left(\frac{\omega\_2}2\right)}\_{e\_2}\right)\left(\wp(z)-\underbrace{\wp\left(\frac{\omega\_1+\omega\_2}2\right)}\_{e\_3}\right)\\]

Now by considering the laurent series expansion and defining

\\[G_k=\sum_{\lambda\in\Lambda-\\{0\\}}\lambda^{-k}\\]

for \\(k>2\\), one obtains

\\[\wp'(z)^2=4\wp(z)^3-60G_4\wp(z)-140G_6\\]

which looks precisely like the elliptic curves we see often in cryptography or other areas that you may encounter them in! We typically define \\(g_2=60G_4,g_3=140G_6\\) so our curve now looks like \\(\wp'(z)^2=4\wp(z)^3-g_2\wp(z)-g_3\\)

With this, we have an extremely simple way to add points on the curve \\(y^2=4x^3-g_2x-g_3\\):

\\[\left(\wp(z_1),\wp'(z_1)\right)+\left(\wp(z_2),\wp'(z_2)\right)=\left(\wp(z_1+z_2),\wp'(z_1+z_2)\right)\\]

It turns out that the solutions to the elliptic curve corresponds bijectively to \\(\mb C/\Lambda\\), more specifically, the map

\\[z\to\begin{cases}(\wp(z),\wp'(z),1)&z\neq0\\\\(0,1,0)&z=0\end{cases}\\]

is a bijection from \\(\mb C/\Lambda\\) to solutions to \\(y^2=4x^3-60G_4x-g_3\\). The bijectivity comes from noticing that \\(\wp(z)\\) is ramified double covering with four branch points since \\(\wp(z)=\wp(-z)\\) from \\(\mb C/\Lambda\to\mb C\cup\{\infty\}\\) and the branch points are \\(e_1,e_2,e_3,\infty\\).

Let \\(\cdot=\left(\wp(z_\cdot),\wp'(z_\cdot),1\right)\\), then one can prove that if \\(P+Q=R\\), then \\(P,Q,-R\\) are colinear. Notice that for any doubly periodic meromorphic function \\(f(z)\\), both the sum of orders of poles/zeros as well as sum of the positions of the poles/zeros must add up to zero in \\(\Pi\\) by integrating \\(\frac{f'(z)}{f(z)}\\) and \\(\frac{zf'(z)}{f(z)}\\) respectively. Let \\(P,Q\\) be on the line \\(y=mx+c\\), then since \\(\wp'(z)-m\wp(z)-c\\) has a triple pole at \\(0\\) and a zero at \\(z_P\\) and \\(z_Q\\) respetively, the last zero bust be at \\(-z_P-z_Q\\), hence we are done. The case of \\(P=Q\\) or \\(P,Q\\) at infinity is handled similarly. This leads to a natural way to generalize addition of points on elliptic curves to other fields!

By considering doubly periodic meromorphic functions on the complex plane, one obtains elliptic curve and the point addition formula with a sufficient number of application of Cauchy's residue theorem. It turns out one can do a lot more with this! By studying maps between different lattices, one can obtain isogenies and complex multiplication quite easily. By trying to compute \\(G_k\\) for \\(k>6\\), one quickly finds modular forms appearing. The construction that points on a line sum to zero is precisely the picard group, which leads to a wild list of constructions in algebraic geometry!
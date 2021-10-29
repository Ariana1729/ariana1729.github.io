---
layout: blog
title: Smart Attack - Elliptic curves over \(\mb Q_p\) and formal groups 
---

This small exposition aims to give a sketch of how the Smart attack works. One can find the precise details in Silverman AEC Exercise 7.13.

Notation used:
 - \\(K\\) is a characteristic \\(0\\) local field with discrete normalized valuation \\(v\\)
 - \\(\mc O\\) is the ring of integers of \\(K\\)
 - \\(\pi\\) a uniformizer of \\(K\\)
 - \\(\mf m\\) is the maximal ideal of \\(\mc O\\)
 - \\(k\\) is the residue field of \\(K\\)
 - \\(p\\) is the characteristic of \\(k\\)
 - \\(q=p^f\\) is the order of \\(k\\)
 - \\(E\\) an elliptic curve over \\(K\\)

The outline of the Smart attack can be summarized as:

We have an exact sequence \\(0\to E_1(K)\to E_0(K)\to\tilde E_{ns}(K)\to 0\\) due to Hensel's lemma, and we have an isomorphism \\(E_1(K)\cong\hat E(\mf m)\\) and finally an isomorphism of formal groups \\(\log_{\hat E}:\hat E(\mf m)\to\hat{\mb G_a}(\mf m)\\). In this post we shall *attempt* to decipher this summary.

For some intuition, one can consider the case that commonly appears in the Smart attack:

 - \\(K=\mb Q_p\\)
 - \\(v=v_p\\)
 - \\(\mc O=\mb Z_p\\)
 - \\(\pi=p\\)
 - \\(\mf m=p\mb Z_p\\)
 - \\(k=\mb F_p\\)

## Exact sequence

First we shall consider the reduction map mod \\(\pi\\). For any point \\(P\in\mb P^n(K)\\), by choosing suitable homogeneous coordinates, when we take mod \\(\pi\\) on each coordinate, we get a new point \\(\tilde P\in\mb P^n(k)\\). In general, we denote reduction mod \\(\pi\\) by adding a \\(\tilde{~}\\) on top. For instance given the point \\([5,6,7]\in\mb P^2(\mb Q_3)\\), the reduction mod \\(3\\) gives the point \\([2,0,1]\in\mb P^2(\mb F_3)\\). This reduction map gives us the curve \\(\tilde E/k\\).

Let \\(\tilde E_{ns}(k)\\) be the group of nonsingular points on \\(\tilde E\\). Since these points are nonsingular, we can lift them up to points in \\(E(K)\\). This suggests we define the group \\(E_0(K)=\left\\{P\in E(K):\tilde P\in\tilde E(k)\right\\}\\). This gives us a surjective map \\(E_0(K)\to\tilde E(k)\\). The kernel of this map is evidently every point that gets mapped to the identity \\(\tilde O\\) of \\(\tilde E(k)\\), hence we define \\(E_1(K)=\left\\{P\in E(K):\tilde P=\tilde O\right\\}\\) as the kernel of reduction. Hence by definition, we have the exact sequence

\\[0\to E_1(K)\to E_0(K)\to\tilde E(k)\to 0\\]

(One should verify the maps are indeed group morphisms)

Before we go on, we need a brief discussion on formal groups.

## Formal groups

Intuitively, a formal group is a group law that is not explicitly defined over any set. The simplest example is the additive formal group, given by \\(\hat{\mb G}_a(X,Y)=X+Y\\). We first define a formal group law over a ring \\(R\\):

**Definition:** A one parameter commutative formal group law \\(\mc F\\) over a ring \\(R\\) is a power series \\(\mc F\in R[\\![X,Y]\\!]\\) satisfying:
 - \\(\mc F(X,0)=X,\mc F(0,Y)=Y\\)
 - \\(\mc F(X,\mc F(Y,Z))=\mc F(\mc F(X,Y),Z)\in R[\\![X,Y,Z]\\!]\quad\\)associativity
 - \\(\mc F(X,Y)=\mc F(Y,X)\quad\\)commutativity

As one typically can't sum infinitely many elements in a ring, the formal group associated with the formal group law can only take on values on the nilpotent elements of \\(R\\). However in the case of rings with a valuation, the notion of convergence is well defined, so in such cases the formal group can take on values in the elements with positive valuation. We denote \\(\mc F(I)\\) as the group associated with the formal group law taking values in \\(I\\). Typically \\(I\\) would be the nilradical but in the case of rings with valuation, \\(I\\) can be any ideal.

**Example:** The formal group law \\(\hat{\mb G}_a=X+Y\\) corresponds to addition and the formal group law \\(\hat{\mb G}_m=X+Y+XY=(1+X)(1+Y)-1\\) corresponds to multiplcation. The power series \\(\frac{X+Y}{1+XY}\\) corresponds to velocity addition in special relativity. We have \\(\hat{\mb G}_a(p\mb Z_p)=(p\mb Z_p)^+\cong\mb Z_p^+\\).

We shall now construct the formal group \\(\hat E\\) associated to an elliptic curve \\(E\\). Suppose we are given the Weiestrass equation of \\(E\\):

\\[y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6\\]

In this presentation, every point in the elliptic curves is given by two variables, while our formal group law can really only take in one variable. This motivates us to perform the substitution \\(z=-\frac xy,w=-\frac1y\\) and we obtain

\\[w=z^3+\left(a_1z+a_2z^2\right)w+\left(a_3+a_4z\right)w^2+a_6w^3\\]

Now by repeatedly substituting the expression into itself and by taking limits, we can obtain \\(w=f(z)\in\mb Z[a_1,\dots,a_6][\\![z]\\!]\\). This gives us a one parameter parametrization of points on the curve. Let \\(g(z)\\) be the corresponding point on the curve, we define the elliptic curve formal group law as

\\[\hat E(X,Y)=g^{-1}\left(g(X)+g(Y)\right)\\]

For notation purposes, we let \\((x(z),y(z))\\) be the cprresponding point on the curve.

Like most algebric objects, we have a notion of morphisms of formal groups as well:

**Definition:** A morphism \\(\phi:\mc F\to\mc G\\) of formal group laws is a power series \\(\phi\in R[\\![X]\\!]\\) such that
 - \\(\phi(0)=0\\)
 - \\(\mc G(\phi(X),\phi(Y))=\phi(\mc F(X,Y))\\)

**Example** We have the identity \\(\phi(X)=X\\) for every formal group law. Consider the power series over a \\(\mb Q\\)-algebra \\(\phi(X)=\log(1+X)=X-\frac{X^2}2+\frac{X^3}3+\dots\\), this is a morphism \\(\phi:\hat{\mb G}_a\to\hat{\mb G}_m\\) and it has an inverse, \\(e^X-1=X+\frac{X^2}{2!}+\frac{X^3}{3!}+\dots\\), hence the formal group laws \\(\hat{\mb G}_a\\) and \\(\hat{\mb G}_m\\) are isomorphic over \\(\mb Q\\)-algebras. 

We see that we have found an isomorphism between \\(\hat{\mb G}_a\\) and \\(\hat{\mb G}_m\\), which would make the discrete log problem quite easy whenever this exists. So now our goal is to find such an isomorphism for other formal groups. If we can find an isomorphism \\(\hat E\cong\hat{\mb G}_a\\), the discrete log problem on the corresponding curve should be computatinally easy to solve. This isomorphism is given by the logarithm of formal groups:

**Definition:** For a formal group \\(\mc F\\), \\(\log_{\mc F}\\) is an isomorphism from \\(\mc F\\) to \\(\hat{\mb G}_a\\).

For \\(\mb Q\\)-algebras, such an isomorphism always exists and is given by

\\[\log_{\mc F}(T)=\int\frac{dT}{\partial_X F(0,T)}\\]

where we require \\(\log_{\mc F}(0)=0\\), fixing the constant of integration. One can quickly verify that we recover \\(\log(1+T)\\) in the case of \\(\hat{\mb G}_m\\). In the case of elliptic curves, the differential being integrated is the classic invariant differential of an elliptic curve

\\[\frac{dz}{\partial_X{\hat E}(0,z)}=\frac{dx(z)}{2y(z)+a_1x(z)+a_3}\\]

As the inverse of \\(\log_{\mc F}\\) may not converge for a formal group associated with \\(\mc F\\), we may not always have the isomorphism \\(\mc F(I)\cong\hat{\mb G}_a\\), however for charateristic \\(0\\) local fields (using the convention at the start), we have

\\[\log_{\mc F}:\mc F\left(\mf m^r\right)\to\hat{\mb G}_a\left(\mf m^r\right)\\]

is an isomorphism if \\(r>\frac{v(p)}{p-1}\\).

In summary, each point on a curve can be parametrized by a single parameter \\(z\\), with \\(z=0\\) being the identity. This gives rise to a formal group law \\(\hat E\\) which takes this parameter as its input and we have an isomorphism \\(\hat E\cong\hat{\mb G}_a\\).

## Smart attack

Evidently \\(\hat E(\mf m)\\) is isomorphic to the group of points on \\(E(K)\\) such that \\(\frac xy\\) has positive valuation. This turns out to be precisely the group \\(E_1(K)\\) that we defined above as all such points must be in the kernel of the reduction map, hence nonsingular. From here we're almost done. Suppose \\(E_{ns}(k)\\) is a group of order \\(q\\) and suppose we have \\(n\tilde P=\tilde Q\\) in \\(E_{ns}(k)\\). Let \\(\log\\) be the composite map \\(E_1(K)\cong\hat E(\mf m)\cong\hat{\mb G}_a(\mf m)\\). Lift \\(\tilde P,\tilde Q\\) to points \\(P,Q\in E_0(K)\\), then since \\(nP-Q\in E_1(K)\\), we have

\\[n\log(qP)-\log(qQ)=q\log(nP-Q)=0\pmod{\mf m^{f+1}}\\]

which gives us some \\(n\in\frac{\mc O}{\mf m^f}=\frac{\mc O}{(q)}\\) as long as \\(\log(qP)\notin\mf m^2\\). Hence \\(n\\) is a well defined multiplication map of \\(\tilde E(k)\\), which gives us a solution to the DLP over \\(\tilde E(k)\\).

## References
 - Johannes Anschütz - Lubin-Tate Spaces (Sommersemester 2021) [lecture notes](http://www.math.uni-bonn.de/people/ja/lubintate/lecture_notes_lubin_tate.pdf)
 - Joseph H. Silverman - The Arithmetic of Elliptic Curves


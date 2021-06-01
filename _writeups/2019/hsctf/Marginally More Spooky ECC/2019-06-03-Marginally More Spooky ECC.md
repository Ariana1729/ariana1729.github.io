---
layout: writeup
ctf: HSCTF 6
chal: Marginally More Spooky ECC
flag: hsctf{Y_does_4lice_have_such_weird_cuRV3s?}
points: 473
category: crypto
---

>Now marginally more spooky!

>[intercept.txt](intercept.txt)

>[problem.sage](problem.sage)

We are given [intercept.txt](intercept.txt) and [problem.sage](problem.sage), which are some data the challenge script.

## Description

This implements an elliptic curve key distribution algorithm, and the curve has quite a interesting property, `E_order = N`. This allows us to use the smart attack.

## Smart attack

The main idea about this is to lift the curve from mod `N` to mod `N^2`, and ECC multiplication becomes an additive group. More detail is in the paper about smart attack [here](https://www.hpl.hp.com/techreports/97/HPL-97-128.pdf)

## Derivation of Hensel lifting

Here is just a short derivation of Hensel lifting for this particular case.

Let \\(f(y)=y^2-k\\) where \\(k\\) is given by \\(x^3+ax+b\\). Let's say we found a root of \\(f(y)\pmod p\\), then we can find a root, with \\(s=y\pmod p\\) and \\(f(s)=0\pmod{p^2}\\).

Since \\(y^2-k=0\pmod N,\quad y^2-k=rN\pmod{N^2}\\)

\\[f(y+aN)=y^2-k+2yaN=(r+2ya)N=0\pmod{N^2}\\]

Since we just need to find \\(a\\), we get \\(r+2ya=0\pmod N\\) and \\(a=-\frac r{2y}=-\frac{y^2-j}{2yN}\pmod N\\). 

The division of \\(N\\) is well defined since \\(y^2-k=0\pmod N\\).

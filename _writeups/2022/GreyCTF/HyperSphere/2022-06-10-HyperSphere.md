---
layout: writeup
ctf: Grey CTF 2022
chal: HyperSphere
category: crypto
flag: grey{HyperSphereCanBeUsedForKeyExchangeToo!(JustProbablyNotThatSecure)_33JxCZjzQQ7dVGvT}
points: 489
solves: 12
---

> Why would anyone use quaternion to do DLP...

Files given:
 - [main.py](main.py)
 - [point.py](point.py)

This problem a generic DLP problem, except the discrete log is over the quaterions. Interestingly, we are able to input our own prime and point such that it passes the following checks:

```python
def checkPrime(prime : int) -> bool:
    return prime.bit_length() >= 512 and isPrime(prime)

def checkPoint(ta : int, tb : int, tc : int, td : int) -> bool:
    cond1 = 10 < ta < p - 2
    cond2 = 10 < tb < p - 2
    cond3 = 10 < tc < p - 2
    cond4 = 10 < td < p - 2
    cond5 = (ta * ta + tb * tb + tc * tc + td * td) % p == 1
    return cond1 and cond2 and cond3 and cond4 and cond5
```

Notice that none of these checks are checking if the group generated by our input is small or has small prime factors! This suggests that we find some root of unity of small order. This can easily be done with the following observation:

\\[\left(\frac{-1+i+j+k}2\right)^3=1\\]

Hence this remains true in any quaternion algebra \\((-1,-1)_{\mb F_p}\\) for any \\(2\nmid p\\). We simply need to send this to the server and get our flag.

Solution at [solve.py](solve.py)

---
layout: writeup
ctf: WhiteHats CTF 2021
chal: This requires a very Smart Attack (A, B)
category: crypto
flag: WH2021{N0t_4_v3rY_S3cUr3_3nCrypT10n_1f_kn0w1ng_0n3_s33d_C4n_d3crYp4_s0_mUCh}, WH2021{0_w0w_U_d1D_1t_g00d_jOB}
points: 500, 500
solves: 1, 1
---

>So Pat has learnt some Elliptic Curve Point Multiplication and she was like "I wanna implement some Dual_EC_DRBG" and I'm like "Isn't that the one with the fishy NSA backdoor?" but then she was like "I'm gonna generate my own curve".

>So anyways she encrypted secret.txt with a key and threw away secret.txt and said key.

>And I want them back. Can you decrypt as much of secret.txt as you can and recover the key?

Files given:
 - [eccrypt.py](eccrypt.py)
 - [secret-960_992.txt](secret-960_992.txt)
 - [secret.enc](secret.enc)

This challenge has two flags in it and presents a worse version of the [Dual_EC_DRBG](http://projectbullrun.org/dual-ec/) PRNG. We first give a brief description of the implemented PRNG, then describe how it can be broken to obtain the first flag then with more effort, the second flag.

## Flawed PRNG

1. Initialize with
   - Elliptic curve over a finite field of prime order \\(E/\mb F_p\\)
   - Points \\(P,Q\in E\left(\mb F_p\right)\\)
   - Seed \\(seed\\)
2. Generate the keystream by setting \\(seed=(seed\cdot P)\_x\\) and returning \\((seed\cdot Q)\_x\\) as the stream 

Suppose we know that \\(kP=Q\\), then we know \\(k\cdot seed\cdot Q=seed\cdot P\\), which is precisely the next iteration, breaking the PRNG completely.Now we only need to find a \\(k\\) such that \\(kP=Q\\).

Note that as per usual, we XOR the stream with our plaintext. Since we are given the 30th plaintext chunk, we know the 30th output of the stream cipher.

## Curve has trace 1!

If you have seen CTF challenges enough, there is only so many possible attacks. A smooth order of P, low embedding degree, or trace 1 curves. Fortunately the curve has trace 1! To see this open sage and run `EllipticCurve(GF(p),[A,B]).trace_of_frobenius()`.

This allows us to perform the Smart attack. In summary the Smart attack relies on a certain exact sequence of curves over local fields and an isomorphism between one dimensional formal groups, in the future I'm planning to write a blog post about it but for now feel free to find online resources about it!

With this in mind, we decrypt all the text after the 30th block:

```py
s30 = 0xb4a594ad888dfc431ae16437ec0d894a3cac840d151962addf139c4b1f63ec73
sQ = E.lift_x(s30,all=True)[0]
seed[30] = launch_attack(Q,sQ,p,A,B)
for i in range(31,len(seed)):
    seed[i] = ZZ((seed[i-1]*P).xy()[0])
    t = xor(get_stream(seed[i])),enc[i*32:(i+1)*32])
    print("".join(chr(i) for i in t))
```

and this gives us

```
 that  Earth will be very warm i
n the days to come. It will be
warm and will get very cold, and
  will probably turn into a get
 cold again. But  Earth is very
good at  understanding  her own
behavior. In a few weeks , it wi
ll  be good for everyone. I hope
 this is a helpful and instructi
ve  example.

WH2021{N0t_4_v3r
Y_S3cUr3_3nCrypT10n_1f_kn0w1ng_0
n3_s33d_C4n_d3crYp4_s0_mUCh}
```

giving us the first flag.

## Second flag

As we have the smart attack, we can use it iteratively to reverse the PRNG. However as there are two possible points with the same x coordinates, this is quite a lot of bruteforcing. Fortunately we can assume that the plaintext comprises of ascii characters and skip the branches that results in garbage plaintext. This gives us the second flag

```py
def rev(seed,P,n):
    if n == 0:
        print(hex(seed))
        return [[]]
    sP = E.lift_x(seed,all=True)
    if len(sP) == 0:
        return []
    sol = []
    p_seed = launch_attack(P,sP[0],p,A,B)
    t = xor(sec(ZZ(p_seed)).to_bytes(32, 'big'),enc[(n-2)*32:(n-1)*32])
    if not all(0<i<0x80 for i in t):
        return []
    print("".join(chr(i) for i in t))
    for i in rev(p_seed,P,n-1):
        if [p_seed]+i not in sol:
            sol.append([p_seed]+i)
    p_seed = ZZ((-p_seed) % p)
    for i in rev(p_seed,P,n-1):
        if [p_seed]+i not in sol:
            sol.append([p_seed]+i)
    return sol

s = rev(seed[30],P,31)
```

which gives us

```
0x7d424f6a5f643030675f74315f4431645f555f7730775f307b313230324857
b'WH2021{0_w0w_U_d1D_1t_g00d_jOB}\x00'
0xd9fcc53833ad35366b8345a3e3d24894b1b1cc124d3f43514ffe92d2175216a6
b'\xa6\x16R\x17\xd2\x92\xfeOQC?M\x12\xcc\xb1\xb1\x94H\xd2\xe3\xa3E\x83k65\xad38\xc5\xfc\xd9'
```

and here we see our second flag!

Solution script is located at [solve.sage](solve.sage)

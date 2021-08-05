from pwn import *

opt = [1,1,10^100]
pls = Primes()[:1000]
while True:
    p = random_prime(2^128)
    if len(p.bits())==128 and is_prime(2*p+1):
        break
q = 2*p+1

Fp = GF(p)
Fq = GF(q)

def map(P):
    return P[0]/P[1]

r = remote("01.cr.yp.toc.tf",29010)

r.sendline(b"C")
r.sendline(str(p).encode())
r.sendline(b"A")
r.sendline(f"{p*q},{p*q}".encode())
r.sendline(b"S")
r.recvuntil(b"| P = (")
P = map([Fp(i) for i in r.recvuntil(b")")[:-1].split(b",")])
r.recvuntil(b"| k*P = (")
kP = map([Fp(i) for i in r.recvuntil(b")")[:-1].split(b",")])
r.recvuntil(b"| Q = (")
Q = map([Fq(i) for i in r.recvuntil(b")")[:-1].split(b",")])
r.recvuntil(b"| l*Q = (")
lQ = map([Fq(i) for i in r.recvuntil(b")")[:-1].split(b",")])
r.sendline(f"{kP/P},{lQ/Q}")
r.interactive()

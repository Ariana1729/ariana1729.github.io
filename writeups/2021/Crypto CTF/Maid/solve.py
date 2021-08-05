from gmpy2 import gcd,invert
from pwn import *
from random import randint

r = remote("04.cr.yp.toc.tf" ,38010)

nbits = 1024

r.sendlineafter("[Q]uit","E")
t = 2**(3*nbits/2)
r.sendline(str(t))
r.recvuntil("encrypt(msg, pubkey) = ")
p2q = t*t-int(r.recvline())
while p2q % 2 == 0:
    p2q = p2q/2
for i in range(10):
    r.sendlineafter("[Q]uit","E")
    t = 2**(3*nbits/2)-randint(1,100000)
    r.sendline(str(t))
    r.recvuntil("encrypt(msg, pubkey) = ")
    p2q = gcd(p2q,t*t-int(r.recvline()))

r.sendlineafter("[Q]uit","D")
r.sendline("-1")
r.recvuntil("decrypt(enc, privkey) = ")
p = gcd(p2q,pow(int(r.recvline()),2,p2q)-1)
q = p2q/p/p

r.sendlineafter("[Q]uit","S")
r.recvuntil("| enc = ")
c = int(r.recvline())
d = invert(65537,(p-1)*(q-1))
m = pow(c,d,p*q)
print(hex(m)[2:].decode("hex"))

r.close()

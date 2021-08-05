from gmpy2 import *
from Crypto.Util.number import *
from pwn import *

r = remote("03.cr.yp.toc.tf",25010)
r.sendline("S")
r.recvuntil("p = ")
p = int(r.recvline())
r.recvuntil("r = ")
rr = int(r.recvline())
r.sendline("P")
r.recvuntil("pubkey = [")
pubkey = [int(i) for i in r.recvline().strip()[:-1].split(b",")]
r.sendline("E")
r.recvuntil('for "')
msg = r.recvuntil('"')[:-1]
r.recvuntil("signature = [")
sig = [int(i) for i in r.recvline().strip()[:-1].split(b",")]

l = len(msg) // 4
M = [bytes_to_long(msg[4*i:4*(i+1)]) for i in range(l)]
q = int(next_prime(max(M)))
secret = [invert(M[i],q)*sig[i] % q for i in range(l)]

U = [i+j for i,j in zip(pubkey,secret)]

while True:
    if (U[0]*rr%p)>>32 == U[1]>>32:
        break
    U[0] += q
for i in range(4):
    U[i+1] = U[i]*rr%p

d = 32
V = [int(bin(u)[2:][:-d] + '0' * d, 2) for u in U]
S = [int(bin(u)[2:][-d:], 2) for u in U]
privkey, pubkey = S, V

r.sendline("F")
r.recvuntil("ke example: ")
msg = r.recvline().strip()
l = len(msg) // 4
M = [bytes_to_long(msg[4*i:4*(i+1)]) for i in range(l)]
q = int(next_prime(max(M)))
sign = [M[i]*privkey[i] % q for i in range(l)]
r.sendline(",".join(str(i) for i in sign))
r.interactive()

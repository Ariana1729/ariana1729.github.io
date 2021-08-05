from pwn import *

'''
opt = [1,1,10^100]
pls = Primes()[1000:2000]
while opt[-1] > 10^10:
    d = 1
    while d<2^150:
        d *= choice(pls)
    p = (2^159//d+1)*d+1
    while len(p.bits())<161:
        p+=d
        if is_prime(p):
            for i in range(1,2023):
                if is_prime(p+i):
                    if factor(p+i-1)[-1][0] < opt[-1]:
                        opt = [p,p+i,factor(p+i-1)[-1][0]]
                        print(opt)
'''

opt = [775782590282368506469183149039276726730927594409, 775782590282368506469183149039276726730927596223, 322840879]

p,q,_ = opt
Fp = GF(p)
Fq = GF(q)
a = -27
b = 54
a1 = ",".join([str(i) for i in [a%p,b%p,p]])
a2 = ",".join([str(i) for i in [a%q,b%q,q]])

def map(x,y):
    return (y+3*(x-3))/(y-3*(x-3))

r = remote("07.cr.yp.toc.tf",10010)
r.sendline("S")
r.sendline(a1)
r.sendline(a2)
r.recvuntil(b"G is on first  ECC and G = {(")
Gx = Fp(r.recvuntil(b", ")[:-2])
Gy = Fp(r.recvuntil(b")}")[:-2])
r.recvuntil(b"H is on second ECC and H = {(")
Hx = Fq(r.recvuntil(b", ")[:-2])
Hy = Fq(r.recvuntil(b")}")[:-2])
r.recvuntil(b"r * G = {(")
rGx = Fp(r.recvuntil(b", ")[:-2])
rGy = Fp(r.recvuntil(b")}")[:-2])
r.recvuntil(b"s * H = {(")
sHx = Fq(r.recvuntil(b", ")[:-2])
sHy = Fq(r.recvuntil(b")}")[:-2])

G = map(Gx,Gy)
rG = map(rGx,rGy)
rr = rG.log(G)
H = map(Hx,Hy)
sH = map(sHx,sHy)
s = sH.log(H)
# just a sanity check, sometimes the order may be less then we may not get flag
print(G.multiplicative_order(),H.multiplicative_order())
print(p-1,q-1)
r.sendline(f"{rr},{s}")
r.interactive()

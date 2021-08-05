from pwn import *

r = remote("05.cr.yp.toc.tf",14010)

r.sendline("G")
r.recvuntil("Parameters = (")
n,f,v = [int(i) for i in r.recvuntil(")")[:-1].split(b",")]

m1 = 2
cm1 = (pow(m1,f,n*n)-1)//n
m2 = 3
cm2 = (pow(m2,f,n*n)-1)//n
k = (cm1-cm2)*pow(f,-1,n)*m2 %n
m2 += k*n

r.sendline("R")
r.sendline(f"{m1},{m2}")
r.interactive()

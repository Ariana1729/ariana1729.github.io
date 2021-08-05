from pwn import *

r = remote("01.cr.yp.toc.tf",27010)
r.sendline("G")
r.recvuntil("| encrypt(flag) = ")
s1 = r.recvline()[:-1].decode("hex")
s2 = "A"*len(s1)
r.sendline("T")
r.sendline(s2)
r.recvuntil("| enc = ")
s3 = r.recvline()[:-1].decode("hex")[:len(s1)]
print(xor(xor(s1,s2),s3))

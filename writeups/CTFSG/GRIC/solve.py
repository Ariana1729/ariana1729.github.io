from pwn import *

def get_checksum(p,n):
    n = "".join(str(i) for i in n)
    p.sendline("G")
    p.sendline("G"+n)
    p.recvuntil("Your GRIC is ")
    return p.recvline()[-2:-1]

p = remote("chals.ctf.sg",10101)
#p = process(["python3","server.py"])

sbox = "ABCDEFGHJKLMRTXYZ"

matrix = [[randint(0,9) for i in range(10)]+[0]*17 for _ in range(25)]
s = "["
for i in matrix:
    i[10+sbox.index(get_checksum(p,i[:10]))] = 16
    s += str(i)+","
s = s[:-1]+"]"

f = open("matrix","w")
f.write(s)
f.close()

ker = process(["sage","ker.sage"])
sol = eval(ker.readline())
ker.close()
c = sol[:10]
print "Constants",c
n_sbox = [None]*17
for i in range(17):
    n_sbox[sol[10+i]]=sbox[i]
sbox = n_sbox
print "sbox",sbox

p.sendline("C")
for i in range(100):
    p.recvuntil("What is the checksum letter of G")
    chal = [int(i) for i in p.recvline()[:10]]
    ans = sbox[sum(c[i]*chal[i] for i in range(10))%17]
    print chal,ans
    p.sendline(ans)

p.interactive()

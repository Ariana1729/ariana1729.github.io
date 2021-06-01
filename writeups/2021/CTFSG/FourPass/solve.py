from pwn import *

def getsol(s,a,b,c,d):
    ans = 0
    s.sendline(str(b-1))
    s.sendline(str(d-1))
    s.recvuntil(")=")
    ans += int(s.recvline())
    s.sendline(str(a-1))
    s.sendline(str(c-1))
    s.recvuntil(")=")
    ans += int(s.recvline())
    s.sendline(str(a-1))
    s.sendline(str(d-1))
    s.recvuntil(")=")
    ans -= int(s.recvline())
    s.sendline(str(b-1))
    s.sendline(str(c-1))
    s.recvuntil(")=")
    ans -= int(s.recvline())
    return ans


solver = process("solver")
print "Waiting for solver"

for _ in range(27):
    print solver.recvline().strip()

p = remote("chals.ctf.sg",15201)
p.recvline()
a,b,c,d = [int(i) for i in p.recvline().strip().split(" ")]
print a,b,c,d
sol = getsol(solver,a,b,c,d)
print(sol)
p.sendline(str(sol))
p.sendline()
p.interactive()

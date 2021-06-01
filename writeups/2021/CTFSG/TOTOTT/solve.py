from pwn import *

p = remote("chals.ctf.sg",10201)

def query(p,n):
    n = str(n)
    p.sendline("F("+n+")")
    p.recvuntil("You queried F("+n+"), and the output is ")
    return int(p.recvline())

for _ in range(30):
    q1 = query(p,0)
    q1 = bin(q1)[2:].zfill(64)[32:]
    q2 = query(p,2**63)
    q2 = bin(q2)[2:].zfill(64)[:32]
    if q1==q2:
        p.sendline("Pseudo-Random")
    else:
        p.sendline("Truly-Random")

print("Solved stage 1")

for _ in range(30):
    q1 = query(p,0)
    q2 = query(p,1)
    if q1^q2==1:
        p.sendline("Pseudo-Random")
    else:
        p.sendline("Truly-Random")

print("Solved stage 2")

for _ in range(30):
    t = query(p,0)^query(p,1)
    for i in range(10):
        if query(p,2**i+0)^query(p,2**i+1)==t:
            p.sendline("Pseudo-Random")
            break
    else:
        p.sendline("Truly-Random")

print("Solved stage 3")

for _ in range(30):
    l = []
    for i in range(127):
        t = query(p,i)
        if t in l:
            p.sendline("Pseudo-Random")
            break
        l.append(t)
    else:
        p.sendline("Truly-Random")

print("Solved stage 4")

p.interactive()

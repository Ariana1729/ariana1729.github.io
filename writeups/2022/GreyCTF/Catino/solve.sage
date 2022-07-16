from pwn import *

def getd(r,d):
    r.recvuntil(b"Guess the number (0-9)")
    r.sendline(d)
    return r.recvline()[-2:-1]

r = remote("challs.nusgreyhats.org",10520)
print(r.recvuntil(b"Generating random numbers").decode())
t = b""
for i in range(4900):
    if i%100==0 and i:
        print(f"Next 100 digits of t:{t[-100:]}")
        print(i)
    t += getd(r,"0")
print(f"Last 100 digits of t:{t[-100:]}")
print(i)
st = t
t = N(int(t)/10^len(t),digits=len(t)+20)
l = t.algebraic_dependency(4).list()
n = (l[3]/4)^4-l[0]
n /= 10^400
print(f"Found n: {n}")
s = n^(1/4)
s = s-floor(s)
s = s.numerical_approx(digits=5400)
s = s.str().split(".")[1][100:]
for i in range(4900,5000):
    getd(r,s[i])
r.interactive()


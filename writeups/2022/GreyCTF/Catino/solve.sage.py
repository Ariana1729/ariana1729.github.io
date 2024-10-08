

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_10520 = Integer(10520); _sage_const_4900 = Integer(4900); _sage_const_100 = Integer(100); _sage_const_0 = Integer(0); _sage_const_10 = Integer(10); _sage_const_20 = Integer(20); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_400 = Integer(400); _sage_const_5400 = Integer(5400); _sage_const_5000 = Integer(5000)
from pwn import *

def getd(r,d):
    r.recvuntil(b"Guess the number (0-9)")
    r.sendline(d)
    return r.recvline()[-_sage_const_2 :-_sage_const_1 ]

r = remote("challs.nusgreyhats.org",_sage_const_10520 )
print(r.recvuntil(b"Generating random numbers").decode())
t = b""
for i in range(_sage_const_4900 ):
    if i%_sage_const_100 ==_sage_const_0 :
        print(f"Next 100 digits of t:{t[-_sage_const_100 :]}")
        print(i)
    t += getd(r,"0")
print(f"Last 100 digits of t:{t[-_sage_const_100 :]}")
print(i)
st = t
t = N(int(t)/_sage_const_10 **len(t),digits=len(t)+_sage_const_20 )
l = t.algebraic_dependency(_sage_const_4 ).list()
n = (l[_sage_const_3 ]/_sage_const_4 )**_sage_const_4 -l[_sage_const_0 ]
n /= _sage_const_10 **_sage_const_400 
print(f"Found n: {n}")
s = n**(_sage_const_1 /_sage_const_4 )
s = s-floor(s)
s = s.numerical_approx(digits=_sage_const_5400 )
s = s.str().split(".")[_sage_const_1 ][_sage_const_100 :]
assert s[:_sage_const_4900 ]==st.decode()
for i in range(_sage_const_4900 ,_sage_const_5000 ):
    getd(r,s[i])
r.interactive()



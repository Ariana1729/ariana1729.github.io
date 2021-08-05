from pwn import *

r = remote("07.cr.yp.toc.tf",10101)

def inv_l(n):
    f = factor(n)
    rf = f
    invn = 1
    while rf != factor(1):
        pls = [prod(i) for i in subsets([factor(i)^j for i,j in rf])]
        pls[0] = factor(1)
        pls.sort(key=lambda x:-x.prod())
        for pf in pls:
            div = [prod(factor(p)^e for p,e in i) for i in cartesian_product([[(i[0],j) for j in range(i[1]+1)] for i in f/pf])]
            div[0] = factor(1)
            div.sort(key=lambda x:x.prod())
            for i in div:
                if is_prime(i*pf+1):
                    invn *= i*pf+1
                    rf = rf/pf
                    break
            else:
                continue
            break
    return invn

r.recvuntil(b"carmichael_lambda(n) = ")
while True:
    try:
        print(r.recvuntil(b"carmichael_lambda(n) = "))
    except:
        r.interactive()
    n = int(r.recvline()[:-3])
    print(n)
    r.sendline(str(inv_l(n)))
    print(inv_l(n))

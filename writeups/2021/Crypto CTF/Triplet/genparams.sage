while True:
    inc = randint(1,2^160)
    pls = []
    p = 1
    while len(pls)<3:
        p += inc
        if is_prime(p):
            pls.append(p)
    phip = (pls[0]-1)*lcm([i-1 for i in pls])
    facts = flatten([[i]*j for i,j in list(factor(phip+1))])
    d = 1
    e = phip+1
    B = (pls[0]-1)^2
    while e>B or d>B:
        d *= facts[-1]
        e /= facts[-1]
        facts = facts[:-1]
        if len(facts)==0:
            break
    if e<B and d<B:
        break
p,q,r = pls
print(f"p = {p}")
print(f"q = {q}")
print(f"r = {r}")
print(f"e = {e}")
print(f"d = {d}")

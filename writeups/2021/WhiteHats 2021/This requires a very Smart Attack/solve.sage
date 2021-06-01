def launch_attack(P, Q, p, a, b):
    E = P.curve()
    Eqp = EllipticCurve(Qp(p, 8), [a,b])
    P_Qps = Eqp.lift_x(ZZ(P.xy()[0]), all=True)
    for P_Qp in P_Qps:
        if GF(p)(P_Qp.xy()[1]) == P.xy()[1]:
            break
    Q_Qps = Eqp.lift_x(ZZ(Q.xy()[0]), all=True)
    for Q_Qp in Q_Qps:
        if GF(p)(Q_Qp.xy()[1]) == Q.xy()[1]:
            break
    p_times_P = p * P_Qp
    p_times_Q = p * Q_Qp
    x_P, y_P = p_times_P.xy()
    x_Q, y_Q = p_times_Q.xy()
    phi_P = -(x_P / y_P)
    phi_Q = -(x_Q / y_Q)
    k = phi_Q / phi_P
    return ZZ(k) % p

p = 0xda7a07879e0c99669beaa51815318cc616112171c46fbab08079c40447845efd
A = 0x5b8d8423a1a89b3b6b2b35797cb92e6721156696f62ff5fe0302dec3ac4a7001
B = 0x71d1c62ae615f59a60b8721bb9580cfd0e4316e2c690a7eac09e0c9182c083b6

E = EllipticCurve(GF(p),[A,B])

P = E(0xc0ca3e6a02ebd831c8f70f0d80f754b53dc5e238e7111bf272ab09d477531c7e,0x373b5380694320ae35b92615abb87269f2024a19c119ac270ce7b84b2d8c48e8)
Q = E(0x6e008f822af34da1bd489fdfaa12d763f7bc222b9ab7b978a6bbd3d0e656fcee,0x571315163c70f69fbd65dd212bea1b9584d138896210aeb0f0fced2e95307c6d)

xor = lambda A,B:[i^^j for i,j in zip(A,B)]

enc = open("secret.enc","rb").read()

blk30 = open("secret-960_992.txt","rb").read()

# we know the 30th block

sec = lambda s:int((s*Q).xy()[0])
seed = [None]*(len(enc)//32+1)
sec30 = 0xb4a594ad888dfc431ae16437ec0d894a3cac840d151962addf139c4b1f63ec73
#xor(blk30,enc[30*32:31*32])

# get seed
sQ = E.lift_x(sec30,all=True)[0]

s = launch_attack(Q,sQ,p,A,B)
seed[30] = s
for i in range(31,len(seed)):
    seed[i] = ZZ((seed[i-1]*P).xy()[0])
    t = xor(sec(ZZ(seed[i])).to_bytes(32, 'big'),enc[i*32:(i+1)*32])
    print("".join(chr(i) for i in t))
print(seed)

def func_gen(seed,P,n):
    if n == 0:
        print(hex(seed)) # in case garbage
        print(int.to_bytes(int(seed),length=32,byteorder="little"))
        return [[]]
    sP = E.lift_x(seed,all=True)
    if len(sP) == 0:
        return []
    sol = []
    p_seed = launch_attack(P,sP[0],p,A,B)
    t = xor(sec(ZZ(p_seed)).to_bytes(32, 'big'),enc[(n-2)*32:(n-1)*32])
    if not all(0<i<0x80 for i in t):
        return []
    print("".join(chr(i) for i in t))
    for i in func_gen(p_seed,P,n-1):
        if [p_seed]+i not in sol:
            sol.append([p_seed]+i)
    p_seed = ZZ((-p_seed) % p)
    for i in func_gen(p_seed,P,n-1):
        if [p_seed]+i not in sol:
            sol.append([p_seed]+i)
    return sol

s = func_gen(seed[30],P,31)
f = open("dump","w")

def launch_attack(P, Q, p):
    E = P.curve()
    Eqp = EllipticCurve(Qp(p, 8), [ZZ(t) for t in E.a_invariants()])

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

n = 43216667049953267964807040003094883441902922285265979216983383601881964164181
p = 227316839687407660649258155239617355023
q = 190116434441822299465355144611018694747
U = 18230294945466842193029464818176109628473414458693455272527849780121431872221
V = 13100009444194791894141652184719316024656527520759416974806280188465496030062
W = 5543957019331266247602346710470760261172306141315670694208966786894467019982
G = (6907136022576092896571634972837671088049787669883537619895520267229978111036,35183770197918519490131925119869132666355991678945374923783026655753112300226)
sG = (14307615146512108428634858855432876073550684773654843931813155864728883306026,4017273397399838235912099970694615152686460424982458188724369340441833733921)

Ep = EllipticCurve(GF(p), [0, U, 0, V, W])
Eq = EllipticCurve(GF(q), [0, U, 0, V, W])
Gp = Ep(G)
sGp = Ep(sG)
Gq = Eq(G)
sGq = Eq(sG)

sq = launch_attack(Gq,sGq,q)
assert sq*Gq==sGq

g = q*Gp
h = sGp-sq*Gp

Ep2 = Ep.base_extend(GF(p^2))
g2 = Ep2(g)
h2 = Ep2(h)
Rp2 = Ep2.random_point()
hp = h2.tate_pairing(Rp2, Ep.order(), 2)
gp = g2.tate_pairing(Rp2, Ep.order(), 2)

# we discard the largest factor

P = factor(Ep.order())[-1][0]
x = (hp^P).log(gp^P)
assert x*g==h

s = sq+x*q
print(bytes.fromhex(s.hex()))

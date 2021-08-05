def getcd(P,Q):
    Px,Py = P
    Qx,Qy = Q
    d = (Px^2+Py^2-Qx^2-Qy^2)/(-Py^2*Qx^2*Qy^2+Px^2*(-Qx^2*Qy^2+Py^2*(Qx^2+Qy^2)))
    c = (Px^2+Py^2)/(1+d*Px^2*Py^2)
    return c,d

P = (398011447251267732058427934569710020713094, 548950454294712661054528329798266699762662)
Q = (139255151342889674616838168412769112246165, 649791718379009629228240558980851356197207)
sP = (730393937659426993430595540476247076383331, 461597565155009635099537158476419433012710)
tQ = (500532897653416664117493978883484252869079, 620853965501593867437705135137758828401933)

c = []
d = []
for i,j in [[P,Q],[P,sP],[P,tQ],[Q,sP],[Q,tQ],[sP,tQ]]:
    a,b = getcd(i,j)
    c.append((a.numer(),a.denom()))
    d.append((b.numer(),b.denom()))

p = c[0][0]*c[1][1]-c[1][0]*c[0][1]
for i in range(len(c)):
    for j in range(len(c)-i-1):
        p = gcd(c[i][0]*c[j][1]-c[j][0]*c[i][1],p)
for i in range(len(d)):
    for j in range(len(d)-i-1):
        p = gcd(d[i][0]*d[j][1]-d[j][0]*d[i][1],p)
p = factor(p)[-1][0]

FF = GF(p)
c = -FF(c[0][0]/c[0][1]).sqrt()
d = FF(d[0][0]/d[0][1])
for i,j in [[P,Q],[P,sP],[P,tQ],[Q,sP],[Q,tQ],[sP,tQ]]:
    a,b = getcd(i,j)
    assert FF(a)==c^2
    assert FF(b)==d

for i in [P,Q,sP,tQ]:
	u, v = i
	assert(u^2 + v^2 - c^2*(1 + d * u^2*v^2)) % p == 0

def tocurve(pp):
    u,v = pp
    x = (c+v)/(c-v)
    y = 2*c*(c+v)/(u*(c-v))
    x *= (1-c^4*d)
    y *= (1-c^4*d)
    x += (2*(c^4*d + 1))/3
    return (x,y)

a = -(9*c^8*d^2+126*c^4*d+9)/27
b = -(2*c^12*d^3-66*c^8*d^2-66*c^4*d+2)/27
E = EllipticCurve(FF,[a,b])
P = E(tocurve(P))
Q = E(tocurve(Q))
sP = E(tocurve(sP))
tQ = E(tocurve(tQ))
print(bytes.fromhex(P.discrete_log(sP).hex()))
print(bytes.fromhex(Q.discrete_log(tQ).hex()))

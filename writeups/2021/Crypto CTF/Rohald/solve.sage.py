

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_398011447251267732058427934569710020713094 = Integer(398011447251267732058427934569710020713094); _sage_const_548950454294712661054528329798266699762662 = Integer(548950454294712661054528329798266699762662); _sage_const_139255151342889674616838168412769112246165 = Integer(139255151342889674616838168412769112246165); _sage_const_649791718379009629228240558980851356197207 = Integer(649791718379009629228240558980851356197207); _sage_const_730393937659426993430595540476247076383331 = Integer(730393937659426993430595540476247076383331); _sage_const_461597565155009635099537158476419433012710 = Integer(461597565155009635099537158476419433012710); _sage_const_500532897653416664117493978883484252869079 = Integer(500532897653416664117493978883484252869079); _sage_const_620853965501593867437705135137758828401933 = Integer(620853965501593867437705135137758828401933); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_3 = Integer(3); _sage_const_9 = Integer(9); _sage_const_8 = Integer(8); _sage_const_126 = Integer(126); _sage_const_27 = Integer(27); _sage_const_12 = Integer(12); _sage_const_66 = Integer(66)
def getcd(P,Q):
    Px,Py = P
    Qx,Qy = Q
    d = (Px**_sage_const_2 +Py**_sage_const_2 -Qx**_sage_const_2 -Qy**_sage_const_2 )/(-Py**_sage_const_2 *Qx**_sage_const_2 *Qy**_sage_const_2 +Px**_sage_const_2 *(-Qx**_sage_const_2 *Qy**_sage_const_2 +Py**_sage_const_2 *(Qx**_sage_const_2 +Qy**_sage_const_2 )))
    c = (Px**_sage_const_2 +Py**_sage_const_2 )/(_sage_const_1 +d*Px**_sage_const_2 *Py**_sage_const_2 )
    return c,d

P = (_sage_const_398011447251267732058427934569710020713094 , _sage_const_548950454294712661054528329798266699762662 )
Q = (_sage_const_139255151342889674616838168412769112246165 , _sage_const_649791718379009629228240558980851356197207 )
sP = (_sage_const_730393937659426993430595540476247076383331 , _sage_const_461597565155009635099537158476419433012710 )
tQ = (_sage_const_500532897653416664117493978883484252869079 , _sage_const_620853965501593867437705135137758828401933 )

c = []
d = []
for i,j in [[P,Q],[P,sP],[P,tQ],[Q,sP],[Q,tQ],[sP,tQ]]:
    a,b = getcd(i,j)
    c.append((a.numer(),a.denom()))
    d.append((b.numer(),b.denom()))

p = c[_sage_const_0 ][_sage_const_0 ]*c[_sage_const_1 ][_sage_const_1 ]-c[_sage_const_1 ][_sage_const_0 ]*c[_sage_const_0 ][_sage_const_1 ]
for i in range(len(c)):
    for j in range(len(c)-i-_sage_const_1 ):
        p = gcd(c[i][_sage_const_0 ]*c[j][_sage_const_1 ]-c[j][_sage_const_0 ]*c[i][_sage_const_1 ],p)
for i in range(len(d)):
    for j in range(len(d)-i-_sage_const_1 ):
        p = gcd(d[i][_sage_const_0 ]*d[j][_sage_const_1 ]-d[j][_sage_const_0 ]*d[i][_sage_const_1 ],p)
p = factor(p)[-_sage_const_1 ][_sage_const_0 ]

FF = GF(p)
c = -FF(c[_sage_const_0 ][_sage_const_0 ]/c[_sage_const_0 ][_sage_const_1 ]).sqrt()
d = FF(d[_sage_const_0 ][_sage_const_0 ]/d[_sage_const_0 ][_sage_const_1 ])
for i,j in [[P,Q],[P,sP],[P,tQ],[Q,sP],[Q,tQ],[sP,tQ]]:
    a,b = getcd(i,j)
    assert FF(a)==c**_sage_const_2 
    assert FF(b)==d

for i in [P,Q,sP,tQ]:
	u, v = i
	assert(u**_sage_const_2  + v**_sage_const_2  - c**_sage_const_2 *(_sage_const_1  + d * u**_sage_const_2 *v**_sage_const_2 )) % p == _sage_const_0 

print(c,d,p)

def tocurve(pp):
    u,v = pp
    x = (c+v)/(c-v)
    y = _sage_const_2 *c*(c+v)/(u*(c-v))
    x *= (_sage_const_1 -c**_sage_const_4 *d)
    y *= (_sage_const_1 -c**_sage_const_4 *d)
    x += (_sage_const_2 *(c**_sage_const_4 *d + _sage_const_1 ))/_sage_const_3 
    return (x,y)

a = -(_sage_const_9 *c**_sage_const_8 *d**_sage_const_2 +_sage_const_126 *c**_sage_const_4 *d+_sage_const_9 )/_sage_const_27 
b = -(_sage_const_2 *c**_sage_const_12 *d**_sage_const_3 -_sage_const_66 *c**_sage_const_8 *d**_sage_const_2 -_sage_const_66 *c**_sage_const_4 *d+_sage_const_2 )/_sage_const_27 
E = EllipticCurve(FF,[a,b])
P = E(tocurve(P))
Q = E(tocurve(Q))
sP = E(tocurve(sP))
tQ = E(tocurve(tQ))
print(bytes.fromhex(P.discrete_log(sP).hex()))
print(bytes.fromhex(Q.discrete_log(tQ).hex()))


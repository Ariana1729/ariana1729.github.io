PQ = (540660810777215925744546848899656347269220877882, 102385886258464739091823423239617164469644309399)
Q2 = (814107817937473043563607662608397956822280643025, 961531436304505096581595159128436662629537620355)
P2 = (5565164868721370436896101492497307801898270333, 496921328106062528508026412328171886461223562143)

pts = [PQ,Q2,P2]

M = []
x,y = PQ
M.append([x*(y**2 - 1),y*(x**2 - 1)])
for x,y in [Q2,P2]:
    M.append([x*(y**2 - 1),y*(x**2 - 1)])

p = Matrix([M[0],M[1]]).det()
p = gcd(p,Matrix([M[0],M[2]]).det())
p = gcd(p,Matrix([M[1],M[2]]).det())

p = factor(p)[-1][0]
FF = GF(p)
a = FF(M[0][1])
b = FF(M[0][0])

QQp.<x,y,z>=PolynomialRing(QQ)
r_pol = QQ(a)*x*(y**2 - 1) - QQ(b)*y*(x**2 - 1)
h_pol = r_pol.homogenize(var=z)
phi = EllipticCurve_from_cubic(h_pol)
E = phi.codomain().change_ring(FF)
tocurve = lambda a,b:E([i.change_ring(FF).subs(x=a,y=b,z=1) for i in phi.defining_polynomials()])
fromcurve = lambda a,b: (lambda P:[i/P[-1] for i in P[:-1]])\
    ([i.change_ring(FF).subs(x=a,y=b,z=1) for i in phi.inverse().defining_polynomials()])

PQ = tocurve(*PQ)
P2 = tocurve(*P2)
Q2 = tocurve(*Q2)

print([bytes.fromhex(hex(fromcurve(*i.xy())[0])[2:]) for i in P2.division_points(2)])
print([bytes.fromhex(hex(fromcurve(*i.xy())[0])[2:]) for i in Q2.division_points(2)])

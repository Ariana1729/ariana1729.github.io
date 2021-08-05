

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_48790321481981070334284834897002743904143367742567080121139875503627677163558938442363151365001170923856543352995009198916999044114034490190573783771904020525587752191210344256704686085230514048180152780013748635642271859330908866389413727451104623973255339543797167920503564005931662152602543251766255090842659435974220819895436577204154690210899973842334999175452720629152039181296261452873185143203984819655252786655755387428741502392505402920556814585424516239256655975181009 = Integer(48790321481981070334284834897002743904143367742567080121139875503627677163558938442363151365001170923856543352995009198916999044114034490190573783771904020525587752191210344256704686085230514048180152780013748635642271859330908866389413727451104623973255339543797167920503564005931662152602543251766255090842659435974220819895436577204154690210899973842334999175452720629152039181296261452873185143203984819655252786655755387428741502392505402920556814585424516239256655975181009); _sage_const_14631667335665376436840829964208352592651640426073578145070933715959789971380009994599228441748977871671891122780871174585035107716073801876075537824911946177667748022294940252232874085867015283835699627140037360866815484198487657307973080528934669763321149163146222720745301051643570903526702386861550873974220860941488324946388489501970762170927237645397125403189863229303743865435714328534902839262771017996292025035300502112811380090440713136701311095838411721435477641677265625 = Integer(14631667335665376436840829964208352592651640426073578145070933715959789971380009994599228441748977871671891122780871174585035107716073801876075537824911946177667748022294940252232874085867015283835699627140037360866815484198487657307973080528934669763321149163146222720745301051643570903526702386861550873974220860941488324946388489501970762170927237645397125403189863229303743865435714328534902839262771017996292025035300502112811380090440713136701311095838411721435477641677265625); _sage_const_582 = Integer(582); _sage_const_25 = Integer(25); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_8 = Integer(8); _sage_const_7 = Integer(7); _sage_const_65537 = Integer(65537)
c = _sage_const_48790321481981070334284834897002743904143367742567080121139875503627677163558938442363151365001170923856543352995009198916999044114034490190573783771904020525587752191210344256704686085230514048180152780013748635642271859330908866389413727451104623973255339543797167920503564005931662152602543251766255090842659435974220819895436577204154690210899973842334999175452720629152039181296261452873185143203984819655252786655755387428741502392505402920556814585424516239256655975181009 

t = _sage_const_14631667335665376436840829964208352592651640426073578145070933715959789971380009994599228441748977871671891122780871174585035107716073801876075537824911946177667748022294940252232874085867015283835699627140037360866815484198487657307973080528934669763321149163146222720745301051643570903526702386861550873974220860941488324946388489501970762170927237645397125403189863229303743865435714328534902839262771017996292025035300502112811380090440713136701311095838411721435477641677265625 

po = _sage_const_582 
qo = _sage_const_25 

K = QQ[sqrt(-_sage_const_1 )]
factors = K.factor(t)

gens = []
for i in range(_sage_const_0 ,len(factors),_sage_const_2 ):
    gens.append([factors[i][_sage_const_0 ].gens_reduced()[_sage_const_0 ],factors[i+_sage_const_1 ][_sage_const_0 ].gens_reduced()[_sage_const_0 ]])

for e in cartesian_product([range(_sage_const_8 )]*len(gens),flatten=True):
    a,b = prod(i[_sage_const_0 ]**j*i[_sage_const_1 ]**(_sage_const_7 -j) for i,j in zip(gens,e))
    a = abs(a)
    if is_prime(ZZ(a+po)):
        a = a+po
        b = abs(b) + qo
        e = _sage_const_65537 
        d = _sage_const_1 /e % lcm(a-_sage_const_1 ,b-_sage_const_1 )
        print(bytes.fromhex(ZZ(pow(c,d,a*b)).hex()))

---
layout: writeup
ctf: Crypto CTF 2021
chal: RSAphantine
category: crypto
flag: CCTF{y0Ur_jO8_C4l13D_Diophantine_An4LySI5!}
points: 142
solves: 29
---

> RSA and solving equations, but should be a real mathematician to solve it with a diophantine equation?

Files given:
 - [output.txt](output.txt)

```python
2*z**5 - x**3 + y*z = 47769864706750161581152919266942014884728504309791272300873440765010405681123224050402253883248571746202060439521835359010439155922618613520747411963822349374260144229698759495359592287331083229572369186844312169397998958687629858407857496154424105344376591742814310010312178029414792153520127354594349356721
x**4 + y**5 + x*y*z = 89701863794494741579279495149280970802005356650985500935516314994149482802770873012891936617235883383779949043375656934782512958529863426837860653654512392603575042842591799236152988759047643602681210429449595866940656449163014827637584123867198437888098961323599436457342203222948370386342070941174587735051
y**6 + 2*z**5 + z*y = 47769864706750161581152919266942014884728504309791272300873440765010405681123224050402253883248571746202060439521835359010439155922618613609786612391835856376321085593999733543104760294208916442207908167085574197779179315081994735796390000652436258333943257231020011932605906567086908226693333446521506911058
p = nextPrime(x**2 + z**2 + y**2 << 76)
q = nextPrime(z**2 + y**3 - y*x*z ^ 67)
n, e = p * q, 31337
m = bytes_to_long(FLAG)
c = pow(m, e, n)
c = 486675922771716096231737399040548486325658137529857293201278143425470143429646265649376948017991651364539656238516890519597468182912015548139675971112490154510727743335620826075143903361868438931223801236515950567326769413127995861265368340866053590373839051019268657129382281794222269715218496547178894867320406378387056032984394810093686367691759705672
```

Looking at these equations, my first instinct was to throw into mathematica and go for lunch. Mathematica eventually gave the following output:

```
In[1]:= c1=47769864706750161581152919266942014884728504309791272300873440765010405681123224050402253883248571746202060439521835359010439155922618613520747411963822349374260144229698759495359592287331083229572369186844312169397998958687629858407857496154424105344376591742814310010312178029414792153520127354594349356721;
c2=89701863794494741579279495149280970802005356650985500935516314994149482802770873012891936617235883383779949043375656934782512958529863426837860653654512392603575042842591799236152988759047643602681210429449595866940656449163014827637584123867198437888098961323599436457342203222948370386342070941174587735051;
c3=47769864706750161581152919266942014884728504309791272300873440765010405681123224050402253883248571746202060439521835359010439155922618613609786612391835856376321085593999733543104760294208916442207908167085574197779179315081994735796390000652436258333943257231020011932605906567086908226693333446521506911058;
FindInstance[{2z^5-x^3+y z==c1,x^4+y^5+x y z==c2,y^6+2z^5+z y==c3},{x,y,z},Integers]
Out[4]= {{x->-97319611529501810510904538298668204056042623868316550440771307534558768612892,y->311960913464334198969500852124413736815,z->29896806674955692028025365368202021035722548934827533460297089}}
```

which makes it very easy to solve this challenge.

Solution at [sol.nb](sol.nb) and [solve.sage](solve.sage)
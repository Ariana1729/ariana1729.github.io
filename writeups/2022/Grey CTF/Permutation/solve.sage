with open("out.txt","r") as f:
    d = [i.split(" = ")[1] for i in f.read().split("\n")]
g = eval(d[0])
A = eval(d[1])
B = eval(d[2])
c = bytes.fromhex(d[3])

# sage permutation
g = PermutationGroupElement(Permutation([i+1 for i in g]))
A = PermutationGroupElement(Permutation([i+1 for i in A]))
B = PermutationGroupElement(Permutation([i+1 for i in B]))

# very bad dlp implementation
o = g.order()
a = []
b = []
for p,e in factor(o):
    tg = g^(ZZ(o/p^e))
    tA = A^(ZZ(o/p^e))
    tB = B^(ZZ(o/p^e))
    for i in range(p^e):
        if tg^i==tA:
            a.append([i,p^e])
    for i in range(p^e):
        if tg^i==tB:
            b.append([i,p^e])
a = crt([i[0] for i in a],[i[1] for i in a])
b = crt([i[0] for i in b],[i[1] for i in b])
assert g^a == A
assert g^b == B

# solve

from hashlib import shake_256

key = ",".join(str(i-1) for i in Permutation(B^a))
otp = shake_256(key.encode()).digest(len(c))
print(bytes([ x ^^ y for x, y in zip(otp, c)]))

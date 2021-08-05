l = 256

g = open("g.enc","rb").read()
h = open("h.enc","rb").read()

def tobase(n,b=5):
    r = []
    while n>0:
        r.append(n%5)
        n = n//5
    return r[::-1]

g = int(g.hex(),16)
h = int(h.hex(),16)

g = tobase(g)
h = tobase(h)

c = 67

for i in range(len(g)-c-1,-1,-1):
    g[i] -= g[i+c]

for i in range(len(h)-c-1,-1,-1):
    h[i] -= h[i+c]

g = g[c:]
h = h[c:]

for i in range(len(g)-2,-1,-1):
    g[i] -= g[i+1]

for i in range(len(h)-2,-1,-1):
    h[i] -= h[i+1]

print(bytes.fromhex(hex(int("".join(str(i) for i in g[:l]),2))[2:]))

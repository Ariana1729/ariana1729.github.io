from string import printable

p = 8443

W = eval(open("output.txt","r").read())

f = ""
for j in range(len(W)):
    t = {i:[] for i in range(p)}
    for ii in printable:
        for jj in range(127):
            t[ord(ii)*(j+1)*jj%p].append(ii)
    a = [i for i in printable]
    for i in range(len(W)):
        a = [l for l in a if l in t[W[i][j]]]
    f += a[0]
print(f)

v2 = ["VGhpc0lzTm90VGhlRmxhZw==", "U01VV2hpdGVIYXRDaGFsbGVuZ2U=", "gjhU9MzCkbTNF54MXwReLkE=", "yeLGMCaRA8p8xA==", "azMtkQ//3JA=", "zMq9wKxBrbpj1PQ9WLADXJaGRq1gnwyWdUj+2A=="]
v2 = [i.decode("base-64") for i in v2]
v3 = [0x8A, 107, 97, 0x7B, 26, 43, 0x91, -20]
v3 = [i%0x100 for i in v3]
sol = ""
t = v2[2][::-1]
for i in range(len(t)):
    sol += chr(ord(t[i])^v3[i%8])
print sol.encode("base-64")

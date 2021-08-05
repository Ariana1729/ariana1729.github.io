---
layout: writeup
ctf: Crypto CTF 2021
chal: Hyper Normal
category: crypto
flag: CCTF{H0w_f1Nd_th3_4lL_3I9EnV4Lu35_iN_FiN173_Fi3lD5!???}
points: 71
solves: 69
---

> Being normal is hard these days because of Corona virus pandemic!

Files given:
 - [output.txt](output.txt)
 - [hyper_normal.py](hyper_normal.py)

```python
p = 8443

def transpose(x):
	result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
	return result

def encrypt(msg):
	l = len(msg)
	hyper = [ord(m)*(i+1) for (m, i) in zip(list(msg), range(l))]
	V, W = [], []
	for i in range(l):
		v = [0]*i + [hyper[i]] + [0]*(l - i - 1)
		V.append(v)
	random.shuffle(V)
	for _ in range(l):
		R, v = [random.randint(0, 126) for _ in range(l)], [0]*l
		for j in range(l):
			v = vsum(v, sprod(R[j], V[j]))
		W.append(v)
	random.shuffle(transpose(W))
	return W

enc = encrypt(FLAG)
print(enc)
```

We first analyse the encryption function. It starts off by setting up a diagonal matrix \\(V\\) where entries are a fixed multiple of our flag. It then shuffles around the rows of this matrix, then applies a random matrix with elements from \\(0\\) to \\(126\\) to the shuffled matrix, which makes the initial shuffling redundant. Furthermore, notice that `transpose(W)` actually does not affect the input and instead returns a transposed matrix, hence we can ignore the line before the return as it does not affect `W`. Hence, the \\(i\\)th row of the output matrix is actually just our message multipled by a bunch of small random numbers.

As \\(126<<p\\), it is a simple brute force search. We take each row and check what characters are possible and what aren't, eventually we should only be left with one possible character per row, and we can easily get our flag.

Solution at [solve.py](solve.py)

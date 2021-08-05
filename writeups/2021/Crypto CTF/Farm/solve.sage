import string, base64, math

ALPHABET = string.printable[:62] + '\\='

F = list(GF(64))

def keygen(l):
	key = [F[randint(1, 63)] for _ in range(l)] 
	key = math.prod(key) # Optimization the key length :D
	return key

def maptofarm(c):
	assert c in ALPHABET
	return F[ALPHABET.index(c)]

def mapfromfarm(c):
	assert c in F
	return ALPHABET[F.index(c)]

def encrypt(msg, key):
	m64 = base64.b64encode(msg)
	enc, pkey = '', key**5 + key**3 + key**2 + 1
	for m in m64:
		enc += ALPHABET[F.index(pkey * maptofarm(chr(m)))]
	return enc

def decrypt(enc, key):
    m = ""
    pkey = key**5 + key**3 + key**2 + 1
    if pkey == 0:
        return
    for i in enc:
        m += mapfromfarm(F[ALPHABET.index(i)]/pkey)
    for i in range(4):
        try:
            return base64.b64decode(m+"="*i)
        except:
            continue 

enc = "805c9GMYuD5RefTmabUNfS9N9YrkwbAbdZE0df91uCEytcoy9FDSbZ8Ay8jj"
for key in F:
    dec = decrypt(enc, key)
    if dec and b"CCTF{" in dec:
        print(dec)

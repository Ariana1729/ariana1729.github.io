import random
from z3 import *

KEYS = [8, 8, 24, 24]
TAPS = [96, 195, 1310720, 589824]

class lfsr():
    def __init__(self, init, mask, length):
        self.init = init
        self.mask = mask
        self.lengthmask = 2**(length+1)-1
        self.length = length

    def next(self):
        nextdata = (self.init << 1) & self.lengthmask
        i = self.init & self.mask & self.lengthmask

        output = 0
        for j in range(self.length):
            output ^= (i & 1)
            i = i >> 1

        nextdata ^= output
        self.init = nextdata
        return output

def combine(x0,x1,x2,x3):
    return ((x0^x1)&x2)|(((~x1)|x2)&x3)

init0 = BitVec('init0', 24)
init1 = BitVec('init1', 24)
init2 = BitVec('init2', 24)
init3 = BitVec('init3', 24)

l0 = lfsr(init0, TAPS[0], KEYS[0])
l1 = lfsr(init1, TAPS[1], KEYS[1])
l2 = lfsr(init2, TAPS[2], KEYS[2])
l3 = lfsr(init3, TAPS[3], KEYS[3])

s = Solver()

pt = open("decrypted.txt","rb").read().strip()
ct = open("encrypted.enc","rb").read()

known = []
for i,j in zip(pt,ct):
    known += [int(i) for i in bin(i^j)[2:].zfill(8)]

for i in range(len(known)):
    s.add(known[i] == combine(l0.next(), l1.next(), l2.next(), l3.next()))

s.check()
m = s.model()
seed0 = int(str(m[init0]))
seed1 = int(str(m[init1]))
seed2 = int(str(m[init2]))
seed3 = int(str(m[init3]))
print(seed0,seed1,seed2,seed3)

L0 = lfsr(seed0, TAPS[0], KEYS[0])
L1 = lfsr(seed1, TAPS[1], KEYS[1])
L2 = lfsr(seed2, TAPS[2], KEYS[2])
L3 = lfsr(seed3, TAPS[3], KEYS[3])

pt = ""
for i in ct:
    r = 0
    for j in range(8):
        r += combine(L0.next(), L1.next(), L2.next(), L3.next())*(2**(7-j))
    pt += chr(i^r)

print(pt)

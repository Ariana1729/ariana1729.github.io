def mulInv(n:int, q:int):  

    def extEuclid(a:int, b:int):
        s0, s1, t0, t1 = 1, 0, 0, 1
        while b > 0:
            q, r = divmod(a, b)
            a, b = b, r
            s0, s1, t0, t1 = s1, s0 - q * s1, t1, t0 - q * t1
            pass
        return s0, t0, a

    return extEuclid(n, q)[0] % q

class EC:

    'Represents an EC of the form y^2 = x^3 + ax + b'

    def __init__(self, a:int, b:int, q:int):
        
        # Check for basic ranges
        assert 0 < a < q and 0 < b < q and q > 2
        # Check for non-singularity
        assert (4 * a*a*a + 27 * b*b)  % q != 0

        self.a = a
        self.b = b
        self.q = q

    def __eq__(self, ec):

        if type(ec) != type(self):
            return False
        if self.a==ec.a and self.b==ec.b and self.q==ec.q:
            return True
        return False


class ECPoint:

    'Represents a point on an EC'
    
    def __init__(self, x:int, y:int, ec:EC):
        self.x, self.y, self.ec = x,y,ec
        assert self._isOn(), "Point is not on ec"

    def __add__(self, p):

        # Check if p is an ECPoint
        assert type(p) == type(self), "p has to be an ECPoint"
        # Check if p is on same EC
        assert self.ec == p.ec, "both p and self has to be on the same ec"

        x0,y0,ec = self.x, self.y, self.ec

        if p.isZero(): return self
        if self.isZero(): return p
        if x0 == p.x and (y0 != p.y or y0 == 0):
            return ECPoint(0, 0, ec)

        if x0 == p.x:
            l = (3 * x0*x0 + ec.a) * mulInv(2 * y0, ec.q) % ec.q
        else:
            l = (p.y - y0) * mulInv(p.x - x0, ec.q) % ec.q

        x = (l*l - x0 - p.x) % ec.q
        y = (l*(x0 - x) - y0) % ec.q

        return ECPoint(x,y,ec)

    def __mul__(self, n:int):

        r = ECPoint(0,0,self.ec)
        m2 = self
        while 0 < n:
            if n & 1 == 1:
                r += m2
            n >>= 1
            m2 += m2
        return r

    def _isOn(self):

        x,y,ec = self.x, self.y, self.ec

        if self.isZero(): return True
        l = (y*y) % ec.q
        r = ((x*x*x) + ec.a * x + ec.b) % ec.q
        return l == r

    def isZero(self):
        return self.x==0 and self.y==0
       
class Stream:

    'Represents a stream cipher'

    def __init__(self, seed:int, P:ECPoint, Q:ECPoint):

        assert P.ec == Q.ec, "both P and Q have to be on the same ec"
        self.seed = seed
        self.P = P
        self.Q = Q

    def genStream(self):
        self.seed = (self.P * self.seed).x
        return (self.Q * self.seed).x

    def encrypt(self, pt:bytes):

        nblocks = len(pt)//32 + 1
        ct = []
        for i in range(nblocks):
            r = self.genStream().to_bytes(32, 'big')
            block = pt[32*i:32*(i+1)]
            ct += [x^y for x,y in zip(block, r)]
        return bytes(ct)

    def decrypt(self, ct:bytes):
        return self.encrypt(ct)


if __name__ == "__main__":

    prime = 0xda7a07879e0c99669beaa51815318cc616112171c46fbab08079c40447845efd
    A     = 0x5b8d8423a1a89b3b6b2b35797cb92e6721156696f62ff5fe0302dec3ac4a7001
    B     = 0x71d1c62ae615f59a60b8721bb9580cfd0e4316e2c690a7eac09e0c9182c083b6

    ec = EC(A,B,prime)

    P = ECPoint(0xc0ca3e6a02ebd831c8f70f0d80f754b53dc5e238e7111bf272ab09d477531c7e,
                0x373b5380694320ae35b92615abb87269f2024a19c119ac270ce7b84b2d8c48e8,
                ec)
    Q = ECPoint(0x6e008f822af34da1bd489fdfaa12d763f7bc222b9ab7b978a6bbd3d0e656fcee,
                0x571315163c70f69fbd65dd212bea1b9584d138896210aeb0f0fced2e95307c6d,
                ec)

    flag1 = open('flag1', 'rb').read()
    flag2 = open('flag2', 'rb').read()

    assert len(flag2) < 32, "Length of flag2 is too long"
    key = int.from_bytes(flag2, "little")
    stream = Stream(key,P,Q)

    pt = open("secret.txt", "rb").read() + flag1
    ct = stream.encrypt(pt) 
    open("secret.enc", "wb").write(ct)
    open("secret-960_992.txt", "wb").write(pt[960:992])
    
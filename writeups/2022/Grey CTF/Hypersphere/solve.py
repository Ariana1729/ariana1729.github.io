from hashlib import shake_256
from pwn import *

def encrypt(msg : bytes, key : str) -> str:
    otp = shake_256(key.encode()).digest(len(msg))
    return xor(otp, msg)

def xor(a : bytes, b : bytes) -> bytes:
    return bytes([ x ^ y for x, y in zip(a, b)])

r = remote("challs.nusgreyhats.org",10521)
r.recvuntil(b"Prime : ")
p = int(r.recvline())
r.send("Y\n")
r.send(f"{p}\n")
r.send(" ".join([str(pow(-2 if i==0 else 2,-1,p)) for i in range(4)])+"\n")
r.recvuntil(b"c = ")
msg = bytes.fromhex(r.recvline().decode().strip())
r.sendline(encrypt(msg, "1, 0, 0, 0"))
r.interactive()

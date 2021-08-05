from pwn import *
from Crypto.Cipher import AES

r = remote("01.cr.yp.toc.tf", 17010)

r.sendline("G")
r.recvuntil("encrypt(flag) = ")
flag = r.recvline().strip().decode("hex")
r.sendline("T")
r.sendline("\x00"*32)
r.recvuntil("enc = ")
enc = r.recvline().strip()
l1 = len(enc.split("*")[0])
l2 = 4-l1
pt1 = enc[:l1]
pt2 = enc[32-l2:32]
r.recvuntil("key = ")
key = r.recvline()[:-5].decode("hex")
for a in range(256):
    for b in range(256):
        aes = AES.new(key+chr(a)+chr(b), AES.MODE_ECB)
        t = aes.decrypt(enc[32:].decode("hex")).encode("hex")
        if t[:l1] == pt1 and t[-l2:] == pt2:
            tkey = key + chr(a) + chr(b)
            iv = aes.decrypt(t.decode("hex"))
            aes = AES.new(tkey, AES.MODE_CBC, iv)
            aes = AES.new(tkey, AES.MODE_CBC, iv)
            print(aes.decrypt(flag))
r.close()

s = 36578441
f = open("enc","rb").read()
enc = int.from_bytes(f, byteorder='big')
for i in range(s-10,s+10):
    if enc%i == 0:
        break
sol = int(enc/s)
f = open("sol","wb")
f.write(sol.to_bytes((sol.bit_length() + 7) // 8, byteorder='big'))
f.close()

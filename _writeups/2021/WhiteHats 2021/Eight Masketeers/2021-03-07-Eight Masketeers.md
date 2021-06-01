---
layout: writeup
ctf: WhiteHats CTF 2021
chal: Eight Masketeers
category: misc
flag: WH2021{MY_MASKS_R_THE_BEST}
points: 992
solves: 4
---

> Alice discovered a note (titled 8 MASKeteers) left behind by Bob after a lesson on bitwise operations.

> She believes that it is some sort of the "new bitwise masking technique which can extract large amount of information" that Bob had been talking about during class.

> Are you able to help Alice decode the message?

Files given:
 - [Mask.png](Mask.png)

Looking at the description, my first thought was that the image pixels was bitmasked and needed to poke it, however looking closer at the picture, the idea turns out to be very simple, as illustrated in the diagram below:

![masking image](Mask_diagram.png){:width="80%"}
{: style="text-align: center;"}

Essentially the `&` represents 'bitwise AND' with the cells below and the `~` is bitwise NOT. Here we get `4d595f4d`, which we know are ASCII characters, hence we are on the right track, continuing this for every cell, we get `4d595f4d41534b535f525f5448455f42455354`, giving us the flag, `MY_MASKS_R_THE_BEST`

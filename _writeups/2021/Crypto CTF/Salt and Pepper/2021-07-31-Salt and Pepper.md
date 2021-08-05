---
layout: writeup
ctf: Crypto CTF 2021
chal: Salt and Pepper
category: crypto
flag: CCTF{Hunters_Killed_82%_More_Wolves_Than_Quota_Allowed_in_Wisconsin}
points: 71
solves: 69
---

> Salt and Pepper, Salty and Spicy! Can we attack these unnormalized served foods?

Files given:
 - [salt_pepper.py](salt_pepper.py)

```python
assert len(salt) == len(pepper)	== 19
assert md5(salt).hexdigest()	== '5f72c4360a2287bc269e0ccba6fc24ba'
assert sha1(pepper).hexdigest()	== '3e0d000a4b0bd712999d730bc331f400221008e0'

def auth_check(salt, pepper, username, password, h):
	return sha1(pepper + password + md5(salt + username).hexdigest().encode('utf-8')).hexdigest() == h

USERNAME = b'n3T4Dm1n'
PASSWORD = b'P4s5W0rd'
if USERNAME in inp_username and PASSWORD in inp_password:
    if auth_check(salt, pepper, inp_username, inp_password, inp_hash):
        die(f'| Congrats, you are master in hash killing, and it is the flag: {flag}')
```

This challenge is a simple length extension attack, done twice. We first get `md5(salt + username)` then we get the `sha1` and we're done:

```
ariana@ariana ~/D/G/hash_extender (master)> ./hash_extender --data "" --append "n3T4Dm1n" --signature "5f72c4360a2287bc269e0ccba6fc24ba" --format md5 --secret 19
Type: md5
Secret length: 19
New signature: 95623660d3d04c7680a52679e35f041c
New string: 8000000000000000000000000000000000000000000000000000000000000000000000000098000000000000006e335434446d316e

ariana@ariana ~/D/G/hash_extender (master)> ./hash_extender --data "" --append "P4s5W0rd95623660d3d04c7680a52679e35f041c" --signature "3e0d000a4b0bd712999d730bc331f400221008e0" --format sha1 --l 19
Type: sha1
Secret length: 19
New signature: 83875efbe020ced3e2c5ecc908edc98481eba47f
New string: 80000000000000000000000000000000000000000000000000000000000000000000000000000000000000009850347335573072643935363233363630643364303463373638306135323637396533356630343163

ariana@ariana ~/D/G/hash_extender (master)> nc 02.cr.yp.toc.tf 28010
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+   welcome to hash killers battle, your mission is to login into the  +
+   ultra secure authentication server with provided information!!     +
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| Options: 
|	[L]ogin to server 
|	[Q]uit
L
| send your username, password as hex string separated with comma: 
8000000000000000000000000000000000000000000000000000000000000000000000000098000000000000006e335434446d316e,8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000985034733557307264
| send your authentication hash: 
83875efbe020ced3e2c5ecc908edc98481eba47f
| Congrats, you are master in hash killing, and it is the flag: CCTF{Hunters_Killed_82%_More_Wolves_Than_Quota_Allowed_in_Wisconsin}
```

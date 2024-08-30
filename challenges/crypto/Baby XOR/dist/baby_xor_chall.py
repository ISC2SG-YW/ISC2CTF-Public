import random

flag = b"ISC2CTF{?????????????????????}"

seed = random.randint(1, 2**16)
random.seed(seed)

key = random.randbytes(30)
encrypted = bytes([b ^ k for b, k in zip(flag[::-1], key)])

print(encrypted)

# encrypted = b'p\x8c\x97D\xc0\x15\xc2u\xaa\x1e\x85\x8c\x9b>I\x9eL$\xd7O\xe1\x98\x80:\xe62\x17@\x13N'

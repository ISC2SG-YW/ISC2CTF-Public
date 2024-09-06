import random
encrypted = b'p\x8c\x97D\xc0\x15\xc2u\xaa\x1e\x85\x8c\x9b>I\x9eL$\xd7O\xe1\x98\x80:\xe62\x17@\x13N'
for i in range(1, 2**16):
    random.seed(i)
    key = random.randbytes(30)  
    flag = bytes([b ^ k for b, k in zip(encrypted, key)])[::-1] 
    if b"ISC2CTF" in flag:
        print(flag)
        break

import random

flag = b"ISC2CTF{????????????????????????????????????}"

mod = random.randint(4, int(len(flag)**0.5))

encrypted = ""
flag = flag.decode()
for i in range(len(flag)):
    encrypted += chr(((ord(flag[i])+ i % mod)))

print(encrypted.encode())

# encrypted = b'ITE5GTG}z4nl{bV0Uarr1zaust5v4rg`d|x3`d|cbzv6\xc2\x81'

encrypted = b"ITE5GTG}z4nl{bV0Uarr1zaust5v4rg`d|x3`d|cbzv6\xc2\x81".decode()

for mod in range(4, len(encrypted)**2):
    flag = ""
    for i in range(len(encrypted)):
        flag += chr(((ord(encrypted[i]) - i % mod)))
    if "ISC2CTF" in flag:
        print(flag)
        break
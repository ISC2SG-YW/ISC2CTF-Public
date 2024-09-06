from Crypto.Util.number import getPrime, bytes_to_long

FLAG = b"ISC2CTF{??????????????????}"

m = bytes_to_long(FLAG)

def get_big_RSA():
    p = getPrime(1024)
    q = getPrime(1024)
    N = p*q
    phi = (p-1)*(q-1)

    while True:
        d = getPrime(256)
        e = pow(d,-1,phi)
        if e.bit_length() == N.bit_length():
            break
    return N,e

N, e = get_big_RSA()
c = pow(m, e, N)

print(f'N = {hex(N)}')
print(f'e = {hex(e)}')
print(f'c = {hex(c)}')

from pwn import process
from Crypto.Util.number import long_to_bytes
from sympy.ntheory.modular import crt
from gmpy2 import iroot
from time import time
from tqdm import trange

start = time()
r = process('./app.py')

def get_data(r):
    r.recvuntil(b'>> ')
    r.sendline(b'1')
    n, ct = eval(r.recvline().rstrip())
    r.recvuntil(b'>> ')
    r.sendline(b'AAAAAAAA')
    return n, ct

ns, cts = [], []
for _ in trange(8):
    n, ct = get_data(r)
    ns.append(n)
    cts.append(ct)
m257, mods = crt(ns, cts)
msg = iroot(m257, 257)[0]

r.recvuntil(b'>> ')
r.sendline(b'1')
r.recvuntil(b'>> ')
r.sendline(long_to_bytes(msg))
print(r.recvline())
print(r.recvline())
r.close()
print(time() - start)

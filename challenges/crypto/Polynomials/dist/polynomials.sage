from sage.all import PolynomialRing, ZZ
from secret import flag
from random import getrandbits
from Crypto.Util.number import bytes_to_long

F.<x> = PolynomialRing(ZZ)

a1 = getrandbits(128)
flag = bytes_to_long(flag)
priv = (x - flag)*(x - a1)

f, g = priv, priv
for i in range(7):
    f *= (x - getrandbits(128))
    g *= (x - getrandbits(128))

assert f(flag) == 0
assert g(flag) == 0

print(f'{f = }')
print(f'{g = }')
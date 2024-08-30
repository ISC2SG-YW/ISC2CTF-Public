from hashlib import sha256
from Crypto.Cipher import AES
import random


MAGIC_NUMBERS = [(0,6,10,12,14,15), 
                 (0,3,4,7),
                 (0,2),
                 (0,)]


class MT: # omg mersenne twister
    def __init__(self, key:bytes):
        assert len(key) == 16
        self.l0 = [sha256(str(i).encode()).hexdigest() for i in key]
        self.l1 = [sha256(''.join(self.l0[i:i+2]).encode()).hexdigest() for i in range(0, len(self.l0), 2)]
        self.l2 = [sha256(''.join(self.l1[i:i+2]).encode()).hexdigest() for i in range(0, len(self.l1), 2)]
        self.l3 = [sha256(''.join(self.l2[i:i+2]).encode()).hexdigest() for i in range(0, len(self.l2), 2)]
        self.root = sha256(''.join(self.l3).encode()).hexdigest()

    def __repr__(self):
        out = ""
        ptr = 0
        ls = [self.l0, self.l1, self.l2, self.l3]
        for row in MAGIC_NUMBERS:
            for j in row:
                out += ls[ptr][j] + '\n'
            ptr += 1
        out += self.root
        return out
    
    def purge(self):
        self.l0 = [random.randbytes(32).hex() for _ in range(16)]


flag = b"ISC2CTF{???????????????????????????????????????}"
key = random.randbytes(16)
nonce = random.randbytes(8)
cipher = AES.new(key, mode=AES.MODE_CTR, nonce=nonce)
ciphertext = cipher.encrypt(flag).hex()
nonce = nonce.hex()
print(f'{nonce = }')
print(f'{ciphertext = }')

mt = MT(key)
mt.purge()
print("====================")
print("MT PUBLIC DATA BEGIN")
print("====================")
print(mt)
print("====================")
print("MT PUBLIC DATA END  ")
print("====================")
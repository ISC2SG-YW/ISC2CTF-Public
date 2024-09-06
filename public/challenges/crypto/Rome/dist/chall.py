from Crypto.Cipher import AES
import random

flag = b"ISC2CTF{???????????}"

j = random.randint(1, 9999999999999999999999999999999999999999999999999999999999999)
key = random.randbytes(16)
nonce = random.randbytes(8)

key_enc = [(i+j) % 256 for i in key]

cipher = AES.new(key, mode=AES.MODE_CTR, nonce=nonce)
ciphertext = cipher.encrypt(flag).hex()
nonce = nonce.hex()
print(f'{nonce = }')
print(f'{key_enc = }')
print(f'{ciphertext = }')
"""
nonce = '8c4c033113dbe0d9'
key_enc = [252, 154, 160, 50, 132, 1, 20, 168, 204, 57, 173, 91, 46, 15, 107, 111]
ciphertext = '2886c787049a22c57afbcd56ccfa8581ad49caa7'
"""
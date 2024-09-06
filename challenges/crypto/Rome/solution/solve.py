from Crypto.Cipher import AES

nonce = bytes.fromhex('8c4c033113dbe0d9')
key_enc = [252, 154, 160, 50, 132, 1, 20, 168, 204, 57, 173, 91, 46, 15, 107, 111]
ciphertext = bytes.fromhex('2886c787049a22c57afbcd56ccfa8581ad49caa7')

# Brute caesar key
for j in range(0, 256):
    
    key = []
    for key_val in key_enc:
        key.append((key_val - j) % 256)
    key = bytes(key) # convert key from list to bytes

    cipher = AES.new(key, mode=AES.MODE_CTR, nonce=nonce)
    flag = cipher.decrypt(ciphertext)
    if flag.startswith(B"ISC2CTF{"):
        print(flag) # b'ISC2CTF{eT_tu_brut3}'
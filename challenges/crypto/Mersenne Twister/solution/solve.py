from hashlib import sha256
from Crypto.Cipher import AES
from tqdm import trange

# We'll use this as reference
MAGIC_NUMBERS = [(0,7,10,12,14,15), 
                 (0,3,4),
                 (0,2),
                 (0,)]

# Enumerate all l0 possibilities
l0_possibilities = [sha256(str(i).encode()).hexdigest() for i in range(0, 256)]

# Skip the first 6, they're all random data
# 9ae328531bfddaf4823ea545faa93d56c5df6484aed3bb21d3f55916fcdb662a
# 18d4f4968b94f43d088ffa380d94e6e6f01c62c3a64da4c5972a5dacb42876da
# 1ed946fa9394ab889ccef00ba79c10ea71ca7521022debf68f221ce2fe55dc10
# 94763d91d9f061c05e64d3a8a54b5d91685bb56b7d6433307e9d574afd28797d
# ff2bb1dfca0a3573a4f0ca5caab391feb70f26fb066f78e28f93a0a72d09a3cd
# fc1bd31982ebeec1d5618379d2edb3503331883afe6180c7df6d17fe1f85edc8

# Lets construct our partial merkle tree
l1_0 = "1b9ffbbcda745f4d93cc64f4bb671e83f8f211b48bf152adb6ed0f35cf0bf950"
l1_3 = "bdf0e5acc21012e048c1daccd831b0fd6b2255b1ca872bcc93c11b7b04ca95d4"
l1_4 = "f9a0d3e5d930c6df319102433969ecc03a75f63512d86fe6d3711482ed967c16"
l1_7 = "a515ff1776290ccc574c52d7147ddbc58c4c4747e0994a73ddb2aa827fd30d3e"
l2_0 = "fe058709789d822251c4c3737078103e8a976a7dd20048c71a3b96c420ce1943"
l2_2 = "0e7bb79d8b9ac3f69114298d48ec7a3f24384840532580ee9c873c835225eb36"
l3_0 = "4f6ad7acaf8e9ba041d98bd4e83e19b14a9e5d18c49be3fed956cdbbdfbab992"
root = "fa288dd310b9f26e6ad4b41125f9dd205df7618cf88fbff262c4d35159347f01"

key = [-1 for _ in range(16)] # 16 unknown values

def merge(v0, v1):
    return sha256((v0 + v1).encode()).hexdigest()

for ptr in trange(256**2):
    # Enumerate each pair and use what we know of the merkle tree to solve
    # From the first round, we can deduce key bytes at indices 0,1,2,3,6,7 as well as those in 8,9,10,11
    i, j = ptr // 256, ptr % 256
    vi = l0_possibilities[i]
    vj = l0_possibilities[j]
    if merge(vi, vj) == l1_0:
        key[0], key[1] = i, j
    if merge(vi, vj) == l1_3:
        key[6], key[7] = i, j
    if merge(vi, vj) == l1_4:
        key[8], key[9] = i, j
    if merge(vi, vj) == l1_7:
        key[14], key[15] = i, j
    if merge(l1_0, merge(vi, vj)) == l2_0:
        key[2], key[3] = i, j
    if merge(l1_4, merge(vi, vj)) == l2_2:
        key[10], key[11] = i, j
    if merge(l2_0, merge(merge(vi, vj), l1_3)) == l3_0:
        key[4], key[5] = i, j
    if merge(l3_0, merge(l2_2, merge(merge(vi, vj), l1_7))) == root:
        key[12], key[13] = i, j

print(f"Found key {key}")
nonce = bytes.fromhex('f45c3fde6e06b322')
ciphertext = bytes.fromhex('fa26beda69e14c04e1114cf5d4ca3e4d69708fc94bc53b8265bb0ffcf27473897b82512ba2ec3cd083cde5fd2a1569ba')
key = bytes(key)
cipher = AES.new(key, mode=AES.MODE_CTR, nonce=nonce)
pt = cipher.decrypt(ciphertext)
print(pt)
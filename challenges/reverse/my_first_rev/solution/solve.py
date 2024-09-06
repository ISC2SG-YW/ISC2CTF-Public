# echo "abcdefghijklmnopqrstuvwxyzAB" | ./chall
p0 = b"abcdefghijklmnopqrstuvwxyzAB"
c0 = b"hSkE]PMAOB^FC\@I[NGRHKX_ZLYD**".rstrip(b"*")

def de_memfrob(s):
    out = []
    for i in s:
        out.append(i ^ 42)
    return bytes(out)

c0_memfrob = de_memfrob(c0)

# generate lookup table to reverse the swapping
lookup = {}
for ptr in range(len(c0_memfrob)):
    lookup[ptr] = c0_memfrob.index(p0[ptr])

flag_enc = de_memfrob(b"FAfYucHDAeCmRoCKKiuYFHuIuudc")
flag = "IS2CTF{"
for i in range(len(flag_enc)):
    flag += chr(flag_enc[lookup[i]])
flag += "}"
print(flag) # IS2CTF{blaCk_bOxinG_Is_a_NicE_skILl}
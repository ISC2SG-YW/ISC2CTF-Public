enc_flag = open("flag.txt","rb").read()

def next(O000O0000O0O00OOO ):
    return (872 * O000O0000O0O00OOO+173 ) & 0x3c

i = 3
flag = ""
j = 2
for enc_char in enc_flag:
    flag_char = (enc_char - j) ^ i
    i = next(i)
    j += 1
    flag += chr(flag_char)
print(flag) # ISC2CTF{d3OO00OO0o0OobfuSc4t!ng_pYtho00Oo0On_l1ke_4_prO0oOOo}
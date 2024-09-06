# assert FLAG[-4:62] + FLAG[:2] == "4ll" + FLAG[-1] + "IS"
# Evidently we have:
# >> FLAG = ISC2CTF{??????????????????????????????????????????????????4ll}

# assert FLAG[x:2:-y] == "}ctk@Ns1+aAF"
x = -1
y = 5 # (notice that FLAG[2] which is clearly C doesnt appear here, and knowing the flag length there can only be so few options for y)

FLAG = "ISC2CTF{???A????a????+????1????s????N????@????k????t????c?4ll}"
assert FLAG[-4:62] + FLAG[:2] == "4ll" + FLAG[-1] + "IS"
assert FLAG[x:2:-y] == "}ctk@Ns1+aAF"

# assert FLAG[2**y::-z] == "_l1cgVcAiTC"
# so FLAG[32::-z] == "_l1cgVcAiTC"
# Observe that if we use the C and T in isC2cTf{, the subsequent terms line up nicely with what we have. This means z = 3. No concrete evidence so far though

# assert FLAG[z:w:z] == "2F_sr1+gD3wN_saNtsh"
# z=3 would in fact put the `2` in this substring, and this correlates with the `F` right after
# w is either some really large number close to flag length or a negative number

# We dont have much concrete evidence here, but we can't exactly derive anything else either.
# But let's assume z = 3 and see what we have;
z = 3
FLAG = "ISC2CTF{i??A??c?aV??g+?c??1??l?s_???N????@????k????t????c?4ll}" # FLAG[2**y::-z] == "_l1cgVcAiTC"
FLAG = "ISC2CTF{i_?As?craV1?g+?cg?1D?l3s_w??N??_?@s??ak?N??t??s?ch4ll}" # FLAG[z:w:z] == "2F_sr1+gD3wN_saNtsh". Note we dont need to care about w to fill in the substring
assert FLAG[2**y::-z] == "_l1cgVcAiTC"
assert FLAG[z:-2:z] == "2F_sr1+gD3wN_saNtsh" 
# fill in a -2 in there as its the lowest value for this to work, so we know w < -2 IF w isnt some high number like 59 or 60
# you may notice some english words come out now, so we're likely on the right track

# assert FLAG[-y:11*z:w] == "h_1tg1a_@_-E"
# now we figure w's identity. We have FLAG[-5:33:w]. Evidently w must be some negative number of small magnitude
# The substring has 12 characters, and we only have room for about 62-33-5=24 of them So w must be -2
w = -2
FLAG = "ISC2CTF{i_?As?craV1?g+?cg?1D?l3s_w?EN-?_?@s_?ak1Ng?t?1s_ch4ll}"
assert FLAG[-y:11*z:w] == "h_1tg1a_@_-E"

# assert FLAG[-y**2:v-y:w*z] == "-srn_{"
# FLAG[-25:v-5:-6] == "-srn_{"
# FLAG[-25::-6]) gives us "-s???{S". -25 % 62 == 37, so we have 37, 31, 25, 19, 13, 7, 1
# Therefore v-5 >= 1, so v >= 6

# assert FLAG[-2*w:-v:v] == "Cwamdhwkh"
# FLAG[4:-v:v] == "Cwamdhwkh"      < 9 characters
# len(FLAG[4:-7:7])                < 8 characters; Thus v = 6
v = 6
FLAG = "ISC2CTF{i_wAs_craV1ng+mcgr1Ddl3s_whEN-?_w@s_?ak1Ng?th1s_ch4ll}"
assert FLAG[-y**2:v-y:w*z] == "-srn_{"
assert FLAG[-2*w:-v:v] == "Cwamdhwkh"

# assert FLAG[2:-u:v] == "Cicg1_im-"
# By this point we dont need to recover u, and we can easily compute the flag knowing v=6
u = 10
FLAG = "ISC2CTF{i_wAs_craV1ng+mcgr1Ddl3s_whEN-i_w@s_mak1Ng-th1s_ch4ll}"
assert FLAG[2:-u:v] == "Cicg1_im-"

# Solved!
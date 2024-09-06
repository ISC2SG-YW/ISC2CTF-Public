from ans import FLAG, u, v, w, x, y, z

assert all(abs(i) < len(FLAG) for i in (u, v, w, x, y, z))
assert FLAG[2**y::-z] == "_l1cgVcAiTC"
assert FLAG[-y**2:v-y:w*z] == "-srn_{"
assert FLAG[x:2:-y] == "}ctk@Ns1+aAF"
assert FLAG[-y:11*z:w] == "h_1tg1a_@_-E"
assert FLAG[z:w:z] == "2F_sr1+gD3wN_saNtsh"
assert FLAG[-2*w:-v:v] == "Cwamdhwkh"
assert FLAG[-4:62] + FLAG[:2] == "4ll" + FLAG[-1] + "IS"
assert FLAG[2:-u:v] == "Cicg1_im-"
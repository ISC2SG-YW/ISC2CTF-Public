from base64 import b64decode
import pyshark
import json

def xor(a, b):
    return bytes([a[i] ^ b[i % len(b)] for i in range(len(a))])

def extract(pkt):
    if not "WEBSOCKET" in str(pkt.layers):
        return
    if not "TCP" in str(pkt.layers):
        return
    
    pload = bytes.fromhex(''.join(pkt.tcp.payload.split(':')))
    if "Masking-Key:" in str(pkt.websocket):
        masked_key = bytes.fromhex(''.join(pkt.websocket.masking_key.split(':')))
        pload = xor(pload, masked_key)
    start_index = pload.find(b"{\"")

    try:
        pload = json.loads(pload[start_index:])
        return pload
    except:
        return


cap = pyshark.FileCapture("webb.pcapng")
while True:
    try: 
        p = cap.next()
    except StopIteration:
        break

    web_data = extract(p)
    if not web_data:
        continue
    if 'data' not in web_data:
        continue

    data = b64decode(web_data["data"])
    if b"ISC2CTF{" in data:
        flag = data[data.find(b"ISC2CTF{"):].split(b' ')[0]
        print(flag) # b'ISC2CTF{webb_webb_webb_webb_webb_weeb_webb_webb_webb_websockets!}'
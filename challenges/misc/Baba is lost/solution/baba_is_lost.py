from pwn import * 

r = remote('127.0.0.1', 12345)
def answer():
    print(r.recvline())
    n = int(r.recvline().strip().decode())
    x,y = r.recvline().strip().decode().split()
    x = int(x)
    y = int(y)
    lx,ty,rx,by = 0,0,n,n
    direction = r.recvline().decode().strip()
    if "N" in direction:
        by = y 
    if "S" in direction:
        ty = y
    if "E" in direction:
        lx = x
    if "W" in direction:
        rx = x
    while True:
        x = (lx+rx)//2
        y = (ty+by)//2
        r.sendline(f"{x} {y}")
        direction = r.recvline().decode().strip()
        if "Singapore" in direction:
            print("Success!",direction)
            break
        if "N" in direction:
            by = y - 1 
        if "S" in direction:
            ty = y + 1
        if "E" in direction:
            lx = x + 1
        if "W" in direction:
            rx = x - 1
for _ in range(10):
    answer()
print(r.recvall().decode())
        
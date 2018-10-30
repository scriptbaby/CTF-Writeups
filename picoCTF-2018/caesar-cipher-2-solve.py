#!/usr/bin/env python2

with open("ciphertext","r") as ciphertext:
    cipher = ciphertext.read()
    ciphertext.close()

# contains picoCTF
edited = cipher[0:7]
'''
# display ord of 1st 7 chars of ciphertext
for i in edited:
    print ord(i)
print "start\n"
# display ord of picoCTF
for i in "picoCTF":
    print ord(i)
'''
plain = []
for i in cipher:
    plain.append(chr(ord(i)+ 12))
print ''.join(plain)
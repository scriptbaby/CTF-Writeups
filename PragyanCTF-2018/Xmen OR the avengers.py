#!/usr/bin/env python

#Made by ScriptBaby for PragyanCTF 2018

import hashlib
from Crypto.Cipher import AES
import base64 

cleartext = open("info_clear.txt","r").read()
cipher1 = open("info_crypt.txt","r").read()

key = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(cleartext,cipher1))
key2 = hashlib.md5(key.strip("\n")).hexdigest()

cipher2 = open ("superheroes_group_info_crypt.txt","r").read()
cipher2 = cipher2.strip("\n")

obj = AES.new(key2, AES.MODE_ECB)
cipher2 = base64.b64decode(cipher2)

plain2 = obj.decrypt(cipher2)

print plain2


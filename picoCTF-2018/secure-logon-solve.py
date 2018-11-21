#!/usr/bin/env python3

# imports
import requests
import json
import re
from base64 import b64decode as b64d,b64encode as b64e
from pwn import xor
'''
A = IV
B = post decrypt
C = plain text

A xor B = C
B = A xor C

C' = A' xor B
A' = C' xor B
A' = C' xor A xor C
'''

cookie = {}
cookie['password'] = "lol"
cookie['username'] = "lol"
cookie['admin'] = 0
cookie_data = json.dumps(cookie, sort_keys=True)
to_be_flipped = cookie_data.index("0")

cookie = "3p/EY/cO422MTCZ5ctVPTGlVbEiEG4fNiEk2NTeNEPWY+nS63S0EHX9VGQ77nXDUgrRZn+jy1M+NrymZPxg7Mg4rps6w/a+XOa/nTiCOYVo="
decoded = b64d(cookie)

'''
change 10th byte of IV
Since C = 0 , C' = 1 
Therefore 10th byte xor 1 xor 0
'''
new_cookie = b64e(decoded[:10] + xor(decoded[10],'1','0') + decoded[11:])
r = requests.get("http://2018shell1.picoctf.com:12004/flag",cookies={'cookie': new_cookie.decode("utf-8") })
flag = re.findall("<code>(.*?)</code>",r.text)
print(flag[0])
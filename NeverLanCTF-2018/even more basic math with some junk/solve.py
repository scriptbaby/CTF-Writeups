#!/usr/bin/env python3
#created by ScriptBaby for NeverLanCTF 2018

import re
string = open("numbers.txt","r").read()
total = 0
list = re.findall(r'\d+', string)
for i in list:
    i = int(i)
    total += i
print(total)


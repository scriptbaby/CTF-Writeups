#!/usr/bin/env python3

flag = 'gigem{'
a = [65,53,53,51,77,98,49,89]
for i in range(len(a)):
    flag += chr(a[i])
flag += '}'
print(flag)
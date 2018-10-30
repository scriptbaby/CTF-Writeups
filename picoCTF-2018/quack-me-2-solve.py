#!/usr/bin/env python2

import string
charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

refer = "00 30 20 50 40 70 60 90 80 B0 A0 D0 C0 F0 E0 11 01 31 21 51 41 71 61 91 81 B1 02 32 22 52 42 72 62 92 82 B2 A2 D2 C2 F2 E2 13 03 33 23 53 43 73 63 93 83 B3 04 34 24 54 44 74 64 94 84 B4 A4 D4 C4 F4 E4 B5 A5 D5 C5 F5 E5 12 A3 D3 C3 F3 E3 10 A1 D1 C1 F1 15 05 35 25 55 45 75 65 95 85".split(" ")
cipher = "11 80 20 E0 22 53 72 A1 01 41 55 20 A0 C0 25 E3 95 20 15 35 20 15 00 70 C1".split(" ")
flag = []
for i in cipher:
    #print refer.i
    #print refer.index(i)
    flag.append(charset[(refer.index(i))])
print ''.join(flag)

#!/usr/bin/env python

# imports
from Crypto.Util.number import inverse

# declaring primes in n
# found using yafu
P0 = 2161186871
P1 = 2210378543
P2 = 2343629927
P3 = 3599498447
P4 = 3672479309
P5 = 3602658691
P6 = 2253014921
P7 = 2307760907
P8 = 2240036549
P9 = 3773717219
P10 = 3112696043
P11 = 2628947801
P12 = 3607787551
P13 = 3387057041
P14 = 3138129073
P15 = 4210889299
P16 = 2225458549
P17 = 3530941441
P18 = 3689457059
P19 = 3020766599
P20 = 2156826481
P21 = 3208322833
P22 = 2731258897
P23 = 3914481401
P24 = 4072625497
P25 = 3857104213
P26 = 2242297111
P27 = 4088740399
P28 = 2975006687
P29 = 3493376771
P30 = 2221006331
P31 = 3243734983
e = 65537
c = 622615055135998689234552532272711567918347488407760104316754836276370250285362533645112851965941901179204260124991986234193441023765508931490995857249393887656841486154081438554694565283731024037973274991542341844373009531732279951399402375047598135118742985101527148577442326730730394955873290302637911
n = 2163444177926356370001715936364415016055916526316141474034094987358918981439023317216400585132968222779141822558626309537887973763470935289279638564292686203866496655803486075194623157621954568251597989132759497406876204329839645053334938838408889749786051568019216494340005388848925879524377907668085481
prime_list = [P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13,P14,P15,P16,P17,P18,P19,P20,P21,P22,P23,P24,P25,P26,P27,P28,P29,P30,P31]
# phi n can be computed by (a-1)(b-1) and so on for multiple prime rsa
phi = 1
for i in prime_list:
    phi = (i-1) * phi
#print phi
d = inverse(e,phi)
m = pow(c,d,n)
print hex(m)[2:-1].decode('hex')

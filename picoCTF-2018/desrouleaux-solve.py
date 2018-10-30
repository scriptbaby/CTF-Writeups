#!/usr/bin/env python2

# imports
from pwn import remote
import json
import re
# vars

# open json
with open("incidents.json",'r') as inc:
    incidents = json.load(inc)
    inc.close()
for num in range(7,20):
    breaker = 0
    for test in range(20):
        data = incidents["tickets"]
        ips = []
        source = []
        dst = []
        for i in range(10):
            source.append(data[i]["src_ip"])
            ips.append(data[i]["src_ip"] + ":" + data[i]["dst_ip"])
            dst.append(data[i]["dst_ip"])
        collection = [str(i) for i in source]

        counter = 1
        for i in ips:
            #print i
            if ips.count(i) == 1:
                counter +=1
        #print counter

        r = remote("2018shell1.picoctf.com", 10493)
        r.recv()
        r.sendline("21.201.106.115")
        sourceip = r.recv()
        # find the ip for the second qn
        sourceip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", sourceip)
        sourceip = sourceip[0]

        #print collection
        # find number of source ip occurence
        count = collection.count(sourceip)
        # convert to string
        ip_str = [str(i) for i in ips]

        #print ip_str
        dst2 = []


        for i in ip_str:
            if sourceip in i:
                dst2.append(i.split(":")[1])    
        r.sendline(str(len(set(dst2))))
        r.recv()
        decimal = float(num)/(test+1)
        print "[+] Trying {0:.2f} now".format(decimal)
        r.sendline("{0:.2f}".format(decimal))
        response = r.recv()   
        if "Incorrect!" in response:
            print "Wrong answer"
        else:
            print response
            breaker = 1
            break
        if breaker == 1:
            break
            
        r.close()
    


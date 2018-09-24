#!/usr/bin/env python3
#Done by ScriptBaby
#EasyCTF IV

from pwn import *

f = open("zipcode.txt","r")
content = f.read()
content = content.replace("VM78:2","")
content = content.split("\n ")

def sendResponse(type,zipcode):
	for line in content:
		line = line.split("/")
		if(zipcode == line[0]):
			return(line[type])	

p = remote("c1.easyctf.com", 12483)

p.recvuntil('Go!')
for x in range(50):
	p.recvuntil("What is the ")
	datatype = p.recv(10)
	p.recvuntil("zip code ")
	zipcode = p.recv(5)
	p.recv(1)
	print("Round: %r, %r, %r"%(x+1,datatype, zipcode))
	if ("land area" in datatype):
		print(sendResponse(1,zipcode))
		p.sendline(sendResponse(1,zipcode))
	elif ("water area" in datatype):
		print(sendResponse(2,zipcode))
        	p.sendline(sendResponse(2,zipcode))
    	elif ("latitude" in datatype):
		print(sendResponse(3,zipcode))	
		p.sendline(sendResponse(3,zipcode))
   	elif ("longitude" in datatype):
        	print(sendResponse(4,zipcode))
		p.sendline(sendResponse(4,zipcode))
p.recv()
print(p.recv())
	

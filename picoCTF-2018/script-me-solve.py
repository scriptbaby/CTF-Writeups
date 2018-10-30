#!/usr/bin/env python

from pwn import *
import re

c = remote('2018shell1.picoctf.com', 22973)
for i in range(14):
    c.recvline()
    # print c.recvline()

def getLevel(number):

    height = 0
    level = 0
    for char in number:
        if char == '(':
            height = height + 1
        else:
            height = height - 1

        if height > level:
            level = height

    return level

def doMath(left, right):
    leftLevel = getLevel(left)
    rightLevel = getLevel(right)
    # print '{leftLevel}   {left}'
    # print '+'
    # print '{rightLevel}   {right}'
    if leftLevel == rightLevel:
        return left + right

    elif leftLevel > rightLevel:
        return left[:-1] + right + ')'

    else: #leftLevel < rightLevel
        return '(' + left + right[1:]


while True:
    question = c.recvline().decode("utf-8")
    question = question.replace(' = ???', '').replace(' ','').replace('\n', '')
    question = question.split('+')
    # print 'Question: {question}'
    c.recvline()

    while len(question) != 1:
        ans = doMath(question[0], question[1])
        if ans:
            question[0] = ans
            question.remove(question[1])
        else:
            print 'Undefined:\n{question[0]}\n+\n{question[1]}'

    # print 'Answer: {ans}'
    c.sendline(question[0])
    c.recvline()
    c.recvline()
    flagtxt = c.recvline()
    
    flag = re.search(r'(picoCTF{.+})', str(flagtxt))
    if flag:
        print flag.group(0)
        break

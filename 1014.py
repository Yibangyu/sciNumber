#!/usr/bin/python

import re

N = input()

g = re.match(r'([+-])([1-9]\.[0-9]+)E([+-])([0-9]+)',N)

symbol1,string,symbol2,num = g.groups()


li = list(string)

if symbol2 == '-':
    for index in range(int(num)):
        li[0],li[1] = li[1],li[0]
        li.insert(0,'0')
else:
    point = 1
    for index in range(int(num)):
        if point < len(li)-1:
            li[point],li[point+1] = li[point+1],li[point]
        else:
            li.insert(point,'0')
        point = point+1
    if li[len(li)-1] == '.':
        li.pop()


result = ''.join(li)

if symbol1 == '+':
    print(result)
else:
    print('-'+result)

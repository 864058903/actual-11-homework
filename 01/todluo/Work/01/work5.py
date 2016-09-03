#!/usr/bin/env python
#encoding:utf-8
import random
b = random.randint(0,100)

while True:
    _input=raw_input('please you number:')
    a = int(_input)
    if a > b :
        print '猜错了，大了哦！'
    elif a< b :
        print '猜错了，小了哦！'
    else :
        print '恭喜你猜对了！'
        break
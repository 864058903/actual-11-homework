#!/usr/bin/env  python  
#coding=utf8
f = open('aaa.log','r')
f.seek(0,2)
line=''
while True:
    line+=f.readline()   ##当输入的为不换行时,讲输入的值累加,以便输出
    if  line.endswith('\n'):
        print line,
        line=''

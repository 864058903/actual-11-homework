#!/usr/bin/env  python 
#coding=utf8

with open('server.log','r')   as  f:
    while True:
        line=f.read(2048)
        if  line=='':
	    break
        with open('new.log','a+') as ff:
            ff.write(line)


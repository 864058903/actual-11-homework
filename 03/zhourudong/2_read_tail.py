#!/usr/bin/env python
#conding:utf8
from time import sleep

f = open('file.txt','r')
# for line in f:
# 	print line,
# f.close()


while 1:
	line = f.readline()
	if line:
		print line,
	else:
       #  
		sleep(1)
		continue
f.close()
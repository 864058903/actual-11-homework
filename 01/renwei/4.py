#!/usr/bin/python
#encoding: utf-8
for a in range(1, 10):  
    print " ".join(["%d*%d=%d" % (a, b, a*b) for b in range(1, a+1)])



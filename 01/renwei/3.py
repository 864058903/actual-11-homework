#!/usr/bin/python
#coding:utf -8

mums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
i = None
y = None
for a in mums:
     if a is None:
        i = a
     elif a > i:
        i = y
        i = a
     elif y is None:
          y = a
     elif a > y:
          y = i
print 'first:%s, second:%s' % (i, y)
 

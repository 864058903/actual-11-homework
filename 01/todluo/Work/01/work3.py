#!/usr/bin/env python
#encoding:utf-8
_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
maxnum1 = max(_list)
maxnum2 = 0
for i in _list:
    if i < maxnum1 and i > maxnum2  :
        maxnum2 =i
print 'This is two max numer : %s,%s' %( maxnum1,maxnum2)
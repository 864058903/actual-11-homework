#!/usr/bin/env python
#encoding:utf-8
print '9X9 乘法表'

for i in range(1,10):
    for j in range(1,i+1):
        print j,'X',i, '=',j*i,'\t',
    print '\n'
print '===End==='
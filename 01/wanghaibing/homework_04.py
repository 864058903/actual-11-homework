#!/usr/bin/env pythyon
#9*9 multiplication table
for i in range(1,10):
    for j in range(1,i+1):
        pro=j*i
        print '%s*%s=%s' % (j,i,pro) ,
    print "\n"

'''
功能ok
作业二ok，但乘法口诀，每一行多一个换行，可以使用print ''代替line7

'''

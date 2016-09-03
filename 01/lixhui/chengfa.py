#!/usr/bin/evn python
for i in range(1, 10):
    print " ".join(["%d*%d=%d" % (j, i, i*j) for j in range(1, i+1)])


'''
功能ok
'''

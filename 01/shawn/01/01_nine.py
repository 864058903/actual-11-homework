#!/usr/bin/env python
#coding: utf-8

'''
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
1 * 3 = 3  2 * 3 = 6  3 * 3 = 9
'''

for x in range(1,10):
    for y in range(1,x+1):
        print "%s * %s = %s" % (y,x,x*y),
    print ''


'''
功能ok
'''

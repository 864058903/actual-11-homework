#!/usr/bin/env python
_list=[-7,6,8,-3,3,-2,9,-3,9,-4,4,3,8,-4,5,-7,9,-5,-7,10,-8,5,-2,-1,5,3,6,-3]
while True:
    n=int(raw_input('please your mm nu: '))
    _list2=[]
    _list3=[]
    sum1=0
    if n == 1 or n >= len(_list):
       print max(_list)
       exit()
    else:
       for i in  range(0,len(_list)-n+1):
           _list2=_list[i:i+n]
           for j in _list2:
               sum1=sum1+j
           _list3.append(sum1)
           sum1=0
    #print _list3
    print 'Max ai: %s' % (max(_list3))

'''
功能ok
'''

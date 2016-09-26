#!/usr/bin/env python
#encoding:utf-8
unsort_list2=[(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]

def sorts(x):
    return sorted(x,key=lambda a:max(a))

print sorts(unsort_list2)

#!/usr/bin/env python
#encoding:utf-8
#arg1:要排序的序列，arg2:max、min最大最小排序; arg3:0、False升序，1、True降序
def sorts(x,y=max,z=0):
    return sorted(x,key=lambda a:y(a),reverse=z)

if __name__=='__main__':
   unsort_list=[(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
   print sorts(unsort_list,max,1)

#!/usr/bin/env python
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
alist =[]
#print '%s\n%s' %(arr1,arr2)
for i in arr1:
    if  i   in arr1 and i  in arr2 and i not in alist:
       alist.append(i)
print alist


'''
功能
改进:
1. line7-line14是否可以修改为1行
'''

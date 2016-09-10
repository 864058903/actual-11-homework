#!/usr/bin/env python
array = [1,2,3,6,5,4,9,7,8,11,13,10,12]
for i in range(len(array)):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array

'''
逻辑不正确
1. line 4为什么只比较i次，考虑将N个人中最高的排到队尾需要比较几次
'''

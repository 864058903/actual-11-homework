#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
求两个数组共同的值（去重）
'''
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
temp_list = []

for i in xrange(len(arr2)):
	if (arr2[i] in arr1 ) and (arr2[i] not in temp_list):
		temp_list.append(arr2[i])

print temp_list
'''
遍历列表对比，两个数组有相同的元素则添加
使用集合去重
'''
'''
功能ok
'''

# 方法2 集合求交集
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

set_arr1 = set(arr1)
set_arr2 = set(arr2)

same_set = set_arr1 & set_arr2
print list(same_set)

'''
功能ok
'''

#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 方法1
my_list=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
temp_list = []
for i in xrange(len(my_list)):
   if my_list[i] not in temp_list:
       temp_list.append(my_list[i])
print temp_list
'''
定义一个空列表,
遍历列表元素
   如果元素不在空列表中，则追加
   
每次循环需要遍历整个数组 
'''

# 方法2
my_list=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
my_list.sort()
temp_list = [my_list[0]]

for i in xrange(1,len(my_list)):
   if my_list[i] != my_list[i-1]:
       temp_list.append(my_list[i])
print temp_list
'''
先进行排序，前后元素进行对比，如果不相等，则追加元素到列表中
第一次遍历第一个元素不在列表中
'''

# 方法3
# set去重
my_list=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
my_list = list(set(my_list))
print my_list
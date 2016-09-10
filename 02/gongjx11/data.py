#!/usr/bin/env python
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
data = []
for i in (arr1 + arr2):
  if str(i) not in str(data):
	data.append(i)
	a=data.sort()
print (data)

'''
逻辑不正确
问题：
1.咱们想要arr1和arr2中都存在元素，目前实现的是对arr1和arr2组成的list进行去重
2. line6 考虑如何判断元素是否在list中
'''

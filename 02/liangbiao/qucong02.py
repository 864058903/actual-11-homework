#!/usr/bin/python
#encoding: utf-8
#不同数组求相同的元素

arr1 = [14,1,3,2,4,2,3,12,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [999,2,1,3,2,43,234,454,452,234,14,1421]
arr3 = []

combination = [arr1]

for temp_list in combination:
	for element in temp_list:
		num = temp_list.count(element)
		while num > 1:
			temp_list.remove(element)
			num = num -1

temp_list2 = arr1 + arr2
for element in temp_list2:
	if temp_list2.count(element) > 1:
		arr3.append(element)

for element in arr3:
	num = arr3.count(element)
	while num > 1:
		arr3.remove(element)
		num = num - 1

print arr3

'''
功能ok
改进点
1. 将line12-line27修改为1行
'''

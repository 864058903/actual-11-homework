#!/usr/bin/python
# ^_^ coding: utf-8 ^_^
num1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
num2 = []
for i in num1:
	if not i in num2:
		num2.append(i)
print num2

'''
功能ok
改进点:
1. 不在数组中尽量使用e not in list格式
'''

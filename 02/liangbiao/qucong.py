#!/usr/bin/python
#encoding: utf-8
#数组去从

_list1 = [1,12,12,2,3,4,2,3,14,3,2,3,14,3,21,2,2,3,4111,22,3333,4]

for element in _list1:
	num = _list1.count(element)
	while num > 1:
		_list1.remove(element)
		num = num - 1
print _list1

'''
功能ok
'''

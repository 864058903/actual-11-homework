#!/usr/bin/python
#encoding: utf-8
#冒泡排序

_list1 = [12,4,3,5,6,1,2,3,7,1,1,1]

for i in range(len(_list1) - 1):
	if _list1[i] > _list1[i + 1]:
		temp = _list1[i + 1]
		_list1[i + 1] = _list1[i]
		_list1[i] = temp
print _list1

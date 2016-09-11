#!/usr/bin/python
#encoding: utf-8
#冒泡排序

_list1 = [12,4,3,5,6,1,2,3,7,1,1,1]

for j in range(len(_list1) - 1):
	for i in (range(len(_list1) - 1 - j)):
		if _list1[i] > _list1[i + 1]:
			temp = _list1[i + 1]
			_list1[i + 1] = _list1[i]
			_list1[i] = temp
print _list1

'''
此处只将最大的元素排到了list最后，如果想要将list排成一个从小到大，需要把这个过程循环多少次呢
'''

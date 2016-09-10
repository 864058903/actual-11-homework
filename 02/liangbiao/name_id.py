#!/usr/bin/python
#encoding: utf-8
#将用户user:id的输入格式化成由元组组成的列表[(user,id)]输出

names = []

_input = raw_input('please input (name:id):')

for i in _input.split(','):
	names.append(tuple(i.split(':')))
print names

'''
功能ok
'''

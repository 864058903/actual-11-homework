#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
5. 用户输入员工名字和id，名字和id之间用:分隔
   多个用户 用逗号分隔
   最终输入所有用户对应id的信息
   比如用户输入user1:119,user2;112,user3:113
   最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
'''
user_input = raw_input('please input username userid(examp tom:11,python:1112):')



a_list = user_input.split(',')

a_list_of_tuple = [v.split(':') for v in a_list]
temp_tuple = ()
out_list =[]
for x in a_list_of_tuple:
	temp_tuple=(x[0],x[1])
	out_list.append(temp_tuple)

print out_list

'''
功能ok
'''


# 方法2
user_input = raw_input('please input username userid(examp tom:11,python:1112):')
# user_input = 'nginx:2008,python:1991'

while (':' not in user_input) and (',' not in user_input):
    ''' 检查用户输入'''
    user_input = raw_input('please input username userid(examp tom:11,python:1112):')

a = user_input.split(',')
b = [tuple(x.split(':')) for x in a]

print b

'''
功能ok
'''
# [('nginx', '2008'), ('python', '1991')]

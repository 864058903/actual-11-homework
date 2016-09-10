#-*- encoding: utf-8 -*-
'''
Created on 2016/9/6 0006
@author: dongange
题目：字符串格式化
'''

# NameList = raw_input('please input name list:')

NameList = 'user1:119,user2:112,user3:113'
NewList = []

NameBlock = NameList.split(',')

for i in range(len(NameBlock)):
    Name = NameBlock[i].split(':')[0]
    Phone = NameBlock[i].split(':')[1]
    NameTuple = (Name, Phone)
    NewList.append(NameTuple)
print NewList

'''
功能ok
'''

#-*- encoding: utf-8 -*-
'''
Created on 2016/9/6 0006
@author: dongange
题目：求两个数组的交集
'''


NumsList_1 = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
NumsList_2 = [2, 1, 3, 2, 43, 234, 454, 452, 234, 14, 21, 14]
List_1_2 = []
NewList = []

for i in range(len(NumsList_1)):
    if NumsList_1[i] in NumsList_2:
        List_1_2.append(NumsList_1[i])

for i in range(len(List_1_2)):
    if List_1_2[i] in NewList:
        pass
    else:
        NewList.append(List_1_2[i])

print NewList


'''
功能ok
改进点：
1. line14 直接for遍历list中元素
2. 将line14-22使用一个for循环搞定
'''

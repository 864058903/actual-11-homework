#-*- encoding: utf-8 -*-
'''
Created on 2016/9/6 0006
@author: dongange
题目:数组去重
'''

NumsList = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
NewList = []

for i in range(len(NumsList)):
    if NumsList[i] in NewList:
        pass
    else:
        NewList.append(NumsList[i])

print NewList

'''
功能ok
改进点：
1. line11 直接for遍历list中元素
2. 将line12-14使用not 改为2行
'''

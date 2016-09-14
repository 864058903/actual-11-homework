#coding: utf-8

arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

unique =  []

'''
for x in arr1:
    for y in arr2:
        if x == y and x not in unique:
            unique.append(x)

print unique
'''


for i in arr1:
    if i in arr2 and i not in unique:
        unique.append(i)

print unique


'''
功能ok
改进点
1. line 8-10修改为一个for
'''

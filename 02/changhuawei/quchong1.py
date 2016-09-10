#encoding:utf-8
#求两个数组共同的值（去重）
arr3 = []
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
bb = []
for i in arr1:
    if i not in bb:
            bb.append(i)
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
bb2 = []
for i in arr2:
    if i not in bb2:
            bb2.append(i)

for i in bb2:
    if i in bb:
        
        arr3.append(i)
print arr3

#法二
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
arr3 =[]
for i in arr2:
    if i in  arr1 and i not in arr3:
        arr3.append(i)
print arr3
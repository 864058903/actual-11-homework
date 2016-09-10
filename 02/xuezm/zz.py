LL=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
NLL=[]
for  i in LL:
    if i not in NLL:
        NLL.append(i)
print NLL


'''
功能ok
'''

arr1 = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
arr2 = [2, 1, 3, 2, 43, 234, 454, 452, 234, 14, 21, 14]
arr3=[]
for i in arr2:
    if i in  arr1 and inot in arr3:
        arr3.append(i)
print arr3


'''
功能ok
'''


zfc='user1:119,user2:112,user3:113'
#1
LL=zfc.split(",")
J=[]
for i in  LL:
    a=i.split(":")
    J.append([a[0],a[1]])
print  tuple(J)
'''
功能ok
'''
#2
info={}
LL=zfc.split(",")
for i in  LL:
    a=i.split(":")
    info[a[0]]=a[1]
print info.items()

'''
功能ok
'''

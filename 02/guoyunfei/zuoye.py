#coding: utf-8
#

'''
1. 整理今天学的东西
2. 冒泡排序
3. 数组去重
    [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
4.
    arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
    arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
    求两个数组共同的值（去重）
5. 用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2;112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
6. 插入排序 （随意）
'''

#冒泡排序
print("1.冒泡排序")
a = [10,1,5,4,9]
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
print

'''
功能ok
'''

#数组去重(通过set集合方法)
print("2.数组去重")
b = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
print(list(set(b)))
print

'''
功能ok, 建议使用遍历list+list操作进行比较判断
'''

#两个数组取共同的值(通过set集合方法)
print("3.数组共同值")
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
print(arr1)
print(arr2)
print(list(set(arr1).intersection(set(arr2))))
print

'''
功能ok, 建议使用遍历list+list操作进行比较判断
'''

#信息输出
print("4.员工信息")
result = []
message = raw_input("输入员工名字和ID(名字和id之间用:分隔,多个用户用逗号分隔): ").strip()
for mess in message.split(","):
    result.append(tuple(mess.split(':')))
print(result)
print

'''
功能ok
'''

#插入排序
print("5.插入排序")
b = [10,1,5,4,9,2]
for i in range(1, len(b)):
    tmp = b.pop(i)
    for j in range(i, 0, -1):
        if tmp >= b[j-1]:
            b.insert(j, tmp)
            break
    else:
        b.insert(0, tmp)

print(b)

'''
功能ok
'''

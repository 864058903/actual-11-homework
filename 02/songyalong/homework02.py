#encoding:utf-8

'''1. 整理今天学的东西
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

6. 插入排序 （随意）'''

'''冒泡排序'''
# list_num=[2,311,32,41,353,5532,-123,31,-12,343434,4567]
# for j in range(len(list_num)):
#     for i in range(len(list_num)-1):
#         if list_num[i] > list_num[i+1]:
#             list_num[i],list_num[i+1]=list_num[i+1],list_num[i]
# print list_num
'''
功能ok
改进点
1. 考虑下line22可以循环几次就ok
2. 考虑下line23可以循环几次就ok
'''

'''数组去重'''
# num_list01=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
# new_numlist=[]
# for i in num_list01:
#     if not new_numlist:
#         new_numlist.append(i)
#     elif i in new_numlist:
#         continue
#     else:
#         new_numlist.append(i)
# print new_numlist

'''
功能ok
改进:
1. line42-43有用吗？
'''

'''求两个数组共同的值（去重）'''
# arr1 = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
# arr2 = [2, 1, 3, 2, 43, 234, 454, 452, 234, 14, 21, 14]
# new_arr=[]
# if len(arr1) >= len(arr2):
#     for i in arr2:
#         if i in arr1 and i not in new_arr:
#
#             new_arr.append(i)
#         else:
#             continue
# else:
#     for i in arr1:
#         if i in arr2 and i not in new_arr:
#             new_arr.append(i)
#         else:
#             continue
# print new_arr

'''
功能ok
改进点
1. line56有用吗
2. line61-62有用吗
'''

'''5. 用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2;112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]'''

user_input=raw_input('请输入用户信息：')
user_list = user_input.split(',')
user_newlist = []
print  user_list
for i in user_list:
    user_tuple = tuple(i.split(':'))
    print user_tuple
    user_newlist.append(user_tuple)
print user_newlist

'''
功能ok
'''

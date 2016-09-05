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


'''求两个数组共同的值（去重）'''
# arr1 = [1, 2, 3, 4, 2, 12, 3, 14, 3, 2, 12, 3, 14, 3, 21, 2, 2, 3, 4111, 22, 3333, 4]
# arr2 = [2, 1, 3, 2, 43, 234, 454, 452, 234, 14, 21, 14]
# new_arr=[]
# if len(arr1) >= len(arr2):
#     for i in arr2:
#         if i in arr1:
#             new_arr.append(i)
#         else:
#             continue
# else:
#     for i in arr1:
#         if i in arr2:
#             new_arr.append(i)
#         else:
#             continue
# print new_arr

'''5. 用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2;112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]'''

# user_num=int(raw_input('请输入你想创建几个用户数：'))
# user_lists=[]
# for i in range(user_num):
#     user_name=raw_input('请输入用户名：')
#     user_id = raw_input('请输入ID号：')
#     user_lists.append((user_name,user_id))
# print user_lists

#!/usr/bin/env python
#encoding: utf-8

num_list = [6, 4, 5, 3, 1, 7]

for i in range(1, len(num_list) -1):
    for j in range(i, 0, -1):
        if num_list[j-1] > num_list[j]:
            num_list[j],num_list[j-1] = num_list[j-1],num_list[j]
        else:
            break

print num_list


'''
origin_list = []

while True:
    value = raw_input("enter number here: ")
    if value != "end":
        value = int(value)
        if len(origin_list) != 0:
            origin_list.sort()
            if value >= origin_list[-1]:
                origin_list.append(value)
            elif value < origin_list[0]:
                origin_list.insert(0,value)
            else:
                for i in range(len(origin_list)):
                   if origin_list[i] >= value:
                        origin_list.insert(i,value)
                        break
        else:
            origin_list.append(value)
        print origin_list
    else:
        break

'''
'''
功能ok，如果是一个已有的list会怎么排序呢
'''

#encoding: utf-8
'''
使用元组中最大的值进行排序
'''

def tuple_cmp(one,two):
    return max(one) > max(two)

def bubbl(un_sort,tuple_cmp):
    list_len = len(un_sort)
    for i in range(list_len - 1 ):
        for j in range(list_len - 1 ):
            if tuple_cmp(un_sort[j],un_sort[j+1]):
                # 向tuple_cmp传递参数进行比较，返回True则进入交换
                un_sort[j],un_sort[j+1] = un_sort[j+1],un_sort[j]

ab = [(1, 2), (6, 3), (4, 1), (2, 10), (3, 5), (5, 7)]
bubbl(ab,tuple_cmp)

print ab
'''
定义函数接收传参

'''
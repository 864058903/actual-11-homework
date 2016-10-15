#!/usr/bin/env python
# -*- coding: utf-8 -*-
cmp_value = lambda x, y: x > y
cmp_tuple = lambda x, y: x[1] > y[1]
cmp_tuple_max = lambda x, y: max(x) > max(y)

get_key = lambda x: x
get_tuple = lambda x: x[1]
get_tuple_max = lambda x: max(x)


def bubble_sort(unsort_list, cmp=cmp_value, key=get_key):
    length = len(unsort_list)
    for j in range(0, length - 1):
        for i in range(0, length - 1):
            a = unsort_list[i]
            b = unsort_list[i+1]
            if cmp(key(a), key(b)):
                unsort_list[i], unsort_list[i+1] = unsort_list[i+1], unsort_list[i]

if __name__ == '__main__':
    # 根据unsort_list2中最大的元素来排序
    # 使用bubble_sort函数
    unsort_list2 = [(1, 2), (6, 3), (4, 1), (2, 10), (3, 5), (5, 7)]

    bubble_sort(unsort_list2, cmp=cmp_tuple_max)
    print unsort_list2

    bubble_sort(unsort_list2, key=get_tuple_max)
    print unsort_list2
    # 使用sort方法
    unsort_list2.sort(cmp=lambda x, y: 1 if max(x) > max(y) else -1)
    print unsort_list2

    unsort_list2 = [(1, 2), (6, 3), (4, 1), (2, 10), (3, 5), (5, 7)]
    unsort_list2.sort(key=get_tuple_max)
    print unsort_list2

#!/usr/bin/env python 
#coding=utf8
def max_sort(LIST):
    new_list =sorted(LIST,key=lambda x:max(x),reverse=False)
    return  new_list
    
if  __name__   ==  "__main__":
	unsort_list2 = [(1, 2), (6, 3), (4, 1), (2, 10), (3, 5), (5, 7)]
        print max_sort(unsort_list2)

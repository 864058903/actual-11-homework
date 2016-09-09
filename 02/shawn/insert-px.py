#!/usr/bin/env python
#encoding: utf-8

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
        print origin_list
        break
        
        

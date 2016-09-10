#encoding: utf-8

_list = [10,88,27,1,7,9,22]

for j in range(len(_list) - 1):

    for i in range(len(_list) - 1 - j):

        if _list[i] > _list[i + 1]:

            _list[i],_list[i + 1] = _list[i + 1],_list[i]

print _list

'''
功能ok
'''

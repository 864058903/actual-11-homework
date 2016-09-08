#coding: utf-8

mylist = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
unique = []

for i in mylist:
    if i not in unique:
        unique.append(i)

print unique

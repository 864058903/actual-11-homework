#!/usr/bin/python

#homeowrk_one:
num1 = [1,23,99,45,100,3,65536,4000,5000]
max1=num1[0]
max2=num1[0]
for i in num1:
    if i > max1:
        max1=i
print max1
for i in num1:
    if i > max2 and i < max1:
        max2=i
print max2

#homework_two
for i in range(1,10):
    for j in range(1,10):
        ji=i * j
        print '%s * %s = %s' % (i,j,ji)


'''
作业一功能ok

作业二:    考虑和预期有什么差异，由什么原因导致
            a.print打印内容后会自动换行
            b.line 20打后不想换行,与a冲突     ==> 通过在print最后添加逗号来不打印换行
            c.在循环完j后需要有一个换行       ==> line21 通过print ''添加换行
'''

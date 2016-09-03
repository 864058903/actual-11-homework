#-*- encoding: utf-8 -*-
'''
Created on 2016/8/30 0030
@author: dongange
题目：打印乘法口诀表
'''
for i in range(10):
    for j in range(i):
        Num = int(i) * int(j+1)
        print '%s*%s=%s  ' % (j+1, i, Num),
    print '\n'

'''
功能ok, 但每一行乘法口诀中多个一个空行，原因line 11导致
问题原因:
a. print打印内容后会自动换行，若希望不还行可在print后添加逗号，line10
b. line 11, print '\n'为打印换行, 而print会再带一个换行
修改：
方法一：参考a, 在print '\n'后添加,
方法二：直接print ''
'''

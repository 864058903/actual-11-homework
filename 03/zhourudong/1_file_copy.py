#!/usr/bin/env python
#condig:utf-8

f = open('file_read.txt','r')
w = open('file_write.txt','w')

a = f.read()
# print a
w.write(a)

f.close()
w.close()

'''
待完善:
    1、指定路径
    2、读写文件不存在时,文件存在时，操作
'''
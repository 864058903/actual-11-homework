#-*- encoding: utf-8 -*-
'''
Created on 2016/9/21 0021
@author: dongange
题目： python实现tail -f
'''

#FilePath = 'test.txt'

#DirFile = open(FilePath, 'r')
#DirFile.seek(0, 2)

#line = ''
#while True:
#    line += DirFile.readline()
#    if line.endswith('\n'):
#        print line,
#        line = ''

#encoding: utf-8
path = 'test.txt'

fhandler = open(path, 'r')
fhandler.seek(0, 2) #移动文件指针到末尾
line = ''
while True:
    line += fhandler.readline()
    if line.endswith('\n'):
        print line,
        line = ''

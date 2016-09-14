#!/usr/bin/env python
#encoding:utf-8
import os,time
t_file='test.txt'
f=open(t_file,'r')
print f.read(),
f.seek(0,2)
line=''
while True:
    if not os.path.exists(t_file):
       print '\033[31;1mFile does not exist.\033[0m'
       exit()
    
    line += f.readline()  
    if line.endswith('\n') :
         print line,
         line=''

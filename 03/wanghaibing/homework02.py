#!/usr/bin/env python
#encoding:utf-8
import os,sys,time
while True:
    source_file=raw_input('Please input to copy file/exit: ').strip()
    if source_file == 'exit':
        exit()
    #判断被拷贝的文件是否异常
    if not  os.path.exists(source_file) or not os.path.isfile(source_file):
        print '\033[31;1mPath or file is error.\033[0m'
        time.sleep(1)
        continue
    
    while True:    
        new_file=raw_input('Where file copy? : ').strip()
        #判断新文件是否异常
        if len(new_file) ==0 or os.path.basename(new_file) == '' :
             print '\033[31;1mPath or file is error.\033[0m'
             time.sleep(1)
             continue
        elif os.path.exists(new_file):
             print '\033[31;1mFile is exist.\033[0m'
             time.sleep(1)
             continue
        else:
             break
   
    #拷贝文件
    source_f=open(source_file,'rb').read()
    new_f=open(new_file,'wb')
    new_f.write(source_f)
    new_f.close()
   
    #打印拷贝结果，输出新文件及所在目录，新文件用不同颜色标识
    new_fpath=os.path.dirname(new_file)
    if len(new_fpath) == 0:
       new_fpath='./'
       new_fpath2='In the current directory'
    else:
       new_fpath2=new_fpath
    new_fname=os.path.basename(new_file)
    new_flist=os.listdir(new_fpath)
    print '\033[32;1m%s :\033[0m' % new_fpath2
    for i in range(len(new_flist)):
        if new_flist[i] == new_fname:
            print '\033[31m%s\033[0m' % new_fname
        else:
            print new_flist[i]
    print '\033[32;1mFile copy success.\033[0m'

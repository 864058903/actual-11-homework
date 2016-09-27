#!/usr/bin/evn python
#encoding:utf-8
#arg1:要处理的WEB日志文件;arg2:处理后的文件;arg3:0、False,按访问量升序排序,1、True按降序排序;agr4:名次数量
def sorts(log_file,dst_file,y=1,n=10):
   r_file=open(log_file,'rb')
   w_file=open(dst_file,'wb')
   r_dict={}
   tmplist=[]
   num=1
   for line in r_file:
       key=line.split()
       key=key[0],key[8],key[10]
       r_dict[key]=r_dict.setdefault(key,0)+1

   tmplist=sorted(r_dict.items(),key=lambda r_dict:r_dict[1],reverse=y)
   for i in tmplist:
        if num <= n:
           w_file.write('%s %s\n' %(i[1],i[0]))
           num += 1
   r_file.close()
   w_file.close()
   return 'OK,Please check file: %s' %dst_file

if __name__=='__main__':
    sorts('www_access_20140823.log','logsort.txt',1,10)
    print  open('logsort.txt','r').read()

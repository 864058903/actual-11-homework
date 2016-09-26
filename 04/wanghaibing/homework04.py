#!/usr/bin/evn python
#encoding:utf-8

def sorts(log_file,y=1,n=10):
   r_file=open(log_file,'rb')
   r_dict={}
   tmplist=[]
   num=1
   for line in r_file:
       key=line.split()
       key=(key[0],key[8],key[10])
       r_dict[key]=r_dict.setdefault(key,0)+1
   for k,v in r_dict.items():
       tmplist.append((k,v))

   tmplist=sorted(tmplist,key=lambda x:x[1],reverse=y)
   for i in tmplist:
        if num <= n:
           print '%s_%s: \033[31;1m%s\033[0m %s' %('后'+str(n) if y==0 else '前'+str(n),num,i[1],i[0])
           num += 1
if __name__=='__main__':
   #arg1:处理日志文件函数，arg2:0、False，按访问量升序排序;1、True按降序排序。agr3:名次数量
    sorts('www_access_20140823.log',1,10)


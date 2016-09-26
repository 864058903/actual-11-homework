#!/usr/bin/evn python
#encoding:utf-8

def www_log(log_file):
   r_file=open(log_file,'rb')
   r_dict={}
   alist=[]
   for line in r_file:
       key=line.split()
       key=(key[0],key[8],key[10])
       r_dict[key]=r_dict.setdefault(key,0)+1
   for k,v in r_dict.items():
       alist.append((k,v))
   return alist

def sorts(x,y=1,n=10):
    num=1
    tmp_list=sorted(x,key=lambda x:x[1],reverse=y)
    for i in tmp_list:
        if num <= n:
           print '%s_%s: \033[31;1m%s\033[0m %s' %('后'+str(n) if y==0 else '前'+str(n),num,i[1],i[0])
           num += 1
if __name__=='__main__':
   #arg1:处理日志文件函数，arg2:0、False，按访问量升序排序;1、True按降序排序。agr3:名次数量
    sorts(www_log('www_access_20140823.log'),1,10)


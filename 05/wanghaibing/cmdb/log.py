#!/usr/bin/evn python
#encoding:utf-8
def get_topn(log_file,topn=110):
   r_file=open(log_file,'rb')
   r_dict={}
   for line in r_file:
       key=line.split()
       key=key[0],key[8],key[10]
       r_dict[key]=r_dict.setdefault(key,0)+1

   r_file.close()
   result=sorted(r_dict.items(),key=lambda x:x[1])
   return result[:-topn-1:-1]

if __name__=='__main__':
     get_topn('www_access_20140823.log')

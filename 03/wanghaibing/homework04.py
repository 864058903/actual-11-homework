#!/usr/bin/env python
#encoding:utf-8
r_file='www_access_20140823.log'
r_f=open(r_file,'r')
f_list=[]
f_dict={}
num=0
for line in r_f.readlines():
    r_line=line.split()
    r_line2=(r_line[0],r_line[8],r_line[10])
    f_list.append(r_line2)    
#print f_list

for i in f_list:
    f_dict[i]=f_dict.setdefault(i,0)+1
#print f_dict

print ' WWW_LOG_COUNT '.center(50,'#')
for k,v in f_dict.items():
    if num %2 == 0: 
       print '\033[32;1mIp&Url :\033[0m %s\n\033[32;1mCount:\033[0m \033[32;1m%s\033[0m' %(k,v)
    else: 
       print '\033[31;1mIp&Url :\033[0m %s\n\033[31;1mCount:\033[0m \033[31;1m%s\033[0m' %(k,v)
    num += 1
print ' \033[31;1mLines: %s\033[0m '.center(50,'#') %num

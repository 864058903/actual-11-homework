#!/usr/bin/env python 
#coding=utf8

with  open('www_access_20140823.log','r') as f:
    zd={}
    for  i in  f.readlines():
        s=i.split(" ")
        ip,url,code=s[0],s[6],s[8]
        #print ip,url,code
        zd[ip,url,code]=zd.get((ip,url,code),0)+1
print zd
#print  sorted(zd.items(),key=lambda x:x[1],reverse=True)

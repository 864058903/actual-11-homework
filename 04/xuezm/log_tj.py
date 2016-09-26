#!/usr/bin/env python 
#coding=utf8

def access_log_tj(logpath,dsplogpath,topn):
    with  open(logpath,'r') as f:
        zd={}
        for  i in  f.readlines():
            s=i.split(" ")
            ip,url,code=s[0],s[6],s[8]
            #print ip,url,code
            zd[ip,url,code]=zd.get((ip,url,code),0)+1
    #print zd
    result= sorted(zd.items(),key=lambda x:x[1],reverse=True)
    result=result[:topn]
    with open('dsp.log','w+') as f:
        for  i in   result:
            f.write(str(i)+'\n')
    return "success"

if  __name__   == "__main__":
     print access_log_tj('access.log','dsp.log',10)

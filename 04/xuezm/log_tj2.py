#!/usr/bin/env python 
#coding=utf8

def access_log_tj(logpath,dsplogpath,topn=10):
    with  open(logpath,'r') as f:
        zd={}
        for  i in  f.readlines():
            s=i.split(" ")
            ip,url,code=s[0],s[6],s[8]
            zd[ip,url,code]=zd.get((ip,url,code),0)+1
    result= sorted(zd.items(),key=lambda x:x[1],reverse=True)
    with open('dsp.log','w+') as f:
	s =1
        for  k,v in  result:
            f.write('%s %s\n' %(" ".join(k),str(v)))
	    if s>=topn:
	        break
	    s+=1
	    
    return "success"

if  __name__   == "__main__":
    print access_log_tj('access.log','dsp.log',10)

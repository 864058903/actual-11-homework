#coding=utf8
#Python第二周作业
#整理课堂知识点
#作业0：总结知识点、及复习之前知识点
#作业一：copy文件，win加b
#思路：
#判断拷贝的文件名是否存在，不存在进行新建
#如果拷贝window环境文件，
#encoding: utf-8
file1 = 'access.log'
file2 = 'access_copy.log'
src1 = open(file1, 'r')
dest2 = open(file2, 'w')
size = 1024
while True:
    cxt = src1.read(size)
    if not cxt:
        break
    dest2.write(cxt)
src1.close()
dest2.close()


#作业二：实现tail 功能 tail -f 循环读取
#指定文件为：access.log（没有思路）


#统计/home/share/www_access_20140823.log
#日志信息：ip,url,code==>cnt
files=open('access.log')
ip_cnt={}
url_cnt={}
code_cnt={}
temp=files.readlines()
for i in temp:
	tmp=i.split(' ')
	ip_cnt[tmp[0]]=ip_cnt.get(tmp[0],0)+1
	url_cnt[tmp[6]]=url_cnt.get(tmp[6],0)+1
	code_cnt[tmp[8]]=code_cnt.get(tmp[8],0)+1
files.close()
print ip_cnt
print url_cnt
print code_cnt

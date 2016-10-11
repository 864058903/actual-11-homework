#coding:utf8

def openfile(path,topn=10):
	#  临时
	dt = {}
	f = open(path,'r')
	while 1:
		a = f.readline()
		if a == '':
			break
		b = a.split()
		ip, url, status = b[0], b[6], b[8]
		key = (ip,url,status)
		dt[key] = dt.setdefault(key,0) + 1
	f.close()
	ex2 = sorted(dt.items(),key=lambda x: x[1],reverse=True)
	ex3 = ex2[:topn]
	for all,cnt in ex3:
		print all[0],all[1],all[2],cnt

openfile('access.log',10)

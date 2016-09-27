#encoding:utf-8
log1 = '/home/chw/python/03/access.log'
log2 = '/home/chw/python/04/logsort.log'
def openfile(log_srcpath,log_dstpath,topn=10):
    cnts = {}
    logfile = log_srcpath
    fhandler = open(logfile,'r')
    for line in fhandler:
        ip,url,stats = line.split()[0],line.split()[6],line.split()[8]
        cnts[(ip,url,stats)] = cnts.get((ip,url,stats),0) + 1
    fhandler.close()
    cnts_list = cnts.items()
    for i in range(0,len(cnts_list) -1):
        for j in range(0,len(cnts_list) -1 -i):
            if cnts_list[j][1] > cnts_list[j+1][1]:
                cnts_list[j],cnts_list[j+1] = cnts_list[j+1],cnts_list[j]
    fhandler_dst = open(log_dstpath,'w')
    cnts_top = cnts_list[-1:-topn-1:-1]
    for x in cnts_top:
        fhandler_dst.write('ip {} url {} tatus {} cnt {}\n' .format(x[0][0],x[0][1],x[0][2],x[1]))

    fhandler_dst.close()
if __name__=='__main__':
    openfile(log1,log2,8)
    print open(log2,'r').read()

#encoding:utf-8

cnts = {}
logfile = '/home/chw/python/03/access.log'
fhandler = open(logfile,'r')
# print fhandler.readline()
for line in fhandler:
    # print line
    # mylist = line.split()
    # print mylist
    ip,url,stats = line.split()[0],line.split()[6],line.split()[8]
    cnts[(ip,url,stats)] = cnts.get((ip,url,stats),0) + 1

fhandler.close()
# print cnts
cnts_list = cnts.items()
for i in range(0,len(cnts_list) -1):
    for j in range(0,len(cnts_list) -1 -i):
        if cnts_list[j][1] > cnts_list[j+1][1]:
            cnts_list[j],cnts_list[j+1] = cnts_list[j+1],cnts_list[j]

# print cnts_list
# print cnts_list[-1:-5:-1]
cnts_top = cnts_list[-1:-5:-1]
for x in cnts_top:
    # print "ip is %s  url is %s  status is %s  cnt is %s" %(x[0][0],x[0][1],x[0][2], x[1])
    print('ip {} url {} tatus {} cnt {}' .format(x[0][0],x[0][1],x[0][2],x[1]))



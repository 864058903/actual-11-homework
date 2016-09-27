#encoding:utf-8

def loganalysis(logfile, dstpath, topn=10):

    fhandler = open(logfile, 'r')

    rt_dict = {}
    # 统计
    while True:
        line = fhandler.readline()
        if line == '':
            break

        nodes = line.split()
        ip, url, code = nodes[0], nodes[6], nodes[8]
        key = (ip, url, code)
        if key not in rt_dict:
            rt_dict[key] = 1
        else:
            rt_dict[key] = rt_dict[key] + 1

    fhandler.close()
    #print rt_dict

    # 排序
    rt_list = rt_dict.items()
    # [(key, value), (key, value)]

    for j in range(0, topn):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                temp = rt_list[i]
                rt_list[i] = rt_list[i + 1]
                rt_list[i + 1] = temp

    #fhandler = open('result.txt', 'w')
    for node in rt_list[-1:- topn - 1:-1]:
        fhandler = open(dstpath, 'a')
        #((ip, url, code), value)
        fhandler.write('%s %s %s %s\n' % (node[1], node[0][0], node[0][1], node[0][2]))
        fhandler.close()
    #fhandler.close()

if __name__ == '__main__':
    logfile = 'www_access_20140823.log'
    dstpath = 'result.txt'

    loganalysis(topn=10, logfile=logfile, dstpath=dstpath)

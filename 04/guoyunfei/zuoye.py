# coding: utf-8
#

#log日志统计
#将cnt排序，取出TOP10（函数，logpath,dstpath,topn=10）
def func_logstat(logpath, dstpath, topn=10):
    res = {}
    with open(logpath) as fs, open(dstpath, 'w') as fd:
        for line in fs:
            mess = line.strip().split()
            stat = mess[0], mess[6], mess[8]
            res[stat] = res.get(stat, 0) + 1
        sort_res = sorted(res.items(), key=lambda x:x[1], reverse=True)[:topn+1]
        for value in sort_res:
            fd.write('{0} {1}\n'.format(' '.join(value[0]), value[1]))
           
           
#排序
#unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
#使用元组的最大值进行排序
unsort_list = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
sort_list = sorted(unsort_list, key=lambda x:max(x))
print(sort_list)

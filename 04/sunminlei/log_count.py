#!/usr/bin/env python
# -*- coding: utf-8 -*-


def log_count(logdir, dstpath, topn=10):
    stat_dict = {}
    fhandler = open(logdir, 'rb')
    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1
    fhandler.close()
    rt_list = stat_dict.items()

    fhandler = open(dstpath, 'wb')
    for j in range(0, topn):
        for i in range(0, len(rt_list) - 1):
            if rt_list[i][1] > rt_list[i + 1][1]:
                rt_list[i+1], rt_list[i] = rt_list[i], rt_list[i+1]
    for node in rt_list[-1:-topn - 1:-1]:
        fhandler.write('%s %s\n' % (' '.join(node[0]), node[1]))
    fhandler.close()


if __name__ == '__main__':
    logdir = 'access_120101.log'
    dstpath = 'top10_result.txt'
    topn = 10
    log_count(logdir, dstpath, topn)

#!/usr/bin/env python
# coding: utf-8
# author: Xiao Guaishou
 
try:
    import psutil
except ImportError:
    print('Error: psutil module not found!')
    exit()
 
# 函数获取各网卡发送、接收字节数
def get_key():
 
    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称
    key_info.remove('lo')
	
    recv = {}
    sent = {}
 
    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数
 
    return key_info, recv, sent
 
# 函数计算每秒速率
def get_rate(func):
 
    import time
 
    key_info, old_recv, old_sent = func()  # 上一秒收集的数据
 
    time.sleep(2)
 
    key_info, now_recv, now_sent = func()  # 当前所收集的数据
 
    net_in = {}
    net_out = {}
 
    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024.0 /1024.0)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024.0/1024.0)  # 每秒发送速率
 
    return key_info,net_in,net_out
 
 
while True:
    try:
         key_info, net_in,net_out = get_rate(get_key)
 
         for key in key_info:
             print('%s\nInput:\t %-5sMB/s\nOutput:\t %-5sMB/s\n' % (key, round(net_in.get(key),2), round(net_out.get(key),2)))
    except KeyboardInterrupt:
        exit()
 
# End

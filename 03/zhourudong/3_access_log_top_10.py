#!/usr/bin/env python
#coding:utf-8
# from time import sleep

filepath = '/home/share/www_access_20140823.log'
f = open(filepath,'r')

kv = {}
for line in f:
    '''
    分隔字符串为列表
    0是ip , 6是URL ，8是状态码
    
    判断是否在字典中
        在 value += 1
        不在 value = 1
    '''
    a = line.split()
    ip = a[0]
    url = a[6]
    status = a[8]
    k = (ip,url,status)
    if k in kv:
        kv[k] = kv.get(k) + 1
    else:
        kv[k] = 1

f.close()

sort_values = kv.items()
# 转换成[ (key1,value1),(key2,value2)...(key3,value3)] 形式的列表

tem_sort = []
for j in sort_values:
    # t = [j[1],j[0]]
    # 遍历列表将key ，value 翻转
    tem_sort.append([j[1],j[0]])

# 排序(从大到小)
tem_sort.sort(reverse=True)

# 取出最后十个
for last10 in (tem_sort[:10]):
    print str(last10[1])+ ': ' +str(last10[0])












'''
log format:
61.159.140.123 - - [23/Aug/2014:00:01:42 +0800] "GET /favicon.ico HTTP/1.1" 404 \ "-" "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER" "-"

output format:
('118.112.143.148', '/images/cursor_zoom.cur', '404'): 674
('118.112.143.148', '/images/cursor_minify.cur', '404'): 662
('221.12.76.53', '/images/cursor_zoom.cur', '404'): 220
('221.12.76.53', '/images/cursor_minify.cur', '404'): 218
('123.174.51.164', '/public/themes/adreambox/public.css?20110820', '200'): 116
('123.174.51.164', '/public/themes/adreambox/menu.css', '200'): 116
('123.174.51.164', '/public/themes/adreambox/main.css?20110820', '200'): 116
('123.174.51.164', '/public/themes/adreambox/link.css', '200'): 116
('123.174.51.164', '/public/themes/adreambox/layout.css?20110820', '200'): 116
('123.174.51.164', '/public/themes/adreambox/images/btn_top.gif', '200'): 116
'''


















# values_list = kv.values()
# values_list.sort()
# '''  拿出字典所有值进行排序 '''
#
# num = 1
# new_list = []
#
#
# list_len = len(tem_sort)
# while (list_len - 1) > 0 and (num < 11):
#     '''
#     取出最大的10个values
#     排除以下情况：
#         1、当字典 len(dict) < 10
#         2、当字典中有相同的value (100 个key出现的values一样)
#     '''
#     if values_list[-num] < values_list[-(num+1)]:
#         new_list.append(values_list[-num])
#         num += 1
#         list_len -= 1
#
# for last in new_list:



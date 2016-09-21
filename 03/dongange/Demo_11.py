#-*- encoding: utf-8 -*-
'''
Created on 2016/9/21 0021
@author: dongange]
题目：Nginx 日志分析
'''

LogCnt = {}
LogCnt['URLNum'] = 0

IPCnt = {}

LogFilePath = 'www_access_20160921.log'
LogDir = open(LogFilePath, 'r')

line = LogDir.readline()

while line:
    SourceIp = line.split('\t')[1]
    URI = line.split('\t')[6]
    Code = line.split('\t')[8]

    if SourceIp in IPCnt:
        IPCnt[SourceIp] = IPCnt[SourceIp] + 1
    else:
        IPCnt[SourceIp] = 1

    if URI:
        LogCnt['URLNum'] = LogCnt['URLNum'] + 1

    if Code in LogCnt:
        LogCnt[Code] = LogCnt[Code] + 1
    else:
        LogCnt[Code] = 1

    line = LogDir.readline()

print LogCnt
print IPCnt

LogDir.close()

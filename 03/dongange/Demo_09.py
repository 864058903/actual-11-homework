#-*- encoding: utf-8 -*-
'''
Created on 2016/9/21 0021
@author: dongange
题目：copy文件
'''
SourceFile = 'www_access_20160921.log'
TargetFile = 'www_access_20160921.log.bak'

Source = open(SourceFile, 'rb')
Target = open(TargetFile, 'wb')

Target.write(Source.read())

Source.close()
Target.close()

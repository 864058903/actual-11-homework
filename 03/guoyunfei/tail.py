#coding: utf-8
#

FILE = './test'
with open(FILE) as f:
    line = ''
    f.seek(0,2)
    while True:
        line += f.readline()
        if line.endswith('\n'):
            print(line.strip())
            line = ''

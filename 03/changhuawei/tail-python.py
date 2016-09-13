#encoding:utf-8
#tail -f 功能
filename = '/home/chw/a.sh'

fhandler = open( filename,'r')
fhandler.seek(0,2)
line = ''
while True:
    line += fhandler.readline()
    if line.endswith('\n'):
        print line,

    line = ''
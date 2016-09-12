#encoding: utf-8

srcpath = 'www_access_20140823.log'
dstpath = 'zz.log'

srchandler = open(srcpath, 'r')
dsthandler = open(dstpath, 'w')
size = 1024

while True:
    cxt = srchandler.read(size)
    if not cxt:
        break
    dsthandler.write(cxt)

dsthandler.close()
srchandler.close()
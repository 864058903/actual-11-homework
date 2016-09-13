#!/usr/bin/env python3
#coding: utf-8
#

SRC_PATH = './test'
DEST_PATH = './test.bak'
SIZE = 1024


with open(SRC_PATH) as fs, open(DEST_PATH, 'w') as fd:
    while True:
        line = fs.read(SIZE)
        if line:
            fd.write(line)
        else:
            break
        

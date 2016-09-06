#!/usr/bin/env python
alist=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
blist=[]
for i in alist:
    num=0
    for j in blist:
       if i == j:
           num=1
           break
    if num == 0:
       blist.append(i)
print blist


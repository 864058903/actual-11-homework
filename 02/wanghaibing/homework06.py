#!/usr/bin/env python
def px_(alist,px):
  if px == 'sx':
     for i in range(len(alist)):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1] :
                alist[j],alist[j+1]=alist[j+1],alist[j]
  if px == "jx":
     for i in range(len(alist)):
        for j in range(-1,-len(alist),-1):
            if alist[j] > alist[j-1] :
                alist[j],alist[j-1]=alist[j-1],alist[j]
  print alist

px='sx'
pxlist=[]
while True:
    astr=raw_input('Please input num/(sx/jx)/exit:  ')
    if astr == 'exit':
       px_(pxlist,px)
       exit()
    if astr == 'sx' or  astr == 'jx':
       px=astr
       px_(pxlist,px)
       continue
    else:
       pxlist.append(int(astr))
       px_(pxlist,px)

'''
功能ok
'''

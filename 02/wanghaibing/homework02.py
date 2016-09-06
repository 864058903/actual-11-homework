#!/usr/bin/env python
alist=[10,9,8,7,6,5,4,3,2,1]
#print alist
for i in range(len(alist)):
  for j in range(len(alist)-1-i):
       if alist[j] > alist[j+1] :
          alist[j],alist[j+1]=alist[j+1],alist[j]
print   alist

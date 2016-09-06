#!/usr/bin/env python
aa=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
max=aa[0]
temp=0
for i in aa:
  if i > max:
      temp=max
      max=i
      max2=temp
  elif i > temp and i != max:
      temp=i
      max2=temp
print 'the first max: %s \nthe second max: %s' % (max,max2)

  

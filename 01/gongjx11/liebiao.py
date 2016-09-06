#!/usr/bin/env python
aa=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
a=aa

mike = max(a)
a.remove(mike)
while True:
  mike2 = max(a)
  if mike2 == mike:
    a.remove(mike2)
  else:
    break
print mike,mike2


  

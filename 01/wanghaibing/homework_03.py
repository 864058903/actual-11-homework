#!/usr/bin/evn python
#search the first max  and the second max
_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
#print _list
max_1=_list[0]
temp=0
for n in _list:
    if n > max_1:
        temp=max_1
        max_1=n
        max_2=temp
print 'The first max: %s \nThe second max: %s' % (max_1,max_2)
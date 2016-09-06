#!/usr/bin/env python
#encoding:utf-8
while True:
    year = raw_input('Please input year:')
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print '%s is Leap Year!'%(year)
    else:
        print "%s is Not Leap Year!" %(year)
    


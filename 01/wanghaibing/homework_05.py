#!/usr/bin/env python
#Guess a number game
import random
num=random.randint(0,100)
#print 'num: %s ' % num
while True:
    in_num=raw_input('Please enter a number you guess: ')
    if int(in_num) == num:
        print 'result: yes'
        exit()
    elif int(in_num) > num:
        print 'result: %s big' % in_num
    elif int(in_num) < num:
        print 'result: %s small' % in_num
    else:
        print 'You input error.' % in_num

'''
功能ok
'''

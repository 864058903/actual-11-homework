#coding: utf-8

import random
num = random.randint(0,100)

max_num = 100
min_num = 0
print num

while True:
    value = raw_input('Enter a number: ')
    value = int(value)

    if value == num:
        print 'hah, congratulations!'
        break

    elif value > num:
        print '%s To %s' % (min_num,value)
        max_num = value

    elif value < num:
        print '%s To %s' % (value,max_num)
        min_num = value


'''
功能ok
'''

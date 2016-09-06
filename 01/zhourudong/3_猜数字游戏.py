#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
random_num = random.randint(0, 100)
user_input = int(raw_input('please input a number:'))

while user_input != random_num:
    print 'Error,try again:',
    user_input = int(raw_input())
print 'Good!数字为:%s,你猜对了,但是没有奖励' % (user_input)


'''
功能ok, 在猜错时可以给一个提示，猜大了还是猜小了, 然后自己玩下，怎么能快速猜到结果
'''

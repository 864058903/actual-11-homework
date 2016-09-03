#!/usr/bin/python
#encoding: utf-8
import random
secret=random.randint(0, 100)
guess=0
tries=0
print "我们来做猜数字游戏，下面请输入一个数值!"
print "这是一种数字1到100的猜数字游戏,我给您5次猜数字的机会!"
while guess != secret and tries < 5:
    guess=input("请您输入数字:")
    if guess < secret:
        print "您猜的数字太小啦!\n"             

    elif guess > secret:
        print "您猜的数字太大啦!\n"
    tries=tries+1
if guess == secret:
        print "恭喜您猜对啦! "
else:
        print "您已经猜了多次都不正确!祝您下次好运!"
        print "下面我来告诉您这个数值是",secret

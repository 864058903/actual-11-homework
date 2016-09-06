#!/usr/bin/python
# ^_^ coding: utf-8 ^_^
import random
print "----------猜数字游戏开始啦-----------"
while True:
    number = raw_input('please input a number:')
    number = int(number)
    rnum = random.randint(0,100)
    if number == rnum:
        print "---恭喜你！猜对了---"
        break
    else:
        print "---哦哦,你猜错了哦,继续加油哦---"


'''
功能ok, 在猜错时可以给一个提示，猜大了还是猜小了, 然后自己玩下，怎么能快速猜到结果
'''

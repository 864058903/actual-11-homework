#coding: utf-8
#
import random


# 计算最大的两个数字
print
print
print '###取出最大的两个数字###'
orign = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
max_number, second_number = 0, 0
for num in orign:
    if num > second_number:
        if num > max_number:
            second_number = max_number
            max_number = num
        if num < max_number:
            second_number = num
print 'orign: %s' % orign
print 'max_number: %s' % max_number
print 'second_number: %s' % second_number


# 乘法表
print
print
print '###乘法表###'
for x in range(1, 10):
    end = x + 1
    for y in range(1, end):
        value = x * y
        print '%s * %s = %s' % (x, y, value),
    print


# 猜数字游戏
print
print
print '###猜数字游戏###'
ranumber =  random.randint(0, 100)
number = raw_input('请输入数字: ')
if int(number) == ranumber:
    print '恭喜,猜对了数字%s' % number
else:
    print '对不起,猜错了,下次再试'



'''
功能ok, 在猜错时可以给一个提示，猜大了还是猜小了, 然后自己玩下，怎么能快速猜到结果
'''

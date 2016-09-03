#encoding utf-8

import random
num1 = random.randint(0, 100)

while True:
	num2 = raw_input('please input  a mum:')
	num2 = int(num2)
	if num2 != num1:
		print "you input is error"
		continue
	elif num2 == num1:
		print "you input true num: " '%s ' % num2
		break


'''
功能ok, 在猜错时可以给一个提示，猜大了还是猜小了, 然后自己玩下，怎么能快速猜到结果
'''

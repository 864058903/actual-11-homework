#encoding=utf-8
#author:yudingchu
#功能计算最大的两个数字(两个数字不能重复)
test_list=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
# test_dict={}
# for i in test_list:
# 	if i in test_dict:
# 		test_dict[i]+=1
# 	else:
# 		test_dict[i]=1
# test_list2=test_dict.keys()
# print test_list2
max_value=0
sec_value=0
for i in test_list:
	if max_value>i:
		if sec_value<i:
			sec_value=i
	elif max_value<i:
		temp=max_value
		max_value=i
		if sec_value<temp:
			sec_value=temp
print "max value is  %d ,and second value is %d " %(max_value,sec_value)

# 打印乘法口诀
#i * j =格式
#1*1=1
#1*2=2 2*2=4
#1*3=3 2*3=6 3*3=9
for i in range(1,10):
	for j in range(1,i+1):
		print "%d * %d = %d " %(j,i,i*j),
	print ""

#5. 猜数字游戏
#系统生成一个随机的数字
import random
temp=random.randint(0, 100)
# print temp
while True:
	test_num=int(raw_input("please input number"))
	if test_num > temp:
		print "too big,please try again"
		continue
	elif test_num <temp:
		print "too small,please try again"
		continue
	else:
		print "you are good !!!"
		break

'''
功能ok, 考虑line 45,48是否需要
'''

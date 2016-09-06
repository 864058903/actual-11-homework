#encoding: utf-8


num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
max_num1 = None
max_num2 = None
for x in num:
	if max_num1 is None:
		max_num1 = x
	else:
		if max_num1 < x:
			max_num1 = x


for y in num:
	if max_num2 is None:
		max_num2 = y
	elif max_num2 < y and y != max_num1:
		max_num2 = y

print 'max_num1 is:%s' % max_num1
print 'max_num2 is:%s' % max_num2
			
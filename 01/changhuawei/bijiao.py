#encoding:utf-8
#filename:bijiao.py
#changhuawei

nums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
max_num1 = None
max_num2 = None
for x in nums:
    if max_num1 is None:
        max_num1 = x
    if max_num2 is None:
        max_num2 = x
    if x > max_num2:
        if x > max_num1:
            max_num2 = max_num1
            max_num1 = x
        if x < max_num1:
            max_num2 = x
print 'max_num1 is %s \nmax_num2 is %s' % (max_num1,max_num2)
print 'done'


'''
功能ok
'''

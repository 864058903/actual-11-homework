#encoding: utf-8

num_list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

a = None
b = None

for i in num_list:
    if a is None:
        a = i
    elif i > a:
        b = a
        a = i
    elif b is None:
        b = i
    elif i > b:
        b = i

print 'first:%s, second:%s' % (a, b)

'''
功能ok
'''

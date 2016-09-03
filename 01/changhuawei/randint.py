#encoding:utf-8

import random

nums1 = random.randint(0, 100)
while True:
    pass
    nums2 = int(raw_input('please input num:'))
    if nums1 == nums2:
        print '输入匹配正确'
        break
    else:
        print '输入不匹配再接再厉'
print  'done'

'''
功能ok, 在猜错时可以给一个提示，猜大了还是猜小了, 然后自己玩下，怎么能快速猜到结果
'''

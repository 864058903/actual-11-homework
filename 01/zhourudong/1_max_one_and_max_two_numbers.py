#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 3. 计算[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45] 最大的两个数字(两个数字不能重复)

list_2_num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]

max_num_one = list_2_num[0] # 防止有负数情况，初始值不赋为0.
max_num_two = list_2_num[0]

for i in list_2_num:
	if i > max_num_one:
		max_num_two = max_num_one
		max_num_one = i
	elif i > max_num_two and i != max_num_one:
		max_num_two = i

print 'The max_num_one is:%s , max_num_two is:%s' % (max_num_one,max_num_two)

# 解决思路--> 扑克牌例子: 左手的牌永远小于右手的牌,
# ①当右手拿到更大的牌时，将右手边的牌给左手，
# ②当拿到的牌比右手小但是比左手大，则对左手牌进行替换;以此方法最终找到两个最大的数以及次大的数

# ==========================================================================
# 方法2

list_2 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
i = list_2[0]
d = list_2[0]
for a in list_2:
    if a > i:
        i = a
d = list_2[0]

for c in list_2:
    if c > d and c != i:
        d = c
print  'max_num_one: %s ,max_num_two: %s'%(i,d)

# 第一回循环取出最大的数， 第二回取出次大的数， 劣质方法!!

'''
功能ok
'''

#coding: utf-8

nums = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]

new_nums = set(nums)
max_num = max(new_nums)

new_nums.remove(max_num)
sec_num = max(new_nums)

print max_num, sec_num

print "==========="

new_nums = sorted(nums, reverse = True)
max_num = new_nums[0]

for i in new_nums:
    if i != max_num:
        sec_num = i
        break

print max_num, sec_num

print "==========="

max_num = 0

for num in nums:
    if num > max_num:
        max_num = num

for num in nums:
    if num != max_num and num > sec_num:
        sec_num = num

print max_num, sec_num

print "=========="

max_num = sec_num = 0

for num in nums:
    if max_num < num:
        sec_num = max_num
        max_num = num
    elif max_num == num:
        continue
    else:
        if sec_num < num:
            sec_num = num

print max_num, sec_num


'''
功能ok
'''

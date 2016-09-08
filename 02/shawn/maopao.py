#!/usr/bin/env python
#encoding: utf-8
#autho = shawn

nums = [123,23,1,23,13,4,2,14,1]
print nums, '\n'

# exchange two value: a,b = b,a
# j ---> 次数
# i ---> 索引项

for j in range(len(nums) - 1):
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			x = nums[i+1]
			nums[i+1] = nums[i]
			nums[i] = x
print nums

nums = [123,23,1,23,13,4,2,14,1]

for j in range(len(nums)-1):
    for i in range(len(nums)-1-j):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

print nums

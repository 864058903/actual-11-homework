#!/usr/bin/env python
#encoding: utf-8

nums = [23,2,1,23,2223,232,1,133,44]
print nums

for i in range(len(nums) / 2):
    nums[i], nums[-1 - i] = nums[-1 - i], nums[i]


print nums

nums = [23,2,1,23,2223,232,1,133,44]
nums.reverse()
print nums

'''
功能ok
'''

#!/usr/bin/env python
array = [1,2,3,6,5,4,9,7,8,11,13,10,12]
for i in range(len(array)):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print array

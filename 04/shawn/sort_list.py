#encoding: utf-8

unsort_list = [(1,2), (6,3), (4,1), (2,10), (3,5), (5,7)]

result = sorted(unsort_list, key= lambda x : x[0] if x[0] > x[1] else x[1], reverse = True)

print result

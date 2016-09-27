#encoding: utf-8

print '*' * 20

unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]

unsort_list2.sort(cmp=lambda x, y:0 if max(x) > max(y) else -1)

print unsort_list2

print '*' * 20

unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]

unsort_list2.sort(key=lambda x:max(x))

print unsort_list2

print '*' * 20

unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]

unsort_list = sorted(unsort_list2,cmp=lambda x, y:0 if max(x) > max(y) else -1)

print unsort_list

print '*' * 20

unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]

unsort_list = sorted(unsort_list2,key=lambda x:max(x))

print unsort_list
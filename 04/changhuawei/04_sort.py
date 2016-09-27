#encoding:utf-8
#使用元组的最大值进行排序

#1
unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
unsort_list2.sort(lambda x,y:cmp(x[1],y[1]),reverse=False)
print unsort_list2

#2
unsort_list3 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
unsort_list3.sort(key=lambda x:x[1])
print unsort_list3

#3
unsort_list4 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
print sorted(unsort_list4,key = lambda x:x[1])

#4

def _sort(x,z=False):
    return sorted(x,key = lambda x:x[1],reverse=z)
# print globals()

if __name__== '__main__':

    unsort_list5 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
    print _sort(unsort_list5,False)

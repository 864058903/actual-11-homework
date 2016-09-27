#encoding: utf-8


cmp_value = lambda a, b:a > b
get_tuple_key = lambda x:max(x)

def bubble_sort(unsort_list,cmp=lambda a, b:a > b,key=lambda x:max(x)):
    length = len(unsort_list)
    for j in range(length - 1):
        for i in range(length - 1):
            a = unsort_list[i]
            b = unsort_list[i + 1]
            if cmp(key(a),key(b)):
                unsort_list[i], unsort_list[i + 1] = unsort_list[i + 1], unsort_list[i]

if __name__ == '__main__':
    unsort_list2 = [(1,2),(6,3),(4,1),(2,10),(3,5),(5,7)]
    bubble_sort(unsort_list2)
    print unsort_list2
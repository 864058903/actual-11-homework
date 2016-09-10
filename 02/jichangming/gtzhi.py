#encoding: utf-8

arr1=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2=[2,1,3,2,43,234,454,452,234,14,21,14]
arr_num=[]
for x in arr1:
	if x  in arr2:
		arr_num.append(x)
		pass



print arr_num

'''
功能有点小问题, 此时arr_num中是否可能存在多个相同的值
'''

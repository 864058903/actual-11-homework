#coding=utf8
#Python第二周作业
#整理课堂知识点
#作业二：冒泡排序（从小到大）
list1=[12,1,5,6,-1,3,19,14,16,16,12]
for i in range(len(list1)-1):
	for j in range(len(list1)-1):
		if list1[j]>list1[j+1]:
			list1[j],list1[j+1] = list1[j+1],list1[j]
print list1
#作业二：冒泡排序（从大到小）
list2=[12,1,5,6,-1,3,19,14,16,16,12]
for i in range(len(list2)-1):
	for j in range(len(list2)-1):
		if list2[j]<list2[j+1]:
			list2[j],list2[j+1] = list2[j+1],list2[j]
print list2
#作业三：数组去重,统计每个数字出现的次数
repeat_list=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
dedu_list=[]
dedu_dict={}
for i in repeat_list:
	if i not in dedu_list:
		dedu_list.append(i)
for i in repeat_list:
	if i in dedu_dict:
		dedu_dict[i]+=1
	else:
		dedu_dict[i]=1
print dedu_list
print dedu_dict
#作业四：求两个数组共同的值（先去重）
arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
arr1_temp=[]
arr2_temp=[]
arr1_arr2_comm=[]
for i in arr1:
	if i not in arr1_temp:
		arr1_temp.append(i)
print arr1_temp
for i in arr2:
	if i not in arr2_temp:
		arr2_temp.append(i)
print arr2_temp
for i in arr1_temp:
	if i in arr2_temp:
		arr1_arr2_comm.append(i)
print arr1_arr2_comm
#作业五：用户输入员工名字和id，名字和id之间用:分隔多个用户 用逗号分隔最终输入所有用户对应id的信息
#比如用户输入user1:119,user2;112,user3:113
#最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
useid=[]
usertemp=[]
while True:
	temp=raw_input('please input user:idno')
	if temp=='exit':
		break
	elif temp not in usertemp:
		usertemp.append(temp)
print usertemp
for i in usertemp:
	useid.append(tuple(i.split(':')))
print useid
#作业六：插入排序插入(从小到大),排序方法分直接插入排序和折半插入排序两种
#直接插入排序(从小到大)
list3=[12,1,5,6,-1,3,19,14,16,16,12]
for i in range(1,len(list3)):
	#设置当前值前一个元素的标识
	j=i-1
	#如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
	if list3[i] < list3[j]:
		temp=list3[i]
		list3[i]=list3[j]
		#继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
		j=j-1
		while j>=0 and list3[j]>temp:
			list3[j+1]=list3[j]
			j=j-1
		list3[j+1]=temp
print list3

#折半插入排序(从小到大)



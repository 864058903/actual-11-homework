list3=[12,1,5,6,-1,3,19,14,16,16,12]
for i in range(1,len(list3)):
	j=i-1
	if list3[i] < list3[j]:
		temp=list3[i]
		list3[i]=list3[j]
		j=j-1
		while j>=0 and list3[j]>temp:
			list3[j+1]=list3[j]
			j=j-1
		list3[j+1]=temp
print list3
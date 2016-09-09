#encoding  utf-8

sum1=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
sum_num=[]
for x in range(len(sum1)-1):
	
	if  sum1[x]  in sum_num:
		continue
	else:
		sum_num.append(sum1[x])

print sum_num

for i in sum1:
	if i not in sum_num:
		sum_num.append(i)
print sum_num	
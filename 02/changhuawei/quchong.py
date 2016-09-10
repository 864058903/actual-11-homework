#encoding:utf-8
#数组去重，先定义空的，比较，如果不在追加
aa = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
bb = []
for i in aa:
	if i not in bb:
            bb.append(i)
print bb

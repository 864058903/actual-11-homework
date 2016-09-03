#encoding: utf-8

num = range(10)
nummax = 0
for x in num:
	if x > 0:
		for y in range(x+1):
			if y > 0:
				nummax = x * y
				print '%s * %s = %s' % (x, y , nummax) ,
		print '\n'




'''
功能ok, 但每一行乘法口诀中多个一个空行，原因line 11导致
问题原因:
a. print打印内容后会自动换行，若希望不还行可在print后添加逗号，line10
b. line 11, print '\n'为打印换行, 而print会再带一个换行
修改：
方法一：参考a, 在print '\n'后添加,
方法二：直接print ''
'''

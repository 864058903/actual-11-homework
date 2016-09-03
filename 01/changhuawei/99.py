#encoding:utf-8

numlist = [1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    x = ''
    # print i
    for j in range(1,i+1):
        # print j
        x = x + str(j) + '*'  + str(i) + '=' + str(i * j) +' '
    print x



for x in range(1,10):
    for y in range(1,x + 1):
        # z = x * y
        print '%s * %s = %s' %(x,y,x*y)
    print '\n'

'''
方法一:    ok
方法二:    考虑和预期有什么差异，由什么原因导致
            a.print打印内容后会自动换行
            b.line 17打后不想换行,与a冲突     ==> 通过在print最后添加逗号来不打印换行
            c.line 18只想换行                ==> \n是换行, print '\n'会先换行，再打印一个换行, 可以使用print ''或者b步骤得到的结论print '\n', 代替
'''

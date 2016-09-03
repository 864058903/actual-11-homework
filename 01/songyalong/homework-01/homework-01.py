#encoding:utf-8
#Time:2016-08-29
#Author:宋亚龙
#Name:homework01

'''作业
1. 整理课堂内容 FreeMind/xmind
2. github => 发给我
    https://github.com/51reboot/actual-11-homework

3. 计算[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45] 最大的两个数字(两个数字不能重复)

4. 打印乘法口诀

5. 猜数字游戏
    系统生成一个随机的数字
    import random
    random.randint(0, 100)
    '''
'''计算列表中最大的两个数字'''
# num01 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
# num02 = num01[:]
# for i in range(len(num01)-1,-1,-1):
#     for j in range(i):
#         if num01[j] > num01[j+1]:
#             num01[j],num01[j+1] = num01[j+1],num01[j]
# print '排序后的列表num01为：%s ' % num01
# max_num=num01.pop() #删除最后的一个大值并把返回值赋给变量
# while True:#如果列表里的最后一个最大值等于max_num的话则继续删除尾部元素，如果不等于的话，就把最后一个赋给secondMax_num
#     if num01[-1] == max_num:
#         num01.pop()
#     else:
#         secondMax_num = num01[-1]
#         break
# print '列表%s里\n最大数为：%s；第二大的数为：%s；' % (num02,max_num,secondMax_num)
'''第二种计算列表中最大的两个数字'''
num01 = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,65555,45,33,45]
print num01
max_num = 0
for i in num01:
    if i >max_num:
        max_num=i
second_num=0
for i in num01:
    if max_num>i>second_num:
        second_num=i
print '列表num01中\n最大值为：%s;\n第二大的值为：%s;' % (max_num,second_num)

'''乘法口诀'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         k = j * i
#         print '%s X %s = %s' %(j,i,k),
#     print '\n'


'''随机数'''
# import random
# while True:
#     randomNum=random.randint(1,100)
#     num03=int(raw_input('请输入0-100之间的数字：'))
#
#     if num03>100:
#         print '您输入的数字超过范围，请输入小于100的数字！'
#         continue
#     elif num03 < 0:
#         print '您输入的数字超过范围，请输入大于0的数字！'
#     elif num03==randomNum:
#         print '恭喜您，猜对了！\n猜中的数字是：%s' % randomNum
#         break
#     else:
#         print '很遗憾！您猜错了！\n您猜的数字是：%s\n答案是：%s' % (num03,randomNum)


'''练习'''
# nums=range(1,5)
# print nums
# b=0
# for i in nums:
#     b = b+i
# print b

'''
作业一ok
作业二ok，但乘法口诀，每一行多一个换行，可以使用print ''代替line54
作业三：考虑下如果是你，猜对的几率有多大吗？考虑将line 60 写到循环外，在输入后，提示用户应该往输入的值大了猜还是小了猜
'''

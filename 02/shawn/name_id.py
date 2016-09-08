#coding: utf-8

'''用户输入员工名字和id，名字和id之间用:分隔
多个用户 用逗号分隔
最终输入所有用户对应id的信息
比如用户输入user1:119,user2;112,user3:113
最终输出[('user2', '112'), ('user3', '113'), ('user1', '119')]
'''

user = []


while True:
    value = raw_input("Enter your info here: ")
    if value != 'end':
        value = value.split(",") 
        for i in value:
            i = i.strip().split(":")
            mytup = (i[0].strip(), i[1].strip())
            user.append(mytup)
    else:
        print user
        break

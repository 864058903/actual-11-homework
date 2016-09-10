#encoding:utf-8


userid='user1:119,user2:112,user3:113'

user=userid.split(",")
user1=[]
for i in  user:
    a=i.split(":")
    user1.append([a[0],a[1]])
print  tuple(user1)

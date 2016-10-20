#encoding:utf-8

import json
#读取用户文件
def getUser():

    file_user=open("users.txt",'r')
    user_list=json.loads(file_user.read())
    file_user.close()
    return user_list
#新用户注册写入文件
def writeUser(username,password):
    read_file=getUser()
    print read_file

    for i in read_file:
        ids = []
        print i.get('id')
        ids.append(i.get('id'))
    print int(max(ids))+1
    n1=int(max(ids))+1
    user={'id':n1,'username':username,'password':password}
    read_file.append(user)
    print read_file
    file_write=open('users.txt','w')
    file_write.write(json.dumps(read_file))
    file_write.close()


if __name__=='__main__':
    print getUser()


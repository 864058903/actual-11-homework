#encoding:utf-8

import userOperation
def getUsersList():
    list_users=userOperation.getUser()
    # list_users02=[]
    # for i in list_users:
    #     list_users02.append(i)
    return list_users #list_users02

if __name__=="__main__":
    for i in getUsersList():
       print i.get("username")

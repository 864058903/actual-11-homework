#coding=utf8
import json

def  readfile():
    with open('userpass','r') as  f:
        data=f.read()
        result=json.loads(data)
        return  result


def  writefile(data):
    with open('userpass','w+') as  f:
        result=json.dumps(data)
        f.write(result)


def onedata(data,id):
    for  i,k in enumerate(data):
        #print k
        if int(id)==k['id']:
            break
    return i


def checkuser(user):
    readresult=readfile()
    result= [ i.get('name') for  i in  readfile() ]
    if  user in  result:
        return 1
    else:
        return 0





if __name__ =="__main__":
    data=[{'id': 1, 'name': 'kk', 'password': '123456'},{'id': 2, 'name': 'woniu', 'password': '123456'},{'id': 3, 'name': '123', 'password': '123'}]
    writefile(data)
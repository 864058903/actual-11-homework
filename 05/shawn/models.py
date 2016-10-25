#!/usr/bin/env python
#encoding: utf-8

import json
import gconfig

def get_users():
    fh = open(gconfig.DB_PATH, 'r')
    users = json.loads(fh.read())
    fh.close()
    return users

def create_users(username,passwd):
    with open(gconfig.DB_PATH, 'r') as f1:
        users = json.loads(f1.read())
        result = [ i for i in users if i["name"] == username ]
        if len(result) == 0:
            new_id = max([ i['id'] for i in users ]) + 1
            users.append({'id':new_id,'name':username, 'password': passwd})
            with open(gconfig.DB_PATH, 'w') as f2:
                users_cnt = json.dumps(users)
                f2.write(users_cnt)
                f2.flush()
                info = "create success!"
        else:
            info = "username is already be used!"
    return info


def validate_login(username, passwd):
    users = get_users()
    for user in users:
        if user.get("name") == username and user.get("password") == passwd:
            return user
    return None

def log_dict(logpath, topn = 10):
    f1 = open(logpath, 'r')
    scnt = [ line.split() for line in f1.readlines()]
    all_dict = {}
    for line in scnt:
        ip,url,code = line[0],line[6],line[8]
        all_dict[(ip,url,code)] = all_dict.get((ip,url,code),0) + 1

    all_list = sorted(all_dict.items(), key=lambda x: x[1], reverse = True)
    return all_list[:topn]

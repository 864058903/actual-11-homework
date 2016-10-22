#coding:utf-8

import json
import gconf

def get_users():
    fh = open(gconf.USER_DB_PATH,'r')
    users = json.loads(fh.read())
    fh.close()
    return users

def validate_login(username,password):
    users = get_users()
    for user in users:
        if user.get('name') == username and user.get('password') == password:
            return user
    return None




def get_topn(src,  topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")

    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1

    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x:x[1],reverse=True)
    return result[:topn+1]

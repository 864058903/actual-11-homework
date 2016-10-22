#coding=utf-8

import gconf
import json
user_info_file_path =gconf.USER_DB_PATH

def get_user_info():
    f = open(user_info_file_path,'r')
    load_user_info = json.loads(f.read())
    f.close()
    temp = []
    for i in load_user_info:
        a = (i.get('id'),i.get('name'),i.get('password'))
        temp.append(a)

    return temp

################
# Debug

if __name__ == '__main__':
    a = get_user_info()
    print a
    # print temp[0][0],temp[0][1],temp[0][2]

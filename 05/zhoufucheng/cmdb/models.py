#encoding: utf-8

import json
import gconf

def get_user():
    fhandler = open(gconf.USER_DB_PATH,'r')
    user = json.loads(fhandler.read())
    fhandler.close()
    return user

def save_users(users):
    fhandler = open(gconf.USER_DB_PATH,'w')
    fhandler.write(json.dumps(users))
    fhandler.close()

def validate_login(username,password):
    users = get_user()
    for user in users:
        if user.get('name') == username and user.get('password') == password:
            return user
    return None

def validate_add_user(username,password):
    users = get_user()
    for user in users:
        if user.get('name') == username:
            return False, 'username is exists'
    if len(password) < 6:
        return False, 'password length of at least six'
    return True, ''

def add_users(username,password):
    _id = []
    users = get_user()
    for user in users:
        _id.append(user['id'])
    max_id = max(_id)
    max_id += 1
    users.append({'password':password, 'id':max_id, 'name':username})
    save_users(users)

def get_topn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")

    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1

    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x:x[1])

    return result[:-topn - 1:-1]
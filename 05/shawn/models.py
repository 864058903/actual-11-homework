#!/usr/bin/env python
#encoding: utf-8

import json
import gconfig

def get_users():
    fh = open(gconfig.DB_PATH, 'r')
    users = json.loads(fh.read())
    fh.close()
    return users
def get_user(user_id):
    users = get_users()
    for i in users:
        if i.get('id') == int(user_id):
            return i

def save_users(users):
    fh = open(gconfig.DB_PATH, 'w')
    fh.write(json.dumps(users))
    fh.close()
    return True


def validate_user_save(username, password):
    if username.strip() == '' or password.strip() == '':
        return False, "username/password is empty"
    elif len(username.strip()) <= 6:
        return False, 'username must dayu 6'
    elif len(username.strip()) >= 20:
        return False, 'username must xiaoyu 20'
    elif len([ i for i in get_users() if i['name'] == username ]) != 0:
        return False, 'username already be used'
    return True , ''

def user_save(username, password):
    users = get_users()
    user_id = int(max([ i['id'] for i in users ]))
    user = {'id' : user_id + 1, 'name' : str(username).strip(), 'password' : str(password).strip()}
    users.append(user)
    return save_users(users)

def user_update(user_id, username, password):
    users = get_users()
    for index, user in enumerate(users):
        if user.get('id') == int(user_id):
            users[index]['name'] = username
            users[index]['password'] = password
            print username,password,'hah'
    if save_users(users):
        return "edit done."
    else:
        return "something error."

def user_delete(user_id):
    user = get_user(user_id)
    users = get_users()
    users.remove(user)
    return save_users(users)


def create_users(username,passwd):
    users = get_users()
    max_id = max([ int(i['id']) for i in users ]) + 1
    if len([ i for i in users if i['name'] != username ]) == 0:
        users.append({'id':max_id,'name':username, 'password': passwd})
        f2 = open(gconfig.DB_PATH, 'w')
        users_cnt = json.dumps(users)
        f2.write(users_cnt)
        f2.flush()
        f2.close()
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

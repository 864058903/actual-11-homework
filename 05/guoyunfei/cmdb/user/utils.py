#coding: utf-8
#


import json
from uuid import uuid1
from config import *


def validate_login(username, password):
    message = get_read_users()
    username_list = [mess['username'] for mess in message]
    if username not in username_list:
        return (False, u'用户名不存在')
    else:
        for mess in message:
            if username == mess['username'] and password == mess['password']:
                return (True, '')
        else:
            return (False, u'密码错误')


def get_read_users():
    with open(USER_FILE) as f:
        content = f.read()
    return json.loads(content)


def get_write_users(content):
    with open(USER_FILE, 'wb') as f:
        f.write(json.dumps(content))


def validate_user(username, password):
    if not username:
        return False, u'用户名为空'
    if not username.isalnum():
        return False, u'用户名必须为字母或数字'
    message = get_read_users()
    for mess in message:
        if username == mess['username']:
            return False, u'用户名已存在'
    if len(password) < 6:
        return False, u'密码长度必须大于等于6'
    return True, ''


def validate_password(password):
    if len(password) < 6:
        return False, u'密码长度必须大于等于6'
    return True, ''


def add_users(username, password):
    id = uuid1().get_hex()
    message = get_read_users()
    message.append({'id':id, 'username':username, 'password':password})
    get_write_users(message)


def get_id_users(id):
    message = get_read_users()
    for mess in message:
        if id == mess['id']:
            return mess


def modify_password(id, password):
    new_user_list = []
    message = get_read_users()
    for mess in message:
        if id == mess['id']:
            mess['password'] = password
        new_user_list.append(mess)
    get_write_users(message)
    

def delete_users(id):
    message = get_read_users()
    new_user_list = []
    for mess in message:
        if id != mess['id']:
            new_user_list.append(mess)
    else:
        get_write_users(new_user_list)


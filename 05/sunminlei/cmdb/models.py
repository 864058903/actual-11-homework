#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import gconf

validate_none = lambda x, y: 'error: username/password is null' \
    if x == '' or y == '' else ''


def getusers():
    fh = open(gconf.USER_DB_PATH, 'rb')
    users = json.loads(fh.read())
    return users


def getuser(uid):
    users = getusers()
    for user in users:
        if user.get("id") == int(uid):
            return user


def getuserlist_notid(uid):
    users = getusers()
    user_list = []
    for user in users:
        if user.get("id") != int(uid):
            user_list.append(user.get('username'))
    return user_list


def write_users_json(users):
    fh = open(gconf.USER_DB_PATH, 'wb')
    fh.write(json.dumps(users))
    fh.close()


def validate_login(username, password):
    users = getusers()
    for user in users:
        if user.get("username") == username and user.get("password") == password:
            return user
    return None


def gettopn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, 'rb')


    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1
    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x: x[1])[:-topn - 1:-1]
    return result


def validate_create_user(username, password):
    users = getusers()
    error = ''
    id_list = []
    if username == '' or password == '':
        error = 'error: username/password is null'
        return error
    for user in users:
        if user.get("username") == username:
            error = 'error: username exist'
            return error
        else:
            id_list.append(user.get("id"))
    create_id = max(id_list) + 1
    users.append({"username": username, "password": password, "id": create_id})
    write_users_json(users)
    return error


def delete_user(uid):
    users = getusers()
    username = getuser(int(uid)).get('username')
    for index, user in enumerate(users):
        if user.get("id") == int(uid):
            del users[index]
    write_users_json(users)
    return username


def validate_update_user(username, password, uid):
    users = getusers()
    error = validate_none(username, password)
    print uid
    if error:
        return error
    for index, user in enumerate(users):
        if user.get("id") == int(uid):
            if username in getuserlist_notid(uid):
                error = 'error: username(%s) exist' % username
                return error
            else:
                users[index]["username"] = username
                users[index]["password"] = password
    write_users_json(users)


if __name__ == '__main__':
    pass

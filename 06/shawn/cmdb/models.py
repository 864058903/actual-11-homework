#!/usr/bin/env python
#encoding: utf-8

import json
import gconfig
import MySQLdb

SQL_LOGIN = 'select id, name from user where name=%s and password=md5(%s)'
SQL_USER_SAVE = 'insert into user(name,password) values(%s, md5(%s))'
SQL_USER_LIST = 'select id,name,password,age from user'
SQL_USER_GET = 'select id,name,age from user where id=%s'
SQL_USER_UPDATE = 'update user set name=%s, age=%s where id=%s'
SQL_USER_DEL = 'delete from user where id=%s'

def get_users():
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_LIST)
    rt_list = cursor.fetchall()
    cursor.close()
    conn.close()
    columns = ("id", "name", "password", "age")
    return [ dict(zip(columns, line)) for line in rt_list]

def get_user(user_id):
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_GET, (user_id,))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    columns = ("id", "name", "age")
    return {} if record is None else dict(zip(columns, record))


def validate_user_save(uid, username, password):
    # if username.strip() == '' or password.strip() == '':
    #     return False, "username/password is empty"
    # elif len(username.strip()) <= 6:
    #     return False, 'username must dayu 6'
    # elif len(username.strip()) >= 20:
    #     return False, 'username must xiaoyu 20'
    # elif len([ i for i in get_users() if i['name'] == username ]) != 0:
    #     return False, 'username already be used'
    return True , ''

def user_save(uid, username, age):
    
    return True

def user_update(user_id, username, age):
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cnt = cursor.execute(SQL_USER_UPDATE, (username, age, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def user_delete(user_id):
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cnt = cursor.execute(SQL_USER_DEL, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return True


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
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_LOGIN, (username, passwd))
    record = cursor.fetchone()
    columns = ('id', 'name')
    cursor.close()
    conn.close()
    return None if record is None else dict(zip(columns, record))



def log_dict(logpath, topn = 10):
    f1 = open(logpath, 'r')
    scnt = [ line.split() for line in f1.readlines()]
    all_dict = {}
    for line in scnt:
        ip,url,code = line[0],line[6],line[8]
        all_dict[(ip,url,code)] = all_dict.get((ip,url,code),0) + 1

    all_list = sorted(all_dict.items(), key=lambda x: x[1], reverse = True)
    return all_list[:topn]

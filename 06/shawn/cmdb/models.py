#!/usr/bin/env python
#encoding: utf-8

import json
import gconfig
import MySQLdb

SQL_LOGIN = 'select id, name from user where name=%s and password=md5(%s)'
SQL_USER_SAVE = 'insert into user(name,password,age) values(%s, md5(%s),%s)'
SQL_USER_LIST = 'select id,name,password,age from user'
SQL_USER_GET = 'select id,name,age from user where id=%s'
SQL_USER_UPDATE = 'update user set name=%s, age=%s where id=%s'
SQL_USER_DEL = 'delete from user where id=%s'
SQL_EDIT_CHECK = 'select id from user where id != %s and name = %s'

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


def validate_user_save(username, password, age):
    if username.strip() == '' or password.strip() == '':
        return False, "username/password is empty"
    if len(username.strip()) < 6 or len(username.strip()) > 20 :
        return False, 'username must between 6 and 20'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'
    if len([ line for line in get_users() if line['name'] == username ]) != 0:
        return False, 'username is already be used.'
    return True , ''

def validate_edit_save(user_id, username, age):
    if not get_user(user_id):
        return False, "user_id is error."
    if len(username.strip()) < 6 or len(username.strip()) > 20 :
        return False, 'username must between 6 and 20'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_EDIT_CHECK, (user_id,username.strip()))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    if record != None:
        return False, "username is already be used."
    else:
        return True , ''



def user_save(username, password, age):
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_SAVE, (username,password,age))
    conn.commit()
    cursor.close()
    conn.close()
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

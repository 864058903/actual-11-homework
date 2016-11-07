#!/usr/bin/env python
#encoding: utf-8

import json
import gconfig
import MySQLdb

SQL_LOGIN = 'select id, name from user where name=%s and password=md5(%s)'
SQL_USER_SAVE = 'insert into user(name,password,age,department,inro) values(%s, md5(%s),%s,%s,%s)'
SQL_USER_LIST = 'select id,name,password,age,department,inro from user'
SQL_USER_GET = 'select id,name,age,department,inro from user where id=%s'
SQL_USER_UPDATE = 'update user set name=%s, age=%s, department = %s, inro = %s where id=%s'
SQL_USER_DEL = 'delete from user where id=%s'
SQL_EDIT_CHECK = 'select id from user where id != %s and name = %s'
SQL_MACHINE_LIST = 'select id,name,addr,ip_ranges from machine_room'
SQL_MACHINE_SAVE = 'insert into machine_room(name, addr, ip_ranges) values(%s, %s, %s)'
SQL_GET_MACHINE = 'select name,addr,ip_ranges from machine_room where id =%s'
SQL_MACHINE_DEL = 'delete from machine_room where id=%s'
SQL_MACHINE_UPDATE = 'update machine_room set name=%s, addr=%s, ip_ranges=%s where id=%s'
SQL_MACHINE_EDIT_CHECK = 'select id from machine_room where id !=%s and (name=%s or ip_ranges=%s)'


def mysql_get_value(sql, args, is_fetch):
    rt_cnt, rt_list = "", []
    conn = MySQLdb.connect(host=gconfig.MYSQL_HOST, \
                           port=gconfig.MYSQL_PORT,\
                           user=gconfig.MYSQL_USER,\
                           passwd=gconfig.MYSQL_PASSWD,\
                           db=gconfig.MYSQL_DB,\
                           charset=gconfig.MYSQL_CHARSET)
    cursor = conn.cursor()
    rt_cnt = cursor.execute(sql, args)
    if is_fetch:
        rt_list = cursor.fetchall()
    else:
        conn.commit()
    cursor.close()
    conn.close()
    return rt_cnt, rt_list

def get_users():
    rt_list = mysql_get_value(SQL_USER_LIST,(),True)[1]
    columns = ("id", "name", "password", "age", "department", "inro")
    return [ dict(zip(columns, line)) for line in rt_list]

def get_user(user_id):
    record = mysql_get_value(SQL_USER_GET,(user_id,),True)[1][0]
    columns = ("id", "name", "age", "department", "inro")
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

def validate_machine(name, addr, ip_ranges):
    if name.strip() == "" or addr.strip() == "" or ip_ranges.strip() == "":
        return False,  "name/address/ip is empty."
    if len([ line for line in get_machine_list() if line.get("name") == name.strip()\
     or line.get("ip_ranges") == ip_ranges.strip() ]) != 0:
        return False, "name or ip is already be used."
    return True, ""

def validate_edit_save(user_id, username, age):
    if not get_user(user_id):
        return False, "user_id is error."
    if len(username.strip()) < 6 or len(username.strip()) > 20 :
        return False, 'username must between 6 and 20'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'
    record = mysql_get_value(SQL_EDIT_CHECK,(user_id,username.strip()),True)[1]
    if len(record) != 0:
        return False, "username is already be used."
    else:
        return True , ''


def validate_machine_edit(name, addr, ip_ranges, machine_id):
    if name.strip() == "" or addr.strip() == "" or ip_ranges.strip() == "":
        return False,  "name/address/ip is empty."
    rt_list = mysql_get_value(SQL_MACHINE_EDIT_CHECK,(machine_id,name.strip(),ip_ranges.strip()),True)[1]
    if len(rt_list) != 0:
        return False, "name/ip is already be used."
    else:
        return True, ""


def user_save(username, password, age, department, inro):
    rt_cnt = mysql_get_value(SQL_USER_SAVE,(username,password,age,department, inro),False)[0]
    return rt_cnt

def user_update(user_id, username, age, department, inro):
    rt_cnt = mysql_get_value(SQL_USER_UPDATE,(username, age, department, inro, user_id),False)[0]
    return rt_cnt

def user_delete(user_id):
    rt_cnt = mysql_get_value(SQL_USER_DEL,(user_id,),False)[0]
    return rt_cnt


def validate_login(username, passwd):
    rt_list = mysql_get_value(SQL_LOGIN,(username, passwd),True)[1]
    columns = ('id', 'name')
    return None if len(rt_list) == 0 else dict(zip(columns, rt_list[0]))


def get_machine_list():
    rt_list = mysql_get_value(SQL_MACHINE_LIST,(),True)[1]
    columns = ("id", "name", "addr", "ip_ranges")
    return [ dict(zip(columns, line)) for line in rt_list]


def save_machine(name, addr, ip_ranges):
    rt_cnt = mysql_get_value(SQL_MACHINE_SAVE,(name,addr,ip_ranges),False)[0]
    return rt_cnt


def get_machine_info(machine_id):
    rt_list = mysql_get_value(SQL_GET_MACHINE,(machine_id,),True)[1]
    columns = ("name", "addr", "ip_ranges")
    return None if len(rt_list) == 0 else dict(zip(columns, rt_list[0]))


def remove_machine(machine_id):
    rt_cnt = mysql_get_value(SQL_MACHINE_DEL,(machine_id,),False)[0]
    return rt_cnt


def update_machine(name, addr, ip_ranges, machine_id):
    rt_cnt = mysql_get_value(SQL_MACHINE_UPDATE,(name,addr,ip_ranges,machine_id),False)[0]
    return rt_cnt



def log_dict(logpath, topn = 10):
    f1 = open(logpath, 'r')
    scnt = [ line.split() for line in f1.readlines()]
    all_dict = {}
    for line in scnt:
        ip,url,code = line[0],line[6],line[8]
        all_dict[(ip,url,code)] = all_dict.get((ip,url,code),0) + 1

    all_list = sorted(all_dict.items(), key=lambda x: x[1], reverse = True)
    return all_list[:topn]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dbutils
SQL_USER_LIST = 'select id, name, age from user'
SQL_USER_LIST_COLUMNS = ('id', 'username', 'age')

SQL_USER_BY_ID = 'select id, name, age from user where id=%s'
SQL_USER_BY_ID_COLUMNS = ('id', 'name', 'age')

SQL_VALIDATE_LOGIN = 'select id, name from user where name=%s\
                     and password=md5(%s)'
SQL_VALIDATE_LOGIN_COLUMNS = ('id', 'name')

SQL_VALIDATE_USER_SAVE = 'select id, name, age from user where name=%s'
SQL_USER_SAVE = 'insert into user(name,password,age) values(%s, md5(%s), %s)'

SQL_USER_DELETE_BY_ID = 'delete from user where id=%s'

SQL_VALIDATE_USER_MODIFY = 'select id, name, age from user where id!=%s and name=%s'

SQL_USER_MODIFY = 'update user set name=%s, age=%s where id=%s'

SQL_ROOM_LIST_COLUMNS = ('rid', 'roomname', 'addr', 'ip_ranges')
SQL_ROOM_LIST = 'select * from machine_room'

SQL_VALIDATE_ROOM_SAVE = 'select name, addr, ip_ranges from machine_room where name=%s'
SQL_ROOM_SAVE = 'insert into machine_room(name, addr, ip_ranges) values(%s, %s, %s)'

SQL_ROOM_BY_ID_COLUMNS = ('rid', 'roomname', 'addr', 'ip_ranges')
SQL_ROOM_BY_ID = 'select id, name, addr, ip_ranges from machine_room where id=%s'

SQL_ROOM_DELETE_BY_ID = 'delete from machine_room where id=%s'

SQL_VALIDATE_ROOM_MODIFY = 'select id, name, addr, ip_ranges from machine_room where id!=%s and name=%s'
SQL_ROOM_MODIFY = 'update machine_room set name=%s, addr=%s, ip_ranges=%s where id=%s'


def IPChecker_re(isip):
    import re
    pattern = re.compile("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    if pattern.match(isip) is not None:
        return True
    return False


def get_users():
    _count, _rt_list = dbutils.execute_fetch_sql(SQL_USER_LIST)
    return [dict(zip(SQL_USER_LIST_COLUMNS, x)) for x in _rt_list]


def get_user_by_id(uid):
    _count, _rt = dbutils.execute_fetch_sql(SQL_USER_BY_ID, (uid,))
    print _rt
    return {} if _rt is None else dict(zip(SQL_USER_BY_ID_COLUMNS, _rt[0]))
    # 当mysql中id不存在时，返回空字典，存在则返回一个指定的字典


def validate_login(username, password):
    _count, _rt = dbutils.execute_fetch_sql(SQL_VALIDATE_LOGIN, (username, password))
    # rt = None
    # if record is not None:
    #     rt = {'id': record[0], 'name': record[1]}
    return None if _rt is None else dict(zip(SQL_VALIDATE_LOGIN_COLUMNS, _rt))
    # 当mysql中用户名和密码不匹配时，返回空，存在则返回一个指定的字典


def validate_user_save(username, password, age):
    username = username.strip()
    password = password.strip()
    if username == '':
        return False, 'username is empty'
    if len(username) > 25:
        return False, 'username is lt 25'
    if password == '':
        return False, 'password is empty'
    if len(password) > 25 or len(password) < 6:
        return False, 'password is between 6 and 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 120:
        return False, 'age is 1 and 120 integer'
    _count, _rt = dbutils.execute_fetch_sql(SQL_VALIDATE_ROOM_SAVE, (name,))
    if _rt:
        return False, 'username is used by others'
    return True, ''


def user_save(username, password, age):
    _count, _rt = dbutils.execute_commit_sql(SQL_USER_SAVE, (username, password, age))
    return _count != 0  # 当插入成功时_count不等于０，返回_count；插入失败返回的则是默认值None


def user_delete(uid):
    _count, _rt = dbutils.execute_commit_sql(SQL_USER_DELETE_BY_ID, (uid,))
    return _count != 0  # 当删除成功时_count不等于０，返回_count；插入失败返回的则是默认值None


def validate_user_modify(username, age, uid):
    username = username.strip()
    if not get_user_by_id(uid):
        return False, 'user is not found'
    if username == '':
        return False, 'username is empty'
    if len(username) > 25:
        return False, 'username is lt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 120:
        return False, 'age is 1 and 120 integer'
    _count, _rt = dbutils.execute_fetch_sql(SQL_VALIDATE_USER_MODIFY, (uid, username))
    if _rt:
        return False, 'username is used by others'
    return True, ''


def user_modify(username, age, uid):
    _count, _rt = dbutils.execute_commit_sql(SQL_USER_MODIFY, (username, age, uid))
    print _count, _rt
    return _count  # update 可能没修改的话返回０，修改的是１所以都要返回一个值　不能用!=0


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


def get_rooms():
    _count, _rt_list = dbutils.execute_fetch_sql(SQL_ROOM_LIST)
    return [dict(zip(SQL_ROOM_LIST_COLUMNS, li)) for li in _rt_list]


def validate_room_save(roomname, addr, ip_ranges):
    roomname = roomname.strip()
    addr = addr.strip()
    ip_ranges = ip_ranges.strip()
    print ip_ranges
    if roomname == '':
        return False, 'roomname is empty'
    if len(roomname) > 64:
        return False, 'roomname is gt 64'
    if addr == '':
        return False, 'addr is empty'
    if len(addr) > 128:
        return False, 'addr is gt 128'
    if not IPChecker_re(ip_ranges):
        return False, 'ip_ranges is not ip_address type'
    _count, _rt = dbutils.execute_fetch_sql(SQL_VALIDATE_ROOM_SAVE, (roomname,))
    if _rt:
        return False, 'roomname is used by others'
    return True, ''


def room_save(roomname, addr, ip_ranges):
    _count, _rt = dbutils.execute_commit_sql(SQL_ROOM_SAVE, (roomname, addr, ip_ranges))
    return _count != 0


def get_room_by_id(rid):
    _count, _rt = dbutils.execute_fetch_sql(SQL_ROOM_BY_ID, (rid,))
    print _rt
    return {} if _rt is None else dict(zip(SQL_ROOM_BY_ID_COLUMNS, _rt[0]))


def room_delete(rid):
    _count, _rt = dbutils.execute_commit_sql(SQL_ROOM_DELETE_BY_ID, (rid,))
    return _count != 0


def validate_room_modify(rid, roomname, addr, ip_ranges):
    roomname = roomname.strip()
    addr = addr.strip()
    ip_ranges = ip_ranges.strip()
    if not get_room_by_id(rid):
        return False, 'room is not found'
    if roomname == '':
        return False, 'roomname is empty'
    if len(roomname) > 64:
        return False, 'roomname is gt 64'
    if addr == '':
        return False, 'addr is empty'
    if len(addr) > 128:
        return False, 'addr is gt 128'
    if not IPChecker_re(ip_ranges):
        return False, 'ip_ranges is not ip_address type'
    _count, _rt = dbutils.execute_fetch_sql(SQL_VALIDATE_ROOM_MODIFY, (rid, roomname))
    if _rt:
        return False, 'roomname is used by others'
    return True, ''


def room_modify(rid, roomname, addr, ip_ranges):
    _count, _rt = dbutils.execute_commit_sql(SQL_ROOM_MODIFY, (roomname, addr, ip_ranges, rid))
    print _count, _rt
    return _count  # update 可能没修改的话返回０，修改成功返回的是１所以都要返回一个值　不能用!=0


if __name__ == '__main__':
    pass

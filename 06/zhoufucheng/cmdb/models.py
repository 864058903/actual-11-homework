#encoding: utf-8

import json

import gconf

import MySQLdb

SQL_VALIDATE_LOGIN = 'select id, name from user where name = %s and password = md5(%s)'
SQL_USER_SAVE = 'insert into user(name, password, age) values(%s,md5(%s),%s)'

SQL_GET_USERS_COLUMNS = ('id','name','age')
SQL_GET_USERS = 'select id, name, age from user'

SQL_USER_BY_ID_COLUMNS = ('id','name','age')
SQL_USER_BY_ID = 'select id, name, age from user where id = %s'

SQL_VALIDATE_USER_MODIFY = 'select id from user where id != %s and name = %s'

SQL_USER_MODIFY_COLUMNS = ('id','name','age')
SQL_USER_MODIFY = 'update user set name = %s, age = %s where id = %s'

SQL_USER_DELETE = 'delete from user where id = %s'

SQL_GET_IDCS_COLUMNS = ('id','name','addr','ip_ranges')
SQL_GET_IDCS = 'select id,name,addr,ip_ranges from machine_room'

SQL_IDC_SAVE = 'insert into machine_room(name,addr,ip_ranges) values(%s,%s,%s)'

SQL_GET_IDC_ID_COLUMNS = ('id','name','addr','ip_ranges')
SQL_GET_IDC_ID = 'select id,name,addr,ip_ranges from machine_room where id = %s'

SQL_IDC_MODIFY = 'update machine_room set name = %s,addr = %s,ip_ranges = %s where id = %s'

SQL_IDC_DELETE = 'delete from machine_room where id = %s'

def get_users():
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_GET_USERS)
    rt = cursor.fetchall()
    return [dict(zip(SQL_GET_USERS_COLUMNS,line)) for line in rt]
    '''
    fh = open(gconf.USER_DB_PATH, "rb")
    users = json.loads(fh.read())
    fh.close()
    return users
    '''

def save_user(users):
    fh = open(gconf.USER_DB_PATH, "wb")
    fh.write(json.dumps(users))
    fh.close()

def validate_login(username, password):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_VALIDATE_LOGIN,(username,password))
    record = cursor.fetchone()
    cursor.close()
    conn.close()
    rt = None
    if record is not None:
        rt = {'id':record[0], 'name':record[1]}
    return rt    

    '''
    users = get_users()
    for user in users:
        if user.get('name') == username and user.get('password') == password:
            return user
    return None
    '''

def validate_user_save(username,password,age):
    if username.strip() == '':
        return False, 'username is not empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if password.strip() == '':
        return False, 'password is not empty'
    if len(password.strip()) < 6 or len(password.strip()) > 25:
        return False, 'password len is between 6 and 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'
    return True, ''

def user_save(username,password,age):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_SAVE,(username,password,age))
    conn.commit()
    cursor.close()
    conn.close()
    '''
    users = get_users()
    user_id = 0
    for user in users:
        if user_id < user['id']:
            user_id = user['id']
    user = {'id':user_id + 1, 'name':str(username).strip(), 'age':int(age), 'password':str(password).strip()}
    users.append(user)
    return save_user(users)
    '''

def get_user_by_id(uid):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_BY_ID,(uid,))
    rt = cursor.fetchone()
    cursor.close()
    conn.close()
    return {} if rt is None else dict(zip(SQL_USER_BY_ID_COLUMNS,rt))

def validate_user_modify(uid,username,age):
    if not get_user_by_id(uid):
        return False, 'user is not found'
    if username.strip() == '':
        return False, 'username is not empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cnt = cursor.execute(SQL_VALIDATE_USER_MODIFY,(uid,username.strip()))
    cursor.close()
    conn.close()
    if cnt != 0:
        return False, 'username cannot be repeated'

    return True, ''

def user_modify(uid,username,age):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()    
    cnt = cursor.execute(SQL_USER_MODIFY,(username,age,uid))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def user_delete(uid):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_USER_DELETE,(uid,))
    conn.commit()
    cursor.close
    conn.close()
    return True

def get_idcs():
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_GET_IDCS)
    rt = cursor.fetchall()
    return [dict(zip(SQL_GET_IDCS_COLUMNS,line)) for line in rt]

def validate_idc_save(name,addr,ip_ranges):
    return True, ''


def idc_save(name,addr,ip_ranges):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_IDC_SAVE,(name,addr,ip_ranges))
    conn.commit()
    cursor.close()
    conn.close()

def get_idc_id(id):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_GET_IDC_ID,(id,))
    rt = cursor.fetchone()
    cursor.close()
    conn.close()
    return None if rt is None else dict(zip(SQL_GET_IDC_ID_COLUMNS,rt))

def validate_idc_modify(id,name,addr,ip_ranges):
    return True, ''

def idc_modify(id,name,addr,ip_ranges):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_IDC_MODIFY,(name,addr,ip_ranges,id))
    conn.commit()
    cursor.close()
    conn.close()

def idc_delete(id):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(SQL_IDC_DELETE,(id,))
    conn.commit()
    cursor.close()
    conn.close()


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

#encoding: utf-8

import MySQLdb

import gconf

SQL_VALIDATE_LOGIN_COLUMNS = ('id', 'name')

SQL_VALIDATE_LOGIN = 'select id, name from user where name = %s and password = md5(%s)'
SQL_USER_SAVE = 'insert into user(name, age, password) values(%s, %s, md5(%s))'

SQL_USER_LIST_COLUMNS = ('id', 'name', 'age')
SQL_USER_LIST = 'select id, name, age from user'

SQL_USER_BY_ID_COLUMNS = ('id', 'name', 'age')
SQL_USER_BY_ID = 'select id, name, age from user where id=%s'

SQL_USER_MODIFY = 'update user set name=%s, age=%s where id=%s'

SQL_VALIDATE_USER_MODIFY = 'select id from user where id != %s and name = %s'

SQL_USER_DELETE = 'DELETE FROM `zrd`.`user` WHERE  `id`=%s'

# 数据库连接

def execu_sql(sql, args, is_fetch):
    rt_cnt = 0
    rt_list = []
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                        port=gconf.MYSQL_PORT, \
                        user=gconf.MYSQL_USER, \
                        passwd=gconf.MYSQL_PASSWD, \
                        db=gconf.MYSQL_DB, \
                        charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    rt_cnt = cursor.execute(sql, args)
    if is_fetch:
        rt_list = cursor.fetchall()
    else:
        conn.commit()
    cursor.close()
    conn.close()
    return rt_cnt, rt_list

'''
获取用户信息列表
'''
def get_users():
    sql = SQL_USER_LIST
    args = ()

    rt_cnt, rt_list = execu_sql(sql,args,True)

    return [dict(zip(SQL_USER_LIST_COLUMNS, line)) for line in rt_list]

'''
用户登录检查
'''
def validate_login(username, password):
    sql = SQL_VALIDATE_LOGIN
    args = (username, password)
    rt_cnt,rt_list = execu_sql(sql,args,True)

    return None if rt_list is None else dict(zip(SQL_VALIDATE_LOGIN_COLUMNS, rt_list))

'''
新增用户前 检查
'''
def validate_user_save(username, password, age):
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if password.strip() == '':
        return False, 'password is empty'
    if len(password.strip()) < 6 or len(password.strip()) > 25:
        return False, 'password len is between 6 and 25'

    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    return True, ''

'''
保存新增用户信息
返回 True/False
'''
def user_save(username, password, age):
    sql = SQL_USER_SAVE
    args = (username, age, password)
    rt_cnt ,rt_list = execu_sql(sql,args,False)

    return rt_cnt != 0

'''
以ID获取用户信息
返回 : {'age': xx, 'id': xx, 'name': xx}
'''
def get_user_by_id(uid):
    sql = SQL_USER_BY_ID
    args = (uid,)
    rt_cnt, rt_list = execu_sql(sql,args,True)
    return {} if rt_list is None else dict(zip(SQL_USER_BY_ID_COLUMNS, (rt_list[0][0],rt_list[0][1],rt_list[0][2])))

'''
用户修改信息，合法性检查
返回值 True/False
'''
def validate_user_modify(uid, username, age):
    if not get_user_by_id(uid):
        return False, 'user is not found'
    if username.strip() == '':
        return False, 'username is empty'
    if len(username.strip()) > 25:
        return False, 'username len is not gt 25'
    if not str(age).isdigit() or int(age) < 1 or int(age) > 100:
        return False, 'age is not a between 1 and 100 integer'

    sql = SQL_VALIDATE_USER_MODIFY
    args = (uid, username.strip())
    rt_cnt , rt_list = execu_sql(sql,args,False)
    # 已用用户存在返回的值 必然不是0
    if rt_cnt != 0:
        return False, 'username is same to other'
    return True, ''

'''
保存用户修改信息
'''
def user_modify(uid, username, age):
    sql = SQL_USER_MODIFY
    args = (username, age, uid)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True

"""
删除用户信息
"""
def delete_user(uid):
    sql = SQL_USER_DELETE
    args = (uid,)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True


# -----------------------------------------------------------------------
'''
获取机房列表
'''
def get_machines():
    SQL_MACHINES_LIST = 'SELECT  `id`,  `room_name`,  `addr`,  LEFT(`ip_ranges`, 256) FROM `zrd`.`machine_room` LIMIT 1000'
    SQL_MACHINES_LIST_COLUMS = ('id', 'room_name', 'addr','ip_ranges')
    sql = SQL_MACHINES_LIST
    args = ()

    rt_cnt, rt_list=execu_sql(sql,args,True)
    a = [dict(zip(SQL_MACHINES_LIST_COLUMS,line)) for line in rt_list]
    # print a
    return a

'''
机房保存前检查
'''
def validate_machine_save(room_name,addr,ip_ranges):
    if room_name.strip() == '':
        return False, 'room_name is empty'
    if len(room_name.strip()) > 64:
        return False, 'room_name len is not gt 64'

    if addr.strip() == '':
        return False, 'addr is empty'
    if len(addr.strip()) > 128:
        return False, 'addr len is not gt 128'

    if ip_ranges.strip() == '':
        return False, 'ip_ranges is empty'

    SQL_VALIDATE_MACHINE_SAVE = 'SELECT  `room_name` FROM `zrd`.`machine_room` WHERE room_name=%s'
    sql = SQL_VALIDATE_MACHINE_SAVE
    args = (room_name,)
    rt_cnt,rt_list = execu_sql(sql,args,True)
    if rt_cnt:
        return False,'room_name is same'

    return True, ''

'''
保存机房信息
'''
def machine_save(room_name,addr,ip_ranges):
    SQL_USER_SAVE = 'INSERT INTO `zrd`.`machine_room` (`room_name`, `addr`, `ip_ranges`) VALUES (%s, %s, %s)'
    sql = SQL_USER_SAVE
    args = (room_name,addr,ip_ranges)
    rt_cnt,rt_list = execu_sql(sql,args,False)

    # 保存信息影响一行，否则都是不通过
    if rt_cnt == 1:
        return True,''
    return False,'保存信息失败'

'''
以ID获取机房信息
返回 : {'age': xx, 'id': xx, 'name': xx}
'''
def get_machine_by_id(id):
    SQL_MACHINE_BY_ID = 'SELECT `id`, `room_name`, `addr`, `ip_ranges` FROM `zrd`.`machine_room` WHERE  `id`=%s'
    SQL_MACHINE_BY_ID_COLUMS = ('id','room_name','addr','ip_ranges')
    sql = SQL_MACHINE_BY_ID
    args = (id,)
    rt_cnt, rt_list = execu_sql(sql,args,True)
    return {} if rt_list is None else dict(zip(SQL_MACHINE_BY_ID_COLUMS, (rt_list[0][0],rt_list[0][1],rt_list[0][2],rt_list[0][3])))



'''
机房修改信息，合法性检查
返回值 True/False
'''
def validate_machine_modify(id,room_name,addr,ip_ranges):
    if not get_machine_by_id(id):
        return False, 'machine is not found'
    if room_name.strip() == '':
        return False, 'username is empty'
    if addr.strip() == '':
        return False, 'addr  is empty'
    if ip_ranges.strip() == '':
        return False, 'ip_ranges is empty'
    print id
    SQL_VALIDATE_MACHINE_MODIFY ='SELECT  `room_name` FROM `zrd`.`machine_room` WHERE  `id`!=%s AND room_name=%s'
    sql = SQL_VALIDATE_MACHINE_MODIFY
    args = (id,room_name)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    print rt_cnt
    # 已用机房存在返回的值 必然不是0
    if rt_cnt != 0:
        return False, 'room_name is same to other'
    return True, ''



'''
保存机房修改信息
'''
def machine_modify(id,room_name,addr,ip_ranges):
    SQL_MACHINE_MODIFY = 'UPDATE `zrd`.`machine_room` SET `room_name`=%s, `addr`=%s, `ip_ranges`=%s WHERE  `id`=%s'
    sql = SQL_MACHINE_MODIFY
    args = (room_name,addr,ip_ranges,id)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True


"""
删除机房信息
"""
def delete_machine(id):
    SQL_MACHINE_DELETE = 'DELETE FROM `zrd`.`machine_room` WHERE  `id`=%s'
    sql = SQL_MACHINE_DELETE
    args = (id,)
    rt_cnt , rt_list = execu_sql(sql,args,False)
    return True

# ---------------------------------------------
'''
日志信息
'''
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

if __name__ == "__main__":
    pass
    # 批量插入数据
    for i in range(101):
        sql = "INSERT INTO `zrd`.`user`(`name`, `age`, `password`)  VALUES ('zhou%s',%s, md5('%s'))"

        args = (i,i,i)
        execu_sql(sql,args,False)
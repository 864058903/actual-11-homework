#coding:utf8
import gconf
import MySQLdb

# 用户登录检查语句
VALIDATE_LOGIN_SQL_COLUMNS=('username','password')
VALIDATE_LOGIN_SQL='SELECT `username`,`password` FROM `user` WHERE username=%s AND password=md5(%s)'



# 机房所有信息列表获取
VALIDATE_GET_ROOMS_SQL_COLUMS=('id','name','addr','ip_ranges')
VALIDATE_GET_ROOMS_SQL='SELECT `id`,`name`,`addr`,`ip_ranges` FROM machine_room'

# 保存新建机房信息

ROOM_SAVE_SQL='INSERT INTO `zrd`.`machine_room` (`name`, `addr`, `ip_ranges`) VALUES (%s, %s, %s)'

'''
登入用户检查
'''
def validate_login(username, password):
     conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
     cursor = conn.cursor()
     cursor.execute(VALIDATE_LOGIN_SQL, (username,password))
     rt = cursor.fetchone()
     cursor.close()
     conn.close()
     return None if rt is None else dict(zip(VALIDATE_LOGIN_SQL_COLUMNS,rt))



'''
获取机房所用信息
'''
def get_rooms():
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)
    cursor = conn.cursor()
    cursor.execute(VALIDATE_GET_ROOMS_SQL)
    # 返回所有机房列表
    rt_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return [dict(zip(VALIDATE_GET_ROOMS_SQL_COLUMS,room)) for room in rt_list]

'''
保存新建机房前检查输入合法性
返回值 True/False , 提示信息
'''
def validate_room_save(name, addr, ip_ranges):
    if name.strip() == '':
        return False, 'name is empty'
    if addr.strip() == '':
        return False, 'addr is empty'
    if ip_ranges.strip() == '':
        return False,'ip_ranges is empty'

    return True, ''

'''
保存新建机房信息
'''
def room_save(name, addr, ip_ranges):
    ROOM_SAVE_SQL_COLUMS=(name,addr,ip_ranges)
    try:
        conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                                port=gconf.MYSQL_PORT, \
                                user=gconf.MYSQL_USER, \
                                passwd=gconf.MYSQL_PASSWD, \
                                db=gconf.MYSQL_DB, \
                                charset=gconf.MYSQL_CHARSET)
        cursor = conn.cursor()
        r_row = cursor.execute(ROOM_SAVE_SQL,(ROOM_SAVE_SQL_COLUMS))
        conn.commit()
    except BaseException as error:
        return False,u'error'
    finally:
        cursor.close()
        conn.close()
    return True,''

'''
获取一个机房信息 使用 name 字段作为条件
返回 {k:v}
'''
GET_ROOM_SQL_BY_NAME_COLUMNS = ('id','name','addr','ip_ranges')
GET_ROOM_SQL_BY_NAME = 'SELECT  `id`,  `name`,  `addr`,`ip_ranges` FROM `zrd`.`machine_room` WHERE name=%s'
def get_room_by_name(name):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()
    cursor.execute(GET_ROOM_SQL_BY_NAME, (name,))
    rt = cursor.fetchone()
    cursor.close()
    conn.close()

    return {} if rt is None else dict(zip(GET_ROOM_SQL_BY_NAME_COLUMNS, rt))

'''
机房修改合法性检查
'''
def validate_room_modify(name, addr, ip_ranges):
    if not get_room_by_name(name):
        return False, 'user is empty'
    if addr.strip() == '':
        return False, 'addr is empty'
    if ip_ranges == '':
        return False,'ip_ranges is empty'
    return True,''
'''
机房信息修改
'''
SQL_ROOM_MODIFY='UPDATE machine_room SET `addr`=%s, `ip_ranges`=%s WHERE  `name`=%s'
def room_modify(name, addr, ip_ranges):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cnt = cursor.execute(SQL_ROOM_MODIFY, (addr, ip_ranges, name))
    conn.commit()
    cursor.close()
    conn.close()
    return True

'''
删除机房
'''
SQL_ROOM_DELETE='DELETE FROM machine_room WHERE  `name`=%s'

def delete_room(name):
    conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                            port=gconf.MYSQL_PORT, \
                            user=gconf.MYSQL_USER, \
                            passwd=gconf.MYSQL_PASSWD, \
                            db=gconf.MYSQL_DB, \
                            charset=gconf.MYSQL_CHARSET)

    cursor = conn.cursor()

    cnt = cursor.execute(SQL_ROOM_DELETE, (name,))
    conn.commit()
    cursor.close()
    conn.close()
    return True

if __name__ == "__main__":
    print validate_login('zrd','123456')
    print get_rooms()

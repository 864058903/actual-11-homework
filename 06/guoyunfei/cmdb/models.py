# coding=utf-8

from dbutils import MysqlConnect


def get_users():
    columns = 'id,username,password,age'
    sql = 'select {} from user'.format(columns)
    cnt, rt_list = MysqlConnect.execute_sql(sql)
    return [dict(zip(columns.split(','), rt)) for rt in rt_list]


def validate_login(username, password):
    sql = 'select * from user where username=%s and password=md5(%s)'
    cnt, rt_list = MysqlConnect.execute_sql(sql, (username, password))
    return cnt == 1


def get_topn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, "rb")
    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1
    fhandler.close()
    result = sorted(stat_dict.items(), key=lambda x: x[1])
    return result[:-topn - 1:-1]


def validate_user(username=None, password=None, age=None):
    if username is not None:
        if username.strip() == '':
            return False, u'用户名为空'
        users = get_users()
        for user in users:
            if username == user['username']:
                return False, u'用户名已存在'
        if not username.strip().isalnum():
            return False, u'用户名必须为数字或字母'
        if len(username.strip()) >= 26:
            return False, u'用户名长度必须为1-25位'
    if password is not None:
        if password.strip() == '':
            return False, u'密码为空'
        if len(password.strip()) <= 5 or len(password.strip()) >= 26:
            return False, u'密码长度必须为6-25位'
    if age is not None:
        if age.strip() == '':
            return False, u'年龄为空'
        if not age.isdigit():
            return False, u'年龄必须为整数'
        if int(age) <= 0 or int(age) >= 101:
            return False, u'年龄为1-100数字'
    return True, ''


def user_add(username, password, age):
    sql = 'insert into user(username,password,age) values(%s,md5(%s),%s)'
    MysqlConnect.execute_sql(sql, (username, password, age))


def get_by_id(uid):
    columns = 'id,username,password,age'
    sql = 'select * from user where id=%s'
    cnt, rt_list = MysqlConnect.execute_sql(sql, (uid, ))
    return dict(zip(columns.split(','), rt_list[0]))


def user_update(uid, age):
    sql = 'update user set age=%s where id=%s'
    MysqlConnect.execute_sql(sql, (age, uid))


def validate_password(uid, old_password, new1_password, new2_password):
    sql = 'select * from user where id=%s and password=md5(%s)'
    cnt, rt_list = MysqlConnect.execute_sql(sql, (uid, old_password))
    if cnt != 1:
        return False, u'原密码错误'
    status1, message1 = validate_user(password=new1_password)
    if not status1:
        return False, message1
    status2, message2 = validate_user(password=new2_password)
    if not status2:
        return False, message2
    if new1_password != new2_password:
        return False, u'密码前后不匹配'
    return True, ''


def change_passwd(uid, password):
    sql = 'update user set password=md5(%s) where id=%s'
    MysqlConnect.execute_sql(sql, (password, uid))


def user_delete(uid):
    sql = 'delete from user where id=%s'
    MysqlConnect.execute_sql(sql, (uid, ))


'''机房管理
'''


def get_machines():
    columns = 'id,name,addr,ips'
    sql = 'select {} from machine'.format(columns)
    cnt, rt_list = MysqlConnect.execute_sql(sql)
    return [dict(zip(columns.split(','), rt)) for rt in rt_list]


def validate_machine(name=None, addr=None, ips=None):
    if name is not None:
        if name.strip() == '':
            return False, u'机房名称为空'
        machines = get_machines()
        for machine in machines:
            if name == machine['name']:
                return False, u'机房名称已存在'
        if not name.strip().isalnum():
            return False, u'机房名称必须为数字或字母'
        if len(name.strip()) >= 65:
            return False, u'机房名称长度必须为1-64位'
    if addr is not None:
        if addr.strip() == '':
            return False, u'机房地址为空'
        if len(addr.strip()) >= 129:
            return False, u'机房地址长度必须为1-128位'
    if ips is not None:
        if ips.strip() == '':
            return False, u'机房IP为空'
    return True, ''


def machine_add(name, addr, ips):
    sql = 'insert into machine(name, addr, ips) values(%s, %s, %s)'
    args = (name, addr, ips)
    MysqlConnect.execute_sql(sql, args)


def get_machine_id(uid):
    columns = 'id,name,addr,ips'
    sql = 'select * from machine where id=%s'
    cnt, rt_list = MysqlConnect.execute_sql(sql, (uid, ))
    return dict(zip(columns.split(','), rt_list[0]))


def machine_update(uid, name, addr, ips):
    sql = 'update machine set name=%s, addr=%s, ips=%s where id=%s'
    MysqlConnect.execute_sql(sql, (name, addr, ips, uid))


def machine_delete(uid):
    sql = 'delete from machine where id=%s'
    MysqlConnect.execute_sql(sql, (uid,))

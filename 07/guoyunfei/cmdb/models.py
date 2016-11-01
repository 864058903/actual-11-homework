# coding=utf-8

from dbutils import MysqlConnection


def validate_login(username, password):
    sql = 'select * from user where username=%s and password=md5(%s)'
    args = (username, password)
    cnt, rt_list = MysqlConnection.execute_sql(sql, args)
    if cnt == 1:
        return True, ''
    else:
        return False, u'用户名或密码错误'


def validate_password(username, password_old, password_new, password_repeat_new):
    if password_old.strip() == '':
        return False, u'原密码不能为空'
    ret, error = validate_login(username, password_old)
    if not ret:
        return False, u'原密码错误'
    if password_new.strip() == '':
        return False, u'新密码不能为空'
    if password_old == password_new:
        return False, u'新密码不能与原密码相同'
    if password_repeat_new.strip() == '':
        return False, u'确认新密码不能为空'
    if password_new != password_repeat_new:
        return False, u'新密码前后输入不匹配'
    return True, ''


def change_password(username, password):
    sql = 'update user set password=md5(%s) where username=%s'
    args = (password, username)
    MysqlConnection.execute_sql(sql, args)


def get_user_list():
    columns = ("id", "username", "password", "email", "telephone")
    sql = "select * from user"
    cnt, rt_list = MysqlConnection.execute_sql(sql)
    rt = []
    for line in rt_list:
        rt.append(dict(zip(columns, line)))
    return rt


def get_user_id(uid):
    rt = get_user_list()
    for user in rt:
        if user['id'] == int(uid):
            return user


def validate_add(username, password, email, telephone):
    if username.strip() == '':
        return False, u'用户名不能为空'
    if not username.isalnum():
        return False, u'用户名由数字或字母组成'
    if len(username) < 5 or len(username) > 32:
        return False, u'用户名长度5-32位'
    user_list = get_user_list()
    for user in user_list:
        if user['username'] == username:
            return False, u'用户名存在'
    if password.strip() == '':
        return False, u'密码不能为空'
    if len(password) < 6: 
        return False, u'密码长度大于6位'
    if len(email) > 32:
        return False, u'邮箱长度不能大于32位'
    if len(telephone) > 11:
        return False, u'电话长度不能大于11位'
    return True, ''


def user_add(username, password, email, telephone):
    columns = ("username", "password", "email", "telephone")
    sql = 'insert into user({}) values(%s, md5(%s), %s, %s)'.format(','.join(columns))
    args = (username, password, email, telephone)
    MysqlConnection.execute_sql(sql, args)


def validate_change(email, telephone):
    if len(email) > 32:
        return False, u'邮箱长度不能大于32位'
    if len(telephone) > 11:
        return False, u'电话长度不能大于11位'
    return True, ''


def user_change(uid, email, telephone):
    sql = 'update user set email=%s,telephone=%s where id=%s'
    args = (email, telephone, uid)
    MysqlConnection.execute_sql(sql, args)


def user_delete(uid):
    sql = 'delete from user where id=%s'
    MysqlConnection.execute_sql(sql, (uid, ))


def get_idcs_list():
    columns = ("id", "name", "address", "ips", "status")
    sql = "select * from idcs where status=0"
    cnt, rt_list = MysqlConnection.execute_sql(sql)
    rt = []
    for line in rt_list:
        rt.append(dict(zip(columns, line)))
    return rt


def get_idcs_id(uid):
    rt = get_idcs_list()
    for user in rt:
        if user['id'] == int(uid):
            return user


def validate_idcs_add(name, address, ips):
    if name.strip() == '':
        return False, u'机房名称不能为空'
    if len(name) > 32:
        return False, u'机房名称长度不能大于32'
    idcs = get_idcs_list()
    for idc in idcs:
        if idc['name'] == name:
            return False, u'机房名称已存在'
    if len(address) > 32:
        return False, u'机房地址长度不能大于32'
    if ips.strip() == '':
        return False, u'机房IP网段不能为空'
    try:
        for ips in ips.split(','):
            for ip in ips.split('.'):
                if not ip.isdigit():
                    return False, u'IP输入非数字类型'
                else:
                    if int(ip) < 0 or int(ip) > 256:
                        return False, u'IP输入范围1-255'    
    except:
        return False, u'机房IP输入错误'
    return True, ''
 

def validate_idcs_modify(uid, name, address, ips):
    if name.strip() == '':
        return False, u'机房名称不能为空'
    if len(name) > 32:
        return False, u'机房名称长度不能大于32'
    if len(address) > 32:
        return False, u'机房地址长度不能大于32'
    if ips.strip() == '':
        return False, u'机房IP网段不能为空'
    try:
        for ips in ips.split(','):
            for ip in ips.split('.'):
                if not ip.isdigit():
                    return False, u'IP输入非数字类型'
                else:
                    if int(ip) < 0 or int(ip) > 256:
                        return False, u'IP输入范围1-255'    
    except:
        return False, u'机房IP输入错误'
    idc = get_idcs_id(uid)
    if idc['name'] != name:
        idcs = get_idcs_list()
        for sid in idcs:
            if sid['name'] == name:
                return False, u'机房名称已存在'
    return True, ''
    

def idcs_add(name, address, ips):
    columns = ("name", "address", "ips")
    sql = 'insert into idcs({}) values(%s, %s, %s)'.format(','.join(columns))
    args = (name, address, ips)
    print(sql)
    print(args)
    MysqlConnection.execute_sql(sql, args)


def get_idcs_id(uid):
    rt = get_idcs_list()
    for idc in rt:
        if idc['id'] == int(uid):
            return idc


def idcs_change(uid, name, address, ips):
    sql = 'update idcs set name=%s,address=%s,ips=%s where id=%s'
    args = (name, address, ips, uid)
    MysqlConnection.execute_sql(sql, args) 


def idcs_delete(uid):
    sql = 'update idcs set status=1 where id=%s'
    MysqlConnection.execute_sql(sql, (uid, ))

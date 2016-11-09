# coding=utf-8
#

from utils import MysqlConnection, md5_str


class User(object):
    def __init__(self, id, name, password, email, phone):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone

    @classmethod
    def validate_login(cls, name, password):
        _columns = ('id', 'name')
        _sql = 'select id,name from user where name=%s and password=%s'
        _count, _rt_list = MysqlConnection.execute_sql(_sql, (name, md5_str(password)))
        return dict(zip(_columns, _rt_list[0])) if _count != 0 else None

    @classmethod
    def validate_password(cls, username, password_old, password_new, password_repeat_new):
        if password_old.strip() == '':
            return False, u'原密码不能为空'
        _user = cls.validate_login(username, password_old)
        if not _user:
            return False, u'原密码错误'
        if password_new.strip() == '':
            return False, u'新密码不能为空'
        if len(password_new) < 6:
            return False, u'新密码长度不小于6位'
        if password_old == password_new:
            return False, u'新密码不能与原密码相同'
        if password_repeat_new.strip() == '':
            return False, u'确认新密码不能为空'
        if password_new != password_repeat_new:
            return False, u'新密码前后输入不匹配'
        return True, ''

    @classmethod
    def change_password(cls, username, password):
        _sql = 'update user set password=%s where name=%s'
        MysqlConnection.execute_sql(_sql, (md5_str(password), username))

    @classmethod
    def get_user_list(cls):
        _columns = ('id', 'name', 'password', 'email', 'phone')
        _sql = 'select * from user where 1=1'
        _args = []
        _count, _rt_list = MysqlConnection.execute_sql(_sql, _args)
        return [dict(zip(_columns, _line)) for _line in _rt_list]

    def validate_add(self):
        if self.name.strip() == '':
            return False, u'用户名不能为空'
        if not self.name.isalnum():
            return False, u'用户名由数字或字母组成'
        if len(self.name) < 6 or len(self.name) > 32:
            return False, u'用户名长度6-32位'
        user_list = self.get_user_list()
        for user in user_list:
            if user['name'] == self.name:
                return False, u'用户名存在'
        if self.password.strip() == '':
            return False, u'密码不能为空'
        if len(self.password) < 6: 
            return False, u'密码长度大于6位'
        if len(self.email) > 32:
            return False, u'邮箱长度不能超过32位'
        if len(self.phone) > 20:
            return False, u'电话长度不能超过20位'
        return True, ''

    def user_add(self):
        _sql = 'insert into user(name, password, email, phone) values(%s, %s, %s, %s)'
        _args = (self.name, md5_str(self.password), self.email, self.phone)
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def get_user_id(cls, uid):
        _users = cls.get_user_list()
        for _user in _users:
            if _user['id'] == int(uid):
                return _user

    def validate_change(self):
        if len(self.email) > 32:
            return False, u'邮箱长度不能超过32位'
        if len(self.phone) > 20:
            return False, u'电话长度不能超过20位'
        return True, ''

    def user_change(self):
        sql = 'update user set email=%s,phone=%s where id=%s'
        args = (self.email, self.phone, self.id)
        MysqlConnection.execute_sql(sql, args)

    @classmethod
    def user_delete(cls, uid):
        sql = 'delete from user where id=%s'
        MysqlConnection.execute_sql(sql, (uid, ))

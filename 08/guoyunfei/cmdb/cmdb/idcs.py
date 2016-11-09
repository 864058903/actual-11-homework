# coding=utf-8
#

from utils import MysqlConnection


class Idcs(object):
    def __init__(self, id, name, address, ip):
        self.id = id
        self.name = name
        self.address = address
        self.ip = ip 

    @classmethod
    def get_idcs_list(cls):
        _columns = ('id', 'name', 'address', 'ip')
        _sql = 'select * from idc where status=0'
        _args = []
        _count, _rt_list = MysqlConnection.execute_sql(_sql, _args)
        return [dict(zip(_columns, _line)) for _line in _rt_list]

    def validate_idcs_add(self):
        if self.name.strip() == '':
            return False, u'机房名称不能为空'
        if len(self.name) > 32:
            return False, u'机房名称长度不能大于32'
        idcs = self.get_idcs_list()
        for idc in idcs:
            if idc['name'] == self.name:
                return False, u'机房名称已存在'
        if len(self.address) > 32:
            return False, u'机房地址长度不能大于32'
        if self.ip.strip() == '':
            return False, u'机房IP网段不能为空'
        try:
            for ip in self.ip.split(','):
                for _ip in ip.split('.'):
                    if not _ip.isdigit():
                        return False, u'IP输入非数字类型'
                    else:
                        if int(_ip) < 0 or int(_ip) > 256:
                            return False, u'IP输入范围1-255'    
        except:
            return False, u'机房IP输入错误'
        return True, ''

    def idcs_add(self):
        _sql = 'insert into idc(name, address, ip) values(%s, %s, %s)'
        _args = (self.name, self.address, self.ip)
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def get_idc_id(cls, uid):
        _idcs = cls.get_idcs_list()
        for _idc in _idcs:
            if _idc['id'] == int(uid):
                return _idc

    def validate_idcs_change(self):
        if self.name.strip() == '':
            return False, u'机房名称不能为空'
        if len(self.name) > 32:
            return False, u'机房名称长度不能大于32'
        if len(self.address) > 32:
            return False, u'机房地址长度不能大于32'
        if self.ip.strip() == '':
            return False, u'机房IP网段不能为空'
        try:
            for ips in self.ip.split(','):
                for ip in ips.split('.'):
                    if not ip.isdigit():
                        return False, u'IP输入非数字类型'
                    else:
                        if int(ip) < 0 or int(ip) > 256:
                            return False, u'IP输入范围1-255'    
        except:
            return False, u'机房IP输入错误'
        idc = self.get_idc_id(self.id)
        if idc['name'] != self.name:
            idcs = self.get_idcs_list()
            for sid in idcs:
                if sid['name'] == self.name:
                    return False, u'机房名称已存在'
        return True, ''

    def idcs_change(self):
        sql = 'update idc set name=%s,address=%s,ip=%s where id=%s'
        args = (self.name, self.address, self.ip, self.id)
        print(args)
        MysqlConnection.execute_sql(sql, args)

    @classmethod
    def idcs_delete(cls, uid):
        sql = 'update idc set status=1 where id=%s'
        MysqlConnection.execute_sql(sql, (uid, ))
    

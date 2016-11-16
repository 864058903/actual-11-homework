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

    @classmethod
    def validate_idcs_create(cls, form):
        if len(form) == 0:
            return False, u'不能为空'
        if form['name'].strip() == '':
            return False, u'机房名称不能为空'
        if len(form['name']) > 32:
            return False, u'机房名称长度不能大于32'
        idcs = cls.get_idcs_list()
        for idc in idcs:
            if idc['name'] == form['name']:
                return False, u'机房名称已存在'
        if len(form['address']) > 32:
            return False, u'机房地址长度不能大于32'
        if form['ip'].strip() == '':
            return False, u'机房IP网段不能为空'
        try:
            for ip in form['ip'].split(','):
                for _ip in ip.split('.'):
                    if not _ip.isdigit():
                        return False, u'IP输入非数字类型'
                    else:
                        if int(_ip) < 0 or int(_ip) > 256:
                            return False, u'IP输入范围1-255'    
        except:
            return False, u'机房IP输入错误'
        return True, ''

    @classmethod
    def idcs_add(cls, form):
        _column_str = 'name,address,ip'
        _columns = _column_str.split(',')
        _args = []
        for _column in _columns:
            _args.append(form.get(_column, ''))
        _sql = 'insert into idc({0}) values({1})'.format(_column_str, ','.join(['%s']*len(_columns)))
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def get_idc_id(cls, uid):
        _idcs = cls.get_idcs_list()
        for _idc in _idcs:
            if _idc['id'] == int(uid):
                return _idc

    @classmethod
    def validate_idcs_change(cls, form):
        if len(form) == 0:
            return False, u'不能为空'
        if form['name'].strip() == '':
            return False, u'机房名称不能为空'
        if len(form['name']) > 32:
            return False, u'机房名称长度不能大于32'
        if len(form['address']) > 32:
            return False, u'机房地址长度不能大于32'
        if form['ip'].strip() == '':
            return False, u'机房IP网段不能为空'
        try:
            for ips in form['ip'].split(','):
                for ip in ips.split('.'):
                    if not ip.isdigit():
                        return False, u'IP输入非数字类型'
                    else:
                        if int(ip) < 0 or int(ip) > 256:
                            return False, u'IP输入范围1-255'    
        except:
            return False, u'机房IP输入错误'
        idc = cls.get_idc_id(form['id'])
        if idc['name'] != form['name']:
            idcs = cls.get_idcs_list()
            for sid in idcs:
                if sid['name'] == form['name']:
                    return False, u'机房名称已存在'
        return True, ''

    @classmethod
    def idcs_update(cls, form):
        _column_str = 'name,address,ip'
        _columns = _column_str.split(',')
        _values = []
        _args = []
        for _column in _columns:
            _values.append('{}=%s'.format(_column))
            _args.append(form.get(_column, ''))
        _args.append(form.get('id'))
        _sql = 'update idc set {} where id=%s'.format(','.join(_values))
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def idcs_delete(cls, uid):
        sql = 'update idc set status=1 where id=%s'
        MysqlConnection.execute_sql(sql, (uid, ))

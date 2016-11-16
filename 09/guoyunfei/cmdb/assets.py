# coding=utf-8

from utils import MysqlConnection
from idcs import Idcs


class Asset(object):
    def __init__(self, id, sn, hostname, os, ip,
                 machine_room_id, vendor, model,
                 cpu, ram, disk, time_on_shelves, over_guaranteed_date, business, admin):
        self.id = id
        self.sn = sn
        self.hostname = hostname
        self.os = os
        self.ip = ip
        self.machine_room_id = machine_room_id
        self.vendor = vendor
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.disk = disk
        self.time_on_shelves = time_on_shelves
        self.over_guaranteed_date = over_guaranteed_date
        self.business = business
        self.admin = admin

    @classmethod
    def get_asset_list(cls):
        _columns = 'id,sn,hostname,os,ip,machine_room_id,vendor,' \
                   'model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,business,admin,status'.split(',')
        _sql = 'select id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,' \
               'cpu,disk,time_on_shelves,over_guaranteed_date,business,admin,status from asset where status!=2'
        assets = []
        _count, _rt_list = MysqlConnection.execute_sql(_sql)
        for _line in _rt_list:
            asset = dict(zip(_columns, _line))
            for key in ['time_on_shelves', 'over_guaranteed_date']:
                if asset[key]:
                    asset[key] = asset[key].strftime('%Y-%m-%d')
            assets.append(asset)
        return assets

    @classmethod
    def get_asset_name(cls):
        _assets = cls.get_asset_list()
        _idcs = Idcs.get_idcs_list()
        for _asset in _assets:
            _id = _asset['machine_room_id']
            for _idc in _idcs:
                if _idc['id'] == _id:
                    _asset['machine_room_id'] = _idc['name']
        return _assets

    @classmethod
    def get_asset_id(cls, uid):
        _assets = cls.get_asset_list()
        for _asset in _assets:
            if _asset['id'] == uid:
                return _asset
        return {}

    @classmethod
    def validate_asset_create(cls, form):
        if form['sn'].strip() == '':
            return False, u'SN不能为空'
        asset_list = cls.get_asset_list()
        for asset in asset_list:
            if asset['sn'] == form['sn']:
                return False, u'SN已存在'
        if form['hostname'].strip() == '':
            return False, u'主机名不能为空'
        if form['ip'].strip() == '':
            return False, u'IP不能为空'
        if form['os'].strip() == '':
            return False, u'OS不能为空'
        if form['time_on_shelves'].strip() == '':
            return False, u'上架时间不能为空'
        if form['over_guaranteed_date'].strip() == '':
            return False, u'过保时间不能为空'
        return True, ''

    @classmethod
    def asset_create(cls, form):
        _column_str = 'sn,hostname,os,ip,machine_room_id,vendor,' \
                      'model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,business,admin,status'
        _columns = _column_str.split(',')
        _args = []
        for _column in _columns:
            _args.append(form.get(_column, ''))
        _sql = 'insert into asset({0}) values({1})'.format(_column_str, ','.join(['%s']*len(_columns)))
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def validate_asset_change(cls, form):
        if form['sn'].strip() == '':
            return False, u'SN不能为空'
        asset_list = cls.get_asset_list()
        for asset in asset_list:
            if asset['id'] != int(form['id']):
                if asset['sn'] == form['sn']:
                    return False, u'SN已存在'
        if form['hostname'].strip() == '':
            return False, u'主机名不能为空'
        if form['ip'].strip() == '':
            return False, u'IP不能为空'
        if form['os'].strip() == '':
            return False, u'OS不能为空'
        if form['time_on_shelves'].strip() == '':
            return False, u'上架时间不能为空'
        if form['over_guaranteed_date'].strip() == '':
            return False, u'过保时间不能为空'
        return True, ''

    @classmethod
    def asset_update(cls, form):
        _column_str = 'sn,hostname,os,ip,machine_room_id,vendor,' \
                      'model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,business,admin,status'
        _columns = _column_str.split(',')
        _values = []
        _args = []
        for _column in _columns:
            _values.append('{}=%s'.format(_column))
            _args.append(form.get(_column, ''))
        _args.append(form.get('id'))
        _sql = 'update asset set {} where id=%s'.format(','.join(_values))
        MysqlConnection.execute_sql(_sql, _args, False)

    @classmethod
    def asset_delete(cls, id):
        _sql = 'update asset set status=2 where id=%s'
        MysqlConnection.execute_sql(_sql, (id, ), False)


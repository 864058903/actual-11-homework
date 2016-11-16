# coding=utf-8
#
import pymysql
import hashlib
from config import *


def md5_str(value):
    md5 = hashlib.md5()
    md5.update(value)
    return md5.hexdigest()


class MysqlConnection(object):
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = password
        self.__database = database
        self.__charset = charset
        self.__conn = None
        self.__cur = None
        self.__connect()

    def __connect(self):
        try:
            self.__conn = pymysql.connect(host=self.__host, port=self.__port,
                                          user=self.__user, passwd=self.__password,
                                          database=self.__database, charset=self.__charset)
            self.__cur = self.__conn.cursor()
        except BaseException as e:
            print(e)

    def execute(self, sql, args=()):
        _cnt = 0
        if self.__cur:
            _cnt = self.__cur.execute(sql, args)
        return _cnt

    def fetch(self, sql, args=()):
        _cnt = 0
        _rt_list = []
        if self.__cur:
            _cnt = self.__cur.execute(sql, args)
            _rt_list = self.__cur.fetchall()
        return _cnt, _rt_list

    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def close(self):
        self.commit()
        if self.__cur:
            self.__cur.close()
            self.__cur = None
        if self.__conn:
            self.__conn.close()
            self.__conn = None

    @classmethod
    def execute_sql(cls, sql, args=(), is_fetch=True):
        _rt_list = []
        _conn = MysqlConnection(host=MYSQL_HOST, port=MYSQL_PORT,
                                user=MYSQL_USER, password=MYSQL_PASSWORD,
                                database=MYSQL_DATABASE, charset=MYSQL_CHARSET)
        if is_fetch:
            _cnt, _rt_list = _conn.fetch(sql, args)
        else:
            _cnt = _conn.execute(sql, args)
        _conn.close()
        return _cnt, _rt_list


# coding=utf-8

import pymysql
import conf


class MysqlConnect(object):
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.__conn = None
        self.__cur = None
        self.__connect()

    def __connect(self):
        try:
            self.__conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                          password=self.password, database=self.database, charset=self.charset)
            self.__cur = self.__conn.cursor()
        except BaseException as e:
            print(e)

    def commit(self):
        if self.__conn:
            self.__conn.commit()

    def close(self):
        if self.__cur:
            self.__cur.close()
            self.__cur = None
        if self.__conn:
            self.__conn.close()
            self.__conn = None

    def execute(self, sql, args=()):
        cnt = 0
        rt_list = []
        if self.__cur:
            cnt = self.__cur.execute(sql, args)
            self.__conn.commit()
            rt_list = self.__cur.fetchall()
        return cnt, rt_list

    @classmethod
    def execute_sql(cls, sql, args=()):
        __conn = MysqlConnect(host=conf.MYSQL_HOST, port=conf.MYSQL_PORT,
                              user=conf.MYSQL_USER, password=conf.MYSQL_PASSWORD,
                              database=conf.MYSQL_DATABASE, charset=conf.MYSQL_CHARSET)
        cnt, rt_list = __conn.execute(sql, args)
        __conn.close()
        return cnt, rt_list




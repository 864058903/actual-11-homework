#encoding: utf-8

import MySQLdb
import gconf

def execute_sql(sql,args=(),fetch=True):
    try:
        _conn = None
        _cursor = None
        _count = 0
        _rt_list = []
        _conn = MySQLdb.connect(host=gconf.MYSQL_HOST, \
                                port=gconf.MYSQL_PORT, \
                                user=gconf.MYSQL_USER, \
                                passwd=gconf.MYSQL_PASSWD, \
                                db=gconf.MYSQL_DB, \
                                charset=gconf.MYSQL_CHARSET)
        _cursor = _conn.cursor()
        _count = _cursor.execute(sql,args)
        if fetch:
            _rt_list = _cursor.fetchall()
        else:
            _conn.commit()
    except BaseException as e:
        print e
    finally:
        if _cursor:
            _cursor.close()
        if _conn:
            _conn.close()
            
    return _count, _rt_list


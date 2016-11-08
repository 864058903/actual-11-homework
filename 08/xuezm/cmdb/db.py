#coding=utf8

import   MySQLdb  as  mysql
from conf  import   config

conn=mysql.connect(user=config.db_user,
                   host=config.db_host,
                   passwd=config.db_password,
                   db=config.db_name,
                   charset=config.db_charset)
conn.autocommit(True)


def selectone(fields,table,where):
    sql ="select  %s from  %s  where  %s"%(','.join(fields),table,where)
    curs = conn.cursor()
    curs.execute(sql)
    result=curs.fetchone()
    if result:
        result=dict(zip(fields,result))
        return   result
    else:
        return  {}



def selectall(fields,table):
    sql ="select  %s from  %s "%(",".join(fields),table)
    curs = conn.cursor()
    curs.execute(sql)
    result=curs.fetchall()
    result=[dict(zip(fields,i))  for  i  in result]
    return   result

def  adddata(table,fields,value):
    sql =" INSERT INTO %s (%s) VALUES ('%s')"%(table,','.join(fields),"','".join(value))
    curs = conn.cursor()
    curs.execute(sql)

def  deldata(table,where):
    sql = "delete  from  %s  where %s"%(table,where)
    curs = conn.cursor()
    curs.execute(sql)

def  updata(table,value,where):
    sql="update  %s   set   %s where  %s "%(table,",".join(value),where)
    curs = conn.cursor()
    curs.execute(sql)


if __name__=="__main__":
        fields=('id','username','password','age')
        where="username='%s'"%'xuezm1'
        result=selectone(",".join(fields),'users',where)
        print result
        #print result (1L, u'xuezm', u'xuezm', u'26')
        #print zip(fields,result)

#encoding:utf-8
import gconf
import MySQLdb

MYSQL_get_user_all='select id,username,groups,tel,status from user'
MYSQL_auth_user='select id,username from user where username=%s and password=md5(%s)'
MYSQL_get_room_all='select id,names,addr,ip_ranges from machine_room'
MYSQL_get_room_one='select id,names,addr,ip_ranges from machine_room where id=%s'
MYSQL_same_room_name='select * from machine_room where names= %s'
MYSQL_same_room_name2='select * from machine_room where names= %s and id !=%s'
MYSQL_save_room_modify='update machine_room set names = %s,addr = %s,ip_ranges = %s  where id = %s'
MYSQL_save_room_add='insert into  machine_room(names,addr,ip_ranges) values(%s,%s,%s)'
MYSQL_save_room_del='delete from  machine_room  where id=%s'
MYSQL_search_room_key='select id,names,addr,ip_ranges from machine_room where names like %s or addr like %s or ip_ranges like %s'


def auth_user(username,password):
   conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                        port=gconf.MYSQL_PORT,\
                        user=gconf.MYSQL_USER,\
                        db=gconf.MYSQL_DB,\
                        passwd=gconf.MYSQL_PASSWD,\
                        charset=gconf.MYSQL_CHARSET)

   cursor=conn.cursor()
   cursor.execute(MYSQL_auth_user,(username,password))
   result=cursor.fetchone()
   cursor.close()
   conn.close()
   return result


def get_room_all():
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    cursor.execute(MYSQL_get_room_all)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    #room_col='id,name,addr,ip_ranges'
    return result    

def get_room_one(roomid):
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    cursor.execute(MYSQL_get_room_one,(roomid,))
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    #room_col='id,name,addr,ip_ranges'
    return result

def same_room_name(roomname,addr,ip_ranges,roomid=None):
    if not roomname.strip(): 
       return False,"machine's name can't null."
    if not addr.strip(): 
       return False,"machine's addr can't null."
    if not ip_ranges.strip(): 
       return False,"machine's ip_ranges can't null."
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    #room_add
    if roomid is None:
         cnt=cursor.execute(MYSQL_same_room_name,(roomname,))
    #room_modify
    else:
         cnt=cursor.execute(MYSQL_same_room_name2,(roomname,roomid))
    cursor.close()
    conn.close()
    #room_col='id,name,addr,ip_ranges'
    if cnt != 0:
        return False,'same name error.'
    else:
        return True,''
 
def save_room_modify(names,addr,ip_ranges,id):
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    cnt=cursor.execute(MYSQL_save_room_modify,(names,addr,ip_ranges,id))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def save_room_add(roomname,addr,ip_ranges):
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    cursor.execute(MYSQL_save_room_add,(roomname,addr,ip_ranges))
    conn.commit()
    cursor.close()
    conn.close()
    #room_col='id,name,addr,ip_ranges'
    return True


def save_room_del(roomid):
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    cursor.execute(MYSQL_save_room_del,(roomid,))
    conn.commit()
    cursor.close()
    conn.close()
    return  True

def search_room_key(key=None):
    conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                         port=gconf.MYSQL_PORT,\
                         user=gconf.MYSQL_USER,\
                         passwd=gconf.MYSQL_PASSWD,\
                         db=gconf.MYSQL_DB,\
                         charset=gconf.MYSQL_CHARSET)
    cursor=conn.cursor()
    #key is None
    if not key:
        cursor.execute(MYSQL_get_room_all)
    #key 
    else:
        key='%'+key+'%'
        cursor.execute(MYSQL_search_room_key,(key,key,key))
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return  result


if __name__=='__main__':
     save_room_one('ttt','yyy','uuuuu',1)

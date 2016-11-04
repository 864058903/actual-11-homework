#encoding:utf-8
import gconf
import MySQLdb

MYSQL_get_user_all='select id,username,t2.deptname,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  from user t1 left join depts t2 on t2.dept_en=t1.dept'
MYSQL_get_user_key='select id,username,dept,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  where username like %s or groups like %s or tel like %s'
MYSQL_auth_user='select id,username from user where username=%s and password=md5(%s)'
MYSQL_same_user='select id  from user where username=%s'
MYSQL_add_user='insert into  user(username,password,groups,tel,status,email,birthday,age,sex,dept,hobby,bz) values(%s,md5(%s),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
MYSQL_same_user_modify='select id  from user where username=%s and id !=%s'

MYSQL_search_user_valid='select id,username,dept,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  from user where status = %s'
MYSQL_search_user_key='select id,username,dept,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  from user where username like %s or groups like %s or tel like %s or email like %s or hobby like %s or bz like %s'
MYSQL_search_user_ukey='select id,username,dept,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  from user where status=%s and ( username like %s or groups like %s or tel like %s or email like %s or hobby like %s or bz like %s)'
MYSQL_get_user_one='select id,username,password,dept,(case when sex=1 then "男" else "女" end) as sex,age,birthday,tel,email,hobby,bz,groups,(case when status="valid" then "有效" else "无效" end) as status  from user where id=%s'
MYSQL_save_user_modify='update user   set username=%s,password=md5(%s),groups=%s,tel=%s,status=%s,email=%s,birthday=%s,age=%s,sex=%s,dept=%s,hobby=%s,bz=%s  where id=%s'
MYSQL_save_user_del='delete from  user where id=%s'



MYSQL_get_room_all='select id,names,addr,ip_ranges from machine_room'
MYSQL_get_room_one='select id,names,addr,ip_ranges from machine_room where id=%s'
MYSQL_same_room_name='select * from machine_room where names= %s'
MYSQL_same_room_name2='select * from machine_room where names= %s and id !=%s'
MYSQL_save_room_modify='update machine_room set names = %s,addr = %s,ip_ranges = %s  where id = %s'
MYSQL_save_room_add='insert into  machine_room(names,addr,ip_ranges) values(%s,%s,%s)'
MYSQL_save_room_del='delete from  machine_room  where id=%s'
MYSQL_search_room_key='select id,names,addr,ip_ranges from machine_room where names like %s or addr like %s or ip_ranges like %s'


def mysql_exe(sql,args='',cnt=False):
   conn=MySQLdb.connect(host=gconf.MYSQL_HOST,\
                          port=gconf.MYSQL_PORT,\
                          user=gconf.MYSQL_USER,\
                          db=gconf.MYSQL_DB,\
                          passwd=gconf.MYSQL_PASSWD,\
                          charset=gconf.MYSQL_CHARSET)
   cursor=conn.cursor()
   if cnt:
       result=cursor.execute(sql,args)
   else:
       cursor.execute(sql,args)
       result=cursor.fetchall()
       conn.commit()
   cursor.close()
   conn.close()
   return result
 


def get_user(key=None):
   if key:
     key='%'+key+'%'
     result=mysql_exe(MYSQL_get_user_key,(key,key,key))
   else:
     result=mysql_exe(MYSQL_get_user_all)
   return result

def auth_user(username,password):
   result=mysql_exe(MYSQL_auth_user,(username,password))
   return result

def same_user(username,password,age,sex):
   if not username:
       return False,'username  cant be empty'
   if not password:
       return False,'password  cant be empty'
   if not str(age).isdigit():
       return False,'age  cant\'t is string'
   if not str(sex).isdigit():
       return False,'sex  cant\'t is string'
   cnt=mysql_exe(MYSQL_same_user,(username,),True)
   if cnt != 0:
      return False,'same username error.'
   else:
      return True,''

def add_user(username,password,groups,tel,email,birthday,age,sex,dept,hobby_l,bz):
   result=mysql_exe(MYSQL_add_user,(username,password,groups,tel,'valid',email,birthday,age,sex,dept,hobby_l,bz))
   return True


def search_user(u_valid,key=None):
   if not key and u_valid == 'all':
      result=mysql_exe(MYSQL_get_user_all)
   elif not key and u_valid != 'all':
      result=mysql_exe(MYSQL_search_user_valid,(u_valid,))
   elif  key and u_valid == 'all':   
      key='%'+key+'%'
      result=mysql_exe(MYSQL_search_user_key,(key,key,key,key,key,key))
   elif  key and u_valid != 'all':   
      key='%'+key+'%'
      result=mysql_exe(MYSQL_search_user_ukey,(u_valid,key,key,key,key,key,key))
   return result


def get_user_one(userid):
   result=mysql_exe(MYSQL_get_user_one,(userid,))
   return result

def same_user_modify(userid,username,password,dept,age,sex):
   if not username:
       return False,'username  cant be empty'
   if not password:
       return False,'password  cant be empty'
   if not dept:
       return False,'dept  cant be empty'
   if not str(age).isdigit():
       return False,'age  cant\'t is string'
   if not str(sex).isdigit():
       return False,'sex  cant\'t is string'
   cnt=mysql_exe(MYSQL_same_user_modify,(username,userid),True)
   if cnt != 0:
      return False,'same username error.'
   else:
      return True,''

def save_user_modify(userid,username,password,groups,tel,status,email,birthday,age,sex,dept,hobby,bz):
   result=mysql_exe(MYSQL_save_user_modify,(username,password,groups,tel,status,email,birthday,age,sex,dept,hobby,bz,userid))
   return True

def save_user_del(userid):
   result=mysql_exe(MYSQL_save_user_del,(userid,))
   return True


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

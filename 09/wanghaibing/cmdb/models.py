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
SQL_ASSET_LIST_COLUMNS = 'id,sn,hostname,os,ip,machine_room,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status'.split(',')
SQL_ASSET_LIST = 'select t1.id,sn,hostname,os,ip,t2.names as machine_room,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,(case when status=0 then "上线"else "维护" end) as status from asset t1 left join machine_room t2 on t2.id=t1.machine_room_id  where status != 2'
SQL_ASSET_LIST_ONE = 'select id,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status from asset where status != 2 and id = %s'
SQL_ASSET_CHECK_DATA_UPDATE = 'select sn from asset where sn = %s and id != %s '
SQL_ASSET_CHECK_DATA_CREATE = 'select sn from asset where sn = %s '
SQL_ASSET_UPDATE_SAVE = 'update asset set sn=%s,hostname=%s,os=%s,ip=%s,machine_room_id=%s,vendor=%s,model=%s,ram=%s,cpu=%s,disk=%s,time_on_shelves=%s,over_guaranteed_date=%s,buiness=%s,admin=%s,status=%s  where id = %s '
SQL_ASSET_DEL_SAVE='update asset set status=2 where id=%s'
SQL_ASSET_CREATE_SAVE = 'insert into  asset(sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '

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
    result=mysql_exe(MYSQL_get_room_all)
    return result    

def get_room_one(roomid):
    result=mysql_exe(MYSQL_get_room_one,(roomid,))
    return result

def same_room_name(roomname,addr,ip_ranges,roomid=None):
    if not roomname.strip(): 
       return False,"machine's name can't null."
    if not addr.strip(): 
       return False,"machine's addr can't null."
    if not ip_ranges.strip(): 
       return False,"machine's ip_ranges can't null."
    #room_add
    if roomid is None:
         cnt=mysql_exe(MYSQL_same_room_name,(roomname,),True)
    #room_modify
    else:
         cnt=mysql_exe(MYSQL_same_room_name2,(roomname,roomid),True)
    #room_col='id,name,addr,ip_ranges'
    if cnt != 0:
        return False,'same name error.'
    else:
        return True,''
 
def save_room_modify(names,addr,ip_ranges,id):
    #room_modify
    mysql_exe(MYSQL_save_room_modify,(names,addr,ip_ranges,id))
    return True

def save_room_add(roomname,addr,ip_ranges):
    mysql_exe(MYSQL_save_room_add,(roomname,addr,ip_ranges))
    #room_col='id,name,addr,ip_ranges'
    return True


def save_room_del(roomid):
    mysql_exe(MYSQL_save_room_del,(roomid,))
    return  True

def search_room_key(key=None):
    #key is None
    if not key:
        result=mysql_exe(MYSQL_get_room_all)
    #key 
    else:
        key='%'+key+'%'
        result=mysql_exe(MYSQL_search_room_key,(key,key,key))
    return  result

def get_assets():
    rt_list = mysql_exe(SQL_ASSET_LIST)
    assets=[]
    for rt in rt_list:
        asset=dict(zip(SQL_ASSET_LIST_COLUMNS,rt))
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
               asset[key]=asset[key].strftime('%Y-%m-%d')
        assets.append(asset) 
    return  assets

def get_assets_one(aid):
    rt_list = mysql_exe(SQL_ASSET_LIST_ONE,(aid,))
    assets=[]
    for rt in rt_list:
        asset=dict(zip(SQL_ASSET_LIST_COLUMNS,rt))
        for key in 'time_on_shelves,over_guaranteed_date'.split(','):
            if asset[key]:
               asset[key]=asset[key].strftime('%Y-%m-%d')
        assets.append(asset)
    return  assets[0] if  assets else {}

#数据合法性这里只检测主机名、管理员
def asset_check(op,sn,hostname,admin,aid):
     if not sn:
          return False,'sn cannot be empty'
     if op == 'update':
        result=mysql_exe(SQL_ASSET_CHECK_DATA_UPDATE,(sn,aid),True)
        if result != 0:
           return False,'sn cannot be repeated'
     else:
        result=mysql_exe(SQL_ASSET_CHECK_DATA_CREATE,(sn,),True)
        if result != 0:
           return False,'sn cannot be repeated'
      
     if not hostname:
          return False,'hostname cannot be empty'
     if not admin:
          return False,'admin cannot be empty'
     return True,''

def update_asset_save(aid,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status):
     #mysql_exe(SQL_ASSET_UPDATE_SAVE,(args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],args[10],args[11],args[12],args[13],args[14],args[15],args[0]))
     mysql_exe(SQL_ASSET_UPDATE_SAVE,(sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status,aid))
     return True

def asset_del(aid):
     result=mysql_exe(SQL_ASSET_DEL_SAVE,(aid,))
     if not  result:
         return True,''
     else :
         return False,'未删除成功'
        
def create_asset_save(sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status):
     mysql_exe(SQL_ASSET_CREATE_SAVE,(sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status))    
     return True


if __name__=='__main__':
     save_room_one('ttt','yyy','uuuuu',1)

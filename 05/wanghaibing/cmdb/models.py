#encoding:utf-8
import json
import gconf

def get_user():
    fh=open(gconf.USER_DB_PATH,'rb')
    user=json.loads(fh.read())
    fh.close()
    return user

def auth_user(username,password):
    users=get_user()
    for user in users:
        if user.get('username')==username and user.get('password')==password and user.get('status') == "valid":
            return user
    return None  

def same_user(username,u_id=0):
    users=get_user()
    #检查是否有系统同名用户
    if u_id == 0:
       for user in users:
           if user.get('username')==username :
              return user
       return None  
    #更名时，检查更名后是否有同名
    else:
       for user in users:
           if user.get('username')==username and user.get('id') != int(u_id):
              return user
       return None  

def add_user(new_user):
    users=get_user()
    new_user['id'] =max([users[x]['id'] for x  in range(len(users))])+1 
    new_user['status'] = "valid"
    users.append(new_user)
    fh=open(gconf.USER_DB_PATH,'wb')
    users=json.dumps(users)
    fh.write(users)
    fh.close()
    return True   

    
def del_user(username):
    result=same_user(username)
    users=get_user()
    for i in range(len(users)):
      if users[i]['username'] == username:
         del users[i]
         break
    #users.append(result)
    fh=open(gconf.USER_DB_PATH,'wb')
    users=json.dumps(users)
    fh.write(users)
    fh.close()
    return True   

def modify_user(new_user):
    users=get_user()
    for i in range(len(users)):
       if users[i]['id'] == new_user['id']:
          users[i]=new_user
          break
    fh=open(gconf.USER_DB_PATH,'wb')
    users=json.dumps(users)
    fh.write(users)
    fh.close()
    return True   
    

def search_user(u_valid,str_key=None):
    users=get_user()
    searched_u=[]
    if   str_key and u_valid != 'all':
       for user  in users:
           if (str_key in user['username'] or str_key in user['tel']) and user['status'] == u_valid:
               searched_u.append(user)
       return searched_u
    if  not str_key   and u_valid != 'all':      
       for user  in users:
           if  user['status'] == u_valid:
               searched_u.append(user)
       return searched_u
    if  str_key  and  u_valid == 'all':      
       for user  in users:
           if str_key in user['username'] or str_key in user['tel']:
               searched_u.append(user)
       return searched_u
    if not  str_key    and u_valid == 'all':      
       for user  in users:
              searched_u.append(user)
       return searched_u

def top_log(log_file,topn=10):
   r_file=open(log_file,'rb')
   r_dict={}
   for line in r_file:
       key=line.split()
       key=key[0],key[8],key[10]
       r_dict[key]=r_dict.setdefault(key,0)+1

   r_file.close()
   result=sorted(r_dict.items(),key=lambda x:x[1])
   return result[:-topn-1:-1]


if __name__=='__main__':
   search_user('all')

    

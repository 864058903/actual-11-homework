#!/usr/bin/evn python
#incoding:utf-8
#导入flask
from flask  import render_template
from flask  import request
from flask  import redirect
from flask  import session

import json

from cmdb import app
import models

@app.route('/')
def index():
    if session.get('user'):return redirect('/users/')
    return render_template('index.html')


@app.route('/login/',methods=['POST'])
def login():
    username=request.form.get('username','')
    password=request.form.get('password','')
    result=models.auth_user(username,password)
    if result:
       session['user']=username
       return redirect('/users/')
    else:
       return render_template('index.html',username=username,password=password,error='Name or password errror, or  name was locked.')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')



@app.route('/users/')
def user_index():
    if not session.get('user'): return redirect('/')
    #result=models.get_user()
    return render_template('users.html')

@app.route('/users/list/')
def view_user():
    if not session.get('user'): return redirect('/')
    result=models.get_user()
    return json.dumps({'data':result})

@app.route('/view_adduser/')
def view_adduser():
    if not session.get('user'): return redirect('/')
    return render_template('user_add.html')


@app.route('/add_users/',methods=['post','get'])
def add_user():
     if not session.get('user'): return redirect('/')
     param = request.args if  request.method == 'GET' else request.form
     username=param.get('username','').strip()
     password=param.get('password','').strip()
     groups=param.get('groups','').strip()
     tel=param.get('tel','').strip()
     email=param.get('email','').strip()
     birthday=param.get('birthday','').strip()
     age=param.get('age','').strip()
     sex= param.get('sex','').strip()
     dept=param.get('dept','').strip()
     hobby_l=' | '.join(param.getlist('hobby'))
     #hobby_l=str(param.getlist('hobby'))
     bz=param.get('bz','').strip()
     
     OK,error=models.same_user(username,password,age,sex)
     if  OK :
        models.add_user(username,password,groups,tel,email,birthday,int(age),int(sex),dept,hobby_l,bz)
        return redirect('/users/')
     else:
        return render_template('/user_add.html/',error=error,username=username,password=password,groups=groups,tel=tel,email=email,birthday=birthday,age=age,sex=sex,dept=dept,bz=bz)  


@app.route('/add_users/json/',methods=['post','get'])
def add_user_json():
     if not session.get('user'): return redirect('/')
     param = request.args if  request.method == 'GET' else request.form
     username=param.get('username','').strip()
     password=param.get('password','').strip()
     groups=param.get('groups','').strip()
     tel=param.get('tel','').strip()
     email=param.get('email','').strip()
     birthday=param.get('birthday','').strip()
     age=param.get('age','').strip()
     sex= param.get('sex','').strip()
     dept=param.get('dept','').strip()
     hobby_l=' | '.join(param.getlist('hobby'))
     #hobby_l=str(param.getlist('hobby'))
     bz=param.get('bz','').strip()
     
     OK,error=models.same_user(username,password,age,sex)
     if  OK :
        models.add_user(username,password,groups,tel,email,birthday,int(age),int(sex),dept,hobby_l,bz)
        return json.dumps({'code':200})
     else:
        #return json.dumps({'code':400,'error':error})  
        return json.dumps({'code':400,'error':error,'username':username,'password':password,'groups':groups,'tel':tel,'email':email,'birthday':birthday,'age':age,'sex':sex,'dept':dept,'bz':bz})  


@app.route('/users/search/')
def search_user():
     if not session.get('user'): return redirect('/')
     u_valid=request.args.get('u_valid')
     key=request.args.get('key','').strip()
     result=models.search_user(u_valid,key)
     return render_template('users.html',users=result,u_valid=u_valid,key=key)


@app.route('/view_usermodify/' )
def view_usermodify():
    if not session.get('user'): return redirect('/')
    userid=request.args.get('userid','')
    result=models.get_user_one(userid)
    return render_template('/user_modify.html/',id=result[0][0],username=result[0][1],password=result[0][2],dept=result[0][3],sex=result[0][4],age=result[0][5],birthday=result[0][6],tel=result[0][7],email=result[0][8],hobby=result[0][9],bz=result[0][10], groups=result[0][11],status=result[0][12])
    #return render_template('/user_modify.html/',id=result[0],username=result[1],password=result[2],dept=result[3],sex=result[4],age=result[5],birthday=result[6],tel=result[7],email=result[8],hobby=result[9],bz=result[10], groups=result[11],status=result[12])


@app.route('/user_modify/', methods=['post'])
def user_modify():
    if not session.get('user'): return redirect('/')
    userid=request.form.get('id','').strip()
    username=request.form.get('username','').strip()
    password=request.form.get('password','').strip()
    groups=request.form.get('groups','').strip()
    tel=request.form.get('tel','').strip()
    status=request.form.get('status','').strip()
    email=request.form.get('email','').strip()
    birthday=request.form.get('birthday','').strip()
    age=request.form.get('age','').strip()
    sex=request.form.get('sex','').strip()
    dept=request.form.get('dept','').strip()
    hobby=' | '.join(request.form.getlist('hobby'))
    bz=request.form.get('bz','').strip()
    OK,error=models.same_user_modify(userid,username,password,dept,age,sex)
    if OK:
        models.save_user_modify(userid,username,password,groups,tel,status,email,birthday,int(age),int(sex),dept,hobby,bz)
        return redirect('/users/')
    else:
        return render_template('/user_modify.html/',error=error,id=userid,username=username,password=password,dept=dept,sex=sex,age=age,birthday=birthday,tel=tel,email=email,hobby=hobby,bz=bz, groups=groups,status=status)


@app.route('/view_userdel/')
def view_userdel():
    if not session.get('user'):  return redirect('/')
    userid=request.args.get('userid','')
    return render_template('user_del.html',id=userid)

@app.route('/users/user_del/',methods=['post'])
def user_del():
    if not session.get('user'): return redirect('/')
    userid=request.form.get('id','')
    models.save_user_del(userid)
    return redirect('/users/')

@app.route('/users/user_del2/')
def user_del2():
    if not session.get('user'): return redirect('/')
    userid=request.args.get('id','')
    models.save_user_del(userid)
    return redirect('/users/')






@app.route('/rooms/')
def rooms():
    if not session.get('user'): return redirect('/')
    rooms=models.get_room_all()  
    #return str(result)
    return render_template('rooms.html',rooms=rooms)  

@app.route('/view_room_modify/')
def view_room_modify():
    if not session.get('user'): return redirect('/')
    roomid=int(request.args.get('roomid',''))
    result=models.get_room_one(roomid)
    return render_template('room_modify.html',rooms=result)


@app.route('/room_modify/',methods=['POST'])
def room_modify():
    if not session.get('user'): return redirect('/')
    roomid=request.form.get('roomid','').strip()
    roomname=request.form.get('roomname','').strip()
    addr=request.form.get('addr','').strip()
    ip_ranges=request.form.get('ip_ranges','').strip()
    #rew_room=(roomname,addr,ipranges,roomid)
    OK,error=models.same_room_name(roomname,addr,ip_ranges,roomid)
    
    if OK:
       models.save_room_modify(roomname,addr,ip_ranges,roomid)
       return redirect('/rooms/')
    else:    
       return render_template('room_modify.html',roomid=roomid,roomname=roomname,addr=addr,ip_ranges=ip_ranges,error=error)
   

@app.route('/view_room_add/')
def view_room_add():
    if not session.get('user'): return redirect('/')
    return render_template('room_add.html')


@app.route('/room_add/',methods=['POST'])
def room_add():
    if not session.get('user'): return redirect('/')
    roomname=request.form.get('roomname','')
    addr=request.form.get('addr','')
    ip_ranges=request.form.get('ip_ranges','')
    OK,error=models.same_room_name(roomname,addr,ip_ranges)
    if OK:
       models.save_room_add(roomname,addr,ip_ranges)
       return redirect('/rooms/')
    else:
       return render_template('/room_add.html/',roomname=roomname,addr=addr,ip_ranges=ip_ranges,error=error)

@app.route('/room_add/json/',methods=['POST'])
def room_add_json():
    if not session.get('user'): return redirect('/')
    roomname=request.form.get('roomname','')
    addr=request.form.get('addr','')
    ip_ranges=request.form.get('ip_ranges','')
    OK,error=models.same_room_name(roomname,addr,ip_ranges)
    if OK:
       #models.save_room_add(roomname,addr,ip_ranges)
       return json.dumps({'code':200})
    else:
       return json.dumps({'code':400,'error':error})

@app.route('/rooms/view_room_del/')
def view_room_del():
     if not session.get('user'): return redirect('/')
     roomid=request.args.get('roomid','')
     return render_template('room_del.html',roomid=roomid)

@app.route('/rooms/room_del/',methods=['post'])
def room_del():
     if not session.get('user'): return redirect('/')
     result=models.save_room_del(request.form.get('roomid',''))
     if result:
        return redirect('/rooms/')
     else:
        return render_template('view_room_del.html',roomid=roomid,error='Del error.')

@app.route('/rooms/room_del/json/')
def room_del_json():
     if not session.get('user'): return redirect('/')
     result=models.save_room_del(request.args.get('roomid',''))
     if result:
        return redirect('/rooms/')
     else:
        return render_template('view_room_del.html',roomid=roomid,error='Del error.')

@app.route('/rooms/search/')
def rooms_search():
     if not session.get('user'): return redirect('/')
     key=request.args.get('key','')
     result=models.search_room_key(key)
     #return str(result)
     return render_template('rooms.html',rooms=result,key=key)

@app.route('/assets/')
def assets_index():
    if not session.get('user'): return redirect('/')
    rooms=models.get_room_all()
    return render_template('assets.html',rooms=rooms)

@app.route('/assets/assets_list/')
def assets_list():
    if not session.get('user'): return redirect('/')
    result = models.get_assets()
    return json.dumps({'data':result})

@app.route('/edit_asset/view/')
def edit_assets_view():
    if not session.get('user'): return redirect('/')
    aid=request.args.get('id','')
    result = models.get_assets_one(aid)
    return json.dumps(result)

@app.route('/edit_asset/save/',methods=['POST'])
def edit_assets_save():
    if not session.get('user'): return redirect('/')
    aid=int(request.form.get('id',''))
    sn=request.form.get('sn','')
    hostname=request.form.get('hostname','')
    os=request.form.get('os','')
    ip=request.form.get('ip','')
    machine_room_id=int(request.form.get('machine_room_id',''))
    vendor=request.form.get('vendor','')
    model=request.form.get('model','')
    ram=int(request.form.get('ram',''))
    cpu=int(request.form.get('cpu',''))
    disk=int(request.form.get('disk',''))
    time_on_shelves=request.form.get('time_on_shelves','')
    over_guaranteed_date=request.form.get('over_guaranteed_date','')
    buiness=request.form.get('buiness','')
    admin=request.form.get('admin','')
    status=int(request.form.get('status',''))
    OK,error = models.asset_check('update',sn,hostname,admin,aid)
    if OK:
        models.update_asset_save(aid,sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status)
        return json.dumps({'code':200})
    else:
        return json.dumps({'code':error})

@app.route('/asset_del/',methods=['POST'])
def assets_del():
    if not session.get('user'): return redirect('/')
    aid=request.form.get('id','')
    ok,error=models.asset_del(aid)
    if ok:
        return json.dumps({'code':200})
    else:
        return json.dumps({'code':error})

@app.route('/create_asset/json/',methods=['POST'])
def create_asset():
    if not session['user']: return redirect('/')
    sn=request.form.get('sn_c','')
    hostname=request.form.get('hostname_c','')
    os=request.form.get('os_c','')
    ip=request.form.get('ip_c','')
    machine_room_id=request.form.get('machine_room_id_c','')
    vendor=request.form.get('vendor_c','')
    model=request.form.get('model_c','')
    ram=request.form.get('ram_c','')
    cpu=request.form.get('cpu_c','')
    disk=request.form.get('disk_c','')
    time_on_shelves=request.form.get('time_on_shelves_c','')
    over_guaranteed_date=request.form.get('over_guaranteed_date_c','')
    buiness=request.form.get('buiness_c','')
    admin=request.form.get('admin_c','')
    status=request.form.get('status_c','')
    OK,error = models.asset_check('create',sn,hostname,admin,None)
    #OK=True
    if OK:
        models.create_asset_save(sn,hostname,os,ip,machine_room_id,vendor,model,ram,cpu,disk,time_on_shelves,over_guaranteed_date,buiness,admin,status)
        return json.dumps({'code':200})
    else:
        return json.dumps({'code':error})

@app.route('/monitor/host/create/',methods=['POST'])
def monitor_host_create():
    models.monitor_host_create(request.form)
    return json.dumps({'code':200,'result':''}) 

@app.route('/monitor/host/list/',methods=['GET','POST'])
def monitor_host_list():
    #ip=str(request.form.get('ip',''))
    #h_limit=request.form.get('h_limit','')
    ip=str(request.args.get('ip',''))
    h_limit=int(request.args.get('h_limit',''))
    print h_limit
    result=models.get_monitor_list(ip,h_limit)
    return json.dumps({'code' : 200, 'result' : result})

    
@app.route('/open_pass_modify/')
def open_pass_modify():
    userid=request.args.get('id','')
    pass_old1=models.get_user_one(userid)[0][2]
    print pass_old1
    return json.dumps({'code':userid,'pass_old1':pass_old1})


@app.route('/pass_modify_save/')
def pass_modify_save():
    ok,error=models.pass_modify_save(request.args)
    if ok:
       return json.dumps({'code':200})
    else:
       return json.dumps({'code':error})

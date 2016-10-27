#!/usr/bin/evn python
#incoding:utf-8
from flask  import Flask
from flask  import render_template
from flask  import request,redirect
import models

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/',methods=['POST'])
def login():
    username=request.form.get('username','')
    password=request.form.get('password','')
    result=models.auth_user(username,password)
    if result:
       return redirect('/rooms/')
    else:
       return render_template('index.html',username=username,password=password,error='name or password errror. or your name was locked.')

@app.route('/rooms/')
def rooms():
    rooms=models.get_room_all()  
    #return str(result)
    return render_template('rooms.html',rooms=rooms)  

@app.route('/view_room_modify/')
def view_room_modify():
    roomid=int(request.args.get('roomid',''))
    result=models.get_room_one(roomid)
    return render_template('room_modify.html',rooms=result)

@app.route('/room_modify/',methods=['POST'])
def room_modify():
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
    return render_template('room_add.html')


@app.route('/room_add/',methods=['POST'])
def room_add():
    roomname=request.form.get('roomname','')
    addr=request.form.get('addr','')
    ip_ranges=request.form.get('ip_ranges','')
    OK,error=models.same_room_name(roomname,addr,ip_ranges)
    if OK:
       models.save_room_add(roomname,addr,ip_ranges)
       return redirect('/rooms/')
    else:
       return render_template('/room_add.html/',roomname=roomname,addr=addr,ip_ranges=ip_ranges,error=error)


@app.route('/rooms/view_room_del/')
def view_room_del():
     roomid=request.args.get('roomid','')
     return render_template('room_del.html',roomid=roomid)

@app.route('/rooms/room_del/',methods=['post'])
def room_del():
     result=models.save_room_del(request.form.get('roomid',''))
     if result:
        return redirect('/rooms/')
     else:
        return render_template('view_room_del.html',roomid=roomid,error='Del error.')

@app.route('/rooms/search/')
def rooms_search():
     key=request.args.get('key','')
     result=models.search_room_key(key)
     #return str(result)
     return render_template('rooms.html',rooms=result,key=key)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=8089,debug=True)

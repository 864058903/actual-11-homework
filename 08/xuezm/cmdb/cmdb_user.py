#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import json
import hashlib  #加密模块

fields=('id','username' ,'age','telephone','password' ,'sex' ,'department','title','role','birthday','email')


@app.route('/')
def index():
    if not session:
        return redirect('/login/')
    if request.method =="GET":
        where="username='%s'"%session['username']
        result=selectone(fields,'users',where)
        print result
        return render_template('user_index.html',userinfo=result)


@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return  render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        where="username='%s'"%username
        result=selectone(fields,'users',where)
        if not result:
            return json.dumps({'code':400,'error':'用户不存在'})
        if result['password']==hashlib.md5(password).hexdigest():
            session['username']=result['username']
            session['role']=result['role']
            session['password']=result['password']
            return json.dumps({'code':200,'error':'登录成功'})
        else:
            return json.dumps({'code':400,'error':'密码错误'})


@app.route('/users/')
def users():
    if not session:
        return redirect('/login/')
    result=selectall(fields,'users')
    return  render_template('users.html',users=result)


@app.route('/users/add',methods=["GET","POST"])
def  useradd():
    if not session:
        return redirect('/login/')
    if  request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        where="username='%s'"%data['username']
        result=selectone(('username',),'users',where)
        if result:
            return json.dumps({'code':400,'error':'用户已经存在'})
        del data['repassword']
        data['password']=hashlib.md5(data['password']).hexdigest()
        adddata('users',data.keys(),data.values())
        return json.dumps({"code":200,"error":"add user success"})


@app.route('/users/delete')
def usersdelete():
    if not session:
        return redirect('/login/')
    id=request.args.get("id")
    where="id='%s'"%id
    deldata('users',where)
    return  redirect('/users/')


@app.route('/users/update',methods=["GET","POST"])
def usersupdate():
    if not session:
        return redirect('/login/')
    if request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        value = ["%s='%s'" % (k,v) for k,v in data.items()]
        print value
        where='id="%s"'%data['id']
        updata('users',value,where)
        return json.dumps({'code':200})
    else:
        id=request.args.get("id")
        where="id='%s'"%id
        result=selectone(fields,'users',where)
        print result
        #return  render_template('user_update.html',info=result)
        return  json.dumps(result)


@app.route('/users/uppass',methods=["GET","POST"])
def uppass():
    if not session:
        return redirect('/login/')
    if request.method=="GET":
        id=request.args.get("id")
        where="id='%s'"%id
        result=selectone(fields,'users',where)
        return  json.dumps(result)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data,session
        if hashlib.md5(data['adminpassword']).hexdigest()!=session['password']:
            #return  render_template('user_pass.html',info=data,error='')
            return  json.dumps({'code':400,'error':'admin password  error!'})
        where="id=%s"%data['id']
        value=["password='%s'"%hashlib.md5(data['password']).hexdigest()]
        updata('users',value,where)
        return json.dumps({'code':200})


@app.route("/logout/")
def logout():
    if session.get('username'):
        session.pop('role',None)
        session.pop('username', None)
    return redirect("/login/")

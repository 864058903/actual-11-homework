#coding=utf8
from  flask  import   Flask,render_template,request,redirect,session
from .   import  app
from db  import   *
import modules
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
            return render_template('login.html',error="username not exist")
        if result['password']==password:
            session['username']=result['username']
            session['role']=result['role']
            session['password']=result['password']
            return redirect('/')
        else:
            return render_template('login.html',error="password error")



@app.route('/users/')
def users():
    if not session:
        return redirect('/login/')
    result=modules.selectall(fields,'users')
    return  render_template('users.html',users=result)



@app.route('/users/add',methods=["GET","POST"])
def  useradd():
    if not session:
        return redirect('/login/')
    if request.method =="GET":
        return   render_template('user_create.html')
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        error=modules.verify_register_info(data)
        print error
        if not error:
            try:
                del data['repassword']
                print data
                modules.adddata('users',data.keys(),data.values())
            except:
                return render_template('user_create.html',error='add not success!')
            return  redirect('/users/')
        else:
            return render_template('user_create.html',error=error)


@app.route('/users/delete')
def usersdelete():
    if not session:
        return redirect('/login/')
    id=request.args.get("id")
    where="id='%s'"%id
    modules.deldata('users',where)
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
        modules.updata('users',value,where)
        return redirect("/users/")
    else:
        id=request.args.get("id")
        where="id='%s'"%id
        result=modules.selectone(fields,'users',where)
        print result
        return  render_template('user_update.html',info=result)

@app.route('/users/uppass',methods=["GET","POST"])
def uppass():
    if not session:
        return redirect('/login/')
    if request.method=="GET":
        id=request.args.get("id")
        where="id='%s'"%id
        result=modules.selectone(fields,'users',where)
        return  render_template('user_pass.html',info=result)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data,session
        if data['adminpassword']!=session['password']:
            return  render_template('user_pass.html',info=data,error='admin password  error!')
        if data['password']!=data['repassword']:
            return  render_template('user_pass.html',info=data,error="password !=repassword")
        where="id=%s"%data['id']
        value=["password='%s'"%data['password']]
        updata('users',value,where)
        return redirect('/users/')




@app.route("/logout/")
def logout():
    if session.get('username'):
        session.pop('role',None)
        session.pop('username', None)
    return redirect("/login")

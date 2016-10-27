#coding=utf8
from  flask  import   Flask,render_template,request,redirect
from .   import  app
from db  import   *
import modules

@app.route('/')
@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return  render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        print username,password
        result=modules.verify_user_pass(username,password)
        print result
        if result:
            return redirect('/users/')
        else:
            return render_template('login.html',error="username or password error")


@app.route('/users/')
def users():
    fields=('id','username','password','age')
    print "select  %s from  %s "%(",".join(fields),'users')
    result=modules.selectall(fields,'users')
    print result
    return  render_template('users.html',users=result)



@app.route('/users/add',methods=["GET","POST"])
def  useradd():
    if request.method =="GET":
        return   render_template('user_create.html')
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        error=modules.verify_register_info(data)
        print error
        if not error:
            try:
                modules.adddata('users',data.keys(),data.values())
            except:
                return render_template('user_create.html',error='add not success!')
            return  redirect('/users/')
        else:
            return render_template('user_create.html',error=error)


@app.route('/users/delete')
def usersdelete():
    id=request.args.get("id")
    where="id='%s'"%id
    modules.deldata('users',where)
    return  redirect('/users/')


@app.route('/users/update',methods=["GET","POST"])
def usersupdate():
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
        fields=('id','username','password','age')
        where="id='%s'"%id
        result=modules.selectone(fields,'users',where)
        print result
        return  render_template('user_update.html',info=result)
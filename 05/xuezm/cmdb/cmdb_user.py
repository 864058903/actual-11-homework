#coding=utf8
from  flask  import   Flask,render_template,request,redirect
from .   import  app
from rwfile  import  readfile,writefile,onedata

@app.route('/')
@app.route('/login/',methods=["GET","POST"])
def login():
    if request.method =="GET":
        return  render_template('login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')
        result=readfile()
        print result,username,password
        for i in result:
            if i.get('name')==username and  i.get('password')==password:
                print "登录成功!"
                return redirect('/users/')
        return render_template('login.html',error="username or password error")


@app.route('/users/add',methods=["GET","POST"])
def  useradd():
    if request.method =="GET":
        return   render_template('user_create.html')
    else:
        readresult=readfile()
        LEN=len(readresult)
        userinfo=request.form
        result={k:v[0] for k,v in dict(userinfo).items()}
        result['id']=LEN+1
        readresult.append(result)
        print readresult
        writefile(readresult)
        return redirect('/users/')





@app.route('/users/')
def users():
    result=readfile()
    return  render_template('users.html',users=result)


@app.route('/users/delete')
def usersdelete():
    id=request.args.get("id")
    result=readfile()
    #print result
    i=onedata(result,id)
    del  result[i]
    writefile(result)
    return  redirect('/users/')

@app.route('/users/update',methods=["GET","POST"])
def usersupdate():
    if request.method=="POST":
        info=request.form.get('password')
        id=request.form.get("id")
        print  id,info
        result=readfile()
        i=onedata(result,id)
        result[i]['password']=info
        writefile(result)
        return redirect("/users/")
    else:
        id=request.args.get("id")
        result=readfile()
        i=onedata(result,id)
        #print result[i],i,id
        return  render_template('user_update.html',info=result[i])
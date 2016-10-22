#encoding:utf-8
from flask import Flask
from flask import render_template
from flask import request,redirect
import models

app = Flask(__name__)

@app.route('/')
def index():
	 return render_template('index.html')

@app.route('/login/',methods=['post','get'])
def login():
    username=''
    password=''
    if request.method == 'POST':
        username = request.form.get('username','')
        password = request.form.get('password','')
    else:
	username = request.args.get('username','')
	password = request.args.get('password','')
    user = models.auth_user(username,password)
    if user:
       return redirect('/users/')
    else:
       return render_template('index.html',username=username,error='username or password error,or user was locked.')

@app.route('/users/')
def view_user():
    u_valid=request.args.get('u_valid')
    result=models.get_user()
    return render_template('users.html',users=result,u_valid=u_valid)

@app.route('/view_adduser/')
def view_adduser():
    return render_template('user_add.html')

@app.route('/add_users/',methods=['post','get'])
def add_user():
     new_user={}
     param = request.args if  request.method == 'GET' else request.form
     new_user['username']=param.get('username','').strip()
     new_user['password']=param.get('password','').strip()
     new_user['group']=param.get('group','').strip()
     new_user['tel']=param.get('tel','').strip()
     result=models.same_user(new_user.get('username'))
     if  result:
        return render_template('/user_add.html/',error='Same name erro.',username=new_user.get('username'),password=new_user.get('password'),group=new_user.get('group'),tel=new_user.get('tel'))
     else:
        models.add_user(new_user)
        return redirect('/users/')
        

@app.route('/view_usermodify/' )
def view_usermodify():
    result=models.same_user(request.args.get('username'),0)
    return render_template('/user_modify.html/',id=result.get('id'),username=result.get('username'),password=result.get('password'),group=result.get('group'),tel=result.get('tel'),status=result.get('status'))

@app.route('/user_modify/', methods=['post'])
def user_modify():
    new_user={}
    username=request.form.get('username')
    new_user['id']=int(request.form.get('id','').strip())
    new_user['username']=request.form.get('username','').strip()
    new_user['password']=request.form.get('password','').strip()
    new_user['group']=request.form.get('group','').strip()
    new_user['tel']=request.form.get('tel','').strip()
    new_user['status']=request.form.get('status','').strip()
     
    result=models.same_user(request.form.get('username'),int(request.form.get('id')))
    if result:
        return render_template('/user_modify.html/',error='Same name erro.',id=int(request.form.get('id')),username=username,password=request.form.get('password'),group=request.form.get('group'),tel=request.form.get('tel'),status=request.form.get('status'))
    else:
        models.modify_user(new_user)
        return redirect('/users/')   

@app.route('/view_userdel/')
def view_userdel():
    username=request.args.get('username')
    return render_template('user_del.html',username=username)

@app.route('/user_del/')
def user_del():
    username=request.args.get('username')
    if models.del_user(username):
       return redirect('/users/')

@app.route('/search/')
def search():
    str_key=request.args.get('txtkey')
    u_valid=request.args.get('u_valid')
    txtkey=request.args.get('txtkey')
    result=models.search_user(u_valid,str_key)
    return render_template('users.html',users=result,u_valid=u_valid,txtkey=txtkey)

@app.route('/logs/')
def logs():
    log_file='www_access_20140823.log'
    topn=request.args.get('topn',10)
    topn=int(topn) if str(topn).isdigit() else 10
    result=models.top_log(log_file,topn)
    return render_template('logs.html',logs=result)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8088,debug=True)

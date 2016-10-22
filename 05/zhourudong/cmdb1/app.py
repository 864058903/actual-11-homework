#conding:utf-8

from  flask import  Flask
from flask import render_template
from flask import request, redirect
import logs
import models
import userinfo
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs/')
def log():
    topn = request.args.get('topn',10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "www_access_20140823.log"
    result = models.get_topn(access_file_path,topn)
    return render_template('logs.html',logs=result)


@app.route('/login/',methods=['GET','POST'])
def login():
    username = ''
    password = ''
    if 'POST' == request.method:
        username = request.form.get('username','')
        password = request.form.get('password','')
    else:
        username = request.args.get('username','')
        password = request.args.get('password','')
    user = models.validate_login(username,password)
    if user:
        return redirect('/users/')
    else:
        return render_template('index.html',username=username,password=password,error='username or password error')
    return 'login'

@app.route('/users/')
def users():
    user_list = userinfo.get_user_info()
    return render_template('users.html',user_list=user_list)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2000,debug=True)
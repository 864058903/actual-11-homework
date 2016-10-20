#encoding: utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import models


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    username = ''
    password = ''
    if 'POST' == request.method:
        username = request.form.get('username', '')
        password = request.form.get('password', '')
    else:
        username = request.args.get('username', '')
        password = request.args.get('password', '')

    user = models.validate_login(username,password)
    if user:
        return redirect('/users/')
    else:
        return render_template('index.html',username=username,password=password,error='usernmae or password is error')

@app.route('/users/')
def users():
    users = models.get_users()
    return render_template('users.html',users=users)

@app.route('/user/create/')
def user_create():
    return render_template('user_create.html')

@app.route('/user/add/', methods=['post'])
def user_add():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    ok, error = models.validate_add_user(username,password)
    if ok:
        models.add_users(username,password)
        return redirect('/users/')
    else:
        return render_template('user_create.html',username=username,password=password,error=error)

@app.route('/user/delete/')
def user_delete():
    username = request.args.get('username', '')
    models.delete_user(username)
    return redirect('/users/')

@app.route('/user/modify/')
def modify_user():
    username = request.args.get('username', '')
    user = models.get_user(username)
    error = ''
    username = ''
    password = ''
    if user is None:
        error = 'username is not exists'
    else:
        username = user['name']
        password = user['password']
    return render_template('user_modify.html',username=username,password=password,error=error)

@app.route('/user/update/', methods=['post'])
def user_update():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    ok,error = models.validate_update_user(username,password)
    if ok:
        models.update_user(username,password)
        return redirect('/users/')
    else:
        return render_template('user_modify.html',username=username,password=password,error=error)

@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "/home/share/www_access_20140823.log"
    result = models.get_topn(access_file_path,topn)
    return render_template('logs.html',logs=result)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=10015,debug=True)
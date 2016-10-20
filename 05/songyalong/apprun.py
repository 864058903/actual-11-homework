# encoding:utf-8

from flask import Flask, render_template, request, redirect
import userOperation
import usersView
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['post', 'get'])
def login():
    username = ''
    password = ''
    if "POST" == request.method:
        username = request.form.get('username')
        password = request.form.get('password')
    users = userOperation.getUser()
    for user in users:
        if user.get('username') == username and user.get('password') == password:
            return redirect('/usersList/')
    return redirect('/')


@app.route('/usersList/')
def getUserList():
    users_list=usersView.getUsersList()
    return render_template('listUsers.html',users_list=users_list)
@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/writeUser/',methods=['post', 'get'])
def writeUser():
    if "POST" == request.method:
        if request.form.get('username')!='' and request.form.get('password')!='':
            username=request.form.get('username')
            password=request.form.get('password')
            userOperation.writeUser(username,password)
            print username
            print password
            return redirect('/')

    return '非法注册'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)

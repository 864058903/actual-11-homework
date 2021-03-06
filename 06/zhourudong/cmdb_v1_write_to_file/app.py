#encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')                     #设置命令行为utf-8

import os
from functools import wraps

from flask import Flask                             #从flask包导入Flask类
from flask import render_template                   #从flask包导入render_template函数
from flask import request                           #从flask包导入request对象
from flask import redirect                          #从flask包导入redirect函数
from flask import url_for
from flask import session
from flask import flash


import user                                         #导入user模块
import room
import loganalysis

app = Flask(__name__)

app.secret_key = 'oF\xd3I\x98\xe5\xb4\x1a\xfb\xc77\xe3\xcc,\xc2\xd2\x05\x8b\xa9\x9b\x01\xa0t\x0f\x04\x11\x19\xcd4\x96\x8d\x14'

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect('/')
        rt = func(*args, **kwargs)
        return rt

    return wrapper


'''打开用户登录页面
'''
@app.route('/')                                     #将url path=/的请求交由index函数处理
def index():
    return render_template('login.html')            #加载login.html模板，并返回页面内容


'''用户登录信息检查
'''
@app.route('/login/', methods=["POST"])             #将url path=/login/的post请求交由login函数处理
def login():
    username = request.form.get('username', '')     #接收用户提交的数据
    password = request.form.get('password', '')

    #需要验证用户名密码是否正确
    # print username, password
    if user.validate_login(username, password):
        session['user'] = {'username' : username}
        return redirect('/users/')                  #跳转到url /users/
    else:
        #登录失败
        return render_template('login.html', username=username, error=u'用户名或密码错误')


'''用户列表显示
'''
@app.route('/users/')                               #将url path=/users/的get请求交由users函数处理
def users():
    #获取所有用户的信息
    # print 'dddd----------',session.get('user')
    if session.get('user') is None:
        return redirect('/')

    _users = user.get_users()
    return render_template('users.html', users=_users, username=session.get('user').get('username'), msg=request.args.get('msg', ''))            #加载渲染users.html模板

'''跳转到新建用户信息输入的页面
'''
@app.route('/user/create/')                         #将url path=/user/create/的get请求交由create_user处理
@login_required
def create_user():
    return render_template('user_create.html')      #加载渲染user_create.html


'''存储新建用户的信息
'''
@app.route('/user/add/', methods=['POST'])          #将url path=/user/add的post请求交由add_user处理
@login_required
def add_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    #检查用户信息
    _is_ok, _error = user.validate_add_user(username, password, age)
    if _is_ok:
        user.add_user(username, password, age)      #检查ok，添加用户信息
        return redirect(url_for('users', msg='新建成功'))                  #跳转到用户列表url_for
    else:
        #跳转到用户新建页面，回显错误信息&用户信息
        return render_template('user_create.html', \
                                error=_error, username=username, \
                                password=password, age=age)


'''
打开用户信息修改页面
'''
@app.route('/user/modify/')                          #将url path=/user/modify/的歌特请求交由modify_user函数处理
@login_required
def modify_user():
    username = request.args.get('username', '')
    _user = user.get_user(username)
    _error = ''
    _username = ''
    _password = ''
    _age = ''
    if _user is None:
        _error = 'user infomation not exits.'
    else:
        _username = _user.get('username')
        _password = _user.get('password')
        _age = _user.get('age')
    # print _username,_password,_age
    return render_template('user_modify.html', error=_error, password=_password, age=_age, username=_username)

'''保存修改用户数据
'''
@app.route('/user/update/', methods=['POST'])           #将url path=/user/update/的post请求交由update_user函数处理
@login_required
def update_user():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', '')

    #检查用户信息
    _is_ok, _error = user.validate_update_user(username, password, age)
    if _is_ok:
        user.update_user(username, password, age)
        flash('修改用户信息成功')
        return redirect('/users/')
    else:
        return render_template('user_modify.html', error=_error, username=username, password=password, age=age)


@app.route('/user/delete/')
@login_required
def delete_user():
    username = request.args.get('username')
    user.delete_user(username)
    flash('删除用户信息成功')
    return redirect('/users/')


@app.route('/logs/')
@login_required
def logs():
    logfile = 'www_access_20140823.log'
    
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10

    rt_list = loganalysis.get_topn(logfile=logfile, topn=topn)
    return render_template('logs.html', rt_list=rt_list, title='topn log')

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    # print session
    return redirect('/')

# ====================================================================
'''
机房信息列表
'''
@app.route('/rooms/')
@login_required
def rooms():
    _rooms = room.get_rooms()
    return render_template('rooms.html',rooms=_rooms)

'''
跳转到机房输入页面
'''
@app.route('/room/create/')                         #将url path=/user/create/的get请求交由create_user处理
@login_required
def create_room():
    return render_template('room_create.html')      #加载渲染room_create.html


'''
存储新建机房信息
'''
@app.route('/room/add/', methods=['POST'])          #将url path=/user/add的post请求交由add_user处理
@login_required
def add_room():
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    iprange = request.form.get('iprange', '')

    #检查用户信息
    _is_ok, _error = room.validate_add_room(name, addr, iprange)  # is_ok 取到状态码 _error取到错误信息
    if _is_ok:
        room.add_room(name, addr, iprange)      #检查ok，添加机房信息
        return redirect(url_for('rooms', msg='新建成功'))                  #跳转到用户列表url_for
    else:
        #跳转到用户新建页面，回显错误信息&用户信息
        return render_template('room_create.html', \
                                error=_error, name=name, \
                                addr=addr, iprange=iprange)

'''
打开机房信息修改页面
'''
@app.route('/room/modify/')                          #将url path=/user/modify/的歌特请求交由modify_user函数处理
@login_required
def modify_room():
    name = request.args.get('name', '')

    _tmp_name = room.get_room(name)
    _name = ''
    _error = ''
    _addr = ''
    _iprange = ''
    if _tmp_name is None:
        _error = '用户信息不存在'
    else:
        _name = _tmp_name.get('name')
        _addr = _tmp_name.get('addr')
        _iprange = _tmp_name.get('iprange')

    return render_template('room_modify.html', error=_error, addr=_addr, iprange=_iprange, name=_name)


'''
保存修改机房数据
'''

@app.route('/room/update/', methods=['POST'])           #将url path=/user/update/的post请求交由update_user函数处理
@login_required
def update_room():
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    iprange = request.form.get('iprange', '')

    #检查用户信息
    print name,addr,iprange
    _is_ok, _error = room.validate_update_room(name=name, addr=addr, iprange=iprange)
    if _is_ok:
        room.update_room(name, addr, iprange)
        flash(u'修改用户信息成功')
        return redirect('/users/')
    else:
        return render_template('room_modify.html', error=_error, name=name, addr=addr, iprange=iprange)

'''
删除机房信息
'''
@app.route('/room/delete/')
@login_required
def delete_room():
    name = request.args.get('name')
    room.delete_room(name)
    flash('删除用户信息成功')
    return redirect('/users/')



if __name__ == '__main__':
    app.run( port=2000, debug=True)

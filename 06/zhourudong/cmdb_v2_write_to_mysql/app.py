#coding:utf8

from flask import Flask
from flask import render_template
import models
from flask import request
from flask import redirect
from flask import session
import os
app = Flask(__name__)
app.secret_key=os.urandom(32)
# 登入界面  输入用户名密码后提交到login
@app.route('/')
def index():
    return render_template('index.html')

# login 页面
@app.route('/login/', methods=['post', 'get'])
def login():
    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')

    user = models.validate_login(username, password)
    if user:
        # 如果验证用户成功直接跳转到机房列表
        session['user'] = { 'username': username }
        return redirect('/rooms/')
    # 否则再转回登入界面
    return render_template('index.html', username=username, password=password, error='username or password is error')

# 机房列表页面
@app.route('/rooms/')
def room_list():
    print session.get('user')
    if session.get('user') is None:
        return  redirect('/')
    rooms = models.get_rooms()
    return render_template('room.html', rooms=rooms)

# 添加机房
@app.route('/room/create/')
def room_create():
    return render_template('room_create.html')

# 保存机房信息
@app.route('/room/save/', methods=['POST'])
def room_save():
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    ip_ranges  = request.form.get('ip_ranges', 0)
    # 进入保存前对数据进行检查
    ok, error = models.validate_room_save(name, addr, ip_ranges)
    if ok:
        _ok, error=models.room_save(name, addr, ip_ranges)
    else:
        return render_template('room_create.html', name=name, addr=addr, ip_ranges=ip_ranges,error=error)
    if _ok:
        return redirect('/rooms/')
    return render_template('room_create.html', name=name, addr=addr, ip_ranges=ip_ranges,error=error)

'''
机房列表
取到数据渲染 提交到修改页面
'''
@app.route('/room/view/')
def room_view():
    room = models.get_room_by_name(request.args.get('name', 0))
    return render_template('room_view.html', id=room.get('id', ''), name=room.get('name', ''), addr=room.get('addr', ''),ip_ranges=room.get('ip_ranges',''))

'''
机房修改页面
'''
@app.route('/user/modify/', methods=['POST'])
def user_modify():
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    print name,addr,ip_ranges
    ok, error = models.validate_room_modify(name, addr, ip_ranges)
    if ok:
        models.room_modify(name, addr, ip_ranges)  # 修改机房合法性通过,则修改机房信息，且跳转到机房列表
        return redirect('/rooms/')
    else:
        return render_template('room_view.html', name=name, addr=addr, ip_ranges=ip_ranges, error=error)


'''
删除机房信息
'''
@app.route('/room/delete/')
def delete_room():
    name = request.args.get('name')
    models.delete_room(name)
    return redirect('/rooms/')

if __name__ == '__main__':
        app.run(debug=True)

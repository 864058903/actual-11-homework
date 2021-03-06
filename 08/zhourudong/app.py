#encoding: utf-8

# 从flask包导入Flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import json
import models
from flask import  session
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#创建Flask对象
app = Flask(__name__)
app.secret_key= os.urandom(32)

#/ ==> index........
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')

    user = models.validate_login(username, password)
    if user:
        session['user'] = {'username' : username}
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')

@app.route('/users/')
def user_list():
    if session.get('user') is None:
        return redirect('/')   # 如果用户session为空直接跳转到首页
    users = models.get_users()
    return render_template('user.html', users=users)


@app.route('/user/create/')
def user_create():
    return render_template('user_create.html')

@app.route('/user/save/', methods=['POST'])
def user_save():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return redirect('/users/')
    else:
        return render_template('user_create.html', username=username, age=age, error=error)

@app.route('/user/save/json/', methods=['POST'])
def user_save_json():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    # print request.form
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return json.dumps({'code': 200})

    else:
        return json.dumps({'code': 400, 'error': error})


@app.route('/user/view/')
def user_view():
    user = models.get_user_by_id(request.args.get('id', 0))
    # print user
    return render_template('user_view.html', id=user.get('id', ''), username=user.get('name', ''), age=user.get('age', ''))
'''
用户修改
'''
@app.route('/user/modify/', methods=['POST'])
def user_modify():
    uid = request.form.get('id', '')
    username = request.form.get('username', '')
    age = request.form.get('age', '')
    ok, error = models.validate_user_modify(uid, username, age)
    if ok:
        models.user_modify(uid, username, age)
        return redirect('/users/')
    else:
        return render_template('user_view.html', id=uid, username=username, age=age, error=error)
"""
删除用户
"""
@app.route('/user/delete/')
def delete_user():
    uid = request.args.get('id')
    models.delete_user(uid)
    return redirect('/users/')

'''
登出
'''

@app.route('/logout/')
def logout():
    return redirect('/')

# ---------------------------------------------------------------------------
# 机房管理
# ---------------------------------------------------------------------------


# 机房列表
@app.route('/machines/')
def get_machines():
    machines = models.get_machines()

    return render_template('machine.html',machines=machines)

'''
机房添加
'''
@app.route('/machine/create/')
def machine_create():
    return render_template('machine_create.html')

'''
机房保存
'''
@app.route('/machine/save/',methods=['POST'])
def machine_save():
    room_name = request.form.get('room_name','')
    addr = request.form.get('addr','')
    ip_ranges = request.form.get('ip_ranges','')

    ok, error = models.validate_machine_save(room_name,addr,ip_ranges)
    if ok:
        ok, error = models.machine_save(room_name,addr,ip_ranges)
        if ok:
            return redirect('/machines/')
        return render_template('machine_create.html', room_name=room_name, addr=addr, ip_ranges=ip_ranges, error=error)
    return render_template('machine_create.html', room_name=room_name, addr=addr, ip_ranges=ip_ranges, error=error)

'''
json格式修改
'''
@app.route('/machine/save/json/', methods=['POST'])
def machine_save_json():
    room_name = request.form.get('room_name','')
    addr = request.form.get('addr','')
    ip_ranges = request.form.get('ip_ranges','')

    ok, error = models.validate_machine_save(room_name,addr,ip_ranges)
    if ok:
        models.machine_save(room_name,addr,ip_ranges)
        return json.dumps({'code': 200})

    else:
        return json.dumps({'code': 400, 'error': error})

'''
'''
@app.route('/machine/view/')
def machine_view():
    machine = models.get_machine_by_id(request.args.get('id', 0))
    # print machine
    return render_template('machine_view.html', id=machine.get('id', ''), room_name=machine.get('room_name', ''), addr=machine.get('addr', ''),ip_ranges=machine.get('ip_ranges', ''))

'''
机房修改
'''
@app.route('/machine/modify/', methods=['POST'])
def machine_modify():
    id = request.form.get('id', '')
    room_name = request.form.get('room_name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_machine_modify(id,room_name,addr,ip_ranges)
    if ok:
        models.machine_modify(id,room_name,addr,ip_ranges)
        return redirect('/machines/')
    else:
        return render_template('machine_view.html', id=id, room_name=room_name, addr=addr,ip_ranges=ip_ranges, error=error)

"""
删除机房信息
"""
@app.route('/machine/delete/')
def delete_machine():
    id = request.args.get('id')
    models.delete_machine(id)
    return redirect('/machines/')



# ----------------------------
#  日志
# ----------------------------
@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "www_access_20140823.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

if __name__ == '__main__':
    # 启动app
    # print app.url_map
    app.run(host='127.0.0.1', port=5000, debug=True)

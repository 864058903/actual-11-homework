# coding=utf-8
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from flask import jsonify
from functools import wraps
from users import User
from idcs import Idcs
from cmdb import app


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user') is None:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper


@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name', '')
        password = request.form.get('password', '')
        _user = User.validate_login(name, password)
        if _user:
            session['user'] = _user
            return redirect(url_for('index'))
        return render_template('login.html', name=name, error='用户名或密码错误')
    return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/user/')
@login_required
def user():
    user_list = User.get_user_list()
    return render_template('user.html', users=user_list)


@app.route('/account/passwd/', methods=['GET', 'POST'])
@login_required
def change_password():
    error = False
    if request.method == 'POST':
        password_old = request.form.get('password_old')
        password_new = request.form.get('password_new')
        password_repeat_new = request.form.get('password_repeat_new')
        username = session['user']['name']
        ret, error = User.validate_password(username, password_old, password_new, password_repeat_new)
        if ret:
            User.change_password(username, password_repeat_new)
            return redirect(url_for('user'))
    return render_template('update_passwd.html', error=error) 


@app.route('/user/create/')
@login_required
def user_create():
    return render_template('user_create.html')


@app.route('/user/add/', methods=['POST'])
@login_required
def user_add():
    name = request.form.get('name', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    _user = User(id=None, name=name, password=password, phone=phone, email=email)
    ret, error = _user.validate_add()
    print(ret, error)
    if ret:
        _user.user_add()
    return jsonify({'status': ret, 'error': error})


@app.route('/user/modify/')
@login_required
def user_modify():
    uid = request.args.get('id', '')
    _user = User.get_user_id(uid)
    return render_template('user_modify.html', id=_user['id'], email=_user['email'], phone=_user['phone'])


@app.route('/user/change/', methods=['POST'])
@login_required
def user_change():
    uid = request.form.get('id', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    _user = User(id=uid, name=None, password=None, email=email, phone=phone)
    ret, error = _user.validate_change()
    print(ret, error)
    if ret:
        _user.user_change()
    return jsonify({'status': ret, 'error': error})


@app.route('/user/delete/')
@login_required
def user_delete():
    uid = request.args.get('id', '')
    User.user_delete(uid)
    return redirect(url_for('user'))


@app.route('/idcs/')
@login_required
def idcs():
    idcs_list = Idcs.get_idcs_list()
    return render_template('idcs.html', idcs=idcs_list)


@app.route('/idc/create/')
@login_required
def idcs_create():
    return render_template('idcs_create.html')


@app.route('/idc/add/', methods=['POST'])
@login_required
def idcs_add():
    name = request.form.get('name', '')
    address = request.form.get('address', '')
    ip = request.form.get('ip', '')
    _idc = Idcs(id=None, name=name, address=address, ip=ip)
    ret, error = _idc.validate_idcs_add()
    if ret:
        _idc.idcs_add()
    return jsonify({'status': ret, 'error': error})


@app.route('/idc/modify/')
@login_required
def idcs_modify():
    uid = request.args.get('id', '')
    _idc = Idcs.get_idc_id(uid)
    return render_template('idcs_modify.html', id=_idc['id'], name=_idc['name'], address=_idc['address'], ip=_idc['ip'])


@app.route('/idc/change/', methods=['POST'])
@login_required
def idcs_change():
    uid = request.form.get('id', '')
    name = request.form.get('name', '')
    address = request.form.get('address', '')
    ip = request.form.get('ip', '')
    _idc = Idcs(id=uid, name=name, address=address, ip=ip)
    ret, error = _idc.validate_idcs_change()
    if ret:
        _idc.idcs_change()
    return jsonify({'status': ret, 'error': error})


@app.route('/idc/delete/')
@login_required
def idcs_delete():
    uid = request.args.get('id', '')
    Idcs.idcs_delete(uid)
    return redirect(url_for('idcs'))

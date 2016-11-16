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
from assets import Asset
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


# 机房管理
@app.route('/idcs/')
@login_required
def idcs():
    return render_template('idcs.html')


@app.route('/idcs/list/')
@login_required
def idcs_list():
    idcs_list = Idcs.get_idcs_list()
    return jsonify({'data': idcs_list})


@app.route('/idcs/add/')
@login_required
def idcs_add():
    return render_template('idcs_create.html')


@app.route('/idcs/create/', methods=['POST'])
@login_required
def idcs_create():
    _form = request.form
    ret, error = Idcs.validate_idcs_create(_form)
    if ret:
        Idcs.idcs_add(_form)
    return jsonify({'error': error})


@app.route('/idcs/view/')
@login_required
def idcs_view():
    aid = request.args.get('id', 0, type=int)
    idcs = Idcs.get_idc_id(aid)
    return jsonify(idcs)


@app.route('/idcs/update/', methods=['POST'])
@login_required
def idcs_update():
    _form = request.form
    ret, error = Idcs.validate_idcs_change(_form)
    if ret:
        Idcs.idcs_update(_form)
    return jsonify({'error': error})


@app.route('/idcs/delete/')
@login_required
def idcs_delete():
    aid = request.args.get('id', 0, type=int)
    Idcs.idcs_delete(aid)
    return ''


# 资产管理
@app.route('/assets/')
@login_required
def asset_index():
    return render_template('asset.html')


@app.route('/asset/list/')
@login_required
def asset_list():
    assets_list = Asset.get_asset_name()
    return jsonify({'data': assets_list})


@app.route('/asset/add/')
@login_required
def asset_add():
    idcs_list = Idcs.get_idcs_list()
    return render_template('asset_create.html', idcs=idcs_list)


@app.route('/asset/create/', methods=['POST'])
@login_required
def asset_creat():
    _form = request.form
    ret, error = Asset.validate_asset_create(_form)
    if ret:
        Asset.asset_create(_form)
    return jsonify({'error': error})


@app.route('/asset/view/')
@login_required
def asset_view():
    aid = request.args.get('id', 0, type=int)
    assets = Asset.get_asset_id(aid)
    idcs = Idcs.get_idcs_list()
    return jsonify({'assets': assets, 'idcs': idcs})


@app.route('/asset/update/', methods=['POST'])
@login_required
def asset_update():
    _form = request.form
    ret, error = Asset.validate_asset_change(_form)
    if ret:
        Asset.asset_update(_form)
    return jsonify({'error': error})


@app.route('/asset/delete/')
@login_required
def asset_delete():
    aid = request.args.get('id', 0, type=int)
    Asset.asset_delete(aid)
    return ''

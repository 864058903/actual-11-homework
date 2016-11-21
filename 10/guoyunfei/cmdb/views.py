# coding=utf-8
#

from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from flask import jsonify
from functools import wraps
from .users import Users
from .idcs import Idcs
from .assets import Asset
import monitors
from . import app


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
        _user = Users.validate_login(name, password)
        if _user:
            session['user'] = _user
            return redirect(url_for('index'))
        return render_template('login.html', name=name, error=u'用户名或密码错误')
    return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/account/passwd/', methods=['GET', 'POST'])
@login_required
def change_password():
    error = False
    if request.method == 'POST':
        password_old = request.form.get('password_old')
        password_new = request.form.get('password_new')
        password_repeat_new = request.form.get('password_repeat_new')
        username = session['user']['name']
        ret, error = Users.validate_password(username, password_old, password_new, password_repeat_new)
        if ret:
            Users.change_password(username, password_repeat_new)
            return redirect(url_for('user'))
    return render_template('update_passwd.html', error=error)
	

# 用户管理
@app.route('/users/')
@login_required
def user():
    return render_template('user.html')
	

@app.route('/users/list/')
@login_required
def user_list():
    users_list = Users.get_user_list()
    return jsonify({'data': users_list})


@app.route('/users/create/', methods=['POST'])
@login_required
def user_create():
	_form = request.form
	print(_form)
	ret, error = Users.validate_user_create(_form)
	print(ret, error)
	if ret:
		Users.user_add(_form)
	return jsonify({'error': error})

	
@app.route('/users/view/')
@login_required
def user_view():
    aid = request.args.get('id', 0, type=int)
    user = Users.get_user_id(aid)
    return jsonify(user)


@app.route('/users/update/', methods=['POST'])
@login_required
def user_update():
    _form = request.form
    ret, error = Users.validate_user_change(_form)
    if ret:
        Users.user_update(_form)
    return jsonify({'error': error})


@app.route('/users/delete/')
@login_required
def user_delete():
    uid = request.args.get('id', '')
    Users.user_delete(uid)
    return ''


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


@app.route('/idcs/deletecheck/')
@login_required
def idcs_deletecheck():
    aid = request.args.get('id', 0, type=int)
    ret, error = Idcs.validate_idcs_delete(aid)
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
    idcs_list = Idcs.get_idcs_list()
    return render_template('asset.html', idcs=idcs_list)


@app.route('/asset/list/')
@login_required
def asset_list():
    assets_list = Asset.get_asset_name()
    return jsonify({'data': assets_list})


@app.route('/asset/create/', methods=['POST'])
@login_required
def asset_creat():
    _form = request.form
    print(_form)
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


# 监控主机
@app.route('/monitor/host/create/', methods=['POST'])
def monitor_create():
    _form = request.json
    values = monitors.monitor_host_create(_form)
    return jsonify({'code': 200, 'data': values, 'error': ''})


@app.route('/monitor/host/list/')
def monitor_host_list():
    uid = request.args.get('id', 0, type=int)
    asset = Asset.get_asset_id(uid)
    ip = asset.get('ip', '')
    result = monitors.monitor_host_list(ip)
    return jsonify({'code': 200, 'result': result})

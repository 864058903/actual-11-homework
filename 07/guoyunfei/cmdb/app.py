# coding=utf-8

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import session
from functools import wraps
import models

app = Flask(__name__)
app.secret_key = 'B?{\x93SDO\x8b\xb1\x1cYq\xb1\xac\x9c\x039\xb0\x8b\xc3e&uv%\xad\xae=\x8e\xfe`Z'


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
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        ret, error = models.validate_login(username, password)
        if ret:
            session['user'] = username
            return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/account/passwd/', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        password_old = request.form.get('password_old')
        password_new = request.form.get('password_new')
        password_repeat_new = request.form.get('password_repeat_new')
        username = session['user']
        ret, error = models.validate_password(username, password_old, password_new, password_repeat_new)
        if ret:
            models.change_password(username, password_repeat_new)
            return redirect(url_for('user'))
        else:
            return render_template('change_password.html', error=error, password_old=password_old, password_new=password_new, password_repeat_new=password_repeat_new)
    return render_template('change_password.html')


@app.route('/user/')
@login_required
def user():
    user_list = models.get_user_list()
    return render_template('user.html', users=user_list)


@app.route('/user/create/')
@login_required
def user_create():
    return render_template('user_create.html')


@app.route('/user/add/', methods=['POST'])
@login_required
def user_add():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')
    telephone = request.form.get('telephone', '')
    ret, error = models.validate_add(username, password, email, telephone)
    if ret:
        models.user_add(username, password, email, telephone)
        return redirect(url_for('user'))
    else:
        return render_template('user_create.html', username=username, password=password,
                               email=email, telephone=telephone, error=error)


@app.route('/user/modify/')
@login_required
def user_modify():
    user_list = models.get_user_list()
    return render_template('user_modify.html', users=user_list)


@app.route('/user/change/', methods=['POST'])
@login_required
def user_change():
    uid = request.form.get('id', '')
    users = models.get_user_id(uid)
    return render_template('user_change.html', id=uid, email=users['email'], telephone=users['telephone'])


@app.route('/user/save/', methods=['POST'])
@login_required
def user_save():
    uid = request.form.get('id', '')
    email = request.form.get('email', '')
    telephone = request.form.get('telephone', '')
    ret, error = models.validate_change(email, telephone)
    if ret:
        models.user_change(uid, email, telephone)
        return redirect(url_for('user'))
    else:
        return render_template('user_change.html', id=uid,
                               email=email, telephone=telephone, error=error)


@app.route('/user/delete/', methods=['GET', 'POST'])
@login_required
def user_delete():
    if request.method == 'POST':
        uid = request.form.get('id', '')
        models.user_delete(uid)
        return redirect(url_for('user'))
    user_list = models.get_user_list()
    return render_template('user_delete.html', users=user_list)


@app.route('/idcs/')
@login_required
def idcs():
    idcs_list = models.get_idcs_list()
    return render_template('idcs.html', idcs=idcs_list)


@app.route('/idcs/create/')
@login_required
def idcs_create():
    return render_template('idcs_create.html')


@app.route('/idcs/add/', methods=['POST'])
@login_required
def idcs_add():
    name = request.form.get('name', '')
    address = request.form.get('address', '')
    ips = request.form.get('ips', '')
    ret, error = models.validate_idcs_add(name, address, ips)
    if ret:
        models.idcs_add(name, address, ips)
        return redirect(url_for('idcs'))
    else:
        return render_template('idcs_create.html', name=name, address=address, ips=ips, error=error)


@app.route('/idcs/modify/')
@login_required
def idcs_modify():
    idcs_list = models.get_idcs_list()
    return render_template('idcs_modify.html', idcs=idcs_list)


@app.route('/idcs/change/', methods=['POST'])
@login_required
def idcs_change():
    uid = request.form.get('id', '')
    idcs = models.get_idcs_id(uid)
    return render_template('idcs_change.html', id=uid, name=idcs['name'], address=idcs['address'], ips=idcs['ips'])


@app.route('/idcs/save/', methods=['POST'])
@login_required
def idcs_save():
    uid = request.form.get('id', '')
    name = request.form.get('name', '')
    address = request.form.get('address', '')
    ips = request.form.get('ips', '') 
    ret, error = models.validate_idcs_modify(uid, name, address, ips)
    if ret:
        models.idcs_change(uid, name, address, ips)
        return redirect(url_for('idcs'))
    else:
        return render_template('idcs_change.html', id=uid, name=name, address=address, ips=ips, error=error)


@app.route('/idcs/delete/', methods=['GET', 'POST'])
@login_required
def idcs_delete():
    if request.method == 'POST':
        uid = request.form.get('id', '')
        models.idcs_delete(uid)
        return redirect(url_for('idcs'))
    idcs_list = models.get_idcs_list()
    return render_template('idcs_delete.html', idcs=idcs_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

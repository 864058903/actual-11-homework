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


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/check_login/', methods=['GET', 'POST'])
def check_login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        ret, error = models.validate_login(username, password)
        if ret:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('new_login.html', error=error, username=username)
    return redirect(url_for('login'))


@app.route('/change/password/')
@login_required
def change_password():
    username = session.get('user')
    return render_template('change_password.html', username=username)


@app.route('/user/')
@login_required
def user():
    user_list = models.get_user_list()
    print(user_list)
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
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
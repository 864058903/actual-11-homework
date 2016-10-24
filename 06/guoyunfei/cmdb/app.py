# coding=utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import models

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('login.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if 'POST' == request.method:
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        status = models.validate_login(username, password)
        if status:
            return redirect(url_for('index'))
        return render_template('login.html', username=username, password=password, error='username or password is error')
    return render_template('login.html')


@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "access.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

'''用户管理
'''


@app.route('/user/')
def user():
    users = models.get_users()
    return render_template('user.html', users=users)


@app.route('/user/create/')
def user_create():
    return render_template('user_create.html')


@app.route('/user/save/', methods=['POST'])
def user_save():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        age = request.form.get('age', '')
        state, error = models.validate_user(username=username, password=password, age=age)
        if state:
            models.user_add(username, password, age)
            return redirect(url_for('user'))
        else:
            return render_template('user_create.html', username=username,
                                   password=password, age=age, error=error)


@app.route('/user/modify/')
def user_modify():
    uid = request.args.get('id', '')
    users = models.get_by_id(uid)
    return render_template('user_modify.html', id=users['id'],  age=users['age'])


@app.route('/user/change/', methods=['POST'])
def user_change():
    if request.method == 'POST':
        uid = request.form.get('id', '')
        age = request.form.get('age', '')
        state, error = models.validate_user(age=age)
        if state:
            models.user_update(uid, age)
            return redirect(url_for('user'))
        else:
            return render_template('user_modify.html', id=uid, age=age, error=error)


@app.route('/modify/password/')
def modify_password():
    uid = request.args.get('id', '')
    return render_template('modify_password.html', id=uid)


@app.route('/change/password/', methods=['POST'])
def change_password():
    if request.method == 'POST':
        uid = request.form.get('id', '')
        old_password = request.form.get('old_password', '')
        new1_password = request.form.get('new1_password', '')
        new2_password = request.form.get('new2_password', '')
        state, error = models.validate_password(uid, old_password, new1_password, new2_password)
        if state:
            models.change_passwd(uid, new2_password)
            return redirect(url_for('user'))
        else:
            return render_template('modify_password.html', id=uid, old_password=old_password,
                                   new1_password=new1_password, new2_password=new2_password, error=error)


@app.route('/user/delete/')
def user_delete():
    uid = request.args.get('id', '')
    models.user_delete(uid)
    return redirect('/user/')


''' 机房管理
'''


@app.route('/machine/')
def machine():
    machines = models.get_machines()
    return render_template('machine.html', machines=machines)


@app.route('/machine/create/')
def machine_create():
    return render_template('machine_create.html')


@app.route('/machine/save/', methods=['POST'])
def machine_save():
    if request.method == 'POST':
        name = request.form.get('name', '')
        addr = request.form.get('addr', '')
        ips = request.form.get('ips', '')
        state, error = models.validate_machine(name=name, addr=addr, ips=ips)
        if state:
            models.machine_add(name, addr, ips)
            return redirect(url_for('machine'))
        else:
            return render_template('machine_create.html', name=name,
                                   addr=addr, ips=ips, error=error)


@app.route('/machine/modify/')
def machine_modify():
    uid = request.args.get('id', '')
    machines = models.get_machine_id(uid)
    return render_template('machine_modify.html', id=machines['id'], name=machines['name'],
                           addr=machines['addr'], ips=machines['ips'])


@app.route('/machine/change/', methods=['POST'])
def machine_change():
    if request.method == 'POST':
        uid = request.form.get('id', '')
        name = request.form.get('name', '')
        addr = request.form.get('addr', '')
        ips = request.form.get('ips', '')
        state, error = models.validate_machine(name, addr, ips)
        if state:
            models.machine_update(uid, name, addr, ips)
            return redirect(url_for('machine'))
        else:
            return render_template('machine_modify.html', id=uid, name=name,
                                   addr=addr, ips=ips, error=error)


@app.route('/machine/delete/')
def machine_delete():
    uid = request.args.get('id', '')
    models.machine_delete(uid)
    return redirect(url_for('machine'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

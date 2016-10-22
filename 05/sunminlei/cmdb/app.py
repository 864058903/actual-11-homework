#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, flash, url_for
import models
import os
app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=["post", "get"])
def login():
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
    else:
        username = request.args.get('username', '')
        password = request.args.get('password', '')
    print username, password
    user = models.validate_login(username, password)
    if user:
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')


@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = '/home/sun/PycharmProjects/s11/day4/access_120101.log'
    result = models.gettopn(access_file_path, topn)
    return render_template('log.html', logs=result)


@app.route('/users/')
def users():
    users = models.getusers()
    return render_template('users.html', users=users)


@app.route('/users/add/')
def users_add():
    return render_template('user_create.html')


@app.route('/users/create/', methods=["post"])
def users_create():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    error = models.validate_create_user(username, password)
    if error:
        flash(error)
        return render_template('user_create.html', username=username, password=password)
    else:
        flash('create user:%s succeed' % username)
        return redirect(url_for('users'))


@app.route('/users/delete/')
def users_delete():
    uid = request.args.get('id', '')
    username = models.delete_user(uid)
    flash('delete user:%s succeed' % username)
    return redirect(url_for('users'))


@app.route('/users/modify/')
def users_modify():
    uid = request.args.get('id', '')
    username = models.getuser(uid).get("username")
    password = models.getuser(uid).get("password")
    return render_template('user_modify.html', username=username, password=password, id=uid)


@app.route('/users/update/', methods=["post"])
def users_update():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    uid = request.form.get('id', '')
    error = models.validate_update_user(username, password, uid)
    if error:
        flash(error)
        return render_template('user_modify.html', username=username, password=password, id=uid)
    else:
        flash('update user:%s succeed' % username)
        return redirect(url_for('users'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)


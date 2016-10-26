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
    param = request.form if request.method == 'POST' else request.form
    username = param.get('username', '')
    password = param.get('password', '')
    user = models.validate_login(username, password)
    if user:
        return redirect('/user/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')


@app.route('/user/')
def user():
    users = models.get_users()
    return render_template('users.html', users=users)


@app.route('/user/create/')
def user_create():
    return render_template('user_create.html')


@app.route('/user/save/', methods=["post"])
def user_save():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        rt = models.user_save(username, password, age)
        if rt:
            flash('create user:%s succeed' % username)
            return redirect(url_for('user'))
    else:
        flash(error)
        return render_template('user_create.html', username=username)


@app.route('/user/delete/')
def user_delete():
    uid = request.args.get('id', '')
    username = models.get_user_by_id(uid).get('name')
    rt = models.user_delete(uid)
    if rt:
        flash('delete user:%s succeed' % username)
        return redirect(url_for('user'))


@app.route('/user/view/')
def user_view():
    user = models.get_user_by_id(request.args.get('id', 0))
    return render_template('user_view.html', id=user.get('id', 0), \
                           username=user.get('name', ''), age=user.get('age', 0))


@app.route('/user/modify/', methods=["post"])
def user_modify():
    username = request.form.get('username', '')
    age = request.form.get('age', 0)
    uid = request.form.get('id', 0)
    ok, error = models.validate_user_modify(username, age, uid)
    if ok:
        rt = models.user_modify(username, age, uid)
        if rt == 0:
            flash('modify user:%s not changed' % username)
        elif rt > 0:
            flash('modify user:%s succeed' % username)
        return redirect(url_for('user'))
    else:
        flash(error)
        return render_template('user_view.html', username=username, age=age, id=uid)


@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = '/home/sun/PycharmProjects/s11/day4/access_120101.log'
    result = models.gettopn(access_file_path, topn)
    return render_template('log.html', logs=result)


@app.route('/room/')
def room():
    rooms = models.get_rooms()
    return render_template('rooms.html', rooms=rooms)


@app.route('/room/create/')
def room_create():
    return render_template('room_create.html')


@app.route('/room/save/', methods=["post"])
def room_save():
    roomname = request.form.get('roomname', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_room_save(roomname, addr, ip_ranges)
    if ok:
        rt = models.room_save(roomname, addr, ip_ranges)
        if rt:
            flash('create room:%s succeed' % roomname)
            return redirect(url_for('room'))
    else:
        flash(error)
        return render_template('room_create.html', roomname=roomname, addr=addr, \
                               ip_ranges=ip_ranges)


@app.route('/room/delete/')
def room_delete():
    rid = request.args.get('id', 0)
    roomname = models.get_room_by_id(rid).get('roomname')
    rt = models.room_delete(rid)
    if rt:
        flash('delete room:%s succeed' % roomname)
        return redirect(url_for('room'))


@app.route('/room/view/')
def room_view():
    room = models.get_room_by_id(request.args.get('id', 0))
    return render_template('room_view.html', id=room.get('rid', 0), \
                           roomname=room.get('roomname', ''), addr=room.get('addr', ''),\
                           ip_ranges=room.get('ip_ranges', ''))


@app.route('/room/modify/', methods=["post"])
def room_modify():
    rid = request.form.get('id', 0)
    roomname = request.form.get('roomname', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_room_modify(rid, roomname, addr, ip_ranges)
    if ok:
        rt = models.room_modify(rid, roomname, addr, ip_ranges)
        if rt == 0:
            flash('modify user:%s not changed' % roomname)
        elif rt > 0:
            flash('modify user:%s succeed' % roomname)
        return redirect(url_for('room'))
    else:
        flash(error)
        return render_template('room_view.html', id=rid, roomname=roomname, \
                               addr=addr, ip_ranges=ip_ranges)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)


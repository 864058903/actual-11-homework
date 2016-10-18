#coding: utf-8
#

from flask import Flask, render_template, redirect, request
from cmdb import app
from .utils import validate_login, validate_password, get_read_users, add_users, validate_user, delete_users, get_id_users, modify_password


@app.route('/')
@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        ret, error = validate_login(username, password)
        if ret:
            return redirect('/users/')
        return render_template('login.html', username=username, password=password, error=error)
    return render_template('login.html')


@app.route('/users/')
def users():
    users = get_read_users()
    return render_template('users.html', users=users)


@app.route('/users/create/')
def users_create():
    return render_template('users_create.html')


@app.route('/users/add/', methods=['POST'])
def users_add():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        ret, error = validate_user(username, password)
        if ret:
            add_users(username, password)
            return redirect('/users/')
        return render_template('users_create.html', username=username, password=password, error=error)
        

@app.route('/users/update/')
def users_update():
    id = request.args.get('id', '')
    users = get_id_users(id)
    if users:
        return render_template('users_update.html', 
                                id=users['id'], username=users['username'], password=users['password'])
    return redirect('/users/')


@app.route('/users/modify/', methods=['POST'])
def users_modify():
    if request.method == 'POST':
        id = request.form.get('id', '')
        password = request.form.get('password', '')
        ret, error = validate_password(password)
        if ret:
            modify_password(id, password)
            return redirect('/users/')
        return render_template('users_update.html', id=id, password=password, error=error)


@app.route('/users/delete/')
def users_delete():
    id = request.args.get('id', '')
    delete_users(id)    
    return redirect('/users/')


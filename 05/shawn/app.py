#!/usr/bin/env python
#encoding: utf-8

#从flask包导入Flask对象
from flask import Flask
#导入模板，需要新建一个templates文件夹
from flask import render_template
#用来获取get请求的参数
from flask import request
#导入跳转模块
from flask import redirect
#从modules导入需要的数据与模块
import models


#创建一个Flask对象
app = Flask(__name__)

#设置路由映射
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/", methods = ['GET', 'POST'])
def login():
    username = ""
    passwd = ""
    if 'POST' == request.method:
        username =  request.form.get("username", '')
        passwd = request.form.get("passwd", '')
    else:
        username = request.args.get("username", "")
        passwd = request.args.get("passwd", "")

    user = models.validate_login(username, passwd)
    if user:
        return redirect("/users/")
    else:
        return render_template("index.html", username = username, passwd = passwd, error = "username or passwd is error")

@app.route("/users/")
def show_users():
    return render_template("users.html", users = models.get_users())

@app.route("/users/add/")
def add_users():
    return render_template("user_create.html")

@app.route("/users/save/", methods = ['POST'])
def save_users():
    name = request.form.get("username", "")
    password = request.form.get("passwd", "")
    ok, error = models.validate_user_save(name, password)
    if ok:
        models.user_save(name, password)
        return redirect("/users/")
    else:
        return render_template("user_create.html", name = name, passwd = password, info = error)

@app.route("/users/view/")
def users_view():
    user_id = request.args.get("id")
    name = models.get_user(user_id).get('name')
    passwd = models.get_user(user_id).get('password')
    return render_template("user_edit.html", user_id = user_id, name = name , passwd = passwd)

@app.route("/users/edit/", methods = ['POST'])
def edit_users():
    user_id = request.form.get("id")
    name = request.form.get("username")
    passwd = request.form.get("passwd")
    ok, error = models.validate_user_save(name, passwd)
    if ok:
        info = models.user_update(user_id, name , passwd)
        return redirect('/users/')
    else:
        info = error
        return render_template('user_edit.html', user_id = user_id, name = name , passwd = passwd, info = info)

@app.route("/users/remove/")
def user_remove():
    user_id = request.args.get("id", "")
    result = models.user_delete(user_id)
    if result:
        return redirect('/users/')
    else:
        return render_template("users.html", info = "something wrong here.")


@app.route("/logs/")
def show_logs():
    topn = request.args.get("topn", 10)
    topn = int(topn) if str(topn).isdigit() else 10
    content = models.log_dict("apache.log",topn)
    return render_template("logs.html", content=content)


if __name__ == "__main__":
    #指定绑定到所有的ip，设置端口号为8686
    app.run(host="0.0.0.0", port=8687, debug=True)

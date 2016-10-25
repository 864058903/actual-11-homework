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

@app.route("/users/add/", methods = ["GET", "POST"])
def add_users():
    if 'GET' == request.method:
        return render_template("user_create.html")
    else:
        username =  request.form.get("username", '')
        passwd = request.form.get("passwd", '')
        info = models.create_users(username, passwd)
        return render_template("user_create.html", info = info)

@app.route("/logs/")
def show_logs():
    topn = request.args.get("topn", 10)
    topn = int(topn) if str(topn).isdigit() else 10
    content = models.log_dict("apache.log",topn)
    return render_template("logs.html", content=content)


if __name__ == "__main__":
    #指定绑定到所有的ip，设置端口号为8687
    app.run(host="0.0.0.0", port=8687, debug=True)

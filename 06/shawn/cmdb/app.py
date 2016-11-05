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
    params = request.form if 'POST' == request.method else request.args
    username = params.get("username", "")
    passwd = params.get("passwd", "")
    user = models.validate_login(username, passwd)
    if user:
        return redirect("/users/")
    else:
        return render_template("index.html", username = username, passwd = passwd, error = "username or passwd is error")

@app.route("/machine/")
def show_machine():
    machine_list = models.get_machine_list()
    return render_template("machine_list.html", machines = machine_list)

@app.route("/machine/add/")
def machine_add():
    return render_template("machine_add.html")

@app.route("/machine/save/", methods = ['POST'])
def machine_save():
    name = request.form.get("machine_name")
    addr = request.form.get("machine_addr")
    ip_ranges = request.form.get("ip_ranges")
    ok,error = models.validate_machine(name, addr, ip_ranges)
    if ok:
        models.save_machine(name, addr, ip_ranges)
        return redirect("/machine/")
    else:
        return render_template("machine_add.html", name = name, addr = addr, ip_ranges = ip_ranges, info = error)

@app.route("/machine/view/")
def machine_view():
    machine_id = request.args.get("id")
    name = models.get_machine_info(machine_id).get('name')
    addr = models.get_machine_info(machine_id).get('addr')
    ip_ranges = models.get_machine_info(machine_id).get('ip_ranges')
    return render_template("machine_edit.html", name = name, addr = addr, ip_ranges = ip_ranges, machine_id = machine_id)


@app.route("/machine/edit/", methods = ['POST'])
def machine_edit():
    machine_id = request.form.get("machine_id")
    name = request.form.get("machine_name")
    addr = request.form.get("machine_addr")
    ip_ranges = request.form.get("ip_ranges")
    ok, error = models.validate_machine_edit(name, addr, ip_ranges, machine_id)
    if ok:
        models.update_machine(name, addr, ip_ranges, machine_id)
        return redirect("/machine/")
    else:
        return render_template("machine_edit.html", machine_id = machine_id, name = name, addr = addr, ip_ranges = ip_ranges, info = error)


@app.route("/machine/remove/", methods = ['GET'])
def machine_remove():
    machine_id = request.args.get("id")
    models.remove_machine(machine_id)
    return redirect("/machine/")

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
    age = request.form.get("age", "")
    ok, error = models.validate_user_save(name, password,age)
    if ok:
        models.user_save(name, password, age)
        return redirect("/users/")
    else:
        return render_template("user_create.html", name = name, passwd = password, age = age, info = error)

@app.route("/users/view/")
def users_view():
    user_id = request.args.get("id")
    name = models.get_user(user_id).get('name')
    age = models.get_user(user_id).get('age')
    return render_template("user_edit.html", user_id = user_id, name = name, age = age)

@app.route("/users/edit/", methods = ['POST'])
def edit_users():
    user_id = request.form.get("id")
    name = request.form.get("username")
    age = request.form.get("age")
    ok, error = models.validate_edit_save(user_id,name, age)
    if ok:
        info = models.user_update(user_id, name , age)
        return redirect('/users/')
    else:
        info = error
        return render_template('user_edit.html', user_id = user_id, name = name , age = age, info = info)

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
    content = models.log_dict("/home/shawn/Desktop/apache.log",topn)
    return render_template("logs.html", content=content)


if __name__ == "__main__":
    #指定绑定到所有的ip，设置端口号为8686
    app.run(host="0.0.0.0", port=8687, debug=True)

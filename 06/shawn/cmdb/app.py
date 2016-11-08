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
#导入session
from flask import session
#从modules导入需要的数据与模块
import models


#创建一个Flask对象
app = Flask(__name__)
app.secret_key = "\xea\tR\xe8#\xa0\xbd\x95\xf44h\xce\xa4\xd6\xdf\x98I\xcb\xea\x15\xce\x83\x7f|k\r\xa6\xafWIY\x0f"

#设置路由映射
@app.route("/")
def index():
    if session.get("username") is None:
        return render_template("index.html")
    else:
        return redirect("/users/")

@app.route("/login/", methods = ['GET', 'POST'])
def login():
    params = request.form if 'POST' == request.method else request.args
    username = params.get("username", "")
    passwd = params.get("passwd", "")
    user = models.validate_login(username, passwd)
    if user:
        session['username'] = username
        return redirect("/users/")
    else:
        return render_template("index.html", username = username, passwd = passwd, error = "username or passwd is error")

@app.route("/machine/")
def show_machine():
    if session.get("username") is None:
        return redirect("/login/")
    machine_list = models.get_machine_list()
    return render_template("machine_list.html", machines = machine_list)

@app.route("/machine/add/")
def machine_add():
    if session.get("username") is None:
        return redirect("/login/")
    return render_template("machine_add.html")

@app.route("/machine/save/", methods = ['POST'])
def machine_save():
    if session.get("username") is None:
        return redirect("/login/")
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
    if session.get("username") is None:
        return redirect("/login/")
    machine_id = request.args.get("id")
    name = models.get_machine_info(machine_id).get('name')
    addr = models.get_machine_info(machine_id).get('addr')
    ip_ranges = models.get_machine_info(machine_id).get('ip_ranges')
    return render_template("machine_edit.html", name = name, addr = addr, ip_ranges = ip_ranges, machine_id = machine_id)


@app.route("/machine/edit/", methods = ['POST'])
def machine_edit():
    if session.get("username") is None:
        return redirect("/login/")
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
    if session.get("username") is None:
        return redirect("/login/")
    machine_id = request.args.get("id")
    models.remove_machine(machine_id)
    return redirect("/machine/")

@app.route("/users/")
def show_users():
    if session.get("username") is None:
        return redirect("/login/")
    return render_template("users.html", users = models.get_users(), username =session.get("username"))

@app.route("/users/add/")
def add_users():
    if session.get("username") is None:
        return redirect("/login/")
    return render_template("user_create.html", username =session.get("username"))

@app.route("/users/save/", methods = ['POST'])
def save_users():
    if session.get("username") is None:
        return redirect("/login/")
    name = request.form.get("username", "")
    password = request.form.get("passwd", "")
    age = request.form.get("age", "")
    department = request.form.get("department", "")
    inro = request.form.get("inro", "")
    hobby_list = request.form.getlist("hobby")
    hobby = ",".join(hobby_list)
    ok, error = models.validate_user_save(name, password,age)
    if ok:
        models.user_save(name, password, age, department, inro, hobby)
        return redirect("/users/")
    else:
        return render_template("user_create.html", name = name, passwd = password, \
        age = age, department = department, inro = inro, hobby = hobby , info = error)

@app.route("/users/view/")
def users_view():
    if session.get("username") is None:
        return redirect("/login/")
    user_id = request.args.get("id")
    name = models.get_user(user_id).get('name')
    age = models.get_user(user_id).get('age')
    department = models.get_user(user_id).get("department")
    inro = models.get_user(user_id).get("inro")
    hobby_list = models.get_user(user_id).get("hobby")
    hobby = (hobby_list).split(",")
    return render_template("user_edit.html", user_id = user_id, name = name, age = age, \
    hobby = hobby_list, department = department, inro = inro, username =session.get("username"))

@app.route("/users/edit/", methods = ['POST'])
def edit_users():
    if session.get("username") is None:
        return redirect("/login/")
    user_id = request.form.get("id")
    name = request.form.get("username")
    age = request.form.get("age")
    department = request.form.get("department")
    inro = request.form.get("inro")
    hobby_list = request.form.getlist("hobby")
    hobby = ",".join(hobby_list)

    ok, error = models.validate_edit_save(user_id,name,age)
    if ok:
        info = models.user_update(user_id, name , age, department, inro, hobby)
        return redirect('/users/')
    else:
        info = error
        return render_template('user_edit.html', user_id = user_id, name = name , age = age, \
        info = info, inro = inro, hobby = hobby_list, username =session.get("username"))

@app.route("/users/remove/")
def user_remove():
    if session.get("username") is None:
        return redirect("/login/")
    user_id = request.args.get("id", "")
    result = models.user_delete(user_id)
    if result:
        return redirect('/users/')
    else:
        return render_template("users.html", info = "something wrong here.", username =session.get("username"))

@app.route("/logs/")
def show_logs():
    if session.get("username") is None:
        return redirect("/login/")
    topn = request.args.get("topn", 10)
    topn = int(topn) if str(topn).isdigit() else 10
    content = models.log_dict("/home/shawn/Desktop/apache.log",topn)
    return render_template("logs.html", content=content, username =session.get("username"))

@app.route('/logout/')
def logout():
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
    #指定绑定到所有的ip，设置端口号为8686
    app.run(host="0.0.0.0", port=8687, debug=True)

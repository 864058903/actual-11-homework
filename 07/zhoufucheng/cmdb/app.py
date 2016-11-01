#encoding: utf-8

# 从flask包导入Flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import models

#创建Flask对象
app = Flask(__name__)

app.secret_key = '\x0f\x7f\xd7\xa6\x1f\xcc\xbe\\\xc0WII\x8f\xe7\xb6\x0b^\xfa_?\x98\x03\x17S\x9c\x95z\xd2\xfbo1\xb9'

#/ ==> index........
@app.route('/')
def index():
    if session.get('user'): return redirect('/users/')
    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    username = ''
    password = ''
    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')
    
    user = models.validate_login(username, password)
    print user
    if user:
        session['user'] = user
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')

@app.route('/users/')
def user_list():
    if session.get('user') is None:
        return redirect('/')
    users = models.get_users()
    return render_template('user.html', users=users)

@app.route('/user/create/')
def user_create():
    if session.get('user') is None:
        return redirect('/')
    return render_template('user_create.html')

@app.route('/user/save/', methods=['POST'])
def user_save():
    if session.get('user') is None:
        return redirect('/')
    sex = request.form.get('sex', '')
    department = request.form.get('department', '')
    birthday = request.form.get('birthday', '')
    hobby = ' '.join(request.form.getlist('hobby'))
    email = request.form.get('email', '')
    detail = request.form.get('detail', '')
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username,password,age,department,email,hobby,birthday,sex,detail)
    if ok:
        models.user_save(username,password,age,department,email,hobby,birthday,sex,detail)
        return redirect('/users/')
    else:
        return render_template('user_create.html',username=username,age=age,error=error)

@app.route('/user/view/')
def user_view():
    if session.get('user') is None:
        return redirect('/')
    user = models.get_user_by_id(request.args.get('id', 0))
    return render_template('user_view.html',username=user.get('name', ''),age=user.get('age', ''),id=user.get('id', ''),department=user.get('department', ''),email=user.get('email', ''),hobby=user.get('hobby', ''),detail=user.get('detail', ''))

@app.route('/user/modify/', methods=['POST'])
def user_modify():
    if session.get('user') is None:
        return redirect('/')
    uid = request.form.get('id', '')
    username = request.form.get('username', '')
    age = request.form.get('age', '')
    department = request.form.get('department', '')
    hobby = ' '.join(request.form.getlist('hobby'))
    email = request.form.get('email', '')
    detail = request.form.get('detail', '')
    ok, error = models.validate_user_modify(uid,username,age,department,hobby,email,detail)
    if ok:
        models.user_modify(uid,username,age,department,hobby,email,detail)
        return redirect('/users/')
    else:
        return render_template('user_view.html',id=uid,username=username,age=age,department=department,hobby=hobby,email=email,detail=detail,error=error)

@app.route('/user/delete/')
def user_delete():
    if session.get('user') is None:
        return redirect('/')
    uid = request.args.get('id', '')
    models.user_delete(uid)
    return redirect('/users/')

@app.route('/idcs/')
def idc_list():
    idcs = models.get_idcs()
    return render_template('idc.html', idcs=idcs)

@app.route('/idc/create/')
def idc_create():
    return render_template('idc_create.html')

@app.route('/idc/save/', methods=['POST'])
def idc_save():
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok, error = models.validate_idc_save(name,addr,ip_ranges)
    if ok:
        models.idc_save(name,addr,ip_ranges)
        return redirect('/idcs/')
    else:
        return render_template('idc_create.html',name=name,addr=addr,ip_ranges=ip_ranges,error=error)

@app.route('/idc/view/')
def idc_view():
    machine = models.get_idc_id(request.args.get('id', ''))
    return render_template('idc_view.html',id=machine.get('id', ''),name=machine.get('name', ''),addr=machine.get('addr', ''),ip_ranges=machine.get('ip_ranges', ''))

@app.route('/idc/modify/',methods=['POST'])
def idc_modify():
    _id = request.form.get('id', '')
    name = request.form.get('name', '')
    addr = request.form.get('addr', '')
    ip_ranges = request.form.get('ip_ranges', '')
    ok,error = models.validate_idc_modify(_id,name,addr,ip_ranges)
    if ok:
        models.idc_modify(_id,name,addr,ip_ranges)
        return redirect('/idcs/')
    else:
        return render_template('idc_view.html',name=name,addr=addr,ip_ranges=ip_ranges,error=error)

@app.route('/idc/delete/')
def idc_delete():
    id = request.args.get('id', '')
    models.idc_delete(id)
    return redirect('/idcs/')

@app.route('/log/')
def log():
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "/home/share/www_access_20140823.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')

@app.route('/test/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    # 启动app
    print app.url_map
    app.run(host='0.0.0.0', port=10015, debug=True)

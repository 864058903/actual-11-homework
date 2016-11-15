#encoding: utf-8
import json
# 从flask包导入Flask对象
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import models

#创建Flask对象
app = Flask(__name__)
app.secret_key = 'F\xbb\xfa<\xf3h\xcaL\xbd\xcb~s\xbf\xe2;P\x025\x83\xa8\x05\x12.NM@<w\x0c*\xd2?'

#/ ==> index........
@app.route('/')
def index():
    if session.get('user'): return redirect('/users/')

    return render_template('index.html')

@app.route('/login/', methods=['post', 'get'])
def login():
    if session.get('user'): return redirect('/users/')
    
    params = request.form if 'POST' == request.method else request.args
    username = params.get('username', '')
    password = params.get('password', '')
    
    user = models.validate_login(username, password)
    if user:
        session['user'] = user
        return redirect('/users/')
    else:
        return render_template('index.html', username=username, password=password, error='username or password is error')

@app.route('/users/')
def user_list():
    if session.get('user') is None: return redirect('/')

    users = models.get_users()
    return render_template('user.html', users=users)


@app.route('/user/create/')
def user_create():
    if session.get('user') is None: return redirect('/')

    return render_template('user_create.html')

@app.route('/user/save/', methods=['POST'])
def user_save():
    if session.get('user') is None: return redirect('/')

    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return redirect('/users/')
    else:
        return render_template('user_create.html', username=username, age=age, error=error)

@app.route('/user/save/json/', methods=['POST'])
def user_save_json():
    if session.get('user') is None: return redirect('/')

    username = request.form.get('username', '')
    password = request.form.get('password', '')
    age = request.form.get('age', 0)
    ok, error = models.validate_user_save(username, password, age)
    if ok:
        models.user_save(username, password, age)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})
    


@app.route('/user/view/')
def user_view():
    if session.get('user') is None: return redirect('/')

    user = models.get_user_by_id(request.args.get('id', 0))

    return render_template('user_view.html',id=user.get('id', ''),
                                            username=user.get('name', ''),
                                            department=user.get('department', '2'),
                                            hobby=user.get('hobby', ['basketball', 'pingpong']),
                                            sex=user.get('sex', '1'),
                                            )

@app.route('/user/modify/', methods=['POST'])
def user_modify():
    if session.get('user') is None: return redirect('/')

    uid = request.form.get('id', '')
    username = request.form.get('username', '')
    age = request.form.get('age', '')
    ok, error = models.validate_user_modify(uid, username, age)
    if ok:
        models.user_modify(uid, username, age)
        return redirect('/users/')
    else:
        return render_template('user_view.html', id=uid, username=username, age=age, error=error)


@app.route('/user/delete/')
def user_delete():
    models.user_delete(request.args.get('id', 0))
    return redirect('/users/')

@app.route('/machine_rooms/')
def machine_rooms():
    machine_rooms = models.get_machine_rooms()
    return render_template('machine_room.html', machine_rooms=machine_rooms);

@app.route('/log/')
def log():
    if session.get('user') is None: return redirect('/')
    topn = request.args.get('topn', 10)
    topn = int(topn) if str(topn).isdigit() else 10
    access_file_path = "/home/kk/www_access_20140823.log"
    result = models.get_topn(access_file_path, topn)
    return render_template('log.html', logs=result)

@app.route('/assets/')
def asset_index():
    if session.get('user') is None: return redirect('/')
    return render_template('asset.html')

@app.route('/assets/list/')
def assets_list():
    if session.get('user') is None: return redirect('/')
    assets = models.get_assets()
    return json.dumps({'data': assets})

@app.route('/assert/view/')
def asset_view():
    _id = request.args.get('id', 0)
    asset = models.get_asset_by_id(_id)
    return json.dumps(asset)

@app.route('/asset/update/', methods=['POST'])
def asset_update():
    return json.dumps({'error':''})

@app.route('/asset/save/', methods=['POST'])
def asset_save():
    if session.get('user') is None: return redirect('/')

    sn = request.form.get('sn', '')
    ip = request.form.get('ip', '')
    os = request.form.get('os', '')
    hostname = request.form.get('hostname', '')
    cpu = request.form.get('cpu', '')
    ram = request.form.get('ram', '')
    disk = request.form.get('disk', '')
    machine_room_id = request.form.get('machine_room_id', '')
    vendor = request.form.get('vendor', '')
    model = request.form.get('model', '')
    time_on_shelves = request.form.get('time_on_shelves', '')
    over_guaranteed_date = request.form.get('over_guaranteed_date', '')
    buiness = request.form.get('buiness', '')
    admin = request.form.get('admin', '')
    status = request.form.get('status', '')

    ok, error = models.validate_asset_save(sn,ip,os,hostname,cpu,ram,disk,machine_room_id,vendor,model,time_on_shelves,over_guaranteed_date,buiness,admin,status)
    if ok:
        models.asset_save(sn,ip,os,hostname,cpu,ram,disk,machine_room_id,vendor,model,time_on_shelves,over_guaranteed_date,buiness,admin,status)
        return json.dumps({'code' : 200})
    else:
        return json.dumps({'code' : 400, 'error' : error})

@app.route('/asset/delete/')
def asset_delete():
    if session.get('user') is None: return redirect('/')
    if models.asset_delete(request.args.get('id', 0)):
        return json.dumps({'code':200})
    
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
    
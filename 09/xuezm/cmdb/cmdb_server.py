#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import json
import  datetime

roomfields=('id','name')
fields=('id','sn','hostname','os','ip','machine_room_id','vendor','model','ram','cpu','disk','time_on_shelves','over_guaranteed_date','buiness','admin','status')
@app.route('/assets/')
def assets():
    if not session.get('username',None):
        return redirect("/login")
    return  render_template('idc/assets.html')

@app.route('/assets/list/')
def assets_list():
    if not session.get('username',None):
        return redirect("/login")

    #获取到ＩＤＣ机房的信息ｉｄ，ｎａｍｅ,拼接为dict {id:name,id1:name1}
    room=selectall(roomfields,'machine_room')
    roomresult = dict((ii['id'],ii['name'])  for ii in room)

    result=selectall(fields,'asset')
    for i in result:
        if i['machine_room_id'] in roomresult:
            i['machine_room_id']=roomresult[i['machine_room_id']]

    return  json.dumps({'data':result})

@app.route('/asset/add',methods=["GET","POST"])
def  assetadd():
    if not session.get('username',None):
        return redirect("/login")
    if request.method =="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        adddata('asset',data.keys(),data.values())
        return  json.dumps({'code':200})


@app.route('/asset/delete')
def assetdelete():
    if not session.get('username',None):
        return redirect("/login")
    id=request.args.get("id")
    where="id='%s'"%id
    print where
    deldata('asset',where)
    return  redirect('/assets/')


@app.route('/asset/update',methods=["GET","POST"])
def assetupdate():
    if not session.get('username',None):
        return redirect("/login")
    if request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        value = ["%s='%s'" % (k,v) for k,v in data.items()]
        where='id="%s"'%data['id']
        print "update  %s   set   %s where  %s "%('asset',",".join(value),where)
        updata('asset',value,where)
        #return redirect("/assets/")
        return json.dumps({'code':200})
    else:
        id=request.args.get("id")
        where="id='%s'"%id
        result=selectone(fields,'asset',where)
        roomresult=selectall(roomfields,'machine_room')
        result['room_name']=roomresult
        print result
        return json.dumps(result)

#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import json

@app.route('/rooms/')
def idcs():
    if not session.get('username',None):
        return redirect("/login")
    fields=('id','name','addr','ip_ranges')
    #print "select  %s from  %s "%(",".join(fields),'machine_room')
    result=selectall(fields,'machine_room')
    #print result
    return  render_template('idc/rooms.html',idcs=result)



@app.route('/room/add',methods=["GET","POST"])
def  idcadd():
    if not session.get('username',None):
        return redirect("/login")
    if request.method =="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        adddata('machine_room',data.keys(),data.values())
        return  json.dumps({'code':200})


@app.route('/room/delete')
def idcdelete():
    if not session.get('username',None):
        return redirect("/login")
    id=request.args.get("id")
    where="id='%s'"%id
    deldata('machine_room',where)
    return  redirect('/rooms/')


@app.route('/room/update',methods=["GET","POST"])
def idcupdate():
    if not session.get('username',None):
        return redirect("/login")
    if request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        value = ["%s='%s'" % (k,v) for k,v in data.items()]
        where='id="%s"'%data['id']
        #print "update  %s   set   %s where  %s "%('machine_room',",".join(value),where)
        updata('machine_room',value,where)
        #return redirect("/rooms/")
        return json.dumps({'code':200})
    else:
        id=request.args.get("id")
        fields=('id','name','addr','ip_ranges')
        where="id='%s'"%id
        result=selectone(fields,'machine_room',where)
        #print result
        #return  render_template('idc/idc_update.html',info=result)
        return json.dumps(result)

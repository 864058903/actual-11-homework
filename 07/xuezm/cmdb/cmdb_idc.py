#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import modules


@app.route('/idcs/')
def idcs():
    if not session.get('username',None):
        return redirect("/login")
    fields=('id','name','addr','ip_ranges')
    print "select  %s from  %s "%(",".join(fields),'machine_room')
    result=selectall(fields,'machine_room')
    print result
    return  render_template('idc/idcs.html',idcs=result)



@app.route('/idc/add',methods=["GET","POST"])
def  idcadd():
    if not session.get('username',None):
        return redirect("/login")
    if request.method =="GET":
        return   render_template('idc/idc_create.html')
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        error=modules.verify_idc_info(data)
        if not error:
            try:
                adddata('machine_room',data.keys(),data.values())
            except:
                return render_template('idc/idc_create.html',error='add not success!')
            return  redirect('/idcs/')
        else:
            return render_template('idc/idc_create.html',error=error)


@app.route('/idc/delete')
def idcdelete():
    if not session.get('username',None):
        return redirect("/login")
    id=request.args.get("id")
    where="id='%s'"%id
    deldata('machine_room',where)
    return  redirect('/idcs/')


@app.route('/idc/update',methods=["GET","POST"])
def idcupdate():
    if not session.get('username',None):
        return redirect("/login")
    if request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        value = ["%s='%s'" % (k,v) for k,v in data.items()]
        where='id="%s"'%data['id']
        print "update  %s   set   %s where  %s "%('machine_room',",".join(value),where)
        updata('machine_room',value,where)
        return redirect("/idcs/")
    else:
        id=request.args.get("id")
        fields=('id','name','addr','ip_ranges')
        where="id='%s'"%id
        result=selectone(fields,'machine_room',where)
        print result
        return  render_template('idc/idc_update.html',info=result)
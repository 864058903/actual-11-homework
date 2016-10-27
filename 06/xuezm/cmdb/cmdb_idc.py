#coding=utf8
from  flask  import   Flask,render_template,request,redirect
from .   import  app
from db  import   *
import modules


@app.route('/idcs/')
def idcs():
    fields=('id','name','addr','ip_ranges')
    print "select  %s from  %s "%(",".join(fields),'machine_room')
    result=modules.selectall(fields,'machine_room')
    print result
    return  render_template('idc/idcs.html',users=result)



@app.route('/idc/add',methods=["GET","POST"])
def  idcadd():
    if request.method =="GET":
        return   render_template('idc/idc_create.html')
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        error=modules.verify_idc_info(data)
        if not error:
            try:
                modules.adddata('machine_room',data.keys(),data.values())
            except:
                return render_template('idc/idc_create.html',error='add not success!')
            return  redirect('/idcs/')
        else:
            return render_template('idc/idc_create.html',error=error)







@app.route('/idc/delete')
def idcdelete():
    id=request.args.get("id")
    where="id='%s'"%id
    modules.deldata('machine_room',where)
    return  redirect('/idcs/')


@app.route('/idc/update',methods=["GET","POST"])
def idcupdate():
    if request.method=="POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        value = ["%s='%s'" % (k,v) for k,v in data.items()]
        print value
        where='id="%s"'%data['id']
        modules.updata('machine_room',value,where)
        return redirect("/idcs/")
    else:
        id=request.args.get("id")
        fields=('id','name','addr','ip_ranges')
        where="id='%s'"%id
        result=modules.selectone(fields,'machine_room',where)
        print result
        return  render_template('idc/idc_update.html',info=result)
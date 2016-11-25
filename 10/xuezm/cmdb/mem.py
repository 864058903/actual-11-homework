#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import json
import  datetime


@app.route('/mem/',methods=['GET','POST'])
def  mem():
    return  render_template('monitor/mem.html')

@app.route('/mem/map',methods=['GET','POST'])
def  mem_map():
    result=selectall(['ip','mem'],'monitor_host')

    print result
    return json.dumps({'code':200})

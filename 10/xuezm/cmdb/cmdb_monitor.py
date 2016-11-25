#coding=utf8
from  flask  import   render_template,request,redirect,session
from .   import  app
from db  import   *
import json
import  datetime

fields=('cpu','mem','disk','m_time')
assetfields=('ip',)

#将agent数据写入到数据库
@app.route('/monitor/host/create',methods=["POST"])
def monitor_host_create():
    data=request.form.to_dict()
    data['r_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    adddata('monitor_host',data.keys(),data.values())
    return  json.dumps({'code':200,'result':''})

@app.route('/monitor/host/get')
def  monitor_host_get():
    id=request.args.get('id')
    where="id='%s'"%id
    data=selectone(assetfields,'asset',where)
    #print "ip _______ip {}".format(data)
    ip=data.get('ip')
    print ip
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    where='where ip="{}"  and r_time >="{}" order by m_time asc'.format(ip,start_time)
    print where
    data=whereselectall(fields,'monitor_host',where)

    # print data
    # [{'mem': 6.0, 'disk': 9.3, 'cpu': 27.3, 'm_time': datetime.datetime(2016, 11, 20, 16, 6, 53)},
    # {'mem': 6.0, 'disk': 9.3, 'cpu': 0.1, 'm_time': datetime.datetime(2016, 11, 20, 16, 7, 53)},
    # {'mem': 6.0, 'disk': 9.3, 'cpu': 0.1, 'm_time': datetime.datetime(2016, 11, 20, 16, 8, 53)},

    categoy_list=[ (line['m_time'].strftime('%H:%M')) for  line  in  data ]
    cpu_list=[ line['cpu'] for  line  in  data ]
    mem_list=[ line['mem'] for  line  in  data ]
    disk_list=[line[ 'disk'] for  line  in  data ]

    result={
      'ip':ip,
      'categories' : categoy_list,
      'series' : [
          {'name': 'CPU','data': cpu_list},
          {'name': u'内存','data': mem_list},
          {'name': u'磁盘','data': disk_list}
      ]
    }
    #拼接为如下类似字符串
    # result={
    #   'categories':['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    #   'series' : [
    #         {'name': 'CPU','data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]},
    #         {'name': u'内存','data': [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]},
    #         {'name': u'磁盘','data': [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]}
    #   ]}
    print result
    return  json.dumps({'code':200,'data':result})



@app.route('/mem/')
def mem():
    result=selectall(['ip','mem','m_time'],'monitor_host')
    ip_list=list(set([i['ip']for  i in  result]))
    return  render_template('monitor/mem.html',ip_list=ip_list)

@app.route('/mem/map')
def mem_map():
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    where='where  r_time >="{}" order by m_time asc'.format(start_time)
    result=whereselectall(['ip','mem','m_time'],'monitor_host',where)
    ip_list=list(set([i['ip']for  i in  result]))
    categoy_list, mem_list,data,RESULT = [], [],{},[]
    for  i in  ip_list:
        for ii in result:
            if ii['ip']==i:
                categoy_list.append(ii['m_time'].strftime('%H:%M'))
                mem_list.append(ii['mem'])
        data['ip']=i
        data['categories']=categoy_list
        data['series']=[{'name':'mem','data':mem_list}]
        RESULT.append(data)
        categoy_list, mem_list,data = [], [],{}
    print RESULT
    return json.dumps({'code':200,'data':RESULT})




@app.route('/cpu/')
def cpu():
    result=selectall(['ip','mem','m_time'],'monitor_host')
    ip_list=list(set([i['ip']for  i in  result]))
    return  render_template('monitor/cpu.html',ip_list=ip_list)


@app.route('/cpu/map')
def cpu_map():
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    where='where  r_time >="{}" order by m_time asc'.format(start_time)
    result=whereselectall(['ip','cpu','m_time'],'monitor_host',where)
    ip_list=list(set([i['ip']for  i in  result]))
    categoy_list, cpu_list,data,RESULT = [], [],{},[]
    for  i in  ip_list:
        for ii in result:
            if ii['ip']==i:
                categoy_list.append(ii['m_time'].strftime('%H:%M'))
                cpu_list.append(ii['cpu'])
        data['ip']=i
        data['categories']=categoy_list
        data['series']=[{'name':'cpu','data':cpu_list}]
        RESULT.append(data)
        categoy_list, cpu_list,data = [], [],{}
    return json.dumps({'code':200,'data':RESULT})


@app.route('/disk/')
def disk():
    result=selectall(['ip','mem','m_time'],'monitor_host')
    ip_list=list(set([i['ip']for  i in  result]))
    return  render_template('monitor/disk.html',ip_list=ip_list)

@app.route('/disk/map')
def disk_map():
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    where='where  r_time >="{}" order by m_time asc'.format(start_time)
    result=whereselectall(['ip','disk','m_time'],'monitor_host',where)
    ip_list=list(set([i['ip']for  i in  result]))
    categoy_list, disk_list,data,RESULT = [], [],{},[]
    for  i in  ip_list:
        for ii in result:
            if ii['ip']==i:
                categoy_list.append(ii['m_time'].strftime('%H:%M'))
                disk_list.append(ii['disk'])
        data['ip']=i
        data['categories']=categoy_list
        data['series']=[{'name':'disk','data':disk_list}]
        RESULT.append(data)
        categoy_list, disk_list,data = [], [],{}
    return json.dumps({'code':200,'data':RESULT})

#将agent数据写入到数据库
@app.route('/monitor/network/create',methods=["POST"])
def monitor_network_create():
    data=request.form.to_dict()
    adddata('network',data.keys(),data.values())
    return  json.dumps({'code':200,'result':''})

@app.route('/network/')
def network():
    result=selectall(['ip',],'network')
    ip_list=list(set([i['ip']for  i in  result]))
    return  render_template('monitor/network.html',ip_list=ip_list)

@app.route('/network/map')
def network_map():
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    where='where  m_time >="{}" order by m_time asc'.format(start_time)
    result=whereselectall(['ip','input','output','m_time'],'network',where)

    ip_list=list(set([i['ip']for  i in  result]))
    categoy_list, input_list,output_list,data,RESULT = [], [],[],{},[]
    for  i in  ip_list:
        for ii in result:
            if ii['ip']==i:
                categoy_list.append(ii['m_time'].strftime('%H:%M'))
                input_list.append(ii['input'])
                output_list.append(ii['output'])
        data['ip']=i
        data['categories']=categoy_list
        data['series']=[{'name':'INPUT','data':input_list},{'name':'OUTPUT','data':output_list}]
        RESULT.append(data)
        categoy_list, input_list,output_list,data = [], [],[],{}
    print RESULT
    return json.dumps({'code':200,'data':RESULT})
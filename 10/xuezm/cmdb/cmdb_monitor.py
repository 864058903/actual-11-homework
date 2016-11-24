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



@app.route('/zhaoyong/',methods=['GET'])
def zhaoyong():
    return  render_template('monitor/mem.html')

@app.route('/zhaoyong/map')
def zhaoyong_map():
        result=selectall(['logtime','module_name','availability'],'check_result')
        DATE=[]
        for i in result:
            if  i['logtime'].strftime('%Y-%m-%d') not  in DATE:
                DATE.append(i['logtime'].strftime('%Y-%m-%d'))
        m_name=list(set([i['module_name'] for  i in  result]))
        LL=[]
        L=[]
        z={}
        for  i in m_name:
            for  ii in result:
                if i==ii['module_name']:
                    L.append(ii['availability'])
                    z['name']=i
                    z['data']=L
            LL.append(z)
            L=[]
            z={}

        result={'categories':DATE,'series':LL}
        print result
        return json.dumps({"code":200,'data':result})

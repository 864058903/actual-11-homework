# coding=utf-8

from datetime import datetime, timedelta
from utils import MysqlConnection


def monitor_host_create(form):
    sql = 'insert into monitor_host(ip, mem, cpu, disk, m_time, r_time) values(%s, %s, %s, %s, %s, %s)'
    values = []
    for key in ['ip', 'mem', 'cpu', 'disk', 'm_time']:
        values.append(form.get(key, ''))
    values.append(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    MysqlConnection.execute_sql(sql, values, False)
    return values


def monitor_host_list(ip):
    start_time = (datetime.now() - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    sql = 'select m_time,cpu,mem,disk from monitor_host where ip=%s and r_time >=%s order by m_time asc'
    rt_cnt, rt_list = MysqlConnection.execute_sql(sql, (ip, start_time), True)
    cate_list, cpu_list, mem_list, disk_list = [], [], [], []
    for line in rt_list:
        cate_list.append(line[0].strftime('%H:%M'))
        cpu_list.append(line[1])
        mem_list.append(line[2])
        disk_list.append(line[3])
    return {
        'categories': cate_list,
        'series': [{
            'name': 'CPU',
            'data': cpu_list
        }, {
            'name': u'内存',
            'data': mem_list
        }, {
            'name': u'磁盘',
            'data': disk_list
        }]
    }

# coding=utf-8

import psutil
from datetime import datetime
import time
import json
import requests

INTERVAL = 10
URL = 'http://192.168.3.50:9000/monitor/host/create/'


def get_host_ip():
    nics = psutil.net_if_addrs()['eth0']
    for nic in nics:
        if nic.family == 2:
            return nic.address


def monitor():
    usage = {}
    ip = get_host_ip()
    usage['ip'] = ip
    while True:
        usage['disk'] = psutil.disk_usage('/').percent
        usage['cpu'] = psutil.cpu_percent()
        usage['mem'] = psutil.virtual_memory().percent
        usage['m_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ret = requests.post(url=URL, data=json.dumps(usage), headers={'content-type': 'application/json'})
        if ret.ok:
            print(ret.json())
        else:
            print('error')
        time.sleep(INTERVAL)


if __name__ == '__main__':
    monitor()

#!/encoding:utf-8

import psutil
import time
from datetime import datetime
import requests
INTERVAL=10
URL='http://localhost:8089/monitor/host/create/'
def get_ip():
   addr='0.0.0.0'
   for ip in psutil.net_if_addrs().get('eth0'):
        if ip.address.find('.') != -1:
           addr=ip.address
           break
   return addr 




def monitor():
   while True:
       params={}
       params['ip']=get_ip()
       params['disk']=psutil.disk_usage('/').percent
       params['cpu']=psutil.cpu_percent()
       params['mem']=psutil.virtual_memory().percent
       params['m_time']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       response=requests.post(URL,data=params)
       if response.ok:
            print response.json()
       else: 
            return 'error'
       time.sleep(INTERVAL)


if __name__ == '__main__':
     monitor()

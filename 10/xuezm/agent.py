#coding=utf8
import psutil
import time
import datetime,requests

SLEEPTIME=60
URL='http://139.198.9.83:8080/monitor/host/create'
def addr():
    nics=psutil.net_if_addrs().get('eth0')
    for i in nics:
        if i.address.find(".") != -1:
            addr=i.address
            break
    return  addr


def  monistor():
    while True:
        data={}
        data['ip']=addr()
        data['disk']=psutil.disk_usage('/').percent
        data['cpu']=psutil.cpu_percent()
        data['mem']=psutil.virtual_memory().percent
        data['m_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print data

        result=requests.post(URL,data=data)
        if result.ok:
            print result.content,result.status_code,result.url
        else:
            print "error"

        time.sleep(SLEEPTIME)


# 函数获取各网卡发送、接收字节数
def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数

    return key_info, recv, sent

# 函数计算每秒速率
def get_rate(func):
    key_info, old_recv, old_sent = func()  # 上一秒收集的数据
    time.sleep(1)
    key_info, now_recv, now_sent = func()  # 当前所收集的数据

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024) # 每秒发送速率

    return key_info, net_in, net_out


while 1:
    try:
         key_info, net_in, net_out = get_rate(get_key)

         for key in key_info:
             print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (key, net_in.get(key), net_out.get(key)))
    except KeyboardInterrupt:
        exit()

# End


if __name__ =="__main__":
    monistor()


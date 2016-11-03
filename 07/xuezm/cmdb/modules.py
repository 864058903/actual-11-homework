#__author__ = 'xuezm'
from db  import  *


def verify_register_info(data):
    if not data['username']:
        return "username  not  null!"
    elif not data['password']:
        return "password  not  null!"
    elif not data['repassword']:
        return "repassword  not  null!"
    elif data['password']!= data['repassword']:
        return "password !=  repassword  "
    elif not   data['age']:
        return "age  not  null!"
    elif not   data['telephone']:
        return "telephone  not  null!"
    elif not   data['email']:
        return "email  not  null!"
    elif len(data['username'])<5 or len(data['username'])>20:
        return ' character 5 <username  <20 '
    elif len(data['password'])<5 :
        return ' character 5 < password '
    elif int(data['age']) >100:
        return "age  too long!"

    else:
        return ''


def verify_idc_info(data):
    if not data['name']:
        return "name  not  null!"
    elif not data['addr']:
        return "addr  not  null!"
    elif not   data['ip_ranges']:
        return "ip_ranges  not  null!"
    elif len(data['name'])<2 or len(data['name'])>20:
        return ' character 2 <username  <20 '
    else:
        return ''



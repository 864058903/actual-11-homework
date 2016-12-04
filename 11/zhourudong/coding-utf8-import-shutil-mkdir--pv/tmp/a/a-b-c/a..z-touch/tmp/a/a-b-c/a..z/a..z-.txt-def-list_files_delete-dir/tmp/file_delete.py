#coding:utf8

import shutil

'''
创建测试文件
mkdir -pv  /tmp/a/{a,b,c}/{a..z}
touch /tmp/a/{a,b,c}/{a..z}/{a..z}.txt
'''

def list_files_delete(dir='/tmp/a'):
    shutil.rmtree(dir)
    return 'del file ok'




if __name__ == '__main__':
    print list_files_delete()	

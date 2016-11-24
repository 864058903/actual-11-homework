#coding:utf-8
from cmdb import  app
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#print app.url_map
print app.url_map
if  __name__   == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

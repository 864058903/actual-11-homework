#coding:utf-8
from cmdb import  app

#print app.url_map

if  __name__   == "__main__":
    app.run(host='127.0.0.1',port=8080,debug=True)

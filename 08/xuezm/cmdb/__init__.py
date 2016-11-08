#coding=utf8
from flask import Flask

app = Flask(__name__)
app.secret_key = "f7c7cf9f1aaa32733a57b7654d905d5e"

import  cmdb_user
import  cmdb_idc


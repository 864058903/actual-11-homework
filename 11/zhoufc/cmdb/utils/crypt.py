#encoding: utf-8

import hashlib

def md5_str(str):
    md5 = hashlib.md5()
    md5.update(str)
    return md5.hexdigest()
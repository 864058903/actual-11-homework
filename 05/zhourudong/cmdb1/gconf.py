#coding:utf-8
import json

# 用户信息保存位置
USER_DB_PATH="user.json"



#################
# debug
if __name__ == "__main__":
    def get_users():
        fh = open(USER_DB_PATH,'r')
        users = json.loads(fh.read())
        fh.close()
        return users

    a = get_users()
    for v in a:
        print v


# def validate_login(username,password):
#     users = get_users()
#     for user in users:
#         if user.get('name') == username and user.get('password') == password:
#             return user
#     return None
#
#
# a = validate_login('kk',123456)
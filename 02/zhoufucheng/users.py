#encoding: utf-8

_list = []

_users = raw_input('please input your user info(user1:id,user2:id):')

user_list = _users.split(',')

for i in user_list:

    _user = i.split(':')[0]
    _id = i.split(':')[1]
    _info = (_user,_id)
    _list.append(_info)

print _list

'''
功能ok
'''

#coding:utf8

import json
import gconf

"""
获取机房信息列表
"""
def get_rooms():
    with open(gconf.ROOM_FILE,'rb') as f:
        rooms_info = f.read()
        f.close()
        return json.loads(rooms_info)

"""
添加机房信息
"""
def add_room(name, addr, iprange):
    _room = {'name' : name, 'addr' : addr, 'iprange' : iprange}
    _rooms = get_rooms()
    _rooms.append(_room)
    save_rooms(_rooms)

'''保存机房信息数据到文件中
'''
def save_rooms(rooms):
    fhandler = open(gconf.ROOM_FILE, 'wb')
    fhandler.write(json.dumps(rooms))
    fhandler.close()

'''
获取机房信息
'''
def get_room(name):
    _rooms = get_rooms()
    for _room in _rooms:
        if _room.get('name') == name:
            return _room

    return None





'''检查新建机房信息信息
返回值: True/False, 错误信息
'''
def validate_add_room(name, addr, iprange):
    if name.strip() == '' or addr.strip() == '' or iprange.strip == '':
        return False, u'信息不能为空'

    #检查用户名是否重复
    _rooms = get_rooms()
    for _room in _rooms:
        if name == _room.get('name'):
            return False, u'机房已存在'
    return True, ''

'''
检查更新机房信息
返回值: True/False, 错误信息
'''
def validate_update_room(name, addr, iprange):
    if get_room(name) is None or get_room(addr) is None or get_room(iprange):
        return False, u'用户信息不存在'


    return True, ''







'''
检查更新机房信息
返回值: True/False, 错误信息
'''
def validate_update_room(name, addr, iprange):
    if get_room(name) is None :
        return False, u'机房名不能被修改'

    # #密码要求长度必须大于等于6
    # if len(password) < 6:
    #     return False, u'密码必须大于等于6'
    #
    # if not str(age).isdigit() or int(age) <= 0 or int(age) > 100:
    #     return False, u'年龄必须是0到100的数字'

    return True, ''

'''
更新机房信息
'''
def update_room(name, addr, iprange):
    _rooms = get_rooms()
    for _room in _rooms:
        if _room.get('name') == name:
            _room['addr'] = addr
            _room['iprange'] = iprange
            save_rooms(_rooms)
            break


'''
删除机房信息
'''
def delete_room(name):
    _rooms = get_rooms()
    _idx = -1
    for _room in _rooms:
        _idx += 1
        if _room.get('name') == name:
            del _rooms[_idx]
            save_rooms(_rooms)
            break


if __name__ == '__main__':
    # print get_rooms()
    # print validate_add_room('shi ji hu lian1','jiu xian qiao','192.168.1.0/24') # 检查机房信息输入
    # add_room('aofei1', 'guangdong', '114.114.114.114')  # 测试添加机房信息
    print get_room('ao fei')
#encoding: utf-8

rs_dict = {}

handler = open('www_access_20140823.log', 'r')
for line in handler:
    nodes = line.split(' ')
    key = (nodes[0], nodes[6], nodes[8])
    rs_dict[key] = rs_dict.get(key, 0) + 1
handler.close()

print rs_dict

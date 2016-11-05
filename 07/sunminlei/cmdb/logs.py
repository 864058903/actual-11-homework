#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gettopn(src, topn=10):
    stat_dict = {}
    fhandler = open(src, 'rb')


    for line in fhandler:
        line_list = line.split()
        key = (line_list[0], line_list[6], line_list[8])
        stat_dict[key] = stat_dict.setdefault(key, 0) + 1
    fhandler.close()

    result = sorted(stat_dict.items(), key=lambda x: x[1])[:-topn - 1:-1]
    return result


if __name__ == '__main__':
    access_file_path = 'access_120101.log'
    result = gettopn(access_file_path)
    tbody = ''

    for line in result:
        tbody += '''
        <tr>
                <th>{ip}</th>
                <th>{url}</th>
                <th>{code}</th>
                <th>{count}</th>
            </tr>
        '''.format(ip=line[0][0], url=line[0][1], code=line[0][2], count=line[1])
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我是一个ＨＴＭＬ页面</title>
</head>
<body>
    <!--给用户看的信息　-->
    我是ＫＫ
    <table border="1">
        <thead>
            <tr>
                <th>IP</th>
                <th>URL</th>
                <th>状态码</th>
                <th>次数</th>
            </tr>
        </thead>
        <tbody>
            {tbody}
        </tbody>
    </table>
</body>
</html>
    ''' .format(tbody=tbody)

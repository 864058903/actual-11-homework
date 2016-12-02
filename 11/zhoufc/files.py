#encoding: utf-8

import os

def list_files(dir='/', ext=''):
    path_list = []
    if os.path.exists(dir):
        names = os.listdir(dir)
        for name in names:
            path = os.path.join(dir, name)
            if os.path.isdir(path):
                path_list.extend(list_files(path,ext))
            else:
                if not ext or path.endswith(ext):
                    path_list.append(path)
    return path_list

if __name__ == '__main__':
    print list_files('/tmp/kk/ddd')
    print list_files('/tmp/kk', '.py')
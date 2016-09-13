#coding: utf-8
#

LOG = './access_log'
stats = {}


with open(LOG) as f:
    for line in f:
        mess = line.split()
        key = mess[0], mess[6], mess[8]
        stats[key] = stats.get(key, 0) + 1 
print(stats)

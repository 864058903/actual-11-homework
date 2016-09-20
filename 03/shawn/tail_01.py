#encoding: utf-8

f1 = open("t.txt", "r")

#f1.seek(0, 2)

# endswith("\n")

"""
line = ""

while True:
    line += f1.readline()
    if line.endswith("\n"):
        print line,
        line = ""
"""

# redline != ""

"""
while True:
    cnt = f1.readline()
    if cnt != "":
        print cnt,

"""

# len(readlines)

cnt = f1.readlines()
count = len(cnt)

while True:
    f1.seek(0)
    cnt2 = f1.readlines()
    count2  = len(cnt2)
    if count < count2:
        for i in  cnt2[ count : count2+1 ]:
            print i,
        #print count, count2
        count = count2

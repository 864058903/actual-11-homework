#encoding: utf-8

# path
path = "www_access_20140823.log"

# open file
f1 = open(path, 'r')

"""
--> {(ip,url,code): count}
"""

# value

cnt = f1.readlines()
scnt = [ line.split() for line in cnt ] 

# homework

all_dict = {}
for line in scnt:
    ip,url,code = line[0],line[6],line[8]
    all_dict.setdefault((ip,url,code),0)
    all_dict[(ip,url,code)] += 0

# print all_dict

# def function  

def len_detail(num):
    inner_dict = {}
    for line in scnt:
        inner_dict.setdefault(line[num],0)
        inner_dict[line[num]] += 1
    return inner_dict 


ip_dict = len_detail(0)
url_dict = len_detail(6)
code_dict = len_detail(8)

print "Total ip: %s" % len(ip_dict)
print "Total url: %s" % len(url_dict)
print "Total code: %s" % len(code_dict)
print ""

# print code --> count 
code_list = sorted( code_dict.items(), key=lambda x: x[1], reverse = True )
print "Print code vs count...."
print ""
for x,y in code_list:
	print "{0} \t {1}".format(y,x)

# Baiduspider

spider_line = [ line for line in cnt if "Baiduspider" in line ]
spider_sline = [ line.split() for line in spider_line ]

print ""
print "Baiduspider claw: %s" % len(spider_line)

print ""
for i in spider_sline:
    if i[8] != "200":
        print i[6],i[8]

# close file
f1.close()

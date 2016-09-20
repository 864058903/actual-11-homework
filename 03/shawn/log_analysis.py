#encoding: utf-8

# path
path = "www_access_20140823.log"

# open file
f1 = open(path, 'r')

"""
索引：

ip_dict --> ip:url
url_dict --> url:code
code_dict --> code:url

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

# ip_dict

def len_detail(num):
    ip_dict = {}

    for line in scnt:
        ip_dict.setdefault(line[num],0)
        ip_dict[line[num]] += 1

    print len(ip_dict)

    sort_ip = sorted(ip_dict.items(), key=lambda x: x[1], reverse = True )

    for x,y in sort_ip:
        print y,x

len_detail(0)
len_detail(6)
len_detail(8)



#print ip_dict.keys()


# close file
f1.close()

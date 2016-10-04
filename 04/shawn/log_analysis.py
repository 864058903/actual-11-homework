#encoding: utf-8

def log_dict(logpath, dstpath, topn = 10):
    f1 = open(logpath, 'r')
    scnt = [ line.split() for line in f1.readlines()]
    all_dict = {}
    for line in scnt:
        ip,url,code = line[0],line[6],line[8]
        all_dict[(ip,url,code)] = all_dict.get((ip,url,code),0) + 1
   
    all_list = sorted(all_dict.items(), key=lambda x: x[1], reverse = True)

    f2 = open(dstpath, "w")
    for i in all_list[:topn]:
        f2.write(str(i) + "\n")

    f1.close()
    f2.close()

log_dict("apache.log","result.txt")
log_dict("apache.log","result2.txt", topn = 20)

    


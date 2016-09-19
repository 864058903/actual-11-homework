#encoding:utf-8
'''copy文件'''
# file_01=open('03.txt','rb')
# file_02=open('03new.txt','wb')
# while True:
#     content_01=file_01.readline()
#     if content_01 != '':
#         file_02.write(file_01.readline())
#     else:
#         break
# file_01.close()
# file_02.close()

'''tail实现'''
# file_tail=open('03.txt','r')
#
# file_tail.seek(0, 2)
# while True:
#     content_str = ''
#     content_str+=file_tail.read()
#     if content_str.endswith('\n'):
#         print content_str,
file_log=open('song.log','r')
data_list=[]
while True:
    content_line_str=''
    if  file_log.readline():
        content_line=file_log.readline()
        tup_tmp=(content_line.split(' ')[0],content_line.split(' ')[6],content_line.split(' ')[8])
        data_list.append(tup_tmp)
    else:
        break
file_log.close()
cnt_list={}
for i in data_list:
    if i in cnt_list:
        cnt_list[i]=cnt_list[i]+1
    else:
        cnt_list[i]=1
print '统计数据为：\n',cnt_list



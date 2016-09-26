#encoding:utf-8
'''统计日志'''
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
cnt_file=open('contFile.txt','w')
'''把统计的内容写到文件里'''
for i in cnt_list:
    # cnt_file.write(str(i))
    cnt_file.write(str(i)+'出现的次数为：'+str(cnt_list[i])+'\n')
cnt_file.close()


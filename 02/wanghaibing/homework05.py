#!/usr/bin/env python
alist=[]
def print_(id):
   print 'The following figures have been used:'
   for i in id:
      print '\033[31m%s\033[0m' % i[1],
   print

while True:
    name=raw_input('Please enter your Name/exit: ')
    if name == "exit":
       exit()
    while True:
       num=0
       n_id=raw_input('Please enter your Id/exit: ')
       if n_id == "exit":
           exit()
       elif not n_id.isdigit():
          print 'Id is int'
          continue
       else:
          for i in alist:
              if i[1] == n_id:
                 num=1
                 #print 'Id repeat'
                 print_(alist)
                 break
          if num == 0 :
              atuple=(name,n_id)
              alist.append(atuple)
              print '\033[31mYour input is :\033[0m\n %s ' % alist
              break


'''
功能ok
'''

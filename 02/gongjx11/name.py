#!/usr/bin/env python
import os,sys
user=raw_input("please input user:")
users=[]

for a in user.split(','):
  username,userid=a.split(':')
  strip=username.strip(),userid.strip()
  users.append(strip)
print(users)


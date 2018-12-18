# -*- coding:utf-8 -*-
# Author:Jone

name = input("userName:")
password = input("passWord:")
print(name)
print(password)
info ='''
-----info----
name:%s
password:%s
''' %(name,password)

info2 ='''
-----info2----
name:{name}
password:{password}
'''.format(name=name,password=password)

print(info)
print(info2)
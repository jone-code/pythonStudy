# -*- coding:utf-8 -*-
# Author:Jone

#the import is a module
import getpass
name = input("name:")
password = getpass.getpass("password:")

if "123" == name and "123" == password:
    print("welcome user {name} login...".format(name=name))
else:
    print("invalid username or password")

age = int(input("age:"));
if 12 == age:
    print("true")
elif 12>age:
    print("think bigger")
else:
    print("think smaller")
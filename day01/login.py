# -*- coding:utf-8 -*-
# Author:Jone
import getpass
name_list = []
password_list = []
username_handle = open("username.txt","r")
password_handle = open("password.txt","r")

while True:
    line = username_handle.readline()
    if line:
        line = line.split("\n")[0]
        name_list.append(line)
    else:
        break
username_handle.close()

while True:
    line = password_handle.readline()
    if line:
        line = line.split("\n")[0]
        password_list.append(line)
    else:
        break
password_handle.close()

print(name_list,password_list)

count = 0
name = input("name:")
while True:
    password = getpass.getpass("password:")
    if name in name_list and password in password_list:
        print("welcome {name}".format(name=name))
        break
    elif count>2:
        print("{name} is locked".format(name=name))
        '''
        username_handle2 = open("username.txt","w")
        for i in name_list:
            if(name_list.index(i)==name):
                username_handle2.write("---"+name_list.index(i)+"\n")
            else:
                username_handle2.write(""+name_list.index(i)+"\n")
        username_handle2.close()
        '''
        break
    else:
        print("password is error!!")
        count+=1




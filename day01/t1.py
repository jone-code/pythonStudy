# -*- coding:utf-8 -*-
# Author:Jone
name = "zhangsan"
username_handle2 = open("username.txt","w")
while True:
    line = username_handle2.readline()
    print(line)
    line = line.split("\n")[0]
    if line==name:
        username_handle2.write("---"+name)
    else:
        break
username_handle2.close()
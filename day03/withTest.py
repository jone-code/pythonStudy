# -*- coding:utf-8 -*-
# Author:Jone
#with 帮组自动关闭文件
with open("yesterday","r",encoding="utf-8") as f:
    for line in f:
        print(line)
#打开多个文件
with open("yesterday","r",encoding="utf-8") as f, \
        open("yestarday2","r",encoding="utf-8") as f2,\
        open("yesterday","r",encoding="utf-8"):
    for line in f:
        print(line)
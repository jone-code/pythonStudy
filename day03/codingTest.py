# -*- coding:utf-8 -*-
# Author:Jone
import sys
print(sys.getdefaultencoding())

msg = "你好"
msg_gb2312  = msg.encode("utf-8").decode("utf-8").encode("gbk")
print(msg_gb2312)

ss = msg.encode("gbk")
sss =  ss.decode("gbk").encode("utf-8")
print(sss)
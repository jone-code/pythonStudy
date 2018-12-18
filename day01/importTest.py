# -*- coding:utf-8 -*-
# Author:Jone
import sys
print(sys.path)
print(sys.argv)

import os
os.system("dir") #执行命令但是不会保存结果
result = os.popen("dir")
print(result.read())

result = os.popen("dir").read()
print(result)

#os.mkdir("newDir")
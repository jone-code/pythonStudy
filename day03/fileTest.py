# -*- coding:utf-8 -*-
# Author:Jone
'''
r 模式 读
w 模式 打开文件会创建一个文件 所以相当于会删除已有的文件
a 模式 是追加
r+    读写  读和追加的模式 write 会写到文件末尾
w+    写读 先创建一个文件然后再写 接着读取， 写的内容也只能在末尾
a+    追加读写
rb    以二进制的方式读取文件
wb    以二进制的方式写文件  写的内容必须 是byte
rU或者r+U 会把 \r \n \r\n  自动转换为 \n
写的内容只能在末尾
'''

file = open("yesterday","r",encoding="utf-8") # this is file handle
#data = file.read()
#print(data)

#readlines 一次性读取了所有的行 只适合读小文件
for index,line in enumerate(file.readlines()):
    if index == 2:
        print("------分割--------")
        continue
    print(line.strip())

file.close()
#这种方式 就是一行行去读
file = open("yesterday","r",encoding="utf-8")
while True:
    data = file.readline()
    if data == "":
        break
    else:
        print(data.strip(),"-------------")
print("#####################")
#这种方式 就是一行行去读 效率比较高
file = open("yesterday","r",encoding="utf-8")
for line in file:
    print(line.strip())
#文件读完 光标到最后 如果想重新读
#看文件读取的位置 记录字符数
file = open("yesterday","r",encoding="utf-8")
print(file.tell())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.tell())
#重置文件读取的位置 参数可以是任意的第几个字符
file.seek(0)
print(file.readline())

print(file.encoding)
#返回操作系统python操作文件接口的编号
print(file.fileno())

#从缓存中刷到硬盘里
file.flush()

#从头清空文件，如果参数是10 表示从10的位置后
file = open("yesterday","a",encoding="utf-8")
file.seek(10)
file.truncate(10)
file.close()

file = open("yesterday","r+",encoding="utf-8")
file.readline()
file.write("---------")
file.close()

file = open("yestarday2","w+",encoding="utf-8")
file.write("12312312123123")
file.write("12312312123123")
file.write("12312312123123")
file.write("12312312123123")
print(file.tell())
file.seek(10)
print(file.tell())
print(file.readline())
file.write("=======================")
file.close()
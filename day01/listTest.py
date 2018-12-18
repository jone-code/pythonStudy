# -*- coding:utf-8 -*-
# Author:Jone

names = ["123","324"]
names.append("123")
names.append("1243123")
icount = names.count("123")
print(icount)
print(names)
print(names[:])#对list的浅拷贝
print(names[0:-1:2])
print(names[::2])
print(len(names))
#add
names.insert(1,"qqq")
print(names)

#del names[0]
names.remove("123")
print(names)
#update
names[0]="123123123213"
print(names)

#get index
index = names.index("123")
print(index)
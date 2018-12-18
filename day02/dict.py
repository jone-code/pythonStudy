# -*- coding:utf-8 -*-
# Author:Jone
#字典是无序的
info = {
    "1":"zhangsan",
    "2":"lisi",
    "3":"wangwu"
}
print(info)
#存在就修改 不存在就去创建
info["1"] = "zhangsan1"
info["123"] = "qweqweqw"
print(info)
#get 是比较安全的获取 为空的话不会报错
print(info.get("123123"))
print("123" in info)


#删除
'''
del info["1"]
info.pop("123")
info.popitem()#随便删一个
'''
print(info.values())
print(info.keys())


b={
    "1":"1111",
    2:1,
    3:5
}

info.update(b)
print(info)

print(info.items())

c = dict.fromkeys([6,7,8],"qweqw")
print(c)


for index in info:
    print(index,info[index])
#上边的方法比下边的高效 因为 info.items 把字典转换为了列表
for k,v in info.items():
    print(k,v)
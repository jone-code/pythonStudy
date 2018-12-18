# -*- coding:utf-8 -*-
# Author:Jone
name = "\tjone"
#首字母大写
print(name.capitalize())

print(name.count("a"))

print(name.center(10,"-"))

print(name.endswith("e"))
#把table键转换为多少个空格
print(name.expandtabs(tabsize=10))
#找到某一个字符串或者字符开头的下标位置
print(name.find("j"))
#截取字符串 叫切片
print(name[name.find("o"):])
name1 = "name is {aaa}"
print(name1.format(aaa="jone"))

print(name1.format_map({"aaa":"1233123"}))
#是不是阿拉伯数字 a-z 0-9
print(name.isalnum())
#是不是纯英文
print(name.isalpha())
#是否是十进制数
print(name.isdecimal())
#是不是 整数
print("123".isdigit())
#是不是一个合法的标识符  是不是一个合法的变量名
print("123123".isidentifier())

#是不是小写
print("aaa".islower())
#是不是大写
print("aaa".isupper())
#是不是数字
print("123123".isnumeric())
#判断是不是title
print("My Name Is Jone".istitle())
#join
print("My Name Is Jone".join("---*"))

print("".join(["1","2","3"]))
#这样不能再 右侧填充
#print("12".ljust(10,"q2"))
#这个可以
print("12".ljust(10,"q"))
print("qqq".rjust(5,"1"))

print("AAA".lower())
print("aaa".upper())

#去空格和回车
print("   aa   ".lstrip())
print("   aa   ".rstrip())
print("   aa   ".strip())

p= str.maketrans("abcdef","123456")
print("daca".translate(p))

print("asdasdasd".partition("s"))

print("asdasdas".replace("a","-a-",1))
#从右边查找
print("qweqwe".rfind("q"))

print("1asdasd".split("a"))

print("qweasd\nsafs".splitlines())

#大小写互换
print("AsasdAAA".swapcase())
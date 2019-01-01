# -*- coding:utf-8 -*-
# Author:Jone

#  所有的元素不为false  0 是false 空字符串也是 false
b = all([1,-1])
print(b)
b = all(["","123"])
print(b)
# 可迭代对象中有一个是True 那么就返回true
b= any(["","123123"])
print(b)
#十进制转二进制
b = bin(10)

#返回一个 字节数组
bytearray("asdas",encoding="utf-8");
# 返回ascall码对应的字符
b = chr(100)

#返回 ascall 码对应的码
b = ord("c")
print(b)


print("===============")
#exec 执行字符串的代码
str = '''
b = chr(100)
print(b)
'''
exec(str)

#查看 类中的方法
a = dict()
dir(a)
#返回商和余数
divmod(5,2)
#转换对象 计算简单运算
eval("1+2")
#转换为16 进制数
hex(100)
#转换八进制
oct(8)

#计算3的5次方
pow(3,5)
# -*- coding:utf-8 -*-
# Author:Jone
from collections import Iterable
from collections import Iterator
'''
集合类型 list，set ，dict，tuple ，str 
生成式 generator  
这些直接用于for循环的对象都是可迭代对象



可以被next函数调用并不断返回下一个值的对象成为迭代器 Iterator

'''

b = isinstance([],Iterable)
print(b)

b = isinstance((x for x in range(10)),Iterable)
print(b)



b = isinstance([],Iterator)
print(b)

b = isinstance((x for x in range(10)),Iterator)
print(b)

b = isinstance(iter([]),Iterator)
print(b)
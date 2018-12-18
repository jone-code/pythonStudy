# -*- coding:utf-8 -*-
# Author:Jone
#集合 无序不可重复

list1 = [2,1,4,6,4,5]
list1 = set(list1)
print(list1)
#定义set的两种方式
#list2=set([2,2,5,6])
list2 = {2,2,5,6,7}
print(list2)
#取交集
print(list1.intersection(list2))
print(list1 & list2)
print("&")
#取并集
print(list1.union(list2))
print(list1 | list2)
print("|")
#求差集
print(list1.difference(list2))
print(list1 - list2)
print(list2.difference(list1))
print(list2 - list1)
print("-")
#判断是不是子集
print(list1.issubset(list2))
#是不是父集
print(list1.issuperset(list2))
#对称差集 取互相没有的
print(list1.symmetric_difference(list2))
print(list1 ^ list2)
print("^")
#没有交集返回true
print(list1.isdisjoint(list2))
list3 = {2,4,6}
list4 = {1,5,7}
print(list3.isdisjoint(list4))

#添加
list3.add(111)
list3.update([1,2,7])
print(list3)

#删除
list3.remove(111)
print(list3)
#随机删 ？？
print(list3.pop())
print(list3.discard(123))
#存在即删除
list3.discard(7)
#判断是否存在
print( 2 in list3)
print( 2 not in list3)


print("===========pop===============")
list3 = [234,2341,234123,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list3 = set(list3)
print(list3)
list3.pop()
print(list3)
list3.pop()
print(list3)
list3.pop()
print(list3)
list3.pop()
print(list3)



# -*- coding:utf-8 -*-
# Author:Jone
'''
装饰器：本身就是第一个函数
作用: 装饰其他函数，为其他函数提供附加功能
原则：不能修改被装饰的函数的源代码,不能修改被装饰的函数的调用方式   装饰器对装饰的函数是完全透明的，对调用方也是不可知的


实现装饰器的知识储备
1.函数即"变量"
2.高阶函数
3.嵌套函数
高阶函数+嵌套函数=>装饰器
'''
import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        print("the func begin time is %s" %(start_time))
        func()
        stop_time = time.time()
        print("the func end time is %s" %(stop_time))
    return warpper

@timmer
def test1():
    print("begin....")
    time.sleep(3)
    print("end....")
test1()
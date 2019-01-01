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

def timer(func):
    def innerFunc(*args,**kwargs):
        start_time = time.time()
        print("the func begin time is %s" %(start_time))
        func(*args,**kwargs)
        #如果装饰的方法需要返回值
        #res =  func(*args,**kwargs)
        #return res
        stop_time = time.time()
        print("the func end time is %s" %(stop_time))
    return innerFunc  # 其实这里返回的是方法的内存地址

@timer
def test1(name):
    print("begin....")
    print(name)
    time.sleep(3)
    print("end....")
'''
@timer 相当于是这个  就是把原来的test1 方法用timer 装饰一下
test1 = timer(test1);

其实调用的test1 已经是在调用 timer 中的内嵌方法 innerFunc 
内嵌方法 innerFunc 加参数  其实也是配合 想要装饰的方法要传参的情况
'''
test1(123)
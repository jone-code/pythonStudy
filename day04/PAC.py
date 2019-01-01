# -*- coding:utf-8 -*-
# Author:Jone
import time

def consumer(name):
    print("%s准备消费" %name)
    while True:
        production = yield
        print("产品[%s],被[%s]消费" %(production,name))

def producter(name):
    c= consumer("zhangsan")
    c1 = consumer("lisi")
    c.__next__()
    c1.__next__()
    print("%s开始生产"%name)
    for i in range(10):
        time.sleep(1)
        print("生产了两个")
        c.send(i)
        c1.send(i)


producter("jone")

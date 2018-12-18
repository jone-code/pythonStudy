# -*- coding:utf-8 -*-
# Author:Jone

name = "Alex"

def change_name():
    name = "Alex2"

    def change_name2():
        name = "Alex3"
        print("第3层打印",name)

    change_name2() #调用内层函数
    print("第2层打印",name)


change_name()
print("最外层打印",name)



def calc(n):
    print(n)
    if int(n/2) ==0:
        return n
    return calc(int(n/2))

calc(10)


def stu_register(name,age,*args):
    print(name,age,args)

stu_register(1,25,123123)

def func2(name,age,**kwargs):
    print(name,age,kwargs)

func2(1,2,qq="1",qqw="2")

company = "company"
def change_name(name):
    #global company #加这个 在函数内修改后会全局生效
    print("before:",name)
    name = "lisi"
    company = "company1"
    print("after:",name)
name = "zhangsan"
change_name(name)
print(name)
print(company)


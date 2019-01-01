# -*- coding:utf-8 -*-
# Author:Jone
#列表生成式
a = [i*2 for i in range(10)]
print(a) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

#生成器 generator  节省空间 不会立刻生成列表 只有在用的时候才会生成
b = (i * 2 for i in range(10))
print(b)  #<generator object <genexpr> at 0x000000000216EE08>   不能直接访问列表中的元素，其实 他也不是列表 ，
#只能通过这种方式去元素  而且他只会保留一个元素 这样节省内存
ele = b.__next__()
print(ele)

print("===========")
for i in b:
    print(i)

print("===========")
def fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        # a,b = b,a+b 并不是 先把a = b  然后计算 b = a+b  而是这样 tub=(b,a+b)  a=tub[0],b = tub[1]
        n+=1
    return "这里会返回异常信息"
f = fib(10);

#next 方法到最后没有元素会报异常  只能去异常处理一下
print(f.__next__())

while True:
    try:
        x=next(f)
    except StopIteration as e:
        print("error",e.value)
        break





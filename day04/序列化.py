# -*- coding:utf-8 -*-
# Author:Jone

import json
import pickle

data = {"name":"zhangsan","age":18}
str = json.dumps(data)
print(str)
data2 = json.loads(str)
print(data2["name"])
print(data2["age"])

def func():
    print("123123")

data = {"name":"zhangsan","age":18,"func":func}
str = pickle.dumps(data)
print(str)
data2 = pickle.loads(str)
print(data2["func"]())
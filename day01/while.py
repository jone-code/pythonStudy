# -*- coding:utf-8 -*-
# Author:Jone
count = 0;

while count<3:
    count+=1
    age = int(input("age:"));
    if 12 == age:
        print("true")
        break
    elif 12>age:
        print("think bigger")
    else:
        print("think smaller")
else:
    print("end")
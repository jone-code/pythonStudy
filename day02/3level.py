# -*- coding:utf-8 -*-
# Author:Jone

data = {
    '北京':{
        "昌平":{
            "沙河":["qqqq","test"],
            "天通苑":["123123","12dwqe"]
        },
        "朝阳":{
            "望京":["21312","12312313"],
            "国贸":{"qqq2213","asdasd13"},
        },
        "海淀":{},
    },
    '山东':{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    '广东':{
        "东莞":{},
        "常熟":{},
        "佛山":{},
    },
}

while True:
    for i in data:
        print(i)
    choice = input("选择1>>")
    if choice in data:
        data2 = data[choice]
        while True:
            for i2 in data2:
                print("\t",i2)
            choice2 = input("选择2>>")
            if choice2 in data2:
                data3 = data2[choice2]
                while True:
                    for i3 in data3:
                        print("\t",i3)
                    choic3 = input("选择2>>")
                    if choic3 in data3:
                        print("\t",data3[choic3])
                    print("最后一层")
                    back = input("按任意键返回上一层")
                    pass

            else:
                back = input("按任意键返回上一层")
                break
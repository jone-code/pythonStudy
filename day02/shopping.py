# -*- coding:utf-8 -*-
# Author:Jone

product_list = [("IPhone",1000),("Mac Pro",9800),("Watch",1000)]
shopping_list = []

salary = input("salary:")

if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("please choses>>>")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice>=0 and user_choice<len(product_list):
                p_item = product_list[user_choice]
                if p_item[1]<=salary:
                    print("you can buy it")
                    shopping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added $s into shoppingcart, you current balance is $d"%(p_item,salary))
                    print("Added $s into shoppingcart, you current balance is $d"%(p_item,salary))
                else:
                    print("\033[41;1m 余额不足 \033[0m")
            else:
                print("product code{code} is no exist".format(code = user_choice))
        elif user_choice == "q":
            print("----shoppinglist-----")
            print(shopping_list)
            print("salary:"+salary)
            print("exit...")
            exit()
        else:
            print("option error")
else:
    print("salary is error！！")
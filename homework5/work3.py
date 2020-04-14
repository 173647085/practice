# -*- encoding: utf-8 -*-
'''
@File : work3.py
@Time : 2020/04/08 07:57:01
@Author : gwd 
@Version : 1.0
@Contact : 1033876073@qq.com
'''
# 编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
# here put the import lib
def auth_func(func):
    def wrapper(*args,**kwargs):
        user_name = input('用户名：').strip()
        user_pass = input('密  码：').strip()
        if user_name == "gwd" and user_pass == "666666":
            ret = func(*args,**kwargs)
            return ret
        else:
            print('账户或密码错误!')
    return wrapper
@auth_func
def index():
    print('欢迎使用')
@auth_func
def home(name):
    print('欢迎%s' %name)
@auth_func
def shopping_car(name,names,namess):
    print('购物车的东西【%s,%s,%s】' %(name,names,namess))

index()
home('高卫东')
shopping_car('奶茶','篮球','裤子')
# -*- encoding: utf-8 -*-
'''
@File : 5_3.py
@Time : 2020/04/14 18:37:32
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
# 编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
# here put the import lib

import time
def auth_func(func):
    def wrapper(*args,**kwargs):
        username = input("用户名：")
        password = input("密  码：")
        if username == "zxl" and password == "123456":
            ret = func(*args,**kwargs)
            return ret
        else:
            print('账户或密码错误!')
    return wrapper
@auth_func
def index():
    print('欢迎使用')
@auth_func
def home():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


index()
home()


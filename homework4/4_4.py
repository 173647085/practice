# -*- encoding: utf-8 -*-
'''
@File : 4_4.py
@Time : 2020/04/14 18:24:11
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# 模拟用户登录:5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
# 系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);
# here put the import lib

import base64

try:
    f=open(r"D:\practice\4_4.txt","r")
    lines = f.readlines()
    key=0
except IOError as error:
    print(error)
else:
    name = input("请输入姓名:")
    for l in lines:
        l=l.strip().split(" ")
        if name == l[0]:
            for i in range(3):
                username =input("请输入账号:")
                if username == l[1]:
                    for i in range(3):
                        password =input("请输入密码:")
                        if l[2]==str(base64.b64encode(password.encode('gbk'))):
                            print("登录成功")
                            key=1
                            break
                        else:
                            print("密码错误,您还可重试{}次".format(2-i))
                            if i==2:
                                print("您的帐号已锁定请下次再试")
                                key=1
                    break
                else:
                    print("账号错误")
        if key==1:
            break
    else:
        print("查无此人")

        
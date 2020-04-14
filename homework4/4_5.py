# -*- encoding: utf-8 -*-
'''
@File : 4_5.py
@Time : 2020/04/14 18:23:57
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# 通过Python来模拟实现一个txt文件的拷贝过程;
# here put the import lib

try:
    f=open(r"D:\practice\4_5.1.txt","r")
    lines =f.readlines()
    f1=open(r"D:\practice\4_5.2.txt","w+")
    for i in lines:
        f1.write(i)
except IOError as error:
    print(error)
f.close()
f1.close()
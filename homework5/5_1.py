# -*- encoding: utf-8 -*-
'''
@File : 5_1.py
@Time : 2020/04/14 18:22:51
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
# 编写一个装饰器，能计算其他函数的运行时间；
# here put the import lib
import time
import random
def outer(func):
    def inner(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print("函数运行时间:%s" %(end - start))
        return res
    return inner

@outer
def func1():
    time.sleep(random.randrange(1,5))
    print("测试")

@outer
def count(x):
    time.sleep(random.randrange(1,5))
    math=0
    for i in range(x):
        math+=i
    return math

func1()

f2 = count(1000)
print(f2)

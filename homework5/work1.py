# -*- encoding: utf-8 -*-
'''
@File : work1.py
@Time : 2020/04/08 07:56:35
@Author : gwd 
@Version : 1.0
@Contact : 1033876073@qq.com
'''
# 编写一个装饰器，能计算其他函数的运行时间；
# here put the import lib
import time
import random
def timmer(func):
    def warpper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print("函数运行时间:%s" %(end - start))
        return res
    return warpper

@timmer
def func1():
    time.sleep(random.randrange(1,5))
    print("测试函数")

@timmer
def func2(date):
    time.sleep(random.randrange(1,5))
    print("Today is %s" %date)
    return 1

f1 = func1()
print(f1)

f2 = func2("Wednesday")
print(f2)

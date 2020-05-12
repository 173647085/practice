# -*- encoding: utf-8 -*-
'''
@File : 8_3.py
@Time : 2020/04/28 18:43:34
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com


3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
# here put the import lib
from multiprocessing import Process, Manager
import os, time, random,math

def is_prime(number):  # 判断是否为素数
    if number == 0 or number == 1:
        return False
    sqrt = int(math.sqrt(number))
    for j in range(2, sqrt + 1):  # 从2到number的算术平方根迭代
        if number % j == 0:  # 判断j是否为number的因数
            return False
    return True

def count_prime(start, end,dict_count):
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    dict_count.append(count)

if __name__=='__main__':
    print('-------对比1: 单进程 : 8进程-------')
    t1 = time.time()
    dict_count=[]
    count_prime(0, 100001, dict_count)
    t2 = time.time()
    print('单进程结果:{},时间:{}'.format(sum(dict_count),t2-t1))
    #https://www.jb51.net/article/129692.htm 多进程通讯
    dict_count=Manager().list()
    tasks = []
    for i in range(8):
        p = Process(target=count_prime,
                    args=(0 + 12500 * i, 1 + 12500 * (i + 1), dict_count))
        tasks.append(p)
        p.start()
    for p in tasks:
        p.join()
    t3 = time.time()
    print('多进程结果:{},时间:{}'.format(sum(dict_count),t3-t2))

    print('-------对比2: 4进程 : 10进程-------')
    t1 = time.time()
    dict_count=Manager().list()
    tasks = []
    for i in range(4):
        p = Process(target=count_prime,
                    args=(0 + 25000 * i, 1 + 25000 * (i + 1), dict_count))
        tasks.append(p)
        p.start()
    for p in tasks:
        p.join()
    t2 = time.time()
    print('4进程结果:{},时间:{}'.format(sum(dict_count),t2-t1))
    #https://www.jb51.net/article/129692.htm 多进程通讯
    dict_count=Manager().list()
    tasks = []
    for i in range(10):
        p = Process(target=count_prime,
                    args=(0 + 10000 * i, 1 + 10000 * (i + 1), dict_count))
        tasks.append(p)
        p.start()
    for p in tasks:
        p.join()
    t3 = time.time()
    print('10进程结果:{},时间:{}'.format(sum(dict_count),t3-t2))



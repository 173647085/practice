# -*- encoding: utf-8 -*-
'''
@File : 8_1.py
@Time : 2020/04/28 18:24:37
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；

'''
# here put the import lib

import threading, random, time
from multiprocessing.pool import ThreadPool


def run(num_stu):
    score = random.randint( 0, 100 )
    print( '学生{}的分数为: {}.'.format(num_stu,score))
    num_stu+=10
    time.sleep(1)

if __name__ == '__main__':
    t = ThreadPool(10)
    for i in range(100):
        t.apply_async(run,(i+1,))
    t.close()
    t.join()

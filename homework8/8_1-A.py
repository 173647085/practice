# -*- encoding: utf-8 -*-
'''
@File : 8_1.py
@Time : 2020/04/28 18:18:56
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；

'''
# here put the import lib

import threading, random, time

stu_num = 1
mutex = threading.Lock()

class Scorethread( threading.Thread ):

    def run( self ):
        global stu_num
        for i in range(20):
            mutex.acquire()
            score = random.randint( 0, 100 )
            print( '%s is running: 学号为%s的学生的分数为: %s.' %( self.name, stu_num, score ) )
            stu_num += 1
            mutex.release()
            time.sleep( 1 )

def test():
    for i in range(5):
        t = Scorethread()
        t.start()

if __name__ == "__main__":
    test()

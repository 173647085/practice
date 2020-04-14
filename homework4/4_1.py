# -*- encoding: utf-8 -*-
'''
@File : 4_1.py
@Time : 2020/04/14 18:25:08
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
# 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
# here put the import lib

import time
import collections
list1=[1,2,3,4,5,6,7,8,9,10]
time1=time.time()
list1.insert(0,0)
list1.append(11)
time2=time.time()
print(list1)
print("运行时间%.30f"%(time2-time1))
q=collections.deque(['a', 'b', 'c'])
time11=time.time()
q.append('x')
q.appendleft('y')
time12=time.time()
print(q)
print("运行时间%.30f"%(time12-time11))
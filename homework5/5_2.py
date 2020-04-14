# -*- encoding: utf-8 -*-
'''
@File : 5_2.py
@Time : 2020/04/14 18:22:11
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
#  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
# here put the import lib
import functools
import logging


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        logfile = r"D:\practice\homework5\log.txt"
        logging.basicConfig(
            level=logging.INFO,            
            format='%(asctime)s - %(levelname)s - %(message)s', 
            datefmt='%Y-%m-%d %H:%M:%S ', 
            filename=logfile,  
        )
        logging.info('Call record.\r') 
        return func(*args, **kw)
    return wrapper

@log
def test1():
    return 1

@log
def test2():
    return 1

test1()
test2()

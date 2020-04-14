# -*- encoding: utf-8 -*-
'''
@File : work2.py
@Time : 2020/04/08 07:56:50
@Author : gwd 
@Version : 1.0
@Contact : 1033876073@qq.com
'''
#  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
# here put the import lib
import functools
import logging


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        logfile = r"E:\pythonworkplace\homework5\log.txt"
        logging.basicConfig(level=logging.INFO,  
                            format='%(asctime)s %(levelname)s %(message)s', 
                            datefmt='%Y-%m-%d %H:%M:%S', 
                            filename=logfile,  
                   )
        logging.info('valid passed.\r') 
        return func(*args, **kw)
    return wrapper

def test1():
    return 1

def test2():
    return 1

f1 = log(test1)
f2 = log(test2)
print(f1())
print(f2())
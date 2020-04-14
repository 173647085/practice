# -*- encoding: utf-8 -*-
'''
@File : 4_6.py
@Time : 2020/04/14 18:23:42
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# 通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小;
# here put the import lib

import os
from datetime import datetime
path = r"D:\practice"
files= os.listdir(path)
for i in files:
    file = os.path.join( r"D:\practice",i)
    if os.path.isfile(file):
        print("{}      {}     {}     {}".format(i,datetime.fromtimestamp(os.path.getmtime(file)),"文件",os.path.getsize(file)))
    else:
        print("{}      {}     {}".format(i,datetime.fromtimestamp(os.path.getmtime(file)),"文件夹"))
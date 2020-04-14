# -*- encoding: utf-8 -*-
'''
@File : 4_7.py
@Time : 2020/04/14 18:23:31
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# 使用python代码统计一个文件夹中所有文件的总大小
# here put the import lib

import os
path = r"D:\practice"
size=0
files= os.listdir(path)
for i in files:
    file = os.path.join( r"D:\practice",i)
    size +=os.path.getsize(file)
    
print("所有文件总大小为:%d" %size)
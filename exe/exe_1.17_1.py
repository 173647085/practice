#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import os
pwd = os.path.abspath('.')
print( os.path.basename('D:\practice') )   # 返回文件名
print( os.path.dirname('D:\practice') )    # 返回目录路径
print( os.path.split('D:\practice') )      # 分割文件名与路径
print( os.path.join('root','test','D:\practice') )  # 将目录和文件名合成一个路径
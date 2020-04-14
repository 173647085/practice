# -*- encoding: utf-8 -*-
'''
@File : 4_8.py
@Time : 2020/04/14 18:23:11
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
#  京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.0/24段的ip;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
# here put the import lib

import random
from collections import Counter

try:
    f=open(r"D:\practice\homework4\ip.txt","w+")
    str1 = "172.25.254."
    for i in range(1200):
        str2 = str1 + str(random.randint(1,255))
        f.write(str2)
        f.write("\n")
    f.close()
    f=open(r"D:\practice\homework4\ip.txt","r")
    lines =f.readlines()
except IOError as error:
    print(error)
else:
    line = []
    for l in lines:
        line.append(l.strip())
    print(Counter(line).most_common(10))
    f.close()
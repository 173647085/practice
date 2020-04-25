# -*- encoding: utf-8 -*-
'''
@File : 7_1.py
@Time : 2020/04/17 17:32:21
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib
'''
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
   提示，文件有1000行，注意控制每次读取的行数；
'''

import re

try:
    fr=open(r'D:\practice\homework7\webspiderUrl.txt', 'r', encoding='utf-8')
    pattern = r'[a-zA-Z]+://[^\s$(;|\')]*'  # 匹配所有的网址形式
    line = fr.readline()
    fw=open(r'D:\practice\homework7\Url.txt', 'a', encoding='utf-8')
    while line:
        url = re.findall(pattern, line)  # 获取每行所有符合该模式的网址
        line = fr.readline()
        if url:  # 如果查得的url不为空,则逐个写入url列表里的网址
            # i = 0
            for i in range(len(url)):
                fw.write(url[i] + '\n')
                # i += 1
    fw.close()

except Exception as e:
    print(type(e), ':', e)
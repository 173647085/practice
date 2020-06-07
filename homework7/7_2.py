# -*- encoding: utf-8 -*-
'''
@File : 7_2.py
@Time : 2020/04/25 17:52:36
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com

给定100个企业网站首页链接地址（用1中给出的URL地址）；
请爬取每个页面上，企业介绍的链接地址；
说明，满足企业介绍网址的条件是，
标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
提示：要用到requests库，BeautifulSoup库
'''
# here put the import lib

import os
import requests
from bs4 import BeautifulSoup
import re

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

list2=[]
def get(url):
    try:
        text2=requests.get(url,headers=headers).content.decode('utf-8')
    except IOError:
        pass
    except requests.exceptions.ConnectionError:   #Requests请求时有时会请求不到页面，或是请求到空白的页面，超时要重试几次，使用try…except语句
        pass
    try:
        bs = BeautifulSoup(text2, 'html.parser') #指定Beautiful的解析器为html.parser
    except BaseException:
        print('处理',url,'时发生异常')
        pass
    else:
        bsa = bs.find_all("a",text2=re.compile(r'关于我们|企业介绍|企业发展|历史|概况'))
        for t in bsa:
            p=t.attrs['href']
            list2.append(p)
                
w1=r'D:\practice\homework7\Url.txt'
with open(w1,'r',encoding='utf-8')as f:
    i=0
    while i<100:
        line=f.readline()
        while line:
            line = line.strip()
            print(line)
            get(line)
            print(list2)
            line = f.readline()
            i += 1





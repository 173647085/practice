# -*- encoding: utf-8 -*-
'''
@File : 7_4.py
@Time : 2020/06/03 17:33:06
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
# 4爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
'''

# here put the import lib
from bs4 import BeautifulSoup
import requests
import re
import os

url = 'https://www.programcreek.com/python/index/221/requests'

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

r=requests.get(url,headers=headers).content.decode('utf-8')
s=BeautifulSoup(r,'html.parser')
ls = s.find(id='api-list').find_all('a')
list1=[]
for i in ls:
	list1.append(i.attrs['href'])

w1=r'D:\practice\homework7\request.txt'
with open(w1,'a+',encoding='utf-8')as f1:
    for k in list1:
        d1={}
        exe = requests.get(k, headers=headers).content.decode('utf-8')
        bs = BeautifulSoup(exe, 'html.parser')
        d1['example'] = bs.find(id='main').h1.text
        l1=[]
        for i in bs.find_all('pre', class_='prettyprint'):
            l1.append(i.text)
            d1['ans'] = l1
        for i in d1['ans']:
            f1.write("********************************************\n")
            print(i)
            break
            f1.write(i+'\n')
            f1.write("********************************************\n")


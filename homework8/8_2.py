# -*- encoding: utf-8 -*-
'''
@File : 8_2.py
@Time : 2020/04/28 18:32:17
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
'''

# here put the import lib


import threading,re,requests
from multiprocessing.pool import ThreadPool

with open(r"D:\practice\homework8\url_data.txt")as f:
    urls = f.readlines()

def getHtmlText(url):
    try:        
        r = requests.get(url,timeout = 5)    
        r.raise_for_status()
        print("%s访问成功" %url)
    except:
        print("%s产生异常" %url)

if __name__ == '__main__':
    t = ThreadPool(10)
    for i in range(len(urls)):
        regular = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')
        ret = re.findall(regular, urls[i])
        for j in range(len(ret)):
            t.apply_async(getHtmlText,(ret[j],))
    t.close()
    t.join()



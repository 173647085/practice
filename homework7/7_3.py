# -*- encoding: utf-8 -*-
'''
@File : 7_2.py
@Time : 2020/04/25 17:52:36
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com

3给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
#Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
'''
# here put the import lib

import requests
import re,os,wget
from urllib.parse import quote
from urllib import request


headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
link = 'http://www.listeningexpress.com/studioclassroom/ad/'

response = requests.get(link, headers=headers)
html = response.text
src=r"sc-ad [^\"]*\.mp3"
mp3 = re.compile(src)
list1 = re.findall(mp3, html)
list1 = list(set(list1))
# os.chdir('homework7')

for i in list1:
    print('下载中', i)
    try:
        wget.download(link + i)
        print('文件{}下载成功'.format(i))
    except request.HTTPError:
        print('文件{}下载失败'.format(i))

print('任务完成！')


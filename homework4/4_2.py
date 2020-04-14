# -*- encoding: utf-8 -*-
'''
@File : 4_2.py
@Time : 2020/04/14 18:24:36
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''
# 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
# 将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
# here put the import lib

import datetime

def main():
    date_str =input('请输入日期（2019/01/01）：')
    date_str1=date_str.split("/")
    date_str1 = list(map(int, date_str1))
    date_time=datetime.date(date_str1[0], date_str1[1], date_str1[2])
    date=datetime.datetime.strptime(date_str, '%Y/%m/%d')
    date_time=date_time.isocalendar()
    list1=["一","二","三","四","五","六","日"]
    print("当前是第{}周周{}".format(date_time[1],list1[date_time[2]]))
    print("校历第{}周.".format(date.isocalendar()[1]-7))
 
if __name__ == '__main__':
    main()

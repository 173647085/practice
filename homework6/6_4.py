# -*- encoding: utf-8 -*-
"""
@File : 6_4.py
@Time : 2020/04/25 15:28:16
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
"""

# here put the import lib
"""
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
"""

class Student:
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score

    def total(self):
        return sum(self.score)

    def average(self):
        return sum(self.score)/3

    def message(self):
        print("学生信息：")
        print("姓名:{}  年龄:{}  性别:{}  分数:{} {} {}".format(self.name,self.age,self.sex,self.score[0],self.score[1],self.score[2]))

stu1=Student("zxl",20,"男",[76,89,84])
print("打印学生信息")
stu1.message()
print("平均分为:{}".format(stu1.average()))
print("总分为:{}".format(stu1.total()))
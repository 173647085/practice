# -*- encoding: utf-8 -*-
'''
@File : 6_2.py
@Time : 2020/04/17 14:47:38
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib
#二 定义一个学生Student类。有下面的类属性：
#1 姓名 name
#2 年龄 age
#3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
#类方法：
#1 获取学生的姓名：get_name() 返回类型:str
#2 获取学生的年龄：get_age() 返回类型:int
#3 返回3门科目中最高的分数。get_course() 返回类型:int
#写好类以后，可以定义2个同学测试下:
class student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_course(self):
        return max(self.score)

stu1=student("张三",18,[89,42,73])
print('姓名：',stu1.get_name())
print(type(stu1.get_name()))
print('年龄：',stu1.get_age())
print(type(stu1.get_age()))
print('最高分：',stu1.get_course())
print(type(stu1.get_course()))

stu2=student("李四",19,[97,83,76])
print("姓名：",stu2.get_name())
print("年龄：",stu2.get_age())
print("最高分：",stu2.get_course())
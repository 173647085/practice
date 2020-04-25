# -*- encoding: utf-8 -*-
'''
@File : 6_6.py
@Time : 2020/04/25 15:40:29
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib
'''
六  用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
'''
import os,sys
class student():
    def __init__(self):
        self.stu_list=[]
        f1=open(r"D:\practice\homework6\6-6.txt",'a+',encoding='utf-8')
        f1.seek(0)
        while 1:
            text=f1.readline()
            if text:
                self.stu_list.append(text.strip().split())
            else:
                break
        f1.close()
    
    def _add(self):
        str1="     "
        list1=input("请输入学生信息(班级,学号,姓名,Python成绩)").split()
        f1=open(r"D:\practice\homework6\6-6.txt",'a+',encoding='utf-8')
        str1=str1.join(list1)
        str1+="\n"
        f1.write(str1)
        f1.close()

    def _del(self):
        id=input('请输入要删除的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                f1=open(r"D:\practice\homework6\6-6.txt",'w',encoding='utf-8')
                del self.stu_list[i]
                for a in self.stu_list:
                    str1="     "
                    str1=str1.join(a)
                    str1+="\n"
                    f1.write(str1)
                print('删除信息成功！')
                f1.close()
                return 
        print('不存在此学号！')

    def _change(self):
        id=input('请输入要修改的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                message=input('请输入修改后的学生信息（班级 学号 姓名 分数）：')
                print(self.stu_list)
                self.stu_list[i]=message.split()
                f1=open(r"D:\practice\homework6\6-6.txt",'w',encoding='utf-8')
                print(self.stu_list)
                for a in self.stu_list:
                    str1="     "
                    str1=str1.join(a)
                    str1+="\n"
                    f1.write(str1)
                f1.close()
                print('修改信息成功！')
                return 
        print('不存在此学号！')

    def _seek(self):
        id=input('请输入要查询的学生的学号：')
        for i,a in enumerate(self.stu_list):
            if id==a[1]:
                print('学生信息如下：')
                str1="     "
                str1=str1.join(a)
                print(str1)
                return 
        print('不存在此学号！')

    def print(self):
        print('学生信息如下(班级、学号、姓名、分数)：')
        for a in self.stu_list:
            str1="     "
            print(str1.join(a))

def mianban():
    os.system('cls')
    while 1:
        os.system('cls')
        print('1.添加学生信息  2.删除学生信息  3.修改学生信息  4.查询学生信息  5.显示学生信息  0.退出')
        choice=int(input('请选择功能:'))
        print(choice)
        if choice>=0 and choice <=5:
            pass
        else:
            print('输入有误！')
            break
        s=student()
        if choice==1:
            s._add()
        elif choice==2:
            s._del()
        elif choice==3:
            s._change()
        elif choice==4:
            s._seek()
        elif choice==5:
            s.print()
        elif choice==0:
            sys.exit()
        os.system('pause')

mianban()
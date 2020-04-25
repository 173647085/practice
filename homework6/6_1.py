# -*- encoding: utf-8 -*-
'''
@File : 6_1.py
@Time : 2020/04/17 14:15:32
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib
#一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#      实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量

class dog():
    list1=[
            {"color":"黑色","num":9,"price":100},
            {"color":"白色","num":5,"price":130},
            {"color":"黄色","num":8,"price":180}
          ]
    def bus(self):
        print("  颜色  数量  价格")
        for i in range(3):
            str1="{}.".format(i+1)+self.list1[i]["color"]+"   "+str(self.list1[i]["num"])+"    "+str(self.list1[i]["price"])
            print(str1)
        while True:
            while True:
                i=input("请输入想要购买的狗的颜色序号:")
                i=int(i)
                if 0<i and i<4:
                    break
                else:
                    print("输入错误")
            self.list1[int(i)-1]["num"]-=1
            p=input("是否继续购买(0/1)")
            if not int(p):
                break
        print("  颜色  数量  价格")
        for i in range(3):
            str1="{}.".format(i+1)+self.list1[i]["color"]+"   "+str(self.list1[i]["num"])+"    "+str(self.list1[i]["price"])
            print(str1)
        

if __name__ == "__main__":
    d=dog()
    d.bus()


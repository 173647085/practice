from dog import dog
from people import people
import random
# -*- encoding: utf-8 -*-
'''
@File : 6_5.py
@Time : 2020/04/17 15:04:30
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib

import time

class fight():
    d=dog()
    p=people()
    def __init__(self):
        i=random.randint(0,2)
        for i in range(i,100):
            time.sleep(0.5)
            if not self.p.fail():
                print("dog胜利")
                break
            elif not self.d.fail():
                print("people胜利")
                break
            elif i%2==1:
                m,m1=self.d.attack()
                x,x1=self.p.behit(m1)
                print("{}攻击了{}".format(m,x1))
                print("{}攻击下降2,生命下降{}".format(x1,m1))
                print(self.p.list1[x])
                if self.p.list1[x]["blo"]==0:
                    print("{}被杀死".format(self.p.list1[x]["name"]))
            elif i%2==0:
                m,m1=self.p.attack()
                x,x1=self.d.behit(m1)
                print("{}攻击了{}".format(m,x1))
                print("{}攻击下降3,生命下降{}".format(x1,m1))
                print(self.d.list1[x])
                if self.d.list1[x]["blo"]==0:
                    print("{}被杀死".format(self.d.list1[x]["name"]))                
f=fight()



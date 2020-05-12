# -*- encoding: utf-8 -*-
'''
@File : 8_4.py
@Time : 2020/04/28 20:12:34
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
'''

# here put the import lib
from multiprocessing import Process, Queue

def sender(q):
    print('开始对话')
    while True:
        msg = input()
        q.put(msg)
        if msg == '88':
            break

def receiver(q):
    while True:
        msg = q.get()
        if msg == '88':
            print('对话结束')
            break
        print('接收:', msg)


if __name__ == '__main__':
    queue = Queue()  # 消息队列
    p = Process(target=receiver, args=(queue,))
    p.start()
    sender(queue)
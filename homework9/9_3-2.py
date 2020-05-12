# -*- encoding: utf-8 -*-
'''
@File : 9_3-2.py
@Time : 2020/05/13 00:31:32
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

# here put the import lib
#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))
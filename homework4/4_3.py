# -*- encoding: utf-8 -*-
'''
@File : 4_3.py
@Time : 2020/04/14 18:24:25
@Author : zxl 
@Version : 1.0
@Contact : 173647085@qq.com
'''

#从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中
# here put the import lib

import base64
f=open(r"D:\practice\4_4.txt","r+")
for i in range(0,5):
    strs=input("请输入5个同学的姓名，账号和密码:")
    strs=strs.split(" ")
    mima=strs[2]
    del strs[2]
    strs.append(str(base64.b64encode(mima.encode('gbk'))))
    strs=" ".join(strs)
    strs+="\n"
    f.write(strs)
    print(strs)
f.close()

# # -*- encoding: utf-8 -*-
# '''
# @File : 5_4.py
# @Time : 2020/04/14 18:45:48
# @Author : zxl 
# @Version : 1.0
# @Contact : 173647085@qq.com
# '''
# #  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
# #      三个目标函数分别为：
# #      A 打印输出20000之内的素数；
# #      B 计算整数2-10000之间的素数的个数；
# #      C 计算整数2-M之间的素数的个数；
# # here put the import lib

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    else:
        return 1

def dec_funcA(func):
    def wrapper():
        func()
    return wrapper

def dec_funcB(func):
    def wrapper():
        return func()
    return wrapper

def dec_funcC(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@dec_funcA
def funcA():
    prime=[]
    for x in range(1,20001):
        if isPrime(x)==1:
            prime.append(x)
    print("20000以内的素数有:",prime)

@dec_funcB
def funcB():
    count = 0
    for x in range(2,10001):
        if isPrime(x) == 1:
            count +=1
    return count

@dec_funcC
def funcC(m):
    count = 0
    for x in range(2,m+1):
        if isPrime(x) == 1:
            print(x)
            count +=1
    print("%d以内的素数有%d个:" %(m,count))

funcA()
print("整数2-10000之间的素数的个数有{}个".format(funcB()))
funcC(100)
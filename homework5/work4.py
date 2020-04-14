# -*- encoding: utf-8 -*-
'''
@File : work4.py
@Time : 2020/04/08 07:57:16
@Author : gwd 
@Version : 1.0
@Contact : 1033876073@qq.com
'''
#  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
# here put the import lib
def func1():
    def isPrime(n):
        for i in range(2,n):
            if n % i == 0:
                return 0
        else:
            return 1
    prime = [x for x in range(2,2001) if isPrime(x) == 1]
    print("2000以内的素数有:",prime)

def func2():
    def isPrime(n):
        for i in range(2,n):
            if n % i == 0:
                return 0
        else:
            return 1
    count = 0
    for x in range(2,2001):
        if isPrime(x) == 1:
            count +=1
    return count

def func3(m):
    def isPrime(n):
        for i in range(2,n):
            if n % i == 0:
                return 0
        else:
            return 1
    count = 0
    for x in range(2,m+1):
        if isPrime(x) == 1:
            count +=1
    print("%d以内的素数有%d个:" %(m,count))

func1()
func2()
func3(100)
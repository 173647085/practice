#6  定义一个函数, 打印输出n以内的斐波那契数列;
def fabs(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
        
n=int(input("请输入n的值:"))
fabs(n)
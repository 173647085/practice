#10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)
def cacluate():
    a,b=eval(input("请输入数字:"))
    print("请选择运算方式:1.+,2.-,3.*,4./")
    c=input()
    if c=="1":
        print("相加的结果是",a+b)
    elif c=="2":
        print("相减的结果是",a-b)
    elif c=="3":
        print("相乘的结果是",a*b)
    elif c=="4":
        print("相除的结果是",a/b)
cacluate()
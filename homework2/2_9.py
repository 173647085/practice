#9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序
def seek(a):
    a.sort()
    print(a)

b=eval(input("请输入数组(以,隔开):"))
seek(list(b))
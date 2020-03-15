#3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
def check():
    count=eval(input("请输入n个数字(以,隔开):"))
    list1=list(count)
    print("奇数有:")
    for i in list1:
        if i%2==1:
            print(i)
check()
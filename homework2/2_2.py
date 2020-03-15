#2 写一个函数，接收n个数字，求这些参数数字的和
def sum(coun):
    sm=0
    for i in coun:
        sm += i
    return sm
count=eval(input("请输入n个数字(以,隔开)"))
print(sum(count))
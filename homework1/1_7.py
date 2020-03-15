#打印输出9*9乘法表，按照下面的格式：
for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={}".format(j,i,i*j),end="  ")
        # print(j,"x",i,"=",i*j,end=" ")
    print()

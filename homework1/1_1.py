#元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
for i in range(0,4):
    if i==0:
        print("0-50之间奇数有:")
        for j in range(0,50):
            if j%2==1:
                print(j,end=" ")
        print()
    elif i==1:
        print("0-50之间偶数有:")
        for j in range(0,50):
            if j%2==0:
                print(j,end=" ")
        print()
    elif i==2:
        print("0-50之间质数有:")
        for j in range(0,50):
            if j > 1:
                for k in range(2,j):
                    if (j % k) == 0:
                        break
                else:
                    print(j,end=" ")
        print()
    else:
        print("0-50之间能同时被2和3整除的有:")
        for j in range(0,50):
            if j%2==0 and j%3==0:
                print(j,end=" ")
                
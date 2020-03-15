#9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
import random
b=int(input("请输入猜的次数:"))
a=random.randint(1,10)
print(a)
for i in range(0,b):
    c=int(input("请输入猜测的数字:"))
    if c==a:
        print("成功！")
        break
else:
    print("失败")
#7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
import random
list1 = [random.randint(0,100) for i in range(20)]
def judge(l):
    for i in l:
        if i>=90:
            print("A")
        elif(i>=80 and i<90):
            print("B")
        elif(i>=60 and i<80):
            print("C")
        elif(i<60):
            print("D")
        
judge(list1)
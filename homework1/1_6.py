#前面2个元素为0，1，输出100以内的斐波那契数列；
f1 = 0
f2 = 1
print(f1)
print(f2)                                
for fi in range(1,101):            
    if fi == f2 + f1:               
        print(fi)
        f1,f2 = f2,fi                    
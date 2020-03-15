#使用random模块，生成随机数，来初始化一个列表，元组；
import random
list1=random.sample(range(1,100),6)
tuple1=tuple(random.sample(range(1,100),6))
print(list1)
print(tuple1)
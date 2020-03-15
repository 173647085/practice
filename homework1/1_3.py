#定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出
list1=[1,1230,412,521,"dsa",512,"dsa31",5151,"vxzcd"]
list2=[521,"deqwfr","vxzcd",41241,"wrasca",2515,15863,"casvaw"]
for i in list1:
    if i in list2:
        print(i,end=" ")
    elif i==list1[len(list1)-1]:
        print("两个列表没有相同元素")
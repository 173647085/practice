#写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
List=[]
def input1():
    while True:
        s = input()
        if not s:
            return List
        List.append(s)
input1()
try:
    f = open(r"D:\text\input.txt","w")
    for x in List:
        print(x)
        f.write(x)
        f.write("\n")
    f.close()
except IOError:
    print("write error;")
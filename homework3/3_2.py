#写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
List = []
def readf():
    try:
        f = open(r"D:\text\input.txt","r")
        while True:
            s = f.readline()
            if not s:
                f.close()
                return List
            s = s.rstrip()
            List.append(s)
    except IOError:
        print("Open Error.")
    else:
        f.close()
list1=["一","二","三","四","五","六","七","八","九","十"]
def printf(L):
    print(L)
    for id,s in enumerate(L):
        print("{}.#第{}行: {}".format(id+1,list1[id],s))

printf(readf())
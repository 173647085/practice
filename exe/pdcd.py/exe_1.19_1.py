def copy(path1,path2):
    f=open(path1,"r")
    f1=open(path2,"a")
    f1.write(f.read())

path1=r"D:\text\a\exe.txt"
path2=r"D:\text\b.txt"
copy(path1,path2)
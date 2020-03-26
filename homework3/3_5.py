f=open(r"D:\practice\Blowing in the wind.txt","w+") #创建文件，准备写入数据。注意打开模式是"w+"，因为我们不仅要写数据，最后还要读数据。
List= ["How many roads must a man walk down",
    "Before they call him a man",
    "How many seas must a white dove sail",
    "Before she sleeps in the sand",
    "How many times must the cannon balls fly",
    "Before they're forever banned",
    "The answer my friend is blowing in the wind",
    "The answer is blowing in the wind"]
str_1="\n"
f.write(str_1.join(List)) #将歌词写入文件
f.seek(0)
L=f.readlines()
L.insert(0,"Blowing in the wind     Bob Dylan\n")
L.append("\n1962 by Warner Bros.Inc.\n")
f.seek(0)
f.writelines(L)
f.seek(0)
for line in f:
    print(line,end="") 
f.close() #最后，关闭文件
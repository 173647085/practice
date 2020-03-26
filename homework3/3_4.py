# 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)将当前img目录所有以.png结尾的后缀名改为.jpg.
import os
# os.mkdir("img")
os.chdir("img")
# for i in range(0,10):
#     os.mkdir("{}.png".format(i+1))
for filename in os.listdir(r"D:\practice\img"):
    name = os.path.splitext(filename)
    if name[1] == ".png":
        newname = name[0] + ".jpg"
        os.rename(filename, newname)
